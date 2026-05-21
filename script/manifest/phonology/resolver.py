"""Resolve manifest schema ids to their schema and dictionary files."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TypeAlias

import yaml


@dataclass(frozen=True)
class ResolvedSource:
    schema_id: str
    schema_path: Path
    dict_path: Path
    dictionary_name: str


@dataclass(frozen=True)
class SkippedSource:
    schema_id: str
    reason: str


Resolution: TypeAlias = ResolvedSource | SkippedSource


def resolve_schema_source(schema_id: str, sources_root: Path, download_root: Path) -> Resolution:
    schema_path = _find_schema(schema_id, sources_root, download_root)
    if schema_path is None:
        return SkippedSource(schema_id=schema_id, reason="missing_schema_file")

    data = _read_yaml(schema_path)
    translator = data.get("translator") or {}
    dictionary_name = translator.get("dictionary") if isinstance(translator, dict) else None
    if not dictionary_name:
        return SkippedSource(schema_id=schema_id, reason="missing_dictionary_ref")

    dict_path = _find_dict(str(dictionary_name), schema_path, sources_root, download_root)
    if dict_path is None:
        return SkippedSource(schema_id=schema_id, reason="missing_dict_file")

    return ResolvedSource(
        schema_id=schema_id,
        schema_path=schema_path,
        dict_path=dict_path,
        dictionary_name=str(dictionary_name),
    )


def _find_schema(schema_id: str, sources_root: Path, download_root: Path) -> Path | None:
    filename = f"{schema_id}.schema.yaml"
    for root in (sources_root, download_root):
        matches = sorted(root.rglob(filename), key=lambda path: (len(path.parts), str(path)))
        if matches:
            return matches[0]
    return None


def _find_dict(dictionary_name: str, schema_path: Path, sources_root: Path, download_root: Path) -> Path | None:
    filename = f"{dictionary_name}.dict.yaml"
    same_dir = schema_path.parent / filename
    if same_dir.exists():
        return same_dir
    for root in (sources_root, download_root):
        matches = sorted(root.rglob(filename), key=lambda path: (len(path.parts), str(path)))
        if matches:
            return matches[0]
    return None


def _read_yaml(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8").replace("\t", " ")
    return yaml.safe_load(raw) or {}
