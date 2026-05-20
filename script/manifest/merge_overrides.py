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

    enriched: list[dict] = []
    for s in schemas:
        sid = s["schema_id"]
        a = assignments.get(sid, {})
        enriched.append({
            **s,
            "branch": a.get("branch"),
            "dialect": a.get("dialect"),
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
        dialects: list[dict] = []
        for dialect_name in defn.get("dialects", []) or []:
            schemas_in = by_branch_dialect.get((key, dialect_name), [])
            dialects.append({"name": dialect_name, "schemas": schemas_in})
        out.append({
            "key": key,
            "name": defn.get("name", key),
            "iso_639_3": defn.get("iso_639_3", key),
            "intro": defn.get("intro", ""),
            "dialects": dialects,
        })
    return out
