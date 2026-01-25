# Ground Forces Window Layout

*Added: v2026.01.25*

The Ground Forces window is the primary interface for designing, building, organizing, and managing all ground combat formations. It combines formation template design, unit class creation, training oversight, and transport management into a single multi-tabbed interface. Access it from the main toolbar or via the F12 shortcut.

## Window Layout

```
+==============================================================================+

| Ground Forces                                                     [_][O][X]  |
+==============================================================================+

| [Ground Unit Classes] [Formation Templates] [Order of Battle] [Unit Series]  |
|                       [Organization]        [Training]                        |
+------------------------------+-----------------------------------------------+

|                              |                                               |
|  [1] FORMATION LIST          |  [5] FORMATION DETAIL / TEMPLATE DESIGNER     |
|                              |                                               |
|  +------------------------+  |  +-------------------------------------------+|
|  | > 1st Infantry Regt    |  |  | Formation: 1st Infantry Regiment          ||
|  |   Location: Earth      |  |  | Template:  Standard Infantry Regt         ||
|  |   Strength: 100%       |  |  | Location:  Earth                          ||
|  | > 2nd Armoured Bde     |  |  | Commander: Col. J. Smith (GC: +15%)       ||
|  |   Location: Mars       |  |  +-------------------------------------------+|
|  |   Strength: 85%        |  |                                               |
|  | > 3rd Artillery Bn     |  |  [6] COMPONENT ELEMENTS                       |
|  |   Location: Earth      |  |  +-------------------------------------------+|
|  |   Strength: 100%       |  |  | Element         | Qty | Tons | GSP | HP   ||
|  | > 5th Construction Eng |  |  |-----------------|-----|------|-----|------||
|  |   Location: Luna       |  |  | Rifle Infantry  | 120 |  360 | 120 | 1200 ||
|  |   Strength: 72%        |  |  | HQ Infantry     |  12 |   48 |  -- |  120 ||
|  +------------------------+  |  | Heavy Infantry  |  36 |  144 | 864 |  360 ||
|                              |  | AA Infantry     |  24 |   96 | 576 |  240 ||
|  [2] FILTER / SORT           |  | Logistics Inf   |  18 |   72 |  -- |  180 ||
|  +------------------------+  |  | Combat Engineer |  12 |   48 |  -- |  120 ||
|  | Race: [Human       v]  |  |  +-------------------------------------------+|
|  | Location: [All     v]  |  |                                               |
|  | Template: [All     v]  |  |  [7] AGGREGATE STATS                          |
|  | [x] Show Garrison      |  |  +-------------------------------------------+|
|  | [ ] Sort by Creation   |  |  | Total Tonnage:    768 tons                 ||
|  +------------------------+  |  | Total GSP:        1,560                    ||
|                              |  | HQ Capacity:      800 tons                 ||
|  [3] TRAINING STATUS         |  | FFD Components:   4                        ||
|  +------------------------+  |  | CIWS Components:  0                        ||
|  | Grade: Regular         |  |  | STO Weapons:      0                        ||
|  | Progress: |||||||.. 70%|  |  | Construction CFE: 120                      ||
|  | Morale: 85/100         |  |  +-------------------------------------------+|
|  | Supply: 8/10 rounds    |  |                                               |
|  +------------------------+  |  [8] TRANSPORT STATUS                          |
|                              |  +-------------------------------------------+|
|  [4] ACTION BUTTONS          |  | Status:   UNLOADED (Garrison)              ||
|  +------------------------+  |  | Assigned: None                             ||
|  | [Build Formation]      |  |  | Capacity: 768 tons required                ||
|  | [Scrap Formation]      |  |  | Bay Type: Troop Transport (standard)      ||
|  | [Copy + Upgrade]       |  |  +-------------------------------------------+|
|  | [Copy Temp]            |  |                                               |
|  | [Instant Organisation] |  |                                               |
|  +------------------------+  |                                               |
|                              |                                               |
+------------------------------+-----------------------------------------------+

|  [9] UNIT CLASS DESIGNER (Ground Unit Classes Tab)                            |
|  +--------------------------------------------------------------------------+|
|  | Base Type: [Infantry     v]   Armor: [4  v]   Capabilities: [x] Mountain ||
|  | Component: [Anti-Personnel v]                                [ ] Jungle  ||
|  | Name:      [Rifle Infantry Mk II    ]        [ ] Boarding  [ ] Desert   ||
|  |                                               [ ] Genetic Enhancement    ||
|  | Size: 3.0 tons | HP: 10 | GSP: 1 | Cost: 3.2 BP                        ||
|  | Racial Armor: 5 (Duranium) | Racial Weapon: 4                           ||
|  | [x] Obsolete Comp (highlight outdated)                                   ||
|  +--------------------------------------------------------------------------+|
|                                                                              |
|  [10] BUILD QUEUE                                                            |
|  +--------------------------------------------------------------------------+|
|  | Template            | Population | Progress     | Completion   | BP Cost ||
|  |---------------------|------------|--------------|--------------|---------|
|  | Std Infantry Regt   | Earth      | ||||||||. 80%| 45 days      | 2,400   ||
|  | Armoured Battalion  | Mars       | |||...... 30%| 120 days     | 8,750   ||
|  | Artillery Battery   | Earth      | Queued       | 200 days     | 4,200   ||
|  +--------------------------------------------------------------------------+|
+==============================================================================+
```

## Element Descriptions

### [1] Formation List
The left panel displays all existing formations for the selected race. Each entry shows the formation name, current location (population/system body), and strength percentage. Formations below 100% strength have sustained losses and may need replacements. Click a formation to view its details in the center panel. Formations are displayed hierarchically -- parent formations show their subordinates as child nodes.

### [2] Filter / Sort Controls
Filters narrow the formation list by race, location, or template type. The "Show Garrison" checkbox includes garrison-duty formations that might otherwise be hidden. "Sort by Creation" orders formations by when they were built rather than alphabetically -- particularly useful when using Roman numeral ordinal naming (e.g., Infantry Regiment I, II, III) which does not sort alphabetically in a useful manner.

### [3] Training Status
Shows the selected formation's current training grade (Green, Regular, Veteran, Elite), training progress toward the next grade, morale level, and remaining inherent supply rounds. Each unit begins with supply for 10 combat rounds; logistics elements extend this. Training progresses automatically when the formation is stationed at a population with training facilities.

### [4] Action Buttons
- **Build Formation**: Adds a formation (from an existing template) to the build queue at the selected population.
- **Scrap Formation**: Destroys the selected formation, recovering 30% of wealth and mineral value. Wealth goes to the racial balance; minerals go to the parent population's stockpile.
- **Copy + Upgrade**: Duplicates the selected template with a year suffix and automatically generates upgraded unit classes when racial armor/weapon modifiers, tracking speed, or ECCM have changed. Creates Unit Series entries for automated replacement.
- **Copy Temp**: Duplicates a template exactly without modifying unit classes. Use for organizational copies.
- **Instant Organisation**: (SpaceMaster) Creates a formation immediately, consuming build points as of v2.3.1.

### [5] Formation Detail / Template Designer
The center-top panel shows identifying information for the selected formation: name, template it was built from, current location, and assigned commander with their ground combat bonus percentage. When on the Formation Templates tab, this area becomes the template editor where you define new formation blueprints.

### [6] Component Elements
A table listing every element type within the selected formation or template. Columns show the unit class name, quantity of units, aggregate tonnage, total Ground Support Points (GSP measures combat effectiveness), and combined hit points. Elements with "--" for GSP are non-combat units (HQ, logistics, construction). Orange-highlighted entries contain obsolete components; red entries contain alien-origin components.

### [7] Aggregate Stats
Summarizes the formation's total characteristics:

- **Total Tonnage**: Determines transport ship capacity requirements.
- **Total GSP**: Overall combat effectiveness rating.
- **HQ Capacity**: Command tonnage available (should match or exceed total tonnage).
- **FFD Components**: Number of Forward Fire Direction elements (each enables 6 ground support fighters + 1 orbital bombardment ship).
- **CIWS Components**: Planetary missile defense capacity.
- **STO Weapons**: Surface-to-orbit energy weapons for engaging orbital targets.
- **Construction CFE**: Construction Factory Equivalents for fortification work.

### [8] Transport Status
Displays whether the formation is currently loaded onto a transport vessel, unloaded as garrison, or in transit. Shows assigned transport ship (if any), tonnage required for loading, and the bay type needed (Troop Transport, Boarding Bay, or Drop Bay). This section is critical for planning planetary assaults and colony transfers.

### [9] Unit Class Designer
Accessed via the "Ground Unit Classes" tab. Design individual unit types by selecting a base type (Infantry through Ultra-Heavy Vehicle or Static Weapon), adding components to available slots, setting armor level, and selecting combat capabilities. The designer shows calculated size, hit points, GSP, and build point cost. The "Obsolete Comp" checkbox highlights classes containing components superseded by newer research (orange) or alien-origin components without research data (red).

### [10] Build Queue
Shows all formations currently under construction or queued. Displays the template being built, the population performing construction, progress percentage, estimated completion date, and total build point cost. Build priority can be reordered. Construction draws from the population's allocated build point budget (see [Section 6.3 Construction](../6-economy-and-industry/6.3-construction.md)).

## Common Workflows

### Designing a Formation Template

1. Navigate to the **Formation Templates** tab.
2. Click **New Template** and enter a name and abbreviation.
3. Set the default rank (used for automated commander assignment).
4. Select a previously designed Ground Unit Class from the class list.
5. Set the element quantity and click **Add Element**.
6. Repeat for each unit type needed (infantry, vehicles, HQ, FFD, logistics, construction, AA).
7. Review the aggregate stats panel to verify HQ capacity covers total tonnage.
8. Optionally enable Roman numeral ordinal numbering via the "Use Roman" checkbox.

### Building a New Formation

1. Select the desired **population** where construction will occur.
2. Click **Build Formation** in the action buttons panel.
3. Choose the **template** from the dropdown list.
4. The formation enters the build queue at the selected population.
5. Monitor progress in the Build Queue panel [10].
6. Once complete, the formation appears in the Formation List [1] at that location.

### Checking Training Status

1. Select a formation from the Formation List [1].
2. View the Training Status panel [3] for current grade and progress.
3. Formations at populations with training facilities progress automatically.
4. Training speed is modified by the assigned commander's Training bonus.
5. Higher training grades improve morale recovery, accuracy, and combat effectiveness.

### Loading Troops onto Transports

1. Ensure a transport ship with Troop Transport Bays is at the same population as the formation.
2. Select the formation and check Transport Status [8] for tonnage requirements.
3. Assign the transport to load the formation (via the Naval Orders system, Section 9).
4. Status changes from "UNLOADED" to "LOADED" with the assigned ship name.
5. For Class Default Ground Forces, ships automatically load matching formations at build completion.

### Upgrading Formations with Newer Technology

1. Research improved armor, weapons, or capabilities.
2. Select the original formation template.
3. Click **Copy + Upgrade** -- a new template is created with year suffix and upgraded unit classes.
4. New unit classes are automatically placed in Unit Series with their predecessors.
5. When formations take casualties, replacements draw the upgraded unit class from the Unit Series.

## Tips and Shortcuts

- **HQ Coverage Rule**: Always ensure HQ capacity (tons) matches or exceeds total formation tonnage. Formations without adequate HQ suffer proportional effectiveness penalties in combat.
- **Transport Budget**: Design formations with transport in mind. A 10,000-ton super-heavy vehicle formation requires enormous transport capacity. Consider whether the firepower justifies the logistical cost.
- **FFD Planning**: Include at least one FFD element per formation that will receive air or orbital support. Each FFD enables 6 ground support fighters and 1 bombardment ship. Without FFD, no external fire support is possible.
- **Supply Autonomy**: Each unit has inherent supply for only 10 combat rounds. For sustained operations, include logistics elements. Vehicle-based logistics can supply other formations; infantry logistics can only supply their own.
- **Mixed Arms**: Combine anti-personnel elements (for infantry targets) with anti-vehicle elements (for armor). Pure infantry formations are cheap but vulnerable to armor; pure armor is expensive and lacks garrison flexibility.
- **Construction Elements**: Include combat engineers if you need fortification beyond self-fortification levels. Vehicles can only reach their maximum fortification (level 2-3) with external construction support.
- **Obsolete Component Checking**: Periodically enable the "Obsolete Comp" checkbox in the Unit Class Designer to identify designs that have fallen behind your current technology. Orange = outdated, Red = alien/unresearched.
- **Drag-and-Drop Reorganization**: On the Order of Battle tab, drag element nodes between formations at the same location to reorganize without rebuilding. Enable "Amount Popup" for partial transfers.
- **Roman Numerals**: For thematic naming (Infantry Regiment I, II, III), enable the "Use Roman" checkbox on the template. Use "Sort by Creation" to keep them in logical order.

## Related Sections

- [Section 6.3 Construction](../6-economy-and-industry/6.3-construction.md) -- Build point allocation for formation construction
- [Section 7.4 Tech Categories](../7-research/7.4-tech-categories.md) -- Ground combat technology research tree
- [Section 9.3 Task Groups](../9-fleet-management/9.3-task-groups.md) -- Transport ship orders for troop movement
- [Section 12.6 Damage and Armor](../12-combat/12.6-damage-and-armor.md) -- Ground combat mechanics
- [Section 13.1 Unit Types](../13-ground-forces/13.1-unit-types.md) -- Detailed unit design and formation template rules
- [Section 13.2 Training and Transport](../13-ground-forces/13.2-training-and-transport.md) -- Training grades and transport bay types
- [Section 16.2 Skills and Bonuses](../16-commanders/16.2-skills-and-bonuses.md) -- Commander ground combat and training bonuses
- [Appendix D: Reference Tables](../appendices/D-reference-tables.md) -- Ground unit component stat tables
