import { describe, expect, it } from "vitest";

import {
  branchSchemaCount,
  getDialectForSchema,
  getManifest,
  getPhonologySummary,
  getSchema,
  getSchemaBySlug,
  getSchemaSlugs,
  getSiblingSchemas,
  hasPhonology
} from "../loader";

describe("manifest loader", () => {
  it("loads manifest stats, branches, and schemas", () => {
    const manifest = getManifest();
    expect(manifest.stats.schema_count).toBe(Object.keys(manifest.schemas).length);
    expect(manifest.branches.length).toBeGreaterThan(0);
  });

  it("looks up schemas by id and slug", () => {
    const first = Object.values(getManifest().schemas)[0];
    expect(getSchema(first.schema_id).slug).toBe(first.slug);
    expect(getSchemaBySlug(first.slug).schema_id).toBe(first.schema_id);
  });

  it("returns one route slug per schema", () => {
    expect(getSchemaSlugs()).toHaveLength(getManifest().stats.schema_count);
  });

  it("places every schema in exactly one branch dialect", () => {
    const manifest = getManifest();
    const treeIds = manifest.branches.flatMap((branch) =>
      branch.dialects.flatMap((dialect) => dialect.schemas)
    );
    expect(new Set(treeIds).size).toBe(Object.keys(manifest.schemas).length);
    expect(treeIds.every((id) => Boolean(manifest.schemas[id]))).toBe(true);
  });

  it("finds siblings from the same dialect", () => {
    const manifest = getManifest();
    const dialect = manifest.branches.flatMap((branch) => branch.dialects).find((d) => d.schemas.length > 1);
    expect(dialect).toBeDefined();
    const first = dialect!.schemas[0];
    expect(getDialectForSchema(first)?.dialect.name).toBe(dialect!.name);
    expect(getSiblingSchemas(first).some((schema) => schema.schema_id === first)).toBe(false);
  });

  it("counts schemas in a branch", () => {
    const branch = getManifest().branches.find((entry) => entry.status !== "missing")!;
    expect(branchSchemaCount(branch)).toBeGreaterThan(0);
  });

  it("loads compact phonology summaries without requiring full public assets", () => {
    const summary = getPhonologySummary("jyutping");
    expect(summary?.asset_path).toBe("/phonology/jyutping.json");
    expect(summary?.grid_status).toBe("ok");
    expect(summary?.initials_grid?.cells.plosive.bilabial[0].spelling).toBe("b");
    expect(summary?.finals_grid?.cells["i|"][0].spelling).toBe("i");
    expect(summary?.preview_syllables.length).toBeGreaterThan(0);
    expect(hasPhonology("jyutping")).toBe(true);
    expect(getPhonologySummary("__missing__")).toBeNull();
    expect(hasPhonology("__missing__")).toBe(false);
  });
});
