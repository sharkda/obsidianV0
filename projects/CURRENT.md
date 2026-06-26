# Current Project Context

Active focus across projects. Update at session END.

---

## Active project
**HootOwl** — SwiftUI iOS/macOS app for Taiwan urban mobility (real-time bus + parking).

## State (2026-06-25, after upgrading Claude Code — Phase 3 implemented, uncommitted)

**Phase 3 (#2 + #3 — scenePhase pause/resume) is implemented in the working tree, NOT yet committed.** Jim greenlit all four recommended decisions from the 2026-06-24 brief. Awaiting his day-of device test before commit.

Working-tree changes this session:
- **New (untracked):** `hootowl/Municipalities/framework/Municipal+Lifecycle.swift` — `pauseForBackground()` / `resumeForForeground()`.
- **Modified:** `hootowl/App/hootowlApp.swift` (`@Environment(\.scenePhase)` + `.onChange`), `Mu1Base+Ext.swift` (`pausePolling()` / `resumePolling()`), `Mu1Proto.swift` (protocol reqs).

**Last commit on this thread:** `61eec92 June24` — Phase 2 (Layer B1) disk cache. (Phase 3 sits on top of it, uncommitted.)

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
| **3 (#2 + #3) — scenePhase handler** | Pause GPS + active-proto timers on `.background`; restart + immediate `minuteFlow()` refresh on `.active` (scope narrowed — CyclopsObs/SourceBase left out, see decisions) | ✓ implemented, **uncommitted** (awaiting device test) |
| 4 (Layer B2) — Cyclops trail history persistence | Optional / deferrable | not started |
| 5 — Consolidate redundant `CLLocationManager` re-init in `Municipal.swift:122` + `:160` | trivial code-health cleanup | not started |

## Phase 3 — done this session (2026-06-25)

All four open decisions were answered with the recommendations and the code landed in the working tree. Full record: [[decisions#2026-06-25--scenephase-pauseresume-handler-phase-3--2--3]].

1. `ReceiptObs.timer` — kept running. ✓
2. Immediate refresh on `.active` — yes, via `minuteFlow()`. ✓
3. Wiring — direct calls from App root `.onChange(of: scenePhase)`. ✓
4. Partition — #2 + #3 shipped together. ✓

**One divergence from the brief:** scope narrowed to GPS + the active protos (`TaipeiObs` / `NewTaipeiCityObs`) only. `CyclopsObs` and `SourceBase` were *not* touched — they're view-local, only tick while their screen is visible, and aren't reachable from the app root. Pausing the proto timers stops cyclops network work indirectly anyway.

**Remaining before this can be committed:** Jim's device test (background/foreground, lock/unlock, `.inactive` no-thrash, app-switcher resume).

## Open bugs (not blocking battery work)

- `bugs.md` 2026-06-15 — IME blocks UI on All-screen search. Open, deferred until after battery pre-release picks land.

## Next steps (when Jim resumes)

- [ ] Device-test Phase 3 (background/foreground refresh, lock/unlock no-thrash, `.inactive` no-op, app-switcher resume), then commit `Municipal+Lifecycle.swift` + the 3 modified files.
- [ ] Decide on Phase 4 (Layer B2 — cyclops trail history persistence) + #5 (Municipal `CLLocationManager` dedupe at `Municipal.swift:122` + `:160`) — both deferrable until after release.
- [ ] Post-launch: take the deferred Energy Impact measurement (verification step in [[battery]]) to confirm the foreground-idle drain hypothesis and quantify the #1/#6/Phase-3 wins.

## Open questions / blockers
- None blocking. Phase 3 just needs Jim's device test before commit.
