# Research Window Layout

The Research window is the primary interface for managing your empire's technological development. It provides access to all research categories, available technologies, scientist assignments, lab allocations, and project progress tracking. Effective use of this window is essential for directing your empire's long-term strategic direction.

---

## Window Layout Diagram

```
+==============================================================================+
|  Research Window                                                       [X]   |
+==============================================================================+
|                                                                              |
| +--------------------+ +--------------------------------------------------+ |
| | [1] Research        | | [3] Available Technologies                      | |
| |     Category List   | | +----------------------------------------------+ | |
| |                     | | | Technology Name              RP Cost  Status  | | |
| | > Biology/Genetics  | | | -------------------------------------------- | | |
| |   Construction/Prod | | | Nuclear Thermal Engine       2,000   Avail.  | | |
| |   Defensive Systems | | | Nuclear Pulse Engine         5,000   Avail.  | | |
| |   Energy Weapons    | | | Ion Drive                   10,000   Locked  | | |
| | * Power/Propulsion  | | |   (Requires: Nuclear Pulse Engine)            | | |
| |   Kinetic Weapons   | | | Magneto-Plasma Drive        20,000   Locked  | | |
| |   Logistics/Ground  | | |   (Requires: Ion Drive)                       | | |
| |   Missiles/Torpedoes| | | Mag. Conf. Fusion Drive     35,000   Locked  | | |
| |   Sensors/Fire Ctrl | | |   (Requires: Magneto-Plasma Drive)            | | |
| |                     | | | Inertial Conf. Fusion Drv   50,000   Locked  | | |
| | [2] Category        | | |   (Requires: Mag. Conf. Fusion Drive)         | | |
| |     Filter          | | | -------------------------------------------- | | |
| | ( ) All             | | | Pressurised Water Reactor    2,000   Avail.  | | |
| | ( ) Available Only  | | | Pebble Bed Reactor           5,000   Avail.  | | |
| | (*) Show Locked     | | | Magnetic Mirror Fusion Rx   10,000   Locked  | | |
| | [ ] Show Next Tech  | | |   (Requires: Pebble Bed Reactor)              | | |
| | [ ] Obsolete        | | | -------------------------------------------- | | |
| | [ ] Prototype       | | | Fuel Consumption: 0.8       3,000   Avail.  | | |
| |                     | | | Fuel Consumption: 0.7       8,000   Locked  | | |
| +--------------------+ | | -------------------------------------------- | | |
|                         | | (Selected category technologies shown)        | | |
|                         | +----------------------------------------------+ | |
|                         +--------------------------------------------------+ |
|                                                                              |
+------------------------------------------------------------------------------+
|                                                                              |
| +--------------------------------------------------------------------------+|
| | [5] Current Research Projects                                             ||
| | +------------------------------------------------------------------------+|
| | | # | Project              | Scientist       | Labs | RP/yr | Progress   ||
| | | --+----------------------+-----------------+------+-------+----------- ||
| | | 1 | Nuclear Pulse Engine | Dr. Yamamoto    |  12  | 1,560 | |||||| 62%||
| | |   |                      | P&P +30%, Adm15 |      |       | ETA: 1.2yr||
| | | --+----------------------+-----------------+------+-------+----------- ||
| | | 2 | Construction Rate 3  | Prof. Martinez  |   8  |   960 | |||... 38% ||
| | |   |                      | C&P +20%, Adm10 |      |       | ETA: 3.2yr||
| | | --+----------------------+-----------------+------+-------+----------- ||
| | | 3 | Research Rate 2       | Dr. Singh       |   6  |   780 | ||.... 22% ||
| | |   |                      | C&P +15%, Adm20 |      |       | ETA: 2.8yr||
| | | --+----------------------+-----------------+------+-------+----------- ||
| | | 4 | 12cm UV Laser         | Dr. Petrova     |   6  |   780 | |..... 12% ||
| | |   |                      | EW +25%, Adm10  |      |       | ETA: 4.5yr||
| | +------------------------------------------------------------------------+|
| +--------------------------------------------------------------------------+|
|                                                                              |
+------------------------------------------------------------------------------+
|                                                                              |
| +-------------------------------+ +----------------------------------------+|
| | [6] Scientist List            | | [8] Lab Allocation Controls           ||
| | +---------------------------+ | | +------------------------------------+ ||
| | | Name          Field  Bonus| | | | Selected Project:                  | ||
| | |              Adm    Age   | | | | [Nuclear Pulse Engine         v]   | ||
| | | -------------------------  | | | |                                    | ||
| | | Dr. Yamamoto  P&P   +30% | | | | Assigned Labs: [12]  Max Eff: 15   | ||
| | |              15     42   | | | | [+1] [+5] [+All] [-1] [-5] [-All]  | ||
| | | Prof. Martinez C&P  +20% | | | |                                    | ||
| | |              10     55   | | | | Total Labs on Colony: 32            | ||
| | | Dr. Singh     C&P   +15% | | | | Unallocated Labs: 0                | ||
| | |              20     38   | | | | [Assign New: [x]]                  | ||
| | | Dr. Petrova   EW    +25% | | | |                                    | ||
| | |              10     47   | | | | [9] Effective Output                | ||
| | | *Unassigned*  Def   +35% | | | | Labs at full efficiency: 12/15     | ||
| | | Dr. Okafor             | | | | Labs at reduced efficiency: 0       | ||
| | |              25     33   | | | | Scientist Bonus: +30%               | ||
| | | *Unassigned*  Bio   +10% | | | | RP per lab: 100/yr (base)           | ||
| | | Dr. Kim                | | | | Effective RP/yr: 1,560               | ||
| | |              15     61   | | | +------------------------------------+ ||
| | +---------------------------+ | +----------------------------------------+|
| |                               |                                           |
| | [7] Scientist Details         | [10] Research Queue                       |
| | Selected: Dr. Yamamoto        | +----------------------------------------+|
| | Field: Power & Propulsion     | | Queue for Dr. Yamamoto:                ||
| | Bonus: +30%                   | | 1. Nuclear Pulse Engine (in progress)  ||
| | Admin Rating: 15              | | 2. Ion Drive (queued)                  ||
| | Age: 42 (Est. 20+ yrs left)  | | 3. Magneto-Plasma Drive (queued)       ||
| | Secondary: None               | | [Add to Queue] [Remove] [Move Up/Dn]  ||
| | Status: Assigned              | +----------------------------------------+|
| +-------------------------------+                                           |
|                                                                              |
+------------------------------------------------------------------------------+
|                                                                              |
| +--------------------------------------------------------------------------+|
| | [11] Technology Prerequisites Display                                     ||
| | +------------------------------------------------------------------------+|
| | | Selected: Ion Drive (10,000 RP)                                        ||
| | |                                                                         ||
| | | Prerequisites:                                                          ||
| | |   [x] Conventional Engine (Complete)                                    ||
| | |   [x] Nuclear Thermal Engine (Complete)                                 ||
| | |   [ ] Nuclear Pulse Engine (In Progress - 62%)                          ||
| | |                                                                         ||
| | | Unlocks:                                                                ||
| | |   Magneto-Plasma Drive (20,000 RP)                                      ||
| | |   Ion Drive Components (Ship Designer)                                  ||
| | +------------------------------------------------------------------------+|
| +--------------------------------------------------------------------------+|
|                                                                              |
| +--------------------------------------------------------------------------+|
| | [12] Completed Technologies Log                      [Filter: ________]  ||
| | +------------------------------------------------------------------------+|
| | | Year  | Technology                | Category        | Scientist        ||
| | | 2048  | Conventional Engine       | Power/Propulsion| (Starting Tech)  ||
| | | 2049  | Construction Rate 2       | Const/Production| Prof. Martinez   ||
| | | 2049  | Nuclear Thermal Engine    | Power/Propulsion| Dr. Yamamoto     ||
| | | 2050  | Mining Production 2       | Const/Production| Dr. Singh        ||
| | | 2050  | Research Rate 1           | Const/Production| Dr. Singh        ||
| | +------------------------------------------------------------------------+|
| +--------------------------------------------------------------------------+|
|                                                                              |
| [13] Status: 4 Active Projects | 32 Labs | 6 Scientists (4 assigned)        |
+==============================================================================+
```

---

## Prototype Controls Detail

```
+----------------------------------------------------+
| [14] Create Research Project / Prototype Controls   |
| +------------------------------------------------+ |
| | Selected Technology: Nuclear Pulse Engine       | |
| |                                                 | |
| | Actions:                                        | |
| | [Create Project]  -- Assign to research queue   | |
| | [Prototype]       -- Create (P) component now   | |
| |                                                 | |
| | Options:                                        | |
| | [x] Show Next Tech  -- Reveal next tier (FP)   | |
| | [ ] Show Obsolete                               | |
| |                                                 | |
| | Prototype Status Key:                           | |
| |   (P)  = Current Prototype (instant, no build) | |
| |   (FP) = Future Prototype (next tier, no build)| |
| |   (RP) = Research Prototype (queued + usable)   | |
| +------------------------------------------------+ |
+----------------------------------------------------+
```

---

## Numbered Element Descriptions

| # | Element | Description |
|---|---------|-------------|
| 1 | Research Category List | The nine research categories. Click a category to filter the Available Technologies list to show only technologies in that field. The active category is marked with an asterisk (*). Categories: Biology/Genetics, Construction/Production, Defensive Systems, Energy Weapons, Power/Propulsion, Kinetic Weapons, Logistics/Ground Combat, Missiles/Torpedoes, Sensors/Fire Control. |
| 2 | Category Filter | Radio buttons and checkboxes to control what technologies appear in the Available Technologies list. "Available Only" hides locked techs. "Show Locked" displays the full prerequisite chain. "Show Next Tech" reveals the next tier for prototype creation (FP). "Obsolete" and "Prototype" toggles filter by component status. |
| 3 | Available Technologies | The central technology list for the selected category. Shows technology name, RP cost, and availability status. Locked technologies display their prerequisite requirements in italics below the entry. Technologies are organized into logical groups (engines, reactors, fuel efficiency, etc.) separated by dividers. |
| 4 | Technology Cost and Status | Each technology entry shows its Research Point cost and current status: Available (can be researched now), Locked (prerequisites incomplete), In Progress (currently being researched), or Complete (already researched). |
| 5 | Current Research Projects | Active research projects across all categories. Shows the technology being researched, assigned scientist (with their field, bonus, and admin rating), number of labs allocated, effective RP per year, progress bar with percentage, and estimated time to completion (ETA). |
| 6 | Scientist List | All scientists in your empire, showing name, research field specialization, bonus percentage, administration rating, and current age. Unassigned scientists are marked and available for project assignment. Assigned scientists show their current project. |
| 7 | Scientist Details | Expanded information for the selected scientist: full name, specialization field, bonus percentage, administration rating (max labs at full efficiency), estimated remaining lifespan, secondary field (if any), and current assignment status. |
| 8 | Lab Allocation Controls | Interface for assigning research labs to the selected project. Shows currently assigned lab count, maximum efficient labs (scientist's admin rating), and buttons to add/remove labs in increments of 1, 5, or all. Also shows total colony labs and unallocated lab count. The "Assign New" checkbox automatically allocates newly-built labs to this project. |
| 9 | Effective Output | Calculated research output for the current project: labs at full efficiency vs. reduced efficiency (beyond admin cap), scientist bonus multiplier, base RP per lab per year, and total effective RP/year. This is the actual production rate driving the progress bar and ETA. |
| 10 | Research Queue | The ordered list of technologies queued for a specific scientist. When the current project completes, the scientist automatically begins the next queued technology. Controls allow adding technologies to the queue, removing entries, and reordering priority. |
| 11 | Technology Prerequisites Display | Detailed prerequisite chain for a selected technology. Shows each required technology with completion status (checkmark for complete, progress percentage for in-progress, empty for not started). Also shows what the selected technology unlocks when completed. |
| 12 | Completed Technologies Log | Historical record of all technologies your empire has researched. Shows completion year, technology name, research category, and the scientist who led the project. Filterable by text search. Useful for tracking research progression and identifying gaps. |
| 13 | Status Bar | Summary line showing total active research projects, total labs on the current colony, total scientists in empire, and how many are currently assigned to projects. Quick reference for overall research capacity utilization. |
| 14 | Prototype Controls | Interface for creating prototype components without full research. "Create Project" initiates formal research. "Prototype" creates an instantly-available (P) component for ship design experimentation. "Show Next Tech" enables future prototype (FP) creation using next-tier technology not yet researched. |

---

## Common Workflows

### Starting a New Research Project

1. Open the Research window.
2. Select a **Research Category** [1] from the left panel (e.g., Power/Propulsion).
3. Review the **Available Technologies** list [3]. Technologies marked "Avail." can be researched immediately; "Locked" ones require prerequisites.
4. Click on an available technology to select it.
5. Check the **Technology Prerequisites Display** [11] to confirm all prerequisites are met.
6. Click "Create Project" in the **Prototype Controls** [14] (or assign directly if using the project assignment interface).
7. The technology appears in the **Current Research Projects** panel [5] awaiting a scientist and labs.
8. Assign a scientist and allocate labs (see workflows below).

### Assigning a Scientist

1. Review the **Scientist List** [6] for unassigned scientists (marked with asterisk).
2. Click a scientist to see their **Scientist Details** [7]: field, bonus, admin rating, age.
3. Match the scientist's field to the project's category for maximum bonus. A Power/Propulsion specialist assigned to an engine project gets their full bonus; assigned elsewhere, they get no field bonus.
4. Select the target project in **Current Research Projects** [5].
5. Assign the scientist to the project. Their bonus and admin rating immediately affect the **Effective Output** [9] calculation.
6. If reassigning from another project, note that progress on the old project is preserved -- it can be resumed later with no penalty.

### Checking Research Prerequisites

1. Select any technology in the **Available Technologies** list [3], including locked ones.
2. The **Technology Prerequisites Display** [11] shows the full prerequisite chain.
3. Completed prerequisites show a checkmark; in-progress ones show their percentage; unstarted ones show empty.
4. To reach a locked technology, trace backwards through the chain and ensure each prerequisite is either complete or queued.
5. For cross-category prerequisites (rare), switch between categories to verify status of dependencies in other fields.

### Redistributing Labs Between Projects

1. Open the **Lab Allocation Controls** [8].
2. Select the project you want to adjust via the project dropdown.
3. Note the "Total Labs on Colony" and "Unallocated Labs" counts.
4. To add labs: click [+1], [+5], or [+All] to assign available labs.
5. To remove labs: click [-1], [-5], or [-All] to free labs for other projects.
6. Switch to another project and assign the freed labs there.
7. Check the **Effective Output** [9] panel for each project after reallocation to confirm the impact.
8. Aim to keep assigned labs at or below each scientist's admin rating for maximum efficiency.

### Setting Up a Research Queue

1. Select a scientist's current project in **Current Research Projects** [5].
2. In the **Research Queue** panel [10], click "Add to Queue."
3. Select the next technology this scientist should research upon completion.
4. Add additional technologies to build a multi-project pipeline.
5. Use "Move Up" / "Move Down" to reorder the queue priority.
6. When the current project completes, the scientist automatically begins the next queued entry with no idle time.

### Creating and Using Prototypes

1. Select a technology in the **Available Technologies** list [3].
2. Click "Prototype" in the **Prototype Controls** [14] to create a (P) component instantly.
3. The prototype is immediately available in the Ship Designer for class designs, but the class cannot be built (produced) while it contains prototypes.
4. Enable "Show Next Tech" [2] to access next-tier technologies and create (FP) future prototypes.
5. To convert a prototype to a formal research project, use the "Research Proto" button in the Ship Designer -- this creates an (RP) entry in the research queue.
6. Once all prototype components in a class are fully researched, the class becomes production-ready.

---

## Tips and Shortcuts

**Scientist Matching to Category Bonuses:**

- The bonus multiplier ONLY applies when the scientist's field matches the technology's category. A +30% Power/Propulsion scientist researching an Energy Weapons tech receives 0% bonus -- they produce at base rate only.
- A mediocre specialist (+15% in-field) always outperforms a brilliant generalist (+40% out-of-field) working outside their specialization. Always match fields first, then optimize for bonus magnitude.
- Scientists with secondary fields get a reduced bonus in that secondary category. This makes them flexible options when no primary specialist is available.
- When a new high-bonus scientist appears, immediately reassign them to their specialty field even if it means displacing an inferior scientist mid-project. Progress is never lost on reassignment.

**Diminishing Returns on Multiple Labs:**

- Labs up to the scientist's admin rating operate at 100% efficiency. Beyond that cap, each additional lab operates at roughly 50% efficiency.
- A scientist with Admin Rating 10 supervising 15 labs gets: 10 labs at 100% + 5 labs at ~50% = effective output of 12.5 labs worth of RP. Those 5 excess labs would produce more total RP if assigned to another scientist's project.
- Rule of thumb: never assign more than 150% of a scientist's admin rating in labs unless all other projects are fully staffed.
- Check the **Effective Output** panel [9] after allocation changes to see the actual impact. If adding 5 labs only increases RP/yr by 250 (instead of the expected 500+), you are past the efficiency threshold.

**Research Queue Management:**

- Always maintain a queue of 2-3 technologies per scientist to prevent idle time between completions. An idle scientist with empty queue wastes lab capacity every day.
- Queue technologies in the same category as the scientist's specialization to maintain the bonus through the entire queue.
- For long prerequisite chains (like the engine path with 12+ levels), queue the entire chain for your Power/Propulsion specialist. They will work through it sequentially with no gaps.
- As of v2.0, queued project ETAs include ancient construct bonuses in their calculations, giving accurate time estimates.

**Focus vs. Breadth Strategy:**

- **Focus** (all labs on one project): Use when a single technology unlock is urgently needed (jump drives, a critical weapon system, construction rate). Fastest time to a single breakthrough.
- **Breadth** (3-6 parallel projects): Use during peacetime for steady advancement across multiple fields. Prevents any single area from falling dangerously behind.
- **Hybrid** (60% to priority, 40% spread): The most common approach. Keeps priority research advancing quickly while maintaining progress elsewhere.

**Research Rate Technology Priority:**

- Researching improved Research Rate early is one of the highest-ROI investments. Each level increases ALL lab output permanently, accelerating everything researched afterward.
- Example: 20 labs at 100 RP/yr = 2,000 RP/yr. After Research Rate improvement (150 RP/yr): 20 labs = 3,000 RP/yr. That 50% increase applies to every future project.
- Similar logic applies to Construction Rate research -- but Research Rate amplifies research capacity, which in turn helps you research Construction Rate faster. Research Rate first, then Construction Rate.

**Prototype Workflow for Fleet Planning:**

- Use prototypes to design entire future ship classes before committing research resources. Create (FP) prototypes using "Show Next Tech," build a theoretical class design, evaluate its capabilities, then selectively research only the components you actually want.
- This prevents wasting research on components you will never use in a class design.
- Prototype classes display a (P) marker and cannot be tooled in shipyards until all components are fully researched.

**Scientist Lifecycle Planning:**

- Scientists have finite lifespans. Track ages in the Scientist List [6] and plan succession.
- When your best specialist reaches age 60+, begin looking for a replacement in their field. If one appears, queue them on a secondary project in the same category to build their research queue.
- A scientist's death mid-project does NOT destroy progress. But the replacement scientist may have a lower bonus, extending the remaining time significantly.

**Ancient Construct Bonuses:**

- If a colony hosts an ancient construct with a research bonus, build labs there specifically for that research field. The construct provides a local bonus to labs on that colony PLUS 10% of its bonus empire-wide.
- A colony with a +50% Power/Propulsion construct should be your primary location for P&P research labs. The +50% local bonus stacks with the scientist's personal bonus.

---

## Related Sections

- [7.1 Technology Tree](../7-research/7.1-technology-tree.md) -- Complete technology structure, prerequisite chains, and cost scaling
- [7.2 Scientists](../7-research/7.2-scientists.md) -- Scientist generation, bonuses, and lifecycle management
- [7.3 Research Facilities](../7-research/7.3-research-facilities.md) -- Lab construction, orbital research, and output maximization
- [7.4 Tech Categories](../7-research/7.4-tech-categories.md) -- Detailed breakdown of each research category's technology lines
- [6.3 Construction](../6-economy-and-industry/6.3-construction.md) -- Building research labs and component development costs
- [8.1 Design Philosophy](../8-ship-design/8.1-design-philosophy.md) -- How research unlocks ship components
- [16.1 Officer Generation](../16-commanders/16.1-officer-generation.md) -- Scientist generation as a commander type
- [17.3 Xenoarchaeology](../17-exploration/17.3-xenoarchaeology.md) -- Ancient constructs providing research bonuses
- [Appendix A: Formulas](../appendices/A-formulas.md) -- Research point calculation formulas
