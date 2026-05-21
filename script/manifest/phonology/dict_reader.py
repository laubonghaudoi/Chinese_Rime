"""Parse the table portion of a Rime *.dict.yaml file."""
from __future__ import annotations

from pathlib import Path

COMMENT_MARKERS = ("||", "◎")


def read_dict(path: Path) -> list[tuple[str, str]]:
    """Return ``[(text, spelling), ...]`` rows in dictionary order."""
    if not path.exists():
        return []

    text = path.read_text(encoding="utf-8")
    marker = "\n...\n"
    if marker in text:
        body = text.split(marker, 1)[1]
    elif text.startswith("...\n"):
        body = text[4:]
    else:
        body = text

    rows: list[tuple[str, str]] = []
    for line in body.splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        text_value = parts[0].strip()
        spelling = _normalise_spelling(parts[1])
        if text_value and spelling:
            rows.append((text_value, spelling))
    return rows


def _normalise_spelling(value: str) -> str:
    spelling = value.strip()
    for marker in COMMENT_MARKERS:
        spelling = spelling.split(marker, 1)[0].strip()
    # Some dictionaries append Cyrillic Pe as an internal annotation after the code.
    return spelling.replace("П", "").strip()
