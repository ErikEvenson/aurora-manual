# Shipyard Window Layout

*Added: v2026.01.25*

The Shipyard management interface is located within the Economics window (F2), under the Shipyard tab. This is where you manage all construction, expansion, retooling, and refit operations for your empire's shipyards. Each colony with shipyard complexes displays its yards here alongside their current tasks, capacity, assigned classes, and construction queues.

## Window Layout

```
+============================================================================+

|  [1] Economics - Shipyard Tab                                     [_][X]   |
+============================================================================+

|  Colony: [2] Earth_________________________ v     Population: 8.42 B       |
+============================================================================+

|  [3] SHIPYARD LIST                                                          |
|  +------------------------------------------------------------------------+|
|  | Name             | Type    | Capacity | Slips | Tooled Class   | Task  ||
|  |-------------------------------------------------------------------------|
|  |>Imperial NY #1   | Naval   | 12,000 t |   3   | Tribal DD      | Build ||
|  | Imperial NY #2   | Naval   |  8,000 t |   2   | Arrow FF       | Idle  ||
|  | Imperial NY #3   | Naval   |  6,000 t |   2   | (Retooling)    | Retool||
|  | Federation CY #1 | Commerc | 80,000 t |   4   | Atlas Freighter| Build ||
|  | Federation CY #2 | Commerc | 50,000 t |   2   | Hermes Tanker  | Idle  ||
|  | Orbital RY #1    | Repair  | 40,000 t |   2   | (Any class)    | Repair||
|  +------------------------------------------------------------------------+|
+============================================================================+

|                                                                             |
| +----------------------------------+  +-----------------------------------+ |
| | [4] CONSTRUCTION QUEUE           |  | [7] SHIP CLASS SELECTOR           | |
| | +------------------------------+ |  | +-------------------------------+ | |
| | | Imperial NY #1 - Slipway 1   | |  | | Available Classes:            | | |
| | |------------------------------|  |  | |-------------------------------|  | |
| | | Tribal DD (Hull #4)          | |  | | Tribal DD          6,250 t   | | |
| | | Progress: [==========>    ]  | |  | | Arrow FF           3,800 t   | | |
| | | 67% complete                 | |  | | Sentinel CL       12,400 t   | | |
| | | BP: 598/892   ETC: 4.7 mo   | |  | | Hawk Corvette      2,100 t   | | |
| | |                              | |  | | Atlas Freighter   45,000 t   | | |
| | | Imperial NY #1 - Slipway 2   | |  | | Hermes Tanker     32,000 t   | | |
| | |------------------------------|  |  | | Scout Frigate      4,500 t   | | |
| | | Tribal DD (Hull #5)          | |  | |                               | | |
| | | Progress: [====>          ]  | |  | | [Only show classes that fit]  | | |
| | | 34% complete                 | |  | +-------------------------------+ | |
| | | BP: 303/892   ETC: 8.8 mo   | |  |                                   | |
| | |                              | |  | [8] BUILD CONTROLS                | |
| | | Imperial NY #1 - Slipway 3   | |  | +-------------------------------+ | |
| | |------------------------------|  |  | | Qty: [__1]                    | | |
| | | (Empty - available)          | |  | | [Start Construction]          | | |
| | |                              | |  | | [Pause Build] [Cancel Build]  | | |
| | +------------------------------+ |  | | [Scrap Ship]                  | | |
| +----------------------------------+  | +-------------------------------+ | |
|                                       +-----------------------------------+ |
| +----------------------------------+  +-----------------------------------+ |
| | [5] CAPACITY & EXPANSION         |  | [9] RETOOLING                     | |
| | +------------------------------+ |  | +-------------------------------+ | |
| | | Current Capacity: 12,000 t   | |  | | Current Class: Tribal DD      | | |
| | | Slipways: 3                   | |  | | Retool To: [_____________  v] | | |
| | |                              | |  | |                               | | |
| | | EXPANSION OPTIONS:            | |  | | Similarity: N/A               | | |
| | | [+1,000t Capacity]  412 BP   | |  | | Retool Time: N/A              | | |
| | | [+1 Slipway]        600 BP   | |  | | Status: Tooled (ready)        | | |
| | | [Cont. Upgrade To:] [15000]  | |  | |                               | | |
| | |                              | |  | | [Begin Retool]                | | |
| | | Current Task: None           | |  | | [Cancel Retool]               | | |
| | | Task Progress: --            | |  | +-------------------------------+ | |
| | +------------------------------+ |  |                                   | |
| +----------------------------------+  +-----------------------------------+ |
|                                                                             |
| +----------------------------------+  +-----------------------------------+ |
| | [6] REFIT OPTIONS                |  | [10] SHIPYARD TASK QUEUE          | |
| | +------------------------------+ |  | +-------------------------------+ | |
| | | Refit From: [Tribal DD    v] | |  | | Priority | Task    | Status   | | |
| | | Refit To:   [Tribal DD II v] | |  | |---------|---------|----------|  | |
| | |                              | |  | | 1       | Build x2| Active   | | |
| | | Component Changes: 4         | |  | | 2       | +1 Slip | Queued   | | |
| | | Refit Cost:  224 BP (25%)    | |  | | 3       | +2000t  | Queued   | | |
| | | Refit Time:  3.2 months      | |  | | 4       | Retool  | Queued   | | |
| | | Ships Available: 2           | |  | |                               | | |
| | |                              | |  | | [Move Up] [Move Down]         | | |
| | | [Begin Refit] [Cancel Refit] | |  | | [Remove Task]                 | | |
| | +------------------------------+ |  | +-------------------------------+ | |
| +----------------------------------+  +-----------------------------------+ |
+============================================================================+

| [11] Status: Imperial NY #1 building Tribal DD. 400 BP/yr/slip. Workers:   |
|      2,500,000 required / 2,500,000 available. Mineral stockpile adequate. |
+============================================================================+
```

## Element Descriptions

**[1] Title Bar** -- The Shipyard tab is within the Economics window (F2). The Economics window contains multiple tabs; select "Shipyard" to access this interface.

**[2] Colony Selector** -- Dropdown listing all colonies with shipyard infrastructure. Selecting a colony displays its shipyards below. Only colonies with at least one shipyard complex appear in this list. Population is shown for workforce reference.

**[3] Shipyard List** -- Master list of all shipyards at the selected colony. Each row shows:

- **Name**: Shipyard identifier (auto-generated or user-renamed)
- **Type**: Naval, Commercial, or Repair
- **Capacity**: Maximum tonnage the yard can construct (determines largest ship class it can build)
- **Slips**: Number of slipways (simultaneous builds)
- **Tooled Class**: The ship class the yard is currently configured to build, "(Retooling)" if in transition, or "(Any class)" for repair yards
- **Task**: Current activity -- Build, Idle, Retool, Expand, Add Slipway, Repair

The currently selected shipyard (indicated by ">") populates all detail panels below.

**[4] Construction Queue** -- Shows all active and pending construction jobs for the selected shipyard, organized by slipway:

- **Hull identifier**: Class name and hull number (sequential per class)
- **Progress bar**: Visual indication of completion percentage
- **Percentage complete**: Numeric completion value
- **BP**: Build points applied / total required
- **ETC**: Estimated time to completion based on current BP generation rate
- **Empty slipways**: Shown as "(Empty - available)" indicating capacity for new orders

**[5] Capacity and Expansion Panel** -- Displays current yard specifications and expansion options:

- **Current Capacity**: Maximum ship size this yard can build (in tons)
- **Slipways**: Current slipway count
- **+1,000t Capacity** (Naval) / **+10,000t** (Commercial): Adds one increment of tonnage capacity. Shows BP cost. Each expansion is processed as a shipyard task.
- **+1 Slipway**: Adds one additional slipway. Shows BP cost. Does not interrupt current construction.
- **Cont. Upgrade To**: Sets a target capacity for Continual Capacity Upgrade. The upgrade task automatically stops when reaching this target, preventing indefinite expansion.
- **Current Task / Task Progress**: Shows any expansion task in progress and its completion status.

**[6] Refit Options Panel** -- Interface for upgrading existing ships to newer designs:

- **Refit From**: The current class of ships to be refitted
- **Refit To**: The target class (must be similar enough for refit; typically a Mark II of the same class)
- **Component Changes**: Number of components being swapped during the refit
- **Refit Cost**: BP cost as absolute value and percentage of full build cost (refits cost proportionally to the number of changes)
- **Refit Time**: Estimated duration based on BP cost and yard output
- **Ships Available**: Number of ships of the "From" class currently available for refit (must be at the colony)
- **Begin Refit / Cancel Refit**: Start or abort the refit process

**[7] Ship Class Selector** -- Lists all locked ship designs available for construction, filtered by the selected shipyard's type (Naval shows military classes, Commercial shows civilian classes):

- Shows class name and tonnage
- Classes exceeding the yard's current capacity are grayed out (cannot be built until capacity is expanded)
- **Only show classes that fit**: Checkbox to hide classes too large for current capacity
- The selected class determines what the "Start Construction" button builds

**[8] Build Controls** -- Buttons for managing construction orders:

- **Qty**: Number of ships to order in this batch
- **Start Construction**: Begins building the selected class in the next available slipway (or queues if all slipways are occupied)
- **Pause Build**: Suspends construction on the selected slipway (BP generation halts, resources freed)
- **Cancel Build**: Aborts construction entirely (partial resources lost)
- **Scrap Ship**: Breaks down a completed ship, recovering a portion of minerals

**[9] Retooling Panel** -- Controls for changing the shipyard's assigned class:

- **Current Class**: The class this yard is currently tooled to build
- **Retool To**: Dropdown of available classes to retool for
- **Similarity**: Percentage of shared components between current and target class (higher = faster retool)
- **Retool Time**: Estimated duration based on design difference (more changes = longer retool)
- **Status**: Current retooling state (Tooled, Retooling, or percentage complete)
- **Begin Retool**: Starts the retooling process (halts all current construction in this yard)
- **Cancel Retool**: Aborts retooling (yard reverts to previous class assignment)

**[10] Shipyard Task Queue** -- Priority-ordered list of all pending tasks for the selected yard:

- Tasks execute sequentially in priority order
- Includes builds, capacity expansions, slipway additions, and retooling
- **Move Up / Move Down**: Reorders task priority
- **Remove Task**: Cancels a queued task without affecting active tasks
- Active tasks cannot be reordered (must be cancelled to change sequence)

**[11] Status Bar** -- Summary information for the selected shipyard: current activity, BP generation rate per slipway, workforce requirements vs. availability, and mineral stockpile status. Warnings appear here if workforce is insufficient or minerals are depleted.

## Common Workflows

### Starting a New Build

1. Select the colony with your desired shipyard using the **Colony Selector [2]**
2. Click the appropriate shipyard in the **Shipyard List [3]** (must be tooled for the desired class)
3. Verify the **Construction Queue [4]** has an empty slipway available
4. In the **Ship Class Selector [7]**, click the class you want to build (must match the yard's tooled class)
5. Set **Qty [8]** to the number of ships desired
6. Click **Start Construction [8]** -- the first ship fills the empty slipway, additional ships queue
7. Monitor progress in the **Construction Queue [4]** -- ETC shows estimated completion date
8. Check the **Status Bar [11]** for workforce and mineral warnings

### Expanding Capacity

1. Select the shipyard needing expansion in the **Shipyard List [3]**
2. In the **Capacity and Expansion Panel [5]**, note the current capacity vs. your target ship class size
3. Calculate how many +1,000t increments you need (e.g., 8,000t yard to 12,000t = 4 increments for naval)
4. Click **+1,000t Capacity** (or +10,000t for commercial) -- this adds an expansion task to the queue
5. Repeat for each increment needed, or use **Cont. Upgrade To [5]** with your target tonnage for automatic sequential expansion
6. Expansion tasks appear in the **Shipyard Task Queue [10]** and process sequentially
7. The yard continues building ships during expansion -- only the next expansion increment requires yard attention
8. Once capacity meets or exceeds your target class tonnage, the yard can begin construction of larger ships

### Retooling for a New Class

1. Select the yard to retool in the **Shipyard List [3]**
2. Ensure all current construction is complete or cancelled (retooling halts all builds)
3. In the **Retooling Panel [9]**, select the new class from the **Retool To** dropdown
4. Review the **Similarity** percentage -- higher similarity means faster retooling:
   - Same hull with minor component changes: 80-90% similarity, very fast retool
   - Different ship same size: 30-50% similarity, moderate retool
   - Completely different class: 0-10% similarity, full retool time
5. Note the **Retool Time** estimate
6. Click **Begin Retool [9]** -- the yard enters retooling state
7. Monitor progress in the **Retooling Panel [9]** status field
8. Once complete, the yard is ready to build the new class

### Performing a Refit

1. Ensure the ship(s) to be refitted are at the colony with the appropriate shipyard
2. Select the shipyard in the **Shipyard List [3]** (must be tooled for either the old or new class)
3. In the **Refit Options Panel [6]**, select the "From" class (current design) and "To" class (upgraded design)
4. Review **Component Changes**, **Refit Cost**, and **Refit Time**
5. Verify **Ships Available** shows the hulls you want to upgrade
6. Click **Begin Refit [6]** -- the ship enters the slipway and components are swapped
7. Refit costs a fraction of full build cost proportional to the number of changed components
8. The refitted ship emerges as the new class with all unchanged components intact

## Tips and Shortcuts

- **Parallel construction** is the fastest way to build fleet tonnage. Adding slipways is more cost-effective than expanding capacity when your current ship classes fit the yard. Two slipways building destroyers produces more tonnage per year than one slipway building cruisers.

- **Retooling time estimates** depend on design similarity. To minimize retool time, design your Mark II variants to share as many components as possible with the original class. Same engines, same armor type, and same hull size dramatically reduce retooling duration.

- **Continual Capacity Upgrade** with a target value prevents the common mistake of accidentally expanding a yard far beyond your needs. Set the target to your largest planned hull class + 10-20% margin.

- **Workforce constraints** can silently reduce your build rate. Check the Status Bar [11] for workforce warnings. Naval yards require 250 workers per slipway per ton of capacity -- a 12,000t yard with 3 slipways needs 9 million workers. Colonies with insufficient population cannot fully staff large yards.

- **Commercial yards are 10x more tonnage-efficient** per cost than naval yards. If a design can be built commercially (no military components), always use a commercial yard.

- **Repair yards do not need retooling** -- they can repair any class. Keep at least one repair yard with capacity matching your largest ship class.

- **Queue management** in the Task Queue [10] lets you plan ahead. A common sequence: complete current builds, add a slipway, expand capacity by 2,000t, then retool for a new class. All queued in advance.

- **Scrap wisely**: Scrapping returns minerals but at a loss. Only scrap truly obsolete ships that have no garrison or training value. Consider converting old warships to training vessels first.

- **Multiple yards per class** provides insurance. If one yard is damaged or retooling, the other continues production. For critical warship classes, maintain at least two tooled yards.

- **Starting a game**: Immediately begin expanding your starting shipyard capacity and adding slipways. These investments compound throughout the entire game as fleet requirements grow. Early slipway additions pay for themselves many times over.

## References

\hypertarget{ref-img-shipyard-1}{[1]}. Aurora C# game database (AuroraDB.db v2.7.1) -- Shipyard mechanics verified against FCT\_Installations and DIM\_PlanetaryInstallation tables. Naval and Commercial shipyard types with distinct capacity and component restrictions.

---

## Related Sections

- [Section 9.1 Shipyards](../9-fleet-management/9.1-shipyards.md) -- Detailed shipyard mechanics (Naval vs Commercial, capacity formulas, workforce)
- [Section 9.2 Construction and Refit](../9-fleet-management/9.2-construction-and-refit.md) -- Build, refit, and scrap mechanics in depth
- [Section 6.1 Minerals](../6-economy-and-industry/6.1-minerals.md) -- Mineral resources consumed during construction
- [Section 6.3 Construction](../6-economy-and-industry/6.3-construction.md) -- Ground-based construction factories
- [Section 8.1 Design Philosophy](../8-ship-design/8.1-design-philosophy.md) -- Ship role design affecting yard type selection
- [Section 7.4 Tech Categories](../7-research/7.4-tech-categories.md) -- Shipyard Operations research (build rate improvements)
