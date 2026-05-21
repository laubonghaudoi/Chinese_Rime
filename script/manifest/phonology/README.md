# Phonology Extraction

`script/build_phonology.py` derives best-effort phonology data from each
schema's own Rime files:

1. Resolve `<schema_id>.schema.yaml`.
2. Read `translator.dictionary`.
3. Resolve `<dictionary>.dict.yaml`.
4. Filter the dictionary body to single-character rows.
5. Split each spelling into initial, final, and tone.
6. Emit a compact build-time summary plus lazy-loaded public JSON assets.

The splitter is intentionally conservative. It strips tones from trailing
digits, configured trailing tone letters, or vowel diacritics, then infers
initials from observed consonant prefixes and schema algebra hints. When a
scheme has unusual spelling conventions, add an entry to
`script/phonology_overrides.yaml`:

```yaml
overrides:
  wugniu_soutseu:
    tone_encoding: letters
    tone_letters: ["q", "r", "h"]
    extra_initials: ["gn", "ng"]
```

Common failure signs:

- unexpectedly high `undecomposable_syllables`
- a wrong tone count
- obvious initials split into one-letter fragments
- historical reconstructions producing too many final-like strings

Use overrides for mechanical spelling conventions only. Do not add
hand-curated phonology tables here; the site should remain generated from the
scheme files.
