---
title: Home
nav_order: 0
---

# Aurora 4X Manual (Unofficial)

[![Latest Release](https://img.shields.io/github/v/release/ErikEvenson/aurora-manual?label=PDF%20Download)](https://github.com/ErikEvenson/aurora-manual/releases/latest)
[![GitHub Discussions](https://img.shields.io/github/discussions/ErikEvenson/aurora-manual)](https://github.com/ErikEvenson/aurora-manual/discussions)

> **Note:** This is an unofficial community manual, not affiliated with or endorsed by Steve Walmsley. It is under active development and may contain inaccuracies. Values and formulas are being verified against the game database. Some content may be incomplete, outdated, or incorrect. If you spot an error, please [report it](../../issues/new?template=inaccuracy-report.md).

A comprehensive reference manual, beginner's guide, and tutorial resource for Aurora C# — the complex 4X space strategy game by Steve Walmsley. Whether you're learning how to play Aurora 4X for the first time or looking up advanced mechanics, this manual covers Aurora C# v2.7.1 with ongoing coverage of new features.

**[Download the latest PDF](https://github.com/ErikEvenson/aurora-manual/releases/latest)** — printable, offline-ready reference

## Structure

This manual is organized using a decimal numbering system. Each major section is a directory containing subsection files. Sub-subsections (e.g., 8.2.1) are headings within files.

| # | Section | Description |
|---|---------|-------------|
| 1 | [Introduction](1-introduction/) | What is Aurora, installation, first launch |
| 2 | [Game Setup](2-game-setup/) | New game options, race creation, system generation, racial traits, starting conditions |
| 3 | [User Interface](3-user-interface/) | Main window, system map, controls, event log, galactic map |
| 4 | [Systems and Bodies](4-systems-and-bodies/) | Stars, planets, moons, asteroids, jump points |
| 5 | [Colonies](5-colonies/) | Establishing, population, environment, terraforming |
| 6 | [Economy and Industry](6-economy-and-industry/) | Minerals, mining, construction, wealth, civilians |
| 7 | [Research](7-research/) | Tech tree, scientists, facilities, categories |
| 8 | [Ship Design](8-ship-design/) | Philosophy, hull, engines, sensors, weapons, other components, examples |
| 9 | [Fleet Management](9-fleet-management/) | Shipyards, construction, task groups, fleet organization, orders, light naval operations |
| 10 | [Navigation](10-navigation/) | Movement, jump transit, survey, waypoints |
| 11 | [Sensors and Detection](11-sensors-and-detection/) | Signatures, passive/active sensors, stealth |
| 12 | [Combat](12-combat/) | Fire controls, beams, missiles, PD, EW, damage, planetary defence centres |
| 13 | [Ground Forces](13-ground-forces/) | Unit types, training, transport, ground combat |
| 14 | [Logistics](14-logistics/) | Fuel, maintenance, supply ships, habitats |
| 15 | [Diplomacy](15-diplomacy/) | Alien races, communications, treaties, diplomacy, espionage |
| 16 | [Commanders](16-commanders/) | Officer generation, skills, assignments |
| 17 | [Exploration](17-exploration/) | Geo survey, grav survey, xenoarchaeology |
| 18 | [Advanced Topics](18-advanced-topics/) | Game mechanics, time increments, spoiler races, late-game strategy, SpaceMaster mode |
| A | [Appendices](appendices/) | Formulas, glossary, tips, reference tables |
| E | [Examples](examples/) | Worked scenarios: ship design, mining, combat, economy |

## How to Play Aurora 4X — Beginner's Guide

New to Aurora 4X? This step-by-step tutorial path will teach you the game from scratch. Follow this reading order to learn Aurora's core mechanics systematically:

1. **Game Setup** ([2.1](2-game-setup/2.1-new-game-options.md), [2.5](2-game-setup/2.5-starting-conditions.md)) — Create your first game
2. **User Interface** ([3.1](3-user-interface/3.1-main-window.md), [3.2](3-user-interface/3.2-system-map.md)) — Navigate the interface
3. **Your Homeworld** ([5.1](5-colonies/5.1-establishing-colonies.md), [5.2](5-colonies/5.2-population.md)) — Understand colony basics
4. **Economy Basics** ([6.1](6-economy-and-industry/6.1-minerals.md), [6.3](6-economy-and-industry/6.3-construction.md)) — Mining and construction
   - *Example:* [Early Game Economy](examples/early-game-economy.md)
5. **Research** ([7.1](7-research/7.1-technology-tree.md), [7.3](7-research/7.3-research-facilities.md)) — Start researching
6. **First Ship Design** ([8.1](8-ship-design/8.1-design-philosophy.md), [8.3](8-ship-design/8.3-engines.md)) — Design philosophy and engines
   - *Example:* [Missile Destroyer Design](examples/missile-destroyer-design.md)
7. **Fleet Management** ([9.1](9-fleet-management/9.1-shipyards.md), [9.3](9-fleet-management/9.3-task-groups.md)) — Build and organize ships
8. **Exploration** ([17.1](17-exploration/17.1-geological-survey.md), [10.2](10-navigation/10.2-jump-transit.md)) — Survey nearby systems
   - *Example:* [Exploration Workflow](examples/exploration-workflow.md)
9. **Navigation** ([10.1](10-navigation/10.1-movement-mechanics.md)) — Move fleets between systems
10. **First Contact** ([15.1](15-diplomacy/15.1-alien-races.md), [12.1](12-combat/12.1-fire-controls.md)) — When you encounter hostiles
    - *Example:* [Fleet Engagement](examples/fleet-engagement.md)

After completing this path, explore sections relevant to your current gameplay challenges.

## What This Manual Covers

This Aurora 4X guide provides detailed documentation on:

- **Getting started** — Installation, game setup, creating your first empire
- **Ship design** — Hull types, engines, sensors, weapons, armor, and component optimization
- **Fleet management** — Task groups, standing orders, fleet organization, naval commands
- **Combat mechanics** — Fire controls, beam weapons, missiles, point defense, electronic warfare
- **Colony management** — Population, infrastructure, terraforming, governors
- **Economy** — Mining, construction, research, wealth generation
- **Exploration** — Geological surveys, gravitational surveys, jump point mechanics
- **Ground combat** — Unit types, formations, invasions, planetary defense
- **Diplomacy** — First contact, treaties, espionage, alien races
- **Formulas and tables** — Verified game mechanics from the Aurora database

## Sources

- Steve Walmsley's forum posts (http://aurora2.pentarch.org/) — the official Aurora forum on pentarch.org, the authoritative primary source for Aurora mechanics and development history since 2003
- Aurora community wiki
- In-game database and tooltips
- Community guides (Reddit r/aurora4x and r/aurora)
- YouTube tutorials — specific credits appear in manual references where content was sourced

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines on reporting inaccuracies, submitting corrections, and adding new content.

**Quick links:**

- [Report an inaccuracy](../../issues/new?template=inaccuracy-report.md) — wrong formulas, incorrect values, outdated mechanics
- [Report missing content](../../issues/new?template=missing-content.md) — undocumented mechanics, edge cases, gaps

### File Format

Each section file should follow this format:

```markdown
# X.Y Section Title

Brief overview of what this section covers.

## X.Y.1 First Sub-topic

Content here with practical examples.

## X.Y.2 Second Sub-topic

Content here.
```

## Building the PDF

Requires: `pandoc`, `tectonic` (LaTeX), `rsvg-convert`

```bash
# Development build (auto-increment version)
bash build-pdf.sh

# Release build (explicit version)
bash build-pdf.sh 2026.01.28.07
```

Output: `releases/aurora-manual-VERSION.pdf`

## Community Review

This manual covers Aurora C# v2.7.1. Coverage of new versions is ongoing. We welcome review from experienced players on:

- Formula and value accuracy
- Missing mechanics or edge cases
- Outdated VB6 references
- Quality of practical tips and advice
- Common player questions not yet answered

## Contributors

- **[@ErikEvenson](https://github.com/ErikEvenson)**
- **[@ManzoorAhmedShaikh](https://github.com/ManzoorAhmedShaikh)**
