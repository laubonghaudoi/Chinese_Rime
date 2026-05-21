"""Cross-reference parsed schemas with source_info.yaml to mark downloadable status."""
from __future__ import annotations

from pathlib import Path

import yaml


def join_source_info(schemas: list[dict], source_info_path: Path) -> list[dict]:
    """Return a new list with `downloadable` and `download_package` fields populated.

    A schema_id is downloadable iff its `<schema_id>.schema.yaml` appears in the
    `files:` list of any download-package entry in source_info.yaml.
    """
    info = yaml.safe_load(source_info_path.read_text(encoding="utf-8")) or {}
    # Build reverse index: schema_id -> download_package key
    reverse: dict[str, str] = {}
    for pkg_key, pkg in info.items():
        for filename in pkg.get("files", []) or []:
            if filename.endswith(".schema.yaml"):
                sid = filename[: -len(".schema.yaml")]
                reverse[sid] = pkg_key

    out: list[dict] = []
    for s in schemas:
        sid = s["schema_id"]
        pkg = reverse.get(sid)
        out.append({**s, "downloadable": pkg is not None, "download_package": pkg})
    return out
