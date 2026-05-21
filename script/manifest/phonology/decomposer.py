"""Split romanized spellings into best-effort initial/final/tone triples."""
from __future__ import annotations

import unicodedata
from collections import Counter
from typing import Callable

from .schema_hints import SchemaHints

VOWELS = set("aeiouAEIOU")
CONSONANTS = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")


def build_decomposer(
    spellings: list[str],
    hints: SchemaHints,
) -> Callable[[str], tuple[str, str, str | None] | None]:
    toneless_pairs = [_strip_tone(spelling, hints) for spelling in spellings]
    toneless = [spelling for spelling, _ in toneless_pairs]
    initials = _empirical_initials(toneless) | hints.recognized_initials
    initials_sorted = sorted(initials, key=len, reverse=True)

    def split(spelling: str) -> tuple[str, str, str | None] | None:
        base, tone = _strip_tone(spelling, hints)
        for initial in initials_sorted:
            if initial and base.lower().startswith(initial):
                return initial, base[len(initial):], tone
        if base and base[0] in VOWELS:
            return "", base, tone
        return None

    return split


def _strip_tone(spelling: str, hints: SchemaHints) -> tuple[str, str | None]:
    if hints.tone_encoding == "digits":
        if spelling and spelling[-1].isdigit():
            return spelling[:-1], spelling[-1]
        return spelling, None
    if hints.tone_encoding == "diacritics":
        normalized = unicodedata.normalize("NFD", spelling)
        base = "".join(char for char in normalized if not unicodedata.combining(char))
        marks = "".join(char for char in normalized if unicodedata.combining(char))
        return unicodedata.normalize("NFC", base), marks or None
    if hints.tone_encoding == "letters":
        if spelling and spelling[-1].lower() in hints.tone_letters:
            return spelling[:-1], spelling[-1].lower()
        return spelling, None
    return spelling, None


def _empirical_initials(toneless_spellings: list[str]) -> set[str]:
    candidates: Counter[str] = Counter()
    for spelling in toneless_spellings:
        prefix = ""
        for char in spelling:
            if char in CONSONANTS:
                prefix += char.lower()
            else:
                break
        candidates[prefix] += 1
    return {
        prefix
        for prefix, count in candidates.items()
        if count >= 2 or len(prefix) <= 1
    }
