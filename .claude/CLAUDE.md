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

## Inline References (MANDATORY for all new content)

Every factual claim (numeric values, game mechanics, formulas, component specs) MUST include an inline reference verified against an authoritative source.

**Inline citation format:** `\hyperlink{ref-X.Y-N}{[N]}` where X.Y is the section number and N is sequential within that section.

**Reference definition format** (in a `## References` section at the bottom of each file):
```
\hypertarget{ref-X.Y-N}{[N]}. Aurora C# game database (AuroraDB.db v2.7.1) — [table_name] [field/details verified]
```

**Rules:**
- Use section-specific prefixes (`ref-8.3-`, `ref-14.1-`) to avoid PDF link ID collisions
- NEVER place `\hyperlink` references inside markdown headings — this causes TeX stack overflow. Place them on the line after the heading instead.
- Verify claims against `~/Downloads/Aurora271Full/AuroraDB.db` (SQLite) first; fall back to Aurora Forums / AuroraWiki
- Claims that cannot be verified against any authoritative source must be marked with `*(unverified)*` inline
- For forum-sourced references: `\hypertarget{ref-X.Y-N}{[N]}. Aurora Forums — [topic URL] — [description]`
- Keep reference numbers sequential within each file
- Each markdown file maintains its own References section

**Example:**
```markdown
Fuel Refineries cost 120 BP and require 120 Boronide per installation \hyperlink{ref-14.1-2}{[2]}

## References

\hypertarget{ref-14.1-2}{[2]}. Aurora C# game database (AuroraDB.db v2.7.1) — DIM_PlanetaryInstallation PlanetaryInstallationID=3 (Fuel Refinery). Cost=120 BP, Boronide=120.
```

## Build System

- **Build command:** `bash build-pdf.sh` (auto-increment) or `bash build-pdf.sh VERSION` (explicit)
- **PDF output:** `releases/aurora-manual-VERSION.pdf`
- **File list:** All source files must be listed in `build-pdf.sh` FILES array
- **Validation:** Build script validates all listed files exist before compilation
- **Releases:** PDFs are .gitignored; attach to GitHub releases via `gh release create`
- **Release versioning:** `vYYYY.MM.DD.##` where `##` is zero-padded (01, 02, etc.) and increments per release within a day

**IMPORTANT: Release version, PDF filename, AND PDF internal version MUST all match.**

When creating a release:

1. Check the next release number: `gh release list --limit 1`
2. Build the PDF with explicit version:
   ```bash
   bash build-pdf.sh 2026.01.28.07
   ```
3. Create the release with matching version:
   ```bash
   gh release create v2026.01.28.07 releases/aurora-manual-2026.01.28.07.pdf --title "..."
   ```

For development/testing builds, use `bash build-pdf.sh` without arguments (auto-increments).

## Game Database

- **Location:** `~/Downloads/Aurora271Full/AuroraDB.db` (SQLite)
- **Use:** Verify formulas, values, and mechanics claims against actual game data
- **Caution:** Values from YouTube videos or forum posts should be cross-checked against the database when possible

## Issue Workflow

- Group related issues into parallel waves for background agents
- Close issues with commit reference comments
- Push all commits before closing issues
- Build PDF and create GitHub release after completing a wave

## README Maintenance

**Keep README.md synchronized with project state.** Check and update when:

1. **Game version changes** — Update the version number in both locations:
   - Line 5: "This manual covers Aurora C# vX.Y.Z"
   - Community Review section: "This manual covers Aurora C# vX.Y.Z"
   - Must match the database version cited in references (currently v2.7.1)

2. **Section structure changes** — Update the Structure table if:
   - New chapters are added
   - Chapter descriptions change significantly
   - Sections are renamed or reorganized

3. **Build system changes** — Update the "Building the PDF" section if:
   - New dependencies are added
   - Build commands change
   - New build options are added

4. **New contributors** — Add to Contributors section (see Contributor Attribution below)

5. **New YouTube sources** — Add to YouTube Tutorial Credits (see YouTube Source Attribution above)

**Version consistency rule:** The README version, database references throughout the manual, and the Game Database section in this file must all reference the same Aurora version.

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
