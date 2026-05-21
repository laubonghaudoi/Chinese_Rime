export interface Manifest {
  generated_at: string;
  stats: ManifestStats;
  branches: Branch[];
  schemas: Record<SchemaId, SchemaEntry>;
}

export interface ManifestStats {
  schema_count: number;
  recipe_count: number;
  download_package_count: number;
  branch_count: number;
  active_branch_count: number;
  missing_branch_count: number;
}

export type BranchStatus = "active" | "missing" | "synthetic";
export type SchemaId = string;

export interface Branch {
  key: string;
  name: string;
  iso_639_3: string;
  intro: string;
  status: BranchStatus;
  dialects: Dialect[];
}

export interface Dialect {
  name: string;
  schemas: SchemaId[];
}

export interface SchemaEntry {
  schema_id: SchemaId;
  slug: string;
  display_name: string;
  branch: string | null;
  dialect: string | null;
  authors: string[];
  version: string;
  description: string;
  dependencies: string[];
  license: string | null;
  recipe: string | null;
  upstream_url: string | null;
  last_commit_at: string | null;
  downloadable: boolean;
  download_package: string | null;
}

export interface PhonologyRow {
  spelling: string;
  example_chars: string[];
  syllable_count: number;
  char_count: number;
}

export interface PhonologyTone {
  value: string;
  example_chars: string[];
  syllable_count: number;
  char_count: number;
}

export interface PhonologySyllable {
  char: string;
  spellings: string[];
}

export interface PhonologyStats {
  total_chars: number;
  total_syllables: number;
  single_char_rows: number;
  undecomposable_syllables: number;
}

export interface PhonologySummaryEntry {
  schema_id: SchemaId;
  display_name: string;
  asset_path: string;
  tone_encoding: "digits" | "diacritics" | "letters" | "none";
  initials: PhonologyRow[];
  finals: PhonologyRow[];
  tones: PhonologyTone[];
  preview_syllables: PhonologySyllable[];
  stats: PhonologyStats;
  status: "ok" | "partial";
}

export interface PhonologySummary {
  generated_at: string;
  schemas: Record<SchemaId, PhonologySummaryEntry>;
  skipped: Record<SchemaId, { reason: string }>;
}

export interface PhonologyFull extends PhonologySummaryEntry {
  dictionary: string;
  source_paths: {
    schema: string;
    dict: string;
  };
  syllable_index: PhonologySyllable[];
}
