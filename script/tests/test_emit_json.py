import json
from pathlib import Path

from manifest.emit_json import emit_json


def test_emit_matches_golden(fixtures_dir: Path, tmp_path: Path):
    # Fully assembled inputs that emit_json itself does NOT compute — caller
    # constructs them from the earlier passes (walk + join + merge).
    schemas = [
        {
            "schema_id": "jyutping",
            "display_name": "粵拼",
            "version": "0.15",
            "authors": ["佛振", "LeiMaau"],
            "description": "採用香港語言學會粵語拼音方案。\n兼容教育學院拼音方案。",
            "dependencies": ["luna_pinyin", "stroke"],
            "downloadable": True,
            "download_package": "粵語/廣州話",
            "branch": "yue",
            "dialect": "廣州話",
            "recipe": "rime/rime-jyutping",
            "upstream_url": "https://github.com/rime/rime-jyutping",
            "license": "CC BY 4.0",
            "last_commit_at": "2025-11-30T08:14:00Z",
        },
        {
            "schema_id": "wugniu_soutseu",
            "display_name": "蘇州話",
            "version": "0.3",
            "authors": ["吳語學堂"],
            "description": "吳語蘇州話拼音輸入方案，採用吳語協會式拼音。",
            "dependencies": [],
            "downloadable": True,
            "download_package": "吳語/蘇州話",
            "branch": "wuu",
            "dialect": "蘇州話",
            "recipe": "wugniu/wugniu",
            "upstream_url": "https://github.com/wugniu/wugniu",
            "license": "CC BY-SA 4.0",
            "last_commit_at": "2025-10-12T11:05:00Z",
        },
    ]
    branches = [
        {
            "key": "yue",
            "name": "粵語",
            "iso_639_3": "yue",
            "intro": "粵語區的拼音輸入方案，以廣州話為主。",
            "dialects": [{"name": "廣州話", "schemas": ["jyutping"]}],
        },
        {
            "key": "wuu",
            "name": "吳語",
            "iso_639_3": "wuu",
            "intro": "吳語區拼音輸入方案。",
            "dialects": [{"name": "蘇州話", "schemas": ["wugniu_soutseu"]}],
        },
    ]

    out_path = tmp_path / "schemas.json"
    emit_json(schemas, branches, out_path)
    produced = json.loads(out_path.read_text(encoding="utf-8"))

    # Compare against the golden fixture, but drop generated_at because it's a
    # wall-clock timestamp.
    produced.pop("generated_at", None)
    expected = json.loads((fixtures_dir / "expected_schemas.json").read_text(encoding="utf-8"))
    expected.pop("generated_at", None)

    assert produced == expected


def test_emit_sanitizes_slug_jyutping_plus(tmp_path: Path):
    schemas = [{
        "schema_id": "jyutping+",
        "display_name": "粵拼⁺",
        "version": "0.1",
        "authors": [],
        "description": "",
        "dependencies": [],
        "downloadable": False,
        "download_package": None,
        "branch": "yue",
        "dialect": "廣州話",
        "recipe": None,
        "upstream_url": None,
        "license": None,
        "last_commit_at": None,
    }]
    out_path = tmp_path / "schemas.json"
    emit_json(schemas, [], out_path)
    data = json.loads(out_path.read_text(encoding="utf-8"))
    assert data["schemas"]["jyutping+"]["slug"] == "jyutping-plus"
