# Appendix D: Reference Tables

This appendix provides quick-reference data tables for minerals, installations, weapons, and technology progressions. Use these tables during ship design and colony planning to quickly look up costs, outputs, and key statistics.

## D.1 Trans-Newtonian Minerals

The eleven Trans-Newtonian minerals are the foundation of all advanced construction in Aurora (see [Section 6.1 Minerals](../6-economy-and-industry/6.1-minerals.md) for mining and exploitation). Each mineral has primary applications that determine where demand will be highest.

| Mineral | Primary Uses |
|---------|-------------|
| Duranium | Hull structure, basic construction, nearly everything |
| Neutronium | Shipyards, advanced armor, railguns |
| Corbomite | Shields, stealth systems, electronic warfare |
| Tritanium | Missile technologies, ordnance factories |
| Boronide | Power systems, capacitors, terraforming |
| Mercassium | Research labs, sensors |
| Vendarite | Gauss cannons, CIWS |
| Sorium | Fuel (after refining), fuel harvesters |
| Uridium | Sensors, fire control systems |
| Corundium | Energy weapons, mining installations |
| Gallicite | Engines (primary mineral for all engine types) |

**Planning Notes:**

- Duranium is consumed by virtually every project; prioritize accessible deposits early.
- Gallicite becomes a bottleneck once you begin building fleets; secure multiple sources.
- Sorium must be refined into fuel before use; raw Sorium has no direct application.
- Corundium demand scales with the number of energy weapon platforms in your navy.
- Mercassium is consumed in bulk by research labs (1,200 per lab); plan ahead for research expansion.

## D.2 Installation Specifications

For installation placement and colony management, see [Section 5.1 Establishing Colonies](../5-colonies/5.1-establishing-colonies.md).

### Key Installation Build Costs

| Installation | BP Cost | Mineral Cost | Workers Required |
|-------------|---------|--------------|-----------------|
| Maintenance Facility | 60 | 30 Duranium + 30 Neutronium | 50,000 |
| Research Lab | 2,400 | 1,200 Duranium + 1,200 Mercassium | 1,000,000 |
| Mine | 120 | 60 Duranium + 60 Corundium | 50,000 |
| Automated Mine | 240 | 120 Duranium + 120 Corundium | 5 (crew only) |
| Construction Factory | 120 | 60 Duranium + 60 Tritanium | 50,000 |
| Ordnance Factory | 120 | 60 Duranium + 60 Tritanium | 50,000 |
| Fuel Refinery | 120 | 60 Duranium + 60 Boronide | 50,000 |
| Terraforming Installation | 600 | 300 Duranium + 300 Boronide | 250,000 |
| Infrastructure | 2 | 1 Duranium + 1 Neutronium | varies |
| Mass Driver | 600 | 300 Duranium + 300 Neutronium | 50,000 |
| Ground Force Training Facility | 2,400 | 1,200 Duranium + 1,200 Neutronium | 500,000 |

### Installation Output Summary

| Installation | Base Output per Unit |
|-------------|---------------------|
| Mine | 1 ton/year per accessibility point |
| Automated Mine | 1 ton/year per accessibility point (no workers needed) |
| Construction Factory | 10 BP/year |
| Ordnance Factory | 10 BP/year (missiles only) |
| Fuel Refinery | 2,000 litres/year |
| Research Lab | 10 RP/year (base, modified by scientist skill) |

### Terraforming Installation Notes

- Mass: 125,000 tons per installation
- Worker requirement: 250,000 per installation
- Base terraform rate: 0.001 atm/year per installation
- Mineral cost is substantial; plan terraforming projects carefully

## D.3 Beam Weapon Quick Reference

For combat usage and tactical considerations, see [Section 12.2 Beam Weapons](../12-combat/12.2-beam-weapons.md).

### Beam Weapon Comparison Table

| Weapon | Example Config | Damage | ROF | Range | Size (HS) | Power | Cost (BP) | Key Mineral |
|--------|---------------|--------|-----|-------|-----------|-------|-----------|-------------|
| Laser | 20cm C5 UV | 10 | 10s | 400K km | 6 | 10 | 63 | Corundium |
| Railgun | 20cm V4/C4 | 4x4 | 15s | 160K km | 7 | 12 | 55 | Neutronium |
| Particle Beam | PB-4 | 4 | 10s | 200K km | 7 | 10 | 70 | Corundium |
| Meson Cannon | R20/C5 | 1* | 10s | 200K km | 6 | 10 | 20 | Corundium |
| Gauss Cannon | R3-100 | 1 | 3/5s | 30K km | 6 | 0 | 36 | Vendarite |
| Plasma Carronade | 30cm C5 | 24 | 25s | 240K km | 9 | 24 | 48 | Corundium |
| HPM | R20/C5 | 1 (3+) | 10s | 200K km | 6 | 10 | 126 | Corundium |
| CIWS | CIWS-160 | 1 | 6/5s | 10K km | 7.4 | 0 | 34 | Vendarite |

### Weapon Notes

- **Meson Cannon** (*): Bypasses both shields and armor entirely; damage is applied directly to internal components. Low damage per hit but extremely difficult to defend against.
- **Railgun** (4x4): Fires 4 shots per volley, each dealing 4 damage. Each shot ignores armor layers equal to its damage value.
- **HPM** (+): Deals 3 damage against shields but only 1 damage against armor/internals. Effective for shield-stripping roles.
- **Gauss Cannon**: Requires no power plant capacity. Rate of fire listed as shots-per-increment/increment-length (e.g., 3 shots per 5-second increment).
- **CIWS**: Self-contained point defense system with integrated sensor. Does not require a separate fire control or power plant.
- **Plasma Carronade**: Highest single-hit damage of any beam weapon but limited by short effective range.
- **Laser**: The most flexible beam weapon; scales well with focal size and capacitor technology.
- **Particle Beam**: No damage falloff at any range within maximum; good against heavily armored targets.

### Beam Weapon Scaling

All beam weapons scale with two key technologies:

1. **Calibre (Size)**: Larger weapons deal more damage but consume more hull space and power.
2. **Capacitor Recharge Rate**: Faster recharge reduces time between shots, increasing sustained DPS.

Focal size (for lasers) and velocity (for railguns) affect maximum range. Higher values extend range at the cost of increased component size.

## D.4 Technology Progression Tables

### Maintenance Capacity per Facility

| Tech Level | Capacity (tons/facility) | Research Cost (RP) |
|-----------|-------------------------|-------------------|
| 1 | 1,000 | 1,000 |
| 2 | 1,250 | 2,000 |
| 3 | 1,500 | 4,000 |
| 4 | 2,000 | 8,000 |
| 5 | 2,500 | 15,000 |
| 6 | 3,000 | 30,000 |
| 7 | 4,000 | 60,000 |
| 8 | 5,000 | 125,000 |
| 9 | 6,250 | 250,000 |

### MSP Production per Facility

| Tech Level | MSP/Year | Research Cost (RP) |
|-----------|----------|-------------------|
| 1 | 80 | 3,000 |
| 2 | 100 | 6,000 |
| 3 | 125 | 12,000 |
| 4 | 160 | 25,000 |
| 5 | 200 | 50,000 |
| 6 | 250 | 100,000 |
| 7 | 300 | 200,000 |
| 8 | 350 | 400,000 |
| 9 | 375 | 800,000 |
| 10 | 400 | 1,200,000 |

### Construction Rate (BP per Factory per Year)

| Tech Level | BP/Factory/Year | Research Cost (RP) |
|-----------|----------------|-------------------|
| Base | 10 | -- |
| Improved (1) | 12 | 2,000 |
| Advanced (2) | 16 | 8,000 |
| Expert (3) | 24 | 30,000 |
| Master (4) | 32 | 100,000 |

### Mining Production (Modifier per Mine)

| Tech Level | Production Modifier | Research Cost (RP) |
|-----------|-------------------|-------------------|
| Base | 1.0 | -- |
| Improved (1) | 1.2 | 2,000 |
| Advanced (2) | 1.44 | 8,000 |
| Expert (3) | 1.728 | 30,000 |
| Master (4) | 2.074 | 100,000 |

Each level multiplies the previous by 1.2x cumulatively.

### Fuel Refinery Output

| Tech Level | Output (litres/year/refinery) | Research Cost (RP) |
|-----------|------------------------------|-------------------|
| Base | 2,000 | -- |
| Improved (1) | 4,000 | 5,000 |
| Advanced (2) | 8,000 | 20,000 |
| Expert (3) | 16,000 | 80,000 |
| Master (4) | 32,000 | 300,000 |

## D.5 Key Design Formulas Quick Reference

This section condenses the most frequently-referenced formulas from [Appendix A: Formulas](../appendices/A-formulas.md) into a single lookup table for use during ship design (see [Section 8.1 Design Philosophy](../8-ship-design/8.1-design-philosophy.md)).

### Sensor Detection Ranges

| Sensor Type | Formula | Key Variable |
|------------|---------|--------------|
| Thermal (Passive) | Sensitivity x Target_Thermal x 10,000 km | Target engine power |
| EM (Passive) | Sensitivity x Target_EM x 10,000 km | Target active emissions |
| Active | sqrt(Strength x Cross_Section) x 10,000 km | Target size vs resolution |

**Active sensor effective range against off-resolution targets:**
```
Effective_Range = Base_Range x sqrt(Target_HS / Sensor_Resolution)
```

### Magazine Capacity

```
Magazine_Size (MSP) = Component_HS x 20 MSP per HS
Missiles_Stored = Magazine_MSP / Missile_MSP_Size
```

Each missile's MSP size is determined in the Missile Design window. Magazines are vulnerable to explosion if hit while loaded; consider:

- Spreading magazines across multiple components
- Using armored magazines (reduced capacity, +1 HTK)
- Accepting the risk on smaller ships where space is at a premium

### Shield Types

| Shield Type | Strength/Emitter | Fuel Consumption | EM Signature |
|------------|-----------------|-----------------|-------------|
| Standard | 1x tech level | High | High |
| Thermal Reduction | 1x tech level | High | Reduced |
| Absorption | 1x tech level | None while inactive | High when active |

**Shield regeneration:**
```
Regen_per_5s = Total_Shield_Strength x Regen_Rate_Tech
```

Shields must be active to regenerate. Active shields generate EM signature detectable by passive sensors.

### Engine Calculations

| Parameter | Formula |
|-----------|---------|
| Speed | Total_Engine_Power / Ship_Mass (tons) |
| Engine Power | Size (HS) x Power_per_HS x Boost_Modifier |
| Fuel/Hour | Total_EP x Consumption_Rate x Boost_Penalty |
| Range | Fuel_Capacity / Fuel_per_Hour x 3,600 x Speed |
| Boost Penalty | Approximately Boost^2 (1.5x = 2.25, 2x = 4, 3x = 9) |

**Practical design tip:** A 1.25x boost provides 25% more power with only ~56% more fuel consumption -- often the best efficiency trade-off for military vessels.

### Quick Conversion Reference

| Unit | Equivalence |
|------|------------|
| 1 HS | 50 tons |
| 1 MSP (missile) | 0.25 HS = 12.5 tons |
| 1 BP | 1 unit of production capacity |
| Speed 1 km/s | 1 EP per ton of ship mass |
| Magazine 1 HS | 20 MSP storage capacity |

## Related Sections

- [Section 6.1 Minerals](../6-economy-and-industry/6.1-minerals.md) -- Mineral extraction, production chains, and installation management
- [Section 7.1 Technology Tree](../7-research/7.1-technology-tree.md) -- Technology progression and research costs
- [Section 8.1 Design Philosophy](../8-ship-design/8.1-design-philosophy.md) -- Using these tables for ship component selection and optimization
- [Section 12.1 Fire Controls](../12-combat/12.1-fire-controls.md) -- Weapon damage, armor penetration, and shield mechanics in practice
- [Appendix A: Formulas](../appendices/A-formulas.md) -- Full mathematical derivations behind these reference values
