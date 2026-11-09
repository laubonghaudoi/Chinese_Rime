import json
from pathlib import Path

import yaml

import build_phonology
from manifest.phonology.ipa_classify import load_ipa_dictionary
from manifest.phonology.second_scheme import (
    _compose,
    base_schema_id,
    compile_second_scheme,
    find_spelling_map,
    is_second_scheme,
    load_table,
)

SCRIPT_DIR = Path(__file__).resolve().parents[1]
TABLE_PATH = SCRIPT_DIR / "phonology_scheme2.tsv"
IPA_DICTIONARY_PATH = SCRIPT_DIR / "phonology_ipa_dictionary.yaml"


def base_overrides() -> dict:
    return {
        "tone_encoding": "none",
        "code_prefix": "G",
        "extra_initials": ["b", "p", "j", "n", "nj", "s", "g", "ng"],
        "extra_finals": ["a", "i", "ï", "ïk", "uet", "m"],
        "whole_syllables": {"m": ["", "m"]},
        "initials_ipa": {
            "b": {"ipa": "p", "place": "bilabial", "manner": "plosive"},
            "p": {"ipa": "pʰ", "place": "bilabial", "manner": "plosive"},
            "j": {"ipa": "tɕ", "place": "palatal", "manner": "affricate"},
            "n": {"ipa": "n", "place": "alveolar", "manner": "nasal"},
            "nj": {"ipa": "ȵ", "place": "palatal", "manner": "nasal"},
            "s": {"ipa": "s", "place": "alveolar", "manner": "fricative"},
            "g": {"ipa": "k", "place": "velar", "manner": "plosive"},
            "ng": {"ipa": "ŋ", "place": "velar", "manner": "nasal"},
        },
        "finals_ipa": {
            "a": {"nucleus": "a", "nucleus_ipa": "a", "coda": "", "ipa": "a"},
            "i": {"nucleus": "i", "nucleus_ipa": "i", "coda": "", "ipa": "i"},
            "ï": {"nucleus": "ï", "nucleus_ipa": "ɿ", "coda": "", "ipa": "ɿ"},
            "ïk": {"nucleus": "ï", "nucleus_ipa": "ɿ", "coda": "k", "ipa": "ɿʔ"},
            "uet": {"nucleus": "ue", "nucleus_ipa": "uə", "coda": "t", "ipa": "uət"},
            "m": {"nucleus": "m", "nucleus_ipa": "m̩", "coda": "", "ipa": "m̩"},
        },
    }


def test_schema_id_helpers():
    assert is_second_scheme("konny_lancong_II")
    assert not is_second_scheme("gannyu_lancong")
    assert base_schema_id("konny_lancong_II") == "gannyu_lancong"


def test_find_spelling_map_reads_lua_table(tmp_path: Path):
    lua = tmp_path / "lua" / "konny_lancong_scheme2.lua"
    lua.parent.mkdir()
    lua.write_text(
        'return {\n  spellings = {\n    ["ba"] = "pa",\n    ["sï"] = "sii",\n  },\n'
        '  tones = {\n    ["1"] = "55",\n  },\n}\n',
        encoding="utf-8",
    )
    schema = tmp_path / "konny_lancong_II.schema.yaml"
    assert find_spelling_map("konny_lancong_II", schema, None, None) == {
        "ba": "pa",
        "sï": "sii",
    }


def test_compose_only_drops_i_medial_for_long_nucleus():
    table = load_table(TABLE_PATH)

    assert _compose("nj", "i", "i", table) == "nji"
    assert _compose("nj", "in", "in", table) == "njin"
    assert _compose("nj", "ia", "ia", table) == "nja"
    assert _compose("nj", "ien", "iɛn", table) == "njen"


def test_compile_second_scheme_uses_dictionary_ipa(tmp_path: Path):
    schema = tmp_path / "konny_test_II.schema.yaml"
    schema.write_text(
        "schema:\n  schema_id: konny_test_II\ntranslator:\n  dictionary: gannyu_test\n",
        encoding="utf-8",
    )
    dictionary = tmp_path / "gannyu_test.dict.yaml"
    dictionary.write_text(
        "...\n"
        "甲\tGba\n"
        "乙\tGpa\n"
        "丙\tGji\n"
        "丁\tGni\n"
        "戊\tGnji\n"
        "己\tGsï\n"
        "庚\tGsïk\n"
        "辛\tGguet\n"
        "壬\tGm\n"
        "癸\tGnga\n",
        encoding="utf-8",
    )
    lua = tmp_path / "lua" / "konny_test_scheme2.lua"
    lua.parent.mkdir()
    lua.write_text(
        "return {\n  spellings = {\n"
        '    ["ba"] = "pa",\n'
        '    ["pa"] = "pha",\n'
        '    ["ji"] = "ci",\n'
        '    ["ni"] = "ni",\n'
        '    ["nji"] = "nji",\n'
        '    ["sï"] = "sii",\n'
        '    ["sïk"] = "siih",\n'
        '    ["guet"] = "kuert",\n'
        '    ["m"] = "m",\n'
        '    ["nga"] = "nga",\n'
        "  },\n  tones = {},\n}\n",
        encoding="utf-8",
    )

    record = compile_second_scheme(
        schema_id="konny_test_II",
        display_name="測試",
        schema_path=schema,
        dict_path=dictionary,
        dictionary_name="gannyu_test",
        repo_root=tmp_path,
        base_overrides=base_overrides(),
        sources_root=None,
        download_root=None,
        ipa_dictionary=load_ipa_dictionary(IPA_DICTIONARY_PATH),
        table_path=TABLE_PATH,
    )

    assert record is not None
    assert record["stats"]["second_scheme_unmapped"] == 0
    assert {row["spelling"] for row in record["initials"] if row["spelling"]} == {
        "p", "ph", "c", "n", "nj", "s", "k", "ng",
    }
    assert {row["spelling"] for row in record["finals"]} == {
        "a", "i", "ii", "iih", "uert", "m",
    }
    assert {entry["char"]: entry["spellings"] for entry in record["syllable_index"]} == {
        "甲": ["pa"],
        "乙": ["pha"],
        "丙": ["ci"],
        "丁": ["ni"],
        "戊": ["nji"],
        "己": ["sii"],
        "庚": ["siih"],
        "辛": ["kuert"],
        "壬": ["m"],
        "癸": ["nga"],
    }
    assert record["grid_status"] == "ok"
    assert record["stats"]["uncategorised_initial_count"] == 0
    assert record["stats"]["uncategorised_final_count"] == 0


def test_build_phonology_cli_compiles_second_scheme(tmp_path: Path):
    sources = tmp_path / "sources"
    sources.mkdir()
    (sources / "lua").mkdir()
    (sources / "konny_test_II.schema.yaml").write_text(
        "schema:\n  schema_id: konny_test_II\ntranslator:\n  dictionary: gannyu_test\n",
        encoding="utf-8",
    )
    (sources / "gannyu_test.dict.yaml").write_text(
        "...\n甲\tGba\n乙\tGsï\n丙\tGm\n",
        encoding="utf-8",
    )
    (sources / "lua" / "konny_test_scheme2.lua").write_text(
        'return {\n  spellings = {\n    ["ba"] = "pa",\n    ["sï"] = "sii",\n'
        '    ["m"] = "m",\n  },\n  tones = {},\n}\n',
        encoding="utf-8",
    )
    schemas = tmp_path / "schemas.json"
    schemas.write_text(json.dumps({
        "schemas": {
            "konny_test_II": {
                "schema_id": "konny_test_II",
                "display_name": "測試二式",
            },
        },
    }), encoding="utf-8")
    overrides = tmp_path / "overrides.yaml"
    overrides.write_text(
        yaml.safe_dump({"overrides": {"gannyu_test": base_overrides()}}, allow_unicode=True),
        encoding="utf-8",
    )
    summary_path = tmp_path / "phonology-summary.json"
    assets_dir = tmp_path / "assets"

    result = build_phonology.main([
        "--schemas", str(schemas),
        "--sources-root", str(sources),
        "--download-root", str(tmp_path / "download"),
        "--overrides", str(overrides),
        "--ipa-dictionary", str(IPA_DICTIONARY_PATH),
        "--scheme2-table", str(TABLE_PATH),
        "--summary-out", str(summary_path),
        "--assets-out-dir", str(assets_dir),
    ])

    assert result == 0
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    assert summary["skipped"] == {}
    assert summary["schemas"]["konny_test_II"]["stats"]["second_scheme_unmapped"] == 0
    assert (assets_dir / "konny_test_II.json").is_file()
