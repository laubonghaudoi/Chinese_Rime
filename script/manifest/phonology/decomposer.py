"""Split romanized spellings into best-effort initial/final/tone triples."""
from __future__ import annotations

import unicodedata
from collections import Counter
from typing import Callable

from .schema_hints import SchemaHints

VOWELS = set("aeiouAEIOU")
CONSONANTS = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
TONE_CONTOURS = set("˥˦˧˨˩")


def build_decomposer(
    spellings: list[str],
    hints: SchemaHints,
) -> Callable[[str], tuple[str, str, str | None] | None]:
    toneless_pairs = [_strip_tone(spelling, hints) for spelling in spellings]
    toneless = [spelling for spelling, _ in toneless_pairs]
    initials = _empirical_initials(toneless) | hints.recognized_initials
    initials_sorted = sorted(initials, key=len, reverse=True)
    recognized_initials = {initial.lower() for initial in hints.recognized_initials}
    recognized_finals = {final.lower() for final in hints.recognized_finals}

    def split(spelling: str) -> tuple[str, str, str | None] | None:
        base, tone = _strip_tone(spelling, hints)
        matches: list[tuple[int, int, int, str, str]] = []
        for initial in initials_sorted:
            lower = base.lower()
            if initial and lower.startswith(initial):
                final = base[len(initial):]
                matches.append(_candidate_score(initial, final, recognized_initials, recognized_finals) + (initial, final))
        if matches:
            _, _, _, initial, final = max(matches)
            return initial, final, tone
        if base and base[0] in VOWELS:
            return "", base, tone
        return None

    return split


def _strip_tone(spelling: str, hints: SchemaHints) -> tuple[str, str | None]:
    if hints.tone_encoding == "digits":
        tone = "".join(char for char in spelling if char.isdigit())
        if tone:
            return "".join(char for char in spelling if not char.isdigit()), tone
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
    if hints.tone_encoding == "contours":
        tone = ""
        index = len(spelling)
        while index > 0 and spelling[index - 1] in TONE_CONTOURS:
            index -= 1
            tone = spelling[index] + tone
        if tone:
            return spelling[:index], tone
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


def _candidate_score(
    initial: str,
    final: str,
    recognized_initials: set[str],
    recognized_finals: set[str],
) -> tuple[int, int, int]:
    lower_final = final.lower()
    exact_final = 1 if lower_final in recognized_finals else 0
    recognized_initial = 1 if initial.lower() in recognized_initials else 0
    # Prefer a known final and known initial over the longest consonant prefix.
    # When both sides are known, keep the longer final: j+yu beats jy+u.
    return (exact_final, recognized_initial, len(final))
