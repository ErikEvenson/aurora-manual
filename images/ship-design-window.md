# Ship Design Window Layout

The Class Design window is where all ship classes are created in Aurora C#. Accessed via the menu bar or keyboard shortcut, this window combines component selection, performance calculation, and design management into a single interface. Every ship in your fleet begins here as a collection of researched components arranged to fulfill a specific tactical role.

## Window Layout

```
+============================================================================+

|  [1] Class Design Window                                          [_][X]   |
+============================================================================+

|  Class Name: [2]__Tribal-class Destroyer_________  Race: [3] Terran Fed v  |
|  Hull Size: [4] 6,250 tons    Crew: [5] 142      Design Cost: [6] 892 BP  |
+----------------------------------+-----------------------------------------+

|  [7] AVAILABLE COMPONENTS        |  [8] DESIGN SUMMARY                     |
|  +----------------------------+  |  +-----------------------------------+  |
|  | Category: [9] All_______ v |  |  | Component          Qty  HS  Tons |  |
|  |                            |  |  |-----------------------------------|  |
|  | 10cm Infrared Laser     *  |  |  | 20cm C3 UV Laser    x4  16  800  |  |
|  | 12cm Infrared Laser        |  |  | Beam FC 96k/1280  x2   2  100  |  |
|  | 15cm Ultraviolet Laser     |  |  | Mag Confinement     x1   8  400  |  |
|  | 20cm C3 Ultraviolet Laser  |  |  | Fuel Storage        x3  12  600  |  |
|  | 25cm C3 Ultraviolet Laser  |  |  | Eng Spaces (30%)    x6  12  600  |  |
|  | Ion Engine 400 EP          |  |  | Duranium Armor      x1  20 1000  |  |
|  | Nuclear Pulse 250 EP       |  |  | Bridge              x1   1   50  |  |
|  | Beam Fire Control 96k      |  |  | --                       --  --- |  |
|  | Active Sensor S10          |  |  | TOTAL:                  125 6250 |  |
|  | Fuel Storage - Large       |  |  +-----------------------------------+  |
|  | Magazine (Standard)        |  |  [10] Add>>  <<Remove  Qty: [_1_]      |
|  | Engineering Spaces         |  |                                         |
|  | ...                        |  +-----------------------------------------+
|  +----------------------------+  |  [11] COMPONENT DETAIL                  |
|  [Scroll: 47 items]              |  +-----------------------------------+  |
|                                   |  | 20cm C3 Ultraviolet Laser         |  |
+----------------------------------+  | Size: 4 HS (200 tons)             |  |

|  [12] PERFORMANCE STATISTICS      |  | Damage: 20 at 0 km               |  |
|  +------------------------------+ |  | Range: 240,000 km (UV)            |  |
|  | Speed:     4,808 km/s        | |  | Rate of Fire: 10 sec              |  |
|  | Range:     12.4 B km         | |  | Power: 20                         |  |
|  | Endurance: 30 days           | |  | Crew: 40                          |  |
|  | Armor:     4 layers          | |  | Cost: 200 BP                      |  |
|  | Shield:    0                  | |  | Dev Cost: 4,000 RP                |  |
|  | Max Weapons Range: 240k km   | |  | Materials: Duranium 100           |  |
|  | Crew Quarters: Standard      | |  |            Corundium 100          |  |
|  | Maint Life: 2.1 years        | |  +-----------------------------------+  |
|  | Annual Failure: 14%          | |                                         |
|  | Power: 80/80 (100%)          | +-----------------------------------------+
|  +------------------------------+ |  [13] DESIGN CONTROLS                   |
|                                    |  +-----------------------------------+  |
+------------------------------------+  | [Save Design] [Load Design]       |  |

|  [14] ARMOR DISPLAY                |  | [Copy Design] [Delete Design]     |  |
|  +------------------------------+  |  | [Lock Design] [Rename]            |  |
|  | Layer 1: ##################  |  |  | [Obsolete]    [Show Costs]        |  |
|  | Layer 2: ##################  |  |  +-----------------------------------+  |
|  | Layer 3: ##################  |  |                                         |
|  | Layer 4: ##################  |  +-----------------------------------------+
|  | Width: 25 columns            |  |  [15] DESIGN NOTES                      |
|  | Strength: Duranium (5)       |  |  +-----------------------------------+  |
|  +------------------------------+  |  | Free-text notes for this design   |  |
|                                     |  | _________________________________  |  |
+-------------------------------------+  +-----------------------------------+  |
+============================================================================+
```

## Element Descriptions

**[1] Title Bar** -- Displays "Class Design" and standard window controls (minimize, close). The window can be resized to accommodate different screen resolutions.

**[2] Class Name Field** -- Editable text field for naming your ship class. Descriptive names (e.g., "Tribal-class Destroyer") help identify designs quickly across fleet management windows. Names can be changed at any time before locking the design.

**[3] Race Selector** -- Dropdown to select which race's technology pool to draw components from. In single-player, this is typically your own race. In SpaceMaster mode, any race's components are available.

**[4] Hull Size Display** -- Shows the total tonnage of the current design in tons. Updates dynamically as components are added or removed. This value determines whether the design fits within your shipyard's capacity.

**[5] Crew Count** -- Total crew required to operate this design. Derived from the sum of all component crew requirements. Crew quarters must be sufficient to house this number (standard, cramped, or luxury deployment).

**[6] Design Cost (Build Points)** -- Total BP required to construct one instance of this class. This determines construction time based on your shipyard's BP output per year.

**[7] Available Components Panel** -- Scrollable list of all components your race has researched and can install. Components are displayed with their key stats and can be filtered by category using the dropdown. An asterisk (*) indicates components already in the design.

**[8] Design Summary Panel** -- Shows all components currently included in the design with quantity, hull space (HS) used, and tonnage. The TOTAL row at the bottom provides a running sum. This is your primary reference for checking remaining capacity.

**[9] Category Filter Dropdown** -- Filters the available components list by type: All, Engines, Weapons, Sensors, Fire Controls, Armor, Shields, Magazines, Engineering, Fuel, Crew, Jump Drives, Hangars, Other. Speeds up component selection on designs with many available options.

**[10] Add/Remove Controls** -- The "Add>>" button adds the selected component from the Available list to the Design summary. "<<Remove" removes the selected component from the Design. The "Qty" field allows adding/removing multiple instances at once.

**[11] Component Detail Panel** -- Displays full specifications for the currently selected component (from either the Available or Design panel). Shows size, damage/capability, range, rate of fire, power requirements, crew, costs, development cost, and material breakdown.

**[12] Performance Statistics Panel** -- Automatically calculated summary of the design's key performance metrics. Updates in real-time as components are added or removed. Shows speed, range, endurance, armor layers, shields, maximum weapons range, crew quarters type, maintenance life, annual failure rate, and power balance (generated vs. consumed).

**[13] Design Controls** -- Buttons for managing the design:

- **Save Design**: Commits the current component list as a named class design
- **Load Design**: Opens a previously saved design for modification
- **Copy Design**: Duplicates the current design under a new name (useful for Mark II iterations)
- **Delete Design**: Permanently removes the design (cannot delete if ships of this class exist)
- **Lock Design**: Prevents further modifications (required before construction can begin)
- **Rename**: Changes the class name without affecting the design
- **Obsolete**: Marks the design as obsolete (hides from new construction lists)
- **Show Costs**: Toggles detailed mineral cost breakdown per component

**[14] Armor Display** -- Visual representation of the ship's armor layout. Shows the number of armor layers, column width (determined by hull size), and armor material strength. Each "#" represents an intact armor cell. This display uses the same layout as the combat damage display.

**[15] Design Notes** -- Free-text field for recording design intent, tactical doctrine, or revision history. Notes are saved with the design and visible in fleet management windows. Not mechanically significant but invaluable for remembering why you made specific choices months later.

## Common Workflows

### Adding an Engine

1. Set the **Category Filter [9]** to "Engines" to narrow the component list
2. Review available engine types in the **Available Components [7]** panel -- note EP (engine power), size, and fuel consumption
3. Select the desired engine and click **Add>> [10]** to add it to the design
4. Check **Performance Statistics [12]** for the resulting speed (speed = total EP / hull size in HS)
5. If speed is insufficient, add more engines or select a higher-power variant
6. Verify the **Power** line in Performance shows sufficient reactor output for all systems

### Setting Armor Layers

1. Set the **Category Filter [9]** to "Armor" to find armor components
2. Select the armor type (Duranium, Composite, Ceramic, etc.) -- higher-tech armors provide more protection per layer
3. Click **Add>> [10]** to add one layer of armor
4. Watch the **Armor Display [14]** update to show the new layer
5. Repeat to add additional layers -- each layer adds the same tonnage (determined by hull size and armor width)
6. Check **Performance Statistics [12]** -- armor adds mass, reducing speed unless engines compensate

### Checking Remaining Tonnage

1. Look at the **TOTAL** row in the **Design Summary [8]** panel
2. Compare the current total HS to your target hull size
3. The difference is your remaining capacity for additional components
4. Cross-reference with **Hull Size [4]** to see current total tonnage
5. If you exceed your target, remove components or accept the larger hull

### Designing a Point Defense Ship

1. Start with a small hull target (3,000-5,000 tons)
2. Add gauss cannon mounts (Category: Weapons) -- 2-4 per fire control
3. Add beam fire controls with **maximum tracking speed** (Category: Fire Controls)
4. Add engines for reasonable fleet speed (match your capital ships)
5. Add fuel for operational endurance
6. Add 2-3 armor layers for survivability
7. Add engineering spaces (10-15% of hull for escorts)
8. Verify power balance is positive in **Performance Statistics [12]**

## Tips and Shortcuts

- **Power balance** in the Performance panel must be positive (green). If negative, your reactors cannot power all systems simultaneously -- add a reactor or remove power-hungry components.

- **Maintenance life** below 1 year means your ship will frequently break down in service. Add more engineering spaces (5% minimum, 15%+ for extended deployments).

- **Locked designs** cannot be modified. If you need to change a locked design, use **Copy Design** to create an unlocked duplicate, modify it, then retool your shipyard to the new version.

- **Annual failure rate** above 20% indicates the design is maintenance-intensive. Consider reducing component count or adding engineering spaces.

- **Crew quarters** default to Standard deployment. If you see warnings about insufficient quarters, check whether you need to add crew quarter components or switch deployment type.

- **Component sorting**: The Available Components list sorts alphabetically within each category. Use the category filter to quickly find specific component types rather than scrolling through the full list.

- **Design iteration**: Use Copy Design liberally. Name copies with version suffixes ("Tribal Mk I", "Tribal Mk II") to track design evolution while preserving the original.

- **Checking tonnage fit**: Before saving a design, verify that your hull size does not exceed your largest available shipyard capacity. A design too large to build is useless until you expand a shipyard.

- **Power from engines**: Military engines generate power proportional to their size. If you need more reactor power, larger or additional engines provide it -- but watch fuel consumption.

## Components Tab

The Class Design window includes a **Components tab** that provides a percentage breakdown of the design by category, giving a high-level view of how tonnage and cost are distributed across the ship's systems.

**Category breakdown (percentage of total hull space):**

| Category | What it includes |
|---|---|
| Propulsion | Engines, fuel tanks |
| Beam Weapons | Lasers, railguns, gauss cannons, plasma carronades, mesons, particle beams |
| Essential Systems | Bridge, engineering spaces, crew quarters, life support |
| Defense | Armor, shield generators |
| Missiles | Missile launchers, magazines |
| Sensors | Active sensors, passive sensors (EM/TH), fire controls |
| Transport/Logistics | Cargo holds, troop transports, hangars, colony modules, fuel harvesting |

**Cost breakdown (displayed at bottom of Components tab):**

- **Class Cost** -- Total BP to build the hull and all installed components
- **Ordnance** -- Cost of missiles and other consumable munitions loaded at commissioning
- **Maintenance Supplies** -- Initial spare parts allocation based on engineering spaces and component complexity

The Components tab is useful for quickly identifying design imbalances -- for example, a "beam cruiser" where Beam Weapons account for only 8% of tonnage may need its weapon loadout revisited, or a frigate where Defense exceeds 40% might be over-armored for its role.

## Related Sections

- [Section 8.1 Design Philosophy](../8-ship-design/8.1-design-philosophy.md) -- Role-based design principles and size guidelines
- [Section 8.2 Hull and Armor](../8-ship-design/8.2-hull-and-armor.md) -- Armor mechanics and hull size considerations
- [Section 8.3 Engines](../8-ship-design/8.3-engines.md) -- Engine types, power, and fuel consumption
- [Section 8.4 Sensors](../8-ship-design/8.4-sensors.md) -- Active/passive sensors and fire controls
- [Section 8.5 Weapons](../8-ship-design/8.5-weapons.md) -- All weapon types and their design parameters
- [Section 8.6 Other Components](../8-ship-design/8.6-other-components.md) -- Fire controls, magazines, engineering spaces
- [Section 8.7 Design Examples](../8-ship-design/8.7-design-examples.md) -- Complete worked ship designs
- [Section 9.1 Shipyards](../9-fleet-management/9.1-shipyards.md) -- Building ships from completed designs
