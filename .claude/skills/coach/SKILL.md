---
name: coach
description: Analyze Aurora C# game state and provide spoiler-free coaching advice. Use when player asks for help, guidance, or "what should I do next" questions.
argument-hint: "[db-path]"
allowed-tools: Bash, Read, Glob, Grep
---

# Aurora Coach

Provide spoiler-free coaching for Aurora C# based on the player's current game state and the Aurora manual.

## Arguments

- `$ARGUMENTS` - Optional: path to AuroraDB.db (default: `../Aurora/AuroraDB.db`)

## Database Location

```
DB_PATH="${ARGUMENTS:-../Aurora/AuroraDB.db}"
```

## Manual Location

The Aurora manual is in the current working directory. Use it to:
- Explain game mechanics in detail
- Cite specific sections for the player to read
- Provide accurate formulas and values

**Manual URL base:** `https://erikevenson.github.io/aurora-manual/`

## Instructions

You are an Aurora C# coach. Analyze the player's game state and provide helpful guidance WITHOUT revealing any information they wouldn't have access to in-game. Reference the manual to explain mechanics.

### Strict Spoiler Rules

**NEVER reveal:**
- NPR (Non-Player Race) information: locations, fleet compositions, tech levels, ship designs
- Unexplored system contents
- Jump point destinations the player hasn't surveyed
- Precursor, Invader, Swarm, or Eldar details
- Hidden events or mechanics outcomes

**ONLY use data from:**
- Player's race (NPR=0)
- Player's known systems and surveys
- Player's own ships, designs, colonies, and research
- Player's commanders and their visible stats

### Analysis Steps

1. **Identify the game and player race:**
   ```sql
   SELECT GameID, GameName, GameTime, StartYear FROM FCT_Game;
   SELECT RaceID, RaceTitle FROM FCT_Race WHERE GameID=<id> AND NPR=0;
   ```

2. **Determine game phase** by checking:
   - GameTime (0.0 = fresh start)
   - Conventional Industry vs Construction Factories
   - Trans-Newtonian tech researched?
   - Ships built?
   - Systems explored?

3. **Assess current state:**
   - Colonies and population
   - Installations (research labs, factories, mines, etc.)
   - Active research projects
   - Ship count and types
   - Shipyard capacity and current activity (expansion, building, idle)
   - Mineral stockpiles (especially Sorium for fuel)
   - Fuel reserves
   - Academy commandant assignment
   - Fleet organization and naval command structure
   - Commander assignments to key positions

4. **Provide phase-appropriate coaching:**

### Coaching by Game Phase

**Phase 0: Conventional Start (no TN tech)**
- Priority: Research Trans-Newtonian Technology
- Consult `2-game-setup/2.5-starting-conditions.md` for CI conversion mechanics
- Suggest browsing ship designer to learn components

**Phase 1: Early TN (TN tech done, no ships)**
- Consult `8-ship-design/` for survey ship design
- Consult `9-fleet-management/9.1-shipyards.md` for retooling
- Consult `7-research/7.1-technology-tree.md` for research priorities

**Phase 2: Exploration (survey ships built)**
- Consult `17-exploration/` for survey mechanics
- Consult `14-logistics/14.1-fuel.md` for fuel harvesting
- Consult `10-navigation/10.2-jump-transit.md` for jump mechanics

**Phase 3: Expansion (jump-capable)**
- Consult `5-colonies/5.1-establishing-colonies.md` for colony setup
- Consult `6-economy-and-industry/6.2-mining.md` for mining operations

**Phase 4: Contact Preparation**
- Consult `12-combat/` for combat mechanics
- Consult `8-ship-design/8.5-weapons.md` for weapon design
- Consult `11-sensors-and-detection/` for detection mechanics

**IMPORTANT:** Always read the relevant manual sections before explaining mechanics. Never state mechanics from memory or from this skill file alone — the manual is the authoritative source. Use Grep/Read tools to verify claims against manual content before presenting to player.

### Key Queries Reference

**Player race ID:**
```sql
SELECT RaceID FROM FCT_Race WHERE GameID=<gid> AND NPR=0;
```

**Population ID (needed for other queries):**
```sql
SELECT PopulationID FROM FCT_Population WHERE RaceID=<rid> AND Population > 0;
```

**Colonies:**
```sql
SELECT PopName, Population FROM FCT_Population WHERE RaceID=<rid> AND Population > 0;
```

**Installations:**
```sql
SELECT di.Name, pi.Amount
FROM FCT_PopulationInstallations pi
JOIN DIM_PlanetaryInstallation di ON pi.PlanetaryInstallationID = di.PlanetaryInstallationID
WHERE pi.PopID IN (SELECT PopulationID FROM FCT_Population WHERE RaceID=<rid>)
AND pi.Amount > 0
ORDER BY pi.Amount DESC;
```

**Research projects (with assigned scientist):**
```sql
SELECT rp.ProjectID, ts.Name as Tech, rp.Facilities as Labs, c.Name as Scientist, rf.FieldName as ScientistField
FROM FCT_ResearchProject rp
JOIN FCT_TechSystem ts ON rp.TechID = ts.TechSystemID
LEFT JOIN FCT_Commander c ON c.CommandType=7 AND c.CommandID = rp.ProjectID
LEFT JOIN DIM_ResearchField rf ON c.ResSpecID = rf.ResearchFieldID
WHERE rp.RaceID=<rid>;
```

Note: Scientists get a 4× research bonus when working in their specialty field.

**Research queue (queued techs per project):**
```sql
SELECT rq.CurrentProjectID, rq.ResearchOrder, ts.Name
FROM FCT_ResearchQueue rq
JOIN FCT_TechSystem ts ON rq.TechSystemID = ts.TechSystemID
WHERE rq.PopulationID=<popid>
ORDER BY rq.CurrentProjectID, rq.ResearchOrder;
```

Note: CurrentProjectID links to FCT_ResearchProject.ProjectID. ResearchOrder is the queue position (1, 2, 3...).

**Ships:**
```sql
SELECT s.ShipName, sc.ClassName
FROM FCT_Ship s
JOIN FCT_ShipClass sc ON s.ShipClassID = sc.ShipClassID
WHERE s.RaceID=<rid>;
```

**Shipyards (with activity):**
```sql
SELECT ShipyardID, ShipyardName, SYType, Slipways, Capacity, TaskType, RequiredBP, CompletedBP
FROM FCT_Shipyard
WHERE PopulationID IN (SELECT PopulationID FROM FCT_Population WHERE RaceID=<rid>);
```

Shipyard types: SYType 1=Naval, 2=Commercial, 3=Light Naval, 4=Repair

Task types: 0=Idle, 1=Build, 2=Refit, 3=Scrap, 4=Add Capacity (Naval), 5=Add Slipway, 6=Continual Capacity (Commercial)

**Minerals:**
```sql
SELECT Duranium, Neutronium, Corbomite, Tritanium, Boronide, Mercassium, Vendarite, Sorium, Uridium, Corundium
FROM FCT_Population WHERE RaceID=<rid>;
```

**Production queue (CI conversions, installations, etc.) — ALWAYS CHECK:**
```sql
SELECT Description, Amount, PartialCompletion, Percentage
FROM FCT_IndustrialProjects
WHERE PopulationID=<popid>;
```

**⚠️ If production queue is empty, check CF count and warn about idle capacity:**
```sql
-- Get CF count (PlanetaryInstallationID=2 is Construction Factory)
SELECT pi.Amount as CFs
FROM FCT_PopulationInstallations pi
WHERE pi.PopID=<popid> AND pi.PlanetaryInstallationID=2;
```

**Calculate idle BP/year:** CFs × Construction Rate (default 10 BP, or 12/14/16 if researched)

Example: 800 CFs × 14 BP = 11,200 BP/year idle capacity

**Check if TN tech researched:**
```sql
-- TN Tech has TechSystemID=27434
SELECT COUNT(*) FROM FCT_RaceTech WHERE RaceID=<rid> AND TechID=27434;
```

**Check researched techs by keyword (e.g., engines, fuel):**
```sql
SELECT ts.TechSystemID, ts.Name
FROM FCT_RaceTech rt
JOIN FCT_TechSystem ts ON rt.TechID = ts.TechSystemID
WHERE rt.RaceID=<rid> AND ts.Name LIKE '%Engine%';
```

**Key engine/fuel tech IDs:**
- 25141: Fuel Consumption 1.0 L/EPH (starting)
- 25129-25140: Fuel Consumption improvements (0.9 down to 0.1)
- 24604: Nuclear Thermal Engine
- 24605: Nuclear Pulse Engine
- 38336: Conventional Engine

### Commander Queries

**Commander types (CommanderType field):**
- 0 = Naval Officer
- 1 = Naval Officer (senior)
- 2 = Ground Officer
- 3 = Scientist
- 4 = Administrator

**Command assignment types (CommandType field):**
- 0 = Unassigned
- 7 = Research Project Leader (CommandID = ProjectID from FCT_ResearchProject)
- 12 = Naval Admin Command
- 17 = Academy Commandant (CommandID = PopulationID)

**Academy Commandant (CommandType=17 with CommandID=PopulationID):**
```sql
SELECT c.Name, c.CommanderType
FROM FCT_Commander c
WHERE c.RaceID=<rid> AND c.CommandType=17 AND c.CommandID=<popid>;
```

**Commander bonuses:**
```sql
SELECT c.Name, bt.Description, cb.BonusValue
FROM FCT_Commander c
JOIN FCT_CommanderBonuses cb ON c.CommanderID = cb.CommanderID
JOIN DIM_CommanderBonusType bt ON cb.BonusID = bt.BonusID
WHERE c.RaceID=<rid> AND c.CommanderID=<cid>;
```

**Find commanders with specific bonus (e.g., Crew Training = BonusID 1):**
```sql
SELECT c.Name, c.CommanderType, cb.BonusValue
FROM FCT_Commander c
JOIN FCT_CommanderBonuses cb ON c.CommanderID = cb.CommanderID
WHERE c.RaceID=<rid> AND cb.BonusID=1
ORDER BY cb.BonusValue DESC;
```

Key bonus types: 1=Crew Training, 3=Research, 12=Ground Combat Training, 27=Research Admin, 37=Fleet Training

### Scientist Queries

**Research fields (DIM_ResearchField):**
| ResearchFieldID | FieldName |
|-----------------|-----------|
| 1 | Power and Propulsion |
| 2 | Sensors and Control Systems |
| 3 | Direct Fire Weapons |
| 4 | Missiles |
| 5 | Construction / Production |
| 6 | Logistics |
| 7 | Defensive Systems |
| 8 | Biology / Genetics |
| 9 | Ground Combat |

**List all scientists with their specialization and Research Admin:**
```sql
SELECT c.Name, rf.FieldName, cb.BonusValue as ResearchAdmin, c.CommandType
FROM FCT_Commander c
JOIN DIM_ResearchField rf ON c.ResSpecID = rf.ResearchFieldID
LEFT JOIN FCT_CommanderBonuses cb ON c.CommanderID = cb.CommanderID AND cb.BonusID = 27
WHERE c.RaceID=<rid> AND c.CommanderType=3
ORDER BY cb.BonusValue DESC;
```

**Find unassigned scientists by field:**
```sql
SELECT c.Name, rf.FieldName, cb.BonusValue as ResearchAdmin
FROM FCT_Commander c
JOIN DIM_ResearchField rf ON c.ResSpecID = rf.ResearchFieldID
LEFT JOIN FCT_CommanderBonuses cb ON c.CommanderID = cb.CommanderID AND cb.BonusID = 27
WHERE c.RaceID=<rid> AND c.CommanderType=3 AND c.CommandType=0
ORDER BY rf.ResearchFieldID, cb.BonusValue DESC;
```

**Find which scientist leads each research project:**
```sql
SELECT rp.ProjectID, ts.Name as Tech, c.Name as Scientist, rf.FieldName as ScientistField
FROM FCT_ResearchProject rp
JOIN FCT_TechSystem ts ON rp.TechID = ts.TechSystemID
LEFT JOIN FCT_Commander c ON c.CommandType=7 AND c.CommandID = rp.ProjectID
LEFT JOIN DIM_ResearchField rf ON c.ResSpecID = rf.ResearchFieldID
WHERE rp.RaceID=<rid>;
```

**Academy commandant scientist analysis (for scientist generation):**
When a scientist is Academy Commandant:
- 14% chance each graduate is a scientist (vs 7% base)
- 25% chance generated scientists share the commandant's research field
- If commandant has 20%+ Research Admin, graduates get 2 rolls and keep the better result

```sql
-- Check if commandant is a scientist and their field
SELECT c.Name, c.CommanderType, rf.FieldName, cb.BonusValue as ResearchAdmin
FROM FCT_Commander c
LEFT JOIN DIM_ResearchField rf ON c.ResSpecID = rf.ResearchFieldID
LEFT JOIN FCT_CommanderBonuses cb ON c.CommanderID = cb.CommanderID AND cb.BonusID = 27
WHERE c.RaceID=<rid> AND c.CommandType=17 AND c.CommandID=<popid>;
```

### Fleet Organization Queries

**Fleets:**
```sql
SELECT FleetID, FleetName FROM FCT_Fleet WHERE RaceID=<rid>;
```

**Naval Admin Commands (command hierarchy):**
```sql
SELECT NavalAdminCommandID, AdminCommandName, ParentAdminCommandID
FROM FCT_NavalAdminCommand
WHERE RaceID=<rid>;
```

ParentAdminCommandID=0 means top-level command.

**Commanders assigned to naval admin commands (CommandType=12):**
```sql
SELECT c.Name, c.CommandType, c.CommandID
FROM FCT_Commander c
WHERE c.RaceID=<rid> AND c.CommandType=12;
```

### Ship Design & Shipyard Strategy

**Ship classification (military vs commercial):**
- Survey sensors (Geo or Grav) make a ship **military** — requires naval shipyard
- Weapons, military engines, significant armor → military
- Commercial ships: freighters, tankers, colony ships without military components

**Engine choice for survey ships:**
- Commercial engines: larger but more fuel efficient — good for survey ships needing range
- Military engines: smaller but less fuel efficient — good for warships needing speed
- A survey ship with commercial engines is still military (due to survey sensors) and needs a naval shipyard

**Shipyard strategy (early game):**
- Multiple shipyards > multiple slipways when building different ship classes
- Multiple slipways = mass-produce one class (e.g., 10 destroyers for war)
- Retooling cost is based on tonnage difference, NOT number of slipways
- Keep shipyards tooled for different classes to avoid retooling delays

**Typical shipyard setup:**
- 1 naval yard for survey ships → later retool or build 2nd naval for warships
- 1 commercial yard for freighters, tankers, colony ships

### CI Conversion Rules

*Ref: 6-economy-and-industry/6.3-construction.md*

**CI can convert to (20 BP each = 1/6th normal build cost):**

| Target | Mineral Cost |
|--------|--------------|
| Construction Factory | 10 Dur + 10 Neu |
| Mine | 20 Corundium |
| Fuel Refinery | 20 Boronide |
| Financial Centre | 20 Corbomite |
| Ordnance Factory | 20 Tritanium |
| Fighter Factory (Light Naval in v2.8) | 20 Vendarite |

**Cannot convert from CI — must build from scratch:**
- Research Facility (2,400 BP + 1,200 Dur)
- Maintenance Facility (150 BP + 75 Dur + 75 Neu)
- Military Academy (2,400 BP + 1,200 Dur)
- Infrastructure (2 BP)
- Automated Mine (converts from Mine, not CI)
- Naval/Commercial Shipyard (2,400 BP + 1,200 Dur + 1,200 Neu)
- Terraforming Installation
- Deep Space Tracking Station

**Query to check CI conversion options:**
```sql
SELECT PlanetaryInstallationID, Name FROM DIM_PlanetaryInstallation
WHERE ConversionFrom = 38 ORDER BY Name;
```

### Research Field Mapping

**IMPORTANT:** Database categories (DIM_ResearchCategories) do NOT directly map to scientist fields (DIM_ResearchField).

The database may show a tech as "General Science" category, but for scientist bonuses, determine the field by what the tech enables:

| Tech | DB Category | Actual Scientist Field |
|------|-------------|----------------------|
| Jump Point Theory | General Science | Power and Propulsion (enables jump drives) |
| Fuel Consumption techs | Industry | Power and Propulsion |
| Survey Sensors | Survey Sensors | Sensors and Control |
| Construction Rate | Industry | Construction / Production |
| Shipbuilding Rate | Industry | Construction / Production |

**To check available techs with prerequisites met:**
```sql
SELECT ts.TechSystemID, ts.Name, ts.DevelopCost, rc.Name as Category
FROM FCT_TechSystem ts
JOIN DIM_ResearchCategories rc ON ts.CategoryID = rc.CategoryID
WHERE ts.GameID = 0
  AND ts.TechSystemID NOT IN (SELECT TechID FROM FCT_RaceTech WHERE RaceID=<rid>)
  AND (ts.Prerequisite1 = 0 OR ts.Prerequisite1 IN (SELECT TechID FROM FCT_RaceTech WHERE RaceID=<rid>))
  AND (ts.Prerequisite2 = 0 OR ts.Prerequisite2 IN (SELECT TechID FROM FCT_RaceTech WHERE RaceID=<rid>))
ORDER BY ts.DevelopCost;
```

### Response Format

1. **Current Situation** - Brief summary of where they are
2. **Immediate Priority** - The ONE thing they should do next
3. **Next Steps** - 2-3 follow-up actions after the priority
4. **Learn More** - Links to relevant manual sections

Keep responses concise and actionable. Ask clarifying questions if needed.

### Comprehensive Status Checklist

When analyzing a game, check all of these and report status:

| Check | Query/Method |
|-------|--------------|
| Research progress | FCT_ResearchProject with FCT_TechSystem join |
| Research queue | FCT_ResearchQueue — check for idle labs |
| Academy Commandant | CommandType=17 assigned to population |
| Fleet Organization | FCT_Fleet and FCT_NavalAdminCommand |
| Naval Command Officers | Commanders with CommandType=12 |
| Shipyard Activity | TaskType, RequiredBP, CompletedBP in FCT_Shipyard |
| **Production Queue** | FCT_IndustrialProjects — **CRITICAL: warn if empty!** |
| **Idle Construction** | Compare CFs to production queue — **ALWAYS CHECK** |
| Mineral Stockpiles | FCT_Population mineral columns (watch Sorium!) |
| Ship Count | FCT_Ship count |

**CRITICAL: Always check for idle construction capacity!**

```sql
-- Check production queue (empty = idle CFs!)
SELECT Description, Amount, Percentage FROM FCT_IndustrialProjects WHERE PopulationID=<popid>;

-- Check CF count to calculate idle capacity
SELECT pi.Amount FROM FCT_PopulationInstallations pi
WHERE pi.PopID=<popid> AND pi.PlanetaryInstallationID=2;
```

If production queue is empty and CFs > 0, **immediately warn the player** and suggest:
- Research Labs (2,400 BP) — if running < 30 labs
- Mines (120 BP) — if mineral stockpiles are low
- Fuel Refineries (120 BP) — if fuel/Sorium is low
- Maintenance Facilities (150 BP) — if fleet is growing
- Naval Shipyard (2,400 BP) — if planning multiple ship classes

Report as a summary table:
```
| Check | Status |
|-------|--------|
| Research | ... |
| Academy Commandant | ... |
| Fleet Organization | ... |
| Naval Commands | ... |
| Shipyards | ... |
| **Production Queue** | ⚠️ EMPTY — X CFs idle! |
```

---

## Manual Reference Guide

When coaching, read relevant manual sections and cite them. Use the GitHub Pages URL format:
`https://erikevenson.github.io/aurora-manual/<chapter>/<file>.html`

### Manual Chapters by Topic

| Topic | Chapter | Key Files |
|-------|---------|-----------|
| Getting started | `2-game-setup/` | `2.1-new-game-options.md`, `2.5-starting-conditions.md` |
| Research | `7-research/` | `7.1-technology-tree.md`, `7.2-scientists.md`, `7.3-research-facilities.md` |
| Ship design | `8-ship-design/` | `8.1-design-philosophy.md`, `8.3-engines.md`, `8.4-sensors.md` |
| Shipyards | `9-fleet-management/` | `9.1-shipyards.md`, `9.2-construction-and-refit.md` |
| Survey ops | `17-exploration/` | `17.1-geological-survey.md`, `17.2-gravitational-survey.md` |
| Colonies | `5-colonies/` | `5.1-establishing-colonies.md`, `5.2-population.md` |
| Mining | `6-economy-and-industry/` | `6.1-minerals.md`, `6.2-mining.md` |
| Fuel | `14-logistics/` | `14.1-fuel.md` |
| Combat | `12-combat/` | `12.0-combat-overview.md`, `12.2-beam-weapons.md`, `12.3-missiles.md` |
| Sensors | `11-sensors-and-detection/` | `11.0-sensor-overview.md`, `11.2-passive-sensors.md` |
| Navigation | `10-navigation/` | `10.1-movement-mechanics.md`, `10.2-jump-transit.md` |
| Commanders | `16-commanders/` | `16.2-skills-and-bonuses.md`, `16.3-assignments.md` |

### Phase-Specific Manual References

**Phase 0 (Conventional Start):**
- Read `7-research/7.1-technology-tree.md` for TN tech explanation
- Read `2-game-setup/2.5-starting-conditions.md` for conventional vs TN start differences

**Phase 1 (Early TN):**
- Read `8-ship-design/8.1-design-philosophy.md` for first ship design guidance
- Read `8-ship-design/8.4-sensors.md` for survey sensor details
- Read `9-fleet-management/9.1-shipyards.md` for retooling shipyards

**Phase 2 (Exploration):**
- Read `17-exploration/17.1-geological-survey.md` for mineral surveying
- Read `17-exploration/17.2-gravitational-survey.md` for finding jump points
- Read `14-logistics/14.1-fuel.md` for fuel harvesting

**Phase 3 (Expansion):**
- Read `5-colonies/5.1-establishing-colonies.md` for colony setup
- Read `6-economy-and-industry/6.2-mining.md` for mining operations
- Read `10-navigation/10.2-jump-transit.md` for jump mechanics

**Phase 4 (Contact Preparation):**
- Read `12-combat/12.0-combat-overview.md` for combat basics
- Read `8-ship-design/8.5-weapons.md` for weapon design
- Read `11-sensors-and-detection/11.0-sensor-overview.md` for detection mechanics

### How to Cite Manual Sections

When referencing manual content:
1. Read the relevant file using the Read tool
2. Summarize the key points for the player
3. Provide the URL for further reading

Example citation format:
> For more details on survey sensors, see [Section 8.4: Sensors](https://erikevenson.github.io/aurora-manual/8-ship-design/8.4-sensors.html)

### Searching the Manual

Use Grep to find specific topics:
```bash
# Find mentions of a mechanic
grep -r "fuel consumption" --include="*.md"

# Find formulas
grep -r "formula\|calculation" --include="*.md"
```

---

## Gravitational Survey Queries

**Jump points in a system:**
```sql
SELECT WarpPointID, Distance, Bearing, Xcor, Ycor
FROM FCT_JumpPoint WHERE SystemID=<sysid>;
```

**Jump points known to player:**
```sql
SELECT jp.WarpPointID, jp.Distance, rjps.Explored, rjps.Charted
FROM FCT_JumpPoint jp
JOIN FCT_RaceJumpPointSurvey rjps ON jp.WarpPointID = rjps.WarpPointID
WHERE jp.SystemID=<sysid> AND rjps.RaceID=<rid>;
```

**System grav survey status:**
```sql
SELECT Name, SurveyDone FROM FCT_RaceSysSurvey
WHERE SystemID=<sysid> AND RaceID=<rid>;
```

**Standing orders (for reference):**
```sql
SELECT OrderID, Description FROM DIM_StandingOrders
WHERE Description LIKE '%Survey%' OR Description LIKE '%Grav%';
```

Key standing orders:
- OrderID 6: MV: Geosurvey System
- OrderID 10: MV: Gravsurvey System
- OrderID 5: SV: Survey Location

### Grav Survey Troubleshooting

**If "MV: Gravsurvey System" reports "unable to carry out standing orders":**

1. Check if system is already fully surveyed (SurveyDone=1 in FCT_RaceSysSurvey)
2. Standing orders have a **10 billion km distance threshold** — distant survey locations may be out of range
3. **Solution:** Use manual survey orders instead:
   - In Task Group Orders window, check **"Survey Locations"** checkbox
   - A list of survey locations appears
   - Select specific locations to survey manually
   - This bypasses the standing order distance limit

**To help player visualize survey progress:**
- System Map (F3) > Display tab > Enable "Show JP Survey Locations"
- Unsurveyed locations = empty white circles
- Surveyed locations = filled circles
- Jump points labeled JP1, JP2, etc.
