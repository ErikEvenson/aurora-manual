# Contributing to the Aurora C# Manual

Welcome, and thank you for your interest in improving this community reference manual for Aurora C# (v2.8.0). Aurora is a deeply complex game, and no single player can verify every mechanic, formula, or edge case alone. Your contributions help the entire community play with better information.

Whether you've spotted an outdated formula, discovered an undocumented mechanic through hours of testing, or simply know a better way to explain a concept, we'd love your help.

## Types of Contributions Welcome

- **Inaccuracy reports** - Wrong formulas, incorrect values, outdated mechanics that no longer match in-game behavior.
- **Missing content** - Undocumented mechanics, edge cases, interactions between systems that aren't covered.
- **VB6-era corrections** - Content that inadvertently references the old VB6 version instead of the current C# build. These slip in more often than you'd think.
- **Practical experience** - Tips, strategies, common questions answered, "I wish someone had told me this" moments.
- **Formatting and clarity improvements** - Better explanations, clearer structure, fixing broken cross-references.

## How to Report an Issue

If you've found a problem but don't want to submit a PR, opening an issue is just as valuable.

1. **For incorrect information**, use the "Inaccuracy Report" issue template.
2. **For gaps in coverage**, use the "Missing Content" issue template.
3. **Always include the section number** (e.g., "Section 8.3 - Missile Design") so reviewers can locate the content quickly.
4. **If you know the correct value or formula**, include it along with your source:
   - A link to a forum post (especially one by Steve Walmsley)
   - Results from your own in-game testing
   - A save file or screenshot demonstrating the correct behavior

Even a report that says "Section 5.2.1 says mining rate is X, but in my game it's clearly Y" is helpful. We can investigate from there.

## How to Submit a Pull Request

1. **Fork the repository** and create a branch for your changes.
2. **Follow the file format conventions** - decimal numbering, markdown structure as shown in the README.
3. **Keep changes focused** - one topic per PR. A PR that fixes a missile formula should not also reorganize the ground combat section.
4. **Include source or verification** for any factual claims. See the Verification Standards section below.
5. **Test that cross-references are valid** - if you link to another section, make sure the relative link resolves correctly.
6. **Write a clear PR description** explaining what changed and why. If you're correcting a value, state both the old (incorrect) value and the new (correct) value.

## Style Guide

To keep the manual consistent, please follow these conventions:

- **Decimal section numbering** - Use hierarchical numbering like 8.2.1, not flat numbering or bullet-only structures.
- **Formulas in code blocks** with variable explanations immediately following:
  ```
  Fuel Consumption = Distance / (Fuel Efficiency * Engine Modifier)
  ```
  - `Distance` - total km traveled
  - `Fuel Efficiency` - base efficiency rating of the engine
  - `Engine Modifier` - multiplier from engine technology level

- **Practical examples after abstract descriptions** - If you explain how a formula works, follow it with a concrete scenario showing real numbers.
- **Cross-reference related sections** using relative markdown links (e.g., `[see Missile Launchers](8-ship-design/8.5-weapons.md#853-missile-launchers)`).
- **No VB6-specific content** - This manual covers Aurora C# only. If a mechanic worked differently in VB6, that's historical trivia, not reference material.

## What Reviewers Should Check

When reviewing a PR, consider:

- Are the formulas and values accurate for Aurora C# v2.8.0?
- Are there missing mechanics or edge cases the contribution overlooks?
- Are there outdated VB6 references that slipped through?
- Are the practical tips actually good advice, or could they mislead a new player?
- Does this raise common player questions that aren't answered?
- Are cross-references and links valid?

## Verification Standards

Not all sources are equal. Here's how we rank verification:

| Level | Description | Requirement |
|-------|-------------|-------------|
| **Ideal** | In-game testing | Save file evidence, screenshots, or reproducible steps |
| **Good** | Official forum post by Steve Walmsley | Direct link to the post required |
| **Acceptable** | Multiple community confirmations | At least 2-3 independent players confirming the same behavior |
| **Not sufficient** | Single unverified claim | One person saying "I think it works like X" without evidence |

If your contribution is based on in-game testing, briefly describe your test methodology. You don't need a lab report, but "I tested this with 5 different engine designs and measured fuel consumption across 10 transits" goes a long way toward building confidence.

## Acknowledgment

Contributors will be listed in the README.md Contributors section. If you submit a PR or report an issue that leads to a correction, you've helped every Aurora player who reads this manual. That's worth recognizing.

---

Questions about contributing? Open a discussion thread and the community will help you out. Aurora has a steep learning curve, but the community around it is welcoming. Your contribution, no matter how small, makes the game more accessible for everyone.
