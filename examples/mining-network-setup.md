# Example: Setting Up a Mining Network

This worked example walks through establishing an off-world mining colony and freight network to supplement your homeworld's depleting mineral supplies. We cover site selection, colony establishment, mine deployment, freighter design, and logistics configuration -- with calculated numbers at each step.

## Objective

Establish an off-world mining operation that:

- Supplements Earth's depleting Duranium and Gallicite deposits
- Operates autonomously via standing orders (minimal micromanagement)
- Scales as mineral demand grows with fleet expansion
- Provides a sustainable supply chain for decades of ship construction

## Starting Conditions

- **TN Start**: Trans-Newtonian technology researched, basic industry running
- **Homeworld**: Earth, population ~500 million, mineral deposits showing depletion (Duranium accessibility 0.3, Gallicite accessibility 0.1)
- **Survey Status**: Inner system geological survey complete
- **Survey Results** (example):

| Body | Duranium | Acc. | Gallicite | Acc. | Other Notable | Colony Cost |
|------|----------|------|-----------|------|---------------|-------------|
| Luna | 50,000 | 0.8 | 12,000 | 0.6 | Neutronium 30k/0.7 | 0.00 |
| Mars | 200,000 | 0.4 | 80,000 | 0.3 | Corundium 150k/0.5 | 2.50 |
| Asteroid Belt #1 | 8,000 | 1.0 | 25,000 | 0.9 | Mercassium 5k/1.0 | 0.00 |
| Ceres | 40,000 | 0.6 | 35,000 | 0.7 | Boronide 20k/0.5 | 0.00 |

---

## Step 1: Evaluate Survey Results

When comparing mining sites, **effective annual yield per mine** is the key metric:

```
Annual_Tons_per_Mine = Base_Production x Accessibility x Tech_Modifier
```

At base technology (modifier 1.0), each mine produces:
```
Output per mine = 10 tons/year x Accessibility
```

**Effective yield comparison (per mine, base tech)**:

| Body | Duranium/mine/year | Gallicite/mine/year | Combined Value |
|------|-------------------|--------------------|-|
| Luna | 8 tons | 6 tons | High yield, zero colony cost |
| Mars | 4 tons | 3 tons | Moderate yield, high colony cost |
| Asteroid Belt #1 | 10 tons | 9 tons | Maximum yield, zero colony cost |
| Ceres | 6 tons | 7 tons | Good yield, zero colony cost |

**Decision: Prioritize the Asteroid Belt (#1) for Gallicite (0.9 accessibility) and Luna for Duranium (0.8 accessibility).**

Rationale:

- **Gallicite is the bottleneck** -- every engine requires it, and Earth's 0.1 accessibility deposit is nearly useless (10 mines produce only 10 tons/year)
- Asteroid Belt has 0.9 accessibility Gallicite: 10 mines produce 90 tons/year (9x Earth's output)
- Both Luna and the Asteroid Belt have colony cost 0.00 (no infrastructure needed)
- Mars has high colony cost (2.50) requiring significant infrastructure investment before population can survive

**Primary target: Asteroid Belt #1** (Gallicite + Mercassium)
**Secondary target: Luna** (Duranium + Neutronium)

---

## Step 2: Colony Establishment

### Check Colony Cost

Colony cost 0.00 means no infrastructure is required. Colonists can survive without environmental support. This is the ideal scenario -- we simply need to transport people (for conventional mines) or deploy automated mines (no population needed).

### Decision: Automated vs Conventional Mines

| Factor | Conventional Mines | Automated Mines |
|--------|-------------------|-----------------|
| BP Cost | 120 BP | 240 BP |
| Mineral Cost | 120 Corundium | 240 Corundium |
| Workers Required | 50,000 per mine | 0 (unmanned) |
| Output | 10 tons/year x accessibility | 10 tons/year x accessibility |
| Colony needed? | Yes (population) | No (unmanned) |
| Transport cost | Colony ship for workers | Freighter for mines |

**Decision: Use automated mines for the Asteroid Belt.** Reasons:
1. No need to transport 50,000+ colonists per mine
2. No infrastructure or life support concerns
3. Double the build cost is acceptable given the logistics savings
4. We can ship automated mines via freighter and deploy immediately

For Luna (which is close and has zero colony cost), conventional mines are viable if we want cheaper per-unit cost, but automated mines keep things simpler.

### Deploying Automated Mines

Build 20 automated mines on Earth (our starting industrial base):
```
Build cost: 20 x 240 BP = 4,800 BP
Mineral cost: 20 x 240 Corundium = 4,800 Corundium
Build time: 4,800 BP / (Num_Factories x 10 BP/year)
```

With 200 construction factories at base tech:
```
Build time = 4,800 / (200 x 10) = 4,800 / 2,000 = 2.4 years
```

Too slow. Let us build in batches of 5:
```
5 automated mines = 1,200 BP = 0.6 years (7.2 months)
```

Ship the first batch of 5 while building the next batch.

---

## Step 3: Calculate Mining Output

With 20 automated mines on the Asteroid Belt:

**Gallicite output**:
```
Annual output = 20 mines x 10 tons/year x 0.9 accessibility = 180 tons/year
```

**Duranium output** (from the 1.0 accessibility deposit):
```
Annual output = 20 mines x 10 tons/year x 1.0 accessibility = 200 tons/year
```

**Deposit lifespan**:
```
Gallicite: 25,000 tons / 180 tons/year = 139 years (very long-lasting)
Duranium: 8,000 tons / 200 tons/year = 40 years (plan replacement source)
```

**With Improved Mining Tech (12 tons/year)**:
```
Gallicite: 20 x 12 x 0.9 = 216 tons/year
Duranium: 20 x 12 x 1.0 = 240 tons/year
```

**Scaling to 50 mines (after economy grows)**:
```
Gallicite: 50 x 10 x 0.9 = 450 tons/year (base tech)
Gallicite: 50 x 12 x 0.9 = 540 tons/year (improved tech)
```

**Context**: A single Nuclear Pulse Engine (25 HS, 1,250 tons) requires approximately 1,000+ Gallicite. At 180 tons/year from 20 mines, building one engine takes ~5.5 years of Gallicite production. This illustrates why aggressive mining expansion is critical.

---

## Step 4: Freighter Design

We need a freighter to haul automated mines to the colony and bring minerals back to Earth. Key requirements:

- Carry automated mines outbound (each mine is ~500 tons when transported as cargo)
- Carry minerals homeward (bulk cargo)
- Fuel range for round trips within the inner system
- Affordable (commercial engine to avoid maintenance costs)

### Size vs Speed Trade-Off

Commercial engines are 10x the size of military engines for the same cost, but exempt from maintenance. For a logistics ship, this is the correct choice.

**Target**: 50,000-ton freighter with ~5,000 tons of cargo capacity and decent speed.

Actually, let us recalculate. Freighters should maximize cargo capacity. A common split:

```
Hull: 50,000 tons (1,000 HS)
Engines: ~30% = 15,000 tons (300 HS commercial)
Cargo: ~50% = 25,000 tons (500 HS cargo holds)
Fuel: ~10% = 5,000 tons (100,000 litres)
Bridge + other: ~10% = 5,000 tons
```

With Nuclear Pulse Engine at 8 EP/HS, commercial engines:
```
Commercial EP/HS = 8 / 10 = 0.8 EP/HS (commercial engines are 10x size for same power)
Wait -- commercial engines produce the SAME total power as military for same cost,
but occupy 10x the hull space. So:

300 HS commercial engine at 8 EP/HS base:
Since commercial engines have 10x the HS, they effectively produce:
Power = (300 / 10) x 8 = 240 EP (equivalent to a 30 HS military engine)
```

Actually, re-reading Section 8.3.1: "A commercial engine that costs the same as a 1 HS military engine occupies 10 HS -- providing the same total power output."

So a 300 HS commercial engine produces the same EP as a 30 HS military engine:
```
EP = 30 x 8 = 240 EP
Speed = 240 * 5000 / 50000 = 24 km/s
```

Too slow. Let us increase engine allocation to 40%:
```
Engines: 400 HS commercial = 40 HS military equivalent
EP = 40 x 8 = 320 EP
Speed = 320 * 5000 / 50000 = 32 km/s
```

Still very slow, but acceptable for a commercial freighter. 32 km/s is ~2.8 million km/day.

**Transit time example** (Earth to Asteroid Belt, ~400 million km average):
```
Time = 400,000,000 km / 32 km/s = 12,500,000 seconds = 144.7 days (4.8 months one way)
Round trip: ~9.6 months
```

That is slow but workable for automated logistics. Each freighter makes roughly 1.25 round trips per year.

### Cargo Capacity Calculation

With 25,000 tons of cargo space (500 HS of cargo holds):
```
Minerals per trip: 25,000 tons
Annual mineral delivery: 25,000 x 1.25 trips = 31,250 tons/year per freighter
```

Our 20 mines produce 18 tons of Gallicite + 20 tons of Duranium = 38 tons/year total. A single freighter is wildly overkill for 20 mines. Even a single trip per year carries 25,000 tons -- far more than our mines produce.

**Revised freighter**: Scale down to a smaller, cheaper design:

```
Hull: 10,000 tons (200 HS)
Engines: 80 HS commercial = 8 HS military equivalent
EP = 8 x 8 = 64 EP
Speed = 64 * 5000 / 10000 = 32 km/s (same speed, smaller ship)
Cargo: 80 HS = 4,000 tons capacity
Fuel: 20 HS = 1,000 tons (50,000 litres)
Bridge: 1 HS = 50 tons
Remaining: ~19 HS for crew quarters, engineering
```

A 4,000-ton cargo capacity handles our 38 tons/year of production easily with a single trip. As mining scales up, we add more freighters.

### Fuel Range Check

```
Fuel per hour = 64 EP x Consumption_Rate (commercial engines are efficient)
Range = 50,000 litres / Fuel_per_Hour x 3600 x 32 / 1,000,000,000
```

Commercial engines with modest consumption should provide adequate inner-system range. The ship designer will confirm exact figures, but at 10% fuel fraction, a commercial freighter typically achieves 30-50 billion km range -- more than sufficient for inner system routes.

---

## Step 5: Standing Orders Configuration

Once the mining colony is running and the freighter is built, configure automated logistics:

### Route Configuration

1. **Load minerals at Asteroid Belt colony**: Set "Load All Minerals" order
2. **Travel to Earth**: Navigate to homeworld
3. **Unload minerals at Earth**: Set "Unload All Minerals" order
4. **Return to Asteroid Belt**: Navigate back
5. **Repeat**: Set orders to cycle (conditional repeat)

The standing order sequence:
```
1. Move to [Asteroid Belt Colony]
2. Load All Minerals (wait until full OR no minerals remaining)
3. Move to [Earth]
4. Unload All Minerals
5. Go to Order 1
```

**Important**: Set the load order to "Load until full OR colony stockpile empty" -- otherwise the freighter waits indefinitely for a full load that may never accumulate at low production rates.

### Multiple Mineral Types

If mining both Gallicite and Duranium, the "Load All Minerals" order handles both automatically. The freighter picks up whatever is stockpiled at the colony.

---

## Step 6: Mass Driver Option

Mass drivers offer an alternative to freighter logistics:

**Mass Driver specifications** (from Appendix D):

- BP Cost: 300
- Mineral Cost: 100 Duranium + 100 Neutronium + 100 Boronide
- Workers Required: 0 (unmanned)
- Output: Launches mineral packets at a target body

**Mass Driver advantages**:

- Instantaneous transfer (minerals arrive within the 5-day processing increment)
- No ongoing fuel costs
- No freighter maintenance or crew requirements
- Scales linearly (more drivers = more throughput)

**Mass Driver disadvantages**:

- Requires a mass driver at BOTH ends (one to send, one to catch)
- Total cost: 2 x 600 BP = 1,200 BP + 600 Duranium + 600 Neutronium
- Each installation needs 50,000 workers (requires population at both locations)
- Cannot use with automated-mine-only colonies (need population for mass drivers)
- Catching mass driver needs to be configured to receive

### Mass Driver vs Freighter Comparison

| Factor | Mass Driver | Freighter |
|--------|------------|-----------|
| Setup cost | 1,200 BP + minerals | Ship BP + minerals |
| Ongoing cost | None (workers only) | Fuel |
| Transfer speed | Instant | Months (transit time) |
| Population needed | Yes (both ends) | No (crew only) |
| Flexibility | Fixed route only | Can reroute |
| Scalability | Add more drivers | Add more freighters |
| Works with auto mines? | No (needs workers) | Yes |

**Decision for our example**: Use freighters for the Asteroid Belt (automated mines, no population). Consider mass drivers for Luna (close to Earth, conventional mines with population already feasible).

---

## Step 7: Scaling Up

As your economy grows and mineral demand increases:

### Phase 1: Initial Setup (Year 0-5)
- Deploy 20 automated mines to Asteroid Belt
- Build 1 small freighter (10,000 tons)
- Output: ~38 tons/year combined minerals

### Phase 2: Expansion (Year 5-15)
- Increase to 50 automated mines
- Build 2nd freighter for redundancy
- Research Improved Mining Tech (1.2x modifier)
- Output: ~100 tons/year combined minerals

### Phase 3: Major Operations (Year 15-30)
- Deploy 100+ automated mines across multiple bodies
- Research Advanced Mining Tech (1.44x modifier)
- Consider mass drivers for high-volume routes
- Output: ~250+ tons/year combined minerals

### Adding Mine Production Over Time

```
Phase 1: 20 mines x 0.9 acc x 1.0 tech = 18 tons Gallicite/year
Phase 2: 50 mines x 0.9 acc x 1.2 tech = 54 tons Gallicite/year
Phase 3: 100 mines x 0.9 acc x 1.44 tech = 129.6 tons Gallicite/year
```

---

## Step 8: Multiple Colonies -- Managing Priority Routes

Once you have 3+ mining outposts, logistics complexity grows. Example scenario:

| Colony | Primary Mineral | Output/Year | Distance from Earth |
|--------|----------------|-------------|---------------------|
| Asteroid Belt | Gallicite | 54 tons | 400M km |
| Luna | Duranium | 40 tons | 384,000 km |
| Ceres | Boronide | 25 tons | 350M km |

### Priority Routing Strategy

1. **Highest priority**: Gallicite (engine mineral, always bottlenecked)
2. **Medium priority**: Duranium (bulk construction, high volume needed)
3. **Low priority**: Boronide (power plants, moderate demand)

### Fleet Assignment

- **Dedicated Gallicite run**: 1 freighter on permanent Asteroid Belt route
- **Inner system shuttle**: 1 smaller freighter handling Luna (very short transit, high frequency)
- **Outer system collection**: 1 larger freighter doing a multi-stop route (Ceres then home)

### Multi-Stop Route Example

```
1. Move to [Ceres]
2. Load Boronide (specific mineral, not all)
3. Move to [Asteroid Belt]
4. Load Gallicite (specific mineral)
5. Move to [Earth]
6. Unload All Minerals
7. Go to Order 1
```

**Warning**: Multi-stop routes increase transit time. If Ceres and the Asteroid Belt are on opposite sides of the sun, the detour may double travel time. Monitor route efficiency and split into dedicated routes when volume justifies additional freighters.

---

## Step 9: Integrating Civilian Economy

Government mining and freighter operations are not your only option. The civilian economy can supplement -- or eventually replace -- much of your mining logistics. Understanding when and how to leverage civilian shipping and mining is key to efficient empire management.

### Civilian Mining Overview

Civilian mining colonies appear automatically as your empire develops. Unlike government mining, you do not directly control where civilians mine or how much they produce. However, civilian mining provides significant advantages:

| Factor | Government Mining | Civilian Mining |
|--------|------------------|-----------------|
| Setup cost | 240+ BP per automated mine | Free (civilians invest) |
| Mineral cost | 240 Corundium per mine | None (you pay nothing) |
| Location control | Full (you choose) | None (civilians choose) |
| Output control | Full (deploy more mines) | None (random expansion) |
| Worker requirement | 50,000 per conventional mine | None (complexes are unmanned) |
| Transport logistics | Your freighters or mass drivers | Civilian freighters (automatic) |

### Civilian Mining Colony Requirements

Civilian mining colonies only appear when specific conditions are met (see [Section 6.5.2 Civilian Mining](../6-economy-and-industry/6.5-civilian-economy.md)):

- Your empire has at least two colonies with population or infrastructure
- The target body has at least 10,000 tons of Duranium at 0.7+ accessibility
- The system contains a population of 10 million or more
- The body is within 80 AU of the primary star

**Implication for our example:** The Asteroid Belt will not attract civilian miners initially because our mining operation there is automated (no population). However, if you establish a populated colony in the same system, civilian mining may eventually appear.

### Setting Up Civilian Mining Contracts

While you cannot order civilians to mine specific locations, you can purchase minerals from civilian mining colonies:

1. **Identify civilian mining colonies:** Check the Civilian Mining section of the Economics window for active civilian mines
2. **Purchase minerals:** Select the civilian colony and use the purchase interface to buy stockpiled minerals
3. **Transport:** Civilian freighters automatically transport purchased minerals to your government colonies

> **Tip:** Civilian mining colonies that sell minerals to you are highlighted in **light blue** in the interface, making them easy to identify.

### Civilian Shipping Contracts

Civilian shipping lines can transport minerals, installations, and population between your colonies. This provides an alternative to building government freighters.

**Cost Formula for Installation Transport:**

```
Cost = 5 x Number of Installations x Systems Travelled x (Cargo Points / 25,000)
```

**Example:** Moving 10 automated mines (each 500 cargo points) from Earth to the Asteroid Belt (same system, counts as 0.5 systems):
```
Cost = 5 x 10 x 0.5 x (500 / 25,000) = 0.5 wealth
```

Mineral transport pricing follows the distance-based model from v2.6.0:

| Activity | Rate per unit per billion km |
|----------|------------------------------|
| Cargo transport | 0.00015 per cargo point |

For our Asteroid Belt route (~400 million km one way):
```
Cost per ton = 0.00015 x 0.4 billion km = 0.00006 wealth per ton
1,000 tons of Gallicite = 0.06 wealth
```

This is effectively free compared to the cost of building and fueling your own freighters.

### When to Use Civilian vs Government Transport

| Scenario | Recommended Approach |
|----------|---------------------|
| Early game (few colonies) | Government freighters -- civilians need time to develop |
| Peacetime routine logistics | Civilian shipping -- free capacity, no fuel cost |
| Critical mineral shortages | Government freighters -- guaranteed priority |
| Wartime supply lines | Government freighters -- civilians avoid danger |
| High-volume routes | Mix both -- civilians supplement government capacity |
| New frontier colonies | Government initially, then transition to civilian |

### Cost/Benefit Analysis: Civilian vs Military Transport

**Government Freighter (10,000 tons, from Step 4):**

- Build cost: ~2,000 BP + minerals
- Fuel consumption: ~10,000 litres per round trip
- Annual fuel cost: 12,500 litres (1.25 trips/year)
- Maintenance: Minimal (commercial engines exempt)
- Control: Full (you set routes and priorities)
- Wartime reliability: High (follows your orders)

**Civilian Shipping:**

- Build cost: None (civilians invest their own wealth)
- Fuel cost: None (civilians pay for fuel)
- Transport cost: ~0.06 wealth per 1,000 tons per billion km
- Control: None (civilians optimise for profit)
- Wartime reliability: Low (civilians avoid dangerous systems)

**Break-even calculation:** A government freighter costing 2,000 BP and consuming 12,500 litres of fuel annually compares to civilian transport costing ~1 wealth per year for equivalent tonnage. The government freighter is "paid off" in strategic flexibility and wartime reliability, not raw economics.

> **Note:** In peacetime with safe shipping lanes, civilian transport is almost always more economical. The question is whether you can afford to depend on it when conditions change.

### Encouraging Civilian Mining in Your Target Systems

To attract civilian mining to systems where you have government operations:

1. **Establish a 10M+ population:** Civilians require a populated system to consider mining there
2. **Ensure survey coverage:** Civilians only mine surveyed deposits
3. **Maintain safe routes:** Civilian ships avoid military-restricted or alien-controlled systems
4. **Build commercial shipyards:** Civilians need shipyard capacity to build freighters and colony ships

For our Asteroid Belt example, converting from pure automated mining to a hybrid approach:

1. Keep 20 automated government mines for guaranteed baseline output
2. Establish a small population (via colony ship) to meet civilian threshold
3. Wait for civilian mining complexes to appear (probability increases with empire wealth)
4. Purchase minerals from civilian mines to supplement government production
5. Let civilian freighters handle routine transport while keeping 1 government freighter for emergencies

### Civilian Contract Standing Order (v2.8.0)

If civilian shipping capacity is insufficient, you can assign government freighters to fulfill civilian contracts:

1. Design a freighter with cargo capacity
2. Assign the fleet the **Civilian Contract** standing order
3. The freighter will automatically seek and fulfill civilian trade routes
4. No payment is received (you provide the service free)
5. The freighter uses its own fuel and refuels at designated depots

This is useful during emergencies when civilian capacity cannot meet demand, but is generally inefficient compared to letting civilians handle their own logistics.

### Hybrid Mining Network Example

Combining government and civilian operations for our Asteroid Belt scenario:

**Phase 1 (Years 0-10): Government Only**

- 20 automated government mines
- 1 government freighter on standing orders
- Output: 38 tons/year (government)
- Civilian mining: None (no population in system)

**Phase 2 (Years 10-20): Introduce Population**

- Establish 50,000 population at Asteroid Belt (for mass driver potential)
- Continue government mining operations
- Civilian mining colonies may begin appearing
- Output: 38 tons/year (government) + variable civilian

**Phase 3 (Years 20+): Mature Hybrid**

- 50 automated government mines (expanded)
- 1-2 civilian mining complexes (appeared naturally)
- Civilian freighters handling routine transport
- Government freighter reserved for emergencies
- Output: 100+ tons/year (government) + 20-40 tons/year (civilian)

### Monitoring Civilian Contributions

Track civilian economy contributions in the Economics window:

- **Civilian Shipping Lines:** Fleet sizes, current operations, income
- **Civilian Mining:** Active colonies, output by mineral type
- **Civilian Trade Routes:** Active routes, cargo volumes
- **Empire Mining Tab:** Shows government and civilian production side by side

> **Warning:** Do not become over-reliant on civilian logistics. Civilians optimise for profit and avoid danger. A single raider in a trade lane can halt civilian shipping precisely when you need supplies most. Maintain enough government capacity to sustain critical operations independently.

### Range Limitations

Civilian ships will only travel a maximum of **four systems** from their origin. Plan your jump gate network accordingly:

- Colonies more than four jumps from a major population will not receive civilian services
- Intermediate colonies can serve as relay points
- Hub-and-spoke gate networks are more effective than long linear chains

For in-system operations like our Asteroid Belt example, range is not a concern. For multi-system mining networks, ensure relay colonies every 3-4 jumps.

---

## Key Decisions Explained

### Automated vs Manned Mines
Automated mines cost 2x but eliminate the need for population transport, infrastructure, and life support. For remote colonies with colony cost 0.00, automated mines are almost always the better choice. Reserve conventional mines for your homeworld or populated colonies where workers are already present.

### Mass Drivers vs Freighters
Mass drivers win on throughput and zero ongoing cost, but require population at both ends. They are ideal for established colonies with large populations (Luna, Mars after terraforming). Freighters win for flexibility and automated-mine colonies.

### Which Minerals to Prioritize
**Gallicite first** -- almost always. Every ship needs engines, and Gallicite has no substitute. After Gallicite:
1. Duranium (hulls, armor, everything)
2. Corundium (if building beam weapons or mines)
3. Neutronium (if building heavy armor)
4. Others as needed by current projects

### Colony Size
For automated mining, colony size is irrelevant (no population needed). For conventional mining with 50 mines, you need 50 x 50,000 = 2,500,000 workers minimum. Plan colony ship capacity accordingly.

---

## Common Mistakes

1. **Not Enough Freighter Capacity**: As mines scale up, mineral stockpiles grow at the colony. If your freighter cannot keep up, minerals pile up uselessly. Monitor colony stockpiles and add freighters when they exceed 1 year of production.

2. **Forgetting Fuel for Freighters**: Commercial engines are fuel-efficient but not free. Ensure your fuel refinery output supports freighter operations. At base tech, each refinery produces 40,000 litres/year -- a single freighter may consume 10,000+ litres per round trip.

3. **Mining Low-Accessibility Deposits First**: A deposit with 0.1 accessibility requires 10x more mines for the same output as a 1.0 deposit. Always compare effective yield (quantity x accessibility) not raw quantity.

4. **Not Checking Colony Cost Before Colonizing**: Mars with colony cost 2.50 requires 2.5 infrastructure per colonist. Sending 100,000 colonists needs 250,000 infrastructure -- a massive industrial investment. Start with colony cost 0.00 bodies.

5. **Ignoring Depletion Timelines**: A 5,000-ton deposit at 1.0 accessibility with 50 mines depletes in 10 years at base tech (5,000 / (50 x 10) = 10). With improved tech (12 tons/mine), that drops to 8.3 years. Plan replacement sources well before depletion.

6. **Building Only One Freighter**: A single freighter is a single point of failure. If it is destroyed, damaged, or reassigned, your entire mineral supply chain stops. Build at least 2 freighters per route for redundancy.

7. **Neglecting Survey Expansion**: Your inner system deposits are finite. Begin surveying adjacent systems via jump points well before home system deposits show signs of depletion. A 20-year lead time for new source development is not excessive.

8. **Overbuilding Early**: 100 automated mines cost 28,800 BP and 24,000 minerals. If your economy only needs 20 tons/year of Gallicite currently, do not build for 200 tons/year capacity. Scale mining to demand with ~50% buffer.

---

## Worked Numbers Summary

### Mining Output at Different Scales

| Mines | Accessibility | Tech Level | Annual Output |
|-------|--------------|------------|---------------|
| 10 | 0.9 | Base (1.0x) | 9 tons/year |
| 20 | 0.9 | Base (1.0x) | 18 tons/year |
| 50 | 0.9 | Improved (1.2x) | 54 tons/year |
| 100 | 0.9 | Advanced (1.44x) | 129.6 tons/year |
| 50 | 0.5 | Base (1.0x) | 25 tons/year |
| 50 | 1.0 | Base (1.0x) | 50 tons/year |

### Freighter Transit Times (at 32 km/s)

| Route | Distance | One-Way | Round Trip |
|-------|----------|---------|------------|
| Earth to Luna | 384,000 km | 3.3 hours | 6.6 hours |
| Earth to Mars (close) | 78M km | 28 days | 56 days |
| Earth to Asteroid Belt | 400M km | 145 days | 290 days |
| Earth to Jupiter | 630M km | 228 days | 456 days |

### Deposit Lifespan Examples

| Deposit Size | Mines | Accessibility | Tech | Annual Draw | Years to Depletion |
|-------------|-------|--------------|------|-------------|-------------------|
| 25,000 | 20 | 0.9 | 1.0x | 18 tons | 1,389 years |
| 25,000 | 50 | 0.9 | 1.2x | 54 tons | 463 years |
| 8,000 | 20 | 1.0 | 1.0x | 20 tons | 400 years |
| 5,000 | 50 | 1.0 | 1.44x | 72 tons | 69 years |

---

## Related Sections

- [Section 5.1 Establishing Colonies](../5-colonies/5.1-establishing-colonies.md) -- Colony cost, infrastructure, and colonist transport
- [Section 6.1 Minerals](../6-economy-and-industry/6.1-minerals.md) -- Mineral types, accessibility, and depletion mechanics
- [Section 6.2 Mining](../6-economy-and-industry/6.2-mining.md) -- Mine types, mass drivers, and construction costs
- [Section 6.5 Civilian Economy](../6-economy-and-industry/6.5-civilian-economy.md) -- Civilian shipping lines, mining contracts, and transport pricing
- [Section 14.1 Fuel](../14-logistics/14.1-fuel.md) -- Standing orders and automated logistics
- [Section 17.1 Geological Survey](../17-exploration/17.1-geological-survey.md) -- Discovering mineral deposits
- [Appendix A: Formulas](../appendices/A-formulas.md) -- Mining output, fuel consumption, and transit calculations
- [Appendix D: Reference Tables](../appendices/D-reference-tables.md) -- Installation costs, mining tech progression, mineral reference
