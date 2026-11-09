"""Compile Gonnyu second-scheme phonology from dictionary IPA and Rime maps."""
from __future__ import annotations

import csv
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .compile import _normalise_pinyin_zero_initial, compile_phonology
from .decomposer import build_decomposer
from .dict_reader import read_dict
from .schema_hints import SchemaHints, extract_hints

SECOND_SCHEME_PREFIX = "konny_"
SECOND_SCHEME_SUFFIX = "_II"
DEFAULT_TABLE = Path(__file__).resolve().parents[2] / "phonology_scheme2.tsv"


@dataclass(frozen=True)
class Scheme2Table:
    initials: dict[str, str]
    vowels: dict[str, str]
    codas: dict[str, str]

    @property
    def coda_keys(self) -> tuple[str, ...]:
        return tuple(sorted(self.codas, key=len, reverse=True))


def is_second_scheme(schema_id: str) -> bool:
    return schema_id.startswith(SECOND_SCHEME_PREFIX)


def base_schema_id(schema_id: str) -> str:
    rest = schema_id.removeprefix(SECOND_SCHEME_PREFIX)
    if rest.endswith(SECOND_SCHEME_SUFFIX):
        rest = rest[: -len(SECOND_SCHEME_SUFFIX)]
    return f"gannyu_{rest}"


def load_table(path: Path = DEFAULT_TABLE) -> Scheme2Table:
    groups: dict[str, dict[str, str]] = {"initial": {}, "vowel": {}, "coda": {}}
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            kind = (row.get("kind") or "").strip()
            ipa = (row.get("ipa") or "").strip()
            spelling = (row.get("spelling") or "").strip()
            if kind in groups and ipa and spelling:
                groups[kind][ipa] = spelling
    return Scheme2Table(
        initials=groups["initial"],
        vowels=groups["vowel"],
        codas=groups["coda"],
    )


def find_spelling_map(
    schema_id: str,
    schema_path: Path,
    sources_root: Path | None,
    download_root: Path | None,
) -> dict[str, str] | None:
    region = base_schema_id(schema_id).removeprefix("gannyu_")
    filename = f"konny_{region}_scheme2.lua"
    candidates = [schema_path.parent / "lua" / filename]
    for root in (sources_root, download_root):
        if root is None:
            continue
        candidates.extend(
            sorted(root.rglob(filename), key=lambda path: (len(path.parts), str(path)))
        )
    for path in candidates:
        if path.is_file():
            return _parse_spelling_map(path)
    return None


def compile_second_scheme(
    schema_id: str,
    display_name: str,
    schema_path: Path,
    dict_path: Path,
    dictionary_name: str,
    repo_root: Path,
    base_overrides: dict[str, Any],
    sources_root: Path | None,
    download_root: Path | None,
    ipa_dictionary: dict[str, Any],
    table_path: Path = DEFAULT_TABLE,
) -> dict[str, Any] | None:
    spellings = find_spelling_map(schema_id, schema_path, sources_root, download_root)
    if not spellings:
        return None
    table = load_table(table_path)
    missing_schema = schema_path.parent / "__missing_schema__.yaml"
    base_hints = extract_hints(missing_schema, list(spellings), base_overrides)
    base_split = build_decomposer(list(spellings), base_hints)

    initials: dict[str, dict[str, Any]] = {}
    finals: dict[str, dict[str, Any]] = {}
    whole = dict(base_hints.whole_syllables)
    zero_initial: set[str] = set()
    matched: set[str] = set()
    rows: list[tuple[str, str]] = []
    unmapped = 0

    for base, second in sorted(spellings.items()):
        normalized = (
            _normalise_pinyin_zero_initial(base, base_hints.zero_initial_rewrites)
            if base_hints.zero_initial_pinyin
            else base
        )
        parts = base_split(normalized)
        if parts is None:
            unmapped += 1
            continue
        initial, final, _ = parts
        match = _match(base_hints, table, initial, final, second)
        if match is None:
            unmapped += 1
            continue
        matched.add(base)
        ii_initial, ii_final, nucleus, coda, initial_variant, final_variant, composed = match
        if ii_initial:
            _add(initials, ii_initial, {
                "ipa": str(initial_variant["ipa"]),
                "place": str(initial_variant["place"]),
                "manner": str(initial_variant["manner"]),
            })
        else:
            zero_initial.add(composed)
        _add(finals, ii_final, {
            "nucleus": nucleus,
            "nucleus_ipa": str(final_variant.get("nucleus_ipa", "")),
            "coda": coda,
            "ipa": str(final_variant["ipa"]),
        })
        if composed != ii_initial + ii_final:
            whole.setdefault(composed, (ii_initial, ii_final))

    prefix = base_hints.code_prefix
    for text, spelling in read_dict(dict_path):
        if prefix:
            if not spelling.startswith(prefix):
                continue
            spelling = spelling[len(prefix):]
        if spelling not in matched:
            continue
        second = spellings.get(spelling)
        if second is not None:
            rows.append((text, second))

    overrides: dict[str, Any] = {
        "tone_encoding": "none",
        "extra_initials": sorted(initials),
        "extra_finals": sorted(finals),
        "initials_ipa": _finish(initials),
        "finals_ipa": _finish(finals),
        "zero_initial_finals": sorted(zero_initial),
        "whole_syllables": whole,
        "require_ipa_overrides": True,
    }
    hints = extract_hints(missing_schema, [spelling for _, spelling in rows], overrides)
    record = compile_phonology(
        schema_id=schema_id,
        display_name=display_name,
        schema_path=schema_path,
        dict_path=dict_path,
        dictionary_name=dictionary_name,
        repo_root=repo_root,
        overrides=overrides,
        ipa_dictionary=ipa_dictionary,
        rows=rows,
        hints=hints,
    )
    if record is not None:
        record["stats"]["second_scheme_unmapped"] = unmapped
    return record


def _match(
    base_hints: SchemaHints,
    table: Scheme2Table,
    initial: str,
    final: str,
    second: str,
) -> tuple[str, str, str, str, dict[str, Any], dict[str, Any], str] | None:
    final_entry = base_hints.finals_ipa.get(final)
    if final_entry is None:
        return None
    if initial:
        initial_variants = _variants(base_hints.initials_ipa.get(initial))
    else:
        initial_variants = [{"ipa": ""}]
    for initial_variant in initial_variants:
        ii_initial = _initial_spelling(str(initial_variant["ipa"]), table)
        if ii_initial is None:
            continue
        for final_variant in _variants(final_entry):
            for ee_e_opposition, oo_o_opposition in ((False, False), (True, False), (False, True), (True, True)):
                parts = _final_parts(
                    str(final_variant["ipa"]),
                    table,
                    ee_e_opposition=ee_e_opposition,
                    oo_o_opposition=oo_o_opposition,
                )
                if parts is None:
                    continue
                ii_final, nucleus, coda = parts
                composed = _compose(ii_initial, ii_final, str(final_variant["ipa"]), table)
                if composed == second:
                    return (
                        ii_initial,
                        ii_final,
                        nucleus,
                        coda,
                        initial_variant,
                        final_variant,
                        composed,
                    )
    return None


def _variants(entry: dict[str, Any] | None) -> list[dict[str, Any]]:
    if not entry:
        return []
    variants = entry.get("variants")
    if isinstance(variants, list) and variants:
        return [variant for variant in variants if isinstance(variant, dict)]
    return [entry]


def _initial_spelling(ipa: str, table: Scheme2Table) -> str | None:
    body = normalize_ipa(ipa).strip()
    if not body:
        return ""
    return table.initials.get(body)


def _final_parts(
    ipa: str,
    table: Scheme2Table,
    *,
    ee_e_opposition: bool = False,
    oo_o_opposition: bool = False,
) -> tuple[str, str, str] | None:
    body = normalize_ipa(ipa).lstrip("~").strip()
    if not body:
        return None
    syllabic = _syllabic_spelling(body)
    if syllabic is not None:
        return syllabic, syllabic, ""
    if body.startswith("ʔ"):
        body = body[1:]
        if not body:
            return None
        syllabic = _syllabic_spelling(body)
        if syllabic is not None:
            return syllabic, syllabic, ""

    decomposed = unicodedata.normalize("NFD", body)
    nasalized = "\u0303" in decomposed
    body = unicodedata.normalize("NFC", decomposed.replace("\u0303", ""))

    coda_ipa = ""
    for candidate in table.coda_keys:
        if body.endswith(candidate) and len(body) > len(candidate):
            coda_ipa = candidate
            body = body[: -len(candidate)]
            break

    nucleus: list[str] = []
    for char in body:
        if char == "ɛ" and not ee_e_opposition:
            spelling = "e"
        elif char == "ɔ" and not oo_o_opposition:
            spelling = "o"
        else:
            spelling = table.vowels.get(char)
        if spelling is None:
            return None
        nucleus.append(spelling)
    nucleus_spelling = "".join(nucleus)
    coda_spelling = table.codas.get(coda_ipa, "")
    nasal = "nn" if nasalized and coda_ipa not in {"n", "ng", "m"} else ""
    return nucleus_spelling + nasal + coda_spelling, nucleus_spelling, coda_spelling


def _compose(initial: str, final: str, final_ipa: str, table: Scheme2Table) -> str:
    body = normalize_ipa(final_ipa)
    for coda in table.coda_keys:
        if body.endswith(coda) and len(body) > len(coda):
            body = body[: -len(coda)]
            break
    if initial.endswith("j") and len(body) > 1 and body.startswith("i"):
        final = final[1:]
    return initial + final


def _syllabic_spelling(body: str) -> str | None:
    normalized = unicodedata.normalize("NFD", body)
    if normalized.startswith("ɭ") and normalized[1:] in {"\u0329", ""}:
        return "l"
    match = re.fullmatch(r"([mnŋ])(?:\u0329|\u030d)?", normalized)
    if not match:
        return None
    return {"m": "m", "n": "n", "ŋ": "ng"}[match.group(1)]


def normalize_ipa(value: str) -> str:
    return (
        unicodedata.normalize("NFC", value)
        .replace("Ǿ", "")
        .replace("ʨ", "tɕ")
        .replace("α", "ɑ")
        .replace("I", "i")
        .replace("ʊ", "u")
        .replace("ᴀ", "a")
        .replace("ᴇ", "e")
        .replace("ː", "")
        .replace("ts'", "tsʰ")
        .replace("tɕ'", "tɕʰ")
        .replace("p'", "pʰ")
        .replace("t'", "tʰ")
        .replace("k'", "kʰ")
    )


def _add(store: dict[str, dict[str, Any]], key: str, entry: dict[str, Any]) -> None:
    bucket = store.setdefault(key, {"items": [], "seen": set()})
    signature = tuple(sorted(entry.items()))
    if signature in bucket["seen"]:
        return
    bucket["seen"].add(signature)
    bucket["items"].append(entry)


def _finish(store: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for key, bucket in store.items():
        items = bucket["items"]
        if not items:
            continue
        entry = dict(items[0])
        if len(items) > 1:
            entry["variants"] = [dict(item) for item in items]
        result[key] = entry
    return result


def _parse_spelling_map(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    start = text.find("spellings")
    if start == -1:
        return {}
    brace = text.find("{", start)
    if brace == -1:
        return {}
    end = _matching_brace(text, brace)
    block = text[brace + 1:end]
    return {
        match.group(1): match.group(2)
        for match in re.finditer(r'\["([^"]*)"\]\s*=\s*"([^"]*)"', block)
    }


def _matching_brace(text: str, start: int) -> int:
    depth = 0
    for index in range(start, len(text)):
        char = text[index]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index
    return len(text)
