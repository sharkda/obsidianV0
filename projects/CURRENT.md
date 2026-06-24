# Current Project Context

Active focus across projects. Update at session END.

---

## Active project
**HootOwl** — SwiftUI iOS/macOS app for Taiwan urban mobility (real-time bus + parking).

## State (2026-06-24, session END before Jim upgrades Claude Code)

All battery work to date is committed. Working tree is clean.

**Last commit on this thread:** `61eec92 June24` — Phase 2 (Layer B1) disk cache.

Recent commit chain (battery + cleanup work):
- `61eec92 June24` — Phase 2: `Municipal+Cache.swift` + Codable on `MncplParkAvPack` / `MncplParkItemAvail` in `ParkAvailv02.swift`.
- `2d5eb13 June23` — sync (post Phase 1b).
- `392fa82 June18` — sync (post Phase 1b initial work).
- `04e2165 June16th` — #9 / macOS auth split / dead-code cleanup.
- `837cbef June15th` — #1 + #6 + cleanup waves.
- `08c5816 Jun13` — first cleanup wave (Obs-framework dedup).

## Where we are in the battery partition plan

Full plan + status lives in [[battery]]. Quick map:

| Phase | What | Status |
|---|---|---|
| #1 — GPS Best → HundredMeters | mechanical at 5 sites (reduced to 1 by cleanup) | ✓ committed `837cbef` |
| #6 — Timer.publish tolerance | 5 active sites + cleanup waves | ✓ committed `837cbef` |
| #9 — Drop Always-auth + Info.plist cleanup | iOS escalation removed, macOS preserved, dead code dropped | ✓ committed `04e2165` |
| 1 (Layer A) — Cyclops state → Municipal singleton | `Municipal+Cyclops.swift`, lifted `cyclopsMod`/`availableTime`/`watchList`; thin view | ✓ committed |
| 2 (Layer B1) — Disk cache for cold-launch / jettison | `Municipal+Cache.swift`, `Library/Caches/hootowl-snapshot.json`, 24h stale threshold | ✓ committed `61eec92` |
| **3 (#2 + #3) — scenePhase handler** | Pause GPS + cancel timers on `.background`; restart + immediate refresh on `.active` | **next — plan drafted, 4 open decisions for Jim** |
| 4 (Layer B2) — Cyclops trail history persistence | Optional / deferrable | not started |
| 5 — Consolidate redundant `CLLocationManager` re-init in `Municipal.swift:122` + `:160` | trivial code-health cleanup | not started |

## Phase 3 — pick up here when resuming

Plan + the 4 open decisions live in [[battery#2026-06-24--phase-3-pre-implementation-brief-asked-jim-awaiting-answers]]. **Before writing any Phase 3 code, ask Jim for answers to those 4 decisions.** Recommendations summarized:

1. `ReceiptObs.timer` — keep running (recommended).
2. Immediate refresh on `.active` — yes (recommended).
3. Wiring style — direct calls from App root (recommended).
4. Partition — ship #2 + #3 together (recommended).

Phase 3 scope sketch: new `Municipal+Lifecycle.swift` + pause/resume on `CyclopsObs` and `SourceBase` + App-root `@Environment(\.scenePhase)` handler. ~50 lines.

## Open bugs (not blocking battery work)

- `bugs.md` 2026-06-15 — IME blocks UI on All-screen search. Open, deferred until after battery pre-release picks land.

## Next steps (when Jim resumes)

- [ ] Read CLAUDE.md session START protocol; everything is up to date in the vault, so the summary should reflect "Phase 2 done, Phase 3 plan drafted, waiting on 4 answers from Jim."
- [ ] Ask Jim for the 4 Phase 3 decisions.
- [ ] Implement Phase 3 per his answers.
- [ ] Re-test cold launch + background/foreground after Phase 3 lands.
- [ ] Decide on Phase 4 (Layer B2) + #5 (Municipal CLLocationManager dedupe) — both deferrable until after release.

## Open questions / blockers
- None blocking. The 4 Phase 3 decisions are the only outstanding asks.
