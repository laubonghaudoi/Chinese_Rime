"""Final assembly: write the manifest JSON Astro reads at build time."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def emit_json(schemas: list[dict], branches: list[dict], out_path: Path) -> None:
    """Serialize the assembled schemas + branches to JSON at out_path."""
    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "stats": _stats(schemas, branches),
        "branches": branches,
        "schemas": {s["schema_id"]: _to_schema_entry(s) for s in schemas},
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(out, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )


def _to_schema_entry(s: dict) -> dict:
    return {
        "schema_id": s["schema_id"],
        "slug": _slugify(s["schema_id"]),
        "display_name": s.get("display_name", s["schema_id"]),
        "branch": s.get("branch"),
        "dialect": s.get("dialect"),
        "authors": s.get("authors", []),
        "version": s.get("version", ""),
        "description": s.get("description", ""),
        "dependencies": s.get("dependencies", []),
        "license": s.get("license"),
        "recipe": s.get("recipe"),
        "upstream_url": s.get("upstream_url"),
        "last_commit_at": s.get("last_commit_at"),
        "downloadable": s.get("downloadable", False),
        "download_package": s.get("download_package"),
    }


def _stats(schemas: list[dict], branches: list[dict]) -> dict:
    recipes = {s.get("recipe") for s in schemas if s.get("recipe")}
    download_packages = {s.get("download_package") for s in schemas if s.get("download_package")}
    active_branches = [b for b in branches if b.get("status") != "missing"]
    return {
        "schema_count": len({s["schema_id"] for s in schemas}),
        "recipe_count": len(recipes),
        "download_package_count": len(download_packages),
        "branch_count": len(branches),
        "active_branch_count": len(active_branches),
        "missing_branch_count": sum(1 for b in branches if b.get("status") == "missing"),
    }


def _slugify(schema_id: str) -> str:
    """Sanitize schema_id for use as a URL slug.

    Per spec §3 the only substitution is `+` → `-plus`. All other characters
    pass through unchanged (schema_ids are Latin + dashes/underscores by
    upstream convention).
    """
    return schema_id.replace("+", "-plus")
