# Example: Early Game Economic Bootstrap

*Added: v2026.01.24*

This worked example walks through the first 10 years of a conventional-start Aurora C# game, showing how to transition from pre-TN industry to a functioning trans-newtonian economy capable of supporting fleet expansion and interstellar exploration.

## Objective

Starting from a conventional-technology Earth with no trans-newtonian (TN) knowledge, build a self-sustaining TN economy that can:

- Produce ships and installations at meaningful rates
- Generate sufficient fuel for fleet operations
- Mine minerals faster than you consume them
- Support a survey fleet exploring the home system
- Begin military preparations by year 10

## Starting Conditions (Conventional Start)

| Resource | Starting Value |
|----------|---------------|
| Population | ~1,000 million (~400M in manufacturing sector) |
| Conventional Industry | ~1,600 factories (8x manufacturing population) |
| TN Technology | None (must research) |
| Mineral Deposits | Earth standard (moderate, mixed accessibility) |
| Research Labs | ~16 (1 per 12M manufacturing pop; conventional, not TN) |
| Shipyards | 0 |
| Fuel Reserves | 0 |
| Scientists | 5-8 (randomized) |

> **Note:** Starting values are determined by population and manufacturing ratios. See [Section 2.5.1 Starting Conditions](../2-game-setup/2.5-starting-conditions.md) for detailed starting condition mechanics. Conventional research labs ARE present at game start and can begin researching TN Technology immediately -- you do not need to build labs first.

**Key constraint:** Conventional industry cannot build TN installations. You must research Trans-Newtonian Technology before ANY TN production begins. Every day spent before completing that research is a day your TN economy is not growing.

---

## Step 1: Research Priorities (Years 0-3)

### First Research Project: Trans-Newtonian Technology

**Cost:** 5,000 RP
**Priority:** ABSOLUTE FIRST. Nothing else matters until this completes.

Before this research finishes, you have zero ability to build TN installations. After it completes, your conventional factories immediately gain the ability to construct TN installations (mines, research labs, construction factories, fuel refineries, etc.).

**Estimated completion:** 2-3 years depending on scientist skill and starting lab count (~16 conventional labs are available from game start).

### Research Order After TN Technology

| Priority | Technology | Category | Cost (RP) | Reasoning |
|----------|-----------|----------|-----------|-----------|
| 1st | Trans-Newtonian Technology | Construction | 5,000 | Unlocks everything |
| 2nd | Construction Rate (Improved) | Construction | 2,000 | 12 BP/factory (20% boost to ALL production) |
| 3rd | Nuclear Thermal Engine | Power/Propulsion | ~2,000 | First TN engine -- enables ship design |
| 4th | Mining Production (Improved) | Construction | 2,000 | 1.2x mine output |
| 5th | Pressurised Water Reactor | Power/Propulsion | ~2,000 | Powers ship systems |
| 6th | Active Sensor Strength | Sensors/FC | ~2,000 | Enables survey sensor design |
| 7th | Geological Survey Sensor | Sensors/FC | ~1,000 | For survey ships |
| 8th | Gravitational Survey Sensor | Sensors/FC | ~1,000 | For jump point detection |

**Rationale:** Construction Rate first because it compounds -- every factory you build afterward is 20% more productive. Engines and reactors next because you need ships. Mining production improves mineral income. Sensors enable survey vessels.

### Research Lab Expansion Timeline

You start with ~16 conventional research labs. These function immediately and should be assigned to TN Technology research on day one. You cannot build additional TN labs until TN Technology completes, but your starting labs provide meaningful research output from the start.

| Year | Labs | RP/Year (approx) | Notes |
|------|------|-------------------|-------|
| 0-1 | ~16 | ~160 (conventional) | Starting labs researching TN tech |
| 1-2 | 20 | ~200 | First TN labs added to starting pool |
| 2-3 | 25 | ~250 | Steady TN lab expansion |
| 3-5 | 30 | ~300 | Good research capacity |
| 5-7 | 35-40 | ~350-400 | Strong research base |
| 7-10 | 40-50 | ~400-500 | Mature research base |

**Lab cost:** 2,400 BP and 1,200 Duranium + 1,200 Mercassium each \hyperlink{ref-ex-economy-5}{[5]}. This is expensive -- prioritize labs carefully against other construction needs.

---

## Step 2: Conventional Industry Utilization (Years 0-2)

While waiting for TN Technology to complete, your conventional factories should not sit idle. Build items that remain useful after TN transition:

### Recommended Conventional-Era Builds

| Installation | Priority | Reasoning |
|-------------|----------|-----------|
| Infrastructure | HIGH | Always needed for off-world colonies later |
| Financial Centers | MEDIUM | Generate wealth for ongoing operations |
| Ground Forces | LOW | Basic planetary defense (not urgent) |

**Financial Centers:** Each Financial Center generates 0.25 wealth per year and requires 50,000 workers \hyperlink{ref-ex-economy-1}{[1]}. Converting conventional factories to Financial Centers costs 20 BP and 20 Corbomite per conversion \hyperlink{ref-ex-economy-2}{[2]}. This is a solid pre-TN investment because wealth generation supports your economy throughout the game.

**Infrastructure:** At only 2 BP and 1 Duranium + 1 Mercassium each, infrastructure is cheap and will be essential for any future off-world colonies. Stockpile 500-1,000 units during the conventional phase.

### What NOT to Build Conventionally

- Weapons (no ships to mount them on yet)
- Missiles (no launchers or ships)
- Ground military units beyond basic defense (resources better spent on economy)

---

## Step 2.5: CI-to-TN Conversions (Years 1-3)

*Added: v2026.01.28*

Once Trans-Newtonian Technology completes, a powerful option unlocks: converting Conventional Industry (CI) directly into TN installations. This is **six times cheaper** than building new and should be your first action after TN tech completes. \hyperlink{ref-ex-economy-6}{[6]}

### Conversion Economics

| Method | BP Cost | Result |
|--------|---------|--------|
| Build new TN installation | 120 BP | 1 installation |
| Convert CI to TN installation | 20 BP | 1 installation |

**Savings:** 100 BP per installation (83% discount). With ~1,600 CI units at game start, converting even 200 of them saves 20,000 BP compared to building new.

### Available Conversions

After TN Technology research, the Industry tab shows these conversion options:

| Target Installation | Conversion Cost | Minerals Required |
|---------------------|-----------------|-------------------|
| Construction Factory | 20 BP | 10 Duranium, 10 Neutronium |
| Mine | 20 BP | 20 Corundium |
| Fuel Refinery | 20 BP | 20 Boronide |
| Ordnance Factory | 20 BP | 20 Tritanium |
| Fighter Factory | 20 BP | 20 Vendarite |
| Financial Centre | 20 BP | 20 Corbomite |

### Recommended Conversion Priority

**Priority 1: Construction Factories (50-100 conversions)**

Construction factories compound -- each one helps build more installations faster. Converting 100 CI to construction factories costs only 2,000 BP and 1,000 each of Duranium and Neutronium. Building them new would cost 12,000 BP.

**Priority 2: Mines (50-100 conversions)**

Mines generate the mineral income that funds everything else. Converting 100 CI to mines costs 2,000 BP and 2,000 Corundium. Check your Corundium stockpile first.

**Priority 3: Fuel Refineries (25-50 conversions)**

You need fuel before ships can operate. Converting 50 CI to refineries costs 1,000 BP and 1,000 Boronide.

### Mineral Bottleneck Warning

> **Warning:** Conversions consume minerals from your starting stockpile. Before mass-converting, check that you have sufficient reserves:
> - Corundium for mines (20 per conversion)
> - Neutronium for construction factories (10 per conversion)
> - Boronide for fuel refineries (20 per conversion)
>
> If a mineral is scarce, prioritize building mines first (via conversion or new construction) to increase income.

### How Much CI to Retain

CI is immobile -- it cannot be transported off Earth. However, retaining some CI provides flexibility:

- **Financial Centers:** Converting CI to Financial Centers (20 BP + 20 Corbomite) generates ongoing wealth
- **Infrastructure:** CI can build infrastructure cheaply during the transition
- **Buffer:** Retained CI provides backup production capacity

**Recommendation:** Convert 200-300 CI to TN installations immediately, retain 1,000+ for Financial Center conversions and infrastructure production over time.

### Conversion Timeline

| When | Action | BP Cost | Result |
|------|--------|---------|--------|
| TN Tech completes | Convert 100 CI → Construction Factories | 2,000 | Instant 100 factories |
| +1 month | Convert 100 CI → Mines | 2,000 | Instant 100 mines |
| +2 months | Convert 50 CI → Fuel Refineries | 1,000 | Instant 50 refineries |
| Year 2-3 | Convert remaining CI → Financial Centers | Variable | Ongoing wealth |

**Total immediate conversion cost:** ~5,000 BP for 250 TN installations. Building these new would cost 30,000 BP -- a savings of 25,000 BP that accelerates your economy by 1-2 years.

---

## Step 3: First TN Construction Factories (Years 1-3)

Once TN Technology completes, immediately begin building Construction Factories.

### Growth Rate Calculation

```
Annual_BP = Num_Factories x BP_per_Factory
```

At base tech (10 BP/factory/year):

| Factories | Annual BP | Time to Build 1 More Factory (120 BP) |
|-----------|-----------|----------------------------------------|
| 10 | 100 | 1.2 years |
| 20 | 200 | 0.6 years (~7 months) |
| 50 | 500 | 0.24 years (~3 months) |
| 100 | 1,000 | 0.12 years (~44 days) |
| 200 | 2,000 | 0.06 years (~22 days) |

**Strategy:** Construction factories build more construction factories. This is exponential growth -- the earlier you start, the faster it compounds. Dedicate at least 50% of your early production capacity to building more factories.

### Construction Priority Queue (Year 1-3)

After TN Technology completes, build in this order:

```
1. Construction Factories x20 (2,400 BP total)
2. Research Labs x5 (12,000 BP total)
3. Mines x50 (6,000 BP total)
4. Fuel Refineries x10 (1,200 BP total)
5. More Construction Factories x30 (3,600 BP total)
```

**Total early BP needed: ~25,200 BP**

With 200 conventional factories producing at a fraction of TN rate, plus your growing TN factory count, expect to complete this list by approximately year 3-4.

---

## Step 4: Fuel Infrastructure (Years 2-4)

### When to Build Refineries

Build fuel refineries once you have engine technology researched and are designing your first ships. You need fuel stockpiled BEFORE ships launch.

### How Many Refineries

```
Fuel_per_Refinery_per_Year = 40,000 litres (base tech)
```
\hyperlink{ref-ex-economy-4}{[4]}

**Estimate fuel needs:**

- A small survey ship (~2,000 tons) with efficient engines might consume 50-100 litres/hour at cruise speed
- Annual consumption per ship: ~50 x 8,760 hours = 438,000 litres (at constant cruise)
- Realistic annual consumption (including idle time): ~100,000-200,000 litres per survey ship

**Target:** 10 refineries produce 400,000 litres/year at base tech. This supports moderate fleet operations.

### Recommended Fuel Refinery Expansion

| Year | Refineries | Annual Output (litres) | Sufficient For |
|------|-----------|----------------------|----------------|
| 2 | 10 | 400,000 | Moderate operations |
| 3 | 25 | 1,000,000 | Full fleet operations |
| 4 | 50 | 2,000,000 | Large fleet with reserves |
| 5 | 100 | 4,000,000 | Major naval operations |
| 7 | 200 | 8,000,000 | Multiple theatre operations |

**Critical:** Research Improved Fuel Refinery tech (48,000 litres/year) as soon as practical. This increases output by 20% without adding refineries.

### Sorium Depletion Warning

> **Critical:** Earth's Sorium deposits are finite and WILL deplete over time. Monitor your Sorium reserves on the Minerals tab of the Economics window. If reserves drop below 50,000 tons, prioritize establishing alternative fuel sources immediately. Running out of Sorium with no harvesting infrastructure means your fleet is grounded.

### Alternative: Sorium Harvesting

If a gas giant with accessible Sorium exists in your system, consider building a fuel harvester ship by year 4-5. A single harvester can produce more fuel than dozens of ground refineries, but requires a functioning shipyard first. Given the Sorium depletion risk above, this should be treated as a necessity rather than an option.

---

## Step 5: Mine Deployment (Years 1-5)

### Initial Mine Count

Each mine produces 10 tons/year per mineral deposit (at accessibility 1.0) \hyperlink{ref-ex-economy-3}{[3]}. Earth typically has 11 mineral types, each with varying accessibility.

**Target mineral production rate by year 5:** 500+ tons/year of each critical mineral.

### Mine Production Estimates

```
Annual_Production_per_Mineral = Num_Mines x 10 x Accessibility
```

| Mines on Earth | Annual Duranium (acc 0.8) | Annual Gallicite (acc 0.5) |
|---------------|--------------------------|---------------------------|
| 50 | 400 tons | 250 tons |
| 100 | 800 tons | 500 tons |
| 200 | 1,600 tons | 1,000 tons |
| 300 | 2,400 tons | 1,500 tons |

### Mineral Consumption Estimates (Years 1-5)

| Activity | Annual Duranium | Annual Gallicite | Other Minerals |
|----------|----------------|-----------------|----------------|
| 20 Construction Factories | 1,200 | 0 | 1,200 Tritanium |
| 10 Research Labs | 12,000 | 0 | 12,000 Mercassium |
| 100 Mines | 6,000 | 0 | 6,000 Corundium |
| 50 Fuel Refineries | 3,000 | 0 | 3,000 Boronide |
| 1 Shipyard (1000t naval) | ~500 | 0 | ~500 Neutronium |
| 2 Survey Ships | ~2,000 | ~1,000 | Mixed |

**Warning:** Research labs consume enormous amounts of Mercassium (1,200 per lab). If Earth's Mercassium accessibility is low, this becomes a critical bottleneck. Monitor your Mercassium stockpile carefully.

### Mine Expansion Strategy

- Year 1-2: Build 50 mines (6,000 BP, 3,000 Duranium + 3,000 Corundium)
- Year 3-4: Build 50 more mines (same cost)
- Year 4-5: Build 100 more (if mineral consumption demands it)
- Year 5+: Consider automated mines on Luna or nearby moons with better deposits

---

## Step 6: First Shipyard (Years 2-4)

### When to Build

Build your first shipyard when:
1. You have engine technology researched
2. You have reactor technology researched
3. You have sensor technology for survey instruments
4. You have sufficient mineral stockpiles to construct a ship

Typically this is year 2-3.

### What Size and Type

**First shipyard: Naval, 1,000 tons, 1 slipway**

| Parameter | Value | Reasoning |
|-----------|-------|-----------|
| Type | Naval | Survey ships need military-grade sensors |
| Capacity | 1,000 tons | Sufficient for small survey vessels |
| Slipways | 1 | Add more later as needed |

**Cost to build:** Moderate BP investment plus Duranium and Neutronium.

**Immediately after construction:** Begin adding a second slipway and expanding to 2,000 tons capacity.

### First Ship Class: Geological Survey Vessel

**Target design (~1,500-2,000 tons):**

| Component | Purpose |
|-----------|---------|
| 1-2 TN Engines | Propulsion |
| 1 Reactor | Powers sensors |
| 1 Geological Survey Sensor | Finds minerals |
| Fuel Tanks | Range for in-system surveys |
| Engineering Spaces | Maintenance |
| Bridge | Crew management |

**Design philosophy:** Small, cheap, and fast enough to survey the inner system within 2-3 years. You do not need weapons on survey ships (yet).

### Second Shipyard: Commercial (Year 4-5)

Build a commercial shipyard (starts at 10,000 tons) for:

- Freighters (move minerals from off-world mines)
- Colony ships (establish mining colonies)
- Fuel harvesters (if gas giant Sorium available)

---

## Step 7: Research Lab Expansion (Years 2-7)

### Balancing Labs vs. Other Priorities

Research labs are expensive (2,400 BP each, 1,200 Mercassium), but research underpins everything. The key question: how fast to expand?

### Recommended Lab Growth Curve

```
Target: 1 new lab per 3 months of game time in years 2-5
Target: 1 new lab per 2 months in years 5-10
```

| Year | Total Labs | Scientists Assigned | Annual RP Output |
|------|-----------|--------------------|-----------------|
| 2 | 5 | 2-3 | ~100 |
| 3 | 8 | 3-4 | ~160 |
| 4 | 12 | 4-5 | ~240 |
| 5 | 15 | 5-6 | ~300 |
| 7 | 20 | 6-7 | ~400 |
| 10 | 30 | 8+ | ~600 |

### Scientist Management

- Assign your best scientist (highest skill bonus) to your most important project
- Scientists beyond the lab cap provide diminishing returns
- Train new scientists at Ground Force Training Facilities (if available) or wait for random generation
- A scientist with 50% bonus effectively gives you 50% more RP from their assigned labs

---

## Step 8: First Survey Ships (Years 3-5)

### Why Survey Early

Geological surveys reveal mineral deposits on every body in the system. Without surveys, you do not know where to mine. Gravitational surveys reveal jump points to other star systems.

### Survey Fleet Composition

**Minimum viable survey fleet:**

| Ship | Role | Quantity |
|------|------|----------|
| Geo Survey Vessel | Survey planets/moons for minerals | 2 |
| Grav Survey Vessel | Find jump points | 1 |

### Survey Priorities

1. **Inner system planets and moons** -- closest, fastest to reach
2. **Asteroid belt** -- often has high-accessibility deposits
3. **Gas giant moons** -- frequently mineral-rich
4. **Outer system** -- lowest priority due to travel time
5. **Jump points** -- once grav survey locates them, survey the other side

### Expected Findings

A typical Sol system survey reveals:

- Luna: Moderate deposits, often decent accessibility
- Mars: Variable, sometimes excellent deposits
- Asteroid belt: Many small high-accessibility deposits
- Jovian moons: Often substantial deposits
- Titan/Enceladus: Variable

**Key minerals to watch for:** High-accessibility Gallicite (for engines) and Duranium (for everything) deposits anywhere in the system.

---

## Step 9: Expansion Phase (Years 5-8)

### When to Colonize Off-World

Colonize when:
1. Survey data shows attractive mineral deposits off-world
2. You have freighters or colony ships to transport population/installations
3. Earth's mineral deposits are declining or insufficient
4. You have infrastructure stockpiled for hostile environments

### First Colony Targets

| Priority | Target | Why |
|----------|--------|-----|
| 1st | Mineral-rich moon with high accessibility | Best ROI on mining investment |
| 2nd | Body near a gas giant (fuel harvesting) | Fuel independence |
| 3rd | Most habitable non-Earth body | Reduced infrastructure needs |

### Colony Establishment Checklist

```
1. Transport infrastructure (if hostile environment)
2. Transport automated mines (50-100)
3. Optionally transport population + conventional mines (higher output but more logistics)
4. Build mass drivers at both ends (colony + Earth)
5. Set mass driver destination to Earth
6. Minerals flow automatically
```

### Mass Driver Economics

```
Mass Driver: 300 BP, 100 Duranium + 100 Neutronium + 100 Boronide
Output: 5,000 tons/year mineral transfer
Break-even: Replaces one freighter run per year
```

A pair of mass drivers (600 BP investment) provides permanent, fuel-free mineral transport within a system. This is almost always superior to maintaining a freighter route for mineral logistics.

---

## Step 10: Military Preparation (Years 7-10)

### When to Start Building Combat Ships

**Short answer:** After your first survey reveals something threatening, OR by year 8-9 regardless.

**Triggers for military spending:**

- Survey ship detects alien ruins (potential hostile NPR)
- Jump point survey reveals an inhabited system
- Unexplained sensor contacts
- No threats found but year 8+ (prudent defense)

### Military Ramp-Up Checklist

| Step | Timing | Action |
|------|--------|--------|
| 1 | Year 7 | Research beam or missile weapon technology |
| 2 | Year 7-8 | Research fire control and tracking speed |
| 3 | Year 8 | Design first warship class (destroyer/corvette) |
| 4 | Year 8-9 | Expand naval shipyard to warship tonnage |
| 5 | Year 9 | Retool shipyard for warship class |
| 6 | Year 9-10 | Begin construction (2-4 warships) |
| 7 | Year 10 | First combat-capable task group operational |

### First Warship Recommendations

**For a missile doctrine:**

- 4,000-6,000 ton destroyer
- Size 4-6 missile launchers
- Magazines for 30+ missiles
- Active sensor for target acquisition
- Basic point defense (2x gauss cannons)

**For a beam doctrine:**

- 3,000-5,000 ton escort
- 2-4 lasers (20cm with best wavelength tech)
- Fire control matching laser range
- Heavier armor (to close range)
- Speed advantage over expected threats

---

## Year-by-Year Timeline

### Year 0-1: Foundation

```
Research: Trans-Newtonian Technology (PRIORITY 1)
Build: Infrastructure x500 (conventional), Financial Centers x10
Economy: Conventional factories idle or building infrastructure
Minerals: Untouched Earth deposits
```

### Year 1-2: TN Transition

```
Research: Construction Rate Improved, begin engine tech
Build: Construction Factories x20, Mines x50, Research Labs x5
Economy: First TN factories coming online, compounding begins
Minerals: Earth deposits being tapped (~400-800 t/year critical minerals)
Fuel: 0 (no refineries yet)
```

### Year 2-3: Industrial Growth

```
Research: Nuclear Thermal Engine, Reactor tech
Build: More factories x30, Mines x50, Fuel Refineries x25, Labs x5
Economy: 50+ TN factories, exponential growth phase
Minerals: ~1,000-1,500 t/year critical minerals
Fuel: Stockpiling begins (~50,000 litres accumulated)
Shipyard: First naval shipyard under construction
```

### Year 3-4: First Ships

```
Research: Survey sensors, Mining Production Improved
Build: Labs x5, Refineries x25, first survey ship designed and built
Economy: 100+ factories, research capacity growing
Minerals: ~1,500-2,000 t/year
Fuel: ~100,000 litres stockpiled
Fleet: 1 Geo Survey vessel operational
```

### Year 4-5: Exploration Begins

```
Research: Fuel efficiency, sensor range
Build: 2nd survey ship, freighter (commercial yard), more mines
Economy: Self-sustaining growth, 150+ factories
Minerals: Surveys revealing off-world deposits
Fuel: ~200,000 litres, consumption starting
Fleet: 2 Geo Survey + 1 Grav Survey operational
```

### Year 5-6: Expansion

```
Research: Jump drive theory, improved mining
Build: Colony ship or freighter for off-world mining
Economy: 200+ factories, 20+ labs
Minerals: First off-world mining colony established
Fuel: Balanced production vs consumption
Fleet: Survey fleet exploring system, first jump points found
```

### Year 6-7: Consolidation

```
Research: Begin weapon/defense tech paths
Build: Mass drivers, automated mines for colonies
Economy: Multiple mineral income streams
Minerals: 2,000-3,000 t/year critical minerals from multiple sources
Fuel: Comfortable surplus
Fleet: Survey near-complete for inner system
```

### Year 7-8: Pre-Military

```
Research: Laser/missile tech, fire control, tracking speed
Build: Expand naval shipyard, ordnance factories (if missile doctrine)
Economy: Mature early-game economy, 300+ factories
Minerals: Healthy stockpiles of most minerals
Fuel: 500,000+ litres banked
Fleet: Survey complete or nearly so
```

### Year 8-9: Militarization

```
Research: Advanced weapons, armor, shields
Build: First warship class (destroyer/corvette)
Economy: Shifting 20-30% of production to military
Minerals: Watching Gallicite consumption (engines are hungry)
Fuel: Military consumption beginning
Fleet: First warship under construction
```

### Year 9-10: Combat Ready

```
Research: Continue weapon progression
Build: 2-4 warships, PD escorts, ammunition
Economy: Balanced military/civilian production
Minerals: Gallicite may be bottleneck -- secure additional sources
Fuel: Military-ready reserves
Fleet: First combat task group operational (3-5 warships)
```

---

## Mineral Consumption Summary (10-Year Totals)

Approximate total mineral consumption over 10 years of bootstrap:

| Mineral | Total Consumed (tons) | Primary Consumers |
|---------|----------------------|-------------------|
| Duranium | 50,000-80,000 | Everything (factories, mines, labs, ships) |
| Neutronium | 5,000-10,000 | Shipyards, armor, infrastructure |
| Corbomite | 1,000-3,000 | Financial Centers, shields |
| Tritanium | 10,000-20,000 | Factories, weapons, ordnance factories |
| Boronide | 5,000-10,000 | Refineries, reactors, power plants |
| Mercassium | 15,000-30,000 | Research labs (dominant consumer) |
| Vendarite | 2,000-5,000 | Gauss cannons, CIWS |
| Sorium | 5,000-10,000 | Refined into fuel |
| Uridium | 3,000-8,000 | Sensors, fire controls |
| Corundium | 8,000-15,000 | Mines, energy weapons |
| Gallicite | 5,000-15,000 | Engines (scales with fleet size) |

**Key bottleneck minerals:** Duranium (universal demand), Mercassium (research labs), Gallicite (engines), Corundium (mines + weapons).

---

## Key Decisions

| Decision | Economic Option | Military Option | Recommendation |
|----------|----------------|-----------------|----------------|
| Research order | Construction/Mining first | Weapons/Sensors first | Economic first (compounds) |
| Factory vs. Lab investment | More factories (faster building) | More labs (faster research) | 3:1 ratio factories:labs |
| When to build ships | After year 5 (economy stable) | Year 3 (early defense) | Year 3-4 for survey, Year 8 for military |
| Mine count | Heavy investment (300+) | Minimal (100) | 200+ by year 5 |
| Off-world vs. Earth focus | Expand early (year 4-5) | Fortify Earth | Expand year 5-6 after surveys |

---

## Common Mistakes

1. **Researching weapons before having ships:** Weapon tech is useless without engines, reactors, and shipyards to build warships. Economic and propulsion tech first.

2. **Building too few mines early:** Minerals fund everything. 50 mines on Earth is a start, not an endpoint. Target 200+ by year 5.

3. **Neglecting fuel infrastructure:** Ships without fuel are expensive decorations. Build refineries BEFORE your ships launch, not after they run dry in deep space.

4. **Over-investing in military before the economy sustains it:** A warship consumes resources (maintenance, fuel, crew). If your economy cannot support it, the ship degrades and becomes a liability.

5. **Ignoring Financial Centers:** Wealth generation supports your economy. Converting some conventional factories to Financial Centers (20 BP and 20 Corbomite each) provides ongoing income.

6. **No Mercassium stockpile before labs:** Each research lab costs 1,200 Mercassium. If you plan to build 20 labs, you need 24,000 Mercassium. Check your deposits and accessibility FIRST.

7. **Building one giant ship instead of multiple small ones:** A single 10,000-ton cruiser takes years to build at early shipyard rates. Three 3,000-ton escorts complete faster and provide more tactical flexibility.

8. **Neglecting the commercial shipyard:** You need freighters and colony ships for expansion. A commercial yard (10,000-ton starting capacity) should come online by year 4-5.

9. **Not surveying aggressively enough:** Every year without survey data is a year you cannot make informed colonization decisions. Launch survey ships as soon as technically possible.

10. **Stockpiling minerals instead of investing them:** Minerals sitting in warehouses produce nothing. Invest in factories, labs, and mines that generate returns. The only exception is maintaining a Gallicite reserve for emergency ship construction.

---

## References

\hypertarget{ref-ex-economy-1}{[1]}. Aurora C# game database (AuroraDB.db v2.7.1) -- DIM_PlanetaryInstallation PlanetaryInstallationID=25 (Financial Centre). FinancialProductionValue=0.25 (0.25 wealth/year). Workers=0.05 (50,000 workers per centre).

\hypertarget{ref-ex-economy-2}{[2]}. Aurora C# game database (AuroraDB.db v2.7.1) -- DIM_PlanetaryInstallation PlanetaryInstallationID=50 (Convert CI to Financial Centre). Cost=20 BP, Corbomite=20.

\hypertarget{ref-ex-economy-3}{[3]}. Aurora C# game database (AuroraDB.db v2.7.1) -- DIM_PlanetaryInstallation PlanetaryInstallationID=7 (Mine). MiningProductionValue=1.0 (10 tons/year per mine at accessibility 1.0).

\hypertarget{ref-ex-economy-4}{[4]}. Aurora C# game database (AuroraDB.db v2.7.1) -- DIM_PlanetaryInstallation PlanetaryInstallationID=3 (Fuel Refinery). RefineryProductionValue=1.0 (40,000 litres/year at base tech).

\hypertarget{ref-ex-economy-5}{[5]}. Aurora C# game database (AuroraDB.db v2.7.1) -- DIM_PlanetaryInstallation PlanetaryInstallationID=8 (Research Facility). Cost=2400 BP, Duranium=1200, Mercassium=1200. ResearchValue=1.0.

\hypertarget{ref-ex-economy-6}{[6]}. Aurora C# game database (AuroraDB.db v2.7.1) -- DIM_PlanetaryInstallation CI conversion entries (IDs 27, 28, 30, 36, 37, 50). All conversions cost 20 BP. Target installations cost 120 BP each, making conversion 1/6 the cost of building new. See [Section 6.3 Construction](../6-economy-and-industry/6.3-construction.md) for full conversion table.

---

## Related Sections

- [Section 2.1 New Game Options](../2-game-setup/2.1-new-game-options.md) -- Conventional start configuration options
- [Section 5.1 Establishing Colonies](../5-colonies/5.1-establishing-colonies.md) -- Off-world colony mechanics
- [Section 6.1 Minerals](../6-economy-and-industry/6.1-minerals.md) -- Mineral types, accessibility, and depletion
- [Section 6.2 Mining](../6-economy-and-industry/6.2-mining.md) -- Mine types, automated mines, mass drivers
- [Section 7.1 Technology Tree](../7-research/7.1-technology-tree.md) -- Research priorities and prerequisite chains
- [Section 9.1 Shipyards](../9-fleet-management/9.1-shipyards.md) -- Naval vs commercial yards, capacity expansion
- [Appendix A: Formulas](../appendices/A-formulas.md) -- Production, mining, and research calculations
- [Appendix D: Reference Tables](../appendices/D-reference-tables.md) -- Installation costs, tech progression tables
