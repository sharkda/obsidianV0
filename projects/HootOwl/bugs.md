# HootOwl — Bugs

Known issues, gotchas, and bugs encountered/fixed. Newest at top.

---

<!-- Template:
## YYYY-MM-DD — Short title
**Symptom:** What goes wrong.
**Root cause:** Why it happens (if known).
**Fix / workaround:** What to do.
**Status:** open | fixed | wontfix
**Files:** path:line references.
-->

## 2026-06-09 — District-prefixed Taiwan addresses silently dropped by Apple geocoder
**Symptom:** Typing `北投區中央北路2段350巷66號` in the Nbs address search returned zero results. The same address without the district prefix (`中央北路2段350巷66號`) worked.
**Root cause:** `MKLocalSearchCompleter` and `CLGeocoder` return nothing for Taiwan addresses that lead with a 區 but no 市/縣 prefix. Prepending the city (`台北市…`) resolves them.
**Fix:** Pre-normalize the query via `AddressSearchObs.normalized(_:)` — prepend `台北市` / `新北市` when the query starts with a known district and has no 市/縣 marker. The user-visible search bar is unchanged.
**Status:** fixed (working tree, not yet committed).
**Files:**
- `hootowl/Municipalities/Nbs/AddressSearchObs.swift` — districts Sets, `normalized(_:)`, `query.didSet`.
- `hootowl/Municipalities/Nbs/NbsScreen.swift` — `geocodeAndSearch` calls `normalized(query)`.
**Extension trap:** Adding a third Taiwan city introduces 區-name collisions (中山/中正/信義/大同/北區/南區/東區/西區/中區 are shared across municipalities). First-match-wins will pick wrong. See [[swift-patterns#taiwan-address-pre-normalization]].

## 2026-06-10 — Battery drain (user report, unconfirmed)
**Symptom:** Jim reports HootOwl appears to consume significant battery even when the phone is idle / not actively in use. No instrumented measurement yet.
**Root cause:** Unconfirmed. Code scan on 2026-06-10 surfaced these candidates:
- No `UIBackgroundModes` in `hootowl/Info.plist` — so iOS suspends the app shortly after backgrounding. True post-suspension background drain is unlikely; **foreground-but-idle drain is the more probable cause** (user leaves app open, screen dims/locks before suspension, GPS + timers keep running).
- GPS configured at `kCLLocationAccuracyBest` across 5 `CLLocationManager` instances: `Municipal.swift:162`, `MunicipalObs.swift:53`, `NbsObs0.swift:601`, `NbsObs.swift:618`, `MyLocationObs.swift:42`. `distanceFilter = 100` cuts delegate callbacks but **does not reduce GPS chip power**. `kCLLocationAccuracyHundredMeters` would be sufficient for a parking-search app and ~10× cheaper.
- Auth handler auto-escalates `.authorizedWhenInUse → requestAlwaysAuthorization` at `Municipal+Loc.swift:36` and `:72`. Without `UIBackgroundModes location`, "Always" provides no actual capability — App Store review risk, but not a direct drain cause. The `NSLocationAlwaysAndWhenInUseUsageDescription` string also misleads users (claims background alerts that the app can't deliver).
- No `scenePhase` / `applicationDidEnterBackground` handling found anywhere. Nothing stops the location manager or cancels timers on background transition.
- Multiple repeating `Timer.publish` pipelines across `Mu1Base+Ext.swift`, `MunicipalBase.swift`, `SourceBase.swift`, `CyclopsObs.swift`, `TpeTrailObs.swift`. Intervals are externally injected (`v0`/`interval`) — severity depends on the actual values at the call sites.
**Fix / workaround:** None taken — Jim requested investigation only.
**Status:** open
**Verification step before any fix:** Xcode Debug → Energy Impact gauge, leave app idle on main screen ~5 min. If Medium/High while idle, GPS is dominant; if network activity is constant, timers dominate. Instruments → Location + Energy Log to confirm.
**Files (candidates, not confirmed culprits):** see Root cause section above.
**Option menu + recommended sequence:** see [[battery]] (standalone topic note).

## 2026-06-15 — IME blocks UI, user stuck in search on All screen
**Symptom:** When using IME (Chinese / multi-step input methods) in the search field on the All screen (`MncplAllScreen`), the IME / on-screen keyboard blocks the UI and the user cannot exit the search — they appear stuck on the search input.
**Root cause:** Unknown — not yet investigated. Likely candidates: the search bar fails to dismiss IME on submit/cancel; IME composition state isn't resolved when the user taps outside; a `@FocusState` (or `.searchable` focus binding) is held by the SwiftUI lifecycle. Could also be a `.searchable` / `.searchSuggestions` interaction with IME composition events (vs. final-text events).
**Fix / workaround:** TBD. First step when picking this up: reproduce in the simulator (or device) — capture which input method (注音 / 拼音 / handwriting / English) triggers it and which gesture (tap outside, swipe down, system back, etc.) fails to dismiss the IME.
**Status:** open. Logged 2026-06-15 by Jim; investigation deferred until after the current battery pre-release picks land.
**Files (likely starting point — not verified):** `hootowl/UI/mncplAll/MncplAllScreen.swift` per CLAUDE.md's `@AppStorage("mncpl_Park_SearchData")` note. The search is shared in spirit with `MncplCyclopsScreen` (via the `mncpl_watchList_data` pin list), so the same root cause may surface there.
