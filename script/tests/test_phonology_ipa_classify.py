from pathlib import Path

from manifest.phonology.ipa_classify import (
    classify_final,
    classify_initial,
    compile_finals_grid,
    compile_initials_grid,
    load_ipa_dictionary,
    split_final,
)
from manifest.phonology.schema_hints import SchemaHints


def test_ipa_dictionary_loads_required_keys():
    dictionary = load_ipa_dictionary(Path("script/phonology_ipa_dictionary.yaml"))

    assert set(dictionary) >= {
        "places",
        "manners",
        "initials_default",
        "nuclei_default",
        "codas",
        "finals_default",
    }
    assert dictionary["places"]["bilabial"] == "雙脣音"
    assert dictionary["manners"]["plosive"] == "爆發音"


def test_classify_jyutping_initials_into_ipa_cells():
    dictionary = load_ipa_dictionary(Path("script/phonology_ipa_dictionary.yaml"))
    hints = SchemaHints()

    assert classify_initial("b", hints, dictionary) == {
        "ipa": "p",
        "place": "bilabial",
        "manner": "plosive",
    }
    assert classify_initial("gw", hints, dictionary) == {
        "ipa": "kʷ",
        "place": "velar",
        "manner": "plosive",
    }
    assert classify_initial("j", hints, dictionary) == {
        "ipa": "j",
        "place": "palatal",
        "manner": "approximant",
    }


def test_split_and_classify_jyutping_finals_with_exact_overrides():
    dictionary = load_ipa_dictionary(Path("script/phonology_ipa_dictionary.yaml"))
    hints = SchemaHints()

    assert split_final("aang", dictionary) == ("aa", "ng")
    assert classify_final("ing", hints, dictionary) == {
        "nucleus": "i",
        "nucleus_ipa": "e",
        "coda": "ng",
        "coda_label": "-ng",
        "ipa": "eŋ",
        "row_key": "i:e",
    }
    assert classify_final("uk", hints, dictionary) == {
        "nucleus": "u",
        "nucleus_ipa": "o",
        "coda": "k",
        "coda_label": "-k",
        "ipa": "ok̚",
        "row_key": "u:o",
    }


def test_compile_grids_places_jyutping_inventory():
    dictionary = load_ipa_dictionary(Path("script/phonology_ipa_dictionary.yaml"))
    hints = SchemaHints()
    initials = [
        {"spelling": "b", "example_chars": ["巴"], "syllable_count": 1, "char_count": 1},
        {"spelling": "p", "example_chars": ["怕"], "syllable_count": 1, "char_count": 1},
        {"spelling": "m", "example_chars": ["媽"], "syllable_count": 1, "char_count": 1},
        {"spelling": "z", "example_chars": ["渣"], "syllable_count": 1, "char_count": 1},
        {"spelling": "gw", "example_chars": ["瓜"], "syllable_count": 1, "char_count": 1},
    ]
    finals = [
        {"spelling": "i", "example_chars": ["詩"], "syllable_count": 1, "char_count": 1},
        {"spelling": "ing", "example_chars": ["升"], "syllable_count": 1, "char_count": 1},
        {"spelling": "aa", "example_chars": ["沙"], "syllable_count": 1, "char_count": 1},
        {"spelling": "aak", "example_chars": ["責"], "syllable_count": 1, "char_count": 1},
    ]

    initials_grid = compile_initials_grid(initials, hints, dictionary)
    finals_grid = compile_finals_grid(finals, hints, dictionary)

    assert [entry["spelling"] for entry in initials_grid["cells"]["plosive"]["bilabial"]] == ["b", "p"]
    assert initials_grid["cells"]["plosive"]["velar"][0]["spelling"] == "gw"
    assert initials_grid["coverage"]["categorised"] == 5
    i_rows = [row for row in finals_grid["rows"] if row["nucleus"] == "i"]
    assert [row["ipa"] for row in i_rows] == ["iː", "e"]
    assert finals_grid["cells"]["i|"][0]["ipa"] == "iː"
    assert finals_grid["cells"]["i:e|ng"][0]["ipa"] == "eŋ"
    assert finals_grid["cells"]["aa|k"][0]["ipa"] == "aːk̚"
