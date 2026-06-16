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
