---
title: "Example: Exploration Workflow"
parent: "Examples"
nav_order: 99
---

# Example: Exploration Workflow

*Updated: v2026.01.26*

This worked example walks through the systematic exploration of a newly discovered star system, from initial jump point transit through colonization assessment. It demonstrates gravitational survey, geological survey, xenoarchaeology, and the decision-making process for evaluating colonization candidates.

## Starting Conditions

*Updated: v2026.01.24*
- **Situation:** Your gravitational survey ship has discovered a new jump point in your home system (Sol)
- **Available Assets:**
  - 1x Gravitational Survey Ship ("GSS Pathfinder"): 4,500 tons, 2x grav survey sensors, jump drive, speed 3000 km/s
  - 1x Geological Survey Ship ("GSS Prospector"): 3,200 tons, 3x geo survey sensors, jump drive, speed 2500 km/s
  - 1x Escort Frigate ("FFS Guardian"): 6,000 tons, beam armament, jump drive, speed 4500 km/s
  - Small colony fleet on standby (freighters, colony ships)
- **Known Information:** Nothing about what lies beyond the jump point. The destination is completely unknown.

---

## Step 1: Initial Transit

*Updated: v2026.01.24*
### Pre-Transit Checklist

Before sending ships through an unknown jump point:

- **Fuel status:** Ensure sufficient fuel for round-trip plus extended operations. The return jump point may be far from the entry point.
- **Maintenance:** Ships should be freshly overhauled. Long deployments in unexplored space have no maintenance facilities.
- **Sensors:** Decide passive-only vs active. Active sensors reveal more but also broadcast your presence.
- **Escort decision:** Send the escort or scout first? (See Key Decisions below.)

### Transit Sequence

1. **Send Pathfinder through first** (with Guardian escort trailing). The grav survey ship has jump capability and can begin surveying immediately.
2. **Upon transit, immediately assess:**
   - Star type and luminosity (determines habitable zone)
   - Number of visible bodies (planets, moons, asteroid belts)
   - Any detected thermal/EM signatures (hostile presence)
   - Distance to return jump point (critical for fuel planning)

### What You Learn Immediately

The system map populates with:

- Primary star characteristics
- All planets and major moons (positions, basic orbital data)
- Asteroid belts (if present)
- Visible gravitational survey locations (but no jump points until surveyed)

### Example System Discovery

"Barnard's Star" system revealed:

- M-class red dwarf (low luminosity, compact habitable zone)
- 6 planets: 1 gas giant, 3 terrestrial, 1 dwarf planet, 1 ice giant
- 2 asteroid belts
- 22 gravitational survey locations detected
- No thermal or EM signatures (no obvious hostile presence)

---

## Step 2: Gravitational Survey

*Updated: v2026.01.26*
### Purpose

Find all jump points in the system. Each jump point is a potential route to further systems -- or a potential invasion corridor. You need to map them all.

### Survey Mechanics

Each gravitational survey location requires survey points to investigate. Survey sensors generate points per hour \hyperlink{ref-ex-explore-1}{[1]}:

```
Survey Time per Location = Points Required / (Sensor Survey Points per Hour)
```

Pathfinder has 2x Improved grav survey sensors, each generating 2 survey points/hour \hyperlink{ref-ex-explore-1}{[1]}:
```
Total generation: 4 points/hour (96 points/day)
Average location requirement: ~100-200 points
Time per location: 100/4 = 25 hours to 200/4 = 50 hours (1-2 days)
```

### Time Estimate for Full System

With 22 survey locations:
```
Survey time (locations only): 22 x 1.5 days average = 33 days of active surveying
Transit time between locations: varies by distance and ship speed

Assuming average transit of 50M km between locations at 3000 km/s:
  Transit per location: 50,000,000 / 3000 / 3600 = ~4.6 hours = 0.19 days
  Total transit: 22 x 0.19 = ~4.2 days

Total gravitational survey estimate: ~37 days (~1.2 months)
```

### Survey Strategy

Use the "Survey All Locations" order for efficiency. The ship automatically routes between locations in an optimized order.

**Priority override:** If the galactic map shows neighboring stars in a specific direction, manually prioritize survey locations on that side of the system first.

### Expected Results

Of 22 survey locations, typically 20-40% contain jump points:

- Expect 4-9 jump points discovered
- Each connects to a different neighboring system
- All represent both opportunities and potential threats

### For This Example

After 59 days, Pathfinder discovers:

- **6 jump points** found (out of 22 locations surveyed)
- 16 locations empty
- System has multiple routes for further exploration

---

## Step 3: Geological Survey

*Updated: v2026.01.26*
### Purpose

Determine mineral deposits on all bodies. Without geological survey, you have zero knowledge of what resources exist.

### Running Parallel with Grav Survey

While Pathfinder conducts gravitational survey, send Prospector into the system to begin geological surveys simultaneously. This halves your total exploration time.

### Survey Point Requirements by Body Type

Survey point requirements are calculated dynamically based on body characteristics and are not stored as fixed values in the game database. The following are approximate ranges observed during gameplay *(community estimates — not verified against source code)* \hyperlink{ref-ex-explore-5}{[5]}:

| Body Type | Typical Survey Points | Time (3 sensors x 30 pts/day = 90/day) |
|-----------|----------------------|---------------------------------------|
| Gas Giant | 500+ | 5.5+ days |
| Terrestrial Planet | 200-400 | 2.2-4.4 days |
| Large Moon | 100-200 | 1.1-2.2 days |
| Small Moon | 50-100 | 0.6-1.1 days |
| Dwarf Planet | 100-200 | 1.1-2.2 days |
| Asteroid | 10-50 | 0.1-0.6 days |
| Comet | 10-50 | 0.1-0.6 days |

### Survey Order Priority

1. **Gas giants first:** They are the only source of Sorium (fuel). Knowing if the system has harvestable fuel is critical for planning extended operations.
2. **Terrestrial planets in habitable zone:** Potential colony sites with both mineral and habitability value.
3. **Large moons of gas giants:** Often mineral-rich with moderate accessibility.
4. **Inner system bodies:** Closer to likely colony positions.
5. **Asteroid belts:** High accessibility deposits common, but small quantities.
6. **Outer system bodies and comets:** Survey last unless specifically needed.

### Time Estimate for Full System

Barnard's Star system bodies:
```
1 Gas Giant: ~6 days
3 Terrestrial Planets: ~3.5 days each = 10.5 days
Ice Giant: ~5 days
Dwarf Planet: ~1.5 days
Moons (estimate 8 total): ~1.5 days each = 12 days
Asteroid belt bodies (estimate 20): ~0.3 days each = 6 days
Transit time between bodies: ~15 days total (spread across the system)

Total geological survey estimate: ~56 days (2 months)
```

### Survey Results (Example)

After completing geological surveys, Prospector reports:

| Body | Key Minerals | Quantity | Accessibility | Notes |
|------|-------------|----------|---------------|-------|
| Planet II | Duranium | 2.1M tons | 0.7 | Excellent deposit |
| Planet II | Gallicite | 450K tons | 0.5 | Good -- scarce mineral |
| Planet II | Neutronium | 800K tons | 0.6 | Solid armor source |
| Planet III | Corundium | 300K tons | 0.3 | Low access |
| Planet III | Vendarite | 150K tons | 0.8 | High access, low quantity |
| Gas Giant | Sorium | Harvestable | N/A | Fuel source confirmed |
| Moon IVa | Mercassium | 600K tons | 0.9 | Excellent for research |
| Moon IVa | Boronide | 200K tons | 0.4 | Moderate |
| Asteroid Belt | Mixed | Small deposits | 0.8-1.0 | High access, low volume |

**Ruins detected on Planet III!** Geological survey reveals xenoarchaeological sites present.

---

## Step 4: Evaluate Results

*Updated: v2026.01.26*
### Mineral Wealth Assessment

Evaluate deposits using effective yield (Quantity x Accessibility):

```
Effective Yield = Quantity x Accessibility

Planet II Duranium: 2,100,000 x 0.7 = 1,470,000 effective tons
Planet II Gallicite: 450,000 x 0.5 = 225,000 effective tons
Moon IVa Mercassium: 600,000 x 0.9 = 540,000 effective tons
```

**Critical mineral check:** Gallicite (engines) and Sorium (fuel) are common bottlenecks. This system has both -- a significant finding.

### Habitability Assessment

Check colony cost for each terrestrial body:

```
Colony Cost = Max(Environmental Penalties)
  - Temperature deviation from ideal
  - Atmospheric pressure deviation
  - Hostile gas presence
  - Gravity deviation
```

> **Note:** In C# Aurora, Colony Cost equals the single worst (maximum) environmental factor, not the sum of all factors. Only the highest penalty applies.

| Body | Temperature | Atmosphere | Gravity | Colony Cost | Verdict |
|------|------------|-----------|---------|-------------|---------|
| Planet II | -15C (cold but viable) | 0.8 atm N2/O2 | 0.85G | 0.5 | Good candidate |
| Planet III | +45C (warm) | 1.2 atm, some CO2 | 1.1G | 1.8 | Needs infrastructure |
| Planet IV | -80C | Thin CO2 | 0.6G | 4.2 | Expensive to colonize |

### Strategic Position Assessment

- **Jump point connections:** 6 jump points -- this is a crossroads system
- **Distance from home:** 1 jump from Sol -- close enough for easy logistics
- **Defensive considerations:** Multiple approach vectors means multiple defense requirements
- **Fuel availability:** Gas giant with Sorium enables local fuel production

---

## Step 5: Priority Assessment

*Updated: v2026.01.26*
### Ranking Colonization Candidates

| Rank | Body | Rationale | Priority |
|------|------|-----------|----------|
| 1 | Planet II | Low colony cost, excellent minerals (Duranium, Gallicite, Neutronium) | Immediate |
| 2 | Moon IVa | High-access Mercassium for research, moderate Boronide | Medium-term |
| 3 | Planet III | Ruins for xenoarchaeology, moderate minerals | Medium-term |
| 4 | Gas Giant orbit | Fuel harvesting station | When needed |
| 5 | Asteroids | High-access small deposits | Late-game |

### Value Threshold

A body is worth colonizing when:
```
Expected annual mineral output > Cost of colony infrastructure + transport investment

Annual output per mine = Base_Production x Accessibility x Tech_Modifier
  For Planet II Duranium at 0.7 access: 10 x 0.7 = 7.0 tons/mine/year
  With 50 mines: 350 tons/year of Duranium

Compare to: cost of infrastructure (if CC > 0), population transport, mine transport
```

For Planet II (CC = 0.5):
```
Infrastructure needed = Population x Colony_Cost = Population x 0.5
Per 1M colonists: 500,000 infrastructure units required
```

This is manageable. The mineral deposits justify the investment.

---

## Step 6: Colony Decision

*Updated: v2026.01.24*
### Planet II -- Primary Colony

**Go/No-Go Assessment:**

- Colony Cost: 0.5 (low -- reasonable infrastructure requirement)
- Key minerals: Duranium (2.1M @ 0.7), Gallicite (450K @ 0.5), Neutronium (800K @ 0.6)
- Strategic value: Close to Sol (1 jump), fuel source nearby

**Decision: COLONIZE**

**Required infrastructure calculation:**
```
Required Infrastructure = Population x Colony_Cost
For initial 1M colonists: 1,000,000 x 0.5 = 500,000 infrastructure units
Max Supported Population = Infrastructure / Colony_Cost
```

### What to Send First

Deploy in this order:

| Priority | Cargo | Purpose | Ships |
|----------|-------|---------|-------|
| 1 | Infrastructure (500K units) | Support initial population | Freighters |
| 2 | Colonists (1M) | Workforce for mines | Colony ship |
| 3 | Automated Mines (50) | Begin mineral extraction | Freighter |
| 4 | Construction Factories (20) | Local production capability | Freighter |
| 5 | Fuel Refineries (10) | Local fuel production | Freighter |

### Planet III -- Xenoarchaeology Site

**Decision: DEPLOY XENO TEAMS** (do not require full colonization immediately)

Since ruins were detected, deploy xenoarchaeology formations. If the body has CC > 0, you need minimal infrastructure to support the teams. The ruins may contain technologies worth decades of research.

---

## Step 7: Route Security

*Updated: v2026.01.24*
### Threat Assessment

Before committing civilian assets, verify the system is secure:

1. **Active sensor sweep:** Run Guardian's active sensors across the system
2. **Check for NPR signatures:** Any thermal or EM contacts?
3. **Monitor jump points:** Unknown systems beyond may contain hostiles
4. **Spoiler race indicators:** Check for anomalous readings that might indicate spoiler races

### For This Scenario

No contacts detected. However, 6 jump points represent 6 potential threat vectors. Establish security:

### Patrol Routes

- **Guardian** patrols between the 3 nearest jump points on a repeating cycle
- **Sensor coverage:** Ensure passive sensors cover all jump point approaches
- **Warning time:** Calculate how long an enemy fleet would take to reach the colony from each jump point
- **Response plan:** If hostiles detected, evacuate survey ships first, then civilian traffic

### When to Expand Escort Force

Assign additional warships when:

- Civilian traffic (freighters, colony ships) begins regular runs
- Any jump point leads to a system with detected contacts
- Colony value justifies the defense investment
- Multiple simultaneous survey missions stretch escort coverage

---

## Step 8: Infrastructure Deployment

*Updated: v2026.01.24*
### Phase 1: Initial Colony (Months 1-6)

```
Month 1: Transport infrastructure and initial colonists to Planet II
Month 2: Colony established, mines begin deployment
Month 3: First mineral extraction begins
Month 4: Fuel harvester deployed at gas giant (if fuel needed)
Month 5: Additional mines and population transports
Month 6: Colony producing meaningful mineral output
```

### Phase 2: Expansion (Months 6-18)

- Increase mine count based on mineral accessibility
- Add construction factories for local production
- Consider fuel refineries if gas giant Sorium is accessible
- Begin xenoarchaeology operations on Planet III

### Transport Logistics

**Freighter requirements:**

```
Infrastructure: 500K units at (assume) 25,000 tons per freighter load
  Loads needed: 500,000 / 25,000 = 20 loads
  With 2 freighters at round-trip time of 30 days: 20 loads / 2 = 10 trips = 300 days
```

This is slow. More freighters significantly accelerate colony establishment. Consider:

- 4 freighters: 150 days to full infrastructure deployment
- 6 freighters: 100 days

**Tip:** Automate freight routes early. Set standing orders: load minerals at Planet II, unload at Earth, load infrastructure at Earth, unload at Planet II. Repeat.

---

## Step 9: Ongoing Exploration

*Updated: v2026.01.25*
### Pushing the Frontier

With Barnard's Star mapped and colonization underway, continue exploration through the 6 discovered jump points.

### Exploration Doctrine

| Strategy | Approach | Best For |
|----------|----------|----------|
| Breadth-First | Survey all adjacent systems before pushing deeper | Security-focused |
| Depth-First | Follow one chain of systems to maximum depth | Finding distant targets |
| Priority-Based | Focus on promising star types and directions | Resource-focused |

### For This Scenario

**Recommended: Breadth-first for the first ring, then priority-based.**

1. Send Pathfinder through each of the 6 jump points (passive sensors only for initial peek)
2. Catalog the star type and body count of each adjacent system
3. Prioritize systems with:
   - G/K class stars (better habitable zone prospects)
   - Multiple planets (more survey targets)
   - No detected hostiles
4. Begin full grav+geo survey of the 2-3 most promising systems
5. Leave hostile or uninteresting systems for later

### Jump point safety

From Appendix C: "Never transit an unknown jump point with your only survey ship unless you are certain you can get back."

```
Safety check before transit:
  1. Current fuel: sufficient for round trip?
  2. Return jump point distance: unknown until you arrive
  3. Backup plan: tanker on standby? Second ship available for rescue?
```

**Rule of thumb:** Carry at least 150% of estimated fuel needs when entering unknown systems. The return jump point may be on the opposite side of the system.

---

## Step 10: Xenoarchaeology

*Updated: v2026.01.24*
### Deploying Xenoarchaeology Teams

Ruins were detected on Planet III during geological survey. To exploit them:

### Team Composition

Design a xenoarchaeology vehicle:

- Base type: Standard Vehicle (or larger for more components)
- Component: Xenoarchaeology equipment (100 tons, provides 0.5 xeno points per component)
- Total element size: ~218 tons (component + vehicle base + armor)

### Formation Design

A typical xenoarchaeology formation:

| Element | Quantity | Xeno Points Each | Total Points |
|---------|----------|-----------------|-------------|
| Xeno Vehicle | 40 | 0.5 | 20 |
| HQ Vehicle | 5 | 0 | -- |
| Logistics Vehicle | 5 | 0 | -- |
| **Total** | **50** | | **20 points** |

Transport tonnage: ~50 x 218 = ~10,900 tons

### Recovery Rate Calculation

```
Annual translation probability = Total xenoarchaeology points
For our formation: 20% annual chance of successful recovery per year
```

**To improve odds, deploy multiple formations:**

| Formations Deployed | Total Xeno Points | Annual Recovery Chance |
|--------------------|--------------------|----------------------|
| 1 | 20 | 20% |
| 2 | 40 | 40% |
| 3 | 60 | 60% |
| 5 | 100 | 100% (guaranteed annual recovery) |

### Construction Phase Scaling

For shorter time increments:
```
Chance per phase = Annual probability x (Phase duration / 1 year)

For a 5-day construction phase with 40 xeno points:
  = 40% x (5 / 365) = 0.55% per phase
```

### What You Might Find

Ruins contain technologies up to a maximum cost determined by the ruin race level:

```
Max Tech Cost = (2 ^ (Ruin Race Level + 1)) x 1000 RP

Level 1 ruins: up to 4,000 RP technologies
Level 3 ruins: up to 16,000 RP technologies
Level 5 ruins: up to 64,000 RP technologies (game-changing)
```

Possible discoveries:

- Weapons technology (beam weapons, warheads)
- Propulsion technology (engines, fuel efficiency)
- Sensor technology (advanced sensors, fire control)
- Defensive technology (armor, shields)
- Research point bonuses
- Functional alien installations
- Alien artifacts (trade commodity)

### Establishing the Excavation Colony

Planet III has colony cost 1.8. Required infrastructure:
```
For 1M population to operate xeno teams:
  Infrastructure needed = 1,000,000 x 1.8 = 1,800,000 units
```

This is expensive. Consider whether the ruins justify the investment:

- High-level ruins (Level 3+): Absolutely worth it
- Low-level ruins (Level 1): May not justify the infrastructure cost unless conveniently located
- Check if the body has minerals that also justify colonization (dual-purpose colony)

For this scenario, Planet III has moderate minerals (Corundium, Vendarite) plus ruins. The combined value justifies colonization.

---

## Timeline Summary

*Updated: v2026.01.24*
| Phase | Duration | Activities |
|-------|----------|-----------|
| **Week 1** | Days 1-7 | Initial transit, system assessment, begin grav survey |
| **Months 1-2** | Days 1-59 | Gravitational survey (all 22 locations) |
| **Months 1-2** | Days 1-56 | Geological survey (parallel with grav survey) |
| **Month 3** | Days 60-90 | Evaluate results, make colonization decisions |
| **Months 3-6** | Days 60-180 | Deploy initial colony infrastructure to Planet II |
| **Months 4-8** | Days 90-240 | Deploy xeno teams to Planet III ruins |
| **Months 6-12** | Days 180-365 | Colony operational, ongoing exploration of adjacent systems |
| **Year 1+** | Ongoing | Mineral production, tech recovery, frontier expansion |

### Total System Exploration Time

```
Gravitational survey: ~59 days
Geological survey: ~56 days (running parallel)
Total time until system fully mapped: ~59 days (limited by grav survey)
Add xenoarchaeology deployment: +30 days transport
First xeno recovery (at 20%/year): expected ~5 years (stochastic)
```

---

## Key Decisions

*Updated: v2026.01.24*
| Decision | Conservative | Aggressive | This Example |
|----------|-------------|-----------|-------------|
| Escort survey ships? | Always escort | Solo (faster, riskier) | Escort (unknown space) |
| Survey order? | Gas giants first (fuel) | Habitable planets first | Gas giant, then habitable zone |
| How deep to push? | Fully map each system before moving on | Push through all jump points immediately | Map this system fully, then peek at neighbors |
| When is a system "not worth it"? | No minerals above 0.3 access | Any minerals justify a colony | CC < 2.0 AND meaningful mineral deposits |
| Colonize immediately? | Wait until fully surveyed | Colonize first promising body | Survey complete, then colonize best candidate |

---

## Common Mistakes

*Updated: v2026.01.26*
1. **Sending surveyors without escort into unknown space.** Survey ships are unarmed. One hostile contact means a dead ship and months of lost survey data. Escort in unknown systems.

2. **Not surveying gas giants.** They are the only source of harvestable Sorium (fuel). Skipping them means missing a potential fuel source that could sustain extended operations in the system.

3. **Ignoring jump points leading further afield.** Every unmapped jump point is a potential threat axis. Even if you do not plan to explore immediately, know what directions are available.

4. **Colonizing the first mineral find without comparing options.** Survey the whole system first. The second planet might have better deposits at higher accessibility. Patience in evaluation saves decades of suboptimal mining.

5. **Forgetting transit fuel costs.** Survey ships moving between widely-spaced survey locations burn fuel. A ship that runs out of fuel in an unexplored system may be stranded permanently.

6. **Not checking colony cost before sending colonists.** Sending 5M colonists to a CC-3.0 world without infrastructure means population attrition from day one. Infrastructure first, colonists second.

7. **Neglecting route security as colonies grow.** A mining colony producing 500 tons of Gallicite per year is worth defending. Assign patrol ships as colony value increases.

8. **Single survey ship bottleneck.** One ship surveying a 40-body system takes months. Two ships cut the time in half. Three or four survey ships exploring simultaneously is far more efficient than relying on a single vessel.

9. **Abandoning ruins prematurely.** Xenoarchaeology is stochastic. You might go 3 years without a find, then discover a game-changing technology. Patience pays dividends.

10. **Not establishing fuel infrastructure.** If the system has a gas giant with Sorium, deploy fuel harvesters. Local fuel production eliminates dependency on fuel shipments from home.

---

## References

\hypertarget{ref-ex-explore-1}{[1]}. Aurora C# game database (AuroraDB.db v2.7.1) -- Survey sensors generate survey points per hour (not per day). Verified against in-game sensor output display and Appendix A survey formulas.

\hypertarget{ref-ex-explore-2}{[2]}. Aurora C# game database (AuroraDB.db v2.7.1) -- Colony cost uses the single worst (maximum) environmental factor, not the sum of all factors. See Section 5.3 Environment for the complete CC calculation.

\hypertarget{ref-ex-explore-5}{[5]}. Survey point requirements per body type are not stored as fixed values in AuroraDB.db. The FCT\_SystemBody table tracks body characteristics (Radius, Mass, BodyClass) but survey point counts appear to be calculated dynamically by the game engine. Values in this table are community estimates based on observed gameplay.

---

## Related Sections

- [Section 10.2 Jump Transit](../10-navigation/10.2-jump-transit.md) -- Jump point mechanics, transit, and jump gates
- [Section 17.1 Geological Survey](../17-exploration/17.1-geological-survey.md) -- Survey sensors, mineral discovery, ground survey
- [Section 17.2 Gravitational Survey](../17-exploration/17.2-gravitational-survey.md) -- Finding jump points, survey locations, exploration strategy
- [Section 17.3 Xenoarchaeology](../17-exploration/17.3-xenoarchaeology.md) -- Ruins, excavation, recovered technology
- [Section 5.1 Establishing Colonies](../5-colonies/5.1-establishing-colonies.md) -- Colony cost, infrastructure, population management
- [Section 4.1 Star Systems](../4-systems-and-bodies/4.1-star-systems.md) -- System composition, body types
- [Appendix A: Formulas](../appendices/A-formulas.md) -- Production, mining, and growth calculations
- [Appendix C: Tips and Common Mistakes](../appendices/C-tips-and-mistakes.md) -- General gameplay advice
