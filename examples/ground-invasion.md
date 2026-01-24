# Example: Planning a Ground Invasion

This worked example walks through the process of planning, executing, and consolidating a ground invasion of an enemy colony. It demonstrates force composition calculations, transport logistics, orbital support coordination, and post-conquest occupation requirements.

## Starting Conditions

- **Target:** Enemy colony on Barnard's Star III, estimated population 50 million
- **Enemy Ground Forces:** Unknown composition, estimated 10-20 battalions based on thermal/EM signatures detected from orbit
- **Enemy Orbital Defenses:** 2 Planetary Defense Centers (PDCs) detected via active sensor sweep
- **Your Position:** Fleet has achieved orbital superiority; enemy naval forces have been destroyed or driven off
- **Your Available Forces:** 3 infantry regiments, 2 armored battalions, 1 artillery formation, 1 combat engineer battalion, plus transport and escort ships

---

## Step 1: Intelligence Gathering

Before committing forces, gather what information you can from orbit.

### What You Can Detect

Ground forces are treated as size-1 for detection purposes (Section 13.3.5). Their formation signature is calculated as:

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

### Occupation Strength Formula

From Appendix A, the required occupation strength to prevent unrest:

```
Required Occupation Strength = Population x ((Determination + Militancy + Xenophobia) / 300) x Political Status Modifier
```

### Calculating for This Scenario

Assume conquered population characteristics:

- Population: 50 million
- Determination: 60 (moderate)
- Militancy: 50 (average)
- Xenophobia: 40 (moderate -- they were already spacefaring)
- Political Status Modifier: varies by governance type

```
Required = 50,000,000 x ((60 + 50 + 40) / 300) x Political Status Modifier
         = 50,000,000 x (150 / 300) x Modifier
         = 50,000,000 x 0.5 x Modifier
         = 25,000,000 x Modifier (tons of occupation force)
```

This is the tonnage of ground forces required. With typical infantry at 5 tons per element and 300 elements per battalion:

```
Tons per infantry battalion = 5 x 300 = 1,500 tons
Battalions needed = 25,000,000 / 1,500 = ~16,667 battalions (absurd without modifier context)
```

**Important:** The formula produces a ratio. The actual Political Status Modifier and racial traits dramatically affect the real requirement. In practice, for a 50M population with moderate traits, 5-10 garrison battalions of infantry are typically sufficient to keep unrest manageable, especially with a commander providing a Ground Combat Occupation (OCC) bonus.

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

| Decision | Conservative Choice | Aggressive Choice | Recommendation |
|----------|-------------------|-------------------|----------------|
| Bombard first? | Targeted only (PDCs) | General bombardment | Targeted -- preserve infrastructure |
| Troop ratio | 5:1 | 3:1 minimum | 3:1 with orbital support |
| Landing method | Conventional (safe) | Combat drop (fast) | Conventional after PDC suppression |
| Speed vs mass | Full force, single lift | Fast light force, reinforce later | Single lift preferred |
| Occupation commitment | Minimal garrison | Heavy occupation force | Moderate -- enough to prevent unrest |

---

## Common Mistakes

1. **Insufficient transport capacity.** Calculate total tonnage carefully. Running short means multiple lifts, giving the defender time to react.

2. **Landing directly on PDCs.** PDCs have STO capability and will shred transports. Suppress them first with missile bombardment.

3. **Not enough occupation forces.** Unrest from insufficient occupation generates 100 points/year with no forces present. The colony becomes useless without adequate garrison.

4. **Forgetting to suppress orbital defenses.** STO weapons can engage your support ships. PDCs threaten transports. Neutralize these before committing vulnerable assets.

5. **Attacking without sufficient superiority.** The Forest terrain to-hit modifier (0.5x) combined with level-6 fortification means your base to-hit is ~1.67%. You need volume of fire, orbital support, and breakthrough-capable armor.

6. **Neglecting supply.** 10 rounds of inherent supply goes fast. Without logistics elements, formations drop to 25% effectiveness and cannot attack.

7. **Ignoring the FFD requirement.** Without Forward Fire Direction elements, your formations cannot receive orbital bombardment support or ground support fighter assistance. Include FFD in every combat formation template.

8. **Not planning for post-conquest.** Taking the colony is half the battle. Without garrison forces, a governor, and infrastructure support, the conquest is worthless.

---

## Related Sections

- [Section 13.1 Unit Types and Formation Design](../13-ground-forces/13.1-unit-types.md) -- Ground unit class design, formation templates
- [Section 13.2 Training, Logistics, and Transport](../13-ground-forces/13.2-training-and-transport.md) -- Construction, supply, transport bays
- [Section 13.3 Ground Combat](../13-ground-forces/13.3-ground-combat.md) -- Combat resolution, terrain, fortification, orbital support
- [Section 12.6 Damage and Armor](../12-combat/12.6-damage-and-armor.md) -- Orbital bombardment mechanics
- [Appendix A: Formulas](../appendices/A-formulas.md) -- Unrest, occupation, and production calculations
- [Appendix C: Tips and Common Mistakes](../appendices/C-tips-and-mistakes.md) -- General gameplay advice
