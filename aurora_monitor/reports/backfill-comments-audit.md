# Reddit Monitor Backfill Comments Audit

**Date:** 2026-02-17
**Context:** Bug #1294 (short/empty Reddit posts scoring artificially high) caused the backfill run (Discussion #1296) to post false positive comments on unverified issues. All 85 comments were posted on 2026-02-17 between 08:13:48Z and 08:17:09Z by the aurora-monitor bot.

## Summary

| Metric | Value |
|--------|-------|
| Total backfill comments found | 85 |
| Issues affected | 44 (all issues in match table) |
| Comments with empty quotes | 37 (44%) |
| Issues with at least one empty-quote comment | 32 (73%) |
| All-medium confidence comments (no High matches) | 29 (34%) |
| **Recommendation: delete ALL** | **85 comments** |

## Classification

**ALL 85 comments are false positives and should be deleted.** The reasoning:

1. **Bug #1294 corrupted scoring across the board.** Short/empty Reddit posts scoring artificially high means every match above the 60-point threshold is suspect. Even comments that happen to contain some relevant-looking content were routed through a broken scoring pipeline.

2. **Content is overwhelmingly noise.** Reviewing the actual quotes reveals:
   - 93 empty quotes (`""`) across all comments -- posts/comments with no body text
   - One-word/trivial quotes: "Diplomacy", "Screenshot?", "Hello", "Hi people", "Hey", "Good tip", "Looking good", "Useful stuff!", "Very cool", "no"
   - Meme posts: "You walked into the wrong solar system, fool", "They died for the empire."
   - AAR/story posts with no mechanic verification value
   - General discussion threads ("What was your longest game", "What other games do Aurora players recommend?")

3. **Issue #707 alone has 18 comments (543 items) -- 13 with empty quotes.** This single issue demonstrates the scale of the false positive problem. Section 6.5 has 32 unverified claims; 543 Reddit items will not help verify any of them.

4. **No comment survived manual review as genuinely useful.** Even the highest-scoring matches (100/100) turned out to be trivially short comments that matched due to the bug (e.g., "Screenshot?", "no", "In short - no").

## Recommendation

Delete all 85 comments. After the matcher fix from #1294 is deployed, the backfill can be re-run with correct scoring to generate genuine matches.

## Full Catalog

### Issues with 5+ backfill comments (heavy spam)

| Issue | Title | Comments | Total Items | Empty Quotes | Comment IDs |
|-------|-------|----------|-------------|--------------|-------------|
| #707 | Verify: Section 6.5 unverified claims (32 items) | 18 | 543 | 13 | 3912991046, 3912991229, 3912991406, 3912991571, 3912991722, 3912991893, 3912992068, 3912992255, 3912992397, 3912992564, 3912992739, 3912992913, 3912993085, 3912993254, 3912993421, 3912993594, 3912993761, 3912993893 |
| #722 | Verify: Section 17.1 unverified claims (22 items) | 10 | 310 | 14 | 3912997074, 3912997250, 3912997436, 3912997621, 3912997809, 3912997969, 3912998133, 3912998318, 3912998528, 3912998744 |
| #1214 | Verify: Section 14.1.2 fuel consumption scaling | 5 | 147 | 8 | 3913002377, 3913002542, 3913002702, 3913002865, 3913003070 |
| #1283 | Verify: Chapter 11 sensor mechanics (8 claims) | 3 | 72 | 3 | 3913003888, 3913004079, 3913004260 |
| #713 | Verify: Section 16.2 unverified claims (19 items) | 3 | 87 | 4 | 3912995128, 3912995295, 3912995474 |

### Issues with 2-4 backfill comments

| Issue | Title | Comments | Total Items | Empty Quotes | Comment IDs |
|-------|-------|----------|-------------|--------------|-------------|
| #703 | Verify: Section 6.4 unverified claims (15 items) | 2 | 51 | 2 | 3912990355, 3912990540 |
| #709 | Verify: Section 16.1 unverified claims (7 items) | 2 | 47 | 6 | 3912994248, 3912994463 |
| #718 | Verify: Section 16.3 unverified claims (7 items) | 2 | 38 | 4 | 3912996191, 3912996355 |
| #874 | Verify: 10 million pop threshold for PPV | 2 | 43 | 5 | 3913001825, 3913002010 |
| #851 | Verify: Terminal guidance for laser warheads | 2 | 31 | 2 | 3912999953, 3913000177 |
| #1285 | Verify: Chapter 2 community timeline estimates | 2 | 41 | 9 | 3913004539, 3913004693 |
| #1287 | Verify: HQ unit requirement for commander bonus | 2 | 43 | 9 | 3913004850, 3913004970 |

### Issues with 1 backfill comment

| Issue | Title | Items | Empty Quotes | Comment ID |
|-------|-------|-------|--------------|------------|
| #700 | Verify: Section 1.1 unverified claims (4 items) | 8 | 1 | 3912989987 |
| #701 | Verify: Section 15.1 unverified claims (5 items) | 1 | 0 | 3912990189 |
| #704 | Verify: Section 1.2 unverified claims (4 items) | 10 | 1 | 3912990701 |
| #706 | Verify: Section 3.1 unverified claims (3 items) | 3 | 0 | 3912990889 |
| #708 | Verify: Section 10.2 unverified claims (4 items) | 5 | 1 | 3912994065 |
| #710 | Verify: Section 3.2 unverified claims (3 items) | 1 | 1 | 3912994624 |
| #711 | Verify: Section 7.2 unverified claims (5 items) | 4 | 2 | 3912994791 |
| #712 | Verify: Section 10.3 unverified claims (1 items) | 2 | 0 | 3912994976 |
| #714 | Verify: Section 3.3 unverified claims (8 items) | 3 | 0 | 3912995663 |
| #716 | Verify: Section 11.1 unverified claims (4 items) | 9 | 1 | 3912995829 |
| #717 | Verify: Section 3.4 unverified claims (1 items) | 1 | 0 | 3912996013 |
| #719 | Verify: Section 7.4 unverified claims (1 items) | 1 | 0 | 3912996488 |
| #720 | Verify: Section 11.2 unverified claims (4 items) | 2 | 0 | 3912996707 |
| #721 | Verify: Section 3.5 unverified claims (7 items) | 3 | 1 | 3912996879 |
| #729 | Verify: Section 4.4 unverified claims (6 items) | 13 | 4 | 3912998915 |
| #837 | Live Testing Required: 250 unverified claims | 6 | 1 | 3912999163 |
| #848 | Verify: Section 8.6 hangar maintenance (3 items) | 10 | 1 | 3912999387 |
| #849 | Verify: Section 14.2 deep space maintenance | 20 | 0 | 3912999575 |
| #850 | Verify: Section 5.3 ice sheet melt threshold | 3 | 1 | 3912999754 |
| #854 | Verify: Galactic map node colors (VB6-era ref) | 1 | 0 | 3913000498 |
| #855 | Verify: Real stars import process (VB6-era ref) | 6 | 0 | 3913000708 |
| #856 | Verify: Greenhouse factor formula (VB6-era ref) | 1 | 1 | 3913000894 |
| #857 | Verify: Trojan asteroid generation (VB6-era ref) | 2 | 1 | 3913001093 |
| #858 | Verify: NPR diplomatic teams behavior (VB6-era ref) | 5 | 0 | 3913001292 |
| #871 | Verify: Sub-pulse length button options | 2 | 0 | 3913001459 |
| #873 | Verify: Bombardment vs Anti-Vehicle tactical roles | 29 | 2 | 3913001655 |
| #1212 | Verify: 8.6.3 Hangar nesting restriction | 11 | 2 | 3913002199 |
| #1228 | Verify: Section 5.2.8 PPV and protection mechanics | 7 | 1 | 3913003231 |
| #1229 | Verify: Section 13.1 THM and fortification formula | 22 | 4 | 3913003388 |
| #1230 | Verify: Box launcher reload at OTPs vs hangars | 5 | 1 | 3913003559 |
| #1231 | Verify: Stationary facilities unlimited ships | 1 | 1 | 3913003735 |
| #1284 | Verify: Chapter 11 stealth/cloak mechanics | 8 | 2 | 3913004402 |

## Comment IDs for Deletion (all 85)

```
3912989987
3912990189
3912990355
3912990540
3912990701
3912990889
3912991046
3912991229
3912991406
3912991571
3912991722
3912991893
3912992068
3912992255
3912992397
3912992564
3912992739
3912992913
3912993085
3912993254
3912993421
3912993594
3912993761
3912993893
3912994065
3912994248
3912994463
3912994624
3912994791
3912994976
3912995128
3912995295
3912995474
3912995663
3912995829
3912996013
3912996191
3912996355
3912996488
3912996707
3912996879
3912997074
3912997250
3912997436
3912997621
3912997809
3912997969
3912998133
3912998318
3912998528
3912998744
3912998915
3912999163
3912999387
3912999575
3912999754
3912999953
3913000177
3913000498
3913000708
3913000894
3913001093
3913001292
3913001459
3913001655
3913001825
3913002010
3913002199
3913002377
3913002542
3913002702
3913002865
3913003070
3913003231
3913003388
3913003559
3913003735
3913003888
3913004079
3913004260
3913004402
3913004539
3913004693
3913004850
3913004970
```

## Deletion Script

```bash
#!/bin/bash
# Delete all 85 false positive backfill comments
# Run from repository root
# WARNING: This is destructive. Review the audit before running.

REPO="ErikEvenson/aurora-manual"
COMMENT_IDS=(
3912989987 3912990189 3912990355 3912990540 3912990701 3912990889
3912991046 3912991229 3912991406 3912991571 3912991722 3912991893
3912992068 3912992255 3912992397 3912992564 3912992739 3912992913
3912993085 3912993254 3912993421 3912993594 3912993761 3912993893
3912994065 3912994248 3912994463 3912994624 3912994791 3912994976
3912995128 3912995295 3912995474 3912995663 3912995829 3912996013
3912996191 3912996355 3912996488 3912996707 3912996879 3912997074
3912997250 3912997436 3912997621 3912997809 3912997969 3912998133
3912998318 3912998528 3912998744 3912998915 3912999163 3912999387
3912999575 3912999754 3912999953 3913000177 3913000498 3913000708
3913000894 3913001093 3913001292 3913001459 3913001655 3913001825
3913002010 3913002199 3913002377 3913002542 3913002702 3913002865
3913003070 3913003231 3913003388 3913003559 3913003735 3913003888
3913004079 3913004260 3913004402 3913004539 3913004693 3913004850
3913004970
)

deleted=0
failed=0

for id in "${COMMENT_IDS[@]}"; do
  if gh api -X DELETE "repos/$REPO/issues/comments/$id" 2>/dev/null; then
    echo "Deleted comment $id"
    ((deleted++))
  else
    echo "FAILED to delete comment $id"
    ((failed++))
  fi
  sleep 0.5  # Rate limiting
done

echo ""
echo "Done. Deleted: $deleted, Failed: $failed"
```
