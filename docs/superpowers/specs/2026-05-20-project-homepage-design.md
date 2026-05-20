---
title: 中州韻方案集 site — v1 design
status: drafted
author: laubonghaudoi (with Claude)
date: 2026-05-20
---

# 中州韻方案集 site — v1 design

A static GitHub Pages site that presents the entire Chinese_Rime collection as a navigable catalog of 144 schemas across 17 active language branches, with a per-schema placeholder page for each `schema_id`. v1 ships the catalog and supporting static pages; per-schema phonology tables and sample-text content are deferred to a later milestone.

## 1. Goals & non-goals

**Goals**
- Serve the project's three audiences from a single homepage: native speakers looking to type, learners practicing pronunciation, and researchers using the project as a reference.
- Render the full collection — every `schema_id` known to the project — as an inline-browseable tree, plus one detail URL per schema (`/schemas/<schema-id>/`).
- Keep the catalog and per-schema pages in sync with upstream submodules automatically, via the existing biweekly update workflow.
- Establish a visual system ("scholar + modern tech") that is readable at high content density and stays consistent across all pages.
- Architect for later English translation without shipping translations in v1.

**Non-goals (v1)**
- Per-language and per-dialect landing pages (deferred; covered as anchor sections inside `/catalog/`).
- Populated phonology tables on per-schema pages. **Four layout placeholder sections (聲母表 / 韻母表 / 聲調 / 字音對照) ship in v1** as separate top-level H2 sections, each with `即將推出` badging and a striped band. The actual data extraction (parsing each `*.schema.yaml` for initials, finals, tones, syllable mapping) is deferred to v2. Reference for the eventual format: [jyutping.org/jyutping/](https://jyutping.org/jyutping/).
- Side-by-side schema comparison view.
- Live web-based typing demo.
- Client-side full-text search (Pagefind or otherwise).
- English routes / shipped translations.
- RSS / changelog feeds, per-recipe pages, dialect slug curation.

## 2. Architecture

**Stack.** Astro static-site generator, built with `pnpm`, deployed to GitHub Pages via GitHub Actions. The Astro project lives at `site/` inside the existing `Chinese_Rime` repo — no separate repo.

**Repository layout**

```
Chinese_Rime/
├── site/                                # NEW — Astro project
│   ├── astro.config.mjs
│   ├── package.json
│   ├── pnpm-lock.yaml
│   ├── src/
│   │   ├── pages/                       # routes
│   │   ├── components/                  # Brand, Chop, FilterChips, SchemaRow…
│   │   ├── layouts/                     # BaseLayout, CatalogLayout, SchemaLayout
│   │   ├── data/
│   │   │   └── schemas.json             # ← generated manifest (committed)
│   │   ├── styles/                      # tokens.css, base.css
│   │   └── content/                     # MDX prose for home, about, install, …
│   └── public/
│       ├── brand/
│       │   └── logo.svg                 # 印 chop — swappable single asset
│       └── fonts/                       # if self-hosted
├── script/
│   ├── build_manifest.py                # NEW — manifest builder
│   ├── manifest_overrides.yaml          # NEW — orphan-schema overrides
│   ├── source_info.yaml                 # existing
│   ├── update_download.py               # existing
│   └── update_submodules.sh             # existing
├── .github/workflows/
│   ├── regular_update.yml               # existing — extended with manifest step
│   └── deploy_pages.yml                 # NEW — Astro build + Pages deploy
├── .gitignore                           # NEW — excludes .superpowers/ + site build artifacts
└── …existing dirs (sources/, download/, unmaintained/)…
```

**Data flow**

```
submodules + source_info.yaml + manifest_overrides.yaml
                          │
                          ▼
            script/build_manifest.py
                          │
                          ▼
   site/src/data/schemas.json (committed)
                          │
                          ▼
        Astro build (deploy_pages.yml)
                          │
                          ▼
                  GitHub Pages
```

The manifest is the single source of truth for the site. Submodules are *not* checked out during Pages builds; the build is fast, deterministic, and reviewable via the manifest diff in PRs.

## 3. Data pipeline

`script/build_manifest.py` runs in three passes:

1. **Walk submodules.** For each `*.schema.yaml` under `sources/<語系>/<recipe>/`, parse the YAML and extract: `schema_id`, `name`, `version`, `author`, `description`, `dependencies`. Derive the language family from the immediate parent directory of the recipe. Record the upstream repo URL from the submodule's `.gitmodules` entry.
2. **Join `source_info.yaml`.** For each download-package key (`<語系>/<dialect>/<…>`), record which schemas it bundles and the file list. A schema_id is `downloadable: true` iff it appears in any download package's `files:` list.
3. **Merge `manifest_overrides.yaml`.** For README-listed schemas that have no submodule (e.g. `dkzp`, `kuankhiunn`), pull the fields from this hand-maintained file. The overrides file also contains: ISO 639-3 mapping per language branch, dialect-name assignment per schema, and any field-level corrections.

**Output schema** (`site/src/data/schemas.json`):

```json
{
  "generated_at": "2026-05-20T14:08:11Z",
  "branches": [
    {
      "key": "yue",
      "name": "粵語",
      "iso_639_3": "yue",
      "intro": "粵語區的拼音輸入方案，以廣州話為主。",
      "dialects": [
        {
          "name": "廣州話",
          "schemas": ["jyutping", "jyutping-plus", "zyujam"]
        }
      ]
    }
  ],
  "schemas": {
    "jyutping": {
      "schema_id": "jyutping",
      "display_name": "粵拼",
      "branch": "yue",
      "dialect": "廣州話",
      "authors": ["佛振", "LeiMaau", "劉邦後代"],
      "version": "0.15",
      "description": "採用香港語言學會粵語拼音方案，兼容教育學院拼音方案。碼表源自 scim-table-zh。",
      "dependencies": ["luna_pinyin", "stroke", "cangjie5"],
      "license": "CC BY 4.0",
      "recipe": "rime/rime-jyutping",
      "upstream_url": "https://github.com/rime/rime-jyutping",
      "last_commit_at": "2025-11-30T08:14:00Z",
      "downloadable": true,
      "download_package": "粵語/廣州話"
    }
  }
}
```

**Schema slug sanitization.** `schema_id` → URL slug uses minimal substitution: `+` → `-plus`. All other characters pass through unchanged (`OC_baxter-sagart` stays as-is).

**Orphan handling.** Any schema in README but missing from submodules + overrides surfaces a build error from `build_manifest.py`. The build does not proceed silently.

## 4. Information architecture & routes

**Static routes** (hand-authored MDX in `site/src/content/`):

| Route | Purpose |
|---|---|
| `/` | Homepage — wordmark, three audience paths, distribution chart, footer |
| `/catalog/` | The whole tree — 17 language sections, dialect groups, schema rows |
| `/about/` | Mission, ISO 639-3 classification table, how to read the catalog |
| `/install/` | General Rime + plum install guide, then how to deploy a downloaded package |
| `/resources/` | White papers, tutorials, dictionaries (mirrors README §資源) |
| `/contribute/` | How to submit a new schema (distilled from `AGENT.md`) |
| `/acknowledgments/` | Contributor list (mirrors README §致謝) |

**Generated routes** — one per manifest schema (≈144 today): `/schemas/<schema-id>/`.

**Anchor strategy inside `/catalog/`**
- Language anchors: ISO 639-3 code, clean. `/catalog/#yue`, `/catalog/#wuu`.
- Dialect anchors: auto-generated Chinese heading IDs. `/catalog/#廣州話` — URL-encoded in the address bar, but functional and chat-preview-friendly.
- No `dialect_slugs.yaml`. If pretty romanized dialect URLs are wanted later, add then.

**Total v1 page count.** 7 static + ≈144 generated = **≈151 pages**, all rendered to static HTML at build time.

**Language toggle.** None in v1. The architecture reserves i18n hooks (e.g., route prefix, content-collection locale tag) but no English content is shipped.

**Counts in this document are illustrative.** All concrete numbers — `144 個方案`, `60 個配方`, `80 個下載包`, `17 個語系`, `仍待收錄 N 支` — are derived from the manifest at build time and rendered into the page templates. The spec's example numbers reflect the project's current state but should not be hard-coded into components.

## 5. Page-level designs

### 5.1 Homepage (`/`)

Sequence top-to-bottom:

1. **Nav.** `<Brand />` (chop + wordmark) on the left, 6 nav links on the right (`方案目錄`, `安裝`, `關於`, `資源`, `致謝`, `貢獻`). The active route gets a 朱紅 bottom border.
2. **Hero.** Two columns. Left: 76 px Noto Serif TC wordmark `中州韻 / 方案集`, one-paragraph Chinese lede, two CTAs (primary 朱紅 `瀏覽方案目錄`, outlined ink `如何安裝`). Right: 4-cell stat grid (144 個方案 / 60 個配方 / 17 個語系 / 80 個下載包), labels in Noto Sans TC, numerals in IBM Plex Sans with tabular-nums.
3. **Audience paths.** Section label `為三類讀者`. Three numbered cards: `01 找到母語方案`, `02 練習正音正字`, `03 對照與引用`. Card content is placeholder copy — to be revised after implementation.
4. **Distribution chart.** Section label `收錄分佈`, H2 `各語系方案數量`, explainer `下圖依方案數量降序排列；斜線格表示尚待收錄之語系。` All language branches in the manifest arranged in two columns of horizontal bars, sorted descending by count. Each row: Chinese branch name + ISO 639-3 code (朱紅 mono) + ink-black bar + count. No 朱紅 highlight on leading bars (all bars uniform). 暫缺 branches render with a diagonally-striped placeholder where the bar would be.
5. **Footer.** Ink-black bg. Left: `© 中州韻方案集` + license code `CC BY 4.0` (mono). Right: `源碼倉庫`, `貢獻指南`, `版本發佈` links.

### 5.2 Catalog (`/catalog/`)

Sequence:

1. **Nav.** Same as homepage.
2. **Page header.** Section label `收錄總覽`, H1 `方案目錄`, two-sentence intro, summary line `共收錄 144 個方案、60 個配方、80 個下載包，涵蓋 17 個語系，仍待收錄 4 支。`
3. **Filter chips** (sticky on scroll). `全部`, `℞ 限配方`, `限可下載`, `含暫缺`. Each carries its count in IBM Plex Sans tabular numerals. Active chip flips to ink-black bg with white text. No borders; chip default fill is `#ecebe6`.
4. **Main grid.** Two columns: tree (left, flex) + sticky TOC sidebar (right, 220 px).
   - **Each language section** is a `<section id="<iso>">`. H2 (30 px, weight 700) shows ISO code (朱紅 mono) + Chinese name + count summary (right-aligned, e.g. `13 個方案 · 8 個配方`), with a 2 px ink bottom border.
   - **Dialect groups** as H3 (22 px Noto Serif TC, weight 700), followed by an inline `<meta>` count (e.g. `3 個方案`).
   - **Schema rows** are compact two-line links. Layout: 1 px ink left rail (4 px in 朱紅 on hover) + a content column containing (row 1) display name (Noto Serif TC 15.5 px) + schema_id (朱紅 IBM Plex Mono 11.5 px) + ℞ badge if recipe + 下載 badge if downloadable, and (row 2) the one-line description from upstream `description`, plus a right-arrow at the row end. Hover state lifts background to `#fff` and shifts left-padding 4 px.
   - **暫缺 sections** keep the same H2 treatment with a 暫缺 badge in the count slot and an italicized `尚待收錄` note instead of dialect content.
   - **TOC sidebar.** Sticky, 17 entries. Each: Chinese name + ISO code (朱紅 mono) + count (right-aligned tabular). Active section bolded ink-black.
5. **Footer.** Same as homepage.

### 5.3 Per-schema page (`/schemas/<schema-id>/`)

Sequence:

1. **Nav.** Same.
2. **Breadcrumb.** `方案目錄 / <語系> / <方言> / <方案名>` with 朱紅 separator slashes. Last segment is plain text (current page).
3. **Hero.** Single column. 64 px Noto Serif TC display name. Below it on one row: schema_id pill (朱紅 mono on tinted bg), `℞ 配方` badge (if recipe), `可下載` badge (if downloadable). Below: one-paragraph tagline (Noto Serif TC 17 px) drawn from the schema's `description` field. CTAs: primary 朱紅 `下載安裝包` (only rendered if `downloadable`), outlined ink `前往上游倉庫 →`.
4. **Meta data sheet.** 4-column × 2-row grid (8 fields total): top row `語系` (+ ISO) / `方言` / `配方` (linked to upstream) / `作者`. Bottom row `版本` / `授權` / `最後更新` (last-touched commit date) / `依賴`. Labels in spaced Noto Sans TC 11 px; values in Noto Serif TC 18 px (mono variant for `版本`, `授權`, `最後更新`, `依賴`).
5. **方案說明.** Full `description` rendered as paragraph(s).
6. **如何取得.** Two cards side-by-side. Card A: `透過 plum 安裝` with an ink-black mono code block (`bash rime-install <recipe>`) and a copy button. Card B: `從本站下載整合包` with a link to the download zip and the last-update date in parens. If `downloadable: false`, card B is replaced by `從上游倉庫下載` linking directly to GitHub.
7. **聲母表 (placeholder for v2).** Section label `音系資料 · 01`, H2 `聲母表` with a 朱紅 `即將推出` badge. One-sentence intro: `所有聲母及其對應之 IPA 與例字，將於下一版本加入。` Below: a diagonally-striped placeholder band labeled `data · v2`.
8. **韻母表 (placeholder for v2).** Section label `音系資料 · 02`, H2 `韻母表` with a 朱紅 `即將推出` badge. One-sentence intro: `所有韻母按韻尾分組，附 IPA 與例字。` Striped band beneath.
9. **聲調 (placeholder for v2).** Section label `音系資料 · 03`, H2 `聲調` with a 朱紅 `即將推出` badge. One-sentence intro: `全部聲調之調值、調類與例字。` Striped band beneath.
10. **字音對照 (placeholder for v2).** Section label `音系資料 · 04`, H2 `字音對照` with a 朱紅 `即將推出` badge. One-sentence intro: `常用字之拼寫與發音對照查詢。` Striped band beneath.
11. **更多 \<dialect\> 方案.** Sibling-schema chips (3-column grid) for other schemas under the same dialect. Same left-rail hover treatment as the catalog row. Section is omitted when there are no siblings.
12. **Footer.** Same.

**Why four separate H2 sections instead of one grouped section.** The visual structure matches jyutping.org's linearized layout, and in v2 each section will host a full table that needs its own room. Grouping the labels with `音系資料 · 01–04` communicates they belong together while keeping each as a real top-level section.

**TODO (v2):** populate sections 7–10 with real data extracted from each `*.schema.yaml`. Each requires a parser for the scheme's spelling algorithm — non-trivial; out of scope for v1 and the largest single v2 effort.

## 6. Visual system

**Typography**

| Use | Font | Sizes |
|---|---|---|
| Chinese display & body | Noto Serif TC (400/500/700/800) | H1 54–76 · H2 28–30 · H3 22 · body 15.5–17 · lede 17–18 |
| Chinese labels & UI | Noto Sans TC (300/400/500/700) | nav 13.5 · label 11–12 · chip 13 |
| Latin body & UI | IBM Plex Sans (400/500/600/700) | stat numerals 36–44 · summary 13 |
| Latin data & code | IBM Plex Mono (400/500/600) | schema_id 11–14 · spaced label 10–11 · code block 12.5 |
| Latin display (sparing) | IBM Plex Serif (500/700) | reserved for /about/ |

All fonts loaded from Google Fonts with `display=swap` and a system fallback chain.

**Color tokens**

| Token | Hex | Usage |
|---|---|---|
| `--bg-page` | `#cfcfcf` | outer page background |
| `--bg-panel` | `#fafafa` | primary section panels |
| `--bg-elev` | `#ffffff` | nav, filter row, install cards, related cards |
| `--bg-chip` | `#ecebe6` | default chip fill |
| `--bg-stripe` | `repeating-linear-gradient(45deg, #ececec 0 6px, #fafafa 6px 12px)` | 暫缺 cells |
| `--ink` | `#0a0a0a` | text, ink rails, footer bg, chop neutral |
| `--ink-soft` | `#1a1a1a` | body prose |
| `--ink-meta-2` | `#444` | secondary copy |
| `--ink-meta-3` | `#666` | tertiary copy |
| `--ink-meta-4` | `#888` | quaternary copy / disabled |
| `--zhu` (朱紅) | `#b8281f` | chop bg, primary CTA bg, schema_id text, ISO codes, active hover rail, active chip text |
| `--zhu-tint` | `rgba(184,40,31,.10)` | recipe badge bg, schema_id pill bg |

**No light-gray borders anywhere.** Surfaces separate by background-color contrast. Only borders that exist: ink-black 1 px (schema-row left rail), ink-black 2 px (H2 underlines), 朱紅 0–4 px (hover state on schema rows and nav-active underline).

**Spacing.** Section horizontal padding 36 px (desktop). Section vertical padding 36–54 px top, 24–60 px bottom (heavier on hero/page-head). Card padding 22–32 px. Schema row vertical 11 px; rail-to-content gutter 14 px → 18 px on hover.

**Component inventory** (each becomes a `.astro` component under `site/src/components/`):

`<Brand />` · `<Chop />` (swappable SVG via `site/public/brand/logo.svg`) · `<NavLinks />` · `<Breadcrumb />` · `<FilterChips />` · `<LanguageSection />` · `<DialectGroup />` · `<SchemaRow />` · `<SchemaBadge />` (variant: recipe / downloadable / empty) · `<MetaSheet />` · `<InstallCommand />` · `<DistributionChart />` · `<SidebarTOC />` · `<Footer />`.

## 7. Build & deploy pipeline

**Three moving parts**

1. **`script/build_manifest.py`** — Python 3, uses `pyyaml`. Reads submodule schema YAMLs + `source_info.yaml` + `manifest_overrides.yaml`. Writes `site/src/data/schemas.json`. Re-runnable locally without arguments.
2. **`.github/workflows/regular_update.yml`** (extended) — current biweekly cron + manual dispatch. Existing steps unchanged. New step appended after `update_download.py`: `python3 script/build_manifest.py`. The manifest diff lands in the same biweekly commit as submodule pointer updates.
3. **`.github/workflows/deploy_pages.yml`** (new) — triggers: `push` to `master` and `workflow_dispatch`. Steps:
   - `actions/checkout@v4` (no `submodules: true` — manifest is committed).
   - `pnpm/action-setup@v3` + `actions/setup-node@v4` with Node 20.
   - Cache pnpm store and `site/.astro/`.
   - `pnpm install --frozen-lockfile` in `site/`.
   - `pnpm --filter site build`.
   - `actions/configure-pages@v5`, `actions/upload-pages-artifact@v3` with `path: site/dist`, `actions/deploy-pages@v4`.

**Cache strategy.** pnpm store keyed on `pnpm-lock.yaml` hash. `site/.astro/` keyed on the content-collection inputs (schema manifest hash + content/ hash).

**Failure modes.** Manifest builder failures block the biweekly auto-update commit; site build failures block deploy. Both surface in the GitHub Actions tab.

## 8. Risks & open items

- **English content scoping.** Architecture reserves i18n hooks but ships zero English. Risk: if English routes come within ~3 months, hooks may not match the actual translation workflow. Mitigation: keep i18n scaffolding minimal and revisit at translation time.
- **Manifest overrides drift.** `manifest_overrides.yaml` is hand-maintained for orphan schemas. Risk: it falls out of sync with the README when new orphans are added without updating the file. Mitigation: `build_manifest.py` emits a build error for any README-listed schema that lacks both submodule data and an override.
- **Distribution chart counts.** The chart numbers reflect manifest data. If `manifest_overrides.yaml` undercounts orphans (e.g. for a language with several README-listed schemas not in submodules), the chart underrepresents the project. Same mitigation as above.
- **Sticky filter chips with sticky TOC.** Two sticky elements on the same page can collide on narrow viewports. Mitigation: TOC is hidden on viewports < 1024 px; filter chips remain sticky.
- **Audience-path card copy.** Current text is placeholder; user has indicated revision will come post-implementation. Risk: shipping with placeholder copy. Mitigation: track as an explicit pre-launch checklist item.

## 9. Future milestones (v2+)

In rough priority order (subject to revision):
1. **Populate the four 音系資料 sections** on per-schema pages — fill in the v1 layout placeholders for 聲母表, 韻母表, 聲調, and 字音對照 with data extracted from each `*.schema.yaml`. Reference layout: [jyutping.org/jyutping/](https://jyutping.org/jyutping/). Requires a per-scheme spelling-algorithm parser; non-trivial and the largest single v2 effort.
2. **Spelling samples** (`拼寫示例`) on per-schema pages — common words and sentences in the scheme.
3. **Per-language landing pages** (`/languages/<iso>/`) with history, dialect map, recommended schema.
4. **English translation** — toggle in header, parallel content collection, route prefix.
5. **Pagefind search** — top-bar search box for schemas by name, ID, author.
6. **Side-by-side comparison view** — pick two schemas, render their phonology tables next to each other.
7. **Live typing demo** — embedded Rime web demo per schema.
