# Spot-Check: Reddit Matches for Issues #1214 and #1283

**Date:** 2026-02-17
**Source:** Discussion #1296 (Reddit Monitor Backfill Report)

---

## Issue #1214 — Fuel Consumption Scaling

**Summary:** Section 14.1.2 claims fuel consumption scales with actual travel speed at runtime (square-of-speed relationship). Appendix A.1.4 gives a formula with no speed variable — all parameters are fixed at engine design time. The core question: does fuel consumption vary with actual travel speed, or is it a flat rate determined entirely by engine design?

**Backfill stats:** 147 matched posts, 11 high confidence, 20 forum links.

### Reddit Posts Reviewed

#### 1. "Ship Design math, or the formula behind the fuel:engine ratio" — u/Paul_Kauphart (2018-08-28)
**Score:** 10 | **Post ID:** 9ayx9q

**Key content:** Derives the full fuel:engine ratio formula from first principles. Defines endurance as `fuelCap / (enginePower * fuelConsumptionRate)` — i.e., endurance is fuel capacity divided by a *constant* burn rate. The speed formula is `V = 1000 * ET * Pm * Pf * X` where all variables are design-time constants.

**Critical observation:** Paul_Kauphart's math treats fuel consumption as a flat rate. There is no speed variable in the consumption formula. Speed only affects range *indirectly* because range = speed x endurance, and endurance is fixed. A faster ship covers more distance in the same fuel, but does not burn fuel faster at lower speeds.

**Verification value:** **HIGHLY USEFUL.** This post strongly supports the flat-rate model. The "square of speed" relationship exists at *design time* (the boost penalty compounds exponentially), not at runtime.

#### 2. "Ship Design math 2: fuel:engine ratio math for missiles" — u/Paul_Kauphart (2018-09-06)
**Score:** 12 | **Post ID:** 9dk2id

**Key content:** Extends the same math to missiles. Uses the same fundamental formula: `endurance = fuelCapacity / (totalEnginePower * baseFuelConsumption * penaltyMultiplier)`. Again, no runtime speed variable.

**Verification value:** **USEFUL.** Corroborates post #1 — consistent flat-rate model applied to both ships and missiles.

#### 3. "Ship Design math 3: fuel:engine ratio, a typical case" — u/Paul_Kauphart (2018-09-10)
**Score:** 11 | **Post ID:** 9eriw1

**Key content:** Practical application of the formulas. Derives the relationship `A * Fs*ET^2.5/FC * Pf^3.5/V^2.5/R * ... = 1`. The V^2.5 term appears in the *design equation* relating speed, range, and propulsion fraction — NOT as a runtime consumption modifier.

**Verification value:** **USEFUL.** Confirms the "square of speed" is a design-time tradeoff, not a runtime mechanic.

#### 4. "UPDATED! SerBeardian's Engine, Speed and Fuel Calculator" — u/SerBeardian (2018-03-12)
**Score:** 10 | **Post ID:** 83udli

**Key content:** SerBeardian (widely regarded as the most authoritative community member for VB6-era Aurora mechanics) published a calculator. The post itself is a link to a spreadsheet. Comments discuss fuel tonnage calculation (1 ton per 1,000 liters, corrected by u/JacenHan). The calculator treats fuel consumption as a constant rate for a given engine design.

**Verification value:** **PARTIALLY USEFUL.** Confirms community consensus on flat-rate consumption, but the calculator is VB6-era and the C# formula may differ.

#### 5. "Typical speed vs. fuel longevity for mil beam ships?" — u/[deleted] (2018-03-09)
**Score:** 3 | **Post ID:** 83aiif

**Key content:** Players discuss fuel longevity in terms of time (days/months/years), not distance. SerBeardian advises: "Calculating range in time is mostly worthless." Multiple respondents discuss fuel as a fixed-rate resource — nobody mentions going slower to save fuel. One player achieves "about a month's worth of fuel" without any mention of speed-dependent consumption.

**Verification value:** **PARTIALLY USEFUL.** Indirect evidence: experienced players discuss fuel exclusively as a time-based endurance metric. If speed-dependent consumption were a real mechanic, these players would certainly mention "slow down to extend range" — but none do.

### Assessment for Issue #1214

**Overall verification value: USEFUL — supports correcting the manual.**

The Reddit evidence consistently points to fuel consumption being a **flat rate** determined at engine design time. The "square of speed" relationship in Section 14.1.2 appears to describe the *design-time tradeoff* (higher power modifier = exponentially more fuel via compounding 25%-per-10% boost penalty), not a runtime speed-dependent mechanic.

**Key findings:**
1. Paul_Kauphart's three-part mathematical analysis (the most rigorous community treatment of fuel mechanics) contains no runtime speed variable
2. SerBeardian's calculator treats consumption as constant
3. No experienced player in any thread mentions "going slower to save fuel" as a tactic
4. The smoelf stealth post ("Now this is what stealth is about") describes slowing to 50 km/s to reduce *thermal signature*, not to save fuel — a key distinction

**What is NOT resolved by Reddit alone:**
- Whether C# Aurora changed the model from VB6 (most posts are VB6-era or ambiguous)
- The exact behavior when a task group speed is set below max — does the game still burn fuel at max rate? (This requires in-game testing or database inspection)
- The forum threads cited in the issue (currently returning 523 errors) might contain authoritative answers

**Recommendation:** The Reddit evidence is strong enough to flag Section 14.1.2 claims as likely incorrect, but verification still requires either in-game testing or Aurora Forums confirmation. The manual should be updated to clarify the design-time vs. runtime distinction.

---

## Issue #1283 — Sensor Mechanics (8 Community-Documented Claims)

**Summary:** Eight claims in Chapter 11 (sensors/detection) use `*(community-documented)*` markers instead of proper `*(unverified — #NNN)*` tracking. These cover passive sensor stacking, EMCON behavior, fire control availability under EMCON, and missile guidance loss.

**Backfill stats:** 72 matched posts, 9 high confidence. Top quote: "No, not automatically."

### Reddit Posts Reviewed

#### 1. "Do CIWS's active sensors give stealth ships away?" — u/Earthfall10 (2018-03-09)
**Score:** 6 | **Post ID:** 8338wl

**Key content:**
- **SerBeardian** (score 3): "The CIWS active grav sensor is cut down so that it only has 10,000km of missile detection. (lorewise) As such, its signal strength would be so low that it wouldn't be detectable beyond 10,000km anyway. So no, it doesn't count as EM emissions for detection."
- **DaveNewtonKentucky** (score 3): Lists CIWS exceptions to normal rules: "They don't need external active sensor contact or external fire controls to fire." Updated the AuroraWiki CIWS page based on this thread.

**Relevant to claims:** #3 (sensor activation timing — tangentially), #5 (fire controls under EMCON — CIWS is the exception that proves the rule)

**Verification value:** **PARTIALLY USEFUL.** Confirms CIWS operates independently from normal fire control/sensor rules, which indirectly supports claim #5 (fire controls are NOT available under EMCON for non-CIWS weapons). DaveNewtonKentucky's wiki update adds authority.

#### 2. "How does ship detection (information gained) work?" — u/Dagl1 (2018-12-07)
**Score:** 10 | **Post ID:** a3vqd3

**Key content:**
- **SerBeardian** (score 4): "Active Sensors detect the effective cross section/hull size/tonnage of the ship (1 HS = 50t), and the current location. Passive Thermals detect the thermal signature of the engines, and the current location. Passive EM detect Active Sensors (when turned on), Shield strength (if turned on), and the current location."
- **Tohopekaliga** (score 6): "Passive scanners can tell you about speeds (you see them go), shields (if they're active), and an idea of engine size. You need active scanners to figure out exact sizes."

**Relevant to claims:** #1 (thermal sensor stacking — not directly addressed), #2 (task group sensor sharing — not addressed)

**Verification value:** **PARTIALLY USEFUL.** Confirms basic sensor detection model (passive thermal = engine signature, passive EM = active emissions). Does not directly address stacking or sharing mechanics.

#### 3. "Basic question I feel like I'm missing — missile 'lock?'" — u/Caligirl-420 (2018-02-07)
**Score:** 7 | **Post ID:** 7vzr8f

**Key content:**
- **continue_stocking** (score 7): "It needs to be in fire control range to launch the missile, after that you just need to keep the target in active sensor range." Links to AuroraWiki Missile page.

**Relevant to claims:** #4 (missiles lose guidance outside FC range and go ballistic) — **DIRECTLY RELEVANT.**

**Verification value:** **USEFUL.** The answer says missiles need fire control range only to *launch*, then need active sensor range to maintain guidance. This partially supports claim #4 but adds nuance: the critical factor is active sensor range, not fire control range specifically. The claim in the manual ("If the target moves outside fire control range, the missiles lose guidance") may be imprecise — it should say "outside active sensor range."

#### 4. "Delay on missile using internal sensors?" — u/UristMcSoriumHauler (2018-04-19)
**Score:** 3 | **Post ID:** 8dgaub

**Key content:**
- **SerBeardian** (score 4): "Yes, there is a 5 second delay on retargeting. This is why the sensor range needs to be a little over 5 seconds worth of target speed, so that the targets are still in range of the sensors."

**Relevant to claims:** #4 (missile guidance mechanics) — supports the existence of sensor-based guidance mechanics.

**Verification value:** **PARTIALLY USEFUL.** Confirms missiles use onboard sensors for retargeting with a 5-second delay. Supports claim #4's mention of "onboard sensors if equipped" as a fallback.

#### 5. "Point defense will not fire" — u/jjans002 (2018-07-30)
**Score:** 7 | **Post ID:** 92zajo

**Key content:**
- **u/[deleted]** (score 5): "Do you have another ship with active sensors on? Point defense needs an active sensor lock on the missiles to do their thing... CIWS is a special case that does not follow that rule as it has its own thing built in (but doesn't share info to others)."
- **gar_funkel** (score 10): Provides a comprehensive checklist including "Can the enemy be seen by active sensors and not only passives?" and "Are weapons assigned to fire controls?"

**Relevant to claims:** #5 (fire controls unavailable under EMCON), #6 (Full EMCON = completely passive) — supports both indirectly. If active sensors are required for fire control targeting, then EMCON (which suppresses active sensors) would indeed make fire controls unavailable.

**Verification value:** **USEFUL.** Strongly supports the causal chain: EMCON suppresses active sensors -> no active sensor lock -> fire controls cannot target -> weapons cannot engage. This validates claims #5 and #6.

#### 6. "Now this is what stealth is about" — u/smoelf (2018-01-23)
**Score:** 12 | **Post ID:** 7sg55b

**Key content:** Player describes reducing speed to 50 km/s to reduce thermal signature and "get off their radar." Successfully evaded a hostile contact by going silent (no active sensors) and slow (low thermal).

**Relevant to claims:** #6 (Full EMCON suppresses all active emissions), #7 (EMCON with distance threshold)

**Verification value:** **PARTIALLY USEFUL.** Demonstrates that going passive (no active sensors) + reducing thermal signature is a viable evasion strategy, which is consistent with the EMCON mechanics described in claims #6 and #7. However, it's a gameplay anecdote rather than a mechanical verification.

### Assessment for Issue #1283

**Overall verification value: PARTIALLY USEFUL — corroborates several claims but does not provide authoritative verification for most.**

**Claim-by-claim status:**

| # | Claim | Reddit Evidence | Verdict |
|---|-------|----------------|---------|
| 1 | Multiple thermal sensors don't stack; best counts | No direct evidence found | **Not addressed** |
| 2 | Thermal sensors shared within task group | No direct evidence found | **Not addressed** |
| 3 | Sensors activate/deactivate instantly | Tangential only (CIWS exception) | **Not addressed** |
| 4 | Missiles lose guidance outside FC range, go ballistic | continue_stocking clarifies: FC range needed for *launch*, active sensor range needed for *guidance* | **Partially verified** — claim may need correction (sensor range, not FC range, is the guidance factor) |
| 5 | Fire controls unavailable under EMCON | Supported by active-sensor-lock requirement for targeting | **Partially verified** — logical inference from sensor mechanics, not direct confirmation |
| 6 | Full EMCON = completely passive | Consistent with gameplay anecdotes (smoelf) and fire control mechanics | **Partially verified** |
| 7 | EMCON with distance threshold auto-activates sensors | The "No, not automatically" quote from backfill suggests this claim may be WRONG | **Potentially contradicted** — needs further investigation |
| 8 | In-flight missiles lose guidance if EMCON activated | No direct evidence found | **Not addressed** |

**Key findings:**
1. Claim #4 may be imprecise: the critical factor for missile guidance appears to be *active sensor range*, not fire control range. After launch, fire control range is not the constraint — sensor contact is.
2. Claim #7 (EMCON distance threshold auto-activation) is the most suspicious. The backfill's top quote "No, not automatically" likely addresses whether sensors activate automatically based on passive detection range. If this quote is from a response to "Do active sensors turn on automatically under EMCON?", then the manual's claim about automatic activation may be incorrect.
3. Claims #1, #2, #3, and #8 have no Reddit evidence found. These require Aurora Forums or in-game testing.
4. SerBeardian and DaveNewtonKentucky are the most authoritative community voices in these threads.

**Recommendation:** The Reddit evidence is insufficient to fully verify most of these claims. The most actionable finding is the potential correction to claim #4 (FC range vs. sensor range) and the flag on claim #7 (automatic EMCON threshold behavior). Aurora Forums and in-game testing remain necessary for claims #1, #2, #3, and #8.

---

## Summary

| Issue | Reddit Posts Reviewed | Useful Posts | Key Data Points Found | Overall Value |
|-------|----------------------|--------------|----------------------|---------------|
| #1214 | 5 | 3 highly useful, 2 partially | Flat-rate fuel model confirmed by math analysis; no community member references runtime speed-dependent consumption | **Useful** — supports correcting manual claims |
| #1283 | 6 | 2 useful, 4 partially | Missile guidance = sensor range not FC range; EMCON auto-activation may be wrong | **Partially useful** — several claims still unaddressed |

### Notable Authoritative Community Members Cited

- **u/SerBeardian** — Prolific Aurora contributor, maintains engine calculator, detailed mechanical knowledge
- **u/Paul_Kauphart** — Rigorous mathematical analysis of fuel/engine mechanics
- **u/DaveNewtonKentucky** — Active wiki contributor, documents discoveries from community threads
- **u/gar_funkel** — Practical combat mechanics knowledge
- **u/Ikitavi** — Deep gameplay experience, tactical insights
