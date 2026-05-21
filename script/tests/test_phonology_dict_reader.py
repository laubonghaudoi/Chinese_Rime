from pathlib import Path

from manifest.phonology.dict_reader import read_dict


def test_read_dict_returns_char_spelling_pairs(fixtures_dir: Path):
    rows = read_dict(fixtures_dir / "phonology" / "sample_jyutping.dict.yaml")

    assert ("詩", "si1") in rows
    assert ("試", "si3") in rows
    assert len(rows) == 11


def test_read_dict_handles_missing_file(tmp_path: Path):
    assert read_dict(tmp_path / "missing.dict.yaml") == []


def test_read_dict_skips_blank_comment_and_malformed_rows(tmp_path: Path):
    path = tmp_path / "messy.dict.yaml"
    path.write_text("...\n# comment\n\n啊\taa3\nbad-row\n媽\tmaa1\t100\n", encoding="utf-8")

    assert read_dict(path) == [("啊", "aa3"), ("媽", "maa1")]


def test_read_dict_strips_inline_code_annotations(tmp_path: Path):
    path = tmp_path / "annotated.dict.yaml"
    path.write_text(
        "...\n覆\tfou4◎〔文讀〕\n汃\tpa1||爛熟\n銳\tzuei4П\n",
        encoding="utf-8",
    )

    assert read_dict(path) == [("覆", "fou4"), ("汃", "pa1"), ("銳", "zuei4")]
