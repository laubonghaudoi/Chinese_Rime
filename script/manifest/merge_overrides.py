"""Merge manifest_overrides.yaml — attach per-schema assignments and emit branches."""
from __future__ import annotations

from pathlib import Path

import yaml


def merge_overrides(schemas: list[dict], overrides_path: Path) -> tuple[list[dict], list[dict]]:
    """Return (schemas_with_assignments, branches).

    `schemas_with_assignments` is the input list of schemas with each entry
    augmented by the fields in `schema_assignments.<schema_id>` from the
    overrides file: branch, dialect, recipe, upstream_url, license,
    last_commit_at.

    `branches` is the list of branch definitions, each:
        {
          "key": str,                 # ISO 639-3 code
          "name": str,                # Chinese display name
          "iso_639_3": str,
          "intro": str,
          "dialects": [
            { "name": str, "schemas": list[str] },  # schema_ids
          ]
        }
    """
    overrides = yaml.safe_load(overrides_path.read_text(encoding="utf-8")) or {}
    branch_defs: dict = overrides.get("branches") or {}
    assignments: dict = overrides.get("schema_assignments") or {}
    source_groups = _build_source_group_lookup(branch_defs)

    enriched: list[dict] = []
    for s in schemas:
        sid = s["schema_id"]
        a = assignments.get(sid, {})
        branch = a.get("branch") or s.get("branch") or source_groups.get(s.get("source_group"))
        dialect = (
            a.get("dialect")
            or s.get("dialect")
            or _fallback_dialect(branch_defs, branch, s.get("source_group"))
        )
        enriched.append({
            **s,
            "branch": branch,
            "dialect": dialect,
            "recipe": a.get("recipe"),
            "upstream_url": a.get("upstream_url"),
            "license": a.get("license"),
            "last_commit_at": a.get("last_commit_at"),
        })

    branches = _build_branches(branch_defs, enriched)
    return enriched, branches


def _build_branches(branch_defs: dict, schemas: list[dict]) -> list[dict]:
    """Group schemas into branch.dialects[*].schemas, ordered by branch_defs."""
    by_branch_dialect: dict[tuple[str, str], list[str]] = {}
    for s in schemas:
        branch = s.get("branch")
        dialect = s.get("dialect")
        if not branch or not dialect:
            continue
        by_branch_dialect.setdefault((branch, dialect), []).append(s["schema_id"])

    out: list[dict] = []
    for key, defn in branch_defs.items():
        explicit_dialects = list(defn.get("dialects", []) or [])
        extra_dialects = sorted(
            dialect
            for branch, dialect in by_branch_dialect
            if branch == key and dialect not in explicit_dialects
        )
        dialects: list[dict] = []
        for dialect_name in explicit_dialects + extra_dialects:
            schemas_in = by_branch_dialect.get((key, dialect_name), [])
            dialects.append({"name": dialect_name, "schemas": schemas_in})
        schema_count = sum(len(d["schemas"]) for d in dialects)
        out.append({
            "key": key,
            "name": defn.get("name", key),
            "iso_639_3": defn.get("iso_639_3", key),
            "intro": defn.get("intro", ""),
            "status": defn.get("status") or _branch_status(key, explicit_dialects, schema_count),
            "dialects": dialects,
        })
    return out


def _build_source_group_lookup(branch_defs: dict) -> dict[str, str]:
    lookup: dict[str, str] = {}
    for key, defn in branch_defs.items():
        name = defn.get("name")
        if name:
            lookup[name] = key
        for dialect in defn.get("dialects", []) or []:
            lookup.setdefault(dialect, key)
    return lookup


def _fallback_dialect(branch_defs: dict, branch: str | None, source_group: str | None) -> str | None:
    if not branch:
        return None
    dialects = list((branch_defs.get(branch) or {}).get("dialects", []) or [])
    if source_group in dialects:
        return source_group
    if len(dialects) == 1:
        return dialects[0]
    if dialects:
        return "其他方案"
    return source_group or "其他方案"


def _branch_status(key: str, dialects: list[str], schema_count: int) -> str:
    if key in {"och", "ltc", "extra"}:
        return "synthetic"
    if not dialects and schema_count == 0:
        return "missing"
    return "active"
