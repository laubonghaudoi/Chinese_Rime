"""Walk a sources/ tree and parse every *.schema.yaml file into normalized dicts."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

import yaml


HELPER_SCHEMA_DIRS = {"ext-dict"}


def walk_submodules(sources_dir: Path) -> list[dict]:
    """Return one normalized dict per unique schema_id under sources_dir.

    The shape of each dict:
        {
          "schema_id": str,
          "display_name": str,                  # from schema.name
          "version": str,
          "authors": list[str],                 # emails stripped
          "description": str,                   # trailing whitespace stripped
          "dependencies": list[str],
        }

    When the same schema_id is defined at two paths (e.g. a recipe ships
    both a primary file at sources/<lang>/<recipe>/foo.schema.yaml AND a
    mobile-keyboard variant at .../mobile/foo.schema.yaml), the shallower
    path wins and the deeper one is skipped.
    """
    seen: dict[str, dict] = {}
    for path in _iter_schema_yamls(sources_dir):
        entry = _load_one(path)
        seen.setdefault(entry["schema_id"], entry)
    return list(seen.values())


def _iter_schema_yamls(root: Path) -> Iterable[Path]:
    # Walk recursively but emit shallower paths first so the de-dup in
    # walk_submodules keeps the primary file rather than a nested variant.
    schema_paths = (
        path
        for path in root.rglob("*.schema.yaml")
        if not _is_helper_schema(path.relative_to(root))
    )
    yield from sorted(schema_paths, key=lambda p: (len(p.parts), str(p)))


def _is_helper_schema(relative_path: Path) -> bool:
    return any(part in HELPER_SCHEMA_DIRS for part in relative_path.parts[:-1])


def _load_one(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    # Some upstream schema files use tabs in places pyyaml's strict scanner
    # rejects: trailing after a quoted value, or aligning an inline #comment.
    # YAML forbids tabs as indentation, so any tab here is post-content and
    # safe to convert to a single space.
    cleaned = raw.replace("\t", " ")
    data = yaml.safe_load(cleaned) or {}
    schema = data.get("schema") or {}

    return {
        "schema_id": schema["schema_id"],
        "source_group": _source_group(path),
        "display_name": schema.get("name", schema["schema_id"]),
        "version": str(schema.get("version", "")),
        "authors": _normalize_authors(schema.get("author") or []),
        "description": _normalize_description(schema.get("description")),
        "dependencies": list(schema.get("dependencies") or []),
    }


def _source_group(path: Path) -> str:
    parts = path.parts
    try:
        return parts[parts.index("sources") + 1]
    except (ValueError, IndexError):
        return ""


def _normalize_description(raw) -> str:
    """Some upstream schemas write description as a list of lines; join them."""
    if raw is None:
        return ""
    if isinstance(raw, list):
        return "\n".join(str(line).rstrip() for line in raw).strip()
    return str(raw).strip()


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
