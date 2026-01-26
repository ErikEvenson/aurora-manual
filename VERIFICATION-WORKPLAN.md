# Manual Verification Workplan

## Priority Tiers

### Tier 1: Critical (Formulas and Numbers)
Sections with specific values that can be directly verified against the database.

| Section | File | Risk | Database Tables |
|---------|------|------|-----------------|
| Appendix A | appendices/A-formulas.md | Critical | Various |
| 6.1 Minerals | 6-economy-and-industry/6.1-minerals.md | Critical | DIM_Mineral |
| 6.2 Mining | 6-economy-and-industry/6.2-mining.md | Critical | FCT_Installation |
| 8.3 Engines | 8-ship-design/8.3-engines.md | Critical | DIM_EngineType |
| 8.5 Weapons | 8-ship-design/8.5-weapons.md | Critical | DIM_WeaponType |
| 9.1 Shipyards | 9-fleet-management/9.1-shipyards.md | Critical | FCT_Shipyard |
| 14.1 Fuel | 14-logistics/14.1-fuel.md | Critical | FCT_Installation |
| 14.2 Maintenance | 14-logistics/14.2-maintenance.md | Critical | Various |

### Tier 2: High (Game Mechanics)
Sections describing mechanics that can be verified against forums/wiki.

| Section | File | Risk | Sources |
|---------|------|------|---------|
| 10.1 Movement | 10-navigation/10.1-movement-mechanics.md | High | Forums, Wiki |
| 10.2 Jump Transit | 10-navigation/10.2-jump-transit.md | High | Forums, Wiki |
| 11.1-11.4 Sensors | 11-sensors-and-detection/*.md | High | Database, Forums |
| 12.1-12.6 Combat | 12-combat/*.md | High | Database, Forums |
| 16.1 Officers | 16-commanders/16.1-officer-generation.md | High | Database, Forums |

### Tier 3: Medium (Descriptions)
Sections with general descriptions that should be checked against screenshots/gameplay.

| Section | File | Risk | Sources |
|---------|------|------|---------|
| 2.1 New Game Options | 2-game-setup/2.1-new-game-options.md | Medium | Screenshots |
| 3.x User Interface | 3-user-interface/*.md | Medium | Screenshots |
| 5.x Colonies | 5-colonies/*.md | Medium | Screenshots, Wiki |
| 7.x Research | 7-research/*.md | Medium | Database, Screenshots |

### Tier 4: Lower (General Content)
Sections with general information less likely to have specific errors.

| Section | File | Risk | Sources |
|---------|------|------|---------|
| 1.x Introduction | 1-introduction/*.md | Lower | General |
| 15.x Diplomacy | 15-diplomacy/*.md | Lower | Forums, Wiki |
| 17.x Exploration | 17-exploration/*.md | Lower | Forums, Wiki |

## Verification Process

For each section:
1. Query Aurora database for relevant tables
2. Search Steve Walmsley forum posts for mechanic explanations
3. Check AuroraWiki for documented values
4. Compare YouTube tutorials (Defran Strategy, MO Chad) for gameplay confirmation
5. Add numbered references for verified claims
6. Flag or remove unverified specific values
7. Update Section 1.1.4 verified list

## Parallel Task Strategy

Launch background agents in waves:
- Wave 1: Tier 1 Critical sections (8 parallel agents)
- Wave 2: Tier 2 High sections (5 parallel agents)
- Wave 3: Tier 3 Medium sections (4 parallel agents)
- Wave 4: Tier 4 Lower sections (3 parallel agents)

## Database Tables Reference

Key tables for verification:
- `DIM_Mineral` - Mineral names and properties
- `DIM_EngineType` - Engine specifications
- `DIM_WeaponType` - Weapon specifications
- `DIM_StellarType` - Star types and properties
- `FCT_Installation` - Installation production values
- `FCT_Shipyard` - Shipyard capacities
- `FCT_Race` - Race attributes
- `DIM_GovType` - Government types

## YouTube Sources

- **Defran Strategy**: Ground combat, colonization, early-game
- **MO Chad**: Installation, setup, beginner fundamentals
