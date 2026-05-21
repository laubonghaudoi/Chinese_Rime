from pathlib import Path

from manifest.phonology.resolver import SkippedSource, resolve_schema_source


def _write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def test_resolver_finds_exact_schema_and_dict(tmp_path: Path):
    sources = tmp_path / "sources"
    download = tmp_path / "download"
    schema = _write(
        sources / "粵語" / "sample" / "jyutping.schema.yaml",
        "schema:\n  schema_id: jyutping\ntranslator:\n  dictionary: jyutping\n",
    )
    dictionary = _write(sources / "粵語" / "sample" / "jyutping.dict.yaml", "...\n詩\tsi1\n")

    resolved = resolve_schema_source("jyutping", sources, download)

    assert not isinstance(resolved, SkippedSource)
    assert resolved.schema_path == schema
    assert resolved.dict_path == dictionary
    assert resolved.dictionary_name == "jyutping"


def test_resolver_uses_translator_dictionary_when_name_differs(tmp_path: Path):
    sources = tmp_path / "sources"
    download = tmp_path / "download"
    _write(
        sources / "粵語" / "sample" / "hkcantonese.schema.yaml",
        "schema:\n  schema_id: hkcantonese\ntranslator:\n  dictionary: jyutping\n",
    )
    dictionary = _write(sources / "粵語" / "sample" / "jyutping.dict.yaml", "...\n詩\tsi1\n")

    resolved = resolve_schema_source("hkcantonese", sources, download)

    assert not isinstance(resolved, SkippedSource)
    assert resolved.dict_path == dictionary
    assert resolved.dictionary_name == "jyutping"


def test_resolver_tolerates_tabs_in_schema_yaml(tmp_path: Path):
    sources = tmp_path / "sources"
    download = tmp_path / "download"
    _write(
        sources / "吳語" / "sample" / "tabs.schema.yaml",
        "schema:\n  schema_id: tabs\nspeller:\n  algebra:\n    - derive/^z/dz/\t# tab\ntranslator:\n  dictionary: tabs\n",
    )
    _write(sources / "吳語" / "sample" / "tabs.dict.yaml", "...\n字\tzaq\n")

    resolved = resolve_schema_source("tabs", sources, download)

    assert not isinstance(resolved, SkippedSource)
    assert resolved.dictionary_name == "tabs"


def test_resolver_reports_missing_dictionary_ref(tmp_path: Path):
    sources = tmp_path / "sources"
    download = tmp_path / "download"
    _write(sources / "域外" / "sample" / "todo.schema.yaml", "schema:\n  schema_id: todo\n")

    skipped = resolve_schema_source("todo", sources, download)

    assert isinstance(skipped, SkippedSource)
    assert skipped.reason == "missing_dictionary_ref"


def test_resolver_reports_missing_dict_file(tmp_path: Path):
    sources = tmp_path / "sources"
    download = tmp_path / "download"
    _write(
        sources / "粵語" / "sample" / "missing.schema.yaml",
        "schema:\n  schema_id: missing\ntranslator:\n  dictionary: absent\n",
    )

    skipped = resolve_schema_source("missing", sources, download)

    assert isinstance(skipped, SkippedSource)
    assert skipped.reason == "missing_dict_file"
