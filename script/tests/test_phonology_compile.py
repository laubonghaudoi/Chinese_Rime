from pathlib import Path

from manifest.phonology.compile import compile_phonology, summary_entry

SCRIPT_DIR = Path(__file__).resolve().parents[1]
IPA_DICTIONARY_PATH = SCRIPT_DIR / "phonology_ipa_dictionary.yaml"


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


def test_compile_phonology_filters_single_char_multi_token_codes(tmp_path: Path):
    schema = tmp_path / "multi.schema.yaml"
    dictionary = tmp_path / "multi.dict.yaml"
    schema.write_text(
        "schema:\n  schema_id: multi\ntranslator:\n  dictionary: multi\n",
        encoding="utf-8",
    )
    dictionary.write_text("...\n字\tzi1\n叉\tcaa si bin\n", encoding="utf-8")

    record = compile_phonology(
        schema_id="multi",
        display_name="多碼",
        schema_path=schema,
        dict_path=dictionary,
        dictionary_name="multi",
        repo_root=tmp_path,
        overrides={"extra_initials": ["z", "c"]},
        ipa_dictionary_path=IPA_DICTIONARY_PATH,
    )

    assert record is not None
    assert record["stats"]["single_char_rows"] == 1
    assert record["syllable_index"] == [{"char": "字", "spellings": ["zi1"]}]


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


def test_compile_phonology_emits_ipa_grids_when_dictionary_supplied(fixtures_dir: Path):
    record = compile_phonology(
        schema_id="jyutping",
        display_name="粵拼",
        schema_path=fixtures_dir / "phonology" / "sample_jyutping.schema.yaml",
        dict_path=fixtures_dir / "phonology" / "sample_jyutping.dict.yaml",
        dictionary_name="sample_jyutping",
        repo_root=fixtures_dir,
        ipa_dictionary_path=IPA_DICTIONARY_PATH,
    )

    assert record is not None
    assert record["grid_status"] == "ok"
    assert record["initials_grid"]["cells"]["fricative"]["alveolar"][0]["spelling"] == "s"
    assert record["initials_grid"]["cells"]["plosive"]["bilabial"][0]["ipa"] == "p"
    assert record["finals_grid"]["cells"]["i|"][0]["spelling"] == "i"

    summary = summary_entry(record, asset_path="/phonology/jyutping.json")
    assert summary["grid_status"] == "ok"
    assert "initials_grid" in summary
    assert "finals_grid" in summary


def test_compile_phonology_suppresses_grids_from_overrides(fixtures_dir: Path):
    record = compile_phonology(
        schema_id="OC_baxter1992",
        display_name="上古漢語",
        schema_path=fixtures_dir / "phonology" / "sample_jyutping.schema.yaml",
        dict_path=fixtures_dir / "phonology" / "sample_jyutping.dict.yaml",
        dictionary_name="sample_jyutping",
        repo_root=fixtures_dir,
        overrides={"suppress_grids": True},
        ipa_dictionary_path=IPA_DICTIONARY_PATH,
    )

    assert record is not None
    assert record["grid_status"] == "no_grids"
    assert "initials_grid" not in record
    assert "finals_grid" not in record
    assert record["syllable_index"]


def test_compile_phonology_sorts_superscript_digit_tones(tmp_path: Path):
    schema = tmp_path / "superscript.schema.yaml"
    dictionary = tmp_path / "superscript.dict.yaml"
    schema.write_text(
        "schema:\n  schema_id: superscript\ntranslator:\n  dictionary: superscript\n",
        encoding="utf-8",
    )
    dictionary.write_text("...\n字\tza⁷\n詞\tza⁸\n", encoding="utf-8")

    record = compile_phonology(
        schema_id="superscript",
        display_name="上標調",
        schema_path=schema,
        dict_path=dictionary,
        dictionary_name="superscript",
        repo_root=tmp_path,
        overrides={"extra_initials": ["z"]},
        ipa_dictionary_path=IPA_DICTIONARY_PATH,
    )

    assert record is not None
    assert [tone["value"] for tone in record["tones"]] == ["⁷", "⁸"]
