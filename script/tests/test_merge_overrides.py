from pathlib import Path

from manifest.merge_overrides import merge_overrides


def test_merge_attaches_assignment_fields(fixtures_dir: Path):
    schemas = [
        {"schema_id": "jyutping", "display_name": "粵拼"},
        {"schema_id": "wugniu_soutseu", "display_name": "蘇州話"},
    ]
    merged, branches = merge_overrides(schemas, fixtures_dir / "manifest_overrides.yaml")
    by_id = {s["schema_id"]: s for s in merged}

    assert by_id["jyutping"]["branch"] == "yue"
    assert by_id["jyutping"]["dialect"] == "廣州話"
    assert by_id["jyutping"]["recipe"] == "rime/rime-jyutping"
    assert by_id["jyutping"]["upstream_url"] == "https://github.com/rime/rime-jyutping"
    assert by_id["jyutping"]["license"] == "CC BY 4.0"
    assert by_id["jyutping"]["last_commit_at"] == "2025-11-30T08:14:00Z"


def test_merge_returns_branch_definitions(fixtures_dir: Path):
    schemas = [{"schema_id": "jyutping"}, {"schema_id": "wugniu_soutseu"}]
    _merged, branches = merge_overrides(schemas, fixtures_dir / "manifest_overrides.yaml")

    by_key = {b["key"]: b for b in branches}
    assert by_key["yue"]["name"] == "粵語"
    assert by_key["yue"]["iso_639_3"] == "yue"
    assert by_key["yue"]["intro"].startswith("粵語區")
    assert by_key["yue"]["status"] == "active"


def test_merge_groups_schemas_into_branch_dialects(fixtures_dir: Path):
    schemas = [{"schema_id": "jyutping"}, {"schema_id": "wugniu_soutseu"}]
    _merged, branches = merge_overrides(schemas, fixtures_dir / "manifest_overrides.yaml")
    by_key = {b["key"]: b for b in branches}

    yue_dialects = {d["name"]: d["schemas"] for d in by_key["yue"]["dialects"]}
    assert yue_dialects["廣州話"] == ["jyutping"]

    wuu_dialects = {d["name"]: d["schemas"] for d in by_key["wuu"]["dialects"]}
    assert wuu_dialects["蘇州話"] == ["wugniu_soutseu"]


def test_merge_omits_branches_with_no_schemas(fixtures_dir: Path):
    schemas = [{"schema_id": "jyutping"}]  # only yue, not wuu
    _merged, branches = merge_overrides(schemas, fixtures_dir / "manifest_overrides.yaml")
    keys = {b["key"] for b in branches}
    assert "yue" in keys
    # wuu is in overrides but has no schemas in this run — still emitted so the
    # homepage chart can display it (potentially with count 0). See spec §5.1.
    assert "wuu" in keys


def test_merge_preserves_preassigned_orphan_fields(fixtures_dir: Path):
    schemas = [{"schema_id": "dkzp", "branch": "yue", "dialect": "廣州話"}]
    merged, branches = merge_overrides(schemas, fixtures_dir / "manifest_overrides.yaml")

    assert merged[0]["branch"] == "yue"
    assert merged[0]["dialect"] == "廣州話"
    yue = next(b for b in branches if b["key"] == "yue")
    assert yue["dialects"][0]["schemas"] == ["dkzp"]


def test_merge_assigns_source_only_schema_to_branch_tree(fixtures_dir: Path):
    schemas = [{"schema_id": "extra_variant", "source_group": "粵語"}]
    merged, branches = merge_overrides(schemas, fixtures_dir / "manifest_overrides.yaml")

    assert merged[0]["branch"] == "yue"
    assert merged[0]["dialect"] == "廣州話"
    yue = next(b for b in branches if b["key"] == "yue")
    assert yue["dialects"][0]["schemas"] == ["extra_variant"]
