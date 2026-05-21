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
    _print_report(report_rows, summary["skipped"])
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


def _print_report(records: list[dict[str, Any]], skipped: dict[str, Any]) -> None:
    print("schema_id\tinitials\tfinals\ttone_count\ttotal_chars\tundecomposable", file=sys.stderr)
    for record in records[:40]:
        stats = record["stats"]
        print(
            f"{record['schema_id']}\t{len(record['initials'])}\t{len(record['finals'])}\t"
            f"{len(record['tones'])}\t{stats['total_chars']}\t{stats['undecomposable_syllables']}",
            file=sys.stderr,
        )
    if len(records) > 40:
        print(f"... {len(records) - 40} more schema records omitted", file=sys.stderr)
    print(f"wrote={len(records)} skipped={len(skipped)}", file=sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main())
