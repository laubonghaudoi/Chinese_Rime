from manifest.phonology.decomposer import build_decomposer
from manifest.phonology.schema_hints import SchemaHints


JYUTPING_SAMPLE = [
    "si1",
    "si2",
    "si3",
    "si4",
    "bong1",
    "baan2",
    "paa3",
    "paai4",
    "maa1",
    "gaa1",
    "gwong1",
    "gwong3",
    "zi1",
    "ci1",
    "ng5",
]


def test_decomposer_splits_jyutping_consonant_initial():
    split = build_decomposer(JYUTPING_SAMPLE, SchemaHints(tone_encoding="digits"))

    assert split("si1") == ("s", "i", "1")
    assert split("paai4") == ("p", "aai", "4")
    assert split("zi1") == ("z", "i", "1")


def test_decomposer_handles_two_char_initial_from_hints():
    hints = SchemaHints(tone_encoding="digits", recognized_initials={"gw"})
    split = build_decomposer(JYUTPING_SAMPLE, hints)

    assert split("gwong1") == ("gw", "ong", "1")


def test_decomposer_prefers_jyutping_nucleus_over_overlong_initial():
    hints = SchemaHints(
        tone_encoding="digits",
        recognized_initials={"s", "c", "j", "jyu", "k", "gw"},
        recognized_finals={"yu", "ong"},
    )
    split = build_decomposer(["syu1", "cyu1", "jyu1", "kyu1", "gwong1"], hints)

    assert split("syu1") == ("s", "yu", "1")
    assert split("cyu1") == ("c", "yu", "1")
    assert split("jyu1") == ("j", "yu", "1")
    assert split("kyu1") == ("k", "yu", "1")
    assert split("gwong1") == ("gw", "ong", "1")


def test_decomposer_prefers_aspirated_initial_before_composed_final():
    hints = SchemaHints(
        tone_encoding="digits",
        recognized_initials={"p", "ph", "t", "th", "ts", "tsh"},
        recognized_finals={"iau", "in"},
    )
    split = build_decomposer(["phiau1", "thin1", "tshiau1"], hints)

    assert split("phiau1") == ("ph", "iau", "1")
    assert split("thin1") == ("th", "in", "1")
    assert split("tshiau1") == ("tsh", "iau", "1")


def test_decomposer_handles_null_initial():
    split = build_decomposer(["aa1", "a3", "oi2"], SchemaHints(tone_encoding="digits"))

    assert split("aa1") == ("", "aa", "1")
    assert split("oi2") == ("", "oi", "2")


def test_decomposer_handles_syllabic_consonant_ng():
    hints = SchemaHints(tone_encoding="digits", recognized_initials={"ng"})
    split = build_decomposer(["ng5", "ngaa1", "ngo2"], hints)

    assert split("ng5") == ("ng", "", "5")


def test_decomposer_strips_letter_tone_from_overrides():
    hints = SchemaHints(
        tone_encoding="letters",
        tone_letters={"q", "r"},
        recognized_initials={"z"},
    )
    split = build_decomposer(["zaq", "zar", "zoq"], hints)

    assert split("zaq") == ("z", "a", "q")
    assert split("zar") == ("z", "a", "r")


def test_decomposer_strips_multi_digit_tones():
    hints = SchemaHints(tone_encoding="digits", recognized_initials={"p"})
    split = build_decomposer(["pai44", "pid55"], hints)

    assert split("pai44") == ("p", "ai", "44")
    assert split("pid55") == ("p", "id", "55")


def test_decomposer_strips_digits_before_checked_coda():
    hints = SchemaHints(tone_encoding="digits", recognized_initials={"m"}, recognized_finals={"ok"})
    split = build_decomposer(["mo4k"], hints)

    assert split("mo4k") == ("m", "ok", "4")


def test_decomposer_strips_contour_tones():
    hints = SchemaHints(tone_encoding="contours", recognized_initials={"z"})
    split = build_decomposer(["zaa˥˧", "zuk˨"], hints)

    assert split("zaa˥˧") == ("z", "aa", "˥˧")
    assert split("zuk˨") == ("z", "uk", "˨")


def test_decomposer_returns_none_on_unknown_spelling():
    split = build_decomposer(JYUTPING_SAMPLE, SchemaHints(tone_encoding="digits"))

    assert split("xyz") is None
