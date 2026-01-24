# Example: Defending a Jump Point

This worked example walks through establishing a comprehensive defensive position at a jump point connecting to known hostile space. Every major decision is supported by calculations drawn from the game's formulas, and common pitfalls are highlighted throughout.

## Objective

Establish a layered defensive position at a jump point connecting to a system occupied by a known hostile NPR. The defense must detect, engage, and destroy enemy forces transiting the jump point before they can threaten your colony 1.2 billion km away.

## Starting Conditions

- **Hostile contact:** Known NPR one system away, observed with military-engine ships up to 10,000 tons
- **Jump point location:** 1.2 billion km from your colony
- **Sensor technology:** Active Sensor Strength Level 4, EM Sensor Sensitivity Level 4
- **Weapons available:** Missile and beam weapons (mid-game technology)
- **Missile technology:** Size-6 anti-ship missiles at 20,000 km/s, size-1 AMMs at 32,000 km/s
- **Beam technology:** 15cm lasers, gauss cannons with rate-of-fire 4 (triple turret)
- **Fleet speed:** Combat fleet at 5,000 km/s, pickets at 8,000 km/s
- **FC tracking speed:** 16,000 km/s (PD fire controls)
- **Enemy estimates:** Ships likely in the 15,000-25,000 km/s missile speed range based on observed engine technology

---

## Step 1: Sensor Picket Deployment

The first requirement is detecting enemy transits before their weapons reach your fleet. A dedicated sensor picket stationed near the jump point provides early warning.

### Picket Ship Design

Design a small, fast sensor ship optimized for detection range and survival through speed:

- **Hull:** 2,000 tons (40 HS)
- **Active sensor:** 6 HS, resolution 100 (for fleet detection), Active Sensor Strength tech level 4
- **Passive EM sensor:** 5 HS, EM Sensitivity tech level 4
- **Passive thermal sensor:** 5 HS, Thermal Sensitivity tech level 4
- **Engines:** Sufficient for 8,000 km/s (fast enough to outrun most combatants)
- **Jump drive:** None (relies on jump tender or jump gate for deployment)
- **Armament:** None (speed is its defense)

### Active Sensor Detection Range Calculation

Using the C# Aurora active sensor formula from Appendix A:

```
Detection Range (km) = SQRT(Sensor_Sensitivity * Target_Cross_Section) * 10,000
```

Where:
- Sensor_Sensitivity = Size (HS) * Active_Sensor_Strength * Resolution^(1/1.5)
- Target_Cross_Section = Target HS (for resolution-matched or larger targets)

For our 6 HS sensor at resolution 100, tech level 4:

```
Sensor_Sensitivity = 6 * 4 * 100^(1/1.5) = 24 * 21.54 = 517
```

Against a 10,000-ton (200 HS) target (larger than resolution 100, so full range applies):

```
Detection Range = SQRT(517 * 200) * 10,000
               = SQRT(103,400) * 10,000
               = 321.6 * 10,000
               = 3,216,000 km (~3.2 million km)
```

Against a 5,000-ton target (100 HS, matches resolution exactly):

```
Detection Range = SQRT(517 * 100) * 10,000
               = SQRT(51,700) * 10,000
               = 227.4 * 10,000
               = 2,274,000 km (~2.3 million km)
```

### Passive Sensor Detection

The EM sensor detects enemy active sensors and shields without revealing the picket's position:

```
EM Detection Range (km) = Sensor_Sensitivity * Target_EM_Signature * 10,000
```

With a 5 HS EM sensor at tech level 4:
- Sensor_Sensitivity = 5 * 4 = 20

If the enemy raises shields (estimated strength 100, EM output = 300):

```
EM Detection Range = 20 * 300 * 10,000 = 60,000,000 km (60 million km)
```

If the enemy activates sensors (estimated EM output 150):

```
EM Detection Range = 20 * 150 * 10,000 = 30,000,000 km (30 million km)
```

The thermal sensor detects engine emissions:

```
Thermal Detection Range (km) = Sensor_Sensitivity * Target_Thermal_Signature * 10,000
```

With a 5 HS thermal sensor at tech level 4, Sensitivity = 20.
Against a 10,000-ton warship with engine power 5,000 (standard engines, thermal sig = 5,000):

```
Thermal Detection Range = 20 * 5,000 * 10,000 = 1,000,000,000 km (1 billion km)
```

This is enormous -- passive thermal detection of a full-power warship fleet is highly effective at extreme range.

### Picket Positioning

Station 2-3 picket ships within 500,000 km of the jump point under EMCON (all active sensors OFF). With passive thermal sensors, they will detect any ship transiting the JP the moment it begins moving under power. Keep active sensors in reserve to confirm contacts and provide targeting data when needed.

**Why EMCON matters:** A picket running active sensors has an EM signature of 6 * 4 = 24. An enemy EM sensor could detect this before the picket detects them. Under EMCON, the picket is nearly invisible (idle thermal signature = 40 HS * 0.05 = 2, detectable only at very short range).

---

## Step 2: Fleet Positioning

### Why NOT on the Jump Point

Stationing your combat fleet directly on the jump point is the single most common mistake in jump point defense. Here is why it fails:

1. **No reaction time:** Ships transiting a JP arrive at the exact JP location. If your fleet is there, combat begins at point-blank range with no time to assess the threat.
2. **Beam advantage negated:** Your beam weapons have maximum accuracy at range 0, but so do the enemy's. You lose the advantage of choosing engagement range.
3. **Missile doctrine useless:** Your missiles cannot be used effectively at 0 km -- they need flight distance to build separation from PD.
4. **Surprise salvos:** An enemy fleet could pre-fire missiles timed to arrive at the JP simultaneously with their transit, catching your fleet between ships and missiles.
5. **Fire delay:** Ships suffer a fire delay after jump point transit (see Section 12.4.2). But if YOUR fleet is on the JP and the enemy jumps in, the enemy has fire delay -- you do not. This is the ONE advantage of JP positioning, but it is massively outweighed by the disadvantages above.

### Optimal Fleet Distance

Station your combat fleet at a distance that provides:
- Enough time to assess the threat after sensor detection
- Distance for missiles to build separation from your fleet
- Room to maneuver (retreat or advance) based on threat assessment

**Calculation -- Response Time Available:**

Assume the enemy fleet travels at 4,000 km/s after transit (a reasonable estimate for cruiser-weight ships). Your sensors detect them at the jump point (within 500,000 km of pickets).

If your fleet is stationed 2 million km from the JP:

```
Time to Contact = Distance / Enemy Speed
                = 2,000,000 km / 4,000 km/s
                = 500 seconds (~8 minutes 20 seconds)
```

This gives you over 8 minutes of game time (at 5-second increments, that is 100 combat ticks) to:
- Confirm hostile intent
- Launch missiles
- Adjust fleet positioning
- Activate shields and sensors

If your fleet is stationed 5 million km from the JP:

```
Time to Contact = 5,000,000 / 4,000 = 1,250 seconds (~21 minutes)
```

More reaction time, but the enemy also has more time to assess and potentially retreat through the JP.

### Recommended Position: 3-5 Million km from JP

A distance of 3-5 million km provides:
- 12-21 minutes of reaction time at enemy speed 4,000 km/s
- Within your active sensor detection range (3.2M km for 10,000-ton targets)
- Within missile engagement range (your size-6 missiles likely have 150-300M km range)
- Far enough that enemy beam ships cannot immediately close to beam range

Station the fleet perpendicular to the JP-colony axis, so retreating draws the enemy away from your colony rather than toward it.

---

## Step 3: Engagement Doctrine

### Missile-First Doctrine (Recommended for JP Defense)

At jump point defense, missile-first doctrine is superior because:
- You fire at maximum range while the enemy is still organizing after transit
- Enemy ships suffer fire delay after JP transit (they cannot immediately shoot back)
- Missiles thin enemy numbers before beam range is reached
- You maintain the option to withdraw if the force is overwhelming

**Missile Engagement Envelope:**

Your size-6 missiles at 20,000 km/s with 2 MSP fuel allocation:

```
Fuel capacity = 2 MSP * 2,500 = 5,000 fuel units
Fuel consumption = missile fuel rate (from engine design)
Range = Speed * Endurance
```

Assume your missile design yields approximately 200 million km range. At 20,000 km/s:

```
Flight time to 5M km = 5,000,000 / 20,000 = 250 seconds (just over 4 minutes)
```

This means your first salvo hits the enemy approximately 4 minutes after launch -- well before a 4,000 km/s enemy fleet closes to beam range.

**Salvo Size Planning:**

Against a potential force of 5-10 enemy warships with unknown PD capability:
- Launch a minimum of 30 missiles per salvo (overwhelms typical PD of 10-15 kills/tick)
- Hold second salvo ready for 60 seconds after first to follow up
- Reserve 30% of missile capacity for subsequent waves

### When to Switch to Beam-Only

Use beam-only doctrine when:
- You have expended all missiles and the enemy is still advancing
- The enemy force is small enough that beam weapons can handle it
- Enemy ECM is defeating your missile fire controls

---

## Step 4: Point Defense Layers

### Layer 1: AMM Screen (Long-Range Intercept)

Your size-1 AMMs at 32,000 km/s with resolution-1 missile fire controls.

**AMM Fire Control Range:**

```
MFC Range = SQRT(FC_Sensitivity * Target_Cross_Section) * 10,000
```

For a resolution-1 fire control (6 HS, tech level 4) detecting a 6 MSP (15 ton, ~0.3 HS) incoming missile:

```
FC_Sensitivity = 6 * 4 * 1^(1/1.5) = 24
Target_Cross_Section = 0.3 (enemy missile HS)
Range = SQRT(24 * 0.3) * 10,000 = SQRT(7.2) * 10,000 = 26,833 km
```

This is shorter than ideal. Increase the FC size or consider using passive thermal detection for initial missile warning, with the MFC guiding AMMs for final intercept.

**AMM Intercept Calculation:**

Against incoming missiles at 20,000 km/s, your AMMs at 32,000 km/s:
- Speed advantage: AMMs are faster, so they CAN catch the incoming missiles
- At 32,000 km/s with short fuel endurance, AMMs cover their engagement envelope quickly

**AMM Magazine Sizing:**

Carry at least 3x the expected incoming salvo size in AMMs:
- Expected enemy salvo: 20-40 missiles
- Required AMM stockpile: 60-120 per engagement
- With size-1 AMMs, a single magazine holding 60 MSP of missiles = 60 AMMs
- Deploy 2-3 dedicated AMM magazines per PD ship

### Layer 2: Ranged Beam Defense (Lasers at Distance)

15cm lasers in Ranged Defensive Fire mode engage survivors between full weapon range and 10,000 km:

```
Laser hit chance vs. missile = (1 - Range/Max_Range) * Tracking_Mod
Tracking_Mod = min(1.0, FC_Tracking / Missile_Speed)
             = min(1.0, 16,000 / 20,000)
             = 0.8
```

At 50% of laser range: Base chance = 50% * 0.8 = 40% per shot.
At 10,000 km (point blank for lasers): Base chance = near 100% * 0.8 = 80% per shot.

### Layer 3: CIWS (Final Fire, 10,000 km)

Triple-turret gauss cannons with rate-of-fire 4 technology:

```
Shots per tick = 3 turrets * 4 shots = 12 shots per 5-second tick
Hit Probability = min(1.0, FC_Tracking / Missile_Speed) * Crew_Training
                = min(1.0, 16,000 / 20,000) * 1.0
                = 0.8
Expected kills per tick = 12 * 0.8 = 9.6 missiles
```

With 4 CIWS installations across your fleet:

```
Total fleet CIWS kills per tick = 4 * 9.6 = 38.4 missiles
```

This means your CIWS layer alone can handle a salvo of approximately 38 missiles per 5-second tick.

### Combined Layer Effectiveness

Against a 50-missile salvo:

```
Layer 1 (AMMs, 40% kill rate): 50 * 0.6 = 30 survive
Layer 2 (Ranged beams, 25% kill rate): 30 * 0.75 = 22.5 survive
Layer 3 (CIWS, 38 kills/tick capacity): max(0, 22 - 38) = 0 survive
```

Your layered defense handles a 50-missile salvo with margin. But against 100+ missiles, CIWS becomes the bottleneck:

```
Layer 1: 100 * 0.6 = 60 survive
Layer 2: 60 * 0.75 = 45 survive
Layer 3: 45 - 38 = 7 missiles leak through
```

Plan your PD capacity for 1.5-2x the expected maximum enemy salvo.

---

## Step 5: Jump Point Monitoring with Passive Sensors

### Stealth Detection Strategy

The ideal detection posture at a JP uses passive sensors exclusively until hostiles are confirmed:

1. **Thermal sensors** detect any ship the moment it begins moving after transit (thermal signature from engines)
2. **EM sensors** detect enemy active sensors or shields activating
3. **No active emissions** from your pickets -- the enemy does not know you are watching

### Detecting Transit Signatures

When a ship transits a jump point:
- It appears at the JP location
- If it has movement orders, it immediately produces thermal signature
- If it activates sensors or shields, it produces EM signature
- A ship that transits and remains stationary with all systems off produces only idle thermal (5% of HS)

**Worst-case detection (enemy under full EMCON, stationary after transit):**

A 10,000-ton ship (200 HS) stationary with no active systems:
- Idle thermal signature = 200 * 0.05 = 10
- With your 5 HS thermal sensor (sensitivity 20):

```
Detection range = 20 * 10 * 10,000 = 2,000,000 km (2 million km)
```

Your pickets at 500,000 km from the JP will detect even a fully silent, stationary warship.

**Best-case detection (enemy under power with active sensors):**

Detection occurs at ranges of 30-1,000+ million km, giving your fleet minutes to hours of warning.

### Information Chain

```
Picket detects transit (passive) --> Reports contact to fleet via fleet communications
--> Fleet activates sensors to confirm --> Fleet engages per doctrine
```

The key advantage: your fleet's position remains unknown to the enemy until you choose to reveal it by activating sensors or firing.

---

## Step 6: Reserve Positioning

### Reinforcement Station

Position reserve forces at your colony, 1.2 billion km from the JP:

```
Transit time (reserves at 5,000 km/s) = 1,200,000,000 / 5,000 = 240,000 seconds
                                       = 66.7 hours (~2.8 days)
```

This is a long transit time. Reserves cannot reinforce quickly unless you pre-position them closer.

**Alternative: Forward Reserve Position**

Station reserves 200 million km behind your main fleet (500 million km from JP):

```
Transit time = 200,000,000 / 5,000 = 40,000 seconds = 11.1 hours
```

Still slow for immediate reinforcement, but reserves arrive within a day of combat.

### Fuel Logistics

Extended deployment at a JP requires fuel support:

- **Tanker deployment:** Station 1-2 tankers with your fleet for refueling
- **Fuel depot:** If near a planet or asteroid with Sorium deposits, establish a fuel harvesting operation
- **Rotation:** Cycle ships back to colony for maintenance before their maintenance clocks expire
- **Fuel consumption while stationary:** Stationary ships consume no fuel (engines off), so only pickets and maneuvering forces consume fuel during peacetime

**Tanker Sizing:**

If your combat fleet has total fuel capacity of 500,000 litres and consumes 2,000 litres/hour under power:
- 250 hours of continuous maneuvering before empty
- A single tanker with 200,000 litres provides one full top-up
- Deploy 2 tankers for sustained operations

---

## Step 7: Minefield and Defensive Installation Options

### Buoy Mines at the JP

Missiles designed with no engine (0 km/s speed) can be deployed as stationary mines at the jump point:

- Design a mine as a size-6 missile with maximum warhead, no engine, onboard sensor
- Deploy via minelayer ships that drop mines at the JP coordinates
- Mines activate their sensors when a target transits within detection range
- Effective as a first-strike surprise against unaware enemies

**Limitation:** Mines are stationary and have limited sensor range. A cautious enemy may detect them before entering their engagement envelope.

### PDC Placement (If JP is Near a Planet)

If the jump point happens to be within 200 million km of a planet or moon:

- Build Planetary Defense Centers (PDCs) on that body
- PDCs require no bridge, no jump drive, and no engines
- They can mount massive missile batteries and beam weapons
- They are extremely difficult to destroy (treated as ground installations)

PDCs are ideal JP defenders but require a convenient body near the JP -- which is uncommon.

### Jump Point Defense Station

As an alternative to PDCs, build a large defensive station (no engines) and tow it to the JP:

- Design as a ship with no engines (0 km/s speed, cannot be moved after placement without a tug)
- Mount heavy missile batteries, large magazines, and extensive CIWS
- Include large active sensors for fire control
- Station it 1-2 million km from the JP

**Disadvantage:** Cannot maneuver, and represents a significant investment that is lost if the JP is bypassed.

---

## Step 8: Response Timing Calculations

### Scenario: Enemy Fleet Transits at 4,000 km/s

```
Timeline from transit to engagement:

T+0 seconds:     Enemy fleet transits JP
T+0 seconds:     Picket thermal sensors detect engine signatures (500,000 km range)
T+5 seconds:     Contact report relayed to main fleet
T+10 seconds:    Fleet commander activates sensors, confirms hostile
T+15 seconds:    Missile launch order given
T+20 seconds:    First salvo launched (30 missiles at 20,000 km/s)

Enemy closing at 4,000 km/s from 4 million km (fleet position):
T+0 to T+1000s:  Enemy crosses 4M km gap (1000 seconds = ~17 minutes)

Your missiles reach enemy (4M km away, missiles at 20,000 km/s):
Missile flight time = 4,000,000 / 20,000 = 200 seconds

T+220 seconds:   First salvo impacts enemy fleet (~3.7 minutes after launch)
T+280 seconds:   Second salvo launched (after 60s reload)
T+480 seconds:   Second salvo impacts

Enemy reaches beam range (let's say 200,000 km for your lasers):
Time for enemy to close from 4M km to 200,000 km = 3,800,000 / 4,000 = 950 seconds

T+950 seconds:   Enemy enters beam range (~16 minutes after transit)
```

**Summary:** You have approximately 3.5 minutes for your first missile impact and 16 minutes before beam combat begins. In that window, you can fire 3-4 full missile salvos before transitioning to beam combat.

### Scenario: Fast Enemy (8,000 km/s)

```
Time to cross 4M km = 4,000,000 / 8,000 = 500 seconds (~8 minutes)
Your missile flight time = 4,000,000 / 20,000 = 200 seconds (unchanged)
Time to beam range = 3,800,000 / 8,000 = 475 seconds (~8 minutes)
```

Against a fast enemy, you have only 8 minutes total and perhaps 2 missile salvos before beam engagement. This is why fleet distance from the JP must balance reaction time against the risk of fast enemy fleets.

### Scenario: Enemy Missile Salvo (Incoming at 25,000 km/s)

If the enemy launches missiles immediately after transit from 4M km:

```
Missile flight time = 4,000,000 / 25,000 = 160 seconds (~2.7 minutes)
```

Your PD layers engage during the final approach:
- AMMs launch at detection range (~27,000 km): intercept window ~1 second
- Ranged beams engage from laser range: several ticks of engagement
- CIWS engages at 10,000 km: 10,000 / 25,000 = 0.4 seconds (essentially one tick)

This is tight. Against very fast missiles, your CIWS gets only one engagement tick. Ensure your AMM and ranged beam layers carry the defensive burden.

---

## Key Decisions Summary

| Decision | Recommended | Rationale |
|----------|-------------|-----------|
| Fleet distance from JP | 3-5 million km | Balances reaction time with engagement window |
| Primary doctrine | Missile-first | Exploits enemy fire delay post-transit |
| Picket ship size | 2,000 tons | Fast enough to escape, large enough sensors to detect |
| PD layering | AMM + Laser + CIWS | No single layer handles large salvos alone |
| Jump gate at JP | DO NOT build | Ungated JP limits enemy to jump-capable ships only |
| Active sensors on pickets | OFF until contact | Prevents revealing picket positions |
| Reserve position | 200M km behind fleet | Close enough for same-day reinforcement |
| Tanker support | 2 tankers with fleet | Sustained operations require fuel logistics |

### The Jump Gate Dilemma

Building a jump gate at a hostile JP is almost always wrong:

- **With no gate:** Enemy must use jump-drive-equipped ships only. This limits their force to ships with jump drives (heavy tonnage penalty) or requires a jump tender (limiting squadron transit speed).
- **With a gate:** Any enemy ship, including fuel-inefficient beam monsters and mass missile platforms, can transit freely.
- **Exception:** If you need rapid reinforcement from deeper in your empire AND you have overwhelming local defense, a gate speeds your own logistics. But the risk usually outweighs the benefit at a hostile frontier.

---

## Common Mistakes

### 1. Stationing Fleet Directly on the JP

As detailed in Step 2, this eliminates all your defensive advantages. You become the defender who fights at the attacker's preferred range.

### 2. No Sensor Pickets

Without dedicated pickets under EMCON near the JP, you rely on your main fleet's sensors -- which means either running active sensors continuously (revealing your position) or waiting until the enemy is within passive range of your fleet (much shorter than dedicated sensor ships near the JP).

### 3. Insufficient PD Against Missile-Heavy Enemies

A common failure mode: designing a fleet with excellent offensive missiles but only 1-2 CIWS installations. The first enemy salvo of 40+ missiles overwhelms your single CIWS layer and cripples your fleet before your own missiles arrive.

**Rule of thumb:** Dedicate at least 20% of your fleet tonnage to point defense systems.

### 4. Forgetting Tanker Support

A fleet deployed at a JP 1.2 billion km from your colony without tanker support will eventually run out of fuel during maneuvering exercises or combat. Station tankers with the fleet or establish a nearby fuel depot.

### 5. Single Point of Failure

Concentrating all sensors on one picket, all PD on one escort, or all missiles on one cruiser means losing that ship destroys your entire capability in that area. Distribute capabilities across multiple hulls.

### 6. Ignoring Fire Delay

Ships suffer fire delay after jump point transit (weapons cannot fire immediately). This means an enemy arriving through the JP is temporarily helpless. Your doctrine should exploit this window with immediate missile launches.

### 7. Not Accounting for Enemy Speed

If you station your fleet at 2 million km expecting a slow enemy, but the enemy arrives at 8,000 km/s, you have only 250 seconds of reaction time. Always calculate response timelines for the fastest plausible enemy.

### 8. Building a Jump Gate on a Hostile Frontier

As discussed in the Key Decisions section, gating a hostile JP removes the natural bottleneck that limits enemy force projection through that chokepoint.

---

## Related Sections

- [Section 4.4 Jump Points](../4-systems-and-bodies/4.4-jump-points.md) -- Jump point mechanics, transit, and gates
- [Section 11.1 Thermal and EM Signatures](../11-sensors-and-detection/11.1-thermal-em-signatures.md) -- Signature mechanics and EMCON
- [Section 11.3 Active Sensors](../11-sensors-and-detection/11.3-active-sensors.md) -- Active sensor design and missile fire controls
- [Section 12.3 Missiles](../12-combat/12.3-missiles.md) -- Missile design, combat, and AMMs
- [Section 12.4 Point Defense](../12-combat/12.4-point-defense.md) -- CIWS, PD fire controls, and layered defense
- [Section 14.1 Fuel](../14-logistics/14.1-fuel.md) -- Fuel logistics for extended deployments
- [Appendix A Formulas](../appendices/A-formulas.md) -- Sensor range, combat, and movement formulas
- [Appendix C Tips and Mistakes](../appendices/C-tips-and-mistakes.md) -- General military tips and common errors
