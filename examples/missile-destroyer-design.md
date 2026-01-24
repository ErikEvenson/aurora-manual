# Example: Designing a Missile Destroyer

This worked example walks through designing a 6,000-ton missile destroyer optimized for long-range anti-ship strikes. We cover launcher selection, missile design, fire control configuration, magazine sizing, and point defense -- showing the reasoning and math behind every decision.

## Objective

Design a **6,000-ton missile destroyer** capable of:

- Engaging hostile warships at long range (4,000,000+ km) with anti-ship missiles
- Carrying enough ordnance for sustained engagements (30+ missile salvo capacity)
- Defending itself against incoming missile fire with point defense
- Operating as part of a destroyer flotilla (4-6 ships in a task group)

## Starting Conditions

- **TN Start**: Nuclear Thermal Engine technology (5 EP/HS), Pressurised Water Reactor
- **Missile Technology**: Size-1 launchers available, Magneto-Plasma engine (4x fuel efficiency)
- **Warhead**: Strength-4 warheads (4 damage per MSP of warhead)
- **Missile Agility**: Base agility tech (32 km/s^2 per MSP at speed divisor 1)
- **Active Missile Sensor**: Resolution-1 available (smallest warships), strength 10
- **Fire Control**: Missile FC with base range and tracking
- **Shipyard**: Naval yard capable of 6,000 tons

---

## Step 1: Missile Launcher Selection

The launcher size determines our missile size, which cascades into every other design decision. Key trade-offs:

| Launcher Size (HS) | Missile Size (MSP) | Reload Rate | Launcher Mass |
|---------------------|---------------------|-------------|---------------|
| 1 HS | 1 MSP | 30 sec base | 50 tons |
| 2 HS | 2 MSP | 30 sec base | 100 tons |
| 3 HS | 3 MSP | 30 sec base | 150 tons |
| 4 HS | 4 MSP | 30 sec base | 200 tons |

Larger missiles carry more warhead, fuel, and sensor -- but fewer fit on a small destroyer. For a 6,000-ton hull, we want the best balance of firepower per ton.

**Decision: Size-2 launchers (2 MSP missiles)**

Rationale:
- Size-1 missiles are too small for meaningful warhead + seeker + fuel
- Size-3 and Size-4 launchers consume too much tonnage on a destroyer
- Size-2 gives us a 2 MSP missile budget -- enough for a balanced anti-ship missile

> **Tip:** Size-1 missiles excel as point defense interceptors and area-denial weapons. Save them for dedicated PD platforms. Your anti-ship missiles should be at least size-2 for adequate range and damage.

---

## Step 2: Anti-Ship Missile Design

With 2 MSP of missile space, we must allocate between four components:

1. **Warhead** -- damage on impact
2. **Engine** -- speed (affects both time-to-target and defensive agility)
3. **Fuel** -- range at the given speed
4. **Seeker** -- terminal guidance (active sensor to acquire target)

### Component Budget (2 MSP Total)

```
Warhead:  0.4 MSP  -- Damage = 0.4 * 4 (warhead tech) = 1.6 damage per missile
Engine:   0.8 MSP  -- Speed and agility
Fuel:     0.5 MSP  -- Range
Seeker:   0.3 MSP  -- Terminal guidance sensor
------
Total:    2.0 MSP
```

### Warhead Analysis

At Strength-4 technology:
```
Warhead damage = Warhead_MSP * Warhead_Strength
               = 0.4 * 4 = 1.6 damage per missile
```

A single missile does 1.6 damage -- modest, but we are firing salvos of 8-12. Per salvo:
```
Salvo damage = 8 missiles * 1.6 damage = 12.8 damage
             = 12 missiles * 1.6 damage = 19.2 damage
```

Against a ship with 3 layers of Duranium armor (15 strength per column), a 12-missile salvo concentrating on a few columns will penetrate armor and damage internals.

### Engine Analysis

With Magneto-Plasma drive (4x fuel efficiency multiplier) and 0.8 MSP engine:
```
Missile speed = Engine_MSP * Engine_Power_Per_MSP * 1000 / Missile_Size
             = 0.8 * 12 * 1000 / 2
             = 4,800 km/s (estimated at starting engine tech)
```

Missile agility (for evading point defense; see Appendix A for full formula details):
```
Agility = Engine_MSP / Total_Missile_MSP * Agility_Tech_Modifier * 100
        = 0.8 / 2 * 32 * 100 / 100
        = 12.8 km/s^2
```

Note: At base agility tech, `Agility_Tech_Modifier` corresponds to 32 km/s^2 per MSP at speed divisor 1, giving `(0.8 / 2) * 32 = 12.8`.

> **Tip:** Missile speed serves double duty -- faster missiles both reach targets sooner (less time for PD to engage) and have higher agility (harder for PD to hit). Always prioritize engine allocation in missile design.

### Fuel Analysis

With 0.5 MSP fuel and Magneto-Plasma efficiency:
```
Fuel capacity = 0.5 * 2,500 litres (base per MSP) = 1,250 litres (estimated)
Range = Fuel / (Consumption_Rate) * Speed
```

At 4,800 km/s with efficient engines, estimated range: approximately 60 million km (60 Mkm). This provides engagement capability well beyond beam weapon range.

### Seeker Analysis

The active missile sensor at 0.3 MSP with Resolution-1, Strength-10:
```
Detection range = sqrt(Sensor_Strength * 0.3 * Target_HS) * 10,000 km
```

Against a 10,000-ton target (200 HS):
```
Detection = sqrt(3.0 * 200) * 10,000 = sqrt(600) * 10,000
          = 24.5 * 10,000 = 245,000 km
```

This is the missile's terminal acquisition range -- the distance at which its onboard sensor locks onto the target. The missile uses fire control guidance until it reaches this envelope, then switches to self-guidance.

### Final Missile Specification

```
ASM-2 "Javelin" Anti-Ship Missile
  Size: 2 MSP
  Speed: ~4,800 km/s
  Range: ~60 Mkm
  Damage: 1.6 per missile
  Agility: 12.8 km/s^2
  Seeker: Active, 245,000 km acquisition vs 10,000-ton target
  Cost: ~2 BP per missile
```

---

## Step 3: Fire Control Configuration

Missile fire controls determine how many missiles can be guided simultaneously and at what range they can be launched.

### FC Requirements

```
Missile FC Parameters:
  Range: Must exceed missile range (60+ Mkm)
  Resolution: Match expected target size
  Tracking Speed: Not critical for missile FC (missiles self-guide at terminal)
```

**Decision: 2x Missile Fire Controls at 4 HS each (200 tons each)**

Each FC can guide one salvo at a time. With 2 FCs:
- Fire first salvo on FC-1
- Fire second salvo on FC-2 while FC-1 guides first salvo
- By the time salvo 1 hits (or misses), FC-1 is free for salvo 3

This provides continuous fire capability without guidance gaps.

```
FC allocation: 2x 4 HS = 8 HS = 400 tons total
```

> **Tip:** Always carry at least 2 missile FCs on any dedicated missile ship. A single FC means you cannot fire again until the first salvo resolves -- a potentially fatal delay if the first salvo misses or the target has friends.

---

## Step 4: Launcher Count and Magazine Sizing

### Launcher Count

With size-2 launchers (2 HS = 100 tons each), how many can we fit?

Target: 8-missile salvos (a good balance between concentration and ammunition conservation)

**Decision: 8x Size-2 Missile Launchers**
```
Launcher tonnage: 8 * 100 = 800 tons (16 HS)
```

Eight launchers fire a full salvo every reload cycle. With base 30-second reload (reduced by technology), this gives sustained fire rate of one salvo per 30 seconds.

### Magazine Sizing

Each magazine holds missiles for reloading. We want enough for a sustained engagement:

```
Engagement scenario: 4-6 salvos before needing to withdraw for resupply
Missiles per salvo: 8
Total missiles needed: 8 * 5 = 40 missiles minimum

Magazine capacity at Size-2 missiles:
  Each magazine HS holds: 50/missile_size = 50/2 = 25 missiles per HS (estimated)

Target: 40 missiles
Magazine size needed: 40 / 25 = 1.6 HS (round up to 2 HS = 100 tons)
```

**Decision: 2x Magazine (1 HS each = 50 tons each, 100 tons total)**

This provides 50 reloads (approximately 6 full salvos plus spares). The two magazines provide redundancy -- if one is hit and explodes, half the ammunition survives.

> **Tip:** Magazine explosions are catastrophic. When a magazine is hit and detonates, ALL missiles inside contribute their warhead damage to your own ship. Two small magazines are always safer than one large magazine, even if slightly less tonnage-efficient.

---

## Step 5: Point Defense

A missile destroyer without point defense is vulnerable to counter-fire. We need at least basic self-defense capability.

### PD Options for a Destroyer

1. **CIWS (Close-In Weapon System)**: Automated, no FC needed, short range
2. **Beam PD (Turret-mounted small lasers)**: Longer range, requires FC and power
3. **PD Missiles (interceptors)**: Longest range, uses launchers and magazines

For a 6,000-ton destroyer with limited tonnage remaining, CIWS is the most tonnage-efficient choice.

**Decision: 2x CIWS-1 (Twin Gauss Cannon)**
```
CIWS specs:
  Size: 2 HS each (100 tons each)
  Tracking speed: 5,000 km/s (base)
  Rate of fire: 2 shots per 5-second increment
  Range: 10,000 km
  No FC or power required (self-contained)

Total PD allocation: 4 HS = 200 tons
```

Two CIWS provide overlapping defensive coverage. Against a 4-missile salvo incoming:
```
PD engagement window: ~2 seconds at closing speed of 5,000 km/s
Shots per CIWS: ~2 per 5-sec window
Hit chance vs agility-12 missile: approximately 30-40%
Expected kills: 2 CIWS * 2 shots * 0.35 = 1.4 missiles destroyed per salvo
```

This is modest defense -- enough to thin out small salvos but not stop a concentrated barrage. The destroyer relies on its task group's combined PD umbrella for serious missile defense.

> **Tip:** A flotilla of 4 destroyers with 2 CIWS each provides 8 CIWS total for area defense. Task group PD is calculated collectively -- ships protect each other. Design your PD around the flotilla, not individual ships.

---

## Step 6: Engine and Speed

A missile destroyer needs speed to maintain range advantage and retreat if engaged by beam ships.

**Target speed**: 3,500+ km/s (faster than most cruisers, able to dictate engagement range)

```
Ship size: 6,000 tons = 120 HS
Engine allocation: ~35% of tonnage = 2,100 tons = 42 HS
Split: 3x 14 HS engines (redundancy, HTK = sqrt(14) = 3.74 each)

With Nuclear Thermal at 5 EP/HS, 1.25x boost:
EP per engine = 14 * 5 * 1.25 = 87.5 EP
Total EP = 3 * 87.5 = 262.5 EP

Speed = 262.5 * 1000 / 120 = 2,188 km/s
```

That is below our 3,500 km/s target. Let us increase engine allocation to 45%:

```
Engine allocation: 45% = 2,700 tons = 54 HS
Split: 3x 18 HS engines (HTK = sqrt(18) = 4.24 each)

EP per engine = 18 * 5 * 1.25 = 112.5 EP
Total EP = 3 * 112.5 = 337.5 EP

Speed = 337.5 * 1000 / 120 = 2,813 km/s
```

Still below target. For a destroyer, we may need to accept lighter armor and push to 50%:

```
Engine allocation: 50% = 3,000 tons = 60 HS
Split: 3x 20 HS engines (HTK = sqrt(20) = 4.47 each)

EP per engine = 20 * 5 * 1.25 = 125 EP
Total EP = 3 * 125 = 375 EP

Speed = 375 * 1000 / 120 = 3,125 km/s
```

**Decision: 3x 20 HS engines, 50% tonnage allocation, 3,125 km/s**

This is a missile destroyer doctrine: speed over armor. We engage at range and run from beam ships.

---

## Step 7: Remaining Components

### Sensors

A missile destroyer needs an active sensor to detect targets for fire control lock:

```
Active Sensor: 3 HS (150 tons), Resolution 100
  Detects 10,000-ton ships at ~350,000 km
  Sufficient for missile FC targeting
```

### Armor

With 50% in engines and significant launcher/magazine space, armor must be minimal:

```
Armor: 2 layers Duranium
  Strength per column: 2 * 5 = 10
  Mass: approximately 750 tons
  Philosophy: survive glancing hits, not sustained beam fire
```

### Support Systems

```
Bridge: 50 tons (1 HS) -- mandatory
Engineering: 300 tons (6 HS, 5%) -- maintenance and repair
Fuel: 750 tons (15 HS) -- range for system operations
```

---

## Step 8: Final Design Summary

### Mass Budget

| Component | Mass (tons) | HS |
|-----------|------------|-----|
| Engines (3x 20 HS) | 3,000 | 60 |
| Missile Launchers (8x size-2) | 800 | 16 |
| Magazines (2x 1 HS) | 100 | 2 |
| Missile Fire Controls (2x 4 HS) | 400 | 8 |
| CIWS (2x 2 HS) | 200 | 4 |
| Active Sensor (1x 3 HS) | 150 | 3 |
| Armor (2 layers Duranium) | ~750 | -- |
| Fuel Tanks | 750 | 15 |
| Bridge | 50 | 1 |
| Engineering (5%) | 300 | 6 |
| **Total** | **~6,500** | -- |

**Over budget by ~500 tons.** Iteration needed:

1. Reduce fuel to 500 tons (10 HS) -- saves 250 tons, shorter range but acceptable for system defense
2. Reduce engineering to 4% (240 tons) -- saves 60 tons, slightly higher failure rate
3. Reduce to 1 magazine (50 tons) -- saves 50 tons, less redundancy but acceptable risk
4. Trim sensor to 2 HS (100 tons) -- saves 50 tons, shorter detection but FC provides targeting

**Revised total after trims: ~6,100 tons** -- within tolerance for the ship designer to handle.

### Final Performance

```
DD-6000 "Lancer" Missile Destroyer
  Tonnage: ~6,000 tons (120 HS)
  Speed: 3,125 km/s
  Armament: 8x Size-2 Missile Launchers (ASM-2 "Javelin")
  Magazines: 40+ missiles (5 full salvos)
  Fire Control: 2x Missile FC (continuous salvo capability)
  Point Defense: 2x CIWS-1
  Sensor: Active, resolution 100
  Armor: 2 layers Duranium (10 strength per column)
  Range: ~3.2 billion km
  Engine redundancy: 3 engines, HTK 4.47 each
```

### Flotilla Composition

The Lancer operates in flotillas of 4-6 ships:

```
4-ship flotilla:
  Total launchers: 32
  Salvo size: 32 missiles
  Salvo damage: 32 * 1.6 = 51.2 damage (devastating against cruiser armor)
  Total PD (collective): 8 CIWS
  Combined sensor coverage: overlapping detection zones
```

A 32-missile salvo every 30 seconds provides withering firepower. Against a 10,000-ton cruiser with 3 layers of armor (15 strength per column), concentrated hits will breach armor within 2-3 salvos and begin destroying internal components.

---

## Upgrade Path

### Near-Term Improvements

1. **Better warhead tech (Strength-6)**: Damage jumps from 1.6 to 2.4 per missile (+50%)
2. **Faster missile engines**: Higher speed means less PD engagement time and better agility
3. **Reduced-size launchers**: Technology reduces launcher size, freeing tonnage for more launchers or armor
4. **Better CIWS tracking**: Higher tracking speed dramatically improves PD hit chance

### Long-Term Redesign Triggers

- When Nuclear Pulse engines (8 EP/HS) are researched: same engine mass gives 5,000 km/s
- When size-3 launchers become practical: bigger missiles carry larger warheads
- When box launchers are available: pre-loaded launchers with no magazine needed (one-shot, but very tonnage-efficient for alpha strikes)

---

## Common Mistakes

1. **All warhead, no engine**: A missile with 1.5 MSP warhead and 0.5 MSP engine is slow, easy to intercept, and short-ranged. Balance is critical -- speed saves missiles from PD.

2. **No seeker on anti-ship missiles**: Without an onboard sensor, missiles require continuous FC guidance to impact. If the firing ship loses sensor lock (ECM, destruction, range), the missiles go ballistic and miss.

3. **Single magazine**: One magazine explosion destroys your entire ammunition supply AND deals catastrophic internal damage. Always split ordnance across multiple magazines.

4. **Forgetting reload time**: Launchers fire their loaded missile instantly but take 30+ seconds to reload from magazines. Plan your engagement around reload cycles, not instantaneous fire.

5. **PD neglect on missile ships**: "We engage at range, we do not need PD" fails the moment an enemy missile salvo reaches you. Even modest CIWS coverage saves ships.

6. **Speed neglect**: A missile destroyer caught at beam range dies quickly with only 2 layers of armor. Speed is your primary defense -- maintain range superiority at all times.

---

## Related Sections

- [Section 8.5 Weapons](../8-ship-design/8.5-weapons.md) -- Missile launcher types and sizes
- [Section 12.3 Missiles](../12-combat/12.3-missiles.md) -- Missile combat mechanics and guidance
- [Section 12.4 Point Defense](../12-combat/12.4-point-defense.md) -- CIWS and beam PD systems
- [Section 12.1 Fire Controls](../12-combat/12.1-fire-controls.md) -- Missile FC configuration and guidance limits
- [Section 9.3 Task Groups](../9-fleet-management/9.3-task-groups.md) -- Flotilla organization and collective PD
- [Section 14.1 Fuel](../14-logistics/14.1-fuel.md) -- Operational range planning
- [Appendix A: Formulas](../appendices/A-formulas.md) -- Missile damage, speed, and range calculations
