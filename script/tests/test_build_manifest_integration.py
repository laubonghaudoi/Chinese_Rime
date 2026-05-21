"""End-to-end test: run the full pipeline against the fixture tree."""
import json
import subprocess
from pathlib import Path

import pytest

SCRIPT_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = SCRIPT_DIR.parent


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


def test_root_module_wrapper_runs_against_fixtures(fixtures_dir: Path, tmp_path: Path):
    out_path = tmp_path / "schemas.json"
    readme_list = tmp_path / "readme_ids.txt"
    readme_list.write_text("jyutping\nwugniu_soutseu\n", encoding="utf-8")

    result = subprocess.run(
        [
            "python",
            "-m",
            "build_manifest",
            "--sources",
            str(fixtures_dir / "sources"),
            "--source-info",
            str(fixtures_dir / "source_info.yaml"),
            "--overrides",
            str(fixtures_dir / "manifest_overrides.yaml"),
            "--readme-ids",
            str(readme_list),
            "--out",
            str(out_path),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"stderr was:\n{result.stderr}"
    data = json.loads(out_path.read_text(encoding="utf-8"))
    assert len(data["schemas"]) == 2


def test_root_script_wrapper_exposes_cli_help():
    result = subprocess.run(
        ["python", "build_manifest.py", "--help"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "--sources" in result.stdout


def test_build_phonology_cli_writes_summary_and_assets(tmp_path: Path):
    sources = tmp_path / "sources"
    download = tmp_path / "download"
    schema_dir = sources / "吳語" / "sample"
    schema_dir.mkdir(parents=True)
    (schema_dir / "letter.schema.yaml").write_text(
        "schema:\n  schema_id: letter\n  name: 字母調\ntranslator:\n  dictionary: shared\n",
        encoding="utf-8",
    )
    (schema_dir / "shared.dict.yaml").write_text(
        "...\n字\tzaq\n詞\tzar\n組\tzoq\n詞組\tzar zoq\n",
        encoding="utf-8",
    )
    download.mkdir()

    manifest_path = tmp_path / "schemas.json"
    manifest_path.write_text(
        json.dumps(
            {
                "generated_at": "2026-05-20T00:00:00Z",
                "stats": {"schema_count": 1},
                "branches": [
                    {
                        "key": "wuu",
                        "dialects": [
                            {
                                "name": "吳語",
                                "schemas": ["letter"],
                            }
                        ],
                    }
                ],
                "schemas": {
                    "letter": {
                        "schema_id": "letter",
                        "display_name": "字母調",
                        "slug": "letter",
                    }
                },
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    overrides_path = tmp_path / "phonology_overrides.yaml"
    overrides_path.write_text(
        "overrides:\n  letter:\n    tone_encoding: letters\n    tone_letters: [q, r]\n    extra_initials: [z]\n",
        encoding="utf-8",
    )
    summary_path = tmp_path / "phonology-summary.json"
    assets_dir = tmp_path / "public" / "phonology"

    result = subprocess.run(
        [
            "python",
            "-m",
            "build_phonology",
            "--schemas",
            str(manifest_path),
            "--sources-root",
            str(sources),
            "--download-root",
            str(download),
            "--overrides",
            str(overrides_path),
            "--summary-out",
            str(summary_path),
            "--assets-out-dir",
            str(assets_dir),
        ],
        cwd=SCRIPT_DIR,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"stderr was:\n{result.stderr}"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    asset = json.loads((assets_dir / "letter.json").read_text(encoding="utf-8"))
    assert summary["schemas"]["letter"]["asset_path"] == "/phonology/letter.json"
    assert summary["schemas"]["letter"]["tones"]
    assert "letter" not in summary["skipped"]
    assert asset["dictionary"] == "shared"
    assert all(entry["char"] != "詞組" for entry in asset["syllable_index"])
    assert "schema_id\tfamily\tinit_grid\tfinal_grid" in result.stderr
    assert "\nletter\twuu\t" in result.stderr


def test_root_build_phonology_wrapper_exposes_cli_help():
    result = subprocess.run(
        ["python", "build_phonology.py", "--help"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "--summary-out" in result.stdout
