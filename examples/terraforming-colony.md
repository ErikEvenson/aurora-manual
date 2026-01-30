---
title: "Example: Terraforming a Colony"
parent: "Examples"
nav_order: 99
---

# Example: Terraforming a Colony

*Updated: v2026.01.30*

This worked example walks through reducing a colony's cost from CC 2.0 to CC 0.0 through systematic terraforming. Each step includes timeline calculations, installation requirements, and the decision logic behind gas selection order.

## Quick Reference: Atmospheric Values

*Updated: v2026.01.30*

Before diving into the worked example, here are the key numerical values you need for terraforming calculations.

### Breathable Atmosphere Targets (Human Baseline)

| Gas | Minimum | Target | Maximum | Notes |
|-----|---------|--------|---------|-------|
| Oxygen (O2) | 0.10 atm | 0.21 atm | 0.30 atm | Also max 30% of total atmosphere |
| Nitrogen (N2) | -- | 0.78 atm | 3.00 atm | Primary filler gas; safe at any reasonable level |
| Total Pressure | 0.70 atm | 1.00 atm | 1.50 atm | Species tolerance range |
| Temperature | 0C | 15-20C | 35C | Human habitable range |
| Hydrosphere | 20% | 50-70% | 75% | Above 75% reduces land area |

### Dangerous Gas Thresholds (Must Be Below)

| Gas | Danger Threshold | CC Penalty | Removal Priority |
|-----|------------------|------------|------------------|
| Chlorine (Cl2) | 0.000001 atm (1 ppm) | +3.0 | Highest |
| Nitrogen Oxides (NO/NO2) | 0.000005 atm (5 ppm) | +2.0 | Very High |
| Ammonia (NH3) | 0.00005 atm (50 ppm) | +2.0 | High |
| Methane (CH4) | 0.0005 atm (500 ppm) | +2.0 | High |
| Carbon Dioxide (CO2) | 0.005 atm (5,000 ppm) | +2.0 | Medium |

### Terraforming Installation Rates

| Technology Level | Research Cost | Rate (atm/year/inst) |
|------------------|---------------|----------------------|
| Starting (Racial) | -- | 0.00025 |
| Level 1 | 3,000 RP | 0.00032 |
| Level 2 | 6,000 RP | 0.00040 |
| Level 3 | 12,000 RP | 0.00050 |
| Level 4 | 24,000 RP | 0.00065 |
| Level 5 | 48,000 RP | 0.00080 |
| Level 6 | 96,000 RP | 0.00100 |
| Level 7 | 192,000 RP | 0.00120 |

> **Note:** Actual rate is multiplied by the planet size factor: Earth Surface Area / Planet Surface Area. Smaller worlds terraform faster.

### Installation Requirements by Project Scale

| Gas Change Needed | Installations (Base Tech) | Timeline (0.35 Earth SA) |
|-------------------|---------------------------|--------------------------|
| 0.01 atm | 10-20 | 0.5-1.0 years |
| 0.05 atm | 20-30 | 2.3-3.5 years |
| 0.10 atm | 30-50 | 2.8-4.7 years |
| 0.20 atm | 50-70 | 4.0-5.6 years |
| 0.50 atm | 70-100 | 7.0-10.0 years |
| 1.00 atm | 100-150 | 9.3-14.0 years |

---

## Objective

*Updated: v2026.01.30*

Transform a Mars-like colony world from Colony Cost 2.0 to Colony Cost 0.0 (fully habitable) through atmospheric terraforming, making it suitable for unassisted human habitation.

## Starting Conditions

*Updated: v2026.01.30*

- **World type:** Mars-like rocky planet
- **Planet size:** 0.53 Earth masses, surface area approximately 28% of Earth
- **Surface gravity:** 0.38g (below species minimum -- contributes CC 1.0 from gravity, but this is separate from atmospheric terraforming and cannot be changed)
- **Base temperature:** -60C (very cold, well below the 0-35C habitable range)
- **Atmosphere:** Thin CO2 atmosphere at 0.006 atm total pressure (essentially vacuum for breathing purposes)
- **Atmospheric composition:** 95% CO2 (0.0057 atm), trace N2, trace Ar
- **Hydrosphere:** 0% (no surface water)
- **Colony Cost breakdown:**
  - Temperature factor: 3.43 (60C below habitable minimum of 0C; calculated as 60 / 17.5 = 3.43)
  - Breathable gas factor: 2.0 (no breathable oxygen)
  - Dangerous gas factor: 2.0 (CO2 exceeds 5,000 ppm threshold)
  - Hydrosphere factor: 2.0 (0% water, penalty = (20-0)/10 = 2.0)
  - Gravity factor: 1.0 (below species minimum)
  - **Final CC: 3.43** (only the single highest factor applies in C# Aurora)

**Wait -- the starting CC is higher than 2.0!**

This is an important lesson. Our Mars-like world actually has CC 3.43 due to temperature. The user's stated goal of "CC 2.0 to CC 0.0" represents a world where the worst factor is the breathable gas / dangerous gas penalty of 2.0. Let us adjust our starting conditions to match the stated scenario.

### Revised Starting Conditions (CC 2.0 World)

- **World type:** Rocky planet with partial atmosphere
- **Planet size:** 0.4 Earth masses, surface area ~35% of Earth
- **Surface gravity:** 0.55g (within habitable range -- no gravity penalty)
- **Base temperature:** -10C (cold, but only 10C below the 0C habitable minimum)
- **Atmosphere:** 0.3 atm total pressure, primarily N2 with toxic CO2
- **Atmospheric composition:**
  - N2: 0.28 atm (safe filler gas)
  - CO2: 0.015 atm (well above the 0.005 atm danger threshold)
  - O2: 0.005 atm (far below the 0.1 atm minimum for breathability)
- **Hydrosphere:** 5% (low, contributing CC factor of (20-5)/10 = 1.5)
- **Colony Cost breakdown:**
  - Temperature factor: 0.57 (10C below minimum; 10/17.5 = 0.57)
  - Breathable gas factor: 2.0 (O2 below 0.1 atm)
  - Dangerous gas factor: 2.0 (CO2 above 0.005 atm)
  - Hydrosphere factor: 1.5 (5% water)
  - Gravity factor: 0.0 (within tolerance)
  - **Final CC: 2.0** (worst single factor: breathable gas OR dangerous gas, both at 2.0)
- **Terraforming technology:** Base level (0.00025 atm/year per installation)
- **Planet size modifier:** Earth Surface Area / Planet Surface Area = 1/0.35 = 2.86x speed bonus

---

## Step 1: Analyze Atmosphere

*Updated: v2026.01.30*

### Current State Assessment

```
Current Atmosphere (0.3 atm total):
  N2:  0.28 atm  (93.3%)  -- SAFE, no action needed
  CO2: 0.015 atm (5.0%)   -- DANGEROUS (above 0.005 atm threshold)
  O2:  0.005 atm (1.7%)   -- INSUFFICIENT (need 0.1-0.3 atm)

Colony Cost Factors:
  Temperature:     0.57 (10C below habitable; need warming)
  Breathable gas:  2.00 (O2 too low; need 0.1+ atm)
  Dangerous gas:   2.00 (CO2 too high; need below 0.005 atm)
  Hydrosphere:     1.50 (5% water; need 20%+)
  Gravity:         0.00 (within tolerance)

  WORST FACTOR = 2.00 (current Colony Cost)
```

### Problems to Solve (in Priority Order)

1. **CO2 removal:** Reduce from 0.015 atm to below 0.005 atm (removes CC 2.0 dangerous gas factor)
2. **O2 addition:** Increase from 0.005 atm to at least 0.1 atm (removes CC 2.0 breathable gas factor)
3. **Temperature increase:** Warm from -10C to at least 0C (removes CC 0.57 temperature factor)
4. **Hydrosphere increase:** Raise from 5% to 20%+ (removes CC 1.5 hydrosphere factor)

---

## Step 2: Calculate Target Atmosphere

*Updated: v2026.01.30*

### Ideal Final Atmosphere

For zero colony cost from atmospheric factors, target:

```
Target Atmosphere (~1.0 atm total):
  N2:  0.78 atm  (78%)    -- Primary filler gas
  O2:  0.21 atm  (21%)    -- Breathable range (0.1-0.3 atm, max 30% of total)
  CO2: 0.0003 atm (0.03%) -- Below danger threshold, slight greenhouse benefit
  H2O: 0.01 atm  (1%)     -- Humidity, contributes to hydrosphere

Required Changes from Current:
  N2:  Need +0.50 atm (from 0.28 to 0.78)
  O2:  Need +0.205 atm (from 0.005 to 0.21)
  CO2: Need -0.0147 atm (from 0.015 to 0.0003)
  H2O: Need +0.01 atm (from 0 to 0.01)

Total gas to ADD:    0.715 atm
Total gas to REMOVE: 0.0147 atm
```

### Temperature Calculation

Using the surface temperature formula from [Section 5.5 Terraforming](../5-colonies/5.5-terraforming.md):

```
Surface Temp (K) = Base Temp (K) * Greenhouse Factor / Anti-Greenhouse Factor * Albedo
```

Current state:

- Base Temp: 263K (-10C) determined by stellar distance
- Current Greenhouse Factor: 1 + (0.3/10) + 0.015 = 1.045
- Anti-Greenhouse Factor: 1.0 (no anti-greenhouse gases)
- Surface Temp = 263 * 1.045 = 274.8K (1.8C... wait, this conflicts with our stated -10C)

Let us set the base temperature so that current conditions produce -10C:

- Need: Base_Temp * Greenhouse_Factor = 263K (-10C)
- With GF = 1.045: Base_Temp = 263 / 1.045 = 251.7K (-21.3C)

After terraforming to target atmosphere:

- New Greenhouse Factor: 1 + (1.0/10) + 0.0003 + 0.01 = 1.1103
- New Surface Temp = 251.7 * 1.1103 = 279.4K (6.4C) -- within habitable range!

The increased atmospheric pressure and trace greenhouse gases naturally warm the planet to habitable levels. No dedicated greenhouse gas campaign is needed.

---

## Step 3: Deploy Terraforming Installations

*Updated: v2026.01.30*

### Rate Calculation

Base terraforming rate with planet size modifier:

```
Effective Rate = Base_Rate * Planet_Size_Modifier
               = 0.00025 atm/year/installation * 2.86
               = 0.000715 atm/year/installation
```

Each installation changes atmosphere by 0.000715 atm per year on this world (smaller than Earth, so faster terraforming).

### Installation Requirements by Phase

**Phase 1: Remove CO2 (highest priority -- removes CC 2.0)**

```
CO2 to remove: 0.015 - 0.005 = 0.010 atm (to drop below danger threshold)
               0.015 - 0.0003 = 0.0147 atm (to reach target)

With 20 installations removing CO2:
Rate = 20 * 0.000715 = 0.0143 atm/year

Time to clear danger threshold: 0.010 / 0.0143 = 0.70 years (~8.4 months)
Time to reach target: 0.0147 / 0.0143 = 1.03 years (~12.3 months)
```

CO2 removal is relatively quick because only a small amount needs to be removed, even at the slower C# rate.

**Phase 2: Add O2 (removes CC 2.0 breathable gas factor)**

```
O2 to add: 0.21 - 0.005 = 0.205 atm

With 50 installations adding O2:
Rate = 50 * 0.000715 = 0.03575 atm/year

Time to reach breathable minimum (0.1 atm): (0.1 - 0.005) / 0.03575 = 2.66 years
Time to reach target (0.21 atm): 0.205 / 0.03575 = 5.73 years
```

**Phase 3: Add N2 (builds atmospheric pressure for greenhouse warming)**

```
N2 to add: 0.78 - 0.28 = 0.50 atm

With 50 installations adding N2:
Rate = 50 * 0.000715 = 0.03575 atm/year

Time to reach target: 0.50 / 0.03575 = 13.99 years
```

**Phase 4: Add H2O vapor (builds hydrosphere)**

```
H2O to add: 0.01 atm (plus natural condensation builds hydrosphere)

With 10 installations adding H2O:
Rate = 10 * 0.000715 = 0.00715 atm/year

Time to add 0.01 atm: 0.01 / 0.00715 = 1.40 years (~16.8 months)
```

Note: Water vapor condenses at 0.1 atm per year, increasing Hydro Extent. As water vapor is added, some will condense into surface water, gradually raising hydrosphere percentage. Each year of active water vapor addition at equilibrium adds approximately 4% hydro extent.

To raise hydrosphere from 5% to 20%: need +15%, which requires approximately 3.75 years of water vapor addition and condensation.

---

## Step 4: Gas Selection Strategy

*Updated: v2026.01.30*

### Why This Order Matters

The order of gas manipulation is critical. Getting it wrong can increase colony cost instead of decreasing it.

### Phase Sequencing

```
Phase 1 (Months 1-3):   Remove CO2       [20 installations]
Phase 2 (Months 1-20):  Add N2            [50 installations]  (runs parallel)
Phase 3 (Months 4-21):  Add O2            [50 installations]  (starts after CO2 clear)
Phase 4 (Months 1-48):  Add H2O           [10 installations]  (runs parallel)

Total installations needed: 130 (peak, during parallel operations)
Total timeline: ~10-11 years to CC 0.0 (see detailed Timeline Summary below)
```

### Why Remove CO2 Before Adding O2

Adding oxygen to an atmosphere with high CO2 is not dangerous in the explosive sense (unlike O2 + methane), but it is wasteful. The CO2 danger threshold is at 0.005 atm. If you add O2 first, the breathable gas CC factor disappears once O2 reaches 0.1 atm, but the dangerous gas CC factor remains at 2.0 until CO2 drops below 0.005 atm. Removing CO2 first eliminates the dominant CC factor fastest.

### Why Add N2 in Parallel

Nitrogen is an inert filler gas. Adding it:

- Increases total atmospheric pressure (mild greenhouse warming from the pressure term)
- Dilutes remaining CO2 concentration (though the game uses partial pressure, not concentration)
- Is safe at any quantity within reason
- Can run simultaneously with CO2 removal using separate installations

### Why O2 Goes Last Among Major Gases

Oxygen addition should begin only after toxic/dangerous gases are removed:

- In this case, CO2 is the only dangerous gas and is removed quickly
- O2 addition can safely start after ~year 1 (once CO2 clears danger threshold)
- If the atmosphere contained methane or hydrogen, O2 would need to wait until those are cleared (explosive combinations)

### Temperature Interaction

As we add N2 and increase total pressure from 0.3 atm to 1.0 atm:

```
Greenhouse Factor progression:
  At 0.3 atm: GF = 1 + (0.3/10) + CO2 = 1.030 (after CO2 removal)
  At 0.5 atm: GF = 1 + (0.5/10) = 1.050
  At 0.7 atm: GF = 1 + (0.7/10) = 1.070
  At 1.0 atm: GF = 1 + (1.0/10) + 0.0003 + 0.01 = 1.110

Temperature progression:
  At 0.3 atm: T = 251.7 * 1.030 = 259.3K (-13.7C) -- slightly cooler without CO2!
  At 0.5 atm: T = 251.7 * 1.050 = 264.3K (-8.7C)
  At 0.7 atm: T = 251.7 * 1.070 = 269.3K (-3.7C)
  At 1.0 atm: T = 251.7 * 1.110 = 279.4K (6.4C)  -- habitable!
```

The temperature CC factor disappears naturally as pressure builds. No dedicated greenhouse gas campaign is needed for this world because the pressure-driven greenhouse effect is sufficient.

**Important caveat:** If the base temperature were much lower (e.g., -60C base), pressure alone would not be enough, and dedicated greenhouse gases (CO2 kept at safe levels, or temporary methane) would be required.

---

## Step 5: Monitor Colony Cost Reduction

*Updated: v2026.01.30*

### CC Progression Timeline

Track how colony cost changes as terraforming proceeds (all phases running concurrently where possible):

```
Year 0 (Start):
  Worst factor: Breathable gas = 2.0, Dangerous gas = 2.0
  CC = 2.0

Year 0.7 (CO2 below danger threshold):
  Dangerous gas factor eliminated (CO2 < 0.005 atm)
  Remaining worst: Breathable gas = 2.0 (O2 still below 0.1 atm)
  CC = 2.0 (unchanged -- breathable gas still dominates)

Year 1-2 (O2 building, N2 building):
  O2 rising from 0.005 toward 0.1 atm
  Breathable gas factor: still 2.0 until O2 >= 0.1 atm
  CC = 2.0

Year 2.7 (O2 reaches 0.1 atm):
  Breathable gas factor ELIMINATED
  Remaining worst: Hydrosphere = 1.5 (still at ~9% water, improved from 5%)
  CC = 1.5 (significant improvement!)

Year 5 (Pressure rising, hydro improving):
  Temperature: -5C, factor = 5/17.5 = 0.29
  Hydrosphere: ~12%, factor = (20-12)/10 = 0.8
  CC = 0.8

Year 7 (Pressure at 0.6 atm, hydro at 15%):
  Temperature: -6C, factor = 6/17.5 = 0.34
  Hydrosphere: 15%, factor = (20-15)/10 = 0.5
  CC = 0.5

Year 10 (Near target atmosphere):
  Temperature: 2C (within range), factor = 0.0
  Hydrosphere: 18%, factor = (20-18)/10 = 0.2
  CC = 0.2

Year 14 (Target achieved):
  Temperature: 6.4C, factor = 0.0
  O2: 0.21 atm, within range, factor = 0.0
  CO2: trace, factor = 0.0
  Hydrosphere: 20%+, factor = 0.0
  CC = 0.0!
```

### Key Milestones

| Year | Event | CC |
|------|-------|-----|
| 0 | Terraforming begins | 2.0 |
| 0.7 | CO2 below danger threshold | 2.0 |
| 2.7 | O2 reaches breathable minimum | 1.5 |
| 5 | Hydrosphere improving | 0.8 |
| 10 | Temperature enters habitable range | 0.2 |
| 14 | All factors eliminated | 0.0 |

---

## Step 6: Infrastructure Requirements

*Updated: v2026.01.30*

### Supporting Population During Terraforming

While CC > 0, the colony requires infrastructure to support population:

```
Required Infrastructure = Population * Colony_Cost
```

**Example at CC 2.0 with 10 million population:**

```
Required Infrastructure = 10,000,000 * 2.0 = 20,000,000 units
```

Each infrastructure unit supports one person at CC 1.0. At CC 2.0, you need 2 units per person.

### Infrastructure Logistics

- **Infrastructure weight:** Each unit is a standard cargo item transported by freighters
- **Production:** Infrastructure can be built by Conventional Industry (no TN minerals required!)
- **Tip:** Use Conventional Industry to produce infrastructure cheaply while your TN factories build terraforming installations

### Population Strategy During Terraforming

**Option A: Minimal population during terraforming**

- Station only essential workers (125,000 per ground-based terraforming installation) \hyperlink{ref-ex-terraform-1}{[1]}
- 130 installations * 125,000 = 16.25 million workers needed
- Infrastructure needed: 16,250,000 * 2.0 = 32,500,000 units
- Advantage: Less infrastructure investment
- Disadvantage: No economic output from the colony during terraforming

**Option B: Full colonization during terraforming**

- Import population for mining, industry, and research alongside terraforming
- Higher infrastructure investment but colony becomes productive immediately
- As CC decreases, infrastructure requirements drop automatically
- At CC 1.5 (year 2.7): 32.5M pop needs only 48.75M infrastructure (saved 16.25M!)

**Recommendation:** Use Option A for pure terraforming targets. Use Option B if the world has valuable mineral deposits that justify early economic development.

### Worker Requirement Note

Ground-based terraforming installations each require 125,000 workers:

```
130 installations * 125,000 workers = 16.25 million population minimum
```

An alternative is space-based terraforming modules (ship components with no population requirement), but these cost 500 BP each and require ship construction infrastructure.

---

## Step 7: Temperature Management

*Updated: v2026.01.30*

### Greenhouse Effect Calculations

Our world benefits from a natural warming effect as atmospheric pressure increases. Here is the detailed progression:

```
Surface Temperature Formula:
  Surface Temp (K) = Base Temp * Greenhouse Factor / Anti-Greenhouse Factor

Base Temperature: 251.7K (-21.3C) -- determined by stellar distance

Greenhouse Factor = 1 + (Atmospheric Pressure / 10) + Greenhouse Gas Pressure
Anti-Greenhouse Factor = 1.0 (no anti-greenhouse gases present)
```

**Temperature at Key Pressure Points:**

| Total Pressure (atm) | GH Factor | Surface Temp (K) | Surface Temp (C) | CC Factor |
|---|---|---|---|---|
| 0.30 (start) | 1.045 | 263.0 | -10.0 | 0.57 |
| 0.30 (CO2 removed) | 1.030 | 259.3 | -13.7 | 0.78 |
| 0.50 | 1.050 | 264.3 | -8.7 | 0.50 |
| 0.70 | 1.070 | 269.3 | -3.7 | 0.21 |
| 0.85 | 1.085 | 273.1 | 0.1 | 0.00 |
| 1.00 (target) | 1.110 | 279.4 | 6.4 | 0.00 |

**Observation:** Temperature enters the habitable range (0C+) at approximately 0.85 atm total pressure. Since we are adding N2 at 0.03575 atm/year (50 installations), we cross this threshold at approximately:

```
Time to reach 0.85 atm from 0.30 atm = (0.85 - 0.30) / 0.03575 = 15.38 years
```

However, the temperature CC factor is only 0.57 at best, which is never the dominant CC factor in our scenario. The atmosphere composition factors (2.0) dominate until year 2.7 (when O2 reaches breathable minimum). After that, hydrosphere dominates. Temperature becomes relevant only after hydrosphere is fixed.

### When You DO Need Dedicated Greenhouse Warming

If your world had a base temperature of 200K (-73C), even at 1.0 atm total pressure:

```
Max Greenhouse Factor: 3.0 (cap)
Max Surface Temp: 200 * 3.0 = 600K -- this EXCEEDS habitable range!

But realistically, at 1.0 atm with trace CO2 and water vapor:
GF = 1 + (1.0/10) + 0.01 = 1.11
Surface Temp = 200 * 1.11 = 222K (-51C) -- still frozen!
```

In this case, you WOULD need dedicated greenhouse gases:

- Add CO2 up to 0.004 atm (just below danger threshold) for greenhouse warming
- Add CH4 temporarily for stronger warming (then remove before adding O2)
- Target a Greenhouse Factor high enough to reach 273K (0C)

```
Required GF for 0C: 273 / 200 = 1.365
Need: (1.365 - 1 - 0.1) = 0.265 atm of greenhouse gas pressure
This is achievable with CO2 at 0.004 atm + additional warming from water vapor
```

If even maximum greenhouse cannot reach habitable temperature, the world is impractical to terraform through atmospheric means alone.

### Anti-Greenhouse Gases (For Hot Worlds)

If your world is TOO hot, anti-greenhouse gases cool it:

```
Anti-GH Factor = 1 + Anti-Greenhouse Gas Pressure
Max Anti-GH Factor: 3.0 (divides temperature by up to 3)
```

A 400K world with Anti-GH Factor 1.5 becomes 400/1.5 = 267K (-6C). This is one approach for cooling Venus-type worlds.

---

## Step 8: Completion Criteria

*Updated: v2026.01.30*

### When to Stop Terraforming

Terraforming is complete when all atmospheric CC factors reach 0.0:

```
Completion Checklist:
  [x] O2 partial pressure: 0.1-0.3 atm AND <= 30% of total atmosphere
  [x] CO2 below 0.005 atm (danger threshold)
  [x] No other dangerous gases above their thresholds
  [x] Total pressure within species tolerance (0.7-1.5 atm for humans)
  [x] Surface temperature within 0-35C range
  [x] Hydrosphere >= 20%
```

### Overshoot Prevention

Watch for these overshoot conditions:

- **O2 above 0.3 atm:** Becomes toxic. Stop O2 addition well before this point.
- **O2 above 30% of total atmosphere:** Also triggers breathable gas penalty. At 1.0 atm total, cap O2 at 0.30 atm maximum.
- **Temperature above 35C:** If greenhouse warming overshoots, you need to remove greenhouse gases or add anti-greenhouse gases.
- **Pressure above species tolerance:** If total pressure exceeds maximum (1.5 atm for humans), colony cost increases. Stop adding gas before this point.

### Redeploying Installations

Once terraforming is complete:

1. **Remove installations** from the completed world
2. **Transport** to your next terraforming target (each installation is 50,000 tons -- you need significant freighter capacity)
3. **Reassign** to the next priority gas operation at the new target
4. **Alternative:** Convert some to space-based modules for flexibility

A set of 130 installations represents a major investment. Do not leave them idle on a completed world.

### Maintenance Mode

After achieving CC 0.0, the atmosphere is stable. No ongoing terraforming is needed to maintain conditions unless:

- Volcanic activity adds gases (rare game event)
- An asteroid impact introduces dust (anti-greenhouse cooling)
- You deliberately modify the atmosphere for another species

---

## Timeline Summary

*Updated: v2026.01.30*

### Complete Terraforming Schedule (130 Installations, Base Technology)

```
Year 1:
  Remove CO2 (20 inst.) + Add N2 (50 inst.) + Add O2 (50 inst.) + Add H2O (10 inst.)
  CO2 drops below danger threshold by ~month 8
  Switch 20 CO2-removal inst. to O2 addition (now 70 on O2)

Years 2-3:
  O2 approaching breathable minimum (0.1 atm)
  N2 slowly building pressure
  Hydrosphere building via H2O condensation

Year 3 (O2 reaches 0.1 atm):
  CC drops from 2.0 to 1.5 (hydrosphere now dominant factor)
  H2O condensation reaching ~12%

Years 4-5:
  O2 continues toward 0.21 atm target
  N2 continues building (still well below 0.78 target)
  Hydrosphere approaching 15-18%

Year 6 (O2 reaches target):
  Reallocate 70 O2 installations to N2 (now 120 on N2)
  N2 buildup accelerates dramatically
  Hydrosphere passes 20% -- hydrosphere CC factor eliminated

Years 7-10:
  N2 building rapidly with 120 installations
  Temperature improving as pressure increases greenhouse effect
  Pressure approaching 0.85 atm -- temperature crosses 0C

Year 10-11:
  N2 reaches 0.78 atm target
  All CC factors eliminated
  CC = 0.0! Terraforming complete!
  Redeploy installations to next target
```

### With Improved Technology (0.00032 atm/year)

At the first researched terraforming technology level (3,000 RP):

```
Effective Rate = 0.00032 * 2.86 = 0.000915 atm/year/installation
Total timeline: ~8-9 years instead of 10-11
```

At higher tech levels the improvement is more dramatic (e.g., Rate 7 at 0.0012 gives 0.00343 effective rate, reducing the project to ~3 years).

### With Fewer Installations (Budget Approach)

If you can only afford 30 installations total:

```
Phase 1 (CO2 removal, 10 inst.): 0.010 / (10 * 0.000715) = 1.40 years
Phase 2 (O2 addition, 15 inst.): 0.205 / (15 * 0.000715) = 19.1 years
Phase 3 (N2 addition, 15 inst.): 0.50 / (15 * 0.000715) = 46.6 years (parallel with O2)
Phase 4 (H2O, 5 inst.): hydrosphere takes ~7.5 years

Total timeline: ~47 years (N2 is the bottleneck)
```

The relationship is roughly linear: quarter the installations means quadruple the time. This demonstrates why terraforming in C# Aurora is a multi-decade commitment with modest installation counts.

---

## Key Decisions

*Updated: v2026.01.30*

| Decision | Recommended | Rationale |
|----------|-------------|-----------|
| Remove CO2 or add O2 first | Remove CO2 first | Eliminates danger immediately; fast |
| Gas order: N2 vs O2 | N2 parallel, O2 after CO2 | N2 safe at any qty; O2 + toxics = bad |
| Greenhouse strategy | Pressure-based warming | Good within -20C; avoids unwanted gas |
| Ground vs space-based | Ground-based | Higher throughput for multi-year projects |
| Pop. during terraforming | Minimal unless mining | Import pop after CC drops |
| Number of installations | 100-150 (3-5 yr) | Cost/speed sweet spot |
| When to stop | CC 0.0 achieved | Redeploy to next target immediately |

---

## Common Mistakes

*Updated: v2026.01.26*

### 1. Adding the Wrong Gas First

Adding O2 before removing toxic gases can create dangerous combinations. On a world with methane above 500 ppm, adding O2 creates a flammable atmosphere. Always remove toxics first, then add breathable gases.

### 2. Forgetting the Temperature Impact of Gas Changes

Removing CO2 (a greenhouse gas) can cool a world. In our example, removing CO2 dropped the temperature from -10C to -13.7C, actually worsening the temperature CC factor temporarily. This is acceptable because the temperature factor (0.78) is still less than the dangerous gas factor (2.0) that we eliminated. But on a borderline world, removing greenhouse gases without adding pressure compensation can increase overall CC.

### 3. Not Shipping Infrastructure Before Population

If you send 32.5 million colonists to staff terraforming installations at CC 2.0 without pre-shipping infrastructure:

```
Required infrastructure = 32,500,000 * 2.0 = 65,000,000 units
Without infrastructure: population suffers attrition (death)
```

Always ship infrastructure BEFORE or WITH your colonists. Never the other way around.

### 4. Ignoring Planet Size Factor

A common miscalculation is using the base 0.00025 atm/year rate without the planet size modifier. Our world at 35% Earth surface area gets a 2.86x bonus -- terraforming takes 1/2.86 the time compared to an Earth-sized target. Conversely, a super-Earth at 2x surface area takes twice as long. Always factor in planet size when estimating timelines.

### 5. Overshooting O2 Levels

Oxygen becomes toxic above 0.3 atm partial pressure OR above 30% of total atmosphere. If you are adding O2 to a world with only 0.5 atm total pressure:

```
30% of 0.5 atm = 0.15 atm maximum O2
```

You must add N2 to increase total pressure BEFORE adding O2 to target levels. At 1.0 atm total, the 30% cap is 0.30 atm -- well above the 0.21 atm target.

### 6. Not Accounting for Water Vapor Condensation

Water vapor condenses at 0.1 atm per year into surface water. If you are adding water vapor faster than it condenses, atmospheric water vapor can build up and contribute to greenhouse warming. This is usually beneficial (warming cold worlds) but can cause temperature overshoot on worlds near the upper habitable limit.

### 7. Terraforming a World Where Gravity Is the Problem

Gravity cannot be changed by terraforming. If a world's CC is dominated by gravity (below species minimum = CC 1.0, above species maximum = cannot colonize), terraforming the atmosphere is pointless for reducing colony cost unless the atmospheric factors are worse than the gravity factor.

In C# Aurora, only the WORST single factor determines CC. If gravity contributes 1.0 and atmosphere contributes 2.0, fixing the atmosphere drops CC to 1.0 -- still worth doing. But if gravity is 1.0 and atmosphere is 0.5, fixing the atmosphere has no effect on CC.

### 8. Leaving Installations Idle After Completion

130 terraforming installations represent significant construction investment. Once CC reaches 0.0, redeploy them immediately. Each year they sit idle on a completed world is a year they could be working on your next colony target.

---

## References

\hypertarget{ref-ex-terraform-1}{[1]}. Aurora C# game database (AuroraDB.db v2.7.1) -- DIM_PlanetaryInstallation PlanetaryInstallationID=6 (Terraforming Installation). Workers=0.125 (125,000 workers per installation).

---

## Related Sections

- [Section 5.3 Environment](../5-colonies/5.3-environment.md) -- Colony cost factors, temperature calculation, and habitability assessment
- [Section 5.4 Infrastructure](../5-colonies/5.4-infrastructure.md) -- Infrastructure requirements and population support
- [Section 5.5 Terraforming](../5-colonies/5.5-terraforming.md) -- Terraforming installations, rates, and gas strategies
- [Section 6.3 Construction](../6-economy-and-industry/6.3-construction.md) -- Building terraforming installations
- [Section 7.1 Technology Tree](../7-research/7.1-technology-tree.md) -- Terraforming technology upgrades
- [Appendix A: Formulas](../appendices/A-formulas.md) -- Terraforming rate, temperature, and colony cost formulas
- [Appendix C: Tips and Common Mistakes](../appendices/C-tips-and-mistakes.md) -- Colony cost checking and infrastructure tips
