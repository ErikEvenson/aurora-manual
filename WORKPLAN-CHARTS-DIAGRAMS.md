# Workplan: Charts and Diagrams

## Overview

**Total Issues:** 167
- Charts: 72 issues (#875-#946)
- Diagrams: 95 issues (#947-#1042)

**Approach:** Execute in parallel waves using background agents, grouped by chapter and type.

## Execution Strategy

### Wave Structure
- **4-6 parallel agents per wave** (balances throughput vs resource usage)
- **Each agent handles 3-5 related issues** (same chapter/type)
- **Estimated time per wave:** 15-30 minutes
- **Total waves:** ~10-12

### Tool Selection by Type
| Visual Type | Tool | Output |
|-------------|------|--------|
| Line/bar charts | Python/matplotlib | PNG |
| Flowcharts | Graphviz DOT | SVG |
| Decision trees | Graphviz DOT | SVG |
| System diagrams | Graphviz DOT | SVG |
| Tech trees | Graphviz DOT | SVG |
| Matrices/heatmaps | Python/matplotlib | PNG |
| Tactical illustrations | Python/matplotlib | PNG |

---

## Wave 1: Foundation (Simple Charts)
*Establish chart workflow with straightforward visualizations*

| Agent | Issues | Description |
|-------|--------|-------------|
| 1A | #875, #876, #877, #878 | Ch 2-4 basic charts (difficulty modifiers, star types, government types, disaster timeline) |
| 1B | #879, #880, #881, #882 | Ch 4-6 charts (atmosphere, jump points, wealth gen, greenhouse) |
| 1C | #883, #884, #885, #886 | Ch 7 tech progression charts (terraforming, armour, research, accessibility) |
| 1D | #887, #888, #889, #890 | Ch 5-7 charts (economic modifiers, temperature, engines, workforce) |

**Issues completed:** 16 charts

---

## Wave 2: Ship Design Charts
*Complete Chapter 8 charts*

| Agent | Issues | Description |
|-------|--------|-------------|
| 2A | #891, #892, #893, #894 | Construction, engine power, survey perf, jump shock |
| 2B | #895, #896, #897, #898 | Shipyard comparison, workforce, armor tech, survey sensor |
| 2C | #899, #900, #901, #902 | Jump drive efficiency, sensor resolution, engine power, magazine explosion |
| 2D | #903, #904, #905 | Component allocation, fleet speed, railgun trade-offs |

**Issues completed:** 15 charts (cumulative: 31)

---

## Wave 3: Combat & Logistics Charts
*Chapters 11-14 charts*

| Agent | Issues | Description |
|-------|--------|-------------|
| 3A | #906, #907, #908, #909, #910 | Fire control tracking, gauss ROF, armor pen, laser damage, CIWS |
| 3B | #911, #912, #913, #914, #915 | Beam FC range, cloaking cost, maintenance, ground GSP, thermal reduction |
| 3C | #916, #917, #918, #919, #920 | Fuel consumption, refinery output, ordnance transfer, terrain, missile speed |
| 3D | #921, #922, #923, #924 | Passive sensor, crew training, ground survey, accessibility |

**Issues completed:** 19 charts (cumulative: 50)

---

## Wave 4: Advanced & Appendix Charts
*Chapters 15-17 and Appendices*

| Agent | Issues | Description |
|-------|--------|-------------|
| 4A | #925, #926, #927, #928 | NPR personality, officer types, survey points, skill bonus |
| 4B | #929, #930, #931, #932 | Diplomatic points (2), promotion scores, intrusion threat |
| 4C | #933, #934, #935, #936 | Appendix: terraforming, sensor formula, colony cost, weapon damage |
| 4D | #937, #938, #939, #940 | Appendix: shipyard time, installation costs, speed formula, garrison |
| 4E | #941, #942, #943, #944, #945, #946 | Appendix: power plant, beam weapons, to-hit, research, engine fuel, population |

**Issues completed:** 22 charts (cumulative: 72 - ALL CHARTS DONE)

---

## Wave 5: Introduction & Setup Diagrams
*Chapters 1-3 diagrams (Graphviz flowcharts)*

| Agent | Issues | Description |
|-------|--------|-------------|
| 5A | #947, #948, #949, #950 | Game timeline, feature scope, game creation workflow, trait point-buy |
| 5B | #951, #952, #953, #954 | Catastrophe timeline, CI-to-TN, installation chain, government matrix |
| 5C | #955, #956, #957, #958, #959 | Menu organization, time increment, display layers, sub-pulse, survey rings |

**Issues completed:** 13 diagrams (cumulative: 85)

---

## Wave 6: Systems & Colonies Diagrams
*Chapters 4-5 diagrams*

| Agent | Issues | Description |
|-------|--------|-------------|
| 6A | #960, #961, #962, #963 | Habitable zones, binary systems, gas hazard, colony cost factors |
| 6B | #964, #965, #966, #1034, #1035 | Jump point discovery, squadron transit, gate states, HR diagram, planet types |
| 6C | #1036, #1037, #967, #968 | Asteroid belts, gate timeline, workforce pipeline, habitability zones |
| 6D | #969, #970, #971 | Greenhouse feedback, installation dependencies, terraforming decision tree |

**Issues completed:** 16 diagrams (cumulative: 101)

---

## Wave 7: Economy & Research Diagrams
*Chapters 6-7 diagrams*

| Agent | Issues | Description |
|-------|--------|-------------|
| 7A | #972, #973, #974, #1038 | Mineral network, mass driver, factory growth, depletion curve |
| 7B | #975, #976, #977, #978 | Tech tree structure, prototype states, engine progression, research flow |

**Issues completed:** 8 diagrams (cumulative: 109)

---

## Wave 8: Ship Design Diagrams
*Chapter 8 diagrams*

| Agent | Issues | Description |
|-------|--------|-------------|
| 8A | #979, #980, #981, #982 | Role allocation, armor gradients, sensor-FC coordination, meson retardation |
| 8B | #983, #1022, #1023 | Carrier sortie, engine power curve, power boost risk |

**Issues completed:** 7 diagrams (cumulative: 116)

---

## Wave 9: Fleet & Navigation Diagrams
*Chapters 9-10 diagrams*

| Agent | Issues | Description |
|-------|--------|-------------|
| 9A | #984, #985, #986, #987, #1024 | Shipyard decision, speed bottleneck, conditional orders, refuelling, expansion |
| 9B | #988, #989, #990, #991, #1025 | Speed/distance, patrol route, jump efficiency, jump shock, squadron constraints |

**Issues completed:** 10 diagrams (cumulative: 126)

---

## Wave 10: Sensors & Combat Diagrams
*Chapters 11-12 diagrams*

| Agent | Issues | Description |
|-------|--------|-------------|
| 10A | #992, #993, #994, #995, #1029 | Detection workflow, sensor decision tree, cloaking effect, ambush, passive vs active |
| 10B | #1030, #1031, #997, #998 | Signature matrix, EMCON lifecycle, combat interactions, FC resolution |
| 10C | #999, #1000, #1001, #1002, #1039 | Laser falloff, armor penetration, PD layering, missile engagement, weapon failure |
| 10D | #1003, #1032 | Damage grid, shield regeneration |

**Issues completed:** 16 diagrams (cumulative: 142)

---

## Wave 11: Ground Forces & Logistics Diagrams
*Chapters 13-14 diagrams*

| Agent | Issues | Description |
|-------|--------|-------------|
| 11A | #1004, #1005, #1033 | Ground unit hierarchy, base type comparison, armor penetration |
| 11B | #1006, #1007 | Fuel supply chain, harvester automation |

**Issues completed:** 5 diagrams (cumulative: 147)

---

## Wave 12: Diplomacy & Commanders Diagrams
*Chapters 15-16 diagrams*

| Agent | Issues | Description |
|-------|--------|-------------|
| 12A | #1008, #1009, #1010, #1011, #1040 | Diplomatic flow, intrusion, relationship, NPR behavior, claim acceptance |
| 12B | #1012, #1013, #1014, #1026, #1027, #1041 | Officer pipeline, command hierarchy, skill matrix, crew grade, promotion, governor |

**Issues completed:** 11 diagrams (cumulative: 158)

---

## Wave 13: Exploration & Advanced Diagrams
*Chapters 17-18 and Appendix diagrams*

| Agent | Issues | Description |
|-------|--------|-------------|
| 13A | #1015, #1016, #1017, #1028, #1042 | Survey mechanics, jump topology, Lagrange points, excavation rate, ruin value |
| 13B | #1018, #1019, #1020, #1021 | Combat turn sequence, beam to-hit, production formula, mineral dependencies |

**Issues completed:** 9 diagrams (cumulative: 167 - ALL DONE)

---

## Summary

| Wave | Type | Issues | Agents | Est. Time |
|------|------|--------|--------|-----------|
| 1 | Charts | 16 | 4 | 20 min |
| 2 | Charts | 15 | 4 | 20 min |
| 3 | Charts | 19 | 4 | 25 min |
| 4 | Charts | 22 | 5 | 25 min |
| 5 | Diagrams | 13 | 3 | 20 min |
| 6 | Diagrams | 16 | 4 | 25 min |
| 7 | Diagrams | 8 | 2 | 15 min |
| 8 | Diagrams | 7 | 2 | 15 min |
| 9 | Diagrams | 10 | 2 | 20 min |
| 10 | Diagrams | 16 | 4 | 25 min |
| 11 | Diagrams | 5 | 2 | 15 min |
| 12 | Diagrams | 11 | 2 | 20 min |
| 13 | Diagrams | 9 | 2 | 20 min |
| **Total** | | **167** | ~40 agent-runs | ~4-5 hours |

## Quality Assurance

After each wave:
1. Review generated files for consistency
2. Verify SVG/PNG renders correctly
3. Spot-check manual integration
4. Commit and push changes

After all waves:
1. Full PDF build to verify all images render
2. Visual review of PDF output
3. Create release with all visual content

## Notes

- Agents will follow standards in `.claude/CLAUDE.md` (chart and diagram sections)
- Each agent creates files, updates manual sections, and closes issues
- Background execution allows continued work during generation
- Can pause/resume between waves as needed
