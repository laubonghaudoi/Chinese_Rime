"""Compile schema and dictionary files into phonology JSON payloads."""
from __future__ import annotations

import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from .decomposer import build_decomposer
from .dict_reader import read_dict
from .ipa_classify import compile_finals_grid, compile_initials_grid, load_ipa_dictionary
from .schema_hints import extract_hints

SUMMARY_INITIAL_LIMIT = 80
SUMMARY_FINAL_LIMIT = 160
SUMMARY_PREVIEW_LIMIT = 200
GRID_COVERAGE_THRESHOLD = 0.5


def compile_phonology(
    schema_id: str,
    display_name: str,
    schema_path: Path,
    dict_path: Path,
    dictionary_name: str,
    repo_root: Path,
    overrides: dict | None = None,
    ipa_dictionary: dict[str, Any] | None = None,
    ipa_dictionary_path: Path | None = None,
) -> dict[str, Any] | None:
    rows = [
        (char, spelling)
        for char, spelling in read_dict(dict_path)
        if len(char) == 1 and not _is_multi_token_spelling(spelling)
    ]
    if not rows:
        return None

    if ipa_dictionary is None and ipa_dictionary_path is not None:
        ipa_dictionary = load_ipa_dictionary(ipa_dictionary_path)

    spellings = [spelling for _, spelling in rows]
    hints = extract_hints(schema_path, sample_spellings=spellings, overrides=overrides)
    if ipa_dictionary is not None:
        hints.recognized_initials.update(str(key).lower() for key in ipa_dictionary.get("initials_default", {}))
        hints.recognized_finals.update(str(key).lower() for key in ipa_dictionary.get("nuclei_default", {}))
        hints.recognized_finals.update(str(key).lower() for key in ipa_dictionary.get("finals_default", {}))
    split = build_decomposer(sorted(set(spellings)), hints)

    char_spellings: dict[str, list[str]] = defaultdict(list)
    char_spelling_seen: dict[str, set[str]] = defaultdict(set)
    initial_buckets: dict[str, _Bucket] = defaultdict(_Bucket)
    final_buckets: dict[str, _Bucket] = defaultdict(_Bucket)
    tone_buckets: dict[str, _Bucket] = defaultdict(_Bucket)
    undecomposable: set[str] = set()

    for char, spelling in rows:
        if spelling not in char_spelling_seen[char]:
            char_spellings[char].append(spelling)
            char_spelling_seen[char].add(spelling)

        parts = split(spelling)
        if parts is None:
            undecomposable.add(spelling)
            continue
        initial, final, tone = parts
        initial_buckets[initial].add(spelling, char)
        final_buckets[final].add(spelling, char)
        if tone:
            tone_buckets[tone].add(spelling, char)

    syllable_index = [
        {"char": char, "spellings": spellings}
        for char, spellings in sorted(char_spellings.items(), key=lambda item: item[0])
    ]

    initial_rows = _rows_from_buckets(initial_buckets)
    final_rows = _rows_from_buckets(final_buckets)
    record: dict[str, Any] = {
        "schema_id": schema_id,
        "display_name": display_name,
        "dictionary": dictionary_name,
        "source_paths": {
            "schema": _relative_posix(schema_path, repo_root),
            "dict": _relative_posix(dict_path, repo_root),
        },
        "tone_encoding": hints.tone_encoding,
        "initials": initial_rows,
        "finals": final_rows,
        "tones": _tones_from_buckets(tone_buckets),
        "preview_syllables": syllable_index[:SUMMARY_PREVIEW_LIMIT],
        "syllable_index": syllable_index,
        "stats": {
            "total_chars": len(char_spellings),
            "total_syllables": len(set(spellings)),
            "single_char_rows": len(rows),
            "undecomposable_syllables": len(undecomposable),
        },
        "status": "ok" if initial_buckets or final_buckets else "partial",
        "grid_status": "no_grids",
    }
    _attach_grids(record, initial_rows, final_rows, hints, ipa_dictionary)
    return record


def summary_entry(
    record: dict[str, Any],
    asset_path: str,
    initial_limit: int = SUMMARY_INITIAL_LIMIT,
    final_limit: int = SUMMARY_FINAL_LIMIT,
    preview_limit: int = SUMMARY_PREVIEW_LIMIT,
) -> dict[str, Any]:
    entry = {
        "schema_id": record["schema_id"],
        "display_name": record["display_name"],
        "asset_path": asset_path,
        "tone_encoding": record["tone_encoding"],
        "initials": record["initials"][:initial_limit],
        "finals": record["finals"][:final_limit],
        "tones": record["tones"],
        "preview_syllables": record["syllable_index"][:preview_limit],
        "stats": record["stats"],
        "status": record["status"],
        "grid_status": record["grid_status"],
    }
    if "initials_grid" in record:
        entry["initials_grid"] = record["initials_grid"]
    if "finals_grid" in record:
        entry["finals_grid"] = record["finals_grid"]
    return entry


class _Bucket:
    def __init__(self) -> None:
        self.spellings: set[str] = set()
        self.chars: Counter[str] = Counter()

    def add(self, spelling: str, char: str) -> None:
        self.spellings.add(spelling)
        self.chars[char] += 1


def _rows_from_buckets(buckets: dict[str, _Bucket]) -> list[dict[str, Any]]:
    rows = [
        {
            "spelling": spelling,
            "example_chars": _example_chars(bucket),
            "syllable_count": len(bucket.spellings),
            "char_count": sum(bucket.chars.values()),
        }
        for spelling, bucket in buckets.items()
    ]
    return sorted(rows, key=lambda row: (-row["syllable_count"], row["spelling"]))


def _tones_from_buckets(buckets: dict[str, _Bucket]) -> list[dict[str, Any]]:
    rows = [
        {
            "value": tone,
            "example_chars": _example_chars(bucket),
            "syllable_count": len(bucket.spellings),
            "char_count": sum(bucket.chars.values()),
        }
        for tone, bucket in buckets.items()
    ]
    return sorted(rows, key=lambda row: _tone_sort_key(row["value"]))


def _example_chars(bucket: _Bucket) -> list[str]:
    return [
        char
        for char, _ in sorted(bucket.chars.items(), key=lambda item: (-item[1], item[0]))[:5]
    ]


def _tone_sort_key(value: str) -> tuple[int, int | str]:
    if value.isdigit():
        number = 0
        for char in value:
            number = (number * 10) + unicodedata.digit(char)
        return (0, number)
    return (1, value)


def _relative_posix(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def _is_multi_token_spelling(spelling: str) -> bool:
    return any(char.isspace() for char in spelling.strip())


def _attach_grids(
    record: dict[str, Any],
    initials: list[dict[str, Any]],
    finals: list[dict[str, Any]],
    hints: Any,
    ipa_dictionary: dict[str, Any] | None,
) -> None:
    if ipa_dictionary is None or hints.suppress_grids:
        return

    initials_grid = compile_initials_grid(initials, hints, ipa_dictionary)
    finals_grid = compile_finals_grid(finals, hints, ipa_dictionary)
    initial_ratio = float(initials_grid["coverage"]["ratio"])
    final_ratio = float(finals_grid["coverage"]["ratio"])
    record["stats"]["initial_grid_coverage"] = initials_grid["coverage"]
    record["stats"]["final_grid_coverage"] = finals_grid["coverage"]

    if initial_ratio < GRID_COVERAGE_THRESHOLD or final_ratio < GRID_COVERAGE_THRESHOLD:
        return

    record["grid_status"] = "ok"
    record["initials_grid"] = initials_grid
    record["finals_grid"] = finals_grid
