# Missile Design Window Layout

The Missile Design window is where all missile ordnance is created in Aurora C#. Missiles are measured in Missile Size Points (MSP), where each MSP equals 2.5 tons. The window allows you to allocate MSP across engine, warhead, fuel, agility, sensors, ECM, and other components, with performance calculations updating in real-time as you adjust allocations.

## Window Layout

```
+============================================================================+

|  [1] Missile Design                                               [_][X]   |
+============================================================================+

|  Missile Name: [2]__Javelin ASM Mk III___________  Race: [3] Terran Fed v  |
|  Total Size: [4] 6 MSP (15 tons, 0.20 HS)    Series: [5] Anti-Ship______  |
+----------------------------------+-----------------------------------------+

|  [6] MSP ALLOCATION              |  [7] PERFORMANCE SUMMARY                |
|  +----------------------------+  |  +-----------------------------------+  |
|  | COMPONENT        MSP   %   |  |  | Speed:      28,400 km/s          |  |
|  |----------------------------|  |  | Range:      184 M km              |  |
|  | Engine:     [__3.00] [50%] |  |  | Endurance:  107 minutes           |  |
|  | Warhead:    [__1.50] [25%] |  |  | Agility:    32 km/s^2            |  |
|  | Fuel:       [__0.75] [12%] |  |  | Damage:     6                     |  |
|  | Agility:    [__0.00] [ 0%] |  |  | Hit Chance: 72% (vs 5000 km/s)   |  |
|  | Active Snr: [__0.50] [ 8%] |  |  | ECM:        10% reduction         |  |
|  | ECM:        [__0.25] [ 4%] |  |  | Detection:  42,000 km             |  |
|  | ECCM:       [__0.00] [ 0%] |  |  | Seeker Res: 100 (anti-ship)       |  |
|  | Decoys:     [__0.00] [ 0%] |  |  | MR per Mag: 33 missiles           |  |
|  | Term Guide: [__0.00] [ 0%] |  |  | Cost:       3.71 BP               |  |
|  | Retarget:   [__0.00] [ 0%] |  |  +-----------------------------------+  |
|  | Geo Sensor: [__0.00] [ 0%] |  |                                         |
|  |                            |  +-----------------------------------------+
|  | Remaining:    0.00 MSP     |  |  [8] ENGINE CONFIGURATION               |
|  +----------------------------+  |  +-----------------------------------+  |
|                                   |  | Engine Tech: [Nuclear Pulse    v] |  |
+----------------------------------+  | Engine MSP:   3.00                |  |

|  [9] WARHEAD CONFIGURATION        |  | Boost Level:  [__2.0x]            |  |
|  +------------------------------+ |  | Max Boost:    2.0x (racial)       |  |
|  | Type: [Standard         v]   | |  | Fuel Mod:     1.00x (no penalty)  |  |
|  | Strength Tech: [Wrhd-3   v]  | |  | EP Output:    170.4               |  |
|  | Damage: 6 (1.5 MSP * Str 4)  | |  +-----------------------------------+  |
|  | Warhead Count: [__1]          | |                                         |
|  | Damage/Warhead: 6.000         | +-----------------------------------------+
|  +------------------------------+ |  [10] SENSOR CONFIGURATION              |
|                                    |  +-----------------------------------+  |
+------------------------------------+  | Type: [Active Sensor       v]     |  |

|  [11] EXISTING DESIGNS             |  | Resolution: [__100]               |  |
|  +------------------------------+  |  | Sensor Size: 0.50 MSP            |  |
|  | Name            Size  Spd    |  |  | Detection vs Res 100: 42,000 km  |  |
|  |------------------------------|  |  | Detection vs Size 6:  12,600 km  |  |
|  | Javelin ASM Mk I   6  22800  |  |  | EM Signature: 3                   |  |
|  | Javelin ASM Mk II  6  25600  |  |  +-----------------------------------+  |
|  |>Javelin ASM Mk III 6  28400  |  |                                         |
|  | Stiletto AMM        2  48000  |  +-----------------------------------------+
|  | Trident Heavy     12  18200  |  |  [12] DESIGN CONTROLS                   |
|  | Probe Survey       4      0  |  |  +-----------------------------------+  |
|  |                              |  |  | [Save Design] [New Design]        |  |
|  |                              |  |  | [Copy Design] [Delete Design]     |  |
|  |                              |  |  | [Rename]      [Show Materials]    |  |
|  +------------------------------+  |  +-----------------------------------+  |
+-------------------------------------+-----------------------------------------+

|  [13] MATERIAL BREAKDOWN            |  [14] DESIGN NOTES                     |
|  +--------------------------------+ |  +-----------------------------------+ |
|  | Duranium: 1.2  Tritanium: 0.8  | |  | Fast ASM for size-6 launchers.   | |
|  | Boronide: 0.5  Uridium:   0.3  | |  | Trades range for speed and ECM.  | |
|  | Corundium: 0.9                  | |  | Pair with Stiletto AMM escort.   | |
|  +--------------------------------+ |  +-----------------------------------+ |
+============================================================================+

|  [15] STATUS: Design valid. Fits Size 6 launcher. Magazine capacity: 33.   |
+============================================================================+
```

## Element Descriptions

**[1] Title Bar** -- Displays "Missile Design" with standard window controls. The window can be repositioned and resized.

**[2] Missile Name Field** -- Editable text field for naming the missile design. Use descriptive names that indicate role and generation (e.g., "Javelin ASM Mk III" for the third-generation anti-ship missile). Names appear in launcher assignment lists and ordnance production queues.

**[3] Race Selector** -- Dropdown selecting which race's technology pool to use for available engine, warhead, and sensor technologies.

**[4] Total Size Display** -- Shows the missile's total MSP allocation, weight in tons, and hull space equivalent. This determines what launcher size is required (a 6 MSP missile needs a size-6 or larger launcher). Updates dynamically as you adjust allocations.

**[5] Series Selector** -- Optional classification field for organizing missiles by role (Anti-Ship, Anti-Missile, Bombardment, Survey Probe, etc.). Used for filtering in other windows.

**[6] MSP Allocation Panel** -- The core of missile design. Each row represents a component category with an editable MSP value and percentage of total size. The "Remaining" counter at the bottom shows unallocated MSP. All fields accept fractional values (e.g., 0.75 MSP). Adjusting any value triggers recalculation of all performance figures.

**[7] Performance Summary Panel** -- Real-time calculated performance based on current MSP allocations and technology levels:

- **Speed**: Missile velocity in km/s (Engine EP / Total MSP)
- **Range**: Maximum distance before fuel exhaustion in millions of km
- **Endurance**: Time the missile can fly before running out of fuel
- **Agility**: Maneuverability in km/s^2 (affects hit probability against maneuvering targets)
- **Damage**: Total warhead damage on impact
- **Hit Chance**: Estimated probability against a target at specified speed
- **ECM**: Percentage reduction applied to enemy point defense accuracy
- **Detection**: Onboard sensor acquisition range at the missile's sensor resolution
- **Seeker Res**: Sensor resolution (determines what size target the seeker can acquire)
- **MR per Mag**: How many of this missile fit in a standard magazine
- **Cost**: Build point cost per missile

**[8] Engine Configuration Panel** -- Detailed engine settings:

- **Engine Tech**: Dropdown selecting the missile engine technology (Nuclear Pulse, Ion, Magneto-Plasma, etc.)
- **Engine MSP**: Amount of MSP devoted to the engine (mirrors the allocation panel value)
- **Boost Level**: Multiplier applied to engine output -- higher boost means more speed but exponentially more fuel consumption when exceeding racial max boost
- **Max Boost**: Your race's current maximum boost technology (exceeding this incurs fuel penalties)
- **Fuel Mod**: Current fuel consumption modifier (1.0x = no penalty, higher = exceeding max boost)
- **EP Output**: Effective engine power for this configuration

**[9] Warhead Configuration Panel** -- Warhead settings:

- **Type**: Standard, Laser, or Enhanced Radiation warhead
- **Strength Tech**: Current warhead strength technology level (determines damage multiplier per MSP)
- **Damage**: Calculated total damage (MSP * Strength)
- **Warhead Count**: Number of independent warheads (v2.2.0+) -- splits total damage across multiple attacks
- **Damage/Warhead**: Damage per individual warhead when using multiple warheads

**[10] Sensor Configuration Panel** -- Onboard missile sensor settings:

- **Type**: Active, Thermal, EM, Home-on-Jam, Geological, or None
- **Resolution**: Target size the sensor is calibrated to detect (1 = missile-size, 100+ = ship-size)
- **Sensor Size**: MSP allocated to the sensor (minimum 0.25 MSP for any effect)
- **Detection vs Res**: Detection range against targets matching the sensor's resolution
- **Detection vs Size**: Detection range against the missile's own size category (for reference)
- **EM Signature**: Electromagnetic emissions generated by the active sensor (makes the missile more detectable)

**[11] Existing Designs List** -- Scrollable list of all saved missile designs for the selected race. Shows name, size (MSP), and speed. The currently selected/loaded design is highlighted with ">". Double-click a design to load it for modification or review.

**[12] Design Controls** -- Buttons for managing missile designs:

- **Save Design**: Saves the current allocation as a named missile design
- **New Design**: Clears all allocations to start fresh
- **Copy Design**: Duplicates the current design under a new name (useful for Mk II iterations)
- **Delete Design**: Removes the design permanently (cannot delete if missiles of this type exist in magazines)
- **Rename**: Changes the missile name without affecting the design
- **Show Materials**: Toggles the material breakdown display

**[13] Material Breakdown** -- Shows the mineral costs per missile: Duranium, Tritanium, Boronide, Uridium, Corundium, and others as applicable. Visible when "Show Materials" is toggled on.

**[14] Design Notes** -- Free-text field for recording design intent, tactical pairing information, or version history.

**[15] Status Bar** -- Displays validation status, required launcher size, and magazine capacity. Warns if the design has issues (e.g., no engine, sensor below 0.25 MSP minimum, exceeding maximum missile size).

## Common Workflows

### Creating a New Anti-Ship Missile

1. Click **New Design [12]** to clear all fields
2. Set the **Total Size [4]** to match your launcher size (e.g., 6 MSP for size-6 launchers)
3. Allocate **Engine MSP [6]** to 40-50% of total size for a fast missile
4. Select your best **Engine Tech [8]** and set **Boost Level** at or below max boost to avoid fuel penalties
5. Allocate **Warhead MSP [6]** -- check that damage meets your needs in the **Performance Summary [7]**
6. Allocate **Fuel MSP [6]** -- watch the **Range** value in Performance to ensure the missile can reach expected engagement distances
7. Allocate **Active Sensor [6]** at 0.50 MSP minimum for reliable terminal acquisition
8. Set **Resolution [10]** to match expected target sizes (80-120 for capital ships)
9. Optionally add **ECM [6]** (0.25 MSP) to improve survivability against point defense
10. Verify **Remaining [6]** shows 0.00 MSP (all space allocated)
11. Name the missile and click **Save Design [12]**

### Adjusting Speed vs. Range

The fundamental trade-off: more engine MSP = faster missile but less room for fuel. To adjust:

1. Note current **Speed** and **Range** values in **Performance Summary [7]**
2. Increase **Engine MSP [6]** -- speed increases, but total fuel capacity decreases
3. Watch **Range** decrease as fuel MSP is reduced to accommodate the larger engine
4. Alternatively, increase **Fuel MSP [6]** at the expense of engine or warhead
5. The **Boost Level [8]** provides another lever -- higher boost increases speed without changing engine MSP, but incurs fuel consumption penalties above racial max boost
6. The sweet spot depends on tactical doctrine: alpha strike ships need speed, patrol missiles need range

### Adding ECM to a Missile

1. Allocate exactly **0.25 MSP** to **ECM [6]** -- this is the fixed cost regardless of ECM level
2. The ECM level applied is your race's current Missile ECM technology
3. Each ECM level provides 10% reduction to enemy energy weapon accuracy and 10% reduction to enemy MFC lock
4. Check the **ECM** line in **Performance Summary [7]** to verify the reduction percentage
5. The 0.25 MSP must come from somewhere -- typically reduce fuel or warhead slightly
6. For high-threat environments, also consider **Decoys [6]** (0.50 MSP each) which provide probabilistic defense against both PD beams and AMMs

### Designing an Anti-Missile Missile (AMM)

1. Set **Total Size [4]** to 1-2 MSP (small, to fit more in magazines)
2. Maximize **Engine MSP [6]** (60-70% of size) -- AMMs need extreme speed to intercept incoming missiles
3. Set a very small **Warhead [6]** (0.1-0.3 MSP) -- even fractional warhead strength >= 1.0 auto-kills missiles
4. Set **Fuel [6]** to the minimum needed for your PD engagement range (AMMs fire at short range)
5. Set **Active Sensor [6]** at 0.25 MSP minimum with **Resolution [10]** of 1 (anti-missile resolution)
6. No ECM needed (AMMs are not targeted by enemy PD)
7. Consider **Multiple Warheads [9]** to counter enemy decoys (v2.2.0+)

## Key Relationships

> **Note:** Understanding how missile parameters interact is critical for effective design:
>
> - **Engine MSP vs. Speed**: Speed = Engine EP / Total MSP. More engine = proportionally faster.
> - **Fuel MSP vs. Range**: Range depends on fuel amount divided by (consumption rate * speed). Faster missiles consume fuel faster, requiring more fuel MSP for equivalent range.
> - **Boost Level vs. Fuel Consumption**: Exceeding racial max boost applies a linear fuel penalty from 1x to 5x. A 4x boost with 2x max tech means 5x fuel consumption.
> - **Warhead MSP vs. Damage**: Damage = Warhead MSP * Warhead Strength tech. Higher tech multiplies all warhead investments.
> - **Sensor Size vs. Detection Range**: Detection scales with square root of (sensor sensitivity * target cross section). Doubling sensor MSP does not double detection range.
> - **ECM vs. Survivability**: Each ECM level = 10% harder to hit. But 0.25 MSP is a fixed cost regardless of level -- make sure your ECM tech is worth the investment.
> - **Decoys vs. PD**: Each decoy absorbs hits probabilistically. Multiple decoys dramatically reduce PD effectiveness but cost 0.50 MSP each.
> - **Total Size vs. Magazine Capacity**: Larger missiles store fewer per magazine. A 12 MSP missile takes 4x the magazine space of a 3 MSP missile.
> - **Launcher Match**: The missile must fit your launcher. Designing a 7 MSP missile when you only have size-6 launchers means you need to redesign or build new launchers.

## Tips and Shortcuts

- **Optimal warhead strengths** are perfect squares (1, 4, 9, 16, 25) due to the square damage profile applied to armor. A warhead strength of 9 creates a 3x3 damage pattern -- more efficient than 8 or 10.

- **No-engine missiles** (0 MSP to engine) create stationary buoys useful for sensor pickets. They cannot move but can carry sensors for persistent surveillance.

- **Minimum sensor size** is 0.25 MSP. Anything below this has no detection capability. This is a common mistake that wastes MSP.

- **Fractional warheads** (v2.2.0+) with strength < 1.0 have reduced kill probability against missiles. Ensure AMM warheads have at least 1.0 effective strength for guaranteed kills.

- **Active Terminal Guidance** (0.25 MSP, requires Uridium) provides an accuracy multiplier during final approach. The tech progression ranges from 20% to 90% bonus -- worth the MSP on expensive anti-ship missiles.

- **Retargeting** (0.50 MSP) lets a missile make multiple attack passes if it misses, persisting until fuel depletion. Excellent on expensive heavy missiles where each round is precious. Limited to one attempt per time increment (v2.5.0+).

- **Copy Design** is your friend for iteration. Load "Javelin Mk II", copy it, rename to "Mk III", adjust for new technology, save. This preserves the evolutionary history.

- **Magazine efficiency**: Smaller missiles pack more rounds per magazine. A fleet of size-2 AMMs stores 6x more rounds than size-12 ASMs in the same magazine space. Balance salvo weight against ammunition depth.

## Related Sections

- [Section 8.5 Weapons](../8-ship-design/8.5-weapons.md) -- Missile launchers, box launchers, and launcher sizing
- [Section 8.6 Other Components](../8-ship-design/8.6-other-components.md) -- Magazines and missile fire controls
- [Section 12.3 Missiles](../12-combat/12.3-missiles.md) -- Detailed missile combat mechanics
- [Section 12.4 Point Defense](../12-combat/12.4-point-defense.md) -- How missiles are intercepted
- [Section 12.5 Electronic Warfare](../12-combat/12.5-electronic-warfare.md) -- ECM and ECCM interactions
- [Section 7.4 Tech Categories](../7-research/7.4-tech-categories.md) -- Missile engine, warhead, and sensor research
