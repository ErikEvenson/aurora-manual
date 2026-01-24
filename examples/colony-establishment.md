# Example: Establishing a New Colony

This worked example walks through the complete process of establishing a productive colony on a surveyed world -- from initial geological survey through colony ship deployment, infrastructure buildup, and trade route development. Each step includes the decision logic, numerical requirements, and timeline expectations.

## Objective

Establish a **self-sustaining mining and industrial colony** on a mineral-rich moon in a neighboring star system, growing it from initial landing to a productive 50-million-population world over approximately 20 years of game time.

## Starting Conditions

- **Home system**: Sol, Earth population 800 million, 20 automated mines on Mars
- **Target**: Ganymede (Jupiter system) -- previously surveyed, confirmed mineral deposits
- **Jump capability**: Jump drive technology available, 1 jump point from Sol to Alpha Centauri (but Ganymede is in-system, no jump needed)
- **Available ships**: 2x colony ships (50,000 tons, 25,000 colonist capacity each), 4x freighters (50,000 tons cargo each)
- **Technology**: TN-start with basic conventional industry and construction factories
- **Starting minerals on Earth**: Adequate Duranium, Neutronium, Corbomite, Tritanium stocks

---

## Step 1: Survey and Site Selection

### Geological Survey Results (Previously Completed)

Before colonizing, a geological survey ship must have surveyed the target body. Our survey of Ganymede returned:

```
Ganymede Mineral Survey:
  Duranium:    Acc 0.7, Qty 2,800,000 tons  (good)
  Neutronium:  Acc 0.4, Qty 1,200,000 tons  (moderate)
  Corbomite:   Acc 0.9, Qty 500,000 tons    (excellent accessibility)
  Tritanium:   Acc 0.3, Qty 3,500,000 tons  (low accessibility but huge quantity)
  Boronide:    Acc 0.6, Qty 800,000 tons    (good)
  Mercassium:  Acc 0.1, Qty 200,000 tons    (poor -- not worth mining initially)
  Vendarite:   Acc 0.5, Qty 600,000 tons    (moderate)
  Sorium:      Acc 0.8, Qty 1,500,000 tons  (excellent -- fuel production!)
  Uridium:     Acc 0.2, Qty 400,000 tons    (low)
  Corundium:   Acc 0.4, Qty 900,000 tons    (moderate)
  Gallicite:   Acc 0.6, Qty 700,000 tons    (good -- engine production)
```

### Why Ganymede?

Selection criteria for a colony target:

1. **Multiple high-accessibility minerals** -- Duranium (0.7), Corbomite (0.9), Sorium (0.8) are all excellent
2. **Sorium deposits** -- enables local fuel production (critical for self-sufficiency)
3. **Gallicite availability** -- needed for engine construction
4. **Quantity** -- multi-million ton deposits last decades under heavy mining
5. **Location** -- in-system, no jump transit required (simplifies initial logistics)

> **Tip:** Accessibility determines mining output per mine. An accessibility of 0.9 means each mine produces 90% of its theoretical maximum. Below 0.3, consider automated mines instead of manned operations -- the population cost is not worth the low output.

### Colony Cost Assessment

```
Ganymede Environment:
  Temperature: -160C (well below habitable range)
  Atmosphere: None (vacuum)
  Gravity: 0.146g (below species minimum)
  Hydrosphere: 0% (subsurface ice only)

Colony Cost Factors:
  Temperature: (160/17.5) = 9.14
  Breathable gas: 2.0 (no atmosphere)
  Gravity: 1.0 (below minimum)

  Final CC: 9.14 (temperature is worst factor)
```

This is a HIGH colony cost world. Every colonist requires 9.14 units of infrastructure to survive. This means our colony will be infrastructure-intensive, but the mineral wealth justifies the investment.

---

## Step 2: Initial Colony Ship Deployment

### Preparing the Colony Fleet

Before launching colony ships, we need to pre-position infrastructure:

```
Initial deployment (Year 1):
  Colony Ship 1: 25,000 colonists (workers for installations)
  Colony Ship 2: 25,000 colonists (additional workers)
  Freighter 1: Infrastructure (minimum 50,000 * 9.14 = 457,000 units needed!)
  Freighter 2: Infrastructure (continued)
  Freighter 3: Infrastructure (continued)
  Freighter 4: Automated mines + construction factories
```

### Infrastructure Calculation

```
Initial population: 50,000 colonists
Colony Cost: 9.14
Required infrastructure: 50,000 * 9.14 = 457,000 units

Infrastructure per freighter load (50,000 ton capacity):
  Each infrastructure unit = 1 ton (transported as cargo)
  Per freighter: 50,000 units

Freighter loads needed: 457,000 / 50,000 = 9.14 loads
```

**Problem**: We need 10 freighter loads just for initial infrastructure, but only have 4 freighters. This means multiple trips.

> **Tip:** Always ship infrastructure BEFORE or WITH your colonists. Never send population to a world without sufficient infrastructure -- unhoused colonists suffer attrition (death). Calculate infrastructure needs before launching colony ships.

### Revised Deployment Strategy

```
Phase 1 (Year 1, Months 1-6):
  4 freighters carry infrastructure (200,000 units total)
  Hold colony ships at Earth

Phase 2 (Year 1, Months 7-12):
  4 freighters carry remaining infrastructure (257,000 units)
  Colony ships depart with initial population

Phase 3 (Year 2):
  Freighters carry automated mines and construction factories
  Colony ships return to Earth for next load
```

Transit time Earth to Ganymede at freighter speed (~1,500 km/s):
```
Distance: ~600 million km (average Earth-Jupiter)
Transit time: 600,000,000 / (1,500 * 3600) = 111 hours = ~4.6 days
Round trip: ~10 days
```

With in-system transit this short, multiple runs are very feasible.

---

## Step 3: Mining Operations Setup

### Automated Mines vs Manned Mines

For a CC 9.14 world, manned mines require massive infrastructure support per worker. Automated mines require no population but produce less per unit:

```
Manned Mine:
  Output: 10 units/year per mine (at accessibility 1.0)
  Workers: 50,000 per mine
  Infrastructure: 50,000 * 9.14 = 457,000 per mine
  Advantage: Higher output, uses population (renewable resource)

Automated Mine:
  Output: 5 units/year per mine (at accessibility 1.0, half of manned)
  Workers: 0
  Infrastructure: 0
  Advantage: No population/infrastructure overhead
  Disadvantage: Each is 50,000 tons to transport, lower output
```

**Decision: Start with automated mines, transition to manned as infrastructure grows.**

In C# Aurora, mines extract from ALL mineral deposits on a body simultaneously. Each mine produces from each mineral based on that mineral's accessibility. Initial deployment:

```
Per Automated Mine (annual output per mineral):
  Production = 5 * Accessibility
  Duranium: 5 * 0.7 = 3.5 tons/year
  Sorium: 5 * 0.8 = 4.0 tons/year
  Corbomite: 5 * 0.9 = 4.5 tons/year
  Gallicite: 5 * 0.6 = 3.0 tons/year
  ...etc for all minerals present

20 Automated Mines Total Annual Output:
  Duranium: 20 * 3.5 = 70 tons/year
  Sorium: 20 * 4.0 = 80 tons/year
  Corbomite: 20 * 4.5 = 90 tons/year
  Gallicite: 20 * 3.0 = 60 tons/year
```

> **Tip:** Mines in C# Aurora extract from ALL mineral deposits on a body simultaneously. You do not assign mines to specific minerals. Output per mine per mineral is simply (mine output) * (mineral accessibility). High-accessibility deposits produce more from every mine.

---

## Step 4: Industrial Buildup

### Construction Factory Deployment

Once basic mining is running, deploy construction factories to build on-site:

```
Year 2-3 Deployment:
  Ship 20 Construction Factories to Ganymede
  Each factory: produces 10 BP/year of installations
  Total production: 200 BP/year

Priority build queue:
  1. Infrastructure (1 BP each, conventional industry can also help)
  2. Additional automated mines (60 BP each)
  3. Fuel refineries (for local Sorium processing)
  4. Maintenance facilities (reduce failure rates)
```

### Conventional Industry Alternative

Conventional Industry produces infrastructure without TN minerals:

```
Conventional Industry:
  Output: 5 infrastructure/year per factory
  No mineral cost (uses only wealth/population labor)
  Workers: 50,000 per factory

20 Conventional Industry installations:
  Output: 100 infrastructure/year
  Workers needed: 1,000,000
  Infrastructure for workers: 1,000,000 * 9.14 = 9,140,000 units
```

At CC 9.14, the infrastructure overhead for manned facilities is enormous. The colony starts heavily automated and transitions to manned operations only after terraforming reduces colony cost (see the [Terraforming Example](terraforming-colony.md) for that process -- though Ganymede's CC 9.14 makes full terraforming impractical without advanced technology).

---

## Step 5: Growing the Colony

### Population Growth Phases

```
Phase 1 (Years 1-5): Automated Operations
  Population: 50,000 (minimal staff for oversight)
  Mining: 20 automated mines
  Industry: 0 manned (all remote-operated)
  Infrastructure: 457,000 units (minimum)
  Focus: Extract minerals, ship to Earth

Phase 2 (Years 5-10): Initial Manned Expansion
  Population: 500,000 (imported via colony ships)
  Mining: 20 automated + 5 manned mines
  Industry: 10 construction factories
  Infrastructure: 4,570,000 units (500k * 9.14)
  Focus: Local construction, fuel refining

Phase 3 (Years 10-15): Industrial Colony
  Population: 5,000,000
  Mining: 20 automated + 25 manned mines
  Industry: 50 construction factories, 20 fuel refineries
  Infrastructure: 45,700,000 units
  Focus: Self-sufficient mineral/fuel production

Phase 4 (Years 15-20): Major Colony
  Population: 50,000,000
  Mining: 20 automated + 100 manned mines
  Industry: 200 construction factories, 100 fuel refineries, 50 ordnance factories
  Infrastructure: 457,000,000 units
  Focus: Full industrial capacity, fleet support
```

### Population Transport Calculation

To move from Phase 2 to Phase 3 (adding 4.5 million people):
```
Colony ship capacity: 25,000 per ship per trip
Trips needed: 4,500,000 / 25,000 = 180 trips (with 2 ships)
Trips per ship: 90 trips
Trip time: ~10 days round-trip
Total time: 90 * 10 = 900 days = ~2.5 years

With 4 colony ships: ~1.25 years
```

> **Tip:** Population growth is often the bottleneck for colony expansion. Invest in colony ship construction early. A fleet of 8-10 colony ships can move millions of colonists per year within a system.

---

## Step 6: Fuel Production

### Why Local Fuel Matters

Ganymede's high Sorium accessibility (0.8) makes it an ideal fuel depot:

```
Fuel Refinery:
  Input: 1 Sorium per refinery per year
  Output: 20,000 litres of fuel per refinery per year
  Workers: 50,000 per refinery

With 20 fuel refineries:
  Sorium consumed: 20 tons/year
  Fuel produced: 400,000 litres/year
  Workers: 1,000,000
```

At 80 tons/year Sorium production from 20 automated mines, we have abundant raw material. The refineries consume only 20 tons/year, leaving 60 tons/year surplus for stockpiling or export.

400,000 litres of fuel per year supports:
```
A 10,000-ton cruiser at 2,500 km/s consumes ~552 litres/hour at full power
  Annual consumption at 50% duty cycle: 552 * 4,380 = 2,417,760 litres
  Our 20 refineries support: 400,000 / 2,417,760 = 0.17 cruisers continuously

This is inadequate for fleet support -- scale to 100+ refineries for a fleet depot
```

### Fuel Depot Scaling

```
Target: Support a 6-ship destroyer flotilla
  Per destroyer: ~300 litres/hour * 4,380 hours = 1,314,000 litres/year
  6 destroyers: 7,884,000 litres/year
  Refineries needed: 7,884,000 / 20,000 = 395 refineries

This requires Phase 4 industrial capacity (50M+ population)
```

---

## Step 7: Trade Route Development

### Setting Up Civilian Trade

Once a colony reaches 10+ million population with mineral stockpiles, civilian shipping lines begin operating automatically:

```
Civilian Trade Activation Requirements:
  1. Colony population >= 10,000,000
  2. Mineral surplus on colony (supply)
  3. Mineral demand on homeworld (demand)
  4. Civilian shipping line exists with cargo capacity
  5. Route is within civilian shipping range
```

### Trade Route Economics

```
Ganymede exports (Phase 3+):
  Duranium surplus: ~50 tons/year (mining output minus local consumption)
  Sorium surplus: ~60 tons/year (excess beyond refinery input)
  Corbomite surplus: ~80 tons/year (high accessibility, low local demand)

Earth imports:
  All TN minerals in demand for construction and research
  Fuel (processed on Ganymede, shipped to Earth)
```

Civilian shipping generates wealth for both colonies through trade. The wealth income from trade helps fund further infrastructure expansion.

> **Tip:** Civilian trade routes activate automatically when supply and demand conditions are met. You do not need to manually set up routes -- just ensure both colonies have spaceports and the civilian economy is enabled. Check the Economics window to monitor trade activity.

### Military Supply Routes

For strategic mineral transport (when you want guaranteed throughput rather than civilian shipping):

```
Military freighter route (standing order):
  4x Freighters assigned to Ganymede-Earth circuit
  Cargo per trip: 200,000 tons total capacity
  Trip time: 10 days round-trip
  Annual throughput: 36.5 trips * 200,000 = 7,300,000 tons/year

  This vastly exceeds current mining output
  Reduce to 1 freighter for current production levels
  Scale up freighter assignment as mining grows
```

---

## Step 8: Long-Term Colony Viability

### Self-Sufficiency Checklist

A colony is self-sufficient when it can:

```
[x] Mine its own minerals (Phase 1 achieved)
[x] Produce its own fuel (Phase 2 achieved)
[x] Build its own installations (Phase 3: construction factories)
[x] Maintain its own ships (Phase 3: maintenance facilities)
[ ] Build its own ships (requires naval shipyard -- Phase 4+)
[ ] Conduct its own research (requires research labs -- Phase 4+)
[ ] Grow population naturally (requires low CC or massive infrastructure)
```

### When Ganymede Becomes a Fleet Base

```
Fleet Base Requirements:
  Fuel depot: 10,000,000+ litres stored
  Maintenance facilities: 50+ (for destroyer-class vessels)
  Ordnance factories: 20+ (missile production)
  Naval shipyard: 1x 6,000-ton capacity minimum
  Population: 25,000,000+ (workforce for all facilities)

Estimated timeline to fleet base: Year 15-20
```

---

## Common Mistakes

1. **Sending colonists before infrastructure**: At CC 9.14, every colonist needs 9+ infrastructure units. Sending population without pre-positioned infrastructure causes attrition (deaths). Always ship infrastructure first.

2. **Ignoring colony cost in planning**: A CC 1.0 world needs 1 infrastructure per person. A CC 9.14 world needs 9.14x that investment. Factor CC into ALL logistics calculations.

3. **Overcommitting to manned mines on high-CC worlds**: At CC 9.14, the infrastructure cost per manned mine worker makes automated mines far more cost-effective until CC is reduced through terraforming or genetic modification.

4. **Neglecting Sorium deposits**: Fuel independence is critical. A colony that cannot produce its own fuel depends entirely on supply lines from Earth. Prioritize Sorium-rich worlds for colonization.

5. **Forgetting transit capacity**: Moving millions of colonists requires dedicated colony ship fleets. A single 25,000-capacity colony ship takes years to populate a major colony. Plan ship construction accordingly.

6. **Not building a spaceport**: Civilian trade requires spaceports on both endpoints. Without a spaceport, no civilian shipping will service your colony regardless of supply/demand conditions.

7. **Ignoring maintenance**: Ships and installations suffer failures without maintenance facilities. A remote colony without maintenance support will see increasing equipment breakdowns over time.

---

## Related Sections

- [Section 5.1 Establishing Colonies](../5-colonies/5.1-establishing-colonies.md) -- Colony ship operations and initial landing
- [Section 5.2 Population](../5-colonies/5.2-population.md) -- Population growth, transport, and workforce
- [Section 5.4 Infrastructure](../5-colonies/5.4-infrastructure.md) -- Infrastructure requirements and production
- [Section 6.1 Minerals](../6-economy-and-industry/6.1-minerals.md) -- Mineral types and strategic importance
- [Section 6.2 Mining](../6-economy-and-industry/6.2-mining.md) -- Automated vs manned mining operations
- [Section 6.3 Construction](../6-economy-and-industry/6.3-construction.md) -- Factory types and build queues
- [Section 6.5 Civilian Economy](../6-economy-and-industry/6.5-civilian-economy.md) -- Trade routes and shipping lines
- [Section 17.1 Geological Survey](../17-exploration/17.1-geological-survey.md) -- Survey mechanics and mineral detection
- [Appendix A: Formulas](../appendices/A-formulas.md) -- Mining output, infrastructure, and colony cost formulas
