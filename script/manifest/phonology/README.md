# Phonology Extraction

`script/build_phonology.py` derives best-effort phonology data from each
schema's own Rime files:

1. Resolve `<schema_id>.schema.yaml`.
2. Read `translator.dictionary`.
3. Resolve `<dictionary>.dict.yaml`.
4. Filter the dictionary body to single-character rows.
5. Split each spelling into initial, final, and tone.
6. Emit a compact build-time summary plus lazy-loaded public JSON assets.
7. Join the empirical inventory against `script/phonology_ipa_dictionary.yaml`
   to produce broad-IPA grids for initials and finals when coverage is high
   enough.

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

## IPA grid calibration

`script/phonology_ipa_dictionary.yaml` stores cross-scheme defaults for broad
IPA classification. Use `script/phonology_overrides.yaml` when one scheme needs
a local correction:

```yaml
overrides:
  wugniu_soutseu:
    initials_ipa:
      b: { ipa: "b", place: bilabial, manner: plosive }
    nuclei_ipa:
      eq: { ipa: "əʔ", label: "eq" }
```

Use `suppress_grids: true` for schemes where an IPA consonant/vowel chart would
be misleading, such as Old Chinese reconstruction spellings or script-oriented
Sinoxenic schemes. Suppressed schemes still keep `字音對照`; they simply render
placeholders for `聲母表` and `韻母表`.

## Second-scheme schemas

Schemas in the `konny_` series reuse the base `gannyu_` dictionary, which
stores first-scheme codes. Their second-scheme spellings live in
`lua/konny_<region>_scheme2.lua`. For these schemas the compiler:

1. resolves the base schema's overrides, whose `initials_ipa` and `finals_ipa`
   values come from the dictionary IPA;
2. reads the base spelling map from `lua/konny_<region>_scheme2.lua`;
3. projects each base initial and final IPA through
   `script/phonology_scheme2.tsv`; and
4. rewrites the single-character rows to second-scheme spellings before
   splitting them.

`script/phonology_scheme2.tsv` mirrors the Gonnyu transcription table. Update
both copies together when the second-scheme spelling rules change. A `konny_`
schema is skipped when the base overrides or the spelling map is unavailable.
