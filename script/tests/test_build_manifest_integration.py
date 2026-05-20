"""End-to-end test: run the full pipeline against the fixture tree."""
import json
import subprocess
from pathlib import Path

import pytest

SCRIPT_DIR = Path(__file__).resolve().parents[1]


def test_full_pipeline_against_fixtures(fixtures_dir: Path, tmp_path: Path):
    out_path = tmp_path / "schemas.json"
    # Build a minimal "readme list" file the CLI can consume.
    readme_list = tmp_path / "readme_ids.txt"
    readme_list.write_text("jyutping\nwugniu_soutseu\n", encoding="utf-8")

    result = subprocess.run(
        [
            "python", "-m", "build_manifest",
            "--sources", str(fixtures_dir / "sources"),
            "--source-info", str(fixtures_dir / "source_info.yaml"),
            "--overrides", str(fixtures_dir / "manifest_overrides.yaml"),
            "--readme-ids", str(readme_list),
            "--out", str(out_path),
        ],
        cwd=SCRIPT_DIR,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"stderr was:\n{result.stderr}"
    produced = json.loads(out_path.read_text(encoding="utf-8"))
    produced.pop("generated_at", None)
    expected = json.loads((fixtures_dir / "expected_schemas.json").read_text(encoding="utf-8"))
    expected.pop("generated_at", None)
    assert produced == expected


def test_orphan_detection_fails_pipeline(fixtures_dir: Path, tmp_path: Path):
    readme_list = tmp_path / "readme_ids.txt"
    readme_list.write_text("jyutping\nwugniu_soutseu\ndkzp\n", encoding="utf-8")

    result = subprocess.run(
        [
            "python", "-m", "build_manifest",
            "--sources", str(fixtures_dir / "sources"),
            "--source-info", str(fixtures_dir / "source_info.yaml"),
            "--overrides", str(fixtures_dir / "manifest_overrides.yaml"),
            "--readme-ids", str(readme_list),
            "--out", str(tmp_path / "schemas.json"),
        ],
        cwd=SCRIPT_DIR,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "dkzp" in result.stderr
