"""Classify generated romanization inventories into broad IPA grid cells."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

from .schema_hints import SchemaHints


def load_ipa_dictionary(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    required = {"places", "manners", "initials_default", "nuclei_default", "codas", "finals_default"}
    missing = required - set(data)
    if missing:
        raise ValueError(f"IPA dictionary missing keys: {', '.join(sorted(missing))}")
    return data


def classify_initial(
    spelling: str,
    hints: SchemaHints,
    dictionary: dict[str, Any],
) -> dict[str, str] | None:
    key = spelling.lower()
    entry = _merged_entry(dictionary.get("initials_default", {}).get(key), hints.initials_ipa.get(key))
    if not entry:
        return None
    if not {"ipa", "place", "manner"} <= set(entry):
        return None
    return {
        "ipa": str(entry["ipa"]),
        "place": str(entry["place"]),
        "manner": str(entry["manner"]),
    }


def split_final(spelling: str, dictionary: dict[str, Any]) -> tuple[str, str]:
    spelling = spelling.lower()
    codas = [
        str(coda.get("suffix", ""))
        for coda in dictionary.get("codas", [])
        if coda.get("suffix", "") != ""
    ]
    for coda in sorted(codas, key=len, reverse=True):
        if spelling.endswith(coda) and len(spelling) > len(coda):
            return spelling[: -len(coda)], coda
    return spelling, ""


def classify_final(
    spelling: str,
    hints: SchemaHints,
    dictionary: dict[str, Any],
) -> dict[str, str] | None:
    key = spelling.lower()
    exact = _merged_entry(dictionary.get("finals_default", {}).get(key), hints.finals_ipa.get(key))
    if exact:
        nucleus = str(exact.get("nucleus", ""))
        coda = str(exact.get("coda", ""))
        nucleus_entry = _nucleus_entry(nucleus, hints, dictionary)
        coda_entry = _coda_entry(coda, dictionary)
        nucleus_ipa = str(exact.get("nucleus_ipa") or (nucleus_entry or {}).get("ipa", ""))
        if not nucleus or coda_entry is None:
            return None
        return {
            "nucleus": nucleus,
            "nucleus_ipa": nucleus_ipa,
            "coda": coda,
            "coda_label": str(coda_entry.get("label", "")),
            "ipa": str(exact.get("ipa") or f"{nucleus_ipa}{coda_entry.get('ipa', '')}"),
            "row_key": _final_row_key(nucleus, nucleus_ipa, hints, dictionary),
        }

    nucleus, coda = split_final(key, dictionary)
    nucleus_entry = _nucleus_entry(nucleus, hints, dictionary)
    coda_entry = _coda_entry(coda, dictionary)
    if not nucleus_entry or coda_entry is None:
        return None
    nucleus_ipa = str(nucleus_entry.get("ipa", ""))
    return {
        "nucleus": nucleus,
        "nucleus_ipa": nucleus_ipa,
        "coda": coda,
        "coda_label": str(coda_entry.get("label", "")),
        "ipa": f"{nucleus_ipa}{coda_entry.get('ipa', '')}",
        "row_key": nucleus,
    }


def compile_initials_grid(
    initials: list[dict[str, Any]],
    hints: SchemaHints,
    dictionary: dict[str, Any],
) -> dict[str, Any]:
    cells: dict[str, dict[str, list[dict[str, Any]]]] = {}
    used_manners: set[str] = set()
    used_places: set[str] = set()
    uncategorised: list[dict[str, Any]] = []
    total = 0
    categorised = 0

    for row in initials:
        spelling = str(row.get("spelling", ""))
        if spelling == "":
            continue
        total += 1
        classification = classify_initial(spelling, hints, dictionary)
        if not classification:
            uncategorised.append(_uncategorised_entry(row))
            continue

        manner = classification["manner"]
        place = classification["place"]
        used_manners.add(manner)
        used_places.add(place)
        categorised += 1
        cells.setdefault(manner, {}).setdefault(place, []).append(_grid_entry(row, classification["ipa"]))

    rows = _ordered_subset(dictionary.get("manners", {}), used_manners)
    cols = _ordered_subset(dictionary.get("places", {}), used_places)
    _sort_cell_entries(cells)
    return {
        "rows": rows,
        "cols": cols,
        "row_labels": {key: dictionary["manners"][key] for key in rows},
        "col_labels": {key: dictionary["places"][key] for key in cols},
        "cells": cells,
        "uncategorised": uncategorised,
        "coverage": _coverage(categorised, total),
    }


def compile_finals_grid(
    finals: list[dict[str, Any]],
    hints: SchemaHints,
    dictionary: dict[str, Any],
) -> dict[str, Any]:
    cells: dict[str, list[dict[str, Any]]] = {}
    used_rows: dict[str, dict[str, str]] = {}
    uncategorised: list[dict[str, Any]] = []
    total = 0
    categorised = 0

    for row in finals:
        spelling = str(row.get("spelling", ""))
        if spelling == "":
            continue
        total += 1
        classification = classify_final(spelling, hints, dictionary)
        if not classification:
            uncategorised.append(_uncategorised_entry(row))
            continue

        categorised += 1
        row_key = classification["row_key"]
        nucleus = classification["nucleus"]
        coda = classification["coda"]
        used_rows.setdefault(
            row_key,
            {
                "key": row_key,
                "nucleus": nucleus,
                "label": str((_nucleus_entry(nucleus, hints, dictionary) or {}).get("label", nucleus)),
                "ipa": classification["nucleus_ipa"],
            },
        )
        cells.setdefault(f"{row_key}|{coda}", []).append(_grid_entry(row, classification["ipa"]))

    row_order = list(dictionary.get("nuclei_default", {}).keys())
    rows = sorted(used_rows.values(), key=lambda row: _row_order_key(row_order, row))
    cols = deepcopy(dictionary.get("codas", []))
    for entries in cells.values():
        entries.sort(key=lambda entry: entry["spelling"])
    return {
        "rows": rows,
        "cols": cols,
        "cells": cells,
        "uncategorised": uncategorised,
        "coverage": _coverage(categorised, total),
    }


def _nucleus_entry(
    nucleus: str,
    hints: SchemaHints,
    dictionary: dict[str, Any],
) -> dict[str, Any] | None:
    return _merged_entry(dictionary.get("nuclei_default", {}).get(nucleus), hints.nuclei_ipa.get(nucleus))


def _coda_entry(coda: str, dictionary: dict[str, Any]) -> dict[str, Any] | None:
    for entry in dictionary.get("codas", []):
        if str(entry.get("suffix", "")) == coda:
            return entry
    return None


def _final_row_key(
    nucleus: str,
    nucleus_ipa: str,
    hints: SchemaHints,
    dictionary: dict[str, Any],
) -> str:
    default_ipa = str((_nucleus_entry(nucleus, hints, dictionary) or {}).get("ipa", ""))
    if nucleus_ipa and default_ipa and nucleus_ipa != default_ipa:
        return f"{nucleus}:{nucleus_ipa}"
    return nucleus


def _merged_entry(default: Any, override: Any) -> dict[str, Any] | None:
    if default is None and override is None:
        return None
    merged: dict[str, Any] = {}
    if isinstance(default, dict):
        merged.update(default)
    if isinstance(override, dict):
        merged.update(override)
    return merged


def _grid_entry(row: dict[str, Any], ipa: str) -> dict[str, Any]:
    return {
        "spelling": str(row.get("spelling", "")),
        "ipa": ipa,
        "examples": list(row.get("example_chars", []))[:3],
        "syllable_count": int(row.get("syllable_count", 0)),
        "char_count": int(row.get("char_count", 0)),
    }


def _uncategorised_entry(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "spelling": str(row.get("spelling", "")),
        "examples": list(row.get("example_chars", []))[:3],
        "syllable_count": int(row.get("syllable_count", 0)),
        "char_count": int(row.get("char_count", 0)),
    }


def _ordered_subset(labels: dict[str, str], used: set[str]) -> list[str]:
    ordered = [key for key in labels if key in used]
    return ordered + sorted(used - set(labels))


def _sort_cell_entries(cells: dict[str, dict[str, list[dict[str, Any]]]]) -> None:
    for by_place in cells.values():
        for entries in by_place.values():
            entries.sort(key=lambda entry: entry["spelling"])


def _coverage(categorised: int, total: int) -> dict[str, int | float]:
    return {
        "categorised": categorised,
        "total": total,
        "ratio": 1 if total == 0 else categorised / total,
    }


def _order_index(order: list[str], value: str) -> tuple[int, str]:
    try:
        return (order.index(value), value)
    except ValueError:
        return (len(order), value)


def _row_order_key(order: list[str], row: dict[str, str]) -> tuple[int, str, str]:
    base_index, _ = _order_index(order, row["nucleus"])
    default_variant = 0 if row["key"] == row["nucleus"] else 1
    return (base_index, str(default_variant), row["ipa"])
