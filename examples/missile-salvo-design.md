---
title: "Example: Designing a Missile Salvo"
parent: "Examples"
nav_order: 99
---

# Example: Designing a Missile Salvo

*Added: v2026.01.24*

This worked example walks through the complete process of designing an effective anti-ship missile (ASM), matching it with appropriate launchers and fire controls, and planning salvo composition to overwhelm enemy point defense.

## Objective

Design an effective anti-ship missile system including the missile itself, launcher, fire control, and magazine configuration. We will produce three distinct missile designs optimized for different engagement profiles, then discuss how to combine them into a coherent offensive doctrine.

## Starting Conditions

| Parameter | Value |
|-----------|-------|
| Warhead Strength Tech | 3 |
| Missile Engine MSP | 0.5 (per MSP of engine) |
| Fuel Consumption Tech | 0.3 |
| PD Hit Chance | v2.2.0+ speed ratio system (see Appendix A) |
| Available Missile Sizes | 1-6 MSP |
| Missile Fire Control Range Tech | Level 2 |

---

## Step 1: Define Engagement Parameters

Before designing a missile, establish what you are shooting at and what defenses it carries.

**Assumptions for this example:**

| Parameter | Value | Reasoning |
|-----------|-------|-----------|
| Expected target speed | 4,000 km/s | Mid-game cruiser/destroyer |
| Engagement range | 100-200 million km | Beyond beam weapon range |
| Enemy PD capability | Moderate (6x gauss, 1 CIWS) | Typical mid-game escort |
| Enemy tracking speed | 16,000 km/s | Standard CIWS-160 equivalent |
| Enemy AMM speed | ~20,000 km/s | Size-1 fast interceptors |

**Key derived requirements:**

- Missile speed must exceed 4,000 km/s (to catch the target)
- Missile speed should ideally exceed 16,000 km/s (to degrade CIWS hit probability)
- Missile range must cover the engagement distance
- Salvo size must exceed enemy PD kill rate per tick

---

## Step 2: Warhead Sizing

Warhead damage is calculated as:

```
Warhead Damage = Warhead MSP x Warhead Strength Tech
```

At Warhead Strength 3:

| Warhead MSP | Damage | Notes |
|-------------|--------|-------|
| 0.5 | 1.5 | Minimal -- only useful vs missiles |
| 1.0 | 3 | Light damage, 3x3 damage pattern |
| 1.5 | 4.5 | Moderate (4 integer armor damage) |
| 2.0 | 6 | Solid -- penetrates light armor |
| 3.0 | 9 | Heavy -- 3x3 optimal damage pattern |
| 4.0 | 12 | Devastating against most escorts |

**Note on optimal warhead sizes:** Damage is applied in a square pattern against armor. Strengths that are perfect squares (1, 4, 9, 16, 25) produce the most efficient damage patterns. At Warhead Strength tech 3:

- 3 MSP warhead = 9 damage = 3x3 square (optimal)
- 1 MSP warhead = 3 damage = 1x3 strip (acceptable)

---

## Step 3: Engine Allocation

Missile speed depends on engine allocation. *(In v2.2.0+, agility is display-only; hit chance uses the speed ratio system — see PD Survivability section below.)*

### Speed Formula

```
Missile_Speed (km/s) = Engine_Power / Missile_Size (MSP)
```

Where Engine_Power for missile engines (with our tech level):

```
Engine_Power = Engine_MSP x Power_per_MSP
Power_per_MSP = 5 (at our tech level, with missile engine power modifier of 2x base)
```

So with our tech:

```
Engine_Power = Engine_MSP x 10
Missile_Speed = (Engine_MSP x 10) / Total_Missile_MSP
```

### Point Defense Survivability (v2.2.0+)

\hyperlink{ref-ex-salvo-1}{[1]}

In v2.2.0+, point defense hit chance depends on the speed ratio between PD tracking and missile speed:

```
PD_Hit_Chance = min(1.0, FC_Tracking / Missile_Speed)
```

Faster missiles are harder for PD to intercept. There is no separate agility stat used in PD calculations.

### Speed and PD Vulnerability at Various Engine Allocations

For a **Size 4 missile** with varying engine MSP (against CIWS tracking at 16,000 km/s):

| Engine MSP | Speed (km/s) | PD Hit Chance | Remaining MSP |
|------------|-------------|---------------|---------------|
| 1.0 | 2,500 | 100% | 3.0 |
| 1.5 | 3,750 | 100% | 2.5 |
| 2.0 | 5,000 | 100% | 2.0 |
| 2.5 | 6,250 | 100% | 1.5 |
| 3.0 | 7,500 | 100% | 1.0 |

---

## Step 4: Fuel Allocation

### Fuel Capacity

Each MSP of fuel stores 2,500 units of fuel.

### Endurance and Range

```
Fuel_Consumption = Engine_Power x Fuel_Consumption_Tech
Endurance (seconds) = Total_Fuel / Fuel_Consumption_per_second
Range (km) = Speed x Endurance
```

With Fuel Consumption Tech 0.3:

```
Fuel_Consumption_per_second = Engine_Power x 0.3 / 3600
```

Example calculation for 2 MSP engine, 1 MSP fuel in a size 4 missile:

```
Engine_Power = 2.0 x 10 = 20
Speed = 20 / 4 = 5,000 km/s
Fuel = 1.0 x 2,500 = 2,500 units
Fuel_Consumption_per_hour = 20 x 0.3 = 6 units/hour
Fuel_Consumption_per_second = 6 / 3600 = 0.00167 units/sec
Endurance = 2,500 / 0.00167 = 1,497,006 seconds (~17.3 days)
Range = 5,000 x 1,497,006 = 7.49 billion km = 7,485 million km
```

**Note:** The game's missile design window calculates this automatically. The key insight is that even small fuel allocations provide enormous range at moderate speeds. Range becomes a constraint primarily for very high-speed (high-boost) missiles.

---

## Step 5: Example Design A -- "Sprint Missile"

**Design Philosophy:** Small, fast, short-range. Designed to be nearly impossible for CIWS to track. Fired from close escorts or ambush positions.

**Size:** 2 MSP

| Component | MSP | Purpose |
|-----------|-----|---------|
| Engine | 1.2 | Maximum speed |
| Warhead | 0.5 | Light damage (1.5 strength) |
| Fuel | 0.05 | Minimal range |
| Active Sensor | 0.25 | Terminal guidance (minimum viable) |
| **Total** | **2.0** | |

### Calculated Performance

```
Engine_Power = 1.2 x 10 = 12
Speed = 12 / 2 = 6,000 km/s
Agility = (1.2 / 2.0) x 3200 = 1,920 km/s^2
Warhead_Damage = 0.5 x 3 = 1.5 (fractional -- full vs shields, 1 vs armor)
Fuel = 0.05 x 2,500 = 125 units
Fuel_Consumption/hr = 12 x 0.3 = 3.6
Endurance = 125 / (3.6/3600) = 125,000 seconds
Range = 6,000 x 125,000 = 750 million km
```

### Sprint Missile Assessment

| Metric | Value | Rating |
|--------|-------|--------|
| Speed | 6,000 km/s | Excellent -- exceeds most PD tracking |
| Range | 750M km | Moderate -- sufficient for most engagements |
| Damage | 1.5 | Poor -- needs many hits to kill |
| PD vulnerability | 16k tracking: 100% hit | Vulnerable to advanced PD |
| Magazine density | ~8 per HS of magazine | High |

**Verdict:** Best used in massive salvos (40+) to overwhelm PD. Low individual damage means you need volume. The speed advantage makes each missile very likely to leak through CIWS.

---

## Step 6: Example Design B -- "Standoff Missile"

**Design Philosophy:** Balanced design with meaningful warhead, respectable speed, and sufficient range for standoff engagement. The workhorse ASM.

**Size:** 5 MSP

| Component | MSP | Purpose |
|-----------|-----|---------|
| Engine | 2.0 | Good speed without sacrificing payload |
| Warhead | 1.5 | Solid damage (4.5 strength) |
| Fuel | 0.75 | Extended range for standoff |
| Active Sensor | 0.5 | Reliable terminal guidance |
| ECM | 0.25 | Degrades enemy PD accuracy |
| **Total** | **5.0** | |

### Calculated Performance

```
Engine_Power = 2.0 x 10 = 20
Speed = 20 / 5 = 4,000 km/s
Agility = (2.0 / 5.0) x 3200 = 1,280 km/s^2
Warhead_Damage = 1.5 x 3 = 4.5 (4 vs armor)
Fuel = 0.75 x 2,500 = 1,875 units
Fuel_Consumption/hr = 20 x 0.3 = 6.0
Endurance = 1,875 / (6.0/3600) = 1,125,000 seconds
Range = 4,000 x 1,125,000 = 4,500 million km
```

### Standoff Missile Assessment

| Metric | Value | Rating |
|--------|-------|--------|
| Speed | 4,000 km/s | Adequate -- matches target speed |
| Range | 4,500M km | Excellent -- true standoff |
| Damage | 4.5 | Good -- penetrates moderate armor |
| PD vulnerability | 16k tracking: 100% hit | Speed too low to evade PD |
| ECM | Level 1 | -10% PD accuracy |
| Magazine density | ~3 per HS of magazine | Moderate |

**Verdict:** The all-rounder. Sufficient damage to threaten escorts, enough speed to catch most targets, ECM to slightly degrade PD. Best in salvos of 20-30.

**Warning:** Speed of 4,000 km/s exactly matches our assumed target speed. If the target is faster, this missile cannot catch it. Consider increasing engine allocation to 2.5 MSP (yielding 5,000 km/s) and reducing fuel to 0.5 MSP if target speed is uncertain.

---

## Step 7: Example Design C -- "Multi-Stage Missile"

**Design Philosophy:** A booster stage carries an attack missile to extended range, then separates. The attack stage sprints to the target at extreme speed. This overcomes the speed-vs-range trade-off.

### Booster Stage (Outer Missile)

**Size:** 6 MSP (total including the separated warhead)

| Component | MSP | Purpose |
|-----------|-----|---------|
| Engine | 2.0 | Cruise speed for the combined stack |
| Fuel | 1.0 | Long-range cruise |
| Separation Warhead | 3.0 | Contains the attack stage (see below) |
| **Total** | **6.0** | |

### Attack Stage (Separated Missile)

**Size:** 3 MSP (released from the booster's separation warhead)

| Component | MSP | Purpose |
|-----------|-----|---------|
| Engine | 1.5 | Sprint speed after separation |
| Warhead | 1.0 | Meaningful damage (3 strength) |
| Fuel | 0.1 | Short sprint range |
| Active Sensor | 0.25 | Terminal guidance |
| ECM | 0.15 | PD degradation |
| **Total** | **3.0** | |

### Combined Performance

**Cruise Phase (booster active):**
```
Combined_Mass = 6 MSP
Booster_Engine_Power = 2.0 x 10 = 20
Cruise_Speed = 20 / 6 = 3,333 km/s
Cruise_Fuel = 1.0 x 2,500 = 2,500 units
Cruise_Consumption/hr = 20 x 0.3 = 6.0
Cruise_Endurance = 2,500 / (6.0/3600) = 1,500,000 sec
Cruise_Range = 3,333 x 1,500,000 = 5,000 million km
```

**Sprint Phase (attack stage only):**
```
Attack_Mass = 3 MSP
Attack_Engine_Power = 1.5 x 10 = 15
Sprint_Speed = 15 / 3 = 5,000 km/s
Sprint_Agility = (1.5 / 3.0) x 3200 = 1,600 km/s^2
Sprint_Fuel = 0.1 x 2,500 = 250 units
Sprint_Consumption/hr = 15 x 0.3 = 4.5
Sprint_Endurance = 250 / (4.5/3600) = 200,000 sec
Sprint_Range = 5,000 x 200,000 = 1,000 million km
Warhead_Damage = 1.0 x 3 = 3
```

### Multi-Stage Assessment

| Phase | Speed | Range | Damage |
|-------|-------|-------|--------|
| Cruise | 3,333 km/s | 5,000M km | -- |
| Sprint | 5,000 km/s | 1,000M km | 3 |
| **Effective** | **Combined** | **~6,000M km** | **3** |

**Verdict:** Best of both worlds -- extreme range AND high terminal speed. The downside is complexity: you need size-6 launchers, the booster is wasted mass after separation, and the warhead is only moderate. Best when you need to engage targets beyond normal missile range or when you want the speed advantage of sprinters with the reach of standoff missiles.

---

## Step 8: Fire Control Matching

The missile fire control (MFC) must cover the missile's maximum engagement range and have resolution appropriate to the target size.

### Fire Control Range Formula

```
MFC_Range (km) = FC_Size (HS) x Resolution x FC_Range_Tech x 10,000
```

### Critical Rule: FC Range Must Exceed Missile Range

If a missile flies beyond its fire control's maximum range, it loses guidance and goes ballistic. This is the most common mistake in missile ship design.

### Fire Control Design for Each Missile

| Missile | Max Range | Required FC Range | FC Design |
|---------|-----------|-------------------|-----------|
| Sprint (A) | 750M km | 750M+ km | 1 HS, Res 120, Tech 2 = 2,400M km |
| Standoff (B) | 4,500M km | 4,500M+ km | 1 HS, Res 120, Tech 2 = 2,400M km (INSUFFICIENT!) |
| Multi-Stage (C) | 6,000M km | 6,000M+ km | 1 HS, Res 120, Tech 2 = 2,400M km (INSUFFICIENT!) |

**Problem identified:** Our FC tech only provides 2,400M km range at resolution 120. For the Standoff and Multi-Stage missiles, we have two options:

1. **Reduce missile range** to match FC range (reduce fuel)
2. **Add onboard active sensors** so missiles can guide themselves beyond FC range
3. **Research better FC tech** before deploying these designs

For this example, we equip Designs B and C with onboard sensors (already included in their designs). The missile acquires the target independently once beyond FC range.

### Resolution Matching

| Target Type | Approx Tonnage | Resolution Needed |
|-------------|---------------|-------------------|
| Destroyer | 5,000-8,000 t | 100-160 |
| Cruiser | 10,000-15,000 t | 200-300 |
| Capital ship | 20,000+ t | 400+ |

Higher resolution = longer range against larger targets. For general-purpose use, resolution 120 (6,000 tons) is a good compromise for mid-game.

---

## Step 9: Launcher Sizing

### Launcher-to-Missile Matching

The launcher size must equal or exceed the missile size. Using exact-size launchers is most efficient.

| Missile | Size (MSP) | Launcher Size | Launcher HS |
|---------|-----------|---------------|-------------|
| Sprint (A) | 2 | Size 2 | 0.67 HS |
| Standoff (B) | 5 | Size 5 | 1.67 HS |
| Multi-Stage (C) | 6 | Size 6 | 2.0 HS |

### Reload Time Calculation

```
Reload Time = (SQRT(missile_size) x 30 seconds) / Reload_Rate_Tech
```

Assuming Reload Rate Tech = 2:

| Missile | Size | SQRT(Size) | Base Reload | With Tech 2 |
|---------|------|-----------|-------------|--------------|
| Sprint (A) | 2 | 1.41 | 42.4 sec | 21.2 sec |
| Standoff (B) | 5 | 2.24 | 67.1 sec | 33.5 sec |
| Multi-Stage (C) | 6 | 2.45 | 73.5 sec | 36.7 sec |

### Reduced-Size Launcher Option

If hull space is constrained, reduced-size launchers trade reload speed for compactness:

| Size Multiplier | Sprint Reload | Standoff Reload | Multi-Stage Reload |
|-----------------|--------------|-----------------|-------------------|
| 1.0x (standard) | 21.2 sec | 33.5 sec | 36.7 sec |
| 0.75x | 63.6 sec | 100.5 sec | 110.3 sec |
| 0.5x | 212 sec | 335 sec | 367 sec |
| 0.15x (box) | Single fire | Single fire | Single fire |

---

## Step 10: Magazine Logistics

### Magazine Capacity

```
Magazine_Size (MSP) = Magazine_HS x ~17-18 MSP_per_HS
Missiles_Stored = Magazine_MSP / Missile_MSP
```
\hyperlink{ref-ex-salvo-2}{[2]}

For a standard 5 HS magazine (~87 MSP capacity):

| Missile | Size (MSP) | Per Magazine | Per 2 Magazines |
|---------|-----------|-------------|-----------------|
| Sprint (A) | 2 | 43 | 86 |
| Standoff (B) | 5 | 17 | 34 |
| Multi-Stage (C) | 6 | 14 | 28 |

### Salvo Size Planning

A ship with 8 launchers fires 8 missiles per salvo. Magazine capacity determines sustained combat:

```
Number_of_Salvos = Missiles_in_Magazine / Launchers
Time_Between_Salvos = Reload_Time (from Step 9)
Total_Combat_Duration = Number_of_Salvos x Time_Between_Salvos
```

**Example: 8x Size-5 launchers, 2x 5HS magazines (40 Standoff missiles):**
```
Salvos = 40 / 8 = 5 full salvos
Time between = 33.5 seconds
Total sustained fire = 5 x 33.5 = 167.5 seconds (~2.8 minutes)
Total damage potential = 40 missiles x 4.5 damage = 180 damage
```

### Magazine Explosion Risk

Magazines are vulnerable. If hit, all stored missiles may detonate:

```
Explosion_Damage = Sum(All_Warhead_Strengths_in_Magazine)
```

For 20 Standoff missiles in one magazine:
```
Explosion = 20 x 4.5 = 90 internal damage
```

This will destroy most ships from the inside. Mitigation:

- Spread missiles across multiple smaller magazines
- Accept the risk on dedicated missile ships (keep them at range)
- Research magazine explosion reduction technology

---

## Step 11: Salvo Composition

### Overwhelming PD Through Volume

From our assumptions, the enemy has:

- 1 CIWS (6 shots/tick at ~50% hit rate vs 4,000 km/s missiles = ~3 kills/tick)
- 6 gauss cannons in PD mode (~4 kills/tick combined)
- Total PD capacity: ~7 missiles per 5-second tick

**Minimum effective salvo = PD kills per tick + desired hits**

To guarantee 10 hits: 7 + 10 = 17 missiles minimum per salvo.

### Mixed Salvo Doctrine

Combine missile types to exploit PD weaknesses:

**"Saturation Strike" composition (28 missiles):**

| Type | Count | Purpose |
|------|-------|---------|
| Sprint (A) | 16 | Arrive first, absorb PD fire, some leak through |
| Standoff (B) | 12 | Arrive behind sprints, deliver killing blows |

**Timing:** Launch sprints first. Their higher speed means they arrive before standoff missiles. PD engages the sprint salvo, potentially exhausting CIWS ammunition and AMMs. Standoff missiles arrive into weakened defenses.

**"Decoy Swarm" alternative:**

Design a dedicated decoy missile (size 2, no warhead, maximum speed, ECM):

| Component | MSP | Purpose |
|-----------|-----|---------|
| Engine | 1.5 | Maximum speed |
| ECM | 0.25 | Degrades PD tracking |
| Fuel | 0.25 | Sufficient range |
| **Total** | **2.0** | |

Mix 20 decoys with 12 Standoff missiles. PD must engage every contact (it cannot distinguish decoys from real threats until impact). The decoys absorb PD capacity while real missiles close.

---

## Key Decisions Summary

| Decision | Trade-off | Recommendation |
|----------|-----------|----------------|
| Speed vs. Warhead | Fast missiles leak PD but deal less damage | Prioritize speed if enemy PD is strong |
| Single vs. Multi-stage | Multi-stage has range+speed but lower payload | Use multi-stage for long-range engagements |
| Launchers vs. Magazine depth | More launchers = bigger salvos; more magazines = more salvos | Balance based on expected engagement count |
| FC range vs. Missile range | FC must cover missile range or missile needs onboard sensor | Always verify FC range covers engagement distance |
| ECM vs. Payload | ECM costs 0.25 MSP but reduces PD effectiveness | Include ECM on all missiles size 4+ |
| Standard vs. Box launchers | Standard = sustained fire; Box = devastating alpha | Box launchers on corvettes/FACs; standard on cruisers |

---

## Common Mistakes

1. **Missile range exceeds FC range (no onboard sensor):** The missile loses guidance and goes ballistic. Always check that your MFC range covers the missile's maximum engagement distance, OR equip missiles with onboard active sensors.

2. **Speed too low for PD evasion:** In v2.2.0+, PD hit chance is based on the speed ratio (FC_Tracking / Missile_Speed). If your missile speed is below the enemy's tracking speed, PD has 100% base hit chance. Faster missiles are harder to intercept.

3. **Ignoring reload time:** Your first salvo is impressive, but if reload takes 100+ seconds and the enemy is closing, you may only get one shot. Size launchers and magazines for the engagement duration.

4. **Magazine explosion risk ignored:** A single armor-penetrating hit to an unprotected magazine can detonate your entire missile loadout, destroying your ship from within. Spread ordnance across multiple magazines.

5. **Missile speed too low:** If your missile speed equals the target speed, the missile can technically never catch a target fleeing directly away. Build at least 25% speed margin over expected target speed.

6. **Over-investing in warhead, under-investing in speed:** A missile with a massive warhead that gets intercepted by every CIWS does zero damage. Speed is survivability.

7. **No onboard sensors on long-range missiles:** If the target uses ECM or your FC is jammed, missiles without sensors are wasted. Include at least 0.25 MSP active sensor on ASMs.

8. **Identical time-on-target for all missiles:** If all missiles arrive simultaneously, PD engages them all at once. Stagger launch times or use speed differentials to create sequential arrival waves.

---

## References

\hypertarget{ref-ex-salvo-1}{[1]}. Aurora C# v2.2.0+ missile mechanics: Point defense hit chance uses speed ratio: PD_Hit_Chance = min(1.0, FC_Tracking / Missile_Speed). Agility is no longer used in PD calculations. See Appendix A for the complete formula.

\hypertarget{ref-ex-salvo-2}{[2]}. Aurora C# game database (AuroraDB.db v2.7.1) -- Magazine capacity is approximately 17-18 MSP per hull space. Verified against multiple magazine component entries in the database.

---

## Related Sections

- [Section 8.5 Weapons](../8-ship-design/8.5-weapons.md) -- Missile launcher types, box launchers, reduced-size options
- [Section 12.3 Missiles](../12-combat/12.3-missiles.md) -- Missile design parameters, ECM, decoys, multi-stage separation
- [Section 12.4 Point Defense](../12-combat/12.4-point-defense.md) -- Understanding what your missiles face (CIWS, AMMs, layered defense)
- [Appendix A: Formulas](../appendices/A-formulas.md) -- Missile speed, range, and fire control range calculations
- [Appendix D: Reference Tables](../appendices/D-reference-tables.md) -- Magazine capacity, launcher sizes, unit conversions
