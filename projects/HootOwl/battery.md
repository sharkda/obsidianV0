# HootOwl — Battery

Standalone investigation log for battery consumption concerns. Distinct from `decisions.md` (atomic decisions) and `bugs.md` (single-bug entries). This file accumulates findings, the option menu, the chosen sequence, and outcome measurements over time.

Related:
- [[bugs#2026-06-10-battery-drain-user-report-unconfirmed]] — the original symptom report and verification step.
- `decisions.md` — record the chosen option here as an atomic decision when one is taken.

**Convention:** this file is updated **inline during work**, not only at session END. Per Jim 2026-06-11.

---

## How to resume

If you're picking this up after a break, read three sections in order:
1. **Status** — where this investigation currently stands.
2. **Sorted shortlist (low-hanging fruit first)** — ranked picks for quick decision-making.
3. **Verification step** — do this before any code change.

The full **Option menu** below is the reference detail. The **Decision log** and **Measurement log** at the bottom track what's been done.

---

## Status

**Pre-release shortlist complete.** User report 2026-06-10, code-scan diagnosis 2026-06-10, option menu drafted 2026-06-11. All four low-hanging-fruit picks (#1, #6, #9, #2+#3) implemented and committed by 2026-06-26. **#5 applied 2026-08-20 — the shortlist is now fully done.** What remains is verification, not implementation: the owed Phase 3 device test and the deferred (and still confounded) post-launch Energy Impact measurement.

> [!info] Status reconciled 2026-08-07
> This note previously described #9 and #2+#3 as "working tree, not committed". **Both are committed** — verified against `git log`:
> - **#9** → `04e2165` (2026-06-16)
> - **#2 + #3 (Phase 3)** → `aa6b02a` (2026-06-26), including `Municipal+Lifecycle.swift` and the `project.pbxproj` target-membership fix.
>
> Phase 3 was committed **without** the device test this note called for. That test is still owed — see the Verification section. Dated entries in the Decision log below are left as originally written (they were accurate on their date); only forward-looking status has been corrected.

**Completed picks:**
- **#2 + #3 (scenePhase pause/resume) — implemented 2026-06-25, committed `aa6b02a` 2026-06-26.** Single `.onChange(of: scenePhase)` at the App root (`hootowlApp.swift`) calling `municipal.pauseForBackground()` on `.background` and `municipal.resumeForForeground()` on `.active`; `.inactive` is a no-op. New file `Municipal+Lifecycle.swift` + `pausePolling()` / `resumePolling()` on `Mu1Base` (declared in `Mu1Proto`). On `.background`: `stopUpdateLocation()` + cancel each active proto's daily/minutely timers. On `.active`: `startUpdateLocation()` + re-create timers + one immediate `minuteFlow()` fetch per proto. **Scope narrowed from the 2026-06-16/06-24 plan:** only GPS + the active protos (`TaipeiObs` / `NewTaipeiCityObs`) are touched. `CyclopsObs` and `SourceBase` were left out — they're view-local, only tick while their screen is visible, and aren't reachable from the app root; pausing the proto timers stops cyclops network work indirectly. `ReceiptObs.timer` left running per decision. All four brief decisions answered with the recommendations. Atomic entry: [[decisions#2026-06-25--scenephase-pauseresume-handler-phase-3--2--3]]. **2026-07-12 follow-up:** the initial build failure (misleading `onChange` overload error on `hootowlApp.swift:51`) was a **missing target membership** — the new `Municipal+Lifecycle.swift` was never added to the app targets, so its methods were invisible. Added to both iOS + macOS targets; Phase 3 now compiles. Details: [[bugs#2026-07-12-misleading-onchange-expects-01-arguments-error-was-a-missing-target-membership]].
- **#1 (GPS Best → HundredMeters) — done 2026-06-13, committed `837cbef` 2026-06-15.** Sole surviving `desiredAccuracy` site is `Municipal.swift:172` (line re-verified 2026-08-17; recorded as `:163` before the file shifted), already at HundredMeters. Originally applied at 5 sites on 2026-06-12; Jim's 2026-06-13 Obs-framework dedup cleanup deleted 4 of those files. Side effect: active iOS `CLLocationManager` count dropped 5 → 2 (partially pre-completes #5).
- **#6 (Timer.publish tolerance) — done 2026-06-13, committed `837cbef` 2026-06-15.** `tolerance: <interval> * 0.1` added to all 5 active sites. The 2026-06-15 cleanup wave then deleted the 2 "left as-is" sites (`TpeTrailObs.swift`, deprecated `CyclopsScreen.swift`) plus the `zz_` candidate I'd flagged — so all 5 surviving `Timer.publish` sites now have tolerance and no ambiguity remains.
- **#9 (drop Always-auth escalation + Info.plist cleanup) — done 2026-06-15, committed `04e2165` 2026-06-16.** iOS escalation dropped at `Municipal+Loc.swift:36` (`handleAuthChange`) and `:77` (`requestLocationPermission`), both wrapped in `#if os(iOS)`. The macOS branches at lines 38-39 and 83-84 still escalate to Always. `fatalError("alreadyAlways")` at `:79` replaced with a log (latent crash risk if user granted Always via Settings). Removed the misleading `NSLocationAlwaysAndWhenInUseUsageDescription` key + string from `Info.plist`. No more iOS user-facing "Always" prompts; iOS uses WhenInUse only. **Update 2026-06-16:** Jim relaxed macOS `locAuthorized` (lines 53-56) to also accept `.authorizedWhenInUse`, matching iOS — so the macOS escalation is no longer load-bearing for `locAuthorized` to return true. The platform split (`#if os(iOS) / #elseif os(macOS)`) is preserved deliberately because `.authorizedWhenInUse` has had historical macOS-availability complaints in Xcode (see [[feedback-clauthorization-platform-split]] in auto-memory). Dropping the macOS escalation is now a no-op follow-up candidate. **Flagged-then-resolved:** `NbsObsM+LocDel.swift:44` (called `locMan.requestAlwaysAuthorization()` directly from any state, more aggressive than the Municipal escalation) was confirmed dead code — Jim staged the whole file for deletion on 2026-06-16, validating the original suspicion that `locMan` storage being commented out at `NbsObsM.swift:50` meant the site was unreachable.

No instrumented measurement taken — before/after comparison deferred to post-launch.

---

## Hypothesis (from code scan, not measured)

The drain is most likely **foreground-but-idle**, not true background:
- No `UIBackgroundModes` declared in `hootowl/Info.plist`, so iOS suspends the app shortly after backgrounding. True post-suspension drain is prevented by the OS.
- The likely scenario: user leaves the app open, phone goes idle / screen dims, but the app is still in `.active` or `.inactive` foreground state where GPS at `kCLLocationAccuracyBest` and repeating `Timer.publish` pipelines all keep running until iOS suspends.

The user perceives this as "background drain" because the screen is off — but technically it's foreground-idle.

---

## Verification step (do this before any fix)

Xcode → run on a device → Debug Navigator → Energy Impact.
- Leave the app open on the main screen, lock the phone, wait ~5 min.
- If Energy Impact stays Medium / High while idle: GPS is the dominant cost → start with options #1–2 below.
- If network activity is constant: timer polling dominates → start with option #3.
- For pinpoint detail: Instruments → Location + Energy Log.

Without this measurement, any "fix" is a guess.

---

## Sorted shortlist (low-hanging fruit first)

Ratings are estimates from the 2026-06-11 code scan, **not measurements**. Effort 1 = a few line edits across known files; 10 = significant refactor + App Review risk. Impact 1 = adjacent cleanup with no direct battery effect; 10 = directly cuts the biggest cost in this codebase. Net = Impact − Effort (higher = better fruit).

| Rank | #   | Option                                                                                | Effort | Impact     | Net         | One-line note                                                                                                      |
| ---- | --- | ------------------------------------------------------------------------------------- | ------ | ---------- | ----------- | ------------------------------------------------------------------------------------------------------------------ |
| 1    | #1  | **✓ Done 2026-06-13** (committed `837cbef` 2026-06-15). GPS `kCLLocationAccuracyBest` → `HundredMeters` (sole survivor: `Municipal.swift:172`) | 1      | 9          | +8          | Single biggest battery cost in this app. Mechanical 5-line change.                                                 |
| 2    | #2  | **✓ Done 2026-06-25** (committed `aa6b02a` 2026-06-26). Stop GPS on `scenePhase` background | 2      | 6          | +4          | One handler at app root; `stopUpdateLocation()` on `.background`, restart on `.active`.                          |
| 3    | #3  | **✓ Done 2026-06-25** (committed `aa6b02a` 2026-06-26). Cancel repeating timers on background | 3      | 5          | +2          | Same handler as #2. Narrowed to the active protos' daily/minutely timers (not CyclopsObs/SourceBase — view-local). |
| 4    | #6  | **✓ Done 2026-06-13** (committed `837cbef` 2026-06-15). Add `tolerance` to every `Timer.publish` — all 5 surviving sites have it. | 1      | 3          | +2          | Per-line change. Lets iOS coalesce wake-ups system-wide. Effectively free.                                         |
| 5    | #4  | Switch to one-shot `requestLocation()` per query                                      | 7      | 8          | +1          | Largest structural win but changes the location lifecycle model. Defer until after measurement confirms direction. |
| 6    | #9  | **✓ Done 2026-06-15** (committed `04e2165` 2026-06-16). Drop auto-escalation to `requestAlwaysAuthorization` + Info.plist cleanup | 1      | 1 / **7*** | 0 / **+6*** | *Battery impact ~0, but UX + App Store review hygiene is high. Pre-release-friendly.                               |
| 7    | #7  | `CLMonitor` (iOS 17+) for region-based wake-up                                        | 9      | 7 / 0**    | -2 / -9**   | **Impact only if you commit to a real "alert when nearby" feature. Otherwise N/A.                                  |
| 8    | #5  | **✓ Done 2026-08-20** (working tree). Consolidate `CLLocationManager` instances → 1 | 2      | 2          | 0           | Code-health, not battery. Deleted the redundant `self.locationMan = CLLocationManager()` at `wire0()`; the `init()` instance is now configured in place. **One `CLLocationManager` in the app.** |
| 9    | #8  | Add `UIBackgroundModes location` + background-capable architecture                    | 10     | 4**        | -6**        | **Same feature-dependence as #7. App Review hostile.                                                               |

### Pre-release low-hanging fruit (effort ≤ 3, no architectural change)

If you want some battery improvements baked into the release, the strict shortlist is:
- ~~**#1** — GPS accuracy~~ ✓ done 2026-06-13 (committed `837cbef` 2026-06-15). Was the single biggest win; ended up trivially small because the 2026-06-13 cleanup deleted 4 of the 5 sites.
- ~~**#6** — Timer tolerance~~ ✓ done 2026-06-13 (committed `837cbef` 2026-06-15). `tolerance: <interval> * 0.1` on all 5 sites; the 2026-06-15 cleanup wave deleted the previously "left as-is" and "skipped" sites, so no ambiguity remains.
- ~~**#9** — Drop Always-auth escalation + clean up the misleading `NSLocationAlwaysAndWhenInUseUsageDescription` string~~ ✓ done 2026-06-15, committed `04e2165` 2026-06-16. iOS escalation dropped with `#if os(iOS)` (macOS preserved); Info.plist key removed. Flagged `NbsObsM+LocDel.swift:44` for separate follow-up.
- ~~**#2 + #3 together** via one `scenePhase` handler~~ ✓ done 2026-06-25, committed `aa6b02a` 2026-06-26. ~36 lines across 4 files (`Municipal+Lifecycle.swift` new, `hootowlApp.swift` / `Mu1Base+Ext.swift` / `Mu1Proto.swift` modified), no architectural change, easily reversible. Scope narrowed to GPS + active protos.
- ~~**#5** — Dedupe the redundant `self.locationMan = CLLocationManager()` in `Municipal.swift:127` + `:169`~~ ✓ done 2026-08-20 (working tree, not yet committed). The `init` assignment at `:127` is required before `super.init()` (property is non-optional); `wire0()` was discarding it and building a second. Deleted the `wire0()` assignment, kept the config lines. ~1 line + a WHY comment.

**All five pre-release picks are now implemented.** Nothing left to *build* on this shortlist — skip the rest until post-launch measurement. The two remaining items are verifications: Phase 3 device test, and the Energy Impact measurement (still confounded — see the callout in the Measurement log).

---

## Option menu (drafted 2026-06-11)

### Quick wins — low effort, high impact

#### #1 — Lower GPS accuracy from `kCLLocationAccuracyBest` to `kCLLocationAccuracyHundredMeters`
**Effort:** ~10 lines.
**Sites:** `Municipal.swift:162`, `MunicipalObs.swift:53`, `NbsObs0.swift:601`, `NbsObs.swift:618`, `MyLocationObs.swift:42`.
**Impact:** Large. Best-accuracy GPS is the single most expensive thing the app does; HundredMeters mode is roughly an order of magnitude cheaper.
**Tradeoff:** Map dot may look slightly less twitchy. A parking app rarely needs sub-100m precision (100m ≈ half a city block). If a single screen genuinely needs Best (turn-by-turn-ish navigation), keep that one and downgrade the rest.

#### #2 — Stop GPS when app moves to background via `.onChange(of: scenePhase)` at the app root
**Effort:** ~15 lines.
**Impact:** Medium. iOS will suspend the app eventually anyway, but the 5–30s gap at Best accuracy is non-trivial; lock-screen-active states keep GPS running otherwise.
**Tradeoff:** Must restart on `.active`. If any feature needs a fresh location the moment the user re-opens the app, handle the "first location after resume is stale" case explicitly.

#### #3 — Cancel repeating timers on background in the same `scenePhase` handler
**Effort:** ~5 lines per timer.
**Sites:** `dailyTimerSubscription` and `minutelyTimerCancellable` in `Mu1Base+Ext.swift` / `MunicipalBase.swift`; `timerPub` in `CyclopsObs.swift`, `TpeTrailObs.swift`; `timerSubscription` in `SourceBase.swift`.
**Impact:** Medium. Stops network polling during the foreground-to-suspended gap.
**Tradeoff:** None significant — these timers refresh on-screen data; if the screen isn't on-screen, they're wasted. Restart on `.active`.

### Medium effort

#### #4 — Switch from continuous `startUpdatingLocation()` to one-shot `requestLocation()` per query / refresh
**Effort:** Moderate — change call sites and the delegate flow.
**Impact:** Large for battery, but changes the app's mental model.
**Tradeoff:** A parking app fits one-shot well (fetch location → query parking → done). But any screen that *tracks* the user (map dot following them) still needs continuous mode. Identify per-screen which mode each needs.

#### #5 — Consolidate the 5 `CLLocationManager` instances into 1
**Effort:** Moderate refactor.
**Sites:** `Municipal.swift`, `MunicipalObs.swift`, `NbsObs0.swift`, `NbsObs.swift`, `MyLocationObs.swift`.
**Impact:** Small for battery (the GPS chip is shared, so 5 managers don't draw 5× power), but real for delegate work and complexity.
**Tradeoff:** Risk of regressions if any manager had subtle config differences. Worth doing for code health regardless of battery.

#### #6 — Set `tolerance` on every `Timer.publish` so iOS can coalesce wake-ups
**Effort:** Small.
**Impact:** Small but effectively free — letting iOS batch timer fires saves CPU wake-ups and improves battery globally.
**Tradeoff:** None. Currently only `TpeTrailObs.swift` and the deprecated `CyclopsScreen.swift` set tolerance. Recommended value: ~10% of the interval.

### Bigger structural changes

#### #7 — Use `CLMonitor` (iOS 17+) for region-based wake-up instead of continuous tracking
**Effort:** Significant.
**Impact:** Large *only if* you genuinely want a "alert when near a tracked parking lot" feature.
**Tradeoff:** Current usage string `NSLocationAlwaysAndWhenInUseUsageDescription` promises this but the code doesn't deliver. Skip unless committing to that feature.

#### #8 — Add `UIBackgroundModes location` and do it properly
**Effort:** Significant + App Review scrutiny.
**Impact:** Enables a real background-alert feature.
**Tradeoff:** Probably the wrong direction unless committing to that feature — Apple reviews this aggressively, and you have more battery to *lose* than to gain.

### Auth cleanup (not battery, but adjacent)

#### #9 — Stop auto-escalating to `requestAlwaysAuthorization`
**Effort:** ~4 lines.
**Sites:** `Municipal+Loc.swift:36` and `:72`.
**Impact:** Doesn't save battery (Always doesn't get any capability without `UIBackgroundModes`), but removes a misleading second prompt and an App Store review risk.
**Tradeoff:** Also update / remove `NSLocationAlwaysAndWhenInUseUsageDescription` in `Info.plist` since the current string promises background alerts that the app can't deliver.

---

## #2 + #3 — Implementation plan (drafted 2026-06-16, no code change taken)

These two picks share a single `.onChange(of: scenePhase)` handler at the App root. Combined: effort 2-3, net +6 to +10 against foreground-idle drain. Approximate scope: ~30 lines across 4 files.

### What's broken today

When the user taps Home or locks the phone, HootOwl moves through SwiftUI scene phases `.active` → `.inactive` → `.background`. The app currently does nothing at any of these transitions, so:

1. **GPS keeps polling.** `CLLocationManager.startUpdatingLocation()` is never paired with a `stopUpdatingLocation()` on background. The chip keeps running at HundredMeters accuracy (mitigated by #1, not eliminated).
2. **All 5 `Timer.publish` pipelines keep firing.** Daily (`Municipal`), minutely (`Municipal`), cyclops (`CyclopsObs`), source (`SourceBase`), StoreKit retry (`ReceiptObs`). Each fire triggers downstream network work (TDX, Taipei open data, StoreKit).
3. **iOS suspends ~5-30s after backgrounding** (no `UIBackgroundModes` declared). So the wasted work is bounded in time, but the foreground-idle window — screen dimmed, app still in foreground state — is pure drain.

This is exactly the **foreground-idle drain** in the Hypothesis section. #2 + #3 close that window.

### The fix pattern

```swift
@Environment(\.scenePhase) private var scenePhase

ContentView()
    .onChange(of: scenePhase) { _, newPhase in
        switch newPhase {
        case .active:     // resume: restart location + timers, refresh data
        case .background: // tear down: stop location, cancel timers
        case .inactive:   // do nothing — transient
        @unknown default: break
        }
    }
```

**Critical:** `.inactive` must be a no-op. It fires transiently when an alert appears, the user pulls down Notification Center, or the app is multitasked. Tearing down on `.inactive` would cause thrashing.

`#2` = the `.background → stopUpdatingLocation()` + `.active → startUpdateLocation()` half.
`#3` = the `.background → cancel Timer.publish subscriptions` + `.active → re-create them` half.
Combined because they share the same lifecycle event.

### Design decisions (settle these before writing code)

1. **Where does the handler live?** The App root (`@main App` struct) — standard SwiftUI 4+ pattern. Settled.

2. **How does the handler reach the timer + location owners?**
   - **(a) Direct calls — recommended.** App root holds references to `Municipal`, `CyclopsObs`, `SourceBase` (and possibly `ReceiptObs`) singletons and calls `pauseForBackground()` / `resumeForForeground()` on each. Pragmatic, explicit, easy to reason about.
   - (b) NotificationCenter broadcast (`.appDidEnterBackground` / `.appWillEnterForeground`, owners subscribe) — loosest coupling but spreads lifecycle logic across files.
   - (c) Central `AppLifecycle` observable singleton — cleaner than (b) but adds an abstraction layer.

3. **Which timers actually pause?**
   - `dailyTimerSubscription` (Municipal, every 5s or 6h) — **pause**
   - `minutelyTimerCancellable` (Municipal, every ~60s) — **pause** (biggest single win — most frequent network polling)
   - `timerPub` in `CyclopsObs` (watch-list refresh) — **pause**
   - `timerSubscription` in `SourceBase` (zone retriever) — **pause**
   - `self.timer` in `ReceiptObs` (StoreKit retry) — **judgment call.** Lean toward leaving it running so purchases can still validate during the brief background window before suspension. Decide explicitly when implementing.

4. **What happens on `.active` after a long background?** Two staleness concerns:
   - Last location is stale (GPS hasn't fired in N minutes).
   - Parking availability data is stale (minutely timer missed N fires).

   Default: the `.active` branch should restart timers AND trigger an immediate one-shot data refresh — otherwise the user sees stale parking counts until the next regular tick.

### Recommended implementation order

1. Add `pauseForBackground()` / `resumeForForeground()` to each timer owner (`Municipal`, `CyclopsObs`, `SourceBase`). Skip `ReceiptObs` unless decision 3 above is "pause StoreKit too." Each method body is ~3-5 lines.
2. Add the same pair to `Municipal` for location: `stopUpdateLocation()` already exists; `resumeForForeground()` calls it plus restarts the daily / minutely timers and triggers an immediate parking-data refresh.
3. Wire `.onChange(of: scenePhase)` at the App root, calling the 3 owners' pause / resume.

### Risks

- **Resume omission** → app feels frozen on foreground (stale data, no location).
- **Race on rapid background → foreground cycles** → pause / resume methods must be idempotent. The existing `Mu1Base+Ext.swift` timer-start functions already begin with `?.cancel()` (de-dup pattern), so resume is naturally safe; pause needs to guard against double-cancel.
- **Missing data refresh on `.active`** → user sees stale parking counts until the next regular timer tick.

### Manual test plan when implementing

- Background for 30s → foreground (parking counts should refresh visibly).
- Lock → unlock quickly (no thrash, no torn-down state).
- Tap an alert / pull down Notification Center (`.inactive` fires) — nothing should tear down.
- App switcher → return.
- Force-quit + relaunch (no scenePhase fires; clean cold start path verified).

### Three open decisions still owed before code change

- **`ReceiptObs.timer` pause / keep:** pause for consistency, or keep running so StoreKit purchase retries continue during the brief background-before-suspension window?
- **Immediate refresh on `.active`:** trigger now, or let next regular timer fire handle it?
- **Wiring style:** direct calls from App root (option a) is the recommendation — confirm or point at an existing lifecycle pattern in the codebase.

### 2026-06-24 — Phase 3 pre-implementation brief (asked Jim, awaiting answers)

After Phase 2 (cache) committed in `61eec92`, presented Phase 3 plan to Jim with recommendations + 4 open decisions. **Jim left to upgrade Claude Code; pick up here when resuming.**

**Phase 3 scope (proposed, awaiting greenlight):**
- **New file** `Municipal+Lifecycle.swift` — `pauseForBackground()` (calls `stopUpdateLocation()`, cancels the 4 active timers), `resumeForForeground()` (re-creates the timers, calls `startUpdateLocation()`, triggers an immediate availability refresh via `Repository.shared.netRetrieve(...)`).
- **`CyclopsObs`, `SourceBase`** — add `pauseTimer()` / `resumeTimer()` methods called from Municipal's lifecycle handler.
- **App root** (`AppTabView` or wherever `@main App` lives) — `@Environment(\.scenePhase)` + `.onChange(of:)` calling `municipal.pauseForBackground()` / `municipal.resumeForForeground()`. **Skip `.inactive`** (transient — fires for alerts / Notification Center / multitasking, would cause thrashing).
- **`ReceiptObs.timer`** — untouched per Jim-pending decision #1 below.
- Estimated ~50 lines across 4 files.

**Four open decisions for Jim** (recommendations in bold):
1. `ReceiptObs.timer` — **keep running (recommended)** so StoreKit purchase retries continue during the brief background-before-suspension window; cost is a few timer fires.
2. Immediate refresh on `.active` — **yes (recommended)** even though Phase 2's cache softens the "stale 5-min-old data" feel; cost is one network fetch per resume.
3. Wiring style — **(a) direct calls from App root (recommended)**. Phase 1b already made `Municipal` the central orchestrator; one call covers GPS + 2 Municipal timers + 2 child observables.
4. Partition — **ship #2 + #3 together (recommended)** because they share the handler; splitting doubles scaffolding for marginal safety.

**When resuming:** read this section + Status + Recommended sequence, then ask Jim for the four answers before writing code.

---

## Recommended sequence

1. **Measure first** (verification step above). ~5 min. Confirms which culprit dominates before touching code.
2. **Quick wins #1 + #2 + #3 together.** ~30 lines of code across known files, no architectural change, easily reversible. If the user's report is real, these three together should cut idle drain by a large multiple.
3. **Re-measure.** Decide whether to continue.
4. **If still bad, option #4** (one-shot location). The structural fix — most apps in this category don't need continuous GPS.

**Skip for now:** #7, #8 (premature unless committing to a real background-alert feature), #9 (do as a separate auth-cleanup pass, not bundled with battery work).

---

## Decision log (append as decisions are taken)

- **2026-06-12 — Applied #1 (GPS Best → HundredMeters).** Edits at all 5 active sites: `Municipal.swift:162`, `MunicipalObs.swift:53`, `NbsObs0.swift:601`, `NbsObs.swift:618`, `MyLocationObs.swift:42`. Brief inline comment added at each site explaining the WHY. The 6th historical match in `zzz/grog01.swift:173` was skipped (deprecated `zzz/` folder). Working tree only — not committed yet. Atomic entry: [[decisions#2026-06-12-gps-accuracy-best-to-hundredmeters]].
- **2026-06-13 — #1 confirmed complete after Jim's Obs-framework dedup cleanup.** The cleanup deleted 4 of the 5 files I'd edited (`Municipalities/Obs/MunicipalObs.swift`, `Municipalities/Nbs/NbsObs0.swift`, `kitchens/nearBySearch/NbsObs.swift`, `UI/Map/MyLocationObs.swift`) along with the previously-skipped `zzz/grog01.swift`. Surviving site: `Municipal.swift:163` (line shifted from 162 by my inline comment), already at HundredMeters — no further edit needed. Re-scan confirms a single `desiredAccuracy` reference project-wide. **Side effect: active iOS `CLLocationManager()` count dropped 5 → 2** (both now `self.locationMan` re-assignments in `Municipal.swift` at lines 122 and 160 — likely redundant; ~1-line cleanup worth folding into #5 when we get there). The atomic entry [[decisions#2026-06-12-gps-accuracy-best-to-hundredmeters]] has been amended to reflect the post-cleanup state.
- **2026-06-13 — Applied #6 (Timer.publish tolerance).** Added `tolerance: <interval> * 0.1` (Apple's "10% of interval" guideline) to 5 active sites that didn't already have tolerance: `Mu1Base+Ext.swift:66` (daily, interval 5s–21600s), `Mu1Base+Ext.swift:285` (minutely), `CyclopsObs.swift:42` (cyclops watch), `SourceBase.swift:294` (zone retriever), `ReceiptObs.swift:247` (StoreKit retry). Left as-is: `TpeTrailObs.swift:112` (already had `tolerance: 2`), `UI/Cyclops/deprecated/CyclopsScreen.swift:213` (deprecated folder). **Skipped pending Jim's call:** `kitchens/ZoneRetrivers/zz_Ntpc_b08_ob.swift:106` — `zz_` prefix mirrors the deprecation convention used in the 2026-06-13 cleanup. Atomic entry: [[decisions#2026-06-13-add-tolerance-to-timer-publish-10-percent-of-interval]].
- **2026-06-15 — #1 + #6 committed in `837cbef`; ambiguities resolved by a second cleanup wave.** Jim's 2026-06-15 cleanup deleted all 3 sites flagged in the 2026-06-13 #6 entry: `ViewModel/TpeTrailObs.swift` (had `tolerance: 2`), `UI/Cyclops/deprecated/CyclopsScreen.swift` (deprecated, had `tolerance: 2`), and `kitchens/ZoneRetrivers/zz_Ntpc_b08_ob.swift` (the `zz_` candidate I'd flagged for Jim's call). All 5 surviving `Timer.publish` sites now have `tolerance: <interval> * 0.1` with no "left as-is" or "skipped" cases remaining. The `decisions.md` #6 atomic entry has been amended to reflect this.
- **2026-06-15 — Applied #9 (drop Always-auth escalation + Info.plist cleanup).** Two iOS escalation sites in `Municipal+Loc.swift` (`handleAuthChange` case `.authorizedWhenInUse` at line 36; `requestLocationPermission` same case at line 77) wrapped in `#if os(iOS)` — iOS no longer escalates, macOS keeps escalating (macOS `locAuthorized` at that point still required `.authorizedAlways`). Replaced `fatalError("alreadyAlways")` at line 79 with a log to avoid a latent crash if the user grants Always via Settings. Removed `NSLocationAlwaysAndWhenInUseUsageDescription` key + string from `hootowl/Info.plist`. **Out of scope, flagged for separate follow-up:** `NbsObsM+LocDel.swift:44` directly calls `requestAlwaysAuthorization()` from any auth state — more aggressive than the Municipal escalation. The `locMan` storage referenced there is commented out at `NbsObsM.swift:50`, suggesting the site may be dead code; needs investigation before touching. Working tree only, not yet committed. Atomic entry: [[decisions#2026-06-15-drop-always-auth-escalation-info-plist-cleanup]].
- **2026-06-16 — Jim relaxed macOS `locAuthorized` to accept `.authorizedWhenInUse`.** Updated `Municipal+Loc.swift:53-56` (the `#elseif os(macOS)` branch of `locAuthorized`) to use the same expression as iOS: `locAuthStateVbj.value == .authorizedAlways || locAuthStateVbj.value == .authorizedWhenInUse`. The platform split (`#if os(iOS) / #elseif os(macOS)`) was kept deliberately because Xcode has historically flagged `.authorizedWhenInUse` as macOS-unavailable; the explicit split is defensive against future SDK availability regressions. Saved to auto-memory as [[feedback-clauthorization-platform-split]]. **Implication for #9:** macOS no longer needs to be at `.authorizedAlways` to be considered authorized, so the macOS escalation branches at lines 38-39 (`handleAuthChange`) and 83-84 (`requestLocationPermission`) are no longer load-bearing. Dropping macOS escalation is now a clean follow-up — left out of scope for now per Jim's call.
- **2026-06-16 — `NbsObsM+LocDel.swift` deleted, validating the dead-code suspicion.** The file I'd flagged in the 2026-06-15 #9 entry (containing the more-aggressive `locMan.requestAlwaysAuthorization()` call at line 44, with the `locMan` storage commented out at `NbsObsM.swift:50`) is now staged for deletion. Confirms the original read: the site was unreachable dead code. No remaining `requestAlwaysAuthorization` on iOS anywhere in the active codebase.
- **2026-06-16 — Drafted detailed implementation plan for #2 + #3 (no code change).** Jim asked for an explanation of #2 + #3 before authorizing any edits. Captured the issue (foreground-idle drain — GPS + 5 timers never paused on `.background`), the SwiftUI `.onChange(of: scenePhase)` fix pattern, four design decisions (handler location, wiring style, which timers to pause, what to do on `.active` for staleness), recommended implementation order, risks, and manual test plan. See the new [[battery#2--3--implementation-plan-drafted-2026-06-16-no-code-change-taken]] section. Three open decisions still owed before code change: ReceiptObs pause-or-keep, immediate-refresh-on-`.active`, and wiring style.
- **2026-06-17 — Phase 1a finding: identified the Cyclops emptiness root cause (no code change).** Jim raised the "< 5 min switch-out/in shows emptiness" symptom and asked for evaluation before any fix. Investigation confirmed: `MncplCyclopsScreen` holds all display state (`cyclopsMod`, `cancellables`, `watchList`) in `@State`, while `AppTabView` hosts tabs via dynamic `ForEach(AppScreen.sorted(subTier:))` and re-renders its body every ~5s for the auto-hide tab bar (`.task(id: hideToken)`). The combination loses child view identity, wiping `@State` to defaults. `MncplAllScreen` doesn't have the bug because it reads `municipal.actParkInfos` / `parkAvPack` directly as computed properties — the recommended HootOwl pattern. **Fix plan (Phase 1b, awaiting greenlight):** lift `cyclopsMod` (and `availableTime`) onto `Municipal` (or a dedicated `@Observable` class); reduce `MncplCyclopsScreen` to a thin view that reads the singleton. Trail accumulation Combine pipeline moves to the singleton, runs once at app startup. The full SwiftUI-identity knowledge captured in a new reference doc: `~/obsidianV0/patterns/swiftui-state-and-identity.md`. Two design decisions still owed: (a) put on `Municipal` vs. new `CyclopsBuilder` class; (b) whether `watchList` also moves (it's `@AppStorage`-backed so technically safe to leave).
- **2026-06-17 — Applied Phase 1b (Layer A: lift Cyclops state to Municipal singleton).** Jim greenlit with decisions: use `Municipal` directly (not a new class), and move `watchList` too. Added 3 stored properties to `Municipal` (`cyclopsMod`, `availableTime`, `watchList`) and a new extension file `Municipal+Cyclops.swift` containing `wireCyclops()` (called from Municipal init), `refreshCyclops()`, `setWatchList(_:)`, plus persistence helpers. `MncplCyclopsScreen` rewritten as a thin view that reads from `municipal.cyclopsMod` / `availableTime` via `@Bindable` (CyclopsView still requires `@Binding<CyclopsItem>`). Removed ~50 lines of @State / wire / unwire / load / refresh. Reorder sheet extracted to `fileprivate struct ReorderSheet` with a local mutable copy that pushes each edit through `municipal.setWatchList()`. **MncplAllScreen unchanged** — its existing `@AppStorage saveWatchList` write pattern routes through UserDefaults, which Municipal now observes via `NotificationCenter.default.publisher(for: UserDefaults.didChangeNotification)`, so cross-screen pin/unpin keeps working. Working tree only — not yet committed, awaiting Jim's day-of-testing per the partition plan. Pre-existing SourceKit index noise unchanged; none of the diagnostics reference the new code. Atomic entry: [[decisions#2026-06-17-cyclops-state-lifted-to-municipal-singleton-phase-1b]].
- **2026-06-25 — Applied Phase 3 (#2 + #3: scenePhase pause/resume).** Jim greenlit all four decisions from the 2026-06-24 brief with the recommendations: (1) `ReceiptObs.timer` kept running, (2) immediate `.active` refresh = yes, (3) wiring = direct calls from App root, (4) #2 + #3 shipped together. New file `Municipal+Lifecycle.swift` (`pauseForBackground()` / `resumeForForeground()`), iterating `activeProtos`. Added `pausePolling()` / `resumePolling()` to `Mu1Base` (`Mu1Base+Ext.swift`) and declared them on `Mu1Proto`. `pausePolling()` cancels daily + minutely timers and nils `minutelyTimerCancellable` (so `setMinutelyTimer`'s nil-guard re-creates it), without touching `isActive`/fence state. `resumePolling()` guards `isActive`, restarts both timers, and fires `Task.detached { await minuteFlow() }` for the immediate fetch. App root (`hootowlApp.swift`): `@Environment(\.scenePhase)` + `.onChange` → `.active`/`.background` calls, `.inactive`/`@unknown` no-op. **Scope narrowed from the brief:** `CyclopsObs` and `SourceBase` deliberately NOT touched — view-local, only tick while their screen is visible, unreachable from the app root; pausing the proto timers stops cyclops network work indirectly. Working tree only — not committed (untracked `Municipal+Lifecycle.swift` + 3 modified files); awaiting Jim's device test. Atomic entry: [[decisions#2026-06-25--scenephase-pauseresume-handler-phase-3--2--3]].
- **2026-06-24 — Applied Phase 2 (Layer B1: disk cache for cold-launch + jettison recovery).** Jim greenlit with decisions: storage in `Library/Caches/`, 24h stale threshold, staleness badge deferred. New extension file `Municipal+Cache.swift` (~120 lines) containing `wireCacheAndSeed()` (called from Municipal.init *before* `wireCyclops()` so the cyclops rebuild sees seeded data), `noteAvailabilityChanged()` (called from the existing `actMinutely(p0:)` after the in-memory write), and a `userLoc2dVbj` subscriber throttled to 30s (coalesces GPS writes). Disk format: single JSON file `Library/Caches/hootowl-snapshot.json` containing `CachedSnapshot { written: Date, location: CachedLocation?, packs: [MncplParkAvPack] }`. Made `MncplParkItemAvail` and `MncplParkAvPack` `Codable` (declared on the struct definitions in `ParkAvailv02.swift`, not as separate extensions in Municipal+Cache.swift — Xcode caught: Swift only auto-synthesizes `Codable` when the conformance is in the same file as the type). On load, snapshots older than 24h are silently discarded. Atomic writes via `.atomic` option to avoid torn reads if app crashes mid-write. **Defer-list:** staleness badge UI (per Jim's call), `actParkInfos` caching (separate decision), `.active` re-read (slots into Phase 3). Working tree only — not yet committed; awaiting Jim's day-of-testing per the partition plan. Atomic entry: [[decisions#2026-06-24-disk-cache-for-cold-launch-jettison-recovery-phase-2-layer-b1]].

- **2026-08-20 — Applied #5 (CLLocationManager dedupe).** Deleted `self.locationMan = CLLocationManager()` from the top of `wire0()` (`Municipal.swift:169`) and added a two-line WHY comment in its place. The `init()` assignment at `:127` stays — it is required before `super.init()` because `locationMan` is a non-optional `var` (`Municipal.swift:44`). `wire0()` now configures that instance (`delegate`, `desiredAccuracy`, `distanceFilter`) instead of replacing it. **Verified there are exactly two `locationMan =` sites project-wide before the edit, one after** — the app now creates a single `CLLocationManager`. Behaviourally identical: the discarded instance had never been configured or started, so nothing was listening to it. Net effect is one fewer allocation and no ambiguity about which manager `stopUpdateLocation()` / `startUpdateLocation()` act on. **Working tree only — not committed.** **Not compile-verified** — see the caveat below. Atomic entry: [[decisions#2026-08-20-cllocationmanager-dedupe-battery-5]].

> [!warning] #5 is not compile-verified — build it in Xcode before trusting it
> `xcodebuild` cannot build this project from the CLI in a fresh environment: `Package.resolved` is **gitignored** (caught by the `*.xcworkspace` rule at `.gitignore:2`), so SPM tries to re-resolve `ConcaveHull` (a dependency since `dfa738f`, 2024-10-30) over the network and fails. This is pre-existing and unrelated to the edit — Jim's local Xcode has the package resolved in its own DerivedData.
>
> The change is a one-line deletion inside a function body, on a non-optional property that is already initialized before the function runs, so the type-check risk is about as low as a Swift edit gets. But *low risk* is not *verified*. **Build once in Xcode.** The SourceKit "cannot find type in scope" diagnostics on this file are the long-documented index noise, not real errors — none of them reference the changed lines.

---

## New repeating timer added 2026-09-10 — noted so it is not a surprise later

`NbsScreen` gained a **60 s `Timer.publish`** to tick map-pin freshness (`freshnessTick`). It follows the #6 convention — `tolerance: 6`, i.e. 10% of the interval — so it can coalesce with other wake-ups.

**Why it is cheap:** it changes one `Date` in `@State`. It does not fetch, and it deliberately is **not** a `TimelineView`, which would have rebuilt the entire `Map` every minute and made MapKit re-render — by far the most expensive thing on that screen.

**Why it is worth mentioning here anyway:** it is view-local, so like `CyclopsObs` and `SourceBase` it is **not** paused by `Municipal.pauseForBackground()`. It only ticks while `NbsScreen` is on screen, and the app is suspended when backgrounded, so this should not matter — but it is one more timer in a codebase whose battery story is built on knowing where they all are. The Phase 3 scope note already records that view-local timers were deliberately left out of the pause path.

## Measurement log (append as measurements are taken)

_(Nothing measured yet. When measurements are taken, append: date, what was measured, raw Energy Impact / Instruments observation, before/after if comparing.)_

> [!warning] Confound to control for before measuring — added 2026-08-07
> **Every proto polls for every user regardless of location.** `ActDeActOnes(ids:)` (`Municipal+Ext.swift:165–175`) has **zero callers**, and `activeIds` at `:158` is computed and discarded — the fence→activation link described in the code comment was never wired. Zones are activated only by the blanket `loadedProtos.map({ $0.activate() })` at `Municipal+Ext.swift:43`.
>
> So a user in Taipei is also polling New Taipei City continuously. This runs against the #1/#6/#9/Phase-3 wins and **will muddy the before/after Energy Impact reading** — some of the drain being measured is zones the user isn't in. Decide the activation policy, or at minimum note which zones were active, before treating any measurement as a clean read on the foreground-idle hypothesis.
>
> Cost is linear in cities: tolerable at two, meaningful at six. Full context: [[cyclops-first-run]] (Finding 3).

---

## Reconciliation — 2026-08-07

Session opened by re-reading this note against `git log`. Corrections applied above:

| Claim as written | Actual | Where fixed |
|---|---|---|
| #9 "working tree, not yet committed" | committed `04e2165` 2026-06-16 | Status, option table row 6, shortlist |
| #2 + #3 "working tree, awaiting device test" | committed `aa6b02a` 2026-06-26 | Status, option table rows 2–3, shortlist |
| #5 target `Municipal.swift:122` + `:160` | now `:127` + `:169` (file shifted) | Option table row 8, shortlist |

**Phase 3 was committed without the device test this note asked for.** That verification is still owed — background/foreground refresh, lock/unlock no-thrash, `.inactive` no-op, app-switcher resume. It is no longer a gate on committing (already committed), but it is still a gate on trusting the behaviour.

Dated entries in the Decision log above were **left as originally written** — they were accurate on the date they were written, and rewriting them would falsify the record.

---

## Re-verification — 2026-08-17

Status-reset session. Every battery claim in this note was re-checked against the working tree, not just against `git log`. **HEAD is still `860f82d` (2026-07-03), tree clean apart from untracked `AGENTS.md` — the repo has been idle ~6 weeks and nothing has drifted.**

| Claim | Check run | Result |
|---|---|---|
| #1 — one `desiredAccuracy` site, at HundredMeters | `grep -rn desiredAccuracy --include=*.swift` | ✓ exactly one hit, `Municipal.swift:172`, `kCLLocationAccuracyHundredMeters` |
| #6 — all 5 `Timer.publish` sites have tolerance | `grep -rn "Timer.publish"` | ✓ 5 sites, all `tolerance: interval * 0.1` (`SourceBase:294`, `Mu1Base+Ext:86`, `Mu1Base+Ext:305`, `CyclopsObs:42`, `ReceiptObs:247`) |
| #2+#3 — scenePhase handler live | read `hootowlApp.swift:50–58` | ✓ `.active`→`resumeForForeground()`, `.background`→`pauseForBackground()`, `.inactive` no-op |
| #2+#3 — `Municipal+Lifecycle.swift` in both targets | `grep -c` in `project.pbxproj` | ✓ 6 entries incl. 2 Sources-phase (one per target) |
| #5 — still outstanding | `grep -n "CLLocationManager()" Municipal.swift` | ✓ still two: `:127` and `:169`. **Line numbers unchanged — the shortlist is still correct as written.** |

**Only line drift found:** #1's site is `:172`, not `:163` (corrected in the Status section and option table above).

**Nothing new landed and nothing regressed.** The single remaining pre-release item is still #5, and the two owed verifications (Phase 3 device test, post-launch Energy Impact measurement) are still owed. The measurement confound flagged in the callout above is also unchanged — `ActDeActOnes` still has zero callers, re-confirmed by grep this session, so every proto still polls for every user.
