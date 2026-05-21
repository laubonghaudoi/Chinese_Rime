from pathlib import Path

from manifest.walk_submodules import walk_submodules


def test_walk_submodules_finds_both_fixture_schemas(sources_dir: Path):
    result = walk_submodules(sources_dir)
    ids = sorted(s["schema_id"] for s in result)
    assert ids == ["jyutping", "wugniu_soutseu"]


def test_walk_submodules_normalizes_authors(sources_dir: Path):
    result = walk_submodules(sources_dir)
    jyutping = next(s for s in result if s["schema_id"] == "jyutping")
    # YAML: ["佛振 <chen.sst@gmail.com>", "LeiMaau <leimaau@qq.com>"]
    # Normalized: emails stripped, names only
    assert jyutping["authors"] == ["佛振", "LeiMaau"]


def test_walk_submodules_handles_string_author(sources_dir: Path):
    result = walk_submodules(sources_dir)
    wugniu = next(s for s in result if s["schema_id"] == "wugniu_soutseu")
    # YAML: ["吳語學堂"] — single string-only author
    assert wugniu["authors"] == ["吳語學堂"]


def test_walk_submodules_normalizes_description(sources_dir: Path):
    result = walk_submodules(sources_dir)
    jyutping = next(s for s in result if s["schema_id"] == "jyutping")
    # YAML block scalar has trailing newline; we trim it but keep internal newlines.
    assert jyutping["description"] == (
        "採用香港語言學會粵語拼音方案。\n兼容教育學院拼音方案。"
    )


def test_walk_submodules_handles_missing_optional_fields(sources_dir: Path):
    result = walk_submodules(sources_dir)
    wugniu = next(s for s in result if s["schema_id"] == "wugniu_soutseu")
    # wugniu fixture has no `dependencies` field
    assert wugniu["dependencies"] == []


def test_walk_submodules_tolerates_tabs_and_list_descriptions(tmp_path: Path):
    schema_path = tmp_path / "sources" / "晉語" / "tabbed" / "tabbed.schema.yaml"
    schema_path.parent.mkdir(parents=True)
    schema_path.write_text(
        'schema:\n'
        '  schema_id: tabbed\n'
        '  name: Tabbed\n'
        '  version: "2026.01"\t\n'
        '  description:\n'
        '    - line one\t# upstream aligns comments with tabs\n'
        '    - line two\n',
        encoding="utf-8",
    )

    result = walk_submodules(tmp_path / "sources")
    assert result[0]["schema_id"] == "tabbed"
    assert result[0]["description"] == "line one\nline two"


def test_walk_submodules_keeps_shallow_duplicate_schema(tmp_path: Path):
    primary = tmp_path / "sources" / "粵語" / "sample" / "dup.schema.yaml"
    nested = tmp_path / "sources" / "粵語" / "sample" / "mobile" / "dup.schema.yaml"
    primary.parent.mkdir(parents=True)
    nested.parent.mkdir(parents=True)
    primary.write_text("schema:\n  schema_id: dup\n  name: Primary\n", encoding="utf-8")
    nested.write_text("schema:\n  schema_id: dup\n  name: Nested\n", encoding="utf-8")

    result = walk_submodules(tmp_path / "sources")
    assert len(result) == 1
    assert result[0]["display_name"] == "Primary"
