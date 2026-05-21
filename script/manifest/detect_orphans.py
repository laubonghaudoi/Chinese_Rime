"""Detect schemas the README lists but the manifest builder couldn't account for."""
from __future__ import annotations


class OrphanError(RuntimeError):
    """Raised when README mentions a schema_id that the manifest doesn't include."""


def detect_orphans(readme_ids: set[str], manifest_ids: set[str]) -> None:
    """Raise OrphanError listing every README-only schema_id."""
    missing = sorted(readme_ids - manifest_ids)
    if not missing:
        return
    raise OrphanError(
        "The following schema_ids are listed in the README but absent from the manifest. "
        "Either add them under `orphans:` in script/manifest_overrides.yaml, or remove "
        "them from the README:\n  - " + "\n  - ".join(missing)
    )
