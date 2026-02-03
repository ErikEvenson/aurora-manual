---
title: "Example: Planning a Ground Invasion"
parent: "Examples"
nav_order: 99
---

# Example: Planning a Ground Invasion

*Updated: v2026.01.30*

This worked example walks through the process of planning, executing, and consolidating a ground invasion of an enemy colony. It demonstrates force composition calculations, transport logistics, orbital support coordination, and post-conquest occupation requirements.

---

## Contents

*Updated: v2026.01.30*

{: .no_toc }

- TOC
{:toc}

## Starting Conditions

*Updated: v2026.01.30*

- **Target:** Enemy colony on Barnard's Star III, estimated population 50 million
- **Enemy Ground Forces:** Unknown composition, estimated 10-20 battalions based on thermal/EM signatures detected from orbit
- **Enemy Orbital Defenses:** 2 Planetary Defense Centers (PDCs) detected via active sensor sweep
- **Your Position:** Fleet has achieved orbital superiority; enemy naval forces have been destroyed or driven off
- **Your Available Forces:** 3 infantry regiments, 2 armored battalions, 1 artillery formation, 1 combat engineer battalion, plus transport and escort ships

---

## Step 1: Intelligence Gathering

*Updated: v2026.01.30*

Before committing forces, gather what information you can from orbit.

### What You Can Detect

Ground forces are treated as size-1 for detection purposes ([Section 13.3.5 Ground Forces Detection](../13-ground-forces/13.3-ground-combat.md#1335-ground-forces-detection)). Their formation signature is calculated as:

```
Formation Signature = (Total Formation Signature) / 100
Element Signature = (Unit Size x Unit Number) / (Fortification Level x Dominant Terrain Fortification Modifier)
```

From orbit, you can observe:

- **Thermal signatures** of ground installations and active equipment
- **EM emissions** from active sensors (including STO weapon sensors)
- **PDC locations** via active sensor sweeps
- **Terrain type** of the planet (determines combat modifiers)

### What You Cannot Determine

- Exact composition of enemy ground forces (unit types, armor levels, weapons)
- Fortification level (a small well-fortified force and a large unfortified force look similar)
- Whether units have combat capabilities (Mountain Warfare, etc.)
- Location of STO weapons that have not yet fired

### Intelligence Assessment for This Scenario

Barnard's Star III has **Forest** terrain:

- Fortification Modifier: 1.0
- To-Hit Modifier: 0.5 (moderate concealment)

The detected signatures suggest 10-20 battalions. Given the population of 50M, this is a reasonable garrison. The 2 PDCs represent orbital-grade weapons that must be addressed before landing.

**Key Uncertainty:** We do not know if the enemy has STO weapons. If present, they will engage our fleet during bombardment operations. Plan accordingly.

---

## Step 2: Orbital Bombardment Decision

*Updated: v2026.01.30*

### Option A: Bombard First

**Advantages:**

- Reduces enemy fortification levels before landing
- May destroy defensive positions and key installations
- Suppresses PDCs and potential STO weapons
- Reduces casualties during the ground assault

**Disadvantages:**

- Destroys infrastructure you want to capture (factories, mines, shipyards)
- Causes civilian casualties (each shot has a 1/3 chance of hitting the population)
- May trigger diplomatic penalties with neutral factions
- Terrain modifier (0.5 for Forest) reduces bombardment effectiveness by half
- Energy weapon NBG has only 1/3 the accuracy of precision orbital support

### Option B: Land Without Bombardment

**Advantages:**

- Preserves colony infrastructure intact
- No civilian casualties from orbital fire
- No diplomatic complications
- Faster timeline to productive colony

**Disadvantages:**

- Enemy retains full fortification (potentially level 6 for infantry with construction support)
- Higher ground force casualties expected
- PDCs remain active and may engage transports during landing
- STO weapons (if present) remain undamaged

### Decision for This Scenario

**Compromise approach:** Conduct targeted bombardment focused specifically on detected PDCs and any STO contacts. Avoid general bombardment to preserve infrastructure. Accept higher ground force casualties in exchange for a functional colony post-conquest.

### Suppressing PDCs

PDCs must be neutralized before transports enter orbit. Using energy weapons:

```
Ground Damage = 20 x sqrt(Point Blank Ship-to-Ship Damage)
Armor Penetration = Ground Damage / 2
```

Example with 25cm lasers (PB damage ~16):
```
Ground Damage = 20 x sqrt(16) = 80
Ground AP = 40
```

NBG energy weapon accuracy:
```
NBG Energy To-Hit = (Base 20% / 3) x (Terrain To-Hit Modifier) / (Target Fortification x Terrain Fortification Modifier)
              = 6.67% x 0.5 / (Fortification x 1.0)
```

Against a PDC at fortification level 6: effective to-hit = 6.67% x 0.5 / 6 = 0.56% per shot. This is very low -- sustained bombardment over multiple phases is required. PDCs are tough targets.

**Alternative:** Use missile bombardment (100% base to-hit for warheads). A 9-point warhead delivers Ground Damage of 60 and AP of 30, but also increases radiation and dust levels. For 2 PDCs, allocate a significant missile salvo and expect collateral damage.

---

## Step 3: Force Composition Planning

*Updated: v2026.01.30*

### The 3:1 Rule

A minimum 3:1 attacker-to-defender ratio in combat power is recommended for assaulting fortified positions. In Forest terrain with fortification, the effective ratio needed may be higher.

### Estimating Enemy Strength

Assume worst case: 20 battalions of mixed composition:

- 10 infantry battalions (fortified to level 6 with construction support)
- 5 heavy vehicle battalions (fortified to level 3)
- 3 artillery formations (in support position)
- 2 HQ/logistics formations (rear echelon)

### Required Attacker Strength

For a 3:1 ratio against 20 defending battalions, you need the equivalent of 60 battalions of combat power. However, several factors modify this:

**Factors reducing required strength:**

- Orbital bombardment support (precision fire through FFD elements)
- Ground support fighters (if available)
- Attacker surprise (defender has limited intelligence on your composition)

**Factors increasing required strength:**

- Forest terrain to-hit modifier (0.5x, halving accuracy)
- Defender fortification (divides incoming to-hit further)
- Attack mode forfeits all fortification bonuses for your troops
- Environmental penalties if your troops lack appropriate training

### Force Composition Calculation

Design your assault force for combined arms effectiveness:

| Formation | Battalions | Role | Transport Tonnage (each) |
|-----------|-----------|------|--------------------------|
| Infantry Regiments | 3 (9 battalions total) | Front-line attack, occupation | ~3,000-5,000 tons |
| Armored Battalions | 2 | Breakthrough, anti-vehicle | ~8,000-12,000 tons |
| Artillery Formation | 1 | Support position, bombardment | ~5,000-8,000 tons |
| Combat Engineers | 1 | Construction/fortification | ~3,000-5,000 tons |
| HQ Formation | 1 | Command and control | ~2,000-3,000 tons |
| Logistics Formation | 1 | Supply (Standard Logistics Modules) | ~5,000-8,000 tons |
| **Total** | **~15 formations** | | **~60,000-90,000 tons** |

### Detailed Infantry Regiment Composition

A typical assault infantry regiment (3 battalions, ~15,000 tons total):

| Element | Quantity | Tonnage Each | Total Tons | Role |
|---------|----------|-------------|-----------|------|
| Rifle Infantry | 300 | 5 | 1,500 | Front-line combat |
| Heavy Infantry (AV) | 100 | 8 | 800 | Anti-vehicle |
| HQ Infantry | 20 | 10 | 200 | Command |
| FFD Infantry | 10 | 8 | 80 | Fire direction |
| Combat Engineers | 30 | 10 | 300 | Fortification |
| Logistics Infantry (Small) | 50 | 10 | 500 | Own-formation supply |
| AA Infantry | 20 | 8 | 160 | Air defense |

### Supply Calculations

Each combat element has inherent supply for 10 rounds. For sustained operations, plan for 30+ rounds:

```
GSP per 10 rounds (Rifle Infantry) = 1 x 1 x 1 = 1 GSP per element
GSP per 10 rounds (Heavy Infantry) = 4 x 6 x 1 = 24 GSP per element

Total formation GSP per 10 rounds:
  Rifle: 300 x 1 = 300 GSP
  Heavy: 100 x 24 = 2,400 GSP
  Total: 2,700 GSP per 10 rounds

For 30 additional rounds (beyond inherent):
  Required logistics: 2,700 x 3 = 8,100 GSP
  Standard Logistics Modules (500 GSP each): 17 vehicles needed
  Small Logistics Modules (100 GSP each): 81 infantry needed
```

---

## Step 4: Transport Requirements

*Updated: v2026.01.30*

### Calculating Fleet Transport Capacity

Assume total force tonnage: 75,000 tons (midpoint of our estimate).

Each troop transport ship must be designed with sufficient bay capacity. Example transport designs:

| Transport Class | Bay Capacity | Ships Needed | Total Capacity |
|----------------|-------------|-------------|---------------|
| Light Transport (5,000t bays) | 5,000 tons | 15 | 75,000 tons |
| Heavy Transport (10,000t bays) | 10,000 tons | 8 | 80,000 tons |
| Assault Transport (15,000t bays) | 15,000 tons | 5 | 75,000 tons |

### Practical Considerations

- **Build extra capacity:** Plan for 10-20% surplus to account for losses in transit and reinforcement needs
- **Speed matching:** Transports must match escort fleet speed, or travel under separate escort in secured space
- **Fuel range:** Transports need sufficient fuel for the round trip plus orbital operations time
- **Multiple lifts:** If transport capacity is insufficient, you can land forces in waves, but this extends the timeline and allows the defender to react

### For This Scenario

Using 8 Heavy Transports (10,000 tons each = 80,000 ton capacity):

- Load all formations simultaneously
- Escort with combat fleet that has already achieved orbital superiority
- Single-lift deployment preferred to maximize initial shock

---

## Step 5: Orbital Support During Ground Assault

*Updated: v2026.01.30*

### Precision Orbital Bombardment Support

Ships assigned to "Provide Orbital Bombardment Support" fire once per ground combat phase with FFD-directed accuracy:

```
Each FFD component enables 1 orbital bombardment ship OR 6 ground support fighters
```

**For this assault:**

- 10 FFD elements across all formations = 10 ships can provide precision support
- Assign largest-caliber beam ships (25cm+ lasers preferred)
- Ships fire simultaneously with artillery in the bombardment phase

### Orbital Support Accuracy

```
Modified by:
  - Crew grade and morale
  - Tactical Officer: 100% of ground support bonus
  - Ship Commander: 50% of ground support bonus
  - Standard ground combat accuracy calculations
```

Precision orbital support is far more accurate than NBG (Naval Bombardment of Ground Forces) -- it uses full ground combat to-hit rather than the 1/3 reduction for blind fire.

### STO Weapon Risk

Ships in bombardment support orbit are vulnerable to STO weapons:

- STO fire control has 25% range bonus vs ship-mounted equivalents
- Multiple STO formations stack their defensive contribution
- Monitor for STO contacts and be prepared to withdraw ships if losses mount

---

## Step 6: Landing Sequence

*Updated: v2026.01.30*

### Where to Land

- **Away from PDCs:** Do not land directly on detected PDC positions. PDCs have STO capability and will engage transports
- **Away from main force concentrations:** Minimize immediate engagement with fortified positions
- **Consider terrain:** Landing in open terrain near the forest boundary allows initial fortification before advancing

### Landing Options

| Method | Casualties | Speed | Best For |
|--------|-----------|-------|----------|
| Conventional Unload | None | Moderate | When orbital space is secure |
| Combat Drop | 5-15%+ | Fast | Opposed landings, surprise |

### Recommended Sequence for This Scenario

1. **Suppress PDCs** with precision missile strikes (30-60 minutes of bombardment)
2. **Land main force** via conventional unload at a point distant from enemy concentrations
3. **Establish beachhead** -- all formations begin self-fortification immediately (30 days to reach self-fort max)
4. **Deploy logistics and HQ** in rear echelon positions
5. **Position artillery** in support field position
6. **Advance** after achieving at least partial fortification (7-10 days minimum)

### Fortification Timeline

```
Self-Fortification time: 30 days (all unit types)
  Day 0: Fortification = 0
  Day 7: ~23% of max self-fortification
  Day 15: ~50% of max self-fortification
  Day 30: Full self-fortification achieved
    Infantry: Level 3
    Heavy Vehicles: Level 2
    Light Vehicles: Level 2
```

**Trade-off:** Waiting for full fortification gives the defender time to reposition. Attacking immediately means no fortification bonus (which is forfeited in attack mode anyway). The key benefit of partial fortification is protecting your support and rear echelon elements.

---

## Step 7: Ground Combat Phases

*Updated: v2026.01.30*

### Combat Resolution (per 8-hour phase)

Each phase follows this sequence:
1. Supply check (unsupplied units fire at 25%)
2. Target selection (weighted by formation size)
3. Bombardment phase (artillery, fighters, orbital support)
4. Direct combat phase (front-line elements engage)
5. AA phase (anti-aircraft fires on attacking aircraft)
6. Casualty assessment
7. Morale update
8. Breakthrough check (if potential >= 30%)
9. Fortification update

### To-Hit Calculation in Forest Terrain

```
Final To-Hit = (Base 20%) x (Terrain Modifier) x (Morale Ratio) / (Fortification x Environment)

Your infantry attacking fortified enemy infantry:
  = 20% x 0.5 / (6 x 1.0)  [assuming max fortification, no environment penalty]
  = 10% / 6
  = 1.67% per shot
```

This is very low, which is why combined arms and orbital support matter:

```
Your artillery (from support position) bombarding:
  = Base bombardment accuracy x GCA commander bonus x terrain modifier
  [Fires simultaneously with orbital support, bypasses some fortification benefits]

Orbital support (25cm laser, Ground Damage 80, AP 40):
  Against infantry armor (Racial Armor ~3-5):
  AP 40 vs Armor 5: (40/5)^2 = 64x -- automatic penetration
  Damage 80 vs HP ~5: (80/5)^2 = 256x -- automatic destruction
```

Orbital fire is devastating when it hits, but the to-hit chance through fortification and terrain is low. Sustained bombardment gradually attrites the defender.

### Breakthrough Mechanics

```
Breakthrough Value:
  Vehicles: Size x Units x (Morale/100)
  Infantry: Size x Units x (Morale/100) x 0.5

When breakthrough potential >= 30%:
  - Additional attacks without support
  - Can target all hostile formations regardless of position
  - Represents exploitation of gaps in enemy lines
```

**Use armored battalions for breakthrough.** Their larger size and vehicle multiplier (no 0.5x infantry penalty) make them the primary breakthrough force.

### Expected Casualties

Against a fortified defender in Forest terrain with 3:1 superiority:

- **Attacker losses:** 15-30% of front-line combat elements over 10-20 combat phases
- **Defender losses:** Progressive attrition, accelerating after fortification is reduced
- **Timeline:** 5-15 days of combat (15-45 combat phases at 8 hours each)

These are rough estimates. Actual results depend on unit composition, commander bonuses, morale, and combat dice.

---

## Step 8: Occupation Force Requirements

*Updated: v2026.01.30*

### Occupation Strength

\hyperlink{ref-ex-ground-1}{[1]}

The exact occupation strength formula is not fully publicly documented and involves multiple factors including population size, racial traits (Determination, Militancy, Xenophobia), political status modifiers, and governance type. The formula operates on tonnage of ground forces rather than battalion count.

### Practical Garrison Requirements

While the exact formula is complex, practical experience from the Aurora community provides useful guidelines for garrison planning:

**For a 50M conquered population with moderate traits:**

- **Minimum garrison:** 5-10 infantry battalions (sufficient to prevent severe unrest)
- **Comfortable garrison:** 10-15 infantry battalions (minimizes unrest growth)
- **Heavy occupation:** 20+ infantry battalions (rapid unrest suppression)

Key factors that reduce required garrison strength:

- A commander with high OCC (Occupation) bonus significantly reduces requirements
- Lower racial Determination, Militancy, and Xenophobia values
- Favorable political status (e.g., neutral vs. hostile governance)
- Time -- unrest naturally declines if occupation strength exceeds the threshold

Key factors that increase required garrison strength:

- High racial trait values (Determination 80+, Militancy 70+, Xenophobia 60+)
- Hostile political status
- Large populations (scales with population size)
- No assigned governor or commander

### Unrest Without Sufficient Occupation

```
Unrest Points (annual) = 100 x (1 - Actual Strength / Required Strength)
```

If you leave half the required force:
```
Unrest = 100 x (1 - 0.5) = 50 points per year
Production penalty = 50% reduction to all output
```

### Garrison Force Composition

For long-term occupation, use inexpensive garrison formations:

- **Garrison Infantry:** Reduced offensive capability, full defensive strength, lower cost
- **HQ elements:** Maintain command structure
- **Construction elements:** Build fortifications for garrison positions
- **No heavy armor needed:** Garrison duty does not require offensive punch

---

## Step 9: Post-Conquest Management

*Updated: v2026.01.30*

### Immediate Actions (First 30 Days)

1. **Deploy garrison formations** to the planet surface
2. **Assign a governor** with OCC (Occupation) and Admin bonuses
3. **Suppress any remaining hostile formations** (mop-up operations)
4. **Begin fortifying garrison positions** (30 days to self-fortification)
5. **Assess infrastructure damage** from orbital bombardment and ground combat

### Managing Unrest

Unrest reduces production proportionally. To reduce unrest:

```
Natural decline (when cause removed):
  Fall = 20 x (1 - (Determination / 100))
  For Determination 60: Fall = 20 x 0.4 = 8 points/year natural decline

Military suppression (excess occupation strength):
  Police Strength = Actual - Required
  Reduction = 100 x (Police Strength / Effective Population Size)
```

**Key:** Maintain occupation forces above the required threshold. Any shortfall generates unrest that compounds over time.

### Infrastructure Assessment

After conquest, check:

- **Mines:** Are they still operational? Bombardment may have destroyed some
- **Factories:** Construction capacity for rebuilding
- **Research labs:** Technology exploitation potential
- **Fuel refineries:** Fuel production for local fleet support
- **Population:** Civilian casualties reduce workforce

### Integration Timeline

- **Days 1-30:** Garrison deployment, initial fortification
- **Days 30-90:** Unrest stabilization, infrastructure assessment
- **Months 3-12:** Production restoration, infrastructure rebuilding
- **Year 1+:** Full integration, population growth resumption

---

## Key Decisions Summary

*Updated: v2026.01.30*

| Decision | Conservative Choice | Aggressive Choice | Recommendation |
|----------|-------------------|-------------------|----------------|
| Bombard first? | Targeted only (PDCs) | General bombardment | Targeted -- preserve infrastructure |
| Troop ratio | 5:1 | 3:1 minimum | 3:1 with orbital support |
| Landing method | Conventional (safe) | Combat drop (fast) | Conventional after PDC suppression |
| Speed vs mass | Full force, single lift | Fast light force, reinforce later | Single lift preferred |
| Occupation commitment | Minimal garrison | Heavy occupation force | Moderate -- enough to prevent unrest |

---

## Common Mistakes

*Updated: v2026.01.30*

1. **Insufficient transport capacity.** Calculate total tonnage carefully. Running short means multiple lifts, giving the defender time to react.

2. **Landing directly on PDCs.** PDCs have STO capability and will shred transports. Suppress them first with missile bombardment.

3. **Not enough occupation forces.** Unrest from insufficient occupation generates 100 points/year with no forces present. The colony becomes useless without adequate garrison.

4. **Forgetting to suppress orbital defenses.** STO weapons can engage your support ships. PDCs threaten transports. Neutralize these before committing vulnerable assets.

5. **Attacking without sufficient superiority.** The Forest terrain to-hit modifier (0.5x) combined with level-6 fortification means your base to-hit is ~1.67%. You need volume of fire, orbital support, and breakthrough-capable armor.

6. **Neglecting supply.** 10 rounds of inherent supply goes fast. Without logistics elements, formations drop to 25% effectiveness and cannot attack.

7. **Ignoring the FFD requirement.** Without Forward Fire Direction elements, your formations cannot receive orbital bombardment support or ground support fighter assistance. Include FFD in every combat formation template.

8. **Not planning for post-conquest.** Taking the colony is half the battle. Without garrison forces, a governor, and infrastructure support, the conquest is worthless.

---

## Advanced Tactics

*Updated: v2026.01.26*

The preceding sections cover the fundamentals of planetary invasion. This section addresses more sophisticated scenarios requiring multi-formation coordination, integrated orbital assets, PDC assault techniques, and sustained logistics for extended campaigns.

---

### Multi-Formation Coordination

Large-scale invasions require coordination across multiple formations operating with different field positions and tactical roles. Effective command hierarchy and timing are essential.

#### 1. Echelon Structure

Organize your invasion force into a command hierarchy before deployment:

```
Division HQ (125,000 ton capacity)
├── 1st Brigade HQ (25,000 ton capacity)
│   ├── 1st Infantry Battalion (attack)
│   ├── 2nd Infantry Battalion (attack)
│   └── 3rd Infantry Battalion (defence)
├── 2nd Brigade HQ (25,000 ton capacity)
│   ├── 1st Armored Battalion (attack)
│   ├── 2nd Armored Battalion (attack)
│   └── Combat Engineer Battalion (defence)
└── Support Brigade HQ
    ├── Artillery Battalion (support position)
    ├── Logistics Battalion (rear echelon)
    └── AA Battalion (rear echelon)
```

**Why hierarchical organization matters:**

- Commander bonuses cascade down the hierarchy (100% direct, 25% superior)
- Logistics elements at brigade level supply all subordinate formations
- HQ capacity determines effective bonus application
- Formations under the same brigade share supply pools

#### 2. Phased Assault Tactics

**Phase 1 -- Establish Beachhead (Days 1-7):**

| Formation Type | Field Position | Role |
|---------------|---------------|------|
| Infantry battalions | Front Line Attack | Engage immediately while unfortified |
| Armored battalions | Front Line Attack | Breakthrough attempts |
| Artillery | Support | Begin bombardment suppression |
| Engineers/Logistics | Rear Echelon | Build supply base |

**Phase 2 -- Consolidate and Attrit (Days 7-21):**

| Formation Type | Field Position | Role |
|---------------|---------------|------|
| 2/3 Infantry | Front Line Defence | Begin fortification |
| 1/3 Infantry | Front Line Attack | Maintain pressure |
| Armored | Rotate attack/defence | Rest for breakthrough |
| Artillery | Support | Counter-battery fire |

**Phase 3 -- Breakthrough and Exploitation (Day 21+):**

| Formation Type | Field Position | Role |
|---------------|---------------|------|
| Infantry | Front Line Defence | Hold captured ground |
| Armored | Front Line Attack | Exploit breakthroughs |
| Artillery | Support | Suppress reinforcements |
| Engineers | Defence | Fortify captured positions |

> **Tip:** Newly landed formations have zero fortification. Set them to attack mode immediately -- the defensive bonus of front-line defence is wasted until fortification accumulates. After 7-10 days, transition defensive formations to front-line defence to begin building their fortification levels.

#### 3. Commander Bonus Stacking

Maximize combat effectiveness through proper commander assignment:

```
Division Commander (20% GCO, 15% GCD)
└── Brigade Commander (15% GCO, 10% GCD, 10% GCM)
    └── Battalion Commander (10% GCO, 10% GCA)

Effective bonuses at battalion level:
  GCO: 10% (direct) + 3.75% (brigade) + 5% (division) = 18.75%
  GCD: 0% (direct) + 2.5% (brigade) + 3.75% (division) = 6.25%
  GCM: 0% (direct) + 2.5% (brigade) = 2.5%
  GCA: 10% (direct) = 10%
```

**Commander assignment priorities:**

1. **Division/Brigade HQ:** High GCO, GCD, and GCM (offensive bonuses cascade)
2. **Artillery formations:** High GCA (artillery accuracy)
3. **Armored formations:** High GCM (breakthrough probability)
4. **Garrison formations:** High OCC (occupation strength)

---

### Orbital Bombardment Integration

Effective integration of orbital assets with ground forces dramatically increases combat effectiveness but requires careful coordination to avoid friendly fire and manage ship vulnerability.

#### 1. FFD Capacity Planning

Forward Fire Direction elements are the bottleneck for orbital support:

| FFD Elements | Ships Supported | Fighters Supported |
|-------------|-----------------|-------------------|
| 5 | 5 ships | 30 fighters |
| 10 | 10 ships | 60 fighters |
| 20 | 20 ships | 120 fighters |

**FFD distribution strategy:**

- Spread FFD elements across multiple formations (if one formation is destroyed, you retain FFD capability)
- Front-line formations need FFD to call in precision strikes on their targets
- Mark FFD infantry with the "Avoid Combat" flag to protect this critical capability
- Plan for FFD attrition: losing all FFD silences your orbital support

#### 2. Ship Selection for Orbital Support

Not all ships are equally suited for orbital bombardment support:

| Ship Type | Ground Damage | Recommendation |
|-----------|---------------|----------------|
| 25cm+ Lasers | 80+ (devastating) | Excellent -- prioritize these |
| Heavy Particle Beams | 70+ | Excellent -- no damage falloff |
| 15cm Lasers | ~45 | Good secondary |
| Railguns | Lower | Better for suppression volume |
| Carriers (fighters) | Varies | Good if fighters have bombardment pods |

**Ground damage conversion:**

```
Ground Damage = 20 x sqrt(Point Blank Ship-to-Ship Damage)
```

Example calculations:

| Weapon | PB Damage | Ground Damage | Ground AP |
|--------|-----------|---------------|-----------|
| 25cm UV Laser | 16 | 80 | 40 |
| 30cm Particle Beam | 20 | 89 | 45 |
| Heavy Laser (12") | 36 | 120 | 60 |

#### 3. Orbital Support vs. NBG Bombardment

Two distinct orbital fire modes exist:

| Mode | Accuracy | Collateral | Best Use |
|------|----------|------------|----------|
| **Orbital Bombardment Support** | Full ground combat accuracy | None | Coordinated attacks with ground forces |
| **Naval Bombardment (NBG)** | 1/3 base accuracy | 1/3 chance to hit population | Softening before landing |

**When to use each:**

- **Pre-landing softening:** NBG to reduce fortification levels (accept collateral damage)
- **Active ground combat:** Orbital Bombardment Support for precision (requires FFD)
- **PDC suppression:** NBG with missiles (100% base accuracy for warheads)

#### 4. STO Weapon Countermeasures

Surface-to-Orbit weapons threaten ships in bombardment orbit:

**Threat assessment:**

- STO fire controls have 25% range bonus vs. ship equivalents
- STO weapons only reveal themselves after firing (then flagged as "STO Ground Forces" contact)
- Multiple STO formations stack defensive contribution

**Mitigation strategies:**

1. **Identify STOs first:** Conduct initial NBG pass with expendable ships to draw STO fire
2. **Prioritize STO suppression:** Once identified, allocate missile salvos specifically against STO contacts
3. **Rotate bombardment ships:** Cycle damaged ships out of bombardment orbit
4. **Shield optimization:** Heavy shields buy time against STO attrition
5. **Speed matters:** Faster ships are harder for STO to track -- consider using fast destroyers for bombardment support over slow battleships

> **Warning:** Ships in orbital bombardment support are stationary targets for STO weapons. If intelligence indicates significant STO presence, suppress or destroy STOs before committing high-value warships to prolonged bombardment duty.

---

### PDC Assault Strategies

Planetary Defence Centres require specialized tactics due to their isolation mechanics and formidable firepower.

#### 1. PDC Defense Rules

Understanding how PDCs fight is essential for planning assaults:

1. **Isolated garrisons:** Only troops inside the specific PDC being attacked defend it -- other PDCs cannot reinforce
2. **No reinforcement:** Once assault begins, the garrison fights with whoever was present at attack start
3. **No magazine reload:** PDCs under ground attack cannot reload from planetary stockpiles
4. **Offensive sorties:** Troops in OTHER PDCs can emerge to fight offensively (losing their PDC protection)

#### 2. Divide and Conquer Tactics

The isolation mechanic enables sequential reduction:

**Step 1: Isolate a single PDC**

Land your main force away from PDC concentrations. Advance toward one PDC while leaving screening forces to pin troops in other PDCs.

**Step 2: Mass overwhelming force**

Concentrate 5:1 or greater force superiority against the targeted PDC. The isolated garrison cannot receive help.

**Step 3: Starve ammunition**

Sustained ground assault prevents magazine reloads. Even if the garrison holds, the PDC's anti-ship weapons eventually run dry -- valuable for follow-on naval operations.

**Step 4: Exploit defensive sorties**

When defenders emerge from other PDCs to attack your screening forces, they forfeit their PDC's protective fortification. Destroy them in the open with concentrated fire and orbital support.

**Step 5: Repeat**

Move to the next PDC. Each successive PDC has fewer potential reinforcements as you eliminate sortie forces.

#### 3. PDC Suppression Before Landing

Never land troops in active PDC weapon range without suppression:

**Pre-landing bombardment sequence:**

1. **Identify PDC locations** via active sensor sweep from orbit
2. **Missile bombardment first** (100% base accuracy vs. fortified targets)
3. **Allocate significant salvos:** A PDC at fortification 6 has ~0.56% per-shot hit chance from energy weapons; missiles are far more effective
4. **Monitor shield status:** Initial salvos deplete PDC shields; subsequent salvos cause structural damage
5. **Confirm suppression:** PDC weapons should cease firing before transport approach
6. **Land distant from PDCs:** Even suppressed PDCs may retain some capability -- land outside their remaining weapon range

**Bombardment formula reference:**

```
Energy NBG To-Hit = (Base 20% / 3) x (Terrain Modifier) / (Fortification x Terrain Fortification Modifier)
```

For a PDC in Forest terrain at fortification 6:
```
To-Hit = 6.67% x 0.5 / (6 x 1.0) = 0.56% per shot
```

This demonstrates why missiles (100% base accuracy) are vastly preferred for PDC suppression.

#### 4. Ground Assault on PDCs

Once you've landed and softened the PDC via bombardment:

| Tactic | Effectiveness | Risk |
|--------|---------------|------|
| **Conventional assault** | Slow but steady attrition | Moderate casualties from PDC garrison |
| **Siege warfare** | Very slow; starve ammunition | Minimal casualties; PDC remains combat-capable longer |
| **Combined arms mass assault** | Fastest resolution | Highest casualties but quickest PDC neutralization |

**Recommended approach:**

1. Position artillery in support to bombard the PDC garrison
2. Mass armored formations for breakthrough attempts
3. Use orbital bombardment support through FFD coordination
4. Accept casualties to achieve rapid reduction -- prolonged sieges allow other PDCs to sortie
5. After capture, use the PDC's position as your own fortified base

---

### Supply Line Management for Extended Campaigns

Multi-phase invasions lasting weeks or months require sophisticated logistics planning beyond the initial assault supply.

#### 1. Supply Consumption Rates

Calculate total GSP requirements for campaign duration:

```
Total GSP = (GSP per 10 rounds) x (Expected combat rounds / 10) x (Number of combat formations)
```

**Example for a 30-day campaign (90 combat phases):**

| Formation Type | GSP/10 rounds | Formations | Total GSP |
|---------------|---------------|------------|-----------|
| Infantry Battalion | 2,700 | 6 | 145,800 |
| Armored Battalion | 8,500 | 3 | 229,500 |
| Artillery Battalion | 5,000 | 2 | 90,000 |
| **Total** | | | **465,300 GSP** |

**Logistics vehicle requirements:**

- Standard Logistics Module: 500 GSP each
- Required modules: 465,300 / 500 = 931 logistics vehicles

This represents a significant logistics tail requiring dedicated transport capacity.

#### 2. Logistics Formation Design

Design dedicated logistics battalions for sustained campaigns:

**Logistics Battalion Template (example):**

| Element | Quantity | Module | GSP Capacity |
|---------|----------|--------|--------------|
| Logistics Vehicle (Light) | 200 | Standard (500 GSP) | 100,000 GSP |
| Logistics Infantry | 100 | Small (100 GSP) | 10,000 GSP |
| HQ Element | 1 | - | Command |
| **Total Capacity** | | | **110,000 GSP** |

**Logistics battalion placement:**

- Position at brigade HQ level (not individual combat battalions)
- Keeps logistics in rear echelon protected from frontline attrition
- Brigade-level logistics supplies all subordinate formations through hierarchy
- Vehicle-based logistics can supply other formations; infantry logistics cannot

#### 3. Resupply Operations

For campaigns exceeding initial supply:

**Resupply convoy planning:**

1. **Calculate deficit:** Total required GSP minus initial supply
2. **Design supply transports:** Freighters loaded with logistics formations
3. **Time convoy arrivals:** Schedule resupply before combat formations exhaust supply
4. **Establish supply points:** Land logistics formations at rear-echelon positions

**Supply chain security:**

- Maintain orbital superiority throughout the campaign
- Enemy raiders targeting supply convoys can starve your offensive
- Consider armed escorts for supply transports
- Stockpile excess logistics formations at the beachhead

#### 4. Combat Efficiency and GCL Bonus

Commanders with Ground Combat Logistics (GCL) bonus reduce supply consumption:

```
Effective GSP consumption = Base GSP x (1 - GCL bonus percentage)
```

A commander with 20% GCL reduces a formation's supply draw by 20%, effectively extending your logistics by 25%.

**Logistics optimization priorities:**

1. Assign high-GCL commanders to heavy formations (armored battalions consume the most GSP)
2. Position efficient formations on the front line
3. Rotate high-consumption formations to reserve when supply runs low
4. Accept reduced effectiveness (25% fire rate) rather than total supply exhaustion in emergencies

> **Tip:** Formations at 25% effectiveness due to supply exhaustion cannot assume front-line attack positions. If all your attack-capable formations run out of supply simultaneously, your offensive stalls. Always maintain a supply reserve and rotate formations to prevent simultaneous exhaustion.

---

### Extended Campaign Example: Fortress World

This scenario demonstrates advanced tactics against a heavily defended colony.

**Situation:**

- Target: Enemy fortress world with 200M population
- Defenses: 4 PDCs, estimated 40+ battalions, significant STO capability
- Terrain: Mountain (2.0 fortification modifier, 0.5 to-hit modifier)
- Your forces: 2 divisions (8 brigades), fleet superiority achieved

**Phase 1: PDC Suppression (Week 1)**

1. Conduct NBG missile bombardment on all 4 PDCs simultaneously
2. Allocate 500+ missiles per PDC; expect 60-70% to penetrate PD
3. Accept STO losses to bombardment ships (rotate damaged ships)
4. Continue until PDC shields depleted and weapons silenced

**Phase 2: Contested Landing (Week 1-2)**

1. Land 1st Division away from PDC positions in mountain valleys
2. Expect combat drop casualties of 10-15% against AA defenses
3. Immediately engage to prevent defender concentration
4. Establish FFD coordination with orbiting bombardment ships

**Phase 3: Sequential PDC Reduction (Weeks 2-4)**

1. Mass 2 brigades against PDC Alpha while 2 brigades screen
2. Heavy artillery bombardment from support positions
3. Armored breakthrough attempts to penetrate PDC perimeter
4. Once Alpha falls, advance to PDC Beta with accumulated forces

**Phase 4: Main Force Engagement (Weeks 4-8)**

1. With 2 PDCs eliminated, land 2nd Division as reinforcement
2. Engage main enemy field army with superior numbers
3. Use captured PDC positions as fortified logistics bases
4. Exploit breakthrough with armored divisions when morale breaks

**Phase 5: Mopping Up and Occupation (Weeks 8-12)**

1. Reduce remaining PDCs with concentrated force
2. Hunt down scattered enemy formations
3. Transition combat formations to occupation duty
4. Land garrison divisions for long-term control

**Logistics requirements for this campaign:**

- Initial assault supply: 400,000 GSP (2 divisions)
- 8-week sustainment: 1,200,000 additional GSP
- Resupply convoys: 3 convoys of 400,000 GSP each
- Reserve: 200,000 GSP emergency stockpile
- **Total logistics vehicles:** ~3,600 standard modules

---

## References

\hypertarget{ref-ex-ground-1}{[1]}. Aurora Forums and community documentation -- Occupation strength formula is not fully publicly documented. The interaction between population size, racial traits (Determination, Militancy, Xenophobia), political status modifiers, and governance type produces the required occupation tonnage. Practical garrison requirements verified through community gameplay reports.

---

## Related Sections

- [Section 13.1 Unit Types and Formation Design](../13-ground-forces/13.1-unit-types.md) -- Ground unit class design, formation templates
- [Section 13.2 Training, Logistics, and Transport](../13-ground-forces/13.2-training-and-transport.md) -- Construction, supply, transport bays
- [Section 13.3 Ground Combat](../13-ground-forces/13.3-ground-combat.md) -- Combat resolution, terrain, fortification, orbital support
- [Section 12.6 Damage and Armor](../12-combat/12.6-damage-and-armor.md) -- Orbital bombardment mechanics
- [Section 12.7 Planetary Defence Centres](../12-combat/12.7-planetary-defence-centres.md) -- PDC design and countering enemy PDCs
- [Appendix A: Formulas](../appendices/A-formulas.md) -- Unrest, occupation, and production calculations
- [Appendix C: Tips and Common Mistakes](../appendices/C-tips-and-mistakes.md) -- General gameplay advice
