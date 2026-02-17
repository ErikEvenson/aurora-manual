# Discussion #1296 — Reddit Backfill Triage Summary

**Date:** 2026-02-17
**Source:** [Discussion #1296](https://github.com/ErikEvenson/aurora-manual/discussions/1296)

---

## High-Count Issues (from request)

### #707 — Verify: Section 6.5 unverified claims (32 items) — Civilian Economy

| Field | Value |
|-------|-------|
| Posts | 543 |
| High-Confidence | 59 |
| Top Quote | "[removed]" |
| **Assessment** | **Likely False Positive** |

**Reasoning:** 543 posts with 59 high-confidence matches for a single verification issue about civilian shipping lines is implausibly high. The top quote is literally "[removed]" — a deleted Reddit comment. Section 6.5 covers civilian economy mechanics (shipping lines, subsidies, fuel harvesters, mining colonies). While civilian economy is discussed on r/aurora4x, the sheer volume and the "[removed]" top quote strongly suggest the matcher is picking up generic economic/game discussion keywords that happen to overlap with the 32 unverified claims in this issue. The issue contains common terms like "population," "economy," "ships," "fuel," "colony" — all extremely frequent in Aurora Reddit posts regardless of topic.

**Recommended Action:** No manual review of these 543 posts. The keyword overlap is too broad to yield useful verification evidence. If civilian economy verification is desired, targeted forum searches would be far more efficient.

---

### #722 — Verify: Section 17.1 unverified claims (22 items) — Geological Survey

| Field | Value |
|-------|-------|
| Posts | 310 |
| High-Confidence | 15 |
| Top Quote | "Are the ships in a fleet with other orders?" |

| **Assessment** | **Needs Review (partial genuine, mostly noise)** |

**Reasoning:** 310 posts is very high but more plausible than #707 — geological surveying is a frequent topic among new players ("what do I do first?" posts). The top quote "Are the ships in a fleet with other orders?" is tangentially related — it sounds like someone troubleshooting fleet orders, which could relate to survey ship behavior. However, the 22 unverified claims include specific numbers (survey point ranges for body types, ship tonnage estimates) that Reddit comments are unlikely to authoritatively verify. The 15 high-confidence matches may include some genuinely relevant discussions about survey mechanics.

**Recommended Action:** Spot-check a sample of the 15 high-confidence matches for any Steve Walmsley quotes or experienced player confirmations about survey point requirements. Do not attempt to review all 310 posts.

---

### #1214 — Verify: Section 14.1.2 — Fuel consumption vs speed scaling

| Field | Value |
|-------|-------|
| Posts | 147 |
| High-Confidence | 11 |
| Top Quote | "" (empty) |
| **Assessment** | **Needs Review (potentially genuine)** |

**Reasoning:** This is one of the most substantive verification issues in the table — it concerns whether fuel consumption scales with actual travel speed at runtime or is a flat rate. This is a question players actively debate and test. 147 posts with 11 high-confidence matches is plausible for fuel/engine mechanics, a common discussion topic. The empty top quote is a yellow flag but not damning — it may indicate the comment body was extracted improperly. The issue itself documents a potential contradiction between Section 14.1.2 and Appendix A.1.4, which is exactly the kind of thing experienced players would weigh in on.

**Recommended Action:** Review the 11 high-confidence matches. This issue has high verification value — a single authoritative Reddit comment citing in-game testing or a Steve Walmsley post could resolve the flat-rate vs speed-dependent fuel consumption question definitively.

---

### #1283 — Verify: Chapter 11 sensor mechanics (8 claims) — community-documented

| Field | Value |
|-------|-------|
| Posts | 72 |
| High-Confidence | 9 |
| Top Quote | "<3" (per request) / "No, not automatically." (per discussion body) |
| **Assessment** | **Likely Genuine** |

**Reasoning:** The discussion body actually shows the top quote as "No, not automatically." which is much more relevant — it could directly relate to claims like "Sensors take no time to activate" or "thermal sensors on different ships share detections." 72 posts with 9 high-confidence matches for sensor/detection mechanics is a very plausible count. Sensor mechanics (EMCON, passive vs active, detection stacking) are frequently discussed. The 8 claims are concrete, testable mechanics that experienced players would have opinions on.

**Recommended Action:** Review all 9 high-confidence matches. Sensor EMCON behavior and detection stacking are topics where player experience reports could provide useful corroboration or contradiction. Particularly look for posts about EMCON missile guidance loss (claim #8) and sensor stacking (claims #1-2).

---

### #713 — Verify: Section 16.2 unverified claims (19 items) — Commander Skills

| Field | Value |
|-------|-------|
| Posts | 87 |
| High-Confidence | 2 |
| Top Quote | "In Aurora C#, is it possible to remove a gas with a terra..." |
| **Assessment** | **Likely False Positive** |

**Reasoning:** The top quote is about terraforming gas removal — completely unrelated to commander skills and bonuses. The issue covers crew training formulas, morale mechanics, deployment timers, and rank progression. The quote suggests the matcher flagged posts containing "Aurora C#" combined with generic gameplay terms. Only 2 high-confidence matches out of 87 posts further supports low signal quality.

**Recommended Action:** Skip. The 2 high-confidence matches could be briefly checked, but the terraforming top quote strongly signals topic mismatch.

---

### #1287 — Verify: HQ unit requirement for commander bonus application

| Field | Value |
|-------|-------|
| Posts | 43 |
| High-Confidence | 6 |
| Top Quote | "<3" |
| **Assessment** | **Needs Review (uncertain)** |

**Reasoning:** The "<3" top quote is a heart emoji — zero information value. However, the issue itself is a focused, specific question (does HQ capacity act as a binary gate or proportional scaling for ground force commander bonuses?) that is exactly the kind of mechanic players discuss and test. 43 posts with 6 high-confidence matches is a reasonable count for ground combat discussions. The "<3" top quote may simply be the highest-scored comment in a thread where other comments discuss the actual mechanic.

**Recommended Action:** Review the 6 high-confidence matches. This is a narrow, well-defined verification question where even one authoritative player report would be valuable.

---

## Moderate-Count Issues (from request)

### #718 — Verify: Section 16.3 unverified claims (7 items) — Commander Assignments

| Field | Value |
|-------|-------|
| Posts | 38 |
| High-Confidence | 2 |
| Top Quote | "other than that, add more MSP." |
| **Assessment** | **Likely Genuine** |

**Reasoning:** The top quote "other than that, add more MSP" is practical gameplay advice that could appear in a thread discussing ship maintenance, which connects to the claim about "Ships consume fuel as if running engines at 10% power during training exercises" and "maintenance clock increases at 2x the normal rate during training." MSP (Maintenance Supply Points) is directly relevant to the maintenance-during-training claims in this issue. 38 posts with 2 high-confidence is a modest, believable count.

**Recommended Action:** Review the 2 high-confidence matches. The MSP connection suggests at least some posts discuss ship upkeep mechanics that overlap with the training fuel/maintenance claims.

---

### #729 — Verify: Section 4.4 unverified claims (6 items) — Jump Points

| Field | Value |
|-------|-------|
| Posts | 13 |
| High-Confidence | 2 |
| Top Quote | "Will there be a spacemaster for C# Aurora?" |
| **Assessment** | **Likely Genuine** |

**Reasoning:** The top quote directly relates to SpaceMaster mode, and 3 of the 6 unverified claims in this issue are about SpaceMaster features (Regen JP button, configuration dialog, No Geo Survey / No Grav Survey buttons). 13 posts with 2 high-confidence matches is a very reasonable count for a niche topic like SpaceMaster jump point regeneration.

**Recommended Action:** Review both high-confidence matches. These could confirm or deny the existence of SpaceMaster JP regeneration UI features described in the manual.

---

### #849 — Verify: Section 14.2 deep space maintenance capacity

| Field | Value |
|-------|-------|
| Posts | 20 |
| High-Confidence | 2 |
| Top Quote | "This is the original of this." |
| **Assessment** | **Needs Review (unclear signal)** |

**Reasoning:** The top quote "This is the original of this" is ambiguous — it could be a meta-comment linking to a source post, which would actually be valuable for verification. The issue asks a specific question: do maintenance modules work in deep space without planetary infrastructure? 20 posts with 2 high-confidence matches is plausible for deep space logistics discussions. Players often discuss deep space station designs and their maintenance challenges.

**Recommended Action:** Review the 2 high-confidence matches. If the "original" comment links to a Steve Walmsley post or authoritative source about maintenance mechanics, it could directly verify or refute the claim.

---

### #874 — Verify: 10 million population threshold for PPV requirements

| Field | Value |
|-------|-------|
| Posts | 43 |
| High-Confidence | 4 |
| Top Quote | "There are also the main Aurora forums..." |
| **Assessment** | **Likely Genuine** |

**Reasoning:** The top quote references the Aurora forums, suggesting the post is directing someone to authoritative sources — consistent with discussions about game mechanics thresholds. PPV (Planetary Protection Value) and population thresholds are discussed when players encounter unexpected unrest. 43 posts with 4 high-confidence matches is plausible. The issue already cites forum and wiki sources for the 10M threshold but needs in-game confirmation.

**Recommended Action:** Review the 4 high-confidence matches. Look for player reports of unrest behavior at specific population levels. Even anecdotal "I had 8M population and no unrest" reports would help bracket the threshold.

---

## Summary Table

| Issue | Topic | Posts | High | Assessment | Review Priority |
|-------|-------|-------|------|------------|----------------|
| #707 | Civilian Economy (32 claims) | 543 | 59 | **Likely False Positive** | Skip |
| #713 | Commander Skills (19 claims) | 87 | 2 | **Likely False Positive** | Skip |
| #1214 | Fuel consumption vs speed | 147 | 11 | **Needs Review** | **High** |
| #1283 | Sensor mechanics (8 claims) | 72 | 9 | **Likely Genuine** | **High** |
| #874 | PPV 10M threshold | 43 | 4 | **Likely Genuine** | **Medium** |
| #1287 | HQ commander bonus gating | 43 | 6 | **Needs Review** | **Medium** |
| #729 | Jump Points / SpaceMaster | 13 | 2 | **Likely Genuine** | **Medium** |
| #718 | Commander Assignments / MSP | 38 | 2 | **Likely Genuine** | **Low** |
| #849 | Deep space maintenance | 20 | 2 | **Needs Review** | **Low** |
| #722 | Geological Survey (22 claims) | 310 | 15 | **Needs Review** | **Low** |

## Recommended Next Actions

1. **Priority review:** #1214 (fuel consumption) and #1283 (sensor mechanics) — these have the best signal-to-noise ratio and address substantive mechanical questions where community evidence could resolve open contradictions.

2. **Secondary review:** #874 (PPV threshold), #1287 (HQ bonuses), and #729 (SpaceMaster features) — focused questions where even 1-2 relevant posts could provide verification evidence.

3. **Skip:** #707 and #713 — too much keyword noise, too many broad claims, top quotes unrelated to issue topics.

4. **Monitor tuning consideration:** The #707 result (543 posts, 59 high-confidence for a single issue) suggests the matcher may be over-weighting common game terms. Issues with many unverified claims containing generic keywords (population, ships, fuel, economy) will attract false positives. Consider whether the confidence scoring accounts for term specificity / inverse document frequency.
