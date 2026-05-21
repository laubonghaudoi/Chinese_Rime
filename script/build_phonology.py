"""Build generated phonology summary and per-schema public assets."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

from manifest.phonology.compile import compile_phonology, summary_entry
from manifest.phonology.ipa_classify import load_ipa_dictionary
from manifest.phonology.resolver import ResolvedSource, resolve_schema_source


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    manifest = json.loads(args.schemas.read_text(encoding="utf-8"))
    overrides = _read_overrides(args.overrides)
    ipa_dictionary = load_ipa_dictionary(args.ipa_dictionary)
    repo_root = _infer_repo_root(args.sources_root)

    args.summary_out.parent.mkdir(parents=True, exist_ok=True)
    args.assets_out_dir.mkdir(parents=True, exist_ok=True)
    for stale in args.assets_out_dir.glob("*.json"):
        stale.unlink()

    summary: dict[str, Any] = {
        "generated_at": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "schemas": {},
        "skipped": {},
    }
    report_rows: list[dict[str, Any]] = []
    family_by_schema = _schema_family_map(manifest)

    for schema_id, schema in sorted(manifest.get("schemas", {}).items()):
        resolved = resolve_schema_source(schema_id, args.sources_root, args.download_root)
        if not isinstance(resolved, ResolvedSource):
            summary["skipped"][schema_id] = {"reason": resolved.reason}
            continue

        record = compile_phonology(
            schema_id=schema_id,
            display_name=schema.get("display_name", schema_id),
            schema_path=resolved.schema_path,
            dict_path=resolved.dict_path,
            dictionary_name=resolved.dictionary_name,
            repo_root=repo_root,
            overrides=overrides.get(schema_id),
            ipa_dictionary=ipa_dictionary,
        )
        if record is None:
            summary["skipped"][schema_id] = {"reason": "no_single_char_rows"}
            continue

        asset_path = f"/phonology/{schema_id}.json"
        (args.assets_out_dir / f"{schema_id}.json").write_text(
            json.dumps(record, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n",
            encoding="utf-8",
        )
        summary["schemas"][schema_id] = summary_entry(record, asset_path=asset_path)
        report_rows.append(record)

    args.summary_out.write_text(
        json.dumps(summary, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n",
        encoding="utf-8",
    )
    _print_report(report_rows, summary["skipped"], family_by_schema)
    return 0


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schemas", type=Path, default=repo_root / "site" / "src" / "data" / "schemas.json")
    parser.add_argument("--sources-root", type=Path, default=repo_root / "sources")
    parser.add_argument("--download-root", type=Path, default=repo_root / "download")
    parser.add_argument("--overrides", type=Path, default=repo_root / "script" / "phonology_overrides.yaml")
    parser.add_argument("--ipa-dictionary", type=Path, default=repo_root / "script" / "phonology_ipa_dictionary.yaml")
    parser.add_argument("--summary-out", type=Path, default=repo_root / "site" / "src" / "data" / "phonology-summary.json")
    parser.add_argument("--assets-out-dir", type=Path, default=repo_root / "site" / "public" / "phonology")
    return parser.parse_args(argv)


def _read_overrides(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    overrides = data.get("overrides") or {}
    return overrides if isinstance(overrides, dict) else {}


def _infer_repo_root(sources_root: Path) -> Path:
    if sources_root.name == "sources":
        return sources_root.parent
    return Path.cwd()


def _schema_family_map(manifest: dict[str, Any]) -> dict[str, str]:
    families: dict[str, str] = {}
    for branch in manifest.get("branches", []):
        if not isinstance(branch, dict):
            continue
        family = str(branch.get("key", "-"))
        for dialect in branch.get("dialects", []):
            if not isinstance(dialect, dict):
                continue
            for schema_id in dialect.get("schemas", []):
                families[str(schema_id)] = family
    return families


def _print_report(
    records: list[dict[str, Any]],
    skipped: dict[str, Any],
    family_by_schema: dict[str, str] | None = None,
) -> None:
    family_by_schema = family_by_schema or {}
    print(
        "schema_id\tfamily\tinit_grid\tfinal_grid\tuncategorised_init\tuncategorised_final\tstatus",
        file=sys.stderr,
    )
    for record in records:
        stats = record["stats"]
        suppressed = bool(stats.get("grid_suppressed"))
        initial_status = _coverage_status(stats.get("initial_grid_coverage"), suppressed)
        final_status = _coverage_status(stats.get("final_grid_coverage"), suppressed)
        initial_uncategorised = _coverage_gap(stats.get("initial_grid_coverage"), suppressed)
        final_uncategorised = _coverage_gap(stats.get("final_grid_coverage"), suppressed)
        status = "ok" if record.get("grid_status") == "ok" else ("suppressed" if suppressed else "needs_work")
        print(
            f"{record['schema_id']}\t{family_by_schema.get(record['schema_id'], '-')}\t"
            f"{initial_status}\t{final_status}\t{initial_uncategorised}\t{final_uncategorised}\t{status}",
            file=sys.stderr,
        )
    print(f"wrote={len(records)} skipped={len(skipped)}", file=sys.stderr)


def _coverage_status(coverage: Any, suppressed: bool) -> str:
    if suppressed:
        return "-"
    if not isinstance(coverage, dict):
        return "missing"
    if int(coverage.get("total", 0)) == 0:
        return "empty"
    if int(coverage.get("categorised", 0)) == int(coverage.get("total", 0)):
        return "ok"
    return "partial"


def _coverage_gap(coverage: Any, suppressed: bool) -> str | int:
    if suppressed:
        return "-"
    if not isinstance(coverage, dict):
        return "-"
    return int(coverage.get("total", 0)) - int(coverage.get("categorised", 0))


if __name__ == "__main__":
    raise SystemExit(main())
