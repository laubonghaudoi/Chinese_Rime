"""Infer advisory phonology hints from a Rime schema file."""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class SchemaHints:
    tone_encoding: str = "none"
    tone_letters: set[str] = field(default_factory=set)
    recognized_initials: set[str] = field(default_factory=set)
    recognized_finals: set[str] = field(default_factory=set)
    alphabet: str = ""


_INITIAL_ALGEBRA = re.compile(r"^\s*(?:derive|abbrev|fuzz|xform)/\^([a-zA-Z]+)")
_FINAL_ALGEBRA = re.compile(r"^\s*(?:derive|abbrev|fuzz|xform)/.+?([a-zA-Z]+)\$/")


def extract_hints(
    path: Path,
    sample_spellings: list[str],
    overrides: dict | None = None,
) -> SchemaHints:
    """Return best-effort hints from schema YAML plus explicit overrides."""
    overrides = overrides or {}
    if not path.exists():
        return _apply_overrides(SchemaHints(), overrides)

    data = yaml.safe_load(path.read_text(encoding="utf-8").replace("\t", " ")) or {}
    speller = data.get("speller") or {}
    alphabet = speller.get("alphabet", "") or ""
    algebra = speller.get("algebra", []) or []

    hints = SchemaHints(alphabet=alphabet)
    hints.tone_encoding = _sniff_tone_encoding(alphabet, sample_spellings)

    for rule in algebra:
        if not isinstance(rule, str):
            continue
        initial = _INITIAL_ALGEBRA.match(rule)
        if initial:
            hints.recognized_initials.add(initial.group(1).lower())
        final = _FINAL_ALGEBRA.match(rule)
        if final:
            hints.recognized_finals.add(final.group(1).lower())

    return _apply_overrides(hints, overrides)


def _apply_overrides(hints: SchemaHints, overrides: dict) -> SchemaHints:
    if "tone_encoding" in overrides:
        hints.tone_encoding = str(overrides["tone_encoding"])
    hints.tone_letters.update(str(value).lower() for value in overrides.get("tone_letters", []))
    hints.recognized_initials.update(str(value).lower() for value in overrides.get("extra_initials", []))
    hints.recognized_finals.update(str(value).lower() for value in overrides.get("extra_finals", []))
    return hints


def _sniff_tone_encoding(alphabet: str, sample_spellings: list[str]) -> str:
    digits_in_alphabet = any(char.isdigit() for char in alphabet)
    digits_at_end = any(spelling and spelling[-1].isdigit() for spelling in sample_spellings)
    if digits_at_end and (digits_in_alphabet or alphabet == ""):
        return "digits"
    if any(_has_diacritic(spelling) for spelling in sample_spellings):
        return "diacritics"
    return "none"


def _has_diacritic(value: str) -> bool:
    return any(unicodedata.combining(char) for char in unicodedata.normalize("NFD", value))
