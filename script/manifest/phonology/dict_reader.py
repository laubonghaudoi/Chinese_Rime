"""Parse the table portion of a Rime *.dict.yaml file."""
from __future__ import annotations

from pathlib import Path


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
        spelling = parts[1].strip()
        if text_value and spelling:
            rows.append((text_value, spelling))
    return rows
