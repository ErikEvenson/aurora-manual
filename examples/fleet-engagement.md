---
title: "Example: Fleet Engagement -- The Battle of Epsilon Junction"
parent: "Examples"
nav_order: 99
---

# Example: Fleet Engagement -- The Battle of Epsilon Junction

*Added: v2026.01.24*

This worked example walks through a complete tactical fleet engagement between two opposing forces. We cover sensor detection, approach decisions, engagement range selection, missile and beam exchanges, damage assessment, and the critical decision of when to withdraw.

> **Note:** This scenario assumes TN-start era technology (Nuclear Thermal engines at 5 EP/HS, base laser and missile tech, Duranium armor) with no ECM/ECCM, no shields, and no advanced point defense. Higher technology levels will significantly change engagement ranges, damage thresholds, and PD effectiveness. Adjust expectations accordingly for mid- or late-game fleets.

## Scenario Setup

Two hostile fleets encounter each other near a jump point in the Epsilon Eridani system. Neither side expected the other, and first contact occurs at long sensor range.

### Task Force Alpha (Player Fleet)

```
Composition:
  2x BC-10000 "Resolute" Beam Cruisers
    10,000 tons, 2,500 km/s
    6x 10cm UV Lasers (60 damage/volley per ship)
    3 layers Duranium armor (15 strength/column)
    Active sensor: resolution 100, detect 10kt at 500,000 km

  4x DD-6000 "Lancer" Missile Destroyers
    6,000 tons, 3,125 km/s
    8x Size-2 launchers (ASM-2, 1.6 damage per missile)
    2 layers Duranium armor (10 strength/column)
    40 missiles per ship (5 salvos each)
    2x CIWS each

Total Fleet:
  Speed: 2,500 km/s (limited by slowest ship -- the cruisers)
  Firepower: 120 beam damage/volley + 160 missiles (4 salvos of 32)
  Point Defense: 8 CIWS (destroyer contribution)
  Tonnage: 44,000 tons total
```

### Task Force Beta (Enemy Fleet)

```
Composition:
  1x BB-15000 "Overlord" Battleship
    15,000 tons, 1,800 km/s
    8x 12cm Lasers (96 damage/volley)
    5 layers Duranium armor (25 strength/column)
    Active sensor: resolution 200, detect 10kt at 600,000 km

  3x CL-8000 "Sentinel" Light Cruisers
    8,000 tons, 2,800 km/s
    4x 10cm Lasers (40 damage/volley per ship)
    3 layers Duranium armor (15 strength/column)
    4x CIWS each

Total Fleet:
  Speed: 1,800 km/s (limited by the battleship)
  Firepower: 216 beam damage/volley (combined)
  Point Defense: 12 CIWS (light cruiser contribution)
  Tonnage: 39,000 tons total
```

---

## Phase 1: Detection

### Sensor Contact

Both fleets are heading toward the same jump point from different vectors, initial separation 800,000 km.

**Alpha detects Beta first** (resolution 100 sensor vs 15,000-ton battleship):

The active sensor detection formula \hyperlink{ref-ex-fleet-1}{[1]} is:

```
Detection_Range (km) = sqrt((Active_Strength x HS x EM_Sensitivity x Resolution^(2/3)) / PI) x 1,000,000
```

For this engagement, the sensor parameters produce detection ranges in the tens of millions of km. However, this scenario assumes early TN-start technology with modest sensor sizes, keeping effective detection ranges much shorter than what advanced sensors achieve.

With Alpha's small resolution-100 sensor (detect 10kt at 500,000 km as specified in the design):

```
Result: Alpha detects Overlord (15,000t) at approximately 612,000 km -- CONTACT!
  (Larger target detected further than the 10kt design baseline)
```

**Beta detects Alpha** (resolution 200 sensor vs 10,000-ton cruiser):

```
Result: Beta detects Resolute at approximately 600,000 km -- nearly simultaneous detection
  (Higher-resolution sensor with better strength, but smaller target)
```

Both fleets have mutual contact at approximately 600,000+ km range.

> **Tip:** Detection range scales with the SQUARE ROOT of target size. A ship twice as large is not detected at twice the range -- only sqrt(2) = 1.41x the range. This means smaller ships have disproportionate stealth advantage at long range.

---

## Phase 2: Approach Decision

### Alpha's Options

At 800,000 km separation, Alpha's commander must decide:

**Option A: Close to beam range (~200,000 km)**
- Brings cruiser lasers into play
- Exposes fleet to enemy beam fire simultaneously
- Slower approach (Alpha limited to 2,500 km/s by cruisers)

**Option B: Stand off at missile range (~60 Mkm maximum)**
- Destroyers can engage from current range
- Cruiser lasers are useless at this distance
- Must rely on limited missile supply (160 missiles total)

**Option C: Split the fleet**
- Destroyers advance to missile range and harass
- Cruisers close separately for beam engagement
- Risk: fleet defeated in detail if enemy pursues one group

### Decision: Option A (Close to Beam Range)

Rationale:
1. Alpha's total beam damage (120/volley) requires close range
2. 160 missiles alone may not destroy the battleship (25 armor strength/column)
3. Alpha is faster (2,500 vs 1,800 km/s) -- can control engagement distance
4. Combined beam + missile provides highest kill probability

But we modify with an opening missile salvo at medium range to soften targets first.

### Approach Geometry

```
Closing speed (head-on approach): 2,500 + 1,800 = 4,300 km/s relative
Time to beam range (200,000 km from current 800,000 km):
  Distance to close: 600,000 km
  Time: 600,000 / 4,300 = 139.5 seconds = ~2 minutes 20 seconds
```

If Alpha advances while Beta also approaches, beam engagement occurs in under 3 minutes.

**However**, if Beta attempts to flee:
```
Pursuit speed: 2,500 - 1,800 = 700 km/s closure rate
Time to reach beam range from 800,000 km: 800,000 / 700 = 1,143 seconds = ~19 minutes
```

Beta is too slow to escape. Alpha will eventually catch them.

> **Tip:** Speed superiority is decisive in Aurora combat. A faster fleet can always choose to engage or disengage. A slower fleet has no option to refuse battle unless they can reach a jump point first.

---

## Phase 3: Opening Missile Salvo

### Alpha Launches at 500,000 km

At 500,000 km range (still well outside beam range), Alpha's 4 destroyers fire their first salvo:

```
Salvo 1: 32 missiles (8 per destroyer, 4 destroyers)
  Target: BB-15000 "Overlord" (highest priority -- eliminate enemy firepower)
  Missile speed: 4,800 km/s
  Time to target: 500,000 / 4,800 = 104 seconds = ~1.7 minutes
  Missile damage per hit: 1.6
```

### Beta's Point Defense Response

Beta's 12 CIWS (from 3 light cruisers) engage the incoming salvo:

```
PD Engagement:
  CIWS tracking speed: 5,000 km/s
  Missile speed: 4,800 km/s -- within tracking
  Engagement window: ~10,000 km range / 4,800 km/s = 2.08 seconds
  Shots per CIWS: ~2 per engagement window
  Total PD shots: 12 CIWS * 2 = 24 shots

Hit chance per shot \hyperlink{ref-ex-fleet-2}{[2]}:
  Base chance: min(1.0, FC_Tracking / Missile_Speed)
  = min(1.0, 5,000 / 4,800) = 1.0, but with range/engagement window factors
  Estimated effective: ~35% per shot (accounting for limited engagement time)

Expected kills: 24 * 0.35 = 8.4 missiles destroyed
Missiles reaching target: 32 - 8 = 24 missiles (approximately)
```

### Impact on Overlord

```
24 missiles hit BB-15000:
  Damage per missile: 1.6
  Total damage: 24 * 1.6 = 38.4 damage

Overlord armor: 5 layers * 5 strength = 25 per column
Armor columns (approximate for 15,000-ton ship): ~24 columns

Damage distribution: 24 missiles spread across 24 columns
  Average hits per column: 24 / 24 = 1 hit per column
  Damage per column: 1.6

With 25 strength per column, 1.6 damage per hit:
  Each hit strips: 1.6 / 5 = 0.32 layers from that column

Result: MINOR ARMOR DAMAGE -- scattered surface hits, no penetration
```

**Missile salvo 1 is largely ineffective against heavy armor.** The 25-strength armor shrugs off individual 1.6-damage hits. We need concentrated fire or beam weapons to breach this battleship.

> **Tip:** Missiles with low per-missile damage struggle against heavily armored targets. The damage is spread across many armor columns, never penetrating any single one. Against battleships, either use larger warheads, fire massive salvos to saturate individual columns, or rely on beam weapons that hit the same column repeatedly.

---

## Phase 4: Beam Engagement

### Closing to Laser Range

Both fleets continue closing. At 200,000 km, Alpha's cruiser lasers enter effective range.

```
Range: 200,000 km
Alpha laser accuracy at this range:
  Base hit chance: approximately 50% at 200,000 km for 10cm UV laser
  (Range modifier decreases linearly from max range)

Fire control tracking vs target speed:
  Alpha FC: 5,000 km/s tracking
  Overlord speed: 1,800 km/s
  Tracking modifier: min(1.0, 5000/1800) = 1.0 (full tracking)
```

### Alpha's Beam Volley (Both Cruisers Fire)

```
Volley 1 at Overlord:
  12 lasers total (6 per cruiser * 2 cruisers)
  Hit chance: ~50% at 200,000 km
  Expected hits: 12 * 0.5 = 6 hits
  Damage per hit: 10 (10cm laser)

Each hit vs 5-layer Duranium (25 strength):
  10 damage / 5 armor strength = 2 layers stripped per hit

6 hits across 24 armor columns:
  If all hit different columns: 2 layers stripped from 6 columns
  If some repeat (probability exists): deeper penetration on those columns

After volley 1: 6 columns reduced from 5 to 3 layers
  Remaining armor on hit columns: 3 * 5 = 15 strength
```

### Beta's Return Fire

```
Overlord fires at closest Alpha cruiser at 200,000 km:
  8x 12cm Lasers, damage 12 per hit
  Hit chance: ~50% at 200,000 km
  Expected hits: 8 * 0.5 = 4 hits

Each hit vs Alpha's 3-layer Duranium (15 strength):
  12 damage / 5 armor strength = 2.4 layers stripped per hit
  First hit: strips 2.4 layers → 0.6 layers remaining on that column
  Second hit same column: penetrates! 12 - 3 (remaining armor) = 9 internal damage!

4 hits across Alpha's armor columns (~20 columns for 10kt ship):
  Statistical spread: likely all different columns
  Each strips 2.4 layers from its column
  No penetration on first volley (if hits are distributed)

After volley 1: 4 columns reduced to 0.6 layers remaining
```

### Light Cruiser Fire

```
3x Sentinel Light Cruisers fire at second Alpha cruiser:
  12 lasers total (4 per CL * 3 CLs)
  Hit chance: ~50%
  Expected hits: 6
  Damage: 10 per hit

Same analysis as above: 6 columns stripped to ~0.6 layers
```

---

## Phase 5: Continued Exchange (Volleys 2-4)

### Volley 2 (5-Second Increment Later)

Both sides continue firing. Alpha launches second missile salvo while beam weapons cycle.

```
Alpha Missile Salvo 2 (32 missiles at Overlord):
  PD kills: ~8 missiles
  24 missiles hit, 1.6 damage each
  Overlord armor: now weakened on 6 columns (3 layers remaining)
  Hits on weakened columns: 1.6 damage vs 15 strength = minimal effect
  Hits on fresh columns: 1.6 vs 25 = negligible

  Still largely ineffective individually, but cumulative chip damage
```

```
Alpha Beam Volley 2 (at Overlord, now at ~180,000 km):
  Accuracy improves slightly at closer range: ~55%
  Expected hits: 12 * 0.55 = 6.6 ≈ 7 hits
  Each hit strips 2 layers

  If 2 hits land on previously-damaged columns (3 layers left):
    First hit: strips 2 layers → 1 layer remaining (5 strength)
    Second hit: strips remaining 1 layer → PENETRATION → 5 internal damage

  First armor breach on Overlord!
```

### Damage Tracking (Volley 2 Cumulative)

```
Overlord Status after 2 beam volleys:
  Armor breaches: 1-2 columns (internal damage beginning)
  Internal hits: 2-3 (random component targeting)
  Possible: engine hit (speed reduction), weapon hit (firepower loss)
  Hull integrity: ~95%

Alpha Cruiser 1 after 2 volleys from Overlord:
  4+4 = 8 total 12-damage hits over 2 volleys
  Several columns now penetrated (0.6 layers → second hit breaches)
  Internal hits: 3-4 (engine, weapon, or support system damage likely)
  Hull integrity: ~90%

Alpha Cruiser 2 after 2 volleys from Light Cruisers:
  6+6 = 12 total 10-damage hits over 2 volleys
  Multiple columns breached
  Internal hits: 4-5
  Hull integrity: ~85%
```

### Volleys 3-4 (Situation Escalates)

```
Volley 3 (range ~160,000 km, accuracy ~60%):
  Alpha beam damage: 7 hits on Overlord, 2-3 penetrating
  Beta damage: 4 penetrating hits on Cruiser 1, 3-4 on Cruiser 2

  Internal damage accumulating on both sides
  Overlord loses 1 laser (random internal hit) -- firepower drops to 84/volley
  Alpha Cruiser 2 loses 1 engine -- speed drops to 1,875 km/s (if ship detaches)
    BUT fleet stays together at 2,500 km/s on remaining 3 engines...
    Actually: cruiser with 3 remaining engines has:
    EP = 3 * 125 = 375 EP, speed = 375 * 1000 / 200 = 1,875 km/s
    Fleet speed NOW limited to 1,875 km/s (damaged cruiser is slowest)

Volley 4 (range ~140,000 km, accuracy ~65%):
  Multiple penetrating hits on all ships
  Overlord loses second laser -- 72 damage/volley remaining
  Alpha Cruiser 1: engineering hit, increased failure rate
  Sentinel CL #2: takes 2 stray missile hits from salvo 3, minor armor damage
```

---

## Phase 6: Damage Assessment (After 4 Volleys, ~20 Seconds of Combat)

### Task Force Alpha Status

```
BC-10000 "Resolute" #1:
  Armor: 40% of columns breached (1-2 layers remaining elsewhere)
  Internal damage: 6 hits -- 1 laser destroyed, engineering damaged
  Firepower: 50 damage/volley (5 remaining lasers)
  Speed: 2,500 km/s (engines intact)
  Status: DAMAGED -- combat effective

BC-10000 "Resolute" #2:
  Armor: 50% of columns breached
  Internal damage: 8 hits -- 1 engine destroyed, 1 laser destroyed, fuel leak
  Firepower: 50 damage/volley
  Speed: 1,875 km/s (3 engines)
  Status: HEAVILY DAMAGED -- fleet speed now 1,875 km/s

DD-6000 "Lancer" x4:
  Status: UNDAMAGED (not targeted by enemy beams, outside beam priority)
  Missiles remaining: 32 per ship (128 total, salvos 1-3 expended = 96 fired)
  Remaining salvos: 4 more full salvos
```

### Task Force Beta Status

```
BB-15000 "Overlord":
  Armor: 25% of columns breached (many at 1-3 layers remaining)
  Internal damage: 5 hits -- 2 lasers destroyed
  Firepower: 72 damage/volley (6 remaining lasers)
  Speed: 1,800 km/s (engines intact -- redundancy paying off)
  Status: DAMAGED -- armor holding but degrading

CL-8000 "Sentinel" x3:
  CL #1: Minor damage (1 stray missile hit)
  CL #2: Minor damage (2 missile hits, armor intact)
  CL #3: Undamaged
  Combined firepower: 120 damage/volley (unchanged)
  Status: COMBAT EFFECTIVE
```

---

## Phase 7: The Withdrawal Decision

### Alpha's Assessment

After 4 volleys (~20 seconds of beam combat), Alpha's commander evaluates:

```
Favorable factors:
  - Overlord taking armor damage, 2 weapons destroyed
  - Destroyers undamaged with 4 salvos remaining
  - Overlord cannot run (1,800 km/s vs Alpha's 1,875 km/s minimum)

Unfavorable factors:
  - Cruiser 2 heavily damaged, limiting fleet speed
  - Beta's TOTAL firepower (192/volley) exceeds Alpha's (100/volley + missiles)
  - Light cruisers are undamaged and dealing significant damage
  - Alpha is losing the attrition race in beam combat
```

### Critical Calculation: Can Alpha Win?

```
Overlord remaining armor: will fail in ~3-4 more volleys (6-8 more penetrating hits)
  Once armor fails: internal hits accelerate catastrophically
  Estimated volleys to kill Overlord: 6-8 more (30-40 more seconds)

Alpha cruiser survival time at current damage rate:
  Cruiser 2 at 85% hull: ~6-8 volleys before destroyed
  Cruiser 1 at 90%: ~8-10 volleys before destroyed

Risk: If a cruiser is destroyed, remaining cruiser faces 192 damage/volley alone
  Survival time of solo cruiser: 2-3 volleys (catastrophic)
```

### Decision: PARTIAL WITHDRAWAL

The optimal play is not full flight or full commitment, but a tactical repositioning:

```
Orders:
  1. Cruiser 2 (damaged): WITHDRAW at maximum speed (1,875 km/s, away from enemy)
  2. Cruiser 1: WITHDRAW at 2,500 km/s (escorts damaged cruiser initially)
  3. Destroyers: CONTINUE ENGAGEMENT at missile range
     - Speed advantage (3,125 km/s) lets them maintain distance
     - Fire remaining 4 salvos (128 missiles) at Overlord
     - Then withdraw at maximum speed
```

### Why This Works

```
Destroyers at 3,125 km/s vs Beta at 1,800 km/s:
  Destroyers can maintain ANY range they choose
  Beta cannot close to beam range with destroyers
  Destroyers fire missiles from beyond beam range, then flee

Beta's options:
  A: Chase destroyers -- impossible, too slow
  B: Chase cruisers -- gains slowly (1,800 vs 1,875), but cruisers pull away if undamaged cruiser escorts
  C: Head for jump point -- concedes the engagement area
```

> **Tip:** A fleet engagement does not need to end in total destruction of one side. Withdrawing damaged ships while screening with faster units preserves expensive assets. A damaged cruiser returned to shipyard is better than a destroyed cruiser.

---

## Phase 8: Disengagement

### Destroyer Missile Harassment (Salvos 4-7)

```
The 4 destroyers maintain 400,000 km range from Beta (well beyond beam range):

Salvo 4 (32 missiles): PD kills 8, 24 hit Overlord
  Overlord armor now heavily degraded -- some missiles find breached columns
  2-3 missiles deal internal damage (1.6 each)

Salvo 5 (32 missiles): PD kills 8, 24 hit Overlord
  More internal hits as armor collapses on concentrated columns
  Engine hit -- Overlord slows to 1,600 km/s

Salvo 6 (32 missiles): PD kills 7 (one CIWS destroyed by previous internal damage)
  25 hit -- armor nearly gone on facing side
  Multiple internals: fuel leak, fire control damaged

Salvo 7 (final, 32 missiles): PD kills 6 (reduced PD effectiveness)
  26 hit -- significant internal damage
  Overlord at 70% hull integrity, 4 lasers remaining, speed 1,400 km/s
```

### Final Situation

```
After destroyer missile harassment:

Task Force Alpha:
  Cruisers: withdrawing, damaged but alive (~45 minutes to shipyard)
  Destroyers: ammunition expended, withdrawing at 3,125 km/s
  Losses: 0 ships destroyed
  Damage: 2 cruisers need major refit

Task Force Beta:
  Overlord: heavily damaged (70% hull, half weapons, reduced speed)
  Light cruisers: minor damage only
  Losses: 0 ships destroyed
  Damage: Overlord needs 6+ months in shipyard

STRATEGIC RESULT: DRAW (tactical slight advantage to Alpha)
  - Alpha preserved all ships
  - Beta's battleship is crippled but alive
  - Alpha controls the engagement area (temporarily)
  - Neither side achieved decisive victory
```

---

## Lessons From This Engagement

### 1. Speed Dictates Engagement Terms

Alpha's 2,500 km/s (initially) vs Beta's 1,800 km/s meant Alpha could choose when and where to fight. After Cruiser 2 was damaged, the speed advantage narrowed dangerously. Protect your engines.

### 2. Heavy Armor Resists Missile Chip Damage

The Overlord's 5-layer armor made individual 1.6-damage missiles nearly useless until beam weapons weakened specific columns. Against heavy armor, missiles need either large warheads or massive salvo sizes.

### 3. Concentrated Fire Wins

Alpha's cruisers focusing all 12 lasers on the Overlord breached armor in 2-3 volleys. Beta spreading fire across both cruisers reduced effectiveness (neither killed quickly). Focus fire is almost always correct.

### 4. Fleet Composition Matters

Alpha's mixed beam/missile fleet had flexibility -- missiles for harassment, beams for killing. Beta's pure-beam fleet had no long-range option and could not prevent destroyer standoff attacks.

### 5. Know When to Withdraw

Alpha's commander recognized the attrition race was unfavorable (192 vs 100 damage/volley) and withdrew before losing a ship. A destroyed 10,000-ton cruiser takes 2+ years to replace. A damaged one takes 6 months to refit.

### 6. Screening Forces Enable Retreat

The destroyers' speed advantage let them cover the cruiser withdrawal while continuing to deal damage. Without screening forces, the cruisers would have had to run with no covering fire.

---

## Alternative Outcomes

### What If Alpha Had Focused Missiles on Light Cruisers?

```
32 missiles vs CL-8000 (3 layers armor, 15 strength/column):
  PD kills: 4 CIWS * 2 shots = 8 killed
  24 missiles hit, 1.6 damage each

  15 armor columns on 8,000-ton ship
  24 hits / 15 columns = 1.6 hits per column average
  Damage per column: 1.6 * 1.6 = 2.56 -- strips 0.5 layers per column

  Result: Surface damage only. Light cruiser armor holds.
  Conclusion: Missiles are ineffective against ALL armored targets at this warhead tech.
```

### What If Beta Had Focused All Fire on One Cruiser?

```
Combined Beta firepower on single cruiser: 96 + 120 = 216 damage equivalent
  At 50% accuracy: ~27 hits per volley
  Damage: 10-12 per hit

Cruiser with 3 layers (15 strength):
  First volley: 27 hits across 20 columns = 1.35 hits/column
  Multiple columns breached on FIRST VOLLEY
  5-8 internal hits immediately

  Second volley: massive internal damage, possible destruction

  Cruiser destroyed in 2-3 volleys (~10-15 seconds)!
```

Focus fire by Beta would have killed an Alpha cruiser before withdrawal was possible. Beta's tactical error (splitting fire) saved Alpha a ship.

> **Tip:** In Aurora combat, always focus fire on a single target unless you have overwhelming numerical advantage. Splitting fire between targets lets both survive longer and fight back. Concentrated firepower produces exponentially faster kills because armor is column-based -- repeated hits to the same columns penetrate faster.

---

## References

\hypertarget{ref-ex-fleet-1}{[1]}. Aurora C# active sensor formula from Appendix A: Detection_Range (km) = sqrt((Active_Strength x HS x EM_Sensitivity x Resolution^(2/3)) / PI) x 1,000,000. The x 1,000,000 multiplier (not x 10,000) produces detection ranges in the tens of millions of km for standard military sensors.

\hypertarget{ref-ex-fleet-2}{[2]}. Aurora C# v2.2.0+ point defense uses tracking-based hit chance: Base_Hit_Chance = min(1.0, FC_Tracking / Missile_Speed). Agility is no longer used in PD calculations.

---

## Related Sections

- [Section 12.2 Beam Weapons](../12-combat/12.2-beam-weapons.md) -- Laser damage, range, and accuracy calculations
- [Section 12.3 Missiles](../12-combat/12.3-missiles.md) -- Missile flight, seeker acquisition, and impact
- [Section 12.4 Point Defense](../12-combat/12.4-point-defense.md) -- CIWS engagement mechanics
- [Section 12.6 Damage and Armor](../12-combat/12.6-damage-and-armor.md) -- Armor column system and internal damage
- [Section 11.3 Active Sensors](../11-sensors-and-detection/11.3-active-sensors.md) -- Detection range and resolution
- [Section 9.3 Task Groups](../9-fleet-management/9.3-task-groups.md) -- Fleet speed and formation
- [Section 9.5 Orders](../9-fleet-management/9.5-orders.md) -- Engagement and withdrawal orders
- [Appendix A: Formulas](../appendices/A-formulas.md) -- Combat resolution and damage formulas
