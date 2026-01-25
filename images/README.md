# UI Reference Images

This directory contains text-based UI layout references for Aurora C# game windows. Each file provides an annotated ASCII-art diagram of a major game interface, with numbered callouts explaining every element, common workflows, and practical tips.

## Why Text-Based References

Actual screenshots of Aurora C# require a running instance of the game on Windows (Aurora C# is a Windows-only application using .NET/WinForms). Since screenshots cannot be captured in all documentation environments, these text-based references serve as the authoritative layout descriptions until proper screenshot annotations can be produced.

The ASCII-art diagrams use standard box-drawing characters (`+--+`, `|  |`) and numbered callouts (`[1]`, `[2]`, etc.) to identify interface elements. Each numbered callout corresponds to a detailed description below the diagram.

## UI Reference Files

| # | File | Window | Description |
|---|------|--------|-------------|
| 1 | [ship-design-window.md](ship-design-window.md) | Class Design | Ship class creation: component selection, performance stats, design management |
| 2 | [missile-design-window.md](missile-design-window.md) | Missile Design | Missile ordnance design: MSP allocation, warhead/engine/sensor configuration |
| 3 | [fleet-window.md](fleet-window.md) | Fleet/Task Group | Fleet management: task groups, movement orders, combat orders, fleet status |
| 4 | [system-map-window.md](system-map-window.md) | Tactical/System Map | System visualization: orbital bodies, fleets, contacts, sensor overlays |
| 5 | [colony-window.md](colony-window.md) | Colony/Population | Colony management: installations, construction, minerals, environment |
| 6 | [ground-forces-window.md](ground-forces-window.md) | Ground Forces | Ground combat: formation design, unit classes, training, transport |
| 7 | [diplomacy-window.md](diplomacy-window.md) | Intelligence/Foreign Relations | Diplomacy: race relations, treaties, intelligence, territory claims |
| 8 | [research-window.md](research-window.md) | Research | Technology research: scientist assignment, project selection, progress |
| 9 | [shipyard-window.md](shipyard-window.md) | Shipyard Management | Ship construction: build queues, refits, slipway management |
| 10 | [event-log-window.md](event-log-window.md) | Event Log | Event notifications: filtering, categories, interrupts, colour coding |

## File Format

Each UI reference file follows a consistent structure:

1. **Title and Introduction** -- Window name, purpose, and access method (toolbar button, keyboard shortcut).
2. **ASCII Art Diagram** -- Box-drawing layout showing the window's major panels, lists, buttons, and data displays. Numbered callouts `[1]` through `[N]` mark each distinct interface element.
3. **Element Descriptions** -- Detailed explanation of each numbered element: what data it shows, what actions it enables, and how it interacts with other elements.
4. **Common Workflows** -- Step-by-step procedures for typical tasks performed in this window (e.g., "Designing a new ship class", "Proposing a treaty").
5. **Tips and Shortcuts** -- Practical advice, keyboard shortcuts, and non-obvious features.
6. **Related Sections** -- Links to relevant manual chapters for deeper reading.

## Guidelines for Future Screenshot Additions

When actual screenshots become available, follow these conventions:

### Capture Settings

- **Resolution**: 1920x1080 (Full HD) capture resolution for consistency across all screenshots.
- **UI Settings**: Use Aurora C#'s default UI settings (standard font size, default colors, no custom themes).
- **Window State**: Capture windows in their default size, not maximized unless the window is inherently full-screen (e.g., the Tactical Map).
- **Game State**: Use a mid-game save with representative data (multiple colonies, fleets, technologies) rather than an empty new-game state.

### File Format and Naming

- **Format**: PNG with lossless compression. Do not use JPEG (lossy artifacts on UI text).
- **Naming**: Match the corresponding `.md` reference file name, replacing the extension:
  - `ship-design-window.md` --> `ship-design-window.png`
  - `diplomacy-window.md` --> `diplomacy-window.png`
- **Annotated Versions**: Create a second file with `-annotated` suffix containing numbered overlay markers matching the callout descriptions:
  - `ship-design-window-annotated.png`
  - `diplomacy-window-annotated.png`
- **Annotation Style**: Use red circles or arrows with white-on-red numbered labels (e.g., a red circle containing "1" in white text). Place annotations adjacent to (not obscuring) the referenced element.

### Organization

```
images/
  README.md                            <-- This file
  ship-design-window.md                <-- Text-based layout reference
  ship-design-window.png               <-- Raw screenshot (future)
  ship-design-window-annotated.png     <-- Annotated screenshot (future)
  diplomacy-window.md                  <-- Text-based layout reference
  diplomacy-window.png                 <-- Raw screenshot (future)
  diplomacy-window-annotated.png       <-- Annotated screenshot (future)
  ...
```

### Content Guidelines

- Avoid showing personally identifiable information or spoiler content in screenshots.
- Redact any file system paths visible in window title bars if they reveal user directory structure.
- Ensure game text is legible at the captured resolution (zoom or resize if needed).

## Forum Screenshot Sources

> **Historical Note:** The pentarch.org domain hosts the official Aurora forums and developer resources. These URLs are preserved as historical references to original Aurora development materials. The forum has been the primary community hub since Aurora's creation, and Steve Walmsley's posted screenshots document the game's evolution. If any URLs become inaccessible in the future, the Internet Archive (archive.org) may have cached copies.

The Aurora C# developer (Steve Walmsley) has posted many UI screenshots in the official forum's C# Changes List thread. These are hosted at `http://www.pentarch.org/steve/Screenshots/` and can be downloaded for inclusion in this manual.

### Known Screenshot URLs by Category

**Ground Forces Window:**

- http://www.pentarch.org/steve/Screenshots/Ground010.PNG
- http://www.pentarch.org/steve/Screenshots/GroundRules004.PNG
- http://www.pentarch.org/steve/Screenshots/GroundRules005.PNG
- http://www.pentarch.org/steve/Screenshots/GroundRules007.PNG
- http://www.pentarch.org/steve/Screenshots/DominantTerrain.PNG
- http://www.pentarch.org/steve/Screenshots/Elements001.PNG
- http://www.pentarch.org/steve/Screenshots/FormationSupport001.PNG
- http://www.pentarch.org/steve/Screenshots/GroundSupport002.PNG through GroundSupport006.PNG

**Combat / Damage Reports:**

- http://www.pentarch.org/steve/Screenshots/FiringSummary002.PNG
- http://www.pentarch.org/steve/Screenshots/DamageReport003.PNG through DamageReport007.PNG
- http://www.pentarch.org/steve/Screenshots/TargetSize.PNG
- http://www.pentarch.org/steve/Screenshots/ArmourGenerations.PNG
- http://www.pentarch.org/steve/Screenshots/DamageControl02.PNG

**Fleet / Automated Assignments:**

- http://www.pentarch.org/steve/Screenshots/AutomatedAssignment001.PNG through AutomatedAssignment011.PNG

**Sensors and Detection:**

- http://www.pentarch.org/steve/Screenshots/NewSensorModel1.PNG through NewSensorModel200.PNG
- http://www.pentarch.org/steve/Screenshots/ELINT01.PNG
- http://www.pentarch.org/steve/Screenshots/ELINT02.PNG

**Economy / Systems:**

- http://www.pentarch.org/steve/Screenshots/PopCapacity.PNG
- http://www.pentarch.org/steve/Screenshots/FuelModelV2.PNG
- http://www.pentarch.org/steve/Screenshots/PowerPlant01.PNG
- http://www.pentarch.org/steve/Screenshots/Minerva.PNG
- http://www.pentarch.org/steve/Screenshots/NewStars.PNG
- http://www.pentarch.org/steve/Screenshots/RenamedStars.PNG

**Logistics:**

- http://www.pentarch.org/steve/Screenshots/Logistics003.PNG through Logistics005.PNG
- http://www.pentarch.org/steve/Screenshots/SupplyVehicle02.PNG

### Source Thread

All screenshots originate from the [C# Aurora Changes List](http://aurora2.pentarch.org/index.php?topic=8495.0) thread on the official Aurora forum (pentarch.org — the official Aurora community hub since 2003). Additional screenshots can be found by browsing through the thread pages. These forum resources are historically significant primary sources for Aurora documentation.

## Fair Use Considerations

Aurora C# is developed by Steve Walmsley and distributed as freeware. Screenshots of the game UI are included in this manual under fair use principles for the purpose of documentation and education. This manual is a non-commercial community reference project. All game content, interface designs, and intellectual property belong to the Aurora C# developer.

If the developer requests removal of any screenshots, they should be replaced with the text-based ASCII references which describe the interface without reproducing copyrighted visual assets.

## Related Manual Sections

- [Section 3.1 Main Window](../3-user-interface/3.1-main-window.md) -- Overview of the Aurora C# interface and toolbar
- [Section 3.2 System Map](../3-user-interface/3.2-system-map.md) -- Tactical map usage and navigation
- [Section 3.3 Common Controls](../3-user-interface/3.3-common-controls.md) -- Shared UI patterns across windows
- [Section 3.4 Event Log](../3-user-interface/3.4-event-log.md) -- Event notification system
- [Section 8.1 Ship Design](../8-ship-design/8.1-design-philosophy.md) -- Ship design concepts
- [Section 9.3 Task Groups](../9-fleet-management/9.3-task-groups.md) -- Fleet organization concepts
- [Section 13.1 Unit Types](../13-ground-forces/13.1-unit-types.md) -- Ground force design details
- [Section 15.1 Alien Races](../15-diplomacy/15.1-alien-races.md) -- Diplomatic mechanics
