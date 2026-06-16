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

**In progress.** User report 2026-06-10, code-scan diagnosis 2026-06-10, option menu drafted 2026-06-11.

**Completed picks:**
- **#1 (GPS Best → HundredMeters) — done 2026-06-13, committed `837cbef` 2026-06-15.** Sole surviving `desiredAccuracy` site is `Municipal.swift:163`, already at HundredMeters. Originally applied at 5 sites on 2026-06-12; Jim's 2026-06-13 Obs-framework dedup cleanup deleted 4 of those files. Side effect: active iOS `CLLocationManager` count dropped 5 → 2 (partially pre-completes #5).
- **#6 (Timer.publish tolerance) — done 2026-06-13, committed `837cbef` 2026-06-15.** `tolerance: <interval> * 0.1` added to all 5 active sites. The 2026-06-15 cleanup wave then deleted the 2 "left as-is" sites (`TpeTrailObs.swift`, deprecated `CyclopsScreen.swift`) plus the `zz_` candidate I'd flagged — so all 5 surviving `Timer.publish` sites now have tolerance and no ambiguity remains.
- **#9 (drop Always-auth escalation + Info.plist cleanup) — done 2026-06-15, working tree only, not yet committed.** iOS escalation dropped at `Municipal+Loc.swift:36` (`handleAuthChange`) and `:77` (`requestLocationPermission`), both wrapped in `#if os(iOS)`. The macOS branches at lines 38-39 and 83-84 still escalate to Always. `fatalError("alreadyAlways")` at `:79` replaced with a log (latent crash risk if user granted Always via Settings). Removed the misleading `NSLocationAlwaysAndWhenInUseUsageDescription` key + string from `Info.plist`. No more iOS user-facing "Always" prompts; iOS uses WhenInUse only. **Update 2026-06-16:** Jim relaxed macOS `locAuthorized` (lines 53-56) to also accept `.authorizedWhenInUse`, matching iOS — so the macOS escalation is no longer load-bearing for `locAuthorized` to return true. The platform split (`#if os(iOS) / #elseif os(macOS)`) is preserved deliberately because `.authorizedWhenInUse` has had historical macOS-availability complaints in Xcode (see [[feedback-clauthorization-platform-split]] in auto-memory). Dropping the macOS escalation is now a no-op follow-up candidate. **Flagged-then-resolved:** `NbsObsM+LocDel.swift:44` (called `locMan.requestAlwaysAuthorization()` directly from any state, more aggressive than the Municipal escalation) was confirmed dead code — Jim staged the whole file for deletion on 2026-06-16, validating the original suspicion that `locMan` storage being commented out at `NbsObsM.swift:50` meant the site was unreachable.

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
| 1    | #1  | **✓ Done 2026-06-13** (committed `837cbef` 2026-06-15). GPS `kCLLocationAccuracyBest` → `HundredMeters` (sole survivor: `Municipal.swift:163`) | 1      | 9          | +8          | Single biggest battery cost in this app. Mechanical 5-line change.                                                 |
| 2    | #2  | Stop GPS on `scenePhase` background                                                   | 2      | 6          | +4          | One handler at app root; `stopUpdatingLocation()` on `.background`, restart on `.active`.                          |
| 3    | #3  | Cancel repeating timers on background                                                 | 3      | 5          | +2          | Same handler as #2; multiple `Timer.publish` sites to wire up.                                                     |
| 4    | #6  | **✓ Done 2026-06-13** (committed `837cbef` 2026-06-15). Add `tolerance` to every `Timer.publish` — all 5 surviving sites have it. | 1      | 3          | +2          | Per-line change. Lets iOS coalesce wake-ups system-wide. Effectively free.                                         |
| 5    | #4  | Switch to one-shot `requestLocation()` per query                                      | 7      | 8          | +1          | Largest structural win but changes the location lifecycle model. Defer until after measurement confirms direction. |
| 6    | #9  | **✓ Done 2026-06-15** (working tree, not yet committed). Drop auto-escalation to `requestAlwaysAuthorization` + Info.plist cleanup | 1      | 1 / **7*** | 0 / **+6*** | *Battery impact ~0, but UX + App Store review hygiene is high. Pre-release-friendly.                               |
| 7    | #7  | `CLMonitor` (iOS 17+) for region-based wake-up                                        | 9      | 7 / 0**    | -2 / -9**   | **Impact only if you commit to a real "alert when nearby" feature. Otherwise N/A.                                  |
| 8    | #5  | Consolidate `CLLocationManager` instances → 1 (post-cleanup: 2 → 1)                   | 2      | 2          | 0           | Code-health, not battery. **Partially pre-completed by 2026-06-13 cleanup** (5 iOS instances → 2). Remaining: dedupe `Municipal.swift:122` + `:160` (both `self.locationMan = CLLocationManager()`). |
| 9    | #8  | Add `UIBackgroundModes location` + background-capable architecture                    | 10     | 4**        | -6**        | **Same feature-dependence as #7. App Review hostile.                                                               |

### Pre-release low-hanging fruit (effort ≤ 3, no architectural change)

If you want some battery improvements baked into the release, the strict shortlist is:
- ~~**#1** — GPS accuracy~~ ✓ done 2026-06-13 (committed `837cbef` 2026-06-15). Was the single biggest win; ended up trivially small because the 2026-06-13 cleanup deleted 4 of the 5 sites.
- ~~**#6** — Timer tolerance~~ ✓ done 2026-06-13 (committed `837cbef` 2026-06-15). `tolerance: <interval> * 0.1` on all 5 sites; the 2026-06-15 cleanup wave deleted the previously "left as-is" and "skipped" sites, so no ambiguity remains.
- ~~**#9** — Drop Always-auth escalation + clean up the misleading `NSLocationAlwaysAndWhenInUseUsageDescription` string~~ ✓ done 2026-06-15 (working tree, not committed). iOS escalation dropped with `#if os(iOS)` (macOS preserved); Info.plist key removed. Flagged `NbsObsM+LocDel.swift:44` for separate follow-up.
- **#2 + #3 together** via one `scenePhase` handler — ~30 lines, no architectural change, easily reversible.
- **#5** (newly eligible post-cleanup) — Dedupe the redundant `self.locationMan = CLLocationManager()` in `Municipal.swift:122` + `:160`. ~1 line. Code-health, not battery, but trivial.

All four remaining together: under ~35 lines of code, no behavior change visible to users, no risk to the release. Skip the rest until post-launch measurement.

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

---

## Measurement log (append as measurements are taken)

_(Nothing measured yet. When measurements are taken, append: date, what was measured, raw Energy Impact / Instruments observation, before/after if comparing.)_
