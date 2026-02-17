# New Content Detector — Scoring Retune Report

**Date:** 2026-02-17
**Related:** Issue #1300, Discussion #1296

## Problem

Initial scoring weights made threshold 40 unreachable for genuine mechanics posts.
Best real content (Paul_Kauphart's fuel:engine math, SerBeardian's missile warhead testing)
scored only 26 — well below threshold.

### Root Causes

1. **Evidence keywords too low:** +8 each, max 24 — insufficient to reach 40 alone
2. **"database" false positive:** Triggered on patch notes and DB integration posts
3. **No chapter-mapping bonus:** Posts mapping to specific chapters (= more likely real content) got no credit
4. **Text length bonus too flat:** No reward for very long posts (>1000 chars)

## Changes Applied

### Scoring Weights (`new_content.py`)

| Signal | Before | After |
|--------|--------|-------|
| Evidence keyword per hit | +8 | +10 |
| Evidence keyword max | 24 | 30 |
| Text >1000 chars | (n/a) | +15 |
| Text >500 chars | +10 | +10 |
| Text >200 chars | +5 | +5 |
| Chapter mapping: 1 chapter | (n/a) | +10 |
| Chapter mapping: 2+ chapters | (n/a) | +15 |

### Config (`config.yaml`)

- Removed `database` from evidence_keywords (false positive on patch notes)
- Removed `checked the db` (related false positive)
- Kept `min_score: 40` (reachable with retuned weights)

## Validation Against Live Data

**Dataset:** 1,685 posts from r/aurora4x (685) + r/aurora (1,000)

### Target Posts (Before → After)

| Post | Author | Before | After | Status |
|------|--------|--------|-------|--------|
| Ship Design math 3: fuel:engine ratio | Paul_Kauphart | 26 | 50 | Captured |
| Additional missile info - Laser warheads | SerBeardian | 26 | 45 | Captured |

### Threshold Sensitivity

| Threshold | Count |
|-----------|-------|
| >= 15 | 628 |
| >= 20 | 457 |
| >= 25 | 247 |
| >= 30 | 138 |
| >= 35 | 28 |
| >= 40 | 14 |

### Score Distribution (non-zero, n=1,098)

- 1-9: 205
- 10-19: 436
- 20-29: 319
- 30-39: 124
- 40-59: 14
- 60+: 0

## Issues Created

| Issue | Score | Title |
|-------|-------|-------|
| #1302 | 50 | Ship Design math 3: fuel:engine ratio (Paul_Kauphart) |
| #1303 | 50 | Survey Results & Followup (SikeSky) |
| #1304 | 45 | Additional missile info - Laser warheads, ECM, armor (SerBeardian) |
| #1305 | 40 | The Miraculous Space-Time Bubble (DaveNewtonKentucky) |
| #1306 | 40 | Transnewtonian materials (hypervelocityvomit) |

## Test Suite

107 tests pass (unchanged count, updated assertions for new weights).
