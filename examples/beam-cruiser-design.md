# Example: Designing Your First Beam Cruiser

This worked example walks through the complete design process for a 10,000-ton beam cruiser optimized for medium-range engagement. We will make every decision step by step, showing the math behind each choice and explaining the trade-offs involved.

## Objective

Design a **10,000-ton beam cruiser** capable of:

- Engaging hostile warships at medium beam range (~200,000-400,000 km)
- Sustaining combat for multiple volleys
- Operating independently within a star system (reasonable fuel endurance)
- Surviving return fire from comparable opponents

## Starting Conditions

- **TN Start**: Nuclear Thermal Engine technology (5 EP/HS), Pressurised Water Reactor
- **Laser Technology**: 10cm focal size available, Ultraviolet wavelength (1.0x range modifier)
- **Fire Control**: Beam FC with tracking speed up to 5,000 km/s
- **Engine Power Multiplier**: 5 EP/HS (base, no boost applied yet)
- **Fuel Consumption Modifier**: 0.5 (halved consumption, larger engine)
- **Armor**: Duranium (strength 5 per layer)
- **Shipyard**: Naval yard capable of 10,000 tons

---

## Step 1: Determine Role and Engagement Range

Our cruiser is a **medium-range beam combatant**. This means:

- We want to fight at 150,000-300,000 km (close enough for beam accuracy, far enough to maneuver)
- We need weapons that deal meaningful damage at this range
- We need speed to dictate engagement terms against slower opponents
- We need enough armor to survive several volleys while trading fire

**Design target speed**: ~4,000 km/s (fast enough to outrun heavy ships, close enough to catch most opponents)

---

## Step 2: Engine Sizing

We want 4,000 km/s from a 10,000-ton hull. Using the speed formula:

```
Speed (km/s) = Total_Engine_Power / Ship_Mass (tons)
```

Solving for required Engine Power:
```
Required EP = Speed x Ship_Mass
Required EP = 4000 x 10000 / 5000
Required EP = 8000 EP (using the practical formula: Speed = EP * 5000 / Mass)
```

Wait -- let us use the correct practical formula from the manual:
```
Speed = Total EP * 5000 / Ship_Mass (tons)
4000 = Total EP * 5000 / 10000
Total EP = 4000 * 10000 / 5000
Total EP = 8000 EP
```

**But** this assumes the final ship mass is exactly 10,000 tons. In practice, the engines themselves add mass. We need to iterate. Let us start with the engine calculation:

With Nuclear Thermal Engine at 5 EP/HS, we can apply a power boost. Let us try a **1.25x boost** (the sweet spot per Appendix D -- 25% more power with ~56% more fuel consumption):

```
Boosted EP/HS = 5 x 1.25 = 6.25 EP/HS
```

With fuel consumption modifier of 0.5, our engines are physically larger but more fuel-efficient. A 25 HS engine (the maximum starting size) produces:
```
Engine Power = 25 HS x 6.25 EP/HS = 156.25 EP per engine
Engine Mass = 25 HS x 50 tons/HS = 1,250 tons per engine
```

We need ~8,000 EP. Let us try 4 engines:
```
4 engines x 156.25 EP = 625 EP total
```

That is far too low. The issue is that at TN start with only 5 EP/HS, engines are quite weak. Let us recalculate without the fuel consumption modifier affecting size (the fuel consumption modifier of 0.5 makes the engine larger for the same power):

Actually, re-reading Section 8.3.4: "Lower fuel consumption values increase the engine's physical size for the same power output." So with fuel consumption 0.5, an engine occupies 2x the HS for the same EP output. This means:

```
Effective EP/HS (with 0.5 fuel mod) = 6.25 / 2 = 3.125 EP per HS of engine
```

This is extremely bulky. Let us reconsider and use a fuel consumption modifier of **1.0** (standard) with 1.25x boost instead:

```
EP/HS = 5 x 1.25 = 6.25 EP/HS (at standard fuel consumption)
```

For 4 engines at 25 HS each:
```
Total EP = 4 x 25 x 6.25 = 625 EP
Engine Mass = 4 x 25 x 50 = 5,000 tons
```

Speed with just engines and remaining hull:
```
Speed = 625 * 5000 / 10000 = 312.5 km/s
```

This is far too slow. The problem is clear: **at TN-start technology (5 EP/HS), a 10,000-ton cruiser cannot achieve 4,000 km/s**. Let us recalculate what speed is actually achievable.

**Revised speed target**: Let us determine how fast we CAN go, dedicating ~40% of tonnage to engines:

```
Engine tonnage: 4,000 tons = 80 HS total
With 1.25x boost: EP = 80 x 5 x 1.25 = 500 EP
Speed = 500 * 5000 / 10000 = 250 km/s
```

Still too slow. At TN start, we clearly need to adjust expectations. Let us use a **higher boost** (1.5x, accepting 305% fuel consumption):

```
EP = 80 HS x 5 x 1.5 = 600 EP
Speed = 600 * 5000 / 10000 = 300 km/s
```

**Reality check**: At TN-start technology, 10,000-ton beam cruisers are very slow. A more realistic target with Nuclear Thermal is approximately **250-400 km/s** for a full cruiser. For our worked example, let us assume we have researched **one level up** to Nuclear Pulse Engine (8 EP/HS), which is listed as "Early" era and a natural first research target.

**Revised starting assumption**: Nuclear Pulse Engine (8 EP/HS)

```
Engine tonnage budget: 3,000 tons = 60 HS
Split into 3 engines of 20 HS each (for redundancy)
Boost: 1.25x
EP per engine = 20 x 8 x 1.25 = 200 EP
Total EP = 3 x 200 = 600 EP
Engine HTK = sqrt(20) = 4.47 per engine (good redundancy)
```

Preliminary speed estimate (assuming ~10,000 total tons):
```
Speed = 600 * 5000 / 10000 = 300 km/s
```

Hmm, still low. Let us push to **50% of tonnage in engines** (5,000 tons = 100 HS), split as 4 engines of 25 HS:

```
EP per engine = 25 x 8 x 1.25 = 250 EP
Total EP = 4 x 250 = 1000 EP
Speed = 1000 * 5000 / 10000 = 500 km/s
Engine HTK = sqrt(25) = 5 per engine
```

**Final engine decision**: 4x 25 HS Nuclear Pulse Engines at 1.25x boost

- Total engine mass: 5,000 tons
- Total EP: 1,000
- Speed (at 10,000 tons): ~500 km/s
- Engine HTK: 5 each (20 total -- excellent redundancy)

**Note**: 500 km/s is modest but workable for early-game. Fleet doctrine should pair this cruiser with escorts of similar speed.

---

## Step 3: Weapon Selection -- Laser vs Particle Beam

At this tech level, our choices are:

**10cm Laser (UV wavelength)**:

- Damage: 10 per shot (focal size = damage)
- Power required: 10
- Range: base UV range for 10cm (approximately 160,000 km at starting tech)
- Size: approximately 3 HS (150 tons) at base recharge rate
- Damage pattern: Gradient 3 (focused -- excellent armor penetration)

**Particle Beam-4** (if researched):

- Damage: 4 per shot
- Power required: 10
- Range: 200,000 km
- Size: 7 HS (350 tons)
- Damage: single-column (all damage to one armor location)
- No damage falloff within range

**Decision: Lasers win at this tech level.** Here is why:
1. Lasers deal 10 damage vs particle beam's 4 damage for the same power draw
2. Lasers are smaller (3 HS vs 7 HS) -- we can fit more weapons
3. Laser gradient-3 damage pattern already focuses damage well for penetration
4. Particle beams shine later when armor is thicker and single-column penetration matters more

**Weapon loadout**: 6x 10cm Lasers
```
Weapon tonnage: 6 x 3 HS x 50 = 900 tons (18 HS total)
Total power draw: 6 x 10 = 60 power
Total damage per volley: 6 x 10 = 60 damage
```

---

## Step 4: Fire Control Matching

The fire control must:
1. **Track at or above target speed** -- if our FC tracks at 5,000 km/s, it has full accuracy against targets moving up to 5,000 km/s
2. **Have sufficient range** to cover our weapon envelope

```
Tracking modifier = min(1.0, FC_Tracking_Speed / Target_Speed)
```

With FC tracking 5,000 km/s vs a target at 500 km/s (our own speed class):
```
Tracking mod = min(1.0, 5000 / 500) = 1.0 (full accuracy)
```

Even against faster targets at 3,000 km/s:
```
Tracking mod = min(1.0, 5000 / 3000) = 1.0 (still full accuracy)
```

Our 5,000 km/s tracking is more than adequate for this era. It would only degrade against targets faster than 5,000 km/s.

**Fire control range**: We need the FC to cover at least our laser maximum range (~160,000 km). From the formula:
```
FC_Range = FC_Size x Resolution x FC_Tech_Level x 10,000 km
```

A standard beam FC provides range based on its size. We need range >= 160,000 km. With starting tech, a 2 HS beam FC should provide adequate range for our weapon envelope.

**Fire control allocation**: 2x Beam Fire Controls (2 HS each = 4 HS total = 200 tons)

- 3 lasers assigned per FC (provides redundancy -- if one FC is destroyed, half the weapons still fire)

---

## Step 5: Sensor Selection

Our cruiser needs to detect targets at engagement range or beyond. We need:

- **Active sensor** to detect enemy ships
- Resolution matched to expected target size

From the active sensor formula:
```
Detection_Range = sqrt(Sensor_Strength x Target_Cross_Section) x 10,000 km
```

Where:
```
Target_Cross_Section = Target_Tonnage / 50
```

For detecting a 10,000-ton ship (200 HS cross-section) at 500,000 km (beyond weapon range for early warning):
```
500,000 = sqrt(Sensor_Strength x 200) x 10,000
50 = sqrt(Sensor_Strength x 200)
2500 = Sensor_Strength x 200
Sensor_Strength = 12.5
```

A sensor of resolution 100 (optimized for ~5,000-ton ships) at approximately 5 HS should provide adequate detection range for our needs.

**Sensor allocation**: 1x Active Sensor (5 HS = 250 tons), resolution 100

- Detects 10,000-ton ships well beyond weapon range
- Detects 5,000-ton ships at full rated range
- Smaller targets detected at reduced range per the sqrt scaling

---

## Step 6: Armor Selection

With Duranium armor (strength 5 per layer), we need to decide on thickness. Our expected threats are similar-era beam weapons dealing 4-10 damage per hit.

**Armor depth analysis**:

- A 10-damage laser hit vs 5-strength Duranium: penetrates 2 layers per hit
- A 4-damage particle beam: does NOT penetrate even 1 layer (4 < 5)
- Multiple hits to same column will progressively strip armor

Per the guidelines in Section 8.2.3, 4-5 layers is "moderate protection, good for cruiser-weight combatants."

**Decision: 4 layers of Duranium armor**

Armor weight for a 10,000-ton ship at 4 layers (approximate from Section 8.2.3):
```
Armor mass: approximately 2,500-3,500 tons
```

Let us estimate 3,000 tons for our calculations.

**Armor allocation**: 4 layers Duranium = ~3,000 tons

- Stops particle beam hits completely (4 damage < 5 strength)
- Requires 2 laser hits to same column to penetrate (10 damage strips 2 layers)
- Provides 20 total armor strength per column before internals exposed

---

## Step 7: Shield Consideration

**Trade-off analysis**:

A 10 HS shield generator (the starting maximum size) provides:
```
Shield Strength Modifier = sqrt(10/10) = 1.0 (standard reference strength)
```

This costs 500 tons (10 HS x 50 tons) and:

- Provides an energy buffer before armor takes hits
- Generates EM signature (Shield_Strength x 3) making us visible to passive EM sensors
- Requires Corbomite (may be scarce early)
- A single 10 HS generator has HTK = sqrt(10) = 3.16 -- could be destroyed by a few hits

**Decision: Skip shields on this design.** Reasons:
1. At this tech level, shield generators are relatively weak (max 10 HS)
2. The 500 tons is better spent on additional armor or weapons
3. EM signature increase makes us detectable at greater range
4. Corbomite may be needed for other projects
5. A single 10 HS generator is a fragile single point of failure

**Note**: Revisit this decision once Maximum Shield Generator Size research allows 20+ HS generators, where the sqrt scaling provides meaningful efficiency gains.

---

## Step 8: Power Plant Sizing

Our 6 lasers each draw 10 power = 60 total power required.

Using Power Plant output formula:
```
Power_Output = Power_Tech x Size_HS x sqrt(Size_HS / 10)
```

At starting Pressurised Water Reactor tech (let us assume Power_Tech = 5):
```
For a 10 HS power plant:
Output = 5 x 10 x sqrt(10/10) = 5 x 10 x 1.0 = 50 power
```

That is short of our 60 power requirement. Options:
1. One 10 HS plant (50 power) + one small supplemental plant
2. One larger plant (if tech allows)
3. Apply boost

**With 20% boost** (manageable explosion risk at 15%):
```
Boosted output = 50 x 1.2 = 60 power (exactly what we need)
Explosion chance when hit = 5% + (20/2)% = 15%
```

**Decision: 1x 10 HS Power Plant with 20% boost**

- Output: 60 power (matches weapon draw exactly)
- Mass: 500 tons
- HTK: sqrt(10) = 3.16
- Explosion risk: 15% when hit (acceptable)

**Redundancy concern**: A single power plant is a vulnerability. If destroyed, all weapons lose power. Consider adding a 2 HS backup:
```
Backup: 2 HS plant, output = 5 x 2 x sqrt(2/10) = 5 x 2 x 0.447 = 4.47 power
```

That only powers a fraction of one laser. Not worth the tonnage for such minimal backup. **Accept the single-point-of-failure** at this tonnage constraint.

**Power plant allocation**: 1x 10 HS reactor (20% boost) = 500 tons

---

## Step 9: Fuel Tankage

We want enough fuel for sustained system operations. Target: ability to traverse a solar system and engage in combat (~15-20 billion km range).

Fuel consumption with 1.25x engine boost:
```
Boost penalty at 1.25x: approximately 1.56x fuel consumption
Fuel per hour = Total_EP x Fuel_Consumption_Rate x Boost_Penalty
```

With standard fuel consumption rate (1.0) and 1.25x boost:
```
Fuel per hour = 1000 EP x 1.0 x 1.56 = 1,560 litres/hour (approximate)
```

For 15 billion km range:
```
Range (billion km) = Fuel_Capacity / Fuel_per_Hour x Speed x 3600 / 1,000,000,000
15 = Fuel_Capacity / 1560 x 500 x 3600 / 1,000,000,000
15 = Fuel_Capacity x 1,800,000 / (1560 x 1,000,000,000)
15 = Fuel_Capacity x 0.001154
Fuel_Capacity = 15 / 0.001154 = approximately 13,000,000 litres
```

Standard fuel tanks hold 50,000 litres per 250 tons. So:
```
Fuel tanks needed = 13,000,000 / 50,000 = 260 tanks
Tank mass = 260 x 250 = 65,000 tons
```

That is absurd -- more than 6x our ship mass. The issue: at this low speed (500 km/s), enormous fuel is needed for range. This is a fundamental limitation of early-tech beam cruisers.

**Practical adjustment**: Accept shorter range (~5 billion km, enough for inner system operations):
```
Fuel needed for 5 billion km:
5 = Fuel_Capacity x 0.001154
Fuel_Capacity = approximately 4,330,000 litres
Tank mass = 4,330,000 / 200 = approximately 21,650 tons
```

Still too much. Let us simply allocate **15-20% of hull tonnage** to fuel (the warship guideline from Section 8.3.4):

```
Fuel allocation: 1,500 tons = 300,000 litres (6 standard tanks)
```

This gives us limited but workable operational range for system defense. Our cruiser will need tanker support for extended deployments.

**Fuel allocation**: 1,500 tons (300,000 litres)

---

## Step 10: Bridge, Engineering Spaces, MSP Storage

**Bridge**: Mandatory on all ships. 1 HS = 50 tons.

**Engineering spaces**: Critical for maintenance and damage control. Per the Annual Failure Rate formula:
```
AFR_Without_Engineering = 0.2 x Ship_Tonnage (percent)
AFR_With_Engineering = (0.04 / Engineering_Tonnage_Percent) x Ship_Tonnage
```

Targeting 5% engineering (500 tons):
```
AFR = (0.04 / 0.05) x 10000 = 0.8 x 10000 = 8000...
```

Actually, the percentage is of total tonnage. With 500 tons engineering on a 10,000 ton ship (5%):
```
Engineering_Tonnage_Percent = 500 / 10000 = 0.05 (5%)
```

This provides reasonable maintenance support. The MSP stored:
```
MSP_Stored = floor(12.5 x Ship_Build_Cost_BP x Engineering_Tons / Total_Ship_Tons)
MSP_Stored = floor(12.5 x [Build_Cost] x 500 / 10000)
```

The exact MSP depends on total build cost, but 5% engineering gives decent damage repair capability.

**Allocations**:

- Bridge: 50 tons (1 HS)
- Engineering: 500 tons (10 HS, 5% of hull)

---

## Step 11: Final Design Review

### Mass Budget

| Component | Mass (tons) | HS |
|-----------|------------|-----|
| Engines (4x 25 HS) | 5,000 | 100 |
| Lasers (6x 10cm) | 900 | 18 |
| Fire Controls (2x) | 200 | 4 |
| Active Sensor (1x) | 250 | 5 |
| Power Plant (1x 10 HS) | 500 | 10 |
| Armor (4 layers Duranium) | ~3,000 | -- |
| Fuel Tanks | 1,500 | 30 |
| Bridge | 50 | 1 |
| Engineering | 500 | 10 |
| **Subtotal** | **~11,900** | -- |

**Problem**: We are ~1,900 tons over budget. This is the fundamental iteration loop of ship design. Options:

1. **Reduce engines** (drop to 3 engines = 3,750 tons, lose 250 EP, speed drops to ~375 km/s)
2. **Reduce armor** (3 layers instead of 4, saves ~750 tons)
3. **Reduce weapons** (5 lasers instead of 6, saves 150 tons)
4. **Reduce fuel** (saves some tonnage)

**Revised design** -- applying option 1 + 2 + trimming fuel:

| Component | Mass (tons) | HS |
|-----------|------------|-----|
| Engines (3x 25 HS) | 3,750 | 75 |
| Lasers (6x 10cm) | 900 | 18 |
| Fire Controls (2x) | 200 | 4 |
| Active Sensor (1x) | 250 | 5 |
| Power Plant (1x 10 HS) | 500 | 10 |
| Armor (3 layers Duranium) | ~2,250 | -- |
| Fuel Tanks | 1,000 | 20 |
| Bridge | 50 | 1 |
| Engineering | 500 | 10 |
| **Total** | **~9,400** | -- |

Remaining: 600 tons for crew quarters, additional sensors, or a small backup reactor.

### Final Performance Characteristics

```
Speed = 750 EP * 5000 / 10000 = 375 km/s
Armor: 3 layers x 5 strength = 15 damage to penetrate per column
Firepower: 60 damage per volley (6 lasers x 10 damage)
Range: Limited system defense (~200 million km operational radius)
```

---

## Key Decisions Explained

### Why Laser Over Particle Beam?
At early tech, lasers deal 2.5x more damage per power unit (10 vs 4) and occupy less than half the hull space per weapon. Particle beams become competitive when armor reaches 6+ layers and single-column penetration matters. At 3-4 layers of Duranium, raw laser damage is more effective.

### Speed vs Armor Trade-Off
We chose 3 layers (speed doctrine leaning) over 5+ layers (armor doctrine). At 375 km/s, we can disengage from slower opponents but cannot outrun fast scouts. The 3 layers stop particle beams cold and require 2 laser hits per column to penetrate -- reasonable for trading fire at medium range.

### Number of Weapons vs Individual Size
Six 10cm lasers provide better sustained firepower than fewer larger weapons because:

- More individual shots means more chances to hit
- If one laser is destroyed, you lose only 1/6 of firepower
- Six weapons spread across 2 fire controls gives redundancy
- Overkill on each shot is wasted; more smaller shots is often better than fewer large ones

---

## Common Mistakes

1. **Forgetting Power Plants**: Without a reactor, beam weapons cannot fire. Every laser, railgun, and particle beam requires power. Always calculate total power draw before finalizing weapons.

2. **Undersizing Fire Control Tracking**: If your FC tracks at 3,000 km/s but the target moves at 5,000 km/s, your hit chance is reduced to 60%. Always match or exceed expected target speeds.

3. **No Engineering Spaces**: Ships without engineering suffer high failure rates and cannot repair damage in the field. The formula `AFR = 0.2 x Tonnage` without engineering means a 10,000-ton ship has a significant annual failure chance.

4. **Insufficient Fuel for Concept of Operations**: A system defense ship needs 5-15 billion km range minimum. Calculate your actual range, not just fuel mass. At low speeds, even large fuel loads provide short range.

5. **Ignoring the Iterative Nature of Design**: Your first pass will almost always exceed tonnage. Budget overruns of 10-30% are normal in the initial draft. Plan for 2-3 iterations trimming components.

6. **Single Point of Failure Components**: One power plant, one fire control, or one engine means a single hit can cripple your ship. Where tonnage allows, distribute critical systems across multiple components.

7. **Designing in Isolation**: If your cruiser moves at 375 km/s but your destroyers move at 600 km/s, the task group is limited to cruiser speed. Design your fleet as a system.

---

## Related Sections

- [Section 8.1 Design Philosophy](../8-ship-design/8.1-design-philosophy.md) -- Ship designer interface and workflow
- [Section 8.2 Hull and Armor](../8-ship-design/8.2-hull-and-armor.md) -- Armor types, layers, and weight calculations
- [Section 8.3 Engines](../8-ship-design/8.3-engines.md) -- Engine technology, boost, fuel consumption
- [Section 8.4 Sensors](../8-ship-design/8.4-sensors.md) -- Sensor resolution and fire control matching
- [Section 8.5 Weapons](../8-ship-design/8.5-weapons.md) -- Laser, railgun, and particle beam specifications
- [Appendix A: Formulas](../appendices/A-formulas.md) -- Speed, range, sensor, and combat calculations
- [Appendix D: Reference Tables](../appendices/D-reference-tables.md) -- Beam weapon comparison and technology progression
