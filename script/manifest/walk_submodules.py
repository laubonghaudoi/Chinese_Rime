"""Walk a sources/ tree and parse every *.schema.yaml file into normalized dicts."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

import yaml


def walk_submodules(sources_dir: Path) -> list[dict]:
    """Return one normalized dict per *.schema.yaml under sources_dir.

    The shape of each dict:
        {
          "schema_id": str,
          "display_name": str,                  # from schema.name
          "version": str,
          "authors": list[str],                 # emails stripped
          "description": str,                   # trailing whitespace stripped
          "dependencies": list[str],
        }
    """
    return [_load_one(p) for p in _iter_schema_yamls(sources_dir)]


def _iter_schema_yamls(root: Path) -> Iterable[Path]:
    yield from sorted(root.rglob("*.schema.yaml"))


def _load_one(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    schema = data.get("schema") or {}

    return {
        "schema_id": schema["schema_id"],
        "display_name": schema.get("name", schema["schema_id"]),
        "version": str(schema.get("version", "")),
        "authors": _normalize_authors(schema.get("author") or []),
        "description": (schema.get("description") or "").strip(),
        "dependencies": list(schema.get("dependencies") or []),
    }


def _normalize_authors(raw: list) -> list[str]:
    """Strip "<email>" suffixes and surrounding whitespace from each entry."""
    out: list[str] = []
    for entry in raw:
        if not isinstance(entry, str):
            continue
        name = entry.split("<", 1)[0].strip()
        if name:
            out.append(name)
    return out
