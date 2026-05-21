import manifestJson from "./schemas.json";
import type { Branch, Dialect, Manifest, SchemaEntry, SchemaId } from "./types";

const MANIFEST = manifestJson as Manifest;

export function getManifest(): Manifest {
  return MANIFEST;
}

export function getSchema(id: SchemaId): SchemaEntry {
  const schema = MANIFEST.schemas[id];
  if (!schema) {
    throw new Error(`Schema not found: ${id}`);
  }
  return schema;
}

export function getSchemaBySlug(slug: string): SchemaEntry {
  const schema = Object.values(MANIFEST.schemas).find((entry) => entry.slug === slug);
  if (!schema) {
    throw new Error(`Schema slug not found: ${slug}`);
  }
  return schema;
}

export function getSchemaSlugs(): string[] {
  return Object.values(MANIFEST.schemas).map((schema) => schema.slug);
}

export function getBranchByKey(key: string): Branch {
  const branch = MANIFEST.branches.find((entry) => entry.key === key);
  if (!branch) {
    throw new Error(`Branch not found: ${key}`);
  }
  return branch;
}

export function getDialectForSchema(id: SchemaId): { branch: Branch; dialect: Dialect } | null {
  for (const branch of MANIFEST.branches) {
    for (const dialect of branch.dialects) {
      if (dialect.schemas.includes(id)) {
        return { branch, dialect };
      }
    }
  }
  return null;
}

export function getSiblingSchemas(id: SchemaId): SchemaEntry[] {
  const found = getDialectForSchema(id);
  if (!found) return [];
  return found.dialect.schemas
    .filter((schemaId) => schemaId !== id)
    .map((schemaId) => MANIFEST.schemas[schemaId])
    .filter((schema): schema is SchemaEntry => Boolean(schema));
}

export function schemasForDialect(dialect: Dialect): SchemaEntry[] {
  return dialect.schemas.map(getSchema);
}

export function branchSchemaCount(branch: Branch): number {
  return branch.dialects.reduce((sum, dialect) => sum + dialect.schemas.length, 0);
}

export function branchRecipeCount(branch: Branch): number {
  const recipes = new Set<string>();
  for (const dialect of branch.dialects) {
    for (const id of dialect.schemas) {
      const recipe = MANIFEST.schemas[id]?.recipe;
      if (recipe) recipes.add(recipe);
    }
  }
  return recipes.size;
}

export function countRecipeSchemas(): number {
  return Object.values(MANIFEST.schemas).filter((schema) => Boolean(schema.recipe)).length;
}

export function countDownloadableSchemas(): number {
  return Object.values(MANIFEST.schemas).filter((schema) => schema.downloadable).length;
}
