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
