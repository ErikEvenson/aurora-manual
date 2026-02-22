# Aurora 4X Playthrough Guide

*Created: v2026.02.20*

This guide describes how to run a manual-verification playthrough of Aurora C# with Claude making all game decisions and the user executing actions in-game. The purpose is to verify manual accuracy, discover documentation gaps, and identify discrepancies between what the manual says and what the game actually does.

---

## Purpose

1. **Verify manual content** — Test claims, formulas, UI descriptions, and workflows against the live game
2. **Discover documentation gaps** — Find undocumented steps, buttons, or mechanics
3. **File issues** — Create GitHub issues for discrepancies, unverified claims, and missing content
4. **Improve the manual** — Fix errors in real-time as they are discovered
5. **Generate screenshots** — Capture UI screenshots for manual illustrations

## Prerequisites

- Aurora C# installed and runnable on the user's machine
- GitHub Discussion thread created in the "After Action Reports" category
- Discussion title format: `Claude's Game [N] of Aurora` (where N is the game number)
- The user should be prepared to take screenshots and post them to the discussion thread

## Before Starting a New Playthrough (MANDATORY)

**Every new playthrough MUST begin by reviewing all previous After Action Reports.** This prevents repeating mistakes and ensures lessons compound across games.

### Step 1: Fetch All Previous AARs

```bash
# List all AAR discussions
gh api graphql -f query='{
  repository(owner: "ErikEvenson", name: "aurora-manual") {
    discussions(categoryId: "DIC_kwDORAJjec4Cm3bP", first: 50) {
      nodes { number title }
    }
  }
}' --jq '.data.repository.discussions.nodes[] | "#\(.number) \(.title)"'
```

### Step 2: Read Each AAR

For each discussion found, fetch the full comment history and look for the After Action Report comment (typically the last substantive comment):

```bash
# Get the AAR from a specific discussion
gh api graphql -f query='{
  repository(owner: "ErikEvenson", name: "aurora-manual") {
    discussion(number: NNN) {
      comments(last: 5) {
        nodes { body author { login } }
      }
    }
  }
}'
```

### Step 3: Extract Cumulative Lessons

Before making any game decisions, compile a list of:
- All lessons learned from every previous AAR
- All mistakes to avoid (from every "What I Would Do Differently" section)
- All known game mechanics that contradicted the manual
- The current state of issues filed during previous playthroughs

### Previous AAR Index

Update this index after each playthrough:

| Game | Discussion | Date | Key Lesson | Outcome |
|------|-----------|------|------------|---------|
| 1 | [#1346](https://github.com/ErikEvenson/aurora-manual/discussions/1346) | 2026-02-21 | Survey ships need jump drives | Dead end — ships stranded in Sol |
| 2 | [#1350](https://github.com/ErikEvenson/aurora-manual/discussions/1350) | 2026-02-22 | Deployment time, MSP resupply, squadron transit mechanics | P002 lost with all hands; 3 systems explored |

## How the Interaction Works

### Roles

- **Claude** — Makes all strategic decisions, issues one action at a time, posts actions and analysis to the discussion thread
- **User** — Executes each action in-game, takes screenshots, posts screenshots to the discussion, confirms completion

### Communication Protocol

- Claude posts each action as a discussion comment with clear, bolded instructions
- The user executes the action, posts a screenshot, and says "done"
- Claude analyzes the screenshot, posts observations, and gives the next action
- All game decisions and reasoning are documented in the discussion thread

### Key Rules

1. **One action at a time** — Never give the user multiple actions to execute simultaneously
2. **Always request a screenshot** after each action — This is how Claude sees the game state
3. **Post to the discussion thread** — All actions, observations, and decisions go in the thread (not just the chat)
4. **Fix the manual in real-time** — When a discrepancy is found, commit a fix or file an issue immediately
5. **Ask the user to save periodically** — Aurora has no autosave; request saves after milestones
6. **Verify before assuming** — If a screenshot looks different from expectations, investigate rather than assuming

## Game Setup Recommendations

Based on lessons from previous playthroughs:

### Game Settings

| Setting | Recommended | Rationale |
|---------|-------------|-----------|
| Start type | Conventional | Most content to verify |
| Difficulty | 100 | Default, well-documented |
| Systems | 1000 | Default |
| Home System Geo Surveyed | Checked | Saves early busywork |
| Home System Grav Surveyed | **Unchecked** | Gives survey ships work in Sol even without jump drives |
| Spoiler races | Default (unchecked) | Avoid complexity in early games |
| Game name | Include date and "Claude" for identification |

### Critical Design Checklist

Before building any ship, verify the design includes all components needed for its intended mission. This checklist addresses mistakes made in previous playthroughs.

**Survey Ships MUST have:**
- [ ] Survey sensor(s) (gravitational, geological, or both)
- [ ] Engine (commercial for fuel efficiency)
- [ ] **Jump drive** — Non-negotiable. Survey ships without jump drives cannot explore beyond the home system. Design the jump drive component BEFORE the ship class.
- [ ] Sufficient fuel tanks for multi-system range
- [ ] Crew quarters / **deployment time set to 48+ months** (NOT the 3-month default). Game 2 proved that 3-month deployment causes cascading maintenance failures within 4 months.
- [ ] **Maintenance Storage Bays** — Ensure MSP capacity exceeds annual MSP consumption. Game 2's Pathfinder had 75 MSP capacity but 91 annual consumption, leading to MSP exhaustion.

**Survey Ship Standing Orders (correct configuration):**
- [ ] SV: Survey Location (S) — auto-survey gravitational locations
- [ ] Conditional: IF Fuel 20% or Less → Refuel at Colony
- [ ] Conditional: IF Deployment Exceeded → Refuel, Resupply, and Overhaul at Colony
- [ ] Do NOT use "LG: Overhaul at Colony" — it does NOT resupply MSP

**Before clicking "New Ship Class":**
- [ ] All required components have been designed (not just researched)
- [ ] Prototype components have been converted to production via Research Proto + Instant Research
- [ ] Refresh Tech has been clicked to clear any (P) designations

**Before starting shipyard construction:**
- [ ] Ship class has been locked (Lock Design)
- [ ] Shipyard has been retooled to the class (Retool activity, then Set Activity)
- [ ] First retool is free/instant; subsequent retools take time

## Playthrough Phases

### Phase 0: Game Setup Verification

Compare every setting in the New Game Options window against manual Section 2.1. Document any discrepancies. Capture screenshots of:
- Left column (numeric settings)
- Center column (checkboxes)
- Right column (additional settings)
- Race creation window

### Phase 1: Economy Assessment

Open Population and Production (F2) and verify:
- Starting population, installations, and resources match manual Section 2.5
- Research points (IRP) available
- Shipyard count and capacities
- Available scientists per category

### Phase 2: Initial Research

Prioritize technologies needed for the first ship class. Minimum for a survey campaign:
- Jump Point Theory (P&P)
- Fuel Consumption improvements (P&P)
- Engine size/power modifiers (P&P)
- Jump drive techs: efficiency, squadron size, squadron radius (P&P)
- Geological Survey Sensors (S&CS)
- Gravitational Survey Sensors (S&CS)

Assign available scientists to long-term research projects in categories with idle labs.

### Phase 3: Ship Design

Follow the complete prototype-to-production pipeline:

1. **Design components** — Open Class Design (F5), click "Design Tech!", configure each custom component (engines, jump drives), click "Prototype" or "Create"
2. **Research prototypes** — Select prototype component in Class Components view, click "Research Proto", then Instant Research the (P) entry in Economics > Research
3. **Create the ship class** — Select hull type, add all components (enable Prototypes checkbox if needed), rename class
4. **Finalize** — Click "Refresh Tech" to clear (P) designations, then "Lock Design"
5. **Retool shipyard** — In Economics > Shipyards, select a shipyard, change Task Type to "Retool", select the class, click "Set Activity"
6. **Build** — Change Task Type back to "Construction", select class, click "Create Task" for each slipway

### Phase 4: Fleet Operations

- Create task groups and detach ships as needed (Naval Organization, F4)
- Assign movement and survey orders
- Set conditional orders for fuel management (IF fuel < 30%: Refuel at Colony)
- Set standing orders for automated survey operations
- Advance time in appropriate increments

### Phase 5: After Action Report

When the playthrough concludes (either by completing objectives or encountering a dead end), post an After Action Report to the discussion thread covering:

1. **Executive Summary** — One paragraph on what happened
2. **Phase-by-phase review** — What was done and what was learned in each phase
3. **The critical mistake** (if any) — What went wrong and why
4. **Lessons learned** — Numbered list of takeaways
5. **Manual improvements** — Table of issues filed, commits made, and documentation gaps found
6. **What to do differently next time** — Specific changes for the next playthrough

## What to Verify During Play

### High-Priority Verification Targets

| Category | What to Check | Manual Section |
|----------|--------------|----------------|
| Game setup | Default values, checkbox behavior | 2.1, 2.2, 2.5 |
| Research | IRP costs, tech prerequisites, category names | 7.1, 7.4 |
| Ship design | Component sizes, engine classification rules, prototype workflow | 8.1-8.7 |
| Shipyards | Retool mechanics, construction times, slipway behavior | 9.1, 9.2 |
| Orders | Order type names, default actions, standing orders | 9.5 |
| Survey | Survey point rates, sensor stacking, automation | 10.3, 17.1, 17.2 |
| Navigation | Jump transit mechanics, fuel consumption | 10.1, 10.2, 14.1 |

### When You Find a Discrepancy

1. **Immediately note it** in the discussion comment
2. **Check if an issue already exists** — `gh issue list -l unverified --search "keyword"`
3. **If fixable now** — Edit the manual file, commit, and push
4. **If needs investigation** — File a GitHub issue with:
   - What the manual says vs. what the game shows
   - File path and line number
   - Screenshot if applicable
   - Suggested verification method

## Discussion Thread Format

### Posting Actions

```
**Please [specific action in bold].** Context about why we are doing this.
Screenshot after completing the action.
```

### Posting Observations

```
[Analysis of the screenshot — what we see, what it means]

**Manual note:** [Any discrepancy or confirmation found]

**Next:** [Brief preview of what comes next]
```

### Posting Milestones

Use H2 headers to mark major milestones:
```
## Turn N — [Date], [Brief Description]
```

## Known Issues from Previous Playthroughs

### Game 1 (20260221-00-Claude) — Lessons Applied

| Lesson | Status | How to Avoid |
|--------|--------|-------------|
| Survey ships need jump drives | Addressed in checklist above | Always include jump drive in survey ship designs |
| Sol grav surveyed = no survey work in Sol | Addressed in setup recommendations | Leave grav survey unchecked |
| Prototype pipeline has many undocumented steps | Documented in Phase 3 above | Follow the 6-step pipeline |
| "Create Project" button is not for component design | Documented | Use "Design Tech!" in Class Design window |
| Shipyards need retool before construction | Documented in Phase 3 | Always retool first; first retool is free |
| Refresh Tech needed after researching prototype | Documented | Click Refresh Tech before locking design |
| Scientist names must be read carefully | N/A | Always verify names from screenshots |

### Game 2 (20260222-Claude) — Lessons Applied

| Lesson | Status | How to Avoid |
|--------|--------|-------------|
| Deployment time default (3 months) far too short for survey ships | Addressed in checklist below | Set deployment time to 48+ months in Class Design |
| "LG: Overhaul at Colony" does NOT resupply MSP | New finding | Use "Refuel and Resupply from Colony" order for MSP loading |
| Squadron Transit requires ships in the SAME task group | New finding | Always merge task groups with "Join Fleet" before squadron transit |
| JP numbering can shift when new JPs are discovered | Addressed in Game 1 lessons | Always verify JP by destination label, not number |
| Leave Overhaul imposes 30-day performance penalty | Documented in manual | Avoid leaving overhaul unless emergency; Overhaul Factor 0.01→1.0 over 30 days |
| Ships can explode from cascading maintenance failures | New finding | Never let deployment exceed 500%; recall ships before maintenance death spiral |
| Life pods have ~15 day endurance | New finding | Rescue survivors immediately; lifepods expire quickly |
| Fleet speed limited by slowest ship (dead engine = 1 km/s) | New finding | Detach immobilized ships before moving task group |
| Overcrowding from destroyed crew quarters accelerates deployment 4-5x | New finding | Prioritize crew quarters repair; consider scuttling if quarters are destroyed |
| Standing Orders tab only at task group level, not individual ships | Addressed in Game 1 | Always detach ships to own TG before configuring standing orders |
| Overhaul at Colony (standing order) does not dock at shipyard | New finding | May need manual shipyard docking for full overhaul; investigate in Game 3 |
| Annual MSP consumption can exceed ship MSP capacity | Design flaw | Include Maintenance Storage Bays in ship design |

## Expanding This Guide

After each playthrough, update this guide AND commit the changes:
1. Add a row to the **Previous AAR Index** table with the discussion number, date, key lesson, and outcome
2. Add new lessons to the **Known Issues from Previous Playthroughs** section (create a new subsection for each game)
3. Update the **Critical Design Checklist** with new gotchas
4. Refine the phase descriptions based on what worked
5. Add new verification targets discovered during play
6. Update **Game Setup Recommendations** if new settings were tested
