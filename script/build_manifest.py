"""Entry point for the manifest builder.

Usage:
    python -m build_manifest \\
        --sources sources/ \\
        --source-info script/source_info.yaml \\
        --overrides script/manifest_overrides.yaml \\
        --readme-ids script/.readme_ids.txt \\
        --out site/src/data/schemas.json

If --readme-ids is omitted, orphan detection is skipped (useful for ad-hoc runs
during development; CI always supplies it).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from manifest.detect_orphans import OrphanError, detect_orphans
from manifest.emit_json import emit_json
from manifest.join_source_info import join_source_info
from manifest.merge_overrides import merge_overrides
from manifest.walk_submodules import walk_submodules


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    schemas = walk_submodules(args.sources)
    schemas = join_source_info(schemas, args.source_info)
    schemas, branches = merge_overrides(schemas, args.overrides)

    # Append orphan-only entries (schemas that the README mentions but no
    # submodule provides). These are described entirely by the overrides file.
    overrides_data = _read_yaml(args.overrides)
    orphan_entries = _build_orphan_entries(overrides_data.get("orphans") or {})
    schemas.extend(orphan_entries)

    if args.readme_ids:
        readme_ids = _read_id_list(args.readme_ids)
        manifest_ids = {s["schema_id"] for s in schemas}
        try:
            detect_orphans(readme_ids, manifest_ids)
        except OrphanError as e:
            print(str(e), file=sys.stderr)
            return 2

    emit_json(schemas, branches, args.out)
    print(f"Wrote {len(schemas)} schemas across {len(branches)} branches → {args.out}")
    return 0


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--sources", type=Path, required=True)
    p.add_argument("--source-info", type=Path, required=True)
    p.add_argument("--overrides", type=Path, required=True)
    p.add_argument("--readme-ids", type=Path, default=None,
                   help="Optional file with one schema_id per line for orphan detection.")
    p.add_argument("--out", type=Path, required=True)
    return p.parse_args(argv)


def _read_yaml(path: Path) -> dict:
    import yaml
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _read_id_list(path: Path) -> set[str]:
    return {line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}


def _build_orphan_entries(orphans: dict) -> list[dict]:
    """Each orphan entry in YAML is keyed by schema_id with full field set inline."""
    out: list[dict] = []
    for sid, fields in (orphans or {}).items():
        out.append({
            "schema_id": sid,
            "display_name": fields.get("display_name", sid),
            "version": fields.get("version", ""),
            "authors": fields.get("authors", []),
            "description": fields.get("description", ""),
            "dependencies": fields.get("dependencies", []),
            "downloadable": False,
            "download_package": None,
            "branch": fields.get("branch"),
            "dialect": fields.get("dialect"),
            "recipe": fields.get("recipe"),
            "upstream_url": fields.get("upstream_url"),
            "license": fields.get("license"),
            "last_commit_at": fields.get("last_commit_at"),
        })
    return out


if __name__ == "__main__":
    raise SystemExit(main())
