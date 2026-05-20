import pytest

from manifest.detect_orphans import detect_orphans, OrphanError


def test_no_orphans_when_all_ids_covered():
    readme_ids = {"jyutping", "wugniu_soutseu"}
    manifest_ids = {"jyutping", "wugniu_soutseu"}
    # Should not raise.
    detect_orphans(readme_ids, manifest_ids)


def test_orphans_raise_with_listing():
    readme_ids = {"jyutping", "wugniu_soutseu", "dkzp", "kuankhiunn"}
    manifest_ids = {"jyutping", "wugniu_soutseu"}
    with pytest.raises(OrphanError) as info:
        detect_orphans(readme_ids, manifest_ids)
    msg = str(info.value)
    assert "dkzp" in msg
    assert "kuankhiunn" in msg


def test_extras_in_manifest_are_ignored():
    # Schemas present in manifest but NOT in README are fine — manifest is the
    # source of truth for what ships on the site; README is only used to ensure
    # nothing is silently dropped.
    readme_ids = {"jyutping"}
    manifest_ids = {"jyutping", "wugniu_soutseu"}
    detect_orphans(readme_ids, manifest_ids)
