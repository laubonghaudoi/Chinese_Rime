from pathlib import Path

from manifest.phonology.schema_hints import extract_hints


def test_extract_tone_encoding_digits(fixtures_dir: Path):
    hints = extract_hints(
        fixtures_dir / "phonology" / "sample_jyutping.schema.yaml",
        sample_spellings=["si1", "si2", "bong1"],
    )

    assert hints.tone_encoding == "digits"


def test_extract_recognized_initials_from_algebra(fixtures_dir: Path):
    hints = extract_hints(
        fixtures_dir / "phonology" / "sample_jyutping.schema.yaml",
        sample_spellings=["zi1", "ci1", "ji1"],
    )

    assert {"z", "c", "j"}.issubset(hints.recognized_initials)


def test_extract_handles_tabs_in_schema_yaml(fixtures_dir: Path):
    hints = extract_hints(
        fixtures_dir / "phonology" / "sample_tabs.schema.yaml",
        sample_spellings=["zaq"],
    )

    assert "z" in hints.recognized_initials


def test_extract_applies_phonology_overrides(fixtures_dir: Path):
    hints = extract_hints(
        fixtures_dir / "phonology" / "sample_no_tone.schema.yaml",
        sample_spellings=["zaq", "zar"],
        overrides={
            "tone_encoding": "letters",
            "tone_letters": ["q", "r"],
            "extra_initials": ["z"],
        },
    )

    assert hints.tone_encoding == "letters"
    assert hints.tone_letters == {"q", "r"}
    assert "z" in hints.recognized_initials


def test_extract_handles_missing_schema(tmp_path: Path):
    hints = extract_hints(tmp_path / "missing.schema.yaml", sample_spellings=[])

    assert hints.tone_encoding == "none"
    assert hints.recognized_initials == set()
