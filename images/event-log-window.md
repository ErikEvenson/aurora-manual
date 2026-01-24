# Event Log Window Layout

The Event Log (also called the Events Window) is Aurora C#'s primary communication channel to the player. Since the game processes events in batches during time advances rather than in real-time, the Event Log records everything significant that occurred during each increment. Learning to read, filter, and respond to events is a core gameplay skill. The event-check loop (advance time, check events, respond, repeat) is the fundamental rhythm of Aurora gameplay.

Events can also be displayed directly on the Tactical Map (controlled by the Events checkbox in the map layer toggles), using the same colour coding as the Events Window. Double-clicking any event centers the map on the event's location.

## Window Layout Diagram

```
+============================================================================+
|  Events Window                                                        [X]  |
+============================================================================+
| [1] Date/Increment Header                                                  |
| 14 March 2150  08:00:00  -  Increment: 5 days                             |
+============================================================================+
| [2] Filter Controls                                                        |
|                                                                            |
| [x] Combat/Military    [x] Exploration    [x] Research    [x] Economic     |
| [x] Colony             [x] Commander      [x] Diplomacy   [x] Misc/System  |
|                                                                            |
| [3] Sub-Filters:  [ ] Ship Movements  [x] Mineral Finds  [x] Fuel Warns   |
|                   [x] Hostile Contacts [x] Damage Reports [ ] Promotions   |
|                                                                            |
+============================================================================+
| [4] Event Log Entries (Main Area)                                          |
|                                                                            |
| +------------------------------------------------------------------------+ |
| | Date/Time          | Category    | Event Description                   | |
| |--------------------+-------------+-------------------------------------| |
| | 14 Mar 2150 08:00  | COMBAT      | Hostile contact detected in Sol     | |
| |                    |             | system. Thermal signature bearing   | |
| |                    |             | 045, range 182Mkm, est. 8,000t     | |
| | [BG: RED   TXT: WHITE]          |                                     | |
| |--------------------+-------------+-------------------------------------| |
| | 14 Mar 2150 08:00  | COMBAT      | DD Valiant engaging target with     | |
| |                    |             | 10cm Railgun battery. 3 hits,      | |
| |                    |             | target armor penetrated.           | |
| | [BG: RED   TXT: WHITE]          |                                     | |
| |--------------------+-------------+-------------------------------------| |
| | 13 Mar 2150 14:30  | RESEARCH    | Research Complete: Fire Control     | |
| |                    |             | Range 80,000km. New options         | |
| |                    |             | available in Component Design.      | |
| | [BG: BLUE  TXT: WHITE]          |                                     | |
| |--------------------+-------------+-------------------------------------| |
| | 12 Mar 2150 00:00  | EXPLORATION | Geological Survey Complete: Mars.   | |
| |                    |             | 5 mineral deposits found.           | |
| |                    |             | Duranium: 2,400t (Acc: 0.7)        | |
| | [BG: GREEN TXT: BLACK]          |                                     | |
| |--------------------+-------------+-------------------------------------| |
| | 11 Mar 2150 16:00  | ECONOMIC    | Construction Complete: DD Stalwart  | |
| |                    |             | (Tribal-class) at Earth Shipyard.   | |
| |                    |             | Ship assigned to default TG.        | |
| | [BG: CYAN  TXT: BLACK]          |                                     | |
| |--------------------+-------------+-------------------------------------| |
| | 10 Mar 2150 12:00  | COLONY      | Terraforming progress: Mars atmos.  | |
| |                    |             | O2 increased to 0.12 atm.          | |
| | [BG: DKGRN TXT: WHITE]          |                                     | |
| |--------------------+-------------+-------------------------------------| |
| | 10 Mar 2150 00:00  | ECONOMIC    | Mineral Depletion Warning: Gallicite| |
| |                    |             | deposit at Asteroid Colony #3       | |
| |                    |             | exhausted. 0 remaining deposits.    | |
| | [BG: YELLOW TXT: BLACK]         |                                     | |
| |--------------------+-------------+-------------------------------------| |
| | 09 Mar 2150 20:00  | COMMANDER   | Promotion: Lt. Williams promoted    | |
| |                    |             | to Lt. Commander (experience).      | |
| | [BG: GRAY  TXT: BLACK]          |                                     | |
| |--------------------+-------------+-------------------------------------| |
| |                    (scrollable -- additional events below)              | |
| +------------------------------------------------------------------------+ |
|                                                                            |
+============================================================================+
| [5] Event Detail Expansion                                                 |
|                                                                            |
| Selected: "Hostile contact detected in Sol system"                         |
| System: Sol  |  Location: X: 142.3  Y: -87.6 Mkm                          |
| Detection: Thermal (2,100 rating)  |  Est. Tonnage: 8,000                  |
| Detecting Ship: DD Valiant (Active Sensor Res-100)                         |
| Interrupt: YES (time advance halted at this event)                         |
|                                                                            |
+============================================================================+
| [6] Colour Configuration                                                   |
|                                                                            |
| Event Type: [Combat/Military___v]   BG Colour: [###RED###]                 |
|                                     Text Colour: [##WHITE##]               |
| [Apply] [Reset Default]    [7] [Import Colours] [Export Colours]           |
|                                                                            |
+============================================================================+
| [8] Auto-Scroll / Navigation Controls                                      |
|                                                                            |
| [x] Auto-scroll to latest    [<< Previous Increment] [Next Increment >>]  |
| [ ] Show all races (SM only)  Events this increment: 7  |  Total: 2,341   |
|                                                                            |
+============================================================================+
| [9] Interrupt Configuration                                                |
|                                                                            |
| Interrupt on: [x] Hostile Contact  [x] Damage  [x] Ship Destroyed         |
|               [ ] Research Complete  [ ] Construction Complete              |
|               [ ] Fleet Arrival     [x] Jump Point Discovered              |
|                                                                            |
+============================================================================+
```

## Element Descriptions

| # | Element | Description |
|---|---------|-------------|
| 1 | **Date/Increment Header** | Shows the current game date and time at the top of the log, plus the time increment that was just processed. Displayed even if no events occurred during the increment. Matches the format shown on the tactical map events display. |
| 2 | **Filter Controls (Category)** | Major category checkboxes to show/hide entire classes of events: Combat/Military, Exploration, Research, Economic, Colony, Commander, Diplomacy, and Miscellaneous/System. Unchecking a category hides all events of that type from the display. |
| 3 | **Sub-Filters** | Granular toggles within categories for specific event subtypes. Examples: Ship Movements (routine transit notifications), Mineral Finds, Fuel Warnings, Hostile Contacts, Damage Reports, Promotions. Allows fine-tuning what appears without disabling entire categories. |
| 4 | **Event Log Entries (Main Area)** | Scrollable list of timestamped events. Each entry shows: date/time of occurrence, category label, and the event description text. Entries use configurable background and text colours per event type for rapid visual identification. Events are listed chronologically with most recent at top. |
| 5 | **Event Detail Expansion** | When an event is selected (clicked), this panel shows expanded information: the system where the event occurred, precise coordinates, detection details, the ship or installation involved, and whether the event triggered a time interrupt. Double-clicking an event centers the tactical map on the event location. |
| 6 | **Colour Configuration** | Per-event-type colour settings. Select an event type from the dropdown, then choose background and text colours. Custom colours persist across game sessions and apply to both the Events Window and the tactical map events display. |
| 7 | **Import/Export Colours** | Buttons to save and load colour configuration files (CSV format containing Event ID, Background Colour, and Text Colour). Enables sharing colour schemes across races and games. Partial imports only update referenced event types, leaving others unchanged. |
| 8 | **Auto-Scroll / Navigation** | Auto-scroll toggle keeps the display scrolled to the latest events. Navigation buttons step through events by increment (Previous/Next Increment shows events from the prior or next time advance). Counter shows events in current increment and total event count. SM mode option shows events for all player races. |
| 9 | **Interrupt Configuration** | Checkboxes controlling which event types halt time advancement automatically. Critical events (Hostile Contact, Damage, Ship Destroyed) are typically always enabled. Optional interrupts (Research Complete, Construction Complete, Fleet Arrival) balance awareness against fragmented time advances. |

## Event Categories Reference

| Category | Colour (Default) | Key Events |
|----------|-------------------|------------|
| **Combat/Military** | Red background, white text | Hostile contact, weapons fire, ship destroyed, missile launch/impact, shield/armor damage, crew casualties |
| **Exploration** | Green background, black text | Jump point discovered, new system explored, geological survey complete, minerals found |
| **Research** | Blue background, white text | Research complete, breakthrough, new technology available, project initiation |
| **Economic** | Cyan background, black text | Construction complete, shipyard task complete, mineral depletion, fuel warnings, industrial project start |
| **Colony** | Dark green background, white text | Colony established, terraforming progress, infrastructure alerts, unrest/stability |
| **Commander** | Gray background, black text | Promotion, retirement/death, new commander available, assignment changes |
| **Diplomacy** | Purple background, white text | First contact, diplomatic status change, treaty offers, espionage results |
| **Misc/System** | Default/no highlight | Deployment time exceeded, fighter construction, movement completion |

## Common Workflows

### Finding Combat Events

1. In **Filter Controls** (element 2), uncheck all categories except **Combat/Military**
2. The log now shows only combat-related events: contacts, weapons fire, damage, and destruction
3. Scroll through to reconstruct the engagement timeline
4. Click individual events to expand details (element 5) -- see which ships fired, what was hit, damage dealt
5. Double-click events to center the tactical map on the combat location
6. Check for "Ship Destroyed" events to confirm kills and assess losses
7. After review, re-enable other categories to return to full event view

### Filtering by Category

1. Identify your current focus (peacetime development, combat, exploration, etc.)
2. **Peacetime**: Enable Research, Economic, Colony; disable Combat, Commander (routine), Misc
3. **Combat**: Enable Combat/Military only; disable everything else for clarity
4. **Exploration**: Enable Exploration; optionally add Research (for survey-related tech) and Economic (for mineral finds)
5. **Economic Build-Up**: Enable Economic, Colony; disable Exploration, Combat, Commander
6. Use **Sub-Filters** (element 3) for finer control: disable routine ship movements but keep fuel warnings enabled
7. Filter settings persist until changed -- adjust as your gameplay focus shifts

### Reviewing Events After Time Advance

1. After clicking **[Advance]**, the Event Log automatically populates with new events
2. If **Auto-scroll** is enabled (element 8), the display jumps to the latest events
3. Scan event colours first for rapid triage: red = combat (urgent), yellow = warnings, blue = research (positive)
4. Address **interrupt events** first -- these halted the advance for a reason
5. Check for **red/combat entries** even if no interrupt occurred (sub-threshold contacts, distant engagements)
6. Note **yellow/warning entries** (fuel depletion, mineral exhaustion) for medium-term planning
7. Acknowledge **blue/green entries** (research complete, survey complete) -- assign new projects or orders
8. Use **[Previous Increment]** / **[Next Increment]** navigation to step through events by time period

### Tracking Mineral Discoveries

1. Enable the **Exploration** category filter and the **Mineral Finds** sub-filter
2. Survey completion events show: body name, number of deposits found
3. Individual mineral entries follow with: mineral type, quantity (tons), and accessibility rating
4. Accessibility above 0.5 is generally worth mining; below 0.3 is marginal
5. Cross-reference with the Mineral Search Window for empire-wide mineral planning
6. Note which systems have critical minerals (Gallicite, Sorium, Uridium) for expansion priorities

### Responding to a Hostile Contact Interrupt

1. Time advance halts automatically -- the interrupt event is highlighted in the log
2. Read the event detail: system, bearing, range, estimated tonnage, detection type
3. Note whether detection is thermal (passive), EM (passive), or active sensor return
4. **Immediately reduce** time increment to 30 seconds or less (element 6 on main window)
5. Double-click the event to center the tactical map on the contact's location
6. Open the Fleet Window to issue combat or evasion orders to nearby task groups
7. Advance at short increments (5s-30s) until the situation is assessed and resolved
8. Only increase increment again once hostiles are destroyed, fled, or identified as non-threatening

### Configuring Event Interrupts

1. Open the **Interrupt Configuration** panel (element 9)
2. **Essential interrupts** (always enable): Hostile Contact, Damage Reports, Ship Destroyed
3. **Recommended interrupts**: Jump Point Discovered (exploration opportunities), Fuel Critical
4. **Optional interrupts**: Research Complete (assign new projects promptly), Construction Complete (commission new ships)
5. **Avoid over-interrupting**: Every interrupt fragments time advances. In large games with many events, excessive interrupts make advancing even one day tedious
6. Balance awareness against gameplay flow -- critical safety events always interrupt, nice-to-know events can wait until you check the log

## Tips and Shortcuts

- **Colour-code aggressively**: Set distinct, high-contrast colours for event types you care most about. Red/white for combat and yellow/black for warnings creates instant visual triage.
- **Import/Export colours** when starting new races or games. Configure once, reuse everywhere via CSV files.
- **Double-click events** to jump the tactical map to the event location. This is the fastest way to find where something happened spatially.
- **Hostile Contact is always an interrupt** -- never disable this. An undetected enemy fleet approaching during a 30-day advance means 30 days of uncontrolled combat.
- **Mineral Depletion warnings** are not emergencies but represent future bottlenecks. Note them and plan expansion to alternative sources within 1-2 years.
- **"Deployment Time Exceeded"** events (v1.9.0+) warn that ships need maintenance rotation. Set conditional orders to auto-return for overhaul when deployment exceeds limits.
- **Combat events during long advances** do not mean you missed the combat. Sub-pulse processing (5-second intervals) correctly resolved the engagement. The events show the results.
- **Research Complete events** are opportunities: immediately open the Research Window and assign the freed scientist to a new project. Idle scientists waste time.
- **Pattern recognition**: Multiple "Hostile Contact" events in the same system over several advances suggests an NPR is actively scouting your space. Prepare defenses.
- **SM Mode multi-race display** (element 8) shows events for all player races with a faction column. Invaluable for referees managing multiplayer campaigns.
- **Events on the tactical map** (enabled via layer toggles) provide spatial context for events without switching windows. The first line always shows date and increment even with no events.
- **The Event Log tells your empire's story**: sequences of events create narrative arcs. Many players use the log as the basis for After-Action Reports and campaign journals.

## Critical Events to Watch For

| Event | Urgency | Response |
|-------|---------|----------|
| Hostile Contact | IMMEDIATE | Reduce increment, assess threat, issue orders |
| Ship Destroyed (yours) | IMMEDIATE | Assess battle outcome, reinforce or retreat |
| Fuel Critical | HIGH | Redirect to refuelling, check conditional orders |
| Mineral Depletion (Gallicite/Sorium) | HIGH | These are engine/fuel minerals -- find alternatives |
| Jump Point Discovered | MEDIUM | Send scouts, assess exploration priority |
| Research Complete | MEDIUM | Reassign scientist, review new design options |
| Deployment Exceeded | MEDIUM | Schedule overhaul rotation |
| Construction Complete (ship) | LOW | Commission, assign to fleet, give orders |
| Mineral Depletion (other) | LOW | Note for long-term planning |
| Commander Promotion | LOW | Review assignments if skills improved significantly |

## Related Sections

- [Section 3.1 Main Window](../3-user-interface/3.1-main-window.md) -- Time controls, interrupt mechanics, colour import/export
- [Section 3.2 System Map](../3-user-interface/3.2-system-map.md) -- Events displayed on the tactical map, double-click centering
- [Section 3.4 Event Log](../3-user-interface/3.4-event-log.md) -- Full documentation of event types, filtering, and event-driven gameplay
- [Section 11 Sensors and Detection](../11-sensors-and-detection/) -- Contact detection events and sensor mechanics
- [Section 12 Combat](../12-combat/) -- Combat event resolution and damage reports
- [Section 7.1 Technology Tree](../7-research/7.1-technology-tree.md) -- Research completion events
