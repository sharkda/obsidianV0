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

**Open.** User report 2026-06-10, code-scan diagnosis 2026-06-10, option menu drafted 2026-06-11. No code change taken. No instrumented measurement taken.

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
| 1    | #1  | GPS `kCLLocationAccuracyBest` → `HundredMeters` at 5 sites                            | 1      | 9          | +8          | Single biggest battery cost in this app. Mechanical 5-line change.                                                 |
| 2    | #2  | Stop GPS on `scenePhase` background                                                   | 2      | 6          | +4          | One handler at app root; `stopUpdatingLocation()` on `.background`, restart on `.active`.                          |
| 3    | #3  | Cancel repeating timers on background                                                 | 3      | 5          | +2          | Same handler as #2; multiple `Timer.publish` sites to wire up.                                                     |
| 4    | #6  | Add `tolerance` to every `Timer.publish`                                              | 1      | 3          | +2          | Per-line change. Lets iOS coalesce wake-ups system-wide. Effectively free.                                         |
| 5    | #4  | Switch to one-shot `requestLocation()` per query                                      | 7      | 8          | +1          | Largest structural win but changes the location lifecycle model. Defer until after measurement confirms direction. |
| 6    | #9  | Drop auto-escalation to `requestAlwaysAuthorization` + update Info.plist usage string | 1      | 1 / **7*** | 0 / **+6*** | *Battery impact ~0, but UX + App Store review hygiene is high. Pre-release-friendly.                               |
| 7    | #7  | `CLMonitor` (iOS 17+) for region-based wake-up                                        | 9      | 7 / 0**    | -2 / -9**   | **Impact only if you commit to a real "alert when nearby" feature. Otherwise N/A.                                  |
| 8    | #5  | Consolidate 5 `CLLocationManager` instances → 1                                       | 6      | 2          | -4          | Code-health win, not battery (GPS chip is shared so 5 managers don't draw 5×).                                     |
| 9    | #8  | Add `UIBackgroundModes location` + background-capable architecture                    | 10     | 4**        | -6**        | **Same feature-dependence as #7. App Review hostile.                                                               |

### Pre-release low-hanging fruit (effort ≤ 3, no architectural change)

If you want some battery improvements baked into the release, the strict shortlist is:
- **#1** — GPS accuracy. Largest single win in the codebase. ~10 lines, fully reversible.
- **#6** — Timer tolerance. Free, no behavior change.
- **#9** — Drop Always-auth escalation + clean up the misleading `NSLocationAlwaysAndWhenInUseUsageDescription` string. App-Store-review-friendly to do before shipping.
- **#2 + #3 together** via one `scenePhase` handler — ~30 lines, no architectural change, easily reversible.

All four together: under ~60 lines of code, no behavior change visible to users, no risk to the release. Skip the rest until post-launch measurement.

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

_(Nothing chosen yet. When an option is taken, record an atomic decision in `decisions.md` and add a one-line back-link here with the date and chosen option.)_

---

## Measurement log (append as measurements are taken)

_(Nothing measured yet. When measurements are taken, append: date, what was measured, raw Energy Impact / Instruments observation, before/after if comparing.)_
