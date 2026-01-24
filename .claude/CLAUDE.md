# Aurora 4X Manual - Project Instructions

## Project Overview

This is a comprehensive reference manual for Aurora C# (space strategy game by Steve Walmsley). The manual is written in Markdown, organized by numbered sections, and compiled to PDF via `build-pdf.sh` using pandoc + tectonic.

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
- **Output:** `releases/aurora-manual-YYYY.MM.DD.SEQ.pdf`
- **File list:** All source files must be listed in `build-pdf.sh` FILES array
- **Validation:** Build script validates all listed files exist before compilation
- **Releases:** PDFs are .gitignored; attach to GitHub releases via `gh release create`

## Game Database

- **Location:** `~/Downloads/Aurora271Full/AuroraDB.db` (SQLite)
- **Use:** Verify formulas, values, and mechanics claims against actual game data
- **Caution:** Values from YouTube videos or forum posts should be cross-checked against the database when possible

## Issue Workflow

- Group related issues into parallel waves for background agents
- Close issues with commit reference comments
- Push all commits before closing issues
- Build PDF and create GitHub release after completing a wave

## LaTeX Compatibility

- Avoid Unicode symbols that don't render in LaTeX (e.g., use `<=` instead of `≤`)
- Long tables may overflow; consider breaking into multiple tables or using shorter column content
