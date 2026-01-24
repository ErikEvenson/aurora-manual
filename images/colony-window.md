# Colony/Population Window Layout

The Colony window (also called the Economics window or Population window) is the central hub for managing all aspects of your colonies. It provides access to population data, installations, construction queues, mineral stockpiles, environmental information, and ground forces for every colony in your empire.

---

## Window Layout Diagram

```
+============================================================================+
|  Economics Window                                                    [X]    |
+============================================================================+
|                                                                            |
| [1] Colony Selector Dropdown                                               |
| +------------------------------------------------------------------------+ |
| | v  Earth (Sol)                                                         | |
| +------------------------------------------------------------------------+ |
|                                                                            |
| +------------------+  +---------------------------------------------------+|
| | [2] Population   |  | [6] Tab Bar                                       ||
| |     Tree         |  | +-------+-------+------+--------+------+--------+||
| |                  |  | |Summar.|Instal.|Indus.|Environ.|Mining|Grd.Frc.|||
| | > Earth          |  | +-------+-------+------+--------+------+--------+||
| |   > Luna         |  +---------------------------------------------------+|
| |   > Mars         |  |                                                    ||
| | > Alpha Centauri |  | [7] SUMMARY TAB (shown)                           ||
| |   > AC-B II     |  | +------------------------------------------------+ ||
| |   > AC-B III    |  | | [8] Population & Demographics                  | ||
| | > Barnard's Star |  | |   Population: 1,247.32m    Growth Rate: 2.1%   | ||
| |   > BS-A II     |  | |   Manufacturing Pop: 374.20m  (30.0%)          | ||
| |                  |  | |   Service Pop: 873.12m  (70.0%)                | ||
| | [3] Colony       |  | |   Employment: 312.50m / 374.20m  (83.5%)      | ||
| |     Summary      |  | |   Unemployment: 61.70m  (16.5%)               | ||
| | Pop: 1,247.32m   |  | +------------------------------------------------+ ||
| | Cost: 0.00       |  |                                                    ||
| | Temp: 14.5C      |  | [9] Colony Cost & Environment Summary              ||
| | Atm: N2/O2       |  | +------------------------------------------------+ ||
| | Grav: 1.00g      |  | |   Colony Cost: 0.00  (Ideal)                   | ||
| |                  |  | |   Temperature: 14.5C  (within tolerance)       | ||
| | [4] Governor     |  | |   Atm. Pressure: 1.00 atm                     | ||
| | Info             |  | |   Gravity: 1.00g                               | ||
| | Gov: Adm. Chen   |  | |   Hydrosphere: 71%                             | ||
| | Mining: +15%     |  | |   Infrastructure: N/A (cost 0.00)              | ||
| | Mfg: +10%        |  | +------------------------------------------------+ ||
| |                  |  |                                                    ||
| | [5] Wealth       |  | [10] Mineral Stockpile Display                     ||
| | Summary          |  | +------------------------------------------------+ ||
| | Wealth: 24,150   |  | | Mineral        Stockpile    Annual +/-         | ||
| | Tax Rate: 20%    |  | | Duranium       142,350      +8,420             | ||
| | Income: 8,230    |  | | Neutronium      38,720      +2,150             | ||
| |                  |  | | Corbomite       22,100      +1,840             | ||
| +------------------+  | | Tritanium       45,680      +3,200             | ||
|                        | | Boronide        31,450      +1,960             | ||
|                        | | Mercassium      18,900      +1,420             | ||
|                        | | Vendarite       27,300      +2,080             | ||
|                        | | Sorium          52,100      +4,500             | ||
|                        | | Uridium         15,600      +1,180             | ||
|                        | | Corundium       28,400      +2,340             | ||
|                        | | Gallicite       12,800        -920             | ||
|                        | +------------------------------------------------+ ||
|                        |                                                    ||
|                        +----------------------------------------------------+|
|                                                                            |
| [20] Status Bar: Year 2050  |  Pop: 1,247.32m  |  Colonies: 7             |
+============================================================================+
```

---

## Installation Tab Layout

```
+----------------------------------------------------+
| [6] INSTALLATIONS TAB                              |
| +------------------------------------------------+ |
| | [11] Installation List                         | |
| | +--------------------------------------------+ | |
| | | Type               Qty   Workers   Output  | | |
| | | Construction Fac.  420   21.00m    4,200BP | | |
| | | Mine               380   19.00m    3,800t  | | |
| | | Automated Mine      85   --        850t    | | |
| | | Research Lab         32    1.60m    3,200RP | | |
| | | Fuel Refinery        50    2.50m    500k L  | | |
| | | Ordnance Factory     25    1.25m    250BP   | | |
| | | Fighter Factory      10    0.50m    100BP   | | |
| | | Financial Centre     40    2.00m    10,000W | | |
| | | Maintenance Fac.     15    0.75m    --      | | |
| | | Mass Driver           2   --        10,000t| | |
| | | Terraform Install.    5    1.25m    --      | | |
| | | Infrastructure     12000   --        --     | | |
| | | Deep Space Track.     1   --        --      | | |
| | | Naval Shipyard        2   varies    800BP   | | |
| | | Commercial Shipyard   1   varies    400BP   | | |
| | +--------------------------------------------+ | |
| +------------------------------------------------+ |
+----------------------------------------------------+
```

---

## Industry Tab Layout

```
+----------------------------------------------------+
| [6] INDUSTRY TAB                                   |
| +------------------------------------------------+ |
| | [12] Construction Queue                        | |
| | +--------------------------------------------+ | |
| | | #  Item             Qty  %Cap  Progress     | | |
| | | 1  Construction Fac  50  40%   ||||....  32%| | |
| | | 2  Mine              80  30%   |||.....  24%| | |
| | | 3  Infrastructure   500  20%   ||......  16%| | |
| | | 4  Research Lab        5  10%   |.......   8%| | |
| | +--------------------------------------------+ | |
| |                                                | |
| | [13] Queue Controls                            | |
| | [Add Item v] [Qty: ___] [% Cap: ___]          | |
| | [Move Up] [Move Down] [Pause] [Cancel]         | |
| | [Repeat: [ ]] [SM Add: [ ]]                   | |
| |                                                | |
| | [14] Production Summary                        | |
| | Total Factory Output: 4,200 BP/year            | |
| | Unused Capacity: 0%                            | |
| | Construction Rate Tech: Level 3 (x1.5)         | |
| |                                                | |
| | [15] Completion Estimates                      | |
| | Next completion: Construction Fac x1 in 42d    | |
| | Queue finish (all): ~4.2 years                 | |
| +------------------------------------------------+ |
+----------------------------------------------------+
```

---

## Mining Tab Layout

```
+----------------------------------------------------+
| [6] MINING TAB                                     |
| +------------------------------------------------+ |
| | [16] Mining Output Display                     | |
| | +--------------------------------------------+ | |
| | | Mineral      Deposit  Access  Annual Prod   | | |
| | | Duranium     285,000   0.8    24,320 t/yr   | | |
| | | Neutronium   142,000   0.6    13,680 t/yr   | | |
| | | Corbomite     98,000   0.9    10,260 t/yr   | | |
| | | Tritanium    176,000   0.7    15,960 t/yr   | | |
| | | Boronide     120,000   0.5    11,400 t/yr   | | |
| | | Mercassium    65,000   0.4     7,600 t/yr   | | |
| | | Vendarite    105,000   0.6    11,400 t/yr   | | |
| | | Sorium       210,000   0.7    18,050 t/yr   | | |
| | | Uridium       55,000   0.3     5,700 t/yr   | | |
| | | Corundium    130,000   0.8    12,160 t/yr   | | |
| | | Gallicite     42,000   0.2     3,800 t/yr   | | |
| | +--------------------------------------------+ | |
| |                                                | |
| | [17] Mining Summary                            | |
| | Total Mines: 380 conventional + 85 automated   | |
| | Mining Tech Level: 3 (20 t/mine/yr base)       | |
| | Governor Bonus: +15%                           | |
| | Years to Depletion (lowest): Gallicite ~11 yr  | |
| +------------------------------------------------+ |
+----------------------------------------------------+
```

---

## Environment Tab Layout

```
+----------------------------------------------------+
| [6] ENVIRONMENT TAB                                |
| +------------------------------------------------+ |
| | [18] Atmospheric Composition                   | |
| | +--------------------------------------------+ | |
| | | Gas              Partial Pressure   % Atm   | | |
| | | Nitrogen (N2)    0.780 atm          78.0%   | | |
| | | Oxygen (O2)      0.210 atm          21.0%   | | |
| | | Argon (Ar)       0.009 atm           0.9%   | | |
| | | CO2              0.0004 atm          0.04%  | | |
| | | Water Vapor      0.001 atm           0.1%   | | |
| | +--------------------------------------------+ | |
| |                                                | |
| | [19] Terraforming Status                       | |
| | Active Terraforming: None                      | |
| | Terraform Installations: 5                     | |
| | Target Gas: --                                 | |
| | Rate: -- atm/year                             | |
| |                                                | |
| | Colony Cost Breakdown:                         | |
| |   Temperature Factor: 0.00                    | |
| |   Pressure Factor: 0.00                       | |
| |   Breathable Gas Factor: 0.00                 | |
| |   Dangerous Gas Factor: 0.00                  | |
| |   Hydrosphere Factor: 0.00                    | |
| |   Gravity Factor: 0.00                        | |
| |   FINAL COLONY COST: 0.00                     | |
| +------------------------------------------------+ |
+----------------------------------------------------+
```

---

## Ground Forces Tab Layout

```
+----------------------------------------------------+
| [6] GROUND FORCES TAB                              |
| +------------------------------------------------+ |
| | [21] Stationed Formations                      | |
| | +--------------------------------------------+ | |
| | | Formation          Strength  Morale  Status | | |
| | | 1st Infantry Div    12,400   92%    Ready   | | |
| | | 3rd Armored Bde      8,200   88%    Ready   | | |
| | | HQ Company             400   95%    Ready   | | |
| | +--------------------------------------------+ | |
| |                                                | |
| | Garrison Strength: 21,000                      | |
| | Required PPV: 12,474                           | |
| | Current PPV: 21,000 (168% of requirement)      | |
| +------------------------------------------------+ |
+----------------------------------------------------+
```

---

## Numbered Element Descriptions

| # | Element | Description |
|---|---------|-------------|
| 1 | Colony Selector Dropdown | Selects which colony to view. Lists all colonies by system, including population counts. Switch between colonies to compare resources and production. |
| 2 | Population Tree | Hierarchical list of all colonies organized by star system. Expand/collapse system nodes. Click any colony to select it. Shows at-a-glance population for each entry. |
| 3 | Colony Summary | Quick-reference panel showing key colony stats: total population, colony cost, surface temperature, atmospheric composition, and gravity. Updates when colony selection changes. |
| 4 | Governor Info | Displays the assigned governor (if any) and their bonuses. Shows mining bonus percentage, manufacturing bonus, and other relevant modifiers the governor provides. |
| 5 | Wealth Summary | Financial overview for the colony: current wealth stockpile, tax rate setting, and annual income from workers and financial centres. |
| 6 | Tab Bar | Switches between the major colony information views: Summary, Installations, Industry, Environment, Mining, and Ground Forces. Each tab reveals a different panel of colony data. |
| 7 | Summary Tab | Default view showing population demographics, colony cost details, and mineral stockpiles at a glance. The "home screen" for colony management. |
| 8 | Population and Demographics | Detailed population breakdown: total population, manufacturing sector (30% cap), service sector (70% cap), employment ratio, and unemployment figures. |
| 9 | Colony Cost and Environment Summary | Environmental conditions summary showing the colony cost value, temperature, atmospheric pressure, gravity, and hydrosphere percentage. Also shows infrastructure status for non-ideal worlds. |
| 10 | Mineral Stockpile Display | Lists all 11 trans-newtonian minerals with current stockpile quantities and net annual change (production minus consumption). Negative values indicate minerals being consumed faster than produced. |
| 11 | Installation List | Complete inventory of all installations on the colony. Shows type, quantity, worker requirements, and output rates. Includes both ground installations and orbital facilities (shipyards). |
| 12 | Construction Queue | The build queue showing what construction factories are currently producing. Each entry shows the item, quantity ordered, percentage of factory capacity allocated, and completion progress. |
| 13 | Queue Controls | Interface buttons for managing the construction queue: add new items, set quantities, allocate capacity percentages, reorder priority (move up/down), pause/resume, cancel, and set repeat. |
| 14 | Production Summary | Aggregate factory output information: total Build Points per year, unused capacity percentage, and current Construction Rate technology level with its multiplier. |
| 15 | Completion Estimates | Projected completion times for queue items based on current production rates and mineral availability. Shows next completion and total queue duration. |
| 16 | Mining Output Display | Per-mineral breakdown showing remaining deposit size, accessibility rating, and annual production rate. Calculated from mine count, mining tech level, accessibility, and governor bonuses. |
| 17 | Mining Summary | Aggregate mining information: total mine count (conventional and automated), mining technology level with base output, governor bonus percentage, and depletion warnings for lowest deposits. |
| 18 | Atmospheric Composition | Detailed gas breakdown of the colony's atmosphere showing each gas, its partial pressure in atmospheres, and percentage of total atmosphere. Used to identify colony cost factors and terraforming targets. |
| 19 | Terraforming Status | Current terraforming operations: number of installations active, target gas being added/removed, rate of atmospheric change per year. Also shows the complete colony cost breakdown by factor. |
| 20 | Status Bar | Bottom bar showing current game year, selected colony population, and total empire colony count. Provides persistent context while navigating tabs. |
| 21 | Stationed Formations | List of ground force units garrisoning the colony. Shows formation name, combat strength, morale percentage, and readiness status. Also displays PPV (Planetary Protection Value) requirements and coverage. |

---

## Common Workflows

### Checking Mineral Stockpiles

1. Open the Economics window and select the target colony from the **Colony Selector** [1] or **Population Tree** [2].
2. The **Summary Tab** [7] shows the **Mineral Stockpile Display** [10] with all 11 minerals.
3. Look at the "Annual +/-" column to identify minerals with negative net production (being consumed faster than mined).
4. Switch to the **Mining Tab** to see the **Mining Output Display** [16] for deposit sizes and accessibility.
5. Check the **Mining Summary** [17] for depletion estimates -- low deposits with high consumption need attention.

### Queueing Construction

1. Switch to the **Industry Tab** via the **Tab Bar** [6].
2. Review the current **Construction Queue** [12] for existing orders.
3. Use the **Queue Controls** [13]: select an item type from the dropdown, enter the quantity, and set the capacity percentage.
4. Click "Add Item" to place it in the queue.
5. Use "Move Up" / "Move Down" to adjust priority relative to other items.
6. Enable "Repeat" for items you want produced continuously (such as mines or infrastructure).
7. Check **Completion Estimates** [15] to verify the timeline is acceptable.

### Reviewing Colony Cost

1. Select the colony and check the **Colony Summary** [3] for the quick colony cost value.
2. Switch to the **Environment Tab** to see the full **Colony Cost Breakdown** in the **Terraforming Status** section [19].
3. Identify which single factor is driving the colony cost (temperature, dangerous gas, pressure, etc.).
4. Check **Atmospheric Composition** [18] to understand what gases are present and at what concentrations.
5. Determine if terraforming is feasible: can the dominant cost factor be addressed by adding/removing gases?

### Assigning a Governor

1. Governor assignment is managed through the **Commanders** window (Section 16), not directly in the colony window.
2. Once assigned, the **Governor Info** panel [4] in the colony window shows the active governor and their bonuses.
3. Review the governor's mining and manufacturing bonuses to understand their production impact.
4. To change governors, return to the Commanders window and reassign.

### Comparing Multiple Colonies

1. Use the **Population Tree** [2] to rapidly switch between colonies.
2. Note the **Colony Summary** [3] values (population, cost, temperature) for each.
3. Switch to the **Mining Tab** and compare deposit sizes and accessibility across colonies.
4. Check **Installation Lists** [11] to compare industrial capacity.
5. Use the "Pop as Text" or "All Pop as Text" buttons to export colony data for side-by-side comparison.

---

## Tips and Shortcuts

**Production Priority Management:**
- Split construction capacity across multiple items using percentage allocation rather than building sequentially. A 50/30/20 split between factories, mines, and infrastructure ensures parallel progress on all fronts.
- Use the "Repeat" function for items you always need more of (mines, infrastructure). This prevents factories from sitting idle when a queue empties.
- Unused capacity is displayed per production type (Construction, Ordnance, Fighters). If you see unused capacity, you have idle factories -- add queue items immediately.

**Mineral Consumption Monitoring:**
- Watch for negative values in the "Annual +/-" column of the Mineral Stockpile Display. Gallicite is the most common shortage mineral due to engine construction.
- Calculate years until depletion: Stockpile / Annual Deficit = years of reserves remaining. Anything under 5 years demands immediate attention.
- Compare mining output to construction consumption. If your queue consumes 15,000 Duranium/year but you only mine 8,000, either slow construction or find new deposits.

**Multi-Colony Comparison:**
- The "All Pop as Text" button exports all colony data simultaneously, useful for identifying which colony should receive new installations.
- When deciding where to build new mines, compare accessibility ratings across colonies. A 0.8 accessibility deposit produces 4x more per mine than a 0.2 accessibility deposit.

**Workforce Optimization:**
- The Employment figure in the Population Demographics [8] shows how well your installations match your workforce. Aim for 90-100% employment.
- If employment is low, you have too many people and not enough installations -- build more factories and mines.
- If installations are understaffed (visible in reduced output on the Installation List), you need more population -- send colony ships.

**Governor Bonuses:**
- A governor with +25% mining bonus is equivalent to adding 25% more mines for free. Assign your best mining governors to your largest mining colonies.
- Governor bonuses stack with sector commander bonuses (25% of their skill). Optimal placement amplifies total output significantly.

**Environmental Awareness:**
- Colony cost is NOT additive -- only the single worst factor applies. Fixing the dominant factor can slash colony cost dramatically even if other problems remain.
- Before committing to terraforming, verify that greenhouse warming can reach habitable range: 3x base temperature is the maximum possible warming (Greenhouse Factor cap of 3.0).
- Check atmospheric composition for dangerous gases before building infrastructure. Trace fluorine at 1 ppm triggers a colony cost floor of 2.0.

---

## Related Sections

- [5.1 Establishing Colonies](../5-colonies/5.1-establishing-colonies.md) -- Colony ships, initial setup, and colony cost mechanics
- [5.2 Population](../5-colonies/5.2-population.md) -- Growth rates, capacity, labor, and employment
- [5.3 Environment](../5-colonies/5.3-environment.md) -- Colony cost factors, habitability, and environmental hazards
- [5.5 Terraforming](../5-colonies/5.5-terraforming.md) -- Atmospheric modification and temperature control
- [6.1 Minerals](../6-economy-and-industry/6.1-minerals.md) -- Mineral types, accessibility, and depletion
- [6.2 Mining](../6-economy-and-industry/6.2-mining.md) -- Mining installations and production calculations
- [6.3 Construction](../6-economy-and-industry/6.3-construction.md) -- Build queues, factories, and shipyards
- [6.4 Wealth and Trade](../6-economy-and-industry/6.4-wealth-and-trade.md) -- Economic output and taxation
- [13.1 Unit Types](../13-ground-forces/13.1-unit-types.md) -- Ground force garrison mechanics
- [16.1 Officer Generation](../16-commanders/16.1-officer-generation.md) -- Governor generation and assignment
