# Aurora 4X Manual - Project Instructions

## Project Overview

This is a comprehensive reference manual for Aurora C# (space strategy game by Steve Walmsley). The manual is written in Markdown, organized by numbered sections, and compiled to PDF via `build-pdf.sh` using pandoc + tectonic.

## Game Fundamentals

- **Turn-based, not real-time:** Aurora advances time only when the player clicks an increment button (5 sec, 30 sec, 5 min, etc.). There is no "pause" — time never runs automatically.
- **Conventional start:** Earth in 2025 with existing population, installations, and officers
- **Space start:** Single ship, minimal resources, no established infrastructure

## YouTube Source Attribution

**MANDATORY:** When extracting content from YouTube videos for manual updates:

1. **Issue Creation:** Every issue sourced from a YouTube video MUST include:
   - The video title and URL in the issue body under "## Source"
   - A comment on the issue crediting the creator: `**Source Credit:** [Creator Name](channel_url) — description`

2. **README Credits:** After creating YouTube-sourced issues, update `README.md`:
   - Add the creator to the "YouTube Tutorial Credits" subsection under Sources (if not already listed)
   - Add the creator to the "Contributors" section (if not already listed)

3. **Identifying Creators:** Use `yt-dlp --print channel --print channel_url <URL>` to get the official channel name and URL.

## Content Standards

- **Section numbering:** Decimal hierarchy (e.g., 8.2.1 is a heading within file 8.2)
- **Cross-references:** Always use `[Section X.Y Title](../path/to/file.md)` format — never bare "see Section X.Y"
- **Version tags:** New sections get `*Added: v2026.01.24*` after the top heading
- **Callouts:** Use `> **Tip:**`, `> **Note:**`, `> **Warning:**` blockquote format
- **Tables:** Ensure blank lines before and after tables for pandoc compatibility

## Build System

- **Build command:** `bash build-pdf.sh`
- **PDF output:** `releases/aurora-manual-YYYY.MM.DD.SEQ.pdf` (SEQ auto-increments per build)
- **File list:** All source files must be listed in `build-pdf.sh` FILES array
- **Validation:** Build script validates all listed files exist before compilation
- **Releases:** PDFs are .gitignored; attach to GitHub releases via `gh release create`
- **Release versioning:** `vYYYY.MM.DD.##` where `##` is zero-padded (01, 02, etc.) and increments per release within a day (not per build)

## Game Database

- **Location:** `~/Downloads/Aurora271Full/AuroraDB.db` (SQLite)
- **Use:** Verify formulas, values, and mechanics claims against actual game data
- **Caution:** Values from YouTube videos or forum posts should be cross-checked against the database when possible

## Issue Workflow

- Group related issues into parallel waves for background agents
- Close issues with commit reference comments
- Push all commits before closing issues
- Build PDF and create GitHub release after completing a wave

## Contributor Attribution

All repo contributors must appear in three locations:

1. **README.md** — Contributors section: `- **[@username](https://github.com/username)**`
2. **1-introduction/1.1-what-is-aurora.md** — Manual Contributors list (ensures they appear in PDF)
3. **Release notes** — Contributors section when creating releases

To get the current contributor list: `gh api repos/ErikEvenson/aurora-manual/contributors --jq '.[].login'`

## LaTeX Compatibility

- Avoid Unicode symbols that don't render in LaTeX (e.g., use `<=` instead of `≤`)
- Long tables may overflow; consider breaking into multiple tables or using shorter column content

## SVG Images

SVG images are supported via automatic conversion:

- **Source:** Place `.svg` files in `images/tech-trees/`
- **Generated:** Build script converts to PDF in `images/.generated/` (gitignored)
- **Reference in markdown:** `![Caption](../images/.generated/filename.pdf)`
- **Conversion tool:** `rsvg-convert` (must be installed)
- **Tech tree generation:** Use Graphviz DOT format, convert with `dot -Tsvg`

The build script only reconverts if the SVG is newer than the PDF.
