# HootOwl — Decisions

Architectural and design decisions, with brief rationale. Newest at top.

---

<!-- Template:
## YYYY-MM-DD — Short title
**Decision:** What was decided.
**Why:** Constraints/motivation.
**Alternatives considered:** What was rejected and why.
**Impact:** Files/areas affected.
-->

## 2026-06-25 — scenePhase pause/resume handler (Phase 3 — #2 + #3)
**Decision:** Pause GPS and the active protos' daily/minutely timers on `scenePhase == .background`, and resume them (plus one immediate availability fetch) on `.active`. `.inactive` is a deliberate no-op. Implemented per all four recommended answers from the 2026-06-24 pre-implementation brief: (1) `ReceiptObs.timer` left running, (2) immediate refresh on `.active` = yes, (3) wiring = direct calls from App root, (4) #2 + #3 shipped together. Closes the foreground-idle drain window (screen dimmed, app still foreground, GPS + timers running until iOS suspends ~5–30s; no `UIBackgroundModes` declared).
**Why:** The drain hypothesis is foreground-idle, not true background. #1 (GPS accuracy) and #6 (timer tolerance) reduced the per-tick cost; Phase 3 eliminates the wasted ticks entirely while the app is backgrounded. Pairs with Phase 2's cache: cold/resumed launches now seed from disk *and* kick an immediate live fetch on `.active`.
**Scope narrowed vs. the 2026-06-24 brief — only the Municipal-owned live path is touched (GPS + the active protos `TaipeiObs` / `NewTaipeiCityObs`).** The brief had proposed also adding pause/resume to `CyclopsObs` and `SourceBase`; on implementation both were deliberately left out:
- `CyclopsObs` drives the debug `CyclopsScreen2` and `Zone2 SourceBase` drives `ZoneRetrieveScreen` — both are view-local, only tick while their screen is visible, and are **not reachable from the app root**, so there's no handle to pause them from the lifecycle handler.
- Cyclops *display* refresh is driven by `parkInfoVbj` / `parkAvailVbj`, so pausing the proto timers already stops the cyclops network work indirectly.
**Alternatives considered:**
- Tear down on `.inactive` — rejected. `.inactive` fires transiently for alerts / Notification Center pull-down / multitasking; tearing down there causes thrash. Only `.background` tears down.
- NotificationCenter broadcast or a central `AppLifecycle` observable (brief options b/c) — rejected per recommendation (a). Phase 1b already made `Municipal` the central orchestrator; one `.onChange` covers GPS + the active protos' timers.
- Pause `ReceiptObs.timer` too — rejected (decision #1). Left running so StoreKit purchase retries can still validate during the brief background-before-suspension window; cost is a few timer fires.
- Skip the immediate `.active` refresh and let the next regular tick handle it — rejected (decision #2). Even with Phase 2's cache softening staleness, a resume fires one immediate fetch so counts are live, not up-to-a-minute old.
- Split #2 and #3 into separate changes — rejected (decision #4). They share the same handler; splitting doubles scaffolding for marginal safety.
**Implementation:**
- **New file** `hootowl/Municipalities/framework/Municipal+Lifecycle.swift` — `pauseForBackground()` (calls `stopUpdateLocation()`, then `activeProtos.forEach { $0.pausePolling() }`) and `resumeForForeground()` (calls `startUpdateLocation()`, then `activeProtos.forEach { $0.resumePolling() }`). Both log via `ffl(…,.info)`. File header documents the scope-narrowing rationale.
- `hootowl/Municipalities/framework/Mu1Proto.swift:72-76` — added `pausePolling()` / `resumePolling()` to the `Mu1Proto` protocol (default impls in `Mu1Base+Ext.swift`), so the lifecycle handler can iterate `activeProtos` generically.
- `hootowl/Municipalities/framework/Mu1Base+Ext.swift` — `pausePolling()`: `dailyTimerSubscription?.cancel()` + `minutelyTimerCancellable?.cancel()` then `minutelyTimerCancellable = nil` (so `setMinutelyTimer()`'s nil-guard re-creates it on resume); does **not** touch `isActive`/fence state; idempotent for rapid background→foreground cycles. `resumePolling()`: guards `isActive` (skips if inactive), then `startTimerRetrievDaily()` + `setMinutelyTimer()` + `Task.detached { await minuteFlow() }` for the immediate fetch.
- `hootowl/App/hootowlApp.swift` — added `@Environment(\.scenePhase) private var scenePhase` and a `.onChange(of: scenePhase)` on the root scene: `.active → municipal.resumeForForeground()`, `.background → municipal.pauseForBackground()`, `.inactive → break`, `@unknown default → break`.
- Immediate-refresh path uses the existing `minuteFlow()` (not `Repository.shared.netRetrieve(...)` as the brief had guessed) — `minuteFlow()` is the proto's own availability-fetch entry point.
**Idempotency / races:** `pausePolling()` is safe to call twice (double `?.cancel()` is harmless). `resumePolling()` is safe because the timer-start helpers already begin with `?.cancel()` (de-dup pattern). The `isActive` guard in `resumePolling()` prevents resuming a proto that was never started.
**Defer-list:** Phase 4 (Layer B2 — cyclops trail history persistence) and #5 (dedupe `self.locationMan = CLLocationManager()` at `Municipal.swift:122` + `:160`) remain not started, both deferrable to post-launch.
**Validation:** Working tree only — **not committed**. New file `Municipal+Lifecycle.swift` is untracked; `hootowlApp.swift`, `Mu1Base+Ext.swift`, `Mu1Proto.swift` modified. Manual test plan before commit:
- Background for 30s → foreground → counts refresh visibly (immediate fetch fires).
- Lock → unlock quickly → no thrash, no torn-down state.
- Tap an alert / pull down Notification Center (`.inactive` fires) → nothing tears down.
- App switcher → return → GPS + timers resume.
- Force-quit + relaunch → clean cold-start path (no scenePhase fires; Phase 2 cache seeds).

See [[battery]] partition plan; supersedes [[battery#2026-06-24--phase-3-pre-implementation-brief-asked-jim-awaiting-answers]].

## 2026-06-24 — Disk cache for cold-launch / jettison recovery (Phase 2 — Layer B1)
**Decision:** Persist the latest user location and per-municipality `MncplParkAvPack` snapshot to `Library/Caches/hootowl-snapshot.json`. On Municipal init (before `wireCyclops()`), seed the in-memory `parkAvPack` dict and `userLoc2dVbj` from cache if the snapshot is < 24h old. Phase 2 of the battery investigation partition plan; entirely additive (no UI change, no behavior change for warm-starts).
**Why:** Phase 1b fixed warm switches (state survives view re-mount). But cold launches and post-jettison resumes still show empty cells because `parkAvPack` starts empty and the first availability fetch takes ≥1s. With cache, the user sees real numbers immediately; fresh data fades in seconds later. Foundation for Phase 3's `.active` re-read story.
**Alternatives considered:**
- `@AppStorage` / UserDefaults — rejected. Apple discourages larger blobs (parkAvPack can be 10-50KB per municipality); semantically wrong (this is regenerable cache, not preferences).
- `Library/Application Support/` — rejected for now. Survives iOS purges under storage pressure, but the data is regenerable and a parking app on a low-storage device has bigger problems than a re-fetch.
- Cache `actParkInfos` (static daily data) too — deferred. Large, changes rarely, daily timer re-fetches on next foreground tick. Separate decision.
- Write only on `.background` — rejected. Simpler to write on every update (one small write per minute); survives crashes; cost is negligible.
- Stale threshold of 1h / 7d instead of 24h — 24h chosen per Jim's call. Aligns with "user opens HootOwl ~once a day" intuition; tunable later if numbers feel stale or refreshes feel wasteful.
- Staleness badge UI — deferred per Jim's call. Cache infrastructure ships clean; badge ships later once Jim has felt the actual age distribution in real use.
**Implementation:**
- **New file** `hootowl/Municipalities/framework/Municipal+Cache.swift` — `wireCacheAndSeed()` (called from Municipal.init), `noteAvailabilityChanged()` (hook for actMinutely), `wireLocationPersistence()` (throttled 30s userLoc2dVbj sink), `writeSnapshot()`, `seedFromCache()`, `cacheFileURL()`. Plus `CachedSnapshot` + `CachedLocation` envelope types.
- `hootowl/Municipalities/framework/ParkAvailv02.swift` — added `Codable` to the `MncplParkItemAvail` and `MncplParkAvPack` struct declarations directly. Originally written as one-line empty extensions in `Municipal+Cache.swift`, which Xcode rejected: Swift only auto-synthesizes `Codable` when the conformance is declared in the same file as the type. Corrected 2026-06-24 in response to Jim's first compile pass. All members were already primitive Codable types, so no further work needed.
- `hootowl/Municipalities/framework/Municipal.swift:110` — `actMinutely(p0:)` ends with `noteAvailabilityChanged()` to persist on every availability update.
- `hootowl/Municipalities/framework/Municipal.swift:131` — init calls `wireCacheAndSeed()` *before* `wireCyclops()` so the cyclops Combine pipeline sees the seeded data on its first refresh.
- Disk format example: `{ "written": ..., "location": { "lat": ..., "lng": ..., "captured": ... }, "packs": [ { "converted": ..., "published": ..., "municipal": "tpe", "items": [{"parkId": ..., "cars": ..., "chargers": ...}, ...] }, ... ] }`. Written via `Data.write(to:options:.atomic)` to avoid torn-file reads.
- `cacheMaxAge: TimeInterval = 24 * 60 * 60`. Stale snapshots are silently discarded (logged at `.info`).
- `locationWriteThrottle: TimeInterval = 30`. The userLoc2dVbj sink uses Combine's `.throttle(for:scheduler:latest:)` to coalesce rapid GPS updates into one write per ~30s.
**Defer-list:**
- Staleness badge UI (`MncplCyclopsScreen` infoBar augmentation, `MncplAllScreen` row badging) — separate change, requires Jim's visual call + Localizable.xcstrings entries.
- `actParkInfos` (static daily data) caching — separate decision.
- On-`.active` re-read trigger — slots into Phase 3 (`scenePhase` handler). Currently the seed only happens at init (cold launch).
**Validation:** Working tree only, not committed. Pre-existing SourceKit index noise unchanged; the new file inherits the same `Cannot find type 'MncplParkItemAvail' / 'MncplParkAvPack' / 'Municipal' in scope` noise that all Municipal-area edits trigger this session, and downstream `Codable conformance` diagnostics are caused by those misses (not real issues). Manual test plan before commit:
- Cold launch with cached data present: verify counts appear immediately (no flash of empty) and refresh from network shortly after.
- Cold launch with no cache file: verify silent no-op, then normal first-fetch flow.
- Set system clock forward >24h, relaunch: verify cache is treated as stale (no seed), then normal first-fetch flow.
- Move the device significantly between launches: verify last cached location is used briefly until GPS gives a fresh fix.
- Pin/unpin during use: verify cache is written on next `actMinutely` tick (not lost on next launch).

See [[battery]] partition plan for context.

## 2026-06-17 — Cyclops state lifted to Municipal singleton (Phase 1b — Layer A)
**Decision:** Move `cyclopsMod`, `availableTime`, and `watchList` from `MncplCyclopsScreen`'s `@State` onto the `Municipal` `@Observable` singleton. `MncplCyclopsScreen` becomes a thin view that reads from `municipal.*` via `@Bindable` and pushes watchlist edits through `municipal.setWatchList(_:)`. This is Phase 1b of the battery investigation partition plan.
**Why:** The pre-fix `MncplCyclopsScreen` held all display state in `@State`, including the trail-bearing `cyclopsMod`. SwiftUI loses view identity when the host re-renders — `AppTabView` hosts tabs via dynamic `ForEach(AppScreen.sorted(subTier:))` and an auto-hide tab bar that re-renders body every 5s — wiping `@State` to defaults. The result was the user-visible "screen goes empty on quick switch out/in" bug. Lifting display state to the singleton eliminates the dependency on view identity entirely. Background: [[swiftui-state-and-identity]] in the patterns vault.
**Alternatives considered:**
- New `@Observable CyclopsBuilder` class injected separately — rejected per Jim's call: keeping it on `Municipal` is one fewer file, one fewer environment injection, and the cyclops concerns are already coupled to Municipal's data flow.
- Leave `watchList` on the view (`@AppStorage`-backed already survives @State reset) — rejected per Jim's call: consolidate the source of truth on Municipal even though it doesn't strictly need to move. Cleaner data flow and simpler future cache logic in Phase 2.
- Refactor `MncplAllScreen` at the same time — deferred. MncplAllScreen doesn't have the bug (it reads `municipal.actParkInfos` / `parkAvPack` directly). Its existing `@AppStorage saveWatchList` write pattern routes through UserDefaults, which Municipal now observes — so cross-screen pin/unpin keeps working without modification.
**Implementation:**
- **New file** `hootowl/Municipalities/framework/Municipal+Cyclops.swift` — `wireCyclops()` (called from Municipal init), `refreshCyclops()`, `setWatchList(_:)`, `loadWatchListFromStorage()`, `reloadWatchListIfChanged()`. Subscriptions stored in the existing `Municipal.cancelBag`. UserDefaults observed via `NotificationCenter.default.publisher(for: UserDefaults.didChangeNotification)` so writes from any screen flow into Municipal.
- `hootowl/Municipalities/framework/Municipal.swift:76-79` — added 3 stored properties: `cyclopsMod: CyclopsModel = .Zero`, `availableTime: Date? = nil`, `watchList: [String] = []`.
- `hootowl/Municipalities/framework/Municipal.swift:130` — added `wireCyclops()` call at the end of init.
- `hootowl/Municipalities/UI/MncplCyclopsScreen.swift` — rewritten. Removed `@State cyclopsMod`, `@State watchList`, `@State availableTime`, `@State cancellables`, `wire()`, `unwire()`, `loadWatchList()`, `refreshCyclops()`. Body reads `municipal.*` directly. `@Bindable var bindable = municipal` for `CyclopsView`'s `@Binding<CyclopsItem>` requirement. Reorder sheet extracted to `fileprivate struct ReorderSheet` with a local mutable list + push-on-edit via `municipal.setWatchList()`.
- `MncplAllScreen.swift` — unchanged.
**Validation:** Working tree only, not committed. Pre-existing SourceKit index noise unchanged; none of the diagnostics reference the new code. Manual test plan to run before commit:
- Open Cyclops with at least one pin → wait for parking counts to load.
- Switch to another tab → return within 5 min → counts should still be visible (the bug).
- Switch to another tab → wait > 5s (auto-hide tab bar trigger) → return → counts should still be visible.
- Background the app → return after a minute → counts should still be visible.
- Reorder sheet: move and delete should still persist across sessions.
- `MncplAllScreen` swipe-to-pin/unpin should still work, and the change should reflect in Cyclops immediately (Municipal observes UserDefaults).

See [[battery]] partition plan and [[swiftui-state-and-identity]] for the underlying SwiftUI behavior.

## 2026-06-15 — Drop Always-auth escalation + Info.plist cleanup
**Decision:** Stop auto-escalating from `.authorizedWhenInUse` to `requestAlwaysAuthorization()` on iOS, and remove the misleading `NSLocationAlwaysAndWhenInUseUsageDescription` key from `Info.plist`. Pre-release pick **#9** from [[battery#sorted-shortlist-low-hanging-fruit-first]].
**Why:** The escalation was triggering a second iOS dialog asking for Always-permission, but the app declares no `UIBackgroundModes` so Always provided zero actual background capability. The escalation was net-negative: misleading UX + App Store review risk (Apple flags apps that ask for Always without legitimate background usage). The Info.plist string further promised "background alerts" that the code never delivered. With escalation removed and the key gone, the app asks for `WhenInUse` only — honest, minimum-necessary permission.
**Alternatives considered:**
- Keep the key but rewrite the string to match reality — rejected. If the key exists, Apple may still surface the Always prompt path or scrutinize it at review. Cleaner to remove entirely.
- Also touch the macOS branch (relax `locAuthorized` to accept WhenInUse on macOS, then drop macOS escalation) — partly taken on 2026-06-16 by Jim: macOS `locAuthorized` (`Municipal+Loc.swift:53-56`) now accepts `.authorizedAlways || .authorizedWhenInUse`, matching iOS. The platform split (`#if os(iOS) / #elseif os(macOS)`) is preserved deliberately because `.authorizedWhenInUse` has historical macOS-availability complaints in Xcode — see [[feedback-clauthorization-platform-split]]. **macOS still escalates** (lines 38-39, 83-84) — dropping that is a follow-up candidate since the escalation is no longer load-bearing for `locAuthorized`, but it isn't actively harmful and was kept out of #9's scope.
**Implementation:**
- `hootowl/Municipalities/framework/Municipal+Loc.swift:34-37` — `handleAuthChange` case `.authorizedWhenInUse` wrapped in `#if os(iOS)`: iOS logs only, macOS still calls `requestAlwaysAuthorization()`.
- `hootowl/Municipalities/framework/Municipal+Loc.swift:75-78` — `requestLocationPermission` case `.authorizedWhenInUse` wrapped the same way.
- `hootowl/Municipalities/framework/Municipal+Loc.swift:79-80` — `case .authorizedAlways: fatalError("alreadyAlways")` replaced with a log. Latent crash if the user granted Always via Settings while the guard at line 66 raced; now a no-op log.
- `hootowl/Info.plist:7-8` — `NSLocationAlwaysAndWhenInUseUsageDescription` key + string removed.
**Flagged-then-resolved:**
- `hootowl/Municipalities/Nbs/NbsObsM+LocDel.swift:44` — was flagged on 2026-06-15 (`locMan.requestAlwaysAuthorization()` called directly from any auth state, with `locMan` storage commented out at `NbsObsM.swift:50`, suggesting dead code). Jim staged the file for deletion on 2026-06-16, validating the read. No remaining iOS `requestAlwaysAuthorization` call sites in the active codebase.
**Validation:** Working tree only, not yet committed. Manual test plan when verifying: launch app fresh on iOS → grant WhenInUse → confirm no second "Always" prompt appears.

See [[battery]] for the full investigation.

## 2026-06-13 — Add tolerance to Timer.publish (10% of interval)
**Decision:** Add `tolerance: <interval> * 0.1` to all active `Timer.publish` call sites that didn't already have it. Pre-release pick **#6** from [[battery#sorted-shortlist-low-hanging-fruit-first]].
**Why:** A non-zero tolerance on `Timer.publish` lets iOS coalesce timer fires with other apps' wake-ups, reducing CPU wake-ups and improving battery globally. Apple's documented recommendation is ~10% of the interval — small enough to be invisible UX-wise, large enough for meaningful coalescing. Effectively free win.
**Alternatives considered:**
- Fixed `tolerance: 2` to match the existing precedent in `TpeTrailObs.swift:112` — rejected. Fixed tolerance is fine for short intervals but wastes coalescing opportunity for the daily timer (interval up to 21600s = 6h). `interval * 0.1` scales naturally across the full range.
- Higher tolerance (e.g. 25%) — would coalesce harder but starts to feel unreliable. 10% is the documented sweet spot.
**Impact:**
- `hootowl/Municipalities/framework/Mu1Base+Ext.swift:66` — daily timer (interval 5s–21600s depending on `timerDailySoon`)
- `hootowl/Municipalities/framework/Mu1Base+Ext.swift:285` — minutely timer
- `hootowl/ViewModel/CyclopsObs.swift:42` — cyclops watch timer
- `hootowl/Municipalities/Zone2/SourceBase.swift:294` — zone retriever timer
- `hootowl/iAp/Receipe/ReceiptObs.swift:247` — StoreKit receipt retry timer
- Sites originally "left as-is" or "skipped" were all deleted in Jim's 2026-06-15 cleanup wave (so the leave-alone decision became moot via deletion): `ViewModel/TpeTrailObs.swift` (had `tolerance: 2`), `UI/Cyclops/deprecated/CyclopsScreen.swift` (deprecated, had `tolerance: 2`), `kitchens/ZoneRetrivers/zz_Ntpc_b08_ob.swift` (the `zz_` candidate I'd flagged for Jim's call).
**Status:** Functionally complete as of 2026-06-15. All 5 surviving `Timer.publish` sites have `tolerance: <interval> * 0.1`, no remaining ambiguous cases.
**Validation:** Committed in `837cbef` on 2026-06-15. No diagnostics raised on the edited lines.

See [[battery]] for the full investigation and the ranked option list.

## 2026-06-12 — GPS accuracy Best → HundredMeters
**Decision:** Change `desiredAccuracy` from `kCLLocationAccuracyBest` to `kCLLocationAccuracyHundredMeters` at all 5 active `CLLocationManager` configuration sites. This is pre-release pick **#1** from [[battery#sorted-shortlist-low-hanging-fruit-first]].
**Why:** Best-accuracy GPS is the single most expensive thing the app does — HundredMeters is roughly an order of magnitude cheaper. A parking-search app does not need sub-100m precision; `distanceFilter = 100` was already in place, so the existing UX expectation is already 100m-scale.
**Alternatives considered:**
- Keep Best on one or more screens that genuinely need it (e.g. turn-by-turn-ish navigation) — rejected on inspection; none of the 5 sites had surrounding context suggesting Best was load-bearing.
- `kCLLocationAccuracyNearestTenMeters` instead — overkill for parking search and would lose most of the battery savings.
**Impact (after 2026-06-13 cleanup reconciliation):**
- `hootowl/Municipalities/framework/Municipal.swift:163` — sole surviving site, now `kCLLocationAccuracyHundredMeters` with a brief inline rationale comment.
- 4 other originally-edited files were deleted by Jim's 2026-06-13 Obs-framework dedup cleanup (so the edits became moot via deletion): `Municipalities/Obs/MunicipalObs.swift`, `Municipalities/Nbs/NbsObs0.swift`, `kitchens/nearBySearch/NbsObs.swift`, `UI/Map/MyLocationObs.swift`. The deprecated `zzz/grog01.swift` (skipped during the edit) was removed in the same cleanup.
**Status:** Functionally complete as of 2026-06-13. Single live `desiredAccuracy` site, already correct. No further code change needed for #1.
**Side effect:** Active iOS `CLLocationManager()` instance count dropped 5 → 2 — partially pre-completes #5. The 2 remaining are both `self.locationMan = …` re-assignments in `Municipal.swift` at lines 122 and 160; likely 1-line dedupe.
**Validation:** Committed in `837cbef` on 2026-06-15 alongside the #6 edits and Jim's 2026-06-13/15 cleanup waves. Pre-existing SourceKit index noise unchanged; none of the diagnostics reference these lines or `CLLocationManager`.

See [[battery]] for the full investigation and the ranked option list this came from.

## 2026-06-10 — Disambiguate colliding district names by nearest user location
**Decision:** When `AddressSearchObs.normalized(_:)` is extended past Taipei + New Taipei, resolve 區-name collisions by picking the candidate city whose centroid (or nearest loaded `MncplParkItem`) is closest to the user's current location — not by first-match-wins ordering. This promotes option (c) in [[swift-patterns#taiwan-address-pre-normalization]] from "one of three" to the chosen rule.
**Why:** HootOwl is a "what parking is near me" app — the user's location is almost always available and is the strongest disambiguation signal. The "user searching a far destination" failure mode is uncommon here and is already covered by the 市/縣 escape hatch.
**Alternatives considered:**
- First-match-wins ordering — rejected, silently wrong for shared districts.
- Remove colliding names from all Sets to force loud failure — rejected, punishes the common case to handle the rare one.
- `completer.region.center` biasing only — covers typeahead but not the `CLGeocoder` fallback path; explicit nearest-city choice covers both.
**Required fallbacks:**
- Location unavailable (first launch, permission denied, indoors with no fix): return the query unchanged so the geocoder fails loud and the user is prompted to type 市. Do NOT default to a first-match guess — that recreates the original bug.
- Border-zone correctness (e.g. southern 基隆 vs 台北): rank by nearest-known-parking-lot distance using `MncplParkItem` coordinates when lot data is loaded; centroid distance can flip the wrong way near city lines.
- Query already contains 市/縣: skip normalization entirely (current behavior preserved — `台中市信義區` always routes to Taichung).
**Impact (when implemented — not done yet, code change is deferred):**
- `hootowl/Municipalities/Nbs/AddressSearchObs.swift` — `normalized(_:)` switches from ordered `Set<String>` checks to a `[district: [MunicipalEnum]]` lookup + distance ranking. Needs read access to `MyLocationObs.clLoc.location` (or equivalent) at normalization time.
- The MARK warning block in `AddressSearchObs.swift` should be rewritten to describe the chosen rule, not the three-option menu.

See [[bugs#2026-06-09-district-prefixed-taiwan-addresses-silently-dropped-by-apple-geocoder]] and [[swift-patterns#taiwan-address-pre-normalization]].

## 2026-06-09 — Taiwan address normalization for Apple geocoder
**Decision:** Before passing user-typed Taiwan addresses to `MKLocalSearchCompleter` or `CLGeocoder`, run them through `AddressSearchObs.normalized(_:)`, which prepends `台北市` / `新北市` when the query starts with a known 區 and contains no 市/縣 marker. The search bar still shows the original user input.
**Why:** Apple's geocoder returns nothing for Taiwan addresses that lead with a 區 only (e.g. `北投區中央北路2段350巷66號`). The same address resolves cleanly with the city prepended. This is a quiet failure mode — users get an empty result and no signal that they need to add the city.
**Alternatives considered:**
- Show an error/hint asking users to add 市/縣 — rejected, worse UX than silently normalizing.
- Use `completer.region` bias only — insufficient on its own; geocoder still returns nothing without the prefix.
**Impact:**
- `hootowl/Municipalities/Nbs/AddressSearchObs.swift` — `taipeiDistricts`, `newTaipeiDistricts`, `normalized(_:)`, `query.didSet`.
- `hootowl/Municipalities/Nbs/NbsScreen.swift` — `geocodeAndSearch` passes `normalized(query)` to `CLGeocoder().geocodeAddressString(_:in:)`.

See [[swift-patterns#taiwan-address-pre-normalization]] for the collision trap when adding more cities.
