from pathlib import Path

from manifest.phonology.compile import compile_phonology, summary_entry


def test_compile_phonology_filters_phrases_and_builds_tables(fixtures_dir: Path):
    record = compile_phonology(
        schema_id="jyutping",
        display_name="粵拼",
        schema_path=fixtures_dir / "phonology" / "sample_jyutping.schema.yaml",
        dict_path=fixtures_dir / "phonology" / "sample_jyutping.dict.yaml",
        dictionary_name="sample_jyutping",
        repo_root=fixtures_dir,
    )

    assert record is not None
    assert record["schema_id"] == "jyutping"
    assert record["dictionary"] == "sample_jyutping"
    assert record["tone_encoding"] == "digits"
    assert {row["spelling"] for row in record["initials"]} >= {"s", "b", "p", "m", "g"}
    assert {row["value"] for row in record["tones"]} == {"1", "2", "3", "4"}
    assert all(entry["char"] != "中華" for entry in record["syllable_index"])
    assert record["stats"]["single_char_rows"] == 10


def test_compile_phonology_applies_letter_tone_overrides(tmp_path: Path):
    schema = tmp_path / "letter.schema.yaml"
    dictionary = tmp_path / "letter.dict.yaml"
    schema.write_text(
        "schema:\n  schema_id: letter\ntranslator:\n  dictionary: letter\n",
        encoding="utf-8",
    )
    dictionary.write_text("...\n字\tzaq\n詞\tzar\n佐\tzoq\n", encoding="utf-8")

    record = compile_phonology(
        schema_id="letter",
        display_name="字母調",
        schema_path=schema,
        dict_path=dictionary,
        dictionary_name="letter",
        repo_root=tmp_path,
        overrides={"tone_encoding": "letters", "tone_letters": ["q", "r"], "extra_initials": ["z"]},
    )

    assert record is not None
    assert record["tone_encoding"] == "letters"
    assert {row["value"] for row in record["tones"]} == {"q", "r"}


def test_summary_entry_caps_large_arrays(fixtures_dir: Path):
    record = compile_phonology(
        schema_id="jyutping",
        display_name="粵拼",
        schema_path=fixtures_dir / "phonology" / "sample_jyutping.schema.yaml",
        dict_path=fixtures_dir / "phonology" / "sample_jyutping.dict.yaml",
        dictionary_name="sample_jyutping",
        repo_root=fixtures_dir,
    )

    summary = summary_entry(record, asset_path="/phonology/jyutping.json", preview_limit=3)

    assert summary["asset_path"] == "/phonology/jyutping.json"
    assert "syllable_index" not in summary
    assert len(summary["preview_syllables"]) == 3
