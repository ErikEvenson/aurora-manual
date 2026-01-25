# Fleet/Task Group Window Layout

The Fleet Window (also called the Naval Organization window, accessed via F12 or the toolbar) is the primary interface for managing task groups, issuing movement and combat orders, and monitoring fleet status. This window is one of the most frequently used interfaces in Aurora C# and most players keep it open at all times alongside the System Map and Economics windows.

Multiple instances of the Fleet Window can be opened simultaneously (Shift+click the toolbar button) to facilitate ship transfers between fleets via drag-and-drop.

## Window Layout Diagram

```
+============================================================================+

|  Naval Organization                                                   [X]  |
+============================================================================+

| [1] Fleet/TG List   | [2] Ship List (Selected Group)    | [6] Orders Tab  |
|                     |                                    |                 |
| v Sol Fleet         | Name        Class    Speed  Status | [Movement Ord.] |
|   > Battle Group    | DD Valiant  Tribal   4200   Ready  | [Combat Orders] |
|   > Escort Squad    | DD Brave    Tribal   4200   Ready  | [Logistics Ord] |
|     > TG Alpha [3s] | CA Thunder  County   3100   Ready  | [Misc/Controls] |
|     > TG Beta  [2s] | CA Storm    County   3100   Train  | [Standing Ord.] |
|   > Survey TG       | CL Dawn     Town     3500   Ready  | [Order Template]|
|   > Transport TG    | FF Scout    Pathfndr 5200   Ready  |                 |
| v Alpha Centauri Fl |                                    +-----------------+
|   > Patrol TG       | [3] Ship Detail Panel              | [7] Order Queue |
|   > Mining Escort   +------------------------------------+                 |
|                     | Selected: CA Thunder (County-class) | 1. Move to JP-A |
| [Create TG]         | Tonnage: 12,500t  Crew: 350        | 2. Std Transit  |
| [Disband TG]        | Max Speed: 3,100 km/s              | 3. Move to Mars |
| [Rename TG]         | Fuel: 82% (2,460 / 3,000 litres)  | 4. Orbit Mars   |
|                     | MSP: 91%  Ordnance: 100%          | 5. Load Cargo   |
|                     | Shields: Up  Sensors: Active       | 6. Move to JP-A |
|                     | Commander: Capt. Williams (Init:7) | 7. Std Transit  |
|                     | Deployment: 45/180 days            | 8. (Repeat #1)  |
|                     |                                    |                 |
+---------------------+------------------------------------+ [Add Order]     |

| [8] Target Selector                                     | [Remove Order]  |
|                                                         | [Move Up]       |
| [4] Order Type: [Move To________v]  [9] Dist: 142.3Mkm | [Move Down]     |
|                                                         |                 |
| [5] Target:    [Mars____________v]  [10] ETA: 12h 45m   | [Repeat Orders] |
|                                                         | [x] times: [__] |
|                                                         +-----------------+
+-----------------------------------------------+---------+                  |

| [11] Speed/Fuel Display                       | [12] Formation & Controls  |
|                                               |                            |
| TG Max Speed: 3,100 km/s (limited by Thunder) | [Use Max Speed]            |
| TG Fuel Range: 18.2 billion km @ max speed    | [Active On/Off]            |
| Est. Fuel at Dest: 74%                        | [Raise/Lower Shields]      |
| Military Tonnage: 25,000t  Fleet Cost: 4,820  | [Detach Escorts]           |
|                                               | [Recall Escorts]           |
+-----------------------------------------------+----------------------------+

| [13] Status Bar                                                            |
| Fleet: Sol Fleet | TG: Battle Group Alpha | Ships: 6 | Cmdr: Adm. Hayes  |
+============================================================================+

| [14] Tab Bar                                                               |
| [Movement] [Combat] [Ship Combat] [Logistics] [Misc] [Templates]          |
+============================================================================+

| [15] Logistics Reports Tab                                                 |
| Category: [Fuel_____v]  Ships sorted by urgency:                           |
| FF Scout........12%  |  DD Brave.......45%  |  CA Thunder.....82%          |
+============================================================================+
```

## Element Descriptions

| # | Element | Description |
|---|---------|-------------|
| 1 | **Fleet/Task Group List** | Hierarchical tree showing all fleets organized by location (system). Each fleet expands to show its task groups and sub-fleets. Ship count shown in brackets. Select a task group here to populate the ship list and order queue. |
| 2 | **Ship List** | All ships in the currently selected task group. Displays ship name, class, individual max speed, and operational status (Ready, Training, Overhaul, etc.). Ships can be dragged between groups or to another Fleet Window instance. |
| 3 | **Ship Detail Panel** | Comprehensive status for the currently selected ship: tonnage, crew complement, speed, fuel percentage and absolute values, maintenance supply points, ordnance load, shield/sensor state, assigned commander with initiative rating, and deployment time vs. planned deployment. |
| 4 | **Order Type Selector** | Dropdown menu for selecting the type of order to issue. Categories include: Move To, Orbit, Patrol, Follow, Intercept, Engage Target, Evade, Load Cargo, Unload Cargo, Load Ordnance, Refuel, Standard Transit, and many more (see [Section 9.5 Orders](../9-fleet-management/9.5-orders.md) for full list). |
| 5 | **Target Selector** | Dropdown listing valid destinations for the selected order type. Contents change based on order type: shows celestial bodies for Move To, colonies for Load/Unload, other task groups for Follow/Join, jump points for Transit, waypoints, and contacts. |
| 6 | **Orders Tab Selector** | Tab strip switching between order category views: Movement Orders, Combat Orders, Logistics Orders, Miscellaneous/Controls, Standing Orders, and Order Templates. Each tab exposes different controls relevant to that order category. |
| 7 | **Order Queue** | The sequential list of pending orders for the selected task group. Orders execute top-to-bottom. Supports conditional orders (IF/THEN logic), repeating order loops, and order delays. Shows order numbering for reference. |
| 8 | **Target Selector Area** | Combined area containing the order type dropdown, target dropdown, and the "Add Move" button to append orders to the queue. Also contains checkboxes for Auto-Route by System, Use Default Movement Actions, Avoid Danger, and Avoid Alien Systems. |
| 9 | **Distance Display** | Shows the calculated distance from the task group's current position to the selected target in millions of kilometers (Mkm) or AU depending on scale. Updates as you change target selection. |
| 10 | **ETA Display** | Estimated time of arrival at the selected destination based on the task group's current maximum speed. Accounts for the speed-limiting ship in the group. |
| 11 | **Speed/Fuel Display** | Task group speed summary: maximum speed (with the bottleneck ship identified), fuel range at current speed, estimated fuel remaining at destination, total military tonnage, and fleet cost. Critical for logistics planning. |
| 12 | **Formation and Fleet Controls** | Control buttons: Use Maximum Speed checkbox (auto-updates speed each sub-pulse), Active Sensors On/Off toggle, Raise/Lower Shields toggle, Detach Escorts (releases sub-fleets to pre-configured positions), Recall Escorts (reintegrates escort sub-fleets). |
| 13 | **Status Bar** | Bottom summary showing the currently selected fleet name, task group name, total ship count, and assigned fleet commander. Provides at-a-glance context. |
| 14 | **Tab Bar** | Primary navigation between the window's major functional areas. Movement tab for travel orders, Combat tab for engagement rules, Ship Combat for individual fire control assignment, Logistics for cargo/fuel orders, Misc for fleet settings, Templates for saved order sequences. |
| 15 | **Logistics Reports Tab** | Dropdown-selectable fleet-wide status reports across five categories: Fuel, MSP, Ordnance, Deployment Time, and Time Since Overhaul. Ships are sorted by urgency (most critical first), enabling quick identification of vessels needing attention. |

## Common Workflows

### Issuing a Move Order

1. Select the task group from the Fleet/TG List (element 1)
2. Ensure the **Movement Orders** tab is active (element 14)
3. Set Order Type (element 4) to **"Move To"**
4. Select the destination from the Target dropdown (element 5) -- bodies, jump points, waypoints, or other groups appear here
5. Verify the distance (element 9) and ETA (element 10) are reasonable
6. Click **[Add Move]** to append the order to the queue (element 7)
7. The order appears at the bottom of the queue and will execute in sequence

### Setting Up a Repeating Cargo Route

1. Select your transport task group
2. Add orders in sequence: **Orbit Colony A** > **Load Cargo (minerals)** > **Move to Colony B** > **Orbit Colony B** > **Unload All Cargo** > **Move to Colony A**
3. Click **[Repeat Orders]** to cycle the queue indefinitely
4. Optionally enter a number in the "x times" field to limit repetitions
5. The transport will shuttle between colonies autonomously until cancelled or fuel runs low
6. Consider adding a conditional "IF fuel < 25%: Refuel at Colony" as a safety order

### Using Conditional Orders

Conditional orders add IF/THEN logic to your order queue. Each order can have a condition attached -- if the condition is not met, the order is skipped and the next order is evaluated.

**Adding a Conditional Order:**

1. Select the task group and open the **Standing Orders** tab (element 6)
2. Select a **Condition Type** from the dropdown (fuel level, hostile contact, damage, etc.)
3. Set the **Threshold** value (e.g., "30%" for fuel, "200M km" for detection range)
4. Select the **Order** to execute when the condition is met
5. Click **[Add Conditional Order]** to insert it into the queue (element 7)

**Condition Types:**

| Category | Conditions |
|----------|------------|
| Resource | Fuel %, ordnance %, cargo capacity, maintenance supplies |
| Contact | Hostile detected within X km, no hostiles detected, contact type |
| Status | Ship damage %, shield %, speed reduced, deployment exceeded |
| Location | Arrived at destination, within X km of location |

**Example: Safe Survey Ship Configuration**

```
1. IF fuel < 30%: Move to Earth
2. IF fuel < 30%: Refuel at Colony
3. IF deployment exceeded: Refuel, Resupply and Overhaul at Colony
4. Survey System Bodies (Standing Order)
```

**Example: Combat Patrol with Retreat**

```
1. Move to Waypoint Alpha
2. IF hostile contact within 200M km: Move to contact
3. IF hostile contact within 200M km: Engage at will
4. IF fuel < 25%: Move to nearest colony
5. IF fuel < 25%: Refuel at Colony
6. IF shields < 50%: Move to nearest colony
7. Move to Waypoint Beta
8. (Repeat Orders enabled)
```

> **Tip:** Place safety conditions (low fuel, shield damage, deployment exceeded) before mission orders in the queue. Conditions are evaluated in queue order, so higher-priority conditions should come first.

> **Note:** Conditional orders only trigger if the group has sensors capable of detecting the condition. A group without active sensors cannot trigger "hostile contact detected" based on its own detection.

For complete conditional order mechanics, see [Section 9.5.5 Conditional Orders](../9-fleet-management/9.5-orders.md#955-conditional-orders).

### Transferring Ships Between Task Groups

1. Open a **second Fleet Window** (Shift+click the toolbar button)
2. In the first window, select the source task group to see its ships (element 2)
3. In the second window, select the destination task group
4. **Drag** the ship(s) from the source ship list to the destination group in the second window
5. The ship immediately transfers to the new task group
6. Note: the task group speed updates to reflect the new composition

### Setting Fleet Speed

1. Select the task group and observe the Speed/Fuel Display (element 11)
2. Identify which ship is the speed bottleneck (shown parenthetically)
3. To override: enable the **[Use Maximum Speed]** checkbox (element 12) -- the system auto-recalculates speed each sub-pulse if composition changes
4. To increase speed: detach the slow ship to a separate task group, or consider the tactical tradeoff of leaving it behind
5. Remember: fuel consumption is proportional to speed, so slower groups burn less fuel per distance

### Configuring Escort Positions

1. Select the escort fleet/sub-fleet
2. On the Misc tab, set the **Anchor Fleet** to the fleet you want to escort
3. Configure **Distance** (km from anchor) and **Bearing** (degrees from anchor heading)
4. Integrate the escort as a sub-fleet for transit (Join as Sub-Fleet order)
5. At the operational area, click **[Detach Escorts]** (element 12) on the parent fleet
6. Escorts automatically move to their pre-configured positions around the anchor

### Using Auto-Route for Multi-System Travel

1. On the Movement Orders tab, enable the **Auto-Route by System** checkbox
2. The target list changes to show reachable star systems (color-coded: light green = populated, dark green = other colonies)
3. Select the destination system
4. Configure route settings: "Assume Fleet is Jump Capable," "Check Danger Rating," "Exclude Alien-Controlled"
5. Click **[Add Move]** -- all intermediate jump point transits are automatically generated
6. Review the order queue to verify the route is acceptable

## Tips and Shortcuts

- **Double-click destinations** with "Use Default Movement Actions" enabled for quick order creation (jump points default to Standard Transit, populations to Refuel/Resupply, etc.)
- **Conditional fuel orders** should be placed early in the queue with safety conditions. A "IF fuel < 25%: Move to nearest colony" order prevents fleets from stranding in deep space.
- **Order priority matters**: conditional orders are evaluated in queue order. Place safety conditions (low fuel, enemy evasion) above mission orders so they take precedence.
- **Order Templates** save frequently-used order chains. Create a template for standard patrol routes, then apply it to new ships with a single click.
- **Order Delay** (v1.9.0+) allows you to insert wait periods between orders for synchronized fleet operations or timed departures.
- **Combination Orders** (Refuel + Resupply + Load Ordnance) execute simultaneously, with the total time equal to the longest single operation rather than the sum.
- **Keep survey ships at 40-50% fuel threshold** for conditional return orders -- they consume extra fuel from frequent course changes during survey operations.
- **Initiative settings** affect combat turn order. Lower initiative = move first (commit before seeing enemy). Higher initiative = observe then react (better for pursuit or escape).
- **Sub-Pulse processing** means conditional orders are evaluated every 5 seconds even within long time increments. Fleets can detect and respond to threats mid-advance.
- **Logistics Reports** (element 15) quickly reveal which ships need urgent attention. Check fuel status before issuing long-range movement orders.

## Related Sections

- [Section 9.3 Task Groups](../9-fleet-management/9.3-task-groups.md) -- Task group creation, speed mechanics, and conditional orders
- [Section 9.4 Fleet Organization](../9-fleet-management/9.4-fleet-organization.md) -- Fleet hierarchy, admin commands, and sub-fleets
- [Section 9.5 Orders](../9-fleet-management/9.5-orders.md) -- Complete order type reference (movement, combat, logistics, standing, escort)
- [Section 3.1 Main Window](../3-user-interface/3.1-main-window.md) -- Toolbar access, multiple instances, time controls
- [Section 3.2 System Map](../3-user-interface/3.2-system-map.md) -- Issuing orders from the map interface
- [Section 14.1 Fuel](../14-logistics/14.1-fuel.md) -- Supply chain management and fleet maintenance
