# Tactical/System Map Window Layout

The System Map (also called the Tactical Map) is Aurora C#'s primary visual representation of a star system. It displays orbital bodies, fleets, contacts, jump points, and sensor overlays in real-time relative positions. The tactical map is the sole window limited to a single instance -- all other windows can be opened multiple times. The map is also the main game window; the "Keep Tactical in Background" option prevents it from obscuring other windows when toolbar buttons are clicked.

The minimum resolution for Aurora C# is 1440x900. The tactical map is one of the few resizable windows and can be expanded to fill the entire screen for maximum strategic overview.

## Window Layout Diagram

```
+============================================================================+
|  Tactical Map - Sol System                                            [X]  |
+============================================================================+
| [1] Toolbar                                                                |
| [Zoom+][Zoom-][Centre][Layers][Wide] [5s][30s][2m][5m][20m][1h][3h][8h]   |
|                                      [1d][5d][30d] [>> Advance]            |
+========+===================================================================+
| [2]    |                                                                   |
| System |   [3] Map Viewport                                                |
| Select |                                                                   |
|        |                          * Sol                                    |
| [Sol_v]|                                                                   |
|        |              .  .  .  . ( Mercury ) .  .  .  .                    |
|        |                                                                   |
|        |         .                                       .                 |
|        |       .           -----> [TG Alpha]               .               |
|        |      .       ( Venus )                             .              |
|        |                                                                   |
|        |     .                                               .             |
|        |     .              ( Earth )--[Home Fleet]          .             |
|        |     .                  |                             .            |
|        |      .                Moon                          .              |
|        |       .                                           .               |
|        |         .          ( Mars )                     .                  |
|        |              .  .  .  .  .  .  .  .  .  .  .                      |
|        |                                                                   |
|        |                                                                   |
|        |          JP-Alpha Centauri [*]            ( Jupiter )              |
|        |                                              ||||                  |
|        |                                          Io Europa Ganymede        |
|        |                                                                   |
|        |     [?] Thermal Contact                                           |
|        |         Bearing: 045  Range: 182Mkm                               |
|        |         Speed: 4,100 km/s  Size: ~8,000t                          |
|        |                                                                   |
+--------+-------------------------------------------------------------------+
| [4] Layer Toggles                                                          |
|                                                                            |
| [x] Planet Orbits  [x] Ship Paths   [ ] Moon Orbits   [x] Jump Points     |
| [x] Fleet Names    [x] Contacts     [ ] Asteroids     [ ] Comets          |
| [ ] Sensor Ranges  [ ] Missile Mkrs [x] Waypoints     [x] Survey Markers  |
| [ ] Mineral Icons  [x] Fleet Labels [ ] Grav Survey   [x] Events Display  |
|                                                                            |
+----------------------------------+-----------------------------------------+
| [5] Contact List                 | [7] Selected Object Info                |
|                                  |                                         |
| Type     Bearing  Range   Speed  | Object: Earth                           |
| -------- -------  ------  -----  | Type: Terrestrial Planet                |
| Thermal  045 deg  182Mkm  4,100  | Gravity: 1.00g                          |
| EM Sig   045 deg  182Mkm  4,100  | Temperature: 14.0C                      |
| (Same contact, dual detection)   | Atmosphere: Nitrogen/Oxygen (Breathable)|
|                                  | Colony: Earth (Pop: 8,000M)             |
| Allied   180 deg  340Mkm  2,800  | Minerals: Surveyed (12 deposits)        |
| (Diplo contact, shared data)     | Orbital Bodies: 1 (Moon)                |
|                                  | Colonies in Orbit: Home Fleet [6 ships] |
+----------------------------------+-----------------------------------------+
| [6] Time Controls                                                          |
|                                                                            |
| Current Date: 14 March 2150  08:00:00        Increment: [5 days___v]       |
| Race: Terran Federation                      [>> Advance Time]             |
|                                                                            |
+-----------------------------+----------------------------------------------+
| [8] Coordinates Display     | [9] Scale Indicator                          |
| Cursor: X: 142.3  Y: -87.6 | |----| = 50 Mkm                              |
| (Millions of km from star)  | Zoom Level: Inner System                     |
+-----------------------------+----------------------------------------------+
| [10] Distance Tool: Hold Shift+Drag to measure                             |
+============================================================================+
```

## Element Descriptions

| # | Element | Description |
|---|---------|-------------|
| 1 | **Toolbar** | Quick-access buttons for zoom controls (in/out/centre), display layer toggles, wide-view toggle, and the time increment buttons. Time increment buttons span from 5 seconds (fine combat resolution) to 30 days (peacetime development). The Advance button processes the selected increment. |
| 2 | **System Selector** | Dropdown menu to switch between known star systems. Only explored systems appear (systems your ships have visited). In SpaceMaster mode, all systems are available. Light green entries indicate populated systems; dark green indicates other colonies (automated mines, tracking stations). |
| 3 | **Map Viewport** | The main display area showing the star system. Stars appear at center, planets along orbital paths, fleets as labeled icons with movement vectors, jump points as connection markers, and sensor contacts as detection-type indicators. Supports click-drag panning and mouse wheel zooming (zoom centers on cursor). Multi-star systems show all stellar components. |
| 4 | **Layer Toggles** | Checkbox controls to show/hide categories of map information: orbital paths (planet/moon), ship movement lines, fleet names and labels, sensor range circles, missile markers, jump points, waypoints, survey progress indicators, mineral icons, asteroid fields, comets, contacts, and the on-map events display. |
| 5 | **Contact List** | Table of all detected objects belonging to other races. Shows detection type (thermal, EM, active sensor return), bearing from your nearest sensor platform, range in millions of km, and estimated speed. Multiple detection types for the same contact are shown together. Allied contacts with shared sensor data appear separately. |
| 6 | **Time Controls** | Displays current game date/time and the active race. The increment selector sets how much time advances per click. Available increments: 5s, 30s, 2min, 5min, 20min, 1hr, 3hr, 8hr, 1 day, 5 days, 30 days. The Advance button processes all events for that duration. Auto-interrupts stop advancement on critical events (hostile contact, damage, etc.). |
| 7 | **Selected Object Info Panel** | Detailed information about the currently selected map object. For planets: name, type, gravity, temperature, atmosphere, colony status, mineral survey, orbital bodies. For fleets: name, ship count, orders, speed, fuel, commander. For jump points: destination, transit status. For contacts: signature type, estimated size, bearing, speed. |
| 8 | **Coordinates Display** | Shows the cursor position in system coordinates (millions of km from the primary star on X and Y axes). Useful for precise fleet positioning and understanding spatial relationships between objects. |
| 9 | **Scale Indicator** | Visual reference bar showing the current distance-per-unit at the active zoom level. Scales from AU (full system view) down to thousands of km (close tactical view). Includes a label for the current zoom tier (Full System, Outer System, Inner System, Orbital, etc.). |
| 10 | **Distance Measuring Tool** | Hold Shift and drag on the map to draw a measurement line. Displays the distance between the two endpoints in kilometres. The start point remains fixed while Shift is held, allowing rapid measurement of multiple distances from a common reference point. |

## Additional Map Features

### Right-Click Popup Menu

Right-clicking on the tactical map produces a context menu listing all game objects within a few pixels of the click location:

- **Fleet entries**: Selecting a fleet opens the Naval Organization window with that fleet pre-selected
- **Population entries**: Selecting a population opens the Economics window for that colony
- **Jump Point entries**: Selecting a jump point (shown as destination system name) transitions the map to display that system

### Location History (Cycle Previous Locations)

The map records positions whenever you center the view (clicking objects, using Centre On, mineral searches, double-clicking events):

- **Alt+F11**: Navigate backward through location history
- **Alt+F12**: Navigate forward through location history
- Works across systems, enabling rapid navigation between areas of interest
- Normal centering actions discard forward history and append the new location

### Galactic Map Distance Calculations

Two distance modes available from the galactic map overlay:

- **Standard Distance**: Shortest path through all available jump points
- **Restricted Distance**: Ignores Military Restricted jump points, showing civilian-accessible routes

### Automatic Population Selection

When selecting a system on the galactic map and opening an Economics window, the most significant population in that system is automatically pre-selected based on population size and installation importance.

## Common Workflows

### Zooming to a Contact

1. Locate the contact in the **Contact List** (element 5) -- note bearing and range
2. Click the contact entry to select it; the **Selected Object Info** panel (element 7) shows details
3. Double-click the contact on the map (or use Centre On) to center the viewport on its position
4. Use **mouse wheel up** or the **[Zoom+]** button to zoom in on the contact's location
5. With the contact centered, observe its movement vector (line showing heading) and nearby fleet positions
6. The contact's detection type (thermal, EM, active) indicates what sensor detected it

### Enabling Sensor Overlays

1. In the **Layer Toggles** (element 4), check **[Sensor Ranges]**
2. Circles appear around ships/installations showing their detection envelopes
3. Thermal sensor ranges appear as one color, EM as another, active as a third
4. Use this to identify sensor gaps in your coverage
5. During combat setup, sensor overlays reveal whether enemy contacts are within your detection envelope or at the edge of detection
6. Disable sensor overlays during peacetime to reduce visual clutter

### Advancing Time in Combat

1. Upon receiving a "Hostile Contact" interrupt, **immediately reduce increment** to 30 seconds or less
2. Observe the contact position and your fleet positions on the map
3. Issue combat orders via the Fleet Window (or right-click > fleet > Naval Organization)
4. Select **5 seconds** or **30 seconds** from the time controls (element 6)
5. Click **[Advance]** -- watch fleets move and weapons fire resolve
6. Check the **Events Display** on the map (if enabled in layers) for combat results
7. Continue short increments until combat resolves
8. The **Fleet Interception Interrupt** (for increments >= 1 hour) automatically shortens advances when ships approach within 500,000 km of hostile targets

### Selecting and Issuing Orders from the Map

1. **Left-click** a fleet on the map to select it (it highlights and shows info in element 7)
2. **Right-click** on a destination (planet, jump point, waypoint, empty space)
3. From the popup menu, select the movement action
4. The fleet plots a course (visible as a movement line if Ship Paths layer is enabled)
5. For complex orders, right-click the fleet and select it to open the full Naval Organization window
6. The fleet begins executing its new orders on the next time advance

### Measuring Engagement Distances

1. Hold **Shift** on the keyboard
2. Click and **drag** from your fleet's position toward the contact or target location
3. The distance measurement displays in kilometres along the line
4. Release Shift to clear, or drag the endpoint to measure multiple distances from the same origin
5. Compare measured distance against weapon ranges and sensor detection envelopes
6. This is invaluable for determining whether to close range or maintain standoff distance

### Navigating Between Systems

1. Use the **System Selector** dropdown (element 2) to switch between explored systems
2. Alternatively, click a **Jump Point** on the map and select it from the right-click popup to transition to the destination system
3. Use **Alt+F11 / Alt+F12** to cycle through previously-viewed locations across systems
4. Color-coding in the system list: light green = has populated colonies, dark green = has automated installations

## Tips and Shortcuts

- **Mouse wheel zoom centers on cursor position** -- point at the area of interest before scrolling to zoom directly to it without panning.
- **Keep Tactical in Background** option (in settings) prevents the map from covering other windows when you open new panels from the toolbar.
- **Alt+F11 / Alt+F12** for location history cycling is faster than manually searching for previously-viewed positions. Works across star systems.
- **Double-click events** displayed on the map to center the view on the event's location -- same behavior as in the Events Window.
- **Reduce display clutter** by disabling moon orbits, asteroids, and sensor ranges during peacetime. Re-enable sensor ranges when hostiles are detected.
- **Right-click popup** is the fastest way to open the Naval Organization or Economics window for a specific fleet or colony -- no searching through lists required.
- **Shift+drag** distance measurement allows checking engagement ranges without committing to orders. Verify your beam weapons can reach before closing.
- **Sub-pulse processing** (5-second intervals within any increment) means ships never "teleport past" enemies even during 30-day advances. The system correctly resolves encounters during transit.
- **Fleet movement lines** (Ship Paths layer) show exactly where your groups are heading. If a line passes near a hostile contact, consider adding intermediate waypoints to route around.
- **Sensor range circles** reveal blind spots in your coverage. Position picket ships to close gaps, especially around jump points.
- **System blocking** on the Galactic Map prevents auto-route from using dangerous systems. Mark systems with known hostile presence.
- **SpaceMaster mode** reveals all systems and objects regardless of sensor detection -- useful for debugging fleet positions but not for normal gameplay.
- **Wide view** (1900px) provides extra horizontal space. Use it on larger monitors for better spatial awareness during complex multi-fleet operations.

## Related Sections

- [Section 3.1 Main Window](../3-user-interface/3.1-main-window.md) -- Time controls, toolbar, screen resolution, and background mode
- [Section 3.2 System Map](../3-user-interface/3.2-system-map.md) -- Full documentation of map features, layers, and object selection
- [Section 9.5 Orders](../9-fleet-management/9.5-orders.md) -- Movement and combat orders issuable from the map
- [Section 10 Navigation](../10-navigation/) -- Movement mechanics, jump transit, and waypoints
- [Section 11 Sensors and Detection](../11-sensors-and-detection/) -- Sensor ranges, contact detection, and signature types
- [Section 12 Combat](../12-combat/) -- Tactical combat resolution on the system map
