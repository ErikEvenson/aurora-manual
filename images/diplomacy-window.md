# Diplomacy Window Layout

*Added: v2026.01.25*

The Diplomacy window (also referred to as the Intelligence and Foreign Relations window) is the primary interface for managing inter-racial relationships, treaties, intelligence gathering, and diplomatic engagement. It consolidates information about known alien races, their disposition toward you, active treaties, contact history, and intelligence summaries. Access it from the main toolbar.

## Window Layout

```
+==============================================================================+

| Intelligence and Foreign Relations                                [_][O][X]  |
+==============================================================================+

|                                                                              |
+------------------------------+-----------------------------------------------+

|                              |                                               |
|  [1] KNOWN RACES LIST        |  [5] RELATIONSHIP DETAILS                     |
|                              |  +-------------------------------------------+|
|  +------------------------+  |  | Race:     Keth'vari Dominion               ||
|  | Race           Status  |  |  | Status:   NEUTRAL (+12 points)            ||
|  |----------------|--------|  |  | Xenophobia: 45/100                        ||
|  | Keth'vari Dom  Neutral |  |  | Militancy:  62/100                        ||
|  | Vrenn Confed   Friendly|  |  | Determination: 55/100                     ||
|  | Skaal Empire   Hostile |  |  | Diplomacy:  38/100                        ||
|  | Terran Rebels  Allied  |  |  | Trade:      51/100                        ||
|  | Quel Compact   Neutral |  |  | Government: Authoritarian Monarchy        ||
|  | (Minor) Felk   Neutral |  |  | Expansion:  Moderate                      ||
|  |                        |  |  | Language:   42% translated                 ||
|  |                        |  |  +-------------------------------------------+|
|  +------------------------+  |                                               |
|                              |  [6] DIPLOMATIC POINTS BREAKDOWN              |
|  [2] RACE FILTER             |  +-------------------------------------------+|
|  +------------------------+  |  | Active Diplomacy:  +108 pts/year           ||
|  | Status: [All       v]  |  |  | Treaty Generation: +55 pts/year            ||
|  | [x] Show Minor Races   |  |  | Intrusion Penalty: -23 pts/year            ||
|  | [x] Show Contacted     |  |  | Passive Decay:     -8 pts/year             ||
|  | [ ] Show Pre-Contact   |  |  | Net Change:        +132 pts/year           ||
|  +------------------------+  |  | Time to Friendly:  ~36 days                ||
|                              |  +-------------------------------------------+|
|  [3] COMMUNICATION OPTIONS   |                                               |
|  +------------------------+  |  [7] ACTIVE TREATIES                          |
|  | [Propose Treaty     ]  |  |  +-------------------------------------------+|
|  | [Declare War        ]  |  |  | Treaty              | Base Pts/Yr | Since  ||
|  | [Set Protection     ]  |  |  |---------------------|-------------|--------||
|  | [Assign Diplomat    ]  |  |  | Trade Agreement     | +100        | 2145.3 ||
|  | [SM Race Title      ]  |  |  | Geo Survey Treaty   | +100        | 2146.1 ||
|  +------------------------+  |  | (Modified by Xenophobia: x0.55)            ||
|                              |  +-------------------------------------------+|
|  [4] TREATY PROPOSALS        |                                               |
|  +------------------------+  |  [8] TERRITORY STATUS                         |
|  | Available Treaties:    |  |  +-------------------------------------------+|
|  | +--------------------+ |  |  | System        | Value    | Protection      ||
|  | | Trade Agreement    | |  |  |---------------|----------|-----------------|
|  | | Geo Survey Treaty  | |  |  | Alpha Cent    | Claimed  | No Protection   ||
|  | | Grav Survey Treaty | |  |  | Barnard's     | Secondary| Suggest Leave   ||
|  | | Research Treaty    | |  |  | Wolf 359      | Primary  | Demand Leave    ||
|  | +--------------------+ |  |  | Sirius        | Core     | Demand + Threat ||
|  |                        |  |  +-------------------------------------------+|
|  | Requires: Friendly+    |  |                                               |
|  | (Research: Allied)     |  |                                               |
|  +------------------------+  |                                               |
|                              |                                               |
+------------------------------+-----------------------------------------------+

|                                                                              |
|  [9] CONTACT HISTORY                                                         |
|  +--------------------------------------------------------------------------+|
|  | Date     | Event                              | Points | Cumulative      ||
|  |----------|-------------------------------------|--------|-----------------|
|  | 2145.127 | First Contact (survey detection)   |   0    |      0          ||
|  | 2145.130 | Diplomat assigned (Cdr. Williams)   |  --    |      0          ||
|  | 2145.200 | Trade Agreement proposed (accepted) | +100/yr|    +27          ||
|  | 2146.015 | Ships detected in Barnard's         |  -45   |    +94          ||
|  | 2146.030 | Geo Survey Treaty signed            | +100/yr|   +112          ||
|  | 2146.098 | Intrusion warning received (lvl 2)  |  -23   |   +132          ||
|  +--------------------------------------------------------------------------+|
|                                                                              |
|  [10] INTELLIGENCE SUMMARY                                                   |
|  +--------------------------------------------------------------------------+|
|  | Fleet Strength (estimated):  ~85 ships detected | ~2.1M tons total       ||
|  | Tech Level (estimated):      Comparable (beam weapons, moderate shields) ||
|  | Colonies Known:              3 populations detected                       ||
|  | ELINT Coverage:              1 population monitored (234/500 pts)         ||
|  | Racial Intel Points:         67/100 (next espionage check)                ||
|  | Captured Officers:           None                                         ||
|  | Known Ship Classes:          4 classes identified                          ||
|  +--------------------------------------------------------------------------+|
|                                                                              |
|  [11] DIPLOMAT ASSIGNMENT                                                    |
|  +--------------------------------------------------------------------------+|
|  | Assigned:   Cdr. Elena Williams | Diplomacy Bonus: +20%                   ||
|  | Location:   Alpha Centauri (Diplomacy Module ship: DCS Envoy)             ||
|  | Points/Yr:  ((0.20 x 4) + 1) x 100 x (1 - 0.45) = +108                  ||
|  | [Change Diplomat]  [Remove Assignment]                                    ||
|  +--------------------------------------------------------------------------+|
+==============================================================================+
```

## Element Descriptions

### [1] Known Races List
The left panel lists all alien races your civilization has detected or made contact with. Each entry shows the race name and current relationship status (Hostile, Unfriendly, Neutral, Friendly, or Allied). The status is determined by accumulated diplomatic points against defined thresholds. Minor Races are indicated with a "(Minor)" prefix. Click a race to populate all detail panels on the right.

### [2] Race Filter
Filters the race list by relationship status and contact type. "Show Minor Races" includes the reduced-capability civilizations (v2.4.0+). "Show Contacted" displays races with established communication. "Show Pre-Contact" reveals detected but not-yet-communicated races (useful for planning diplomatic outreach).

### [3] Communication Options
Action buttons for diplomatic interactions with the selected race:

- **Propose Treaty**: Opens the treaty proposal interface (requires sufficient relationship level).
- **Declare War**: Sets the relationship to hostile and enables military engagement. Cannot be undone quickly.
- **Set Protection**: Assigns a protection status to your systems, warning the selected NPR to withdraw (see territory mechanics below).
- **Assign Diplomat**: Designate a commander with Diplomacy bonus to actively generate diplomatic points with this race.
- **SM Race Title**: (SpaceMaster) Rename an NPR's species name or race title at any time.

### [4] Treaty Proposals
Lists available treaty types that can be proposed to the selected race. Each treaty has a relationship threshold requirement:

- **Trade Agreement**: Requires Neutral or better (+100 base pts/year).
- **Geological Survey Treaty**: Requires Neutral or better (+100 base pts/year).
- **Gravitational Survey Treaty**: Requires Neutral or better (+100 base pts/year).
- **Research Treaty**: Requires Allied status (+200 base pts/year).

All treaty point generation is modified by the target race's Xenophobia: `Base x (1 - Xenophobia/100)`.

### [5] Relationship Details
Comprehensive profile of the selected race's characteristics:

- **Status and Points**: Current relationship tier and exact diplomatic point value.
- **Personality Attributes**: Xenophobia (distrust of aliens), Militancy (willingness to use force), Determination (stubbornness), Diplomacy (negotiation willingness), and Trade (economic cooperation interest).
- **Government Type**: May affect diplomatic tendencies and internal policies *(unverified -- government types were removed from player race creation in C#)*.
- **Expansion Drive**: How actively the NPR colonizes and builds fleets.
- **Language Progress**: Percentage of the alien language translated; full translation eliminates the 80% ELINT/interrogation penalty.

### [6] Diplomatic Points Breakdown
Shows the mathematical breakdown of how diplomatic points are changing over time:

- **Active Diplomacy**: Points generated by your diplomat commander's presence (formula: `((Bonus x 4) + 1) x 100 x (1 - Xenophobia/100)`).
- **Treaty Generation**: Sum of all active treaty point contributions.
- **Intrusion Penalty**: Negative points from your forces detected in NPR-claimed territory.
- **Passive Decay**: Natural drift toward zero when contact lapses.
- **Net Change**: Combined annual rate determining relationship trajectory.
- **Time to Next Tier**: Estimated days until the next relationship threshold is reached.

### [7] Active Treaties
Lists all currently active agreements with the selected race, showing the treaty type, base points generated per year, and the date the treaty was signed. The Xenophobia modifier note shows the effective multiplier applied to all treaty point generation for this particular race.

### [8] Territory Status
Displays the selected NPR's known system value assignments and your current protection statuses for contested systems. System values range from Neutral (1) to Capital (6). Protection statuses range from "No Protection" to "Demand Leave with Threat", each carrying escalating diplomatic penalties if the NPR refuses. Intrusion warnings only trigger for systems valued at Secondary (3) or higher.

### [9] Contact History
A chronological log of all significant diplomatic events with the selected race. Each entry shows the date (year.day format), event description, point impact, and cumulative diplomatic point total at that time. Events include first contact, treaty proposals/acceptances/rejections, intrusion warnings, combat incidents, and diplomat assignments. This history is invaluable for understanding why a relationship is at its current level.

### [10] Intelligence Summary
Aggregates all intelligence gathered on the selected race through ELINT operations, interrogation of captured crew, and direct observation:

- **Fleet Strength**: Estimated ship count and total tonnage based on observations.
- **Tech Level**: Qualitative assessment based on observed weapons, shields, and engine performance.
- **Colonies Known**: Number of alien populations your sensors have detected.
- **ELINT Coverage**: Which populations are being actively monitored and current intelligence point progress toward the next threshold (100/200/300/500 points for progressively more detailed information).
- **Racial Intel Points**: Progress toward the next automated espionage check (occurs at 100 points).
- **Captured Officers**: Rank of any captured officers providing intelligence (higher rank = exponentially more intel: rank^3 points).
- **Known Ship Classes**: Number of alien ship classes you have identified through observation or espionage.

### [11] Diplomat Assignment
Shows the currently assigned diplomat commander, their Diplomacy bonus percentage, their physical location (system and ship name), and the calculated annual diplomatic point generation rate. The formula is displayed for transparency. Use "Change Diplomat" to assign a different commander or "Remove Assignment" to recall the diplomat entirely.

## Common Workflows

### Proposing a Treaty

1. Select the target race from the Known Races List [1].
2. Verify the Relationship Details [5] show sufficient status (Neutral+ for most treaties, Allied for Research).
3. Check the Treaty Proposals panel [4] for available options.
4. Click **Propose Treaty** in Communication Options [3].
5. Select the desired treaty type from the popup.
6. The NPR evaluates the proposal based on its Diplomacy and Trade attributes.
7. If accepted, the treaty appears in Active Treaties [7] and begins generating points.
8. Monitor Contact History [9] for the acceptance/rejection event.

### Checking Relationship Status

1. Select a race from the Known Races List [1] -- the status column gives a quick overview.
2. Review Relationship Details [5] for the exact point value and personality attributes.
3. Check Diplomatic Points Breakdown [6] to understand whether relations are improving or declining.
4. Note the "Time to Next Tier" estimate for planning purposes.
5. Review Contact History [9] to identify events causing point changes (especially negative ones).

### Assigning a Diplomat

1. Ensure you have a ship equipped with a **Diplomacy Module** (30 HS, 300 BP, 50 crew).
2. Assign a commander with a Diplomacy bonus to that ship.
3. Move the ship to a system where you have contact with the target race.
4. Select the target race in the Known Races List [1].
5. Click **Assign Diplomat** in Communication Options [3].
6. Select the commander from the available list.
7. The Diplomat Assignment panel [11] updates with the calculated point generation rate.
8. Without a Diplomacy Module, positive diplomatic gains are halved.

### Setting Territory Protection

1. Select the NPR whose intrusion you want to address.
2. Click **Set Protection** in Communication Options [3].
3. Choose the target system from your controlled systems list.
4. Select a protection level (Suggest Leave through Demand Leave with Threat).
5. The NPR evaluates whether to withdraw using the claim acceptance formula:
   `Military Advantage x Demand Value x Population Factor > System Value x Resistance`
6. If the NPR refuses, protection resets to "No Protection" automatically.
7. Monitor the diplomatic penalty in Contact History [9].

### Reviewing Contact History

1. Select a race from the Known Races List [1].
2. Scroll through the Contact History panel [9] chronologically.
3. Look for large negative point events (combat incidents, intrusion detections).
4. Identify patterns: repeated intrusion warnings suggest you need to address territorial overlap.
5. Use cumulative point tracking to understand the relationship trajectory over time.

### Gathering Intelligence via ELINT

1. Equip ships with ELINT modules.
2. Position ships within sensor range of target race populations.
3. Monitor the Intelligence Summary panel [10] for point accumulation.
4. At 100 population intel points: population size and installations revealed.
5. At 200 points: factories, mines, and spaceport data.
6. At 300 points: refineries and maintenance facilities.
7. At 500 points: research and training facility details.
8. Ensure language translation progress to avoid the 80% intelligence penalty.

## Tips and Shortcuts

- **Xenophobia Dominates Diplomacy**: A race with 80% Xenophobia generates diplomatic points at only 20% of base rate. Against highly xenophobic races, military deterrence may be more practical than diplomatic investment.
- **Diplomat Module Matters**: Without a Diplomacy Module on your diplomat's ship, all positive point gains are halved. The 30 HS investment pays for itself rapidly.
- **Language First**: Untranslated languages impose an 80% penalty on both ELINT intelligence and interrogation yields. Prioritize language research for races you plan to interact with.
- **Attack Diplomatic Ships Last**: Attacking ships with Diplomacy Modules incurs TRIPLE the normal diplomatic penalty (-300 vs -100 for unprovoked attacks). Be very sure you want war before engaging a diplomat.
- **Treaty Stacking**: Multiple treaties stack their point generation. A Trade + Geo Survey + Grav Survey combination generates 300 base pts/year (modified by Xenophobia).
- **Intrusion Math**: Diplomatic ships receive a 10,000-ton deduction per system in intrusion calculations. Sending diplomats first reduces the territorial penalty of subsequent fleet movements.
- **Protection Escalation**: Start with "Suggest Leave" rather than "Demand Leave with Threat." Each escalation level increases the diplomatic penalty if refused, calculated as `(Demand^2) x (System Value^2) x (Xenophobia/50)`.
- **Intelligence Decay**: ELINT points decay at 25% per year when monitoring ceases. Maintain persistent coverage or accept the need to rebuild intelligence.
- **NPR Tells**: If an NPR masses ships near a jump point to your territory, take it seriously. NPRs do not bluff -- fleet movements indicate intent. Check the Intelligence Summary for fleet strength estimates.
- **Same Atmosphere Competition**: If an alien race breathes the same atmosphere as your species, you are competing for the same habitable worlds. Incompatible atmospheric requirements create natural coexistence opportunities.
- **Human NPR Bonus**: Races sharing your primary species receive a +20 communication bonus, accelerating language development and diplomatic engagement.
- **Minor Race Opportunity**: Minor Races cannot expand beyond their home system without gate access. They make low-risk trading partners and diplomatic practice targets.

## References

\hypertarget{ref-img-diplomacy-1}{[1]}. Aurora C# game interface -- Diplomacy window layout verified against v2.7.1 game client. Treaty types, diplomatic status progression, and communication mechanics.

---

## Related Sections

- [Section 2.1 New Game Options](../2-game-setup/2.1-new-game-options.md) -- Configuring NPR generation, hostility modifiers, and game options
- [Section 11.1 Thermal and EM Signatures](../11-sensors-and-detection/11.1-thermal-em-signatures.md) -- ELINT modules and sensor mechanics for intelligence gathering
- [Section 12.1 Fire Controls](../12-combat/12.1-fire-controls.md) -- Combat diplomatic penalties and engagement rules
- [Section 15.1 Alien Races](../15-diplomacy/15.1-alien-races.md) -- Full diplomatic mechanics, NPR behavior, and territory rules
- [Section 15.2 Communications](../15-diplomacy/15.2-communications.md) -- Language translation and communication mechanics
- [Section 16.2 Skills and Bonuses](../16-commanders/16.2-skills-and-bonuses.md) -- Diplomacy bonus mechanics for commanders
- [Section 17.1 Geological Survey](../17-exploration/17.1-geological-survey.md) -- Survey ships and first contact encounters
- [Appendix A: Formulas](../appendices/A-formulas.md) -- Diplomatic point calculation formulas
