from pathlib import Path

from manifest.join_source_info import join_source_info


def test_join_marks_downloadable_when_schema_in_files(fixtures_dir: Path):
    raw = [
        {"schema_id": "jyutping"},
        {"schema_id": "wugniu_soutseu"},
        {"schema_id": "orphan_not_in_source_info"},
    ]
    enriched = join_source_info(raw, fixtures_dir / "source_info.yaml")
    by_id = {s["schema_id"]: s for s in enriched}

    assert by_id["jyutping"]["downloadable"] is True
    assert by_id["jyutping"]["download_package"] == "粵語/廣州話"
    assert by_id["wugniu_soutseu"]["downloadable"] is True
    assert by_id["wugniu_soutseu"]["download_package"] == "吳語/蘇州話"
    assert by_id["orphan_not_in_source_info"]["downloadable"] is False
    assert by_id["orphan_not_in_source_info"]["download_package"] is None


def test_join_preserves_original_fields(fixtures_dir: Path):
    raw = [{"schema_id": "jyutping", "display_name": "粵拼"}]
    enriched = join_source_info(raw, fixtures_dir / "source_info.yaml")
    assert enriched[0]["display_name"] == "粵拼"
