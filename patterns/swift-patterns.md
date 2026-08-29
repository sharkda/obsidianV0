# Swift Patterns

Established Swift / SwiftUI conventions for Jim's projects. Append new patterns as they're discovered.

---

## Concurrency
- Prefer `async`/`await` over callbacks.
- Mark UI-mutating code with `@MainActor` explicitly.

## Logging
- Use `ffl()` everywhere, not `print()`. Pass a level when relevant: `ffl("msg", .info)`, `ffl("msg", .error)`.
- Pair every `ffl(.error)` with a simulator earcon so errors can't be missed:
  ```swift
  #if targetEnvironment(simulator)
  Earcon.alert_high_intensity
  Earcon.ps(1109)
  #endif
  ```

## Access control
- `fileprivate` for view helpers, sub-views, and state that shouldn't leak.
- `private` for extension members on screens.
- `@Observable` published props: `fileprivate(set)` when external read is needed but writes stay internal.

## SwiftUI
- `NavigationStack`, never `NavigationView`.
- `List` should be a direct child of `NavigationStack` — wrapping in `VStack` breaks bottom safe area on iOS 17+. Use `.safeAreaInset(edge: .top)` for non-scrolling content above a list.
- Search: `.searchable` + `.searchSuggestions` when no inline toolbar layout needed. For search-in-toolbar, use `TextField` in `ToolbarItem(placement: .principal)`.
- `.navigationBarTitleDisplayMode(.inline)` to keep nav bar compact.
- Small debug labels in the nav bar: `ToolbarItem(placement: .principal)` with `.font(.caption2)` — not `.navigationTitle`.

## Observation vs Combine
- `@Observable` types: read properties directly in computed vars; SwiftUI tracks changes automatically.
- Combine (`sink` + `@State`) only when accumulating state across successive deliveries (e.g. trails/history).
- **For state-bearing screens, the accumulation should live on the singleton, NOT in view-local `@State`** — `@State` can silently reset when SwiftUI loses view identity (notably with dynamic `ForEach` inside `TabView(selection:)`, which is exactly how `AppTabView` is constructed). Deep dive + diagnostic checklist: [[swiftui-state-and-identity]].

## Availability
- Target latest iOS/macOS only. Do NOT write `#available` branches or legacy fallbacks unless explicitly asked.

---

<!-- Append new patterns below with a short heading and a one-line rationale. -->

## New Swift file must be added to Target Membership (both iOS + macOS)
**Rule:** A `.swift` file only compiles if it's in a target's Compile Sources phase (`project.pbxproj`). Files created **outside Xcode** (written to disk directly, e.g. by a tool/agent) are on disk but **not in any target** — the compiler never sees their symbols. In this project, app-target files appear **twice** in the Sources phase (iOS app + macOS app), so tick **both** Target Membership boxes.

**Why it matters — the error lands somewhere else.** Symbols from an orphaned file read as "doesn't exist" at every *call site*. When the call is inside an **overloaded** API's trailing closure (e.g. SwiftUI `.onChange(of:)`), Swift can't anchor the closure, fails against all overloads, and reports a **misleading, shifting arg-count error** ("expects 0 arguments, but 1 was used" ↔ "expects 1 argument, but 2 were used") on the *closure*, not a clean "no such member." Editing the closure changes which overload gets blamed — a tell-tale sign the real problem is a missing symbol, not the closure.

**Diagnosis:** `grep -n "MyNewFile.swift" *.xcodeproj/project.pbxproj` — no hits ⇒ not in the build. Confirm by diffing against a known-good sibling file (expect a `PBXFileReference`, a `PBXBuildFile` per target, a group child, and a Sources-phase entry per target).

**Fix:** Xcode → select file → File Inspector (⌥⌘1) → check both Target Membership boxes (or right-click group → Add Files → check both targets). Prefer hand-editing `pbxproj` only as a last resort.

Incident: [[bugs#2026-07-12-misleading-onchange-expects-01-arguments-error-was-a-missing-target-membership]] (Phase 3 `Municipal+Lifecycle.swift`).

## Taiwan address pre-normalization (MKLocalSearchCompleter / CLGeocoder)
**Rule:** Before sending a Taiwan address query to Apple's geocoder, prepend the city (`台北市` / `新北市` / …) when the query starts with a known 區 and contains no 市/縣 marker. Keep the user-visible text untouched — only the geocoder input is normalized.

**Why:** Apple's geocoder silently returns nothing for district-only-prefixed Taiwan addresses (e.g. `北投區…`). Same address with city prepended resolves cleanly. The failure has no error signal, so users blame the app.

**Reference impl:** `AddressSearchObs.normalized(_:)` in `hootowl/Municipalities/Nbs/AddressSearchObs.swift`. Called from `query.didSet` (completer) and `NbsScreen.geocodeAndSearch` (geocoder).

### District-name collision trap (extension warning)
Safe today because only Taipei + New Taipei are supported and their districts don't overlap. **Adding a third city introduces collisions** — many 區 names are shared across municipalities:

| District | Cities |
|----------|--------|
| 中山區   | 台北, 基隆, 高雄 |
| 中正區   | 台北, 基隆, 高雄 |
| 信義區   | 台北, 基隆, 台中 |
| 大同區   | 台北, 台中, 高雄 |
| 仁愛區   | 基隆, 台南 |
| 北/南/東/西/中區 | 台中, 台南, 新竹, 嘉義 |

First-match-wins ordering in `normalized(_:)` will silently pick whichever Set is checked first. Wrong half the time.

**When extending:** for each new district, either (a) confirm uniqueness across all supported cities' Sets, or (b) **remove the colliding name from all Sets** so the geocoder fails loudly and the user types 市 themselves, or (c) disambiguate by **nearest user location** (chosen rule, see below). The 市/縣 guard remains the escape hatch — explicit user input is always respected.

**Chosen rule** (per [[decisions#2026-06-10-disambiguate-colliding-district-names-by-nearest-user-location]]): option (c). When a district is shared across supported cities, pick the candidate city whose centroid (or nearest loaded `MncplParkItem` when lot data is available) is closest to `MyLocationObs`'s current location. This is the right rule for HootOwl because the app is fundamentally a nearby-parking app — the user's location is the strongest available signal and almost always present.

**Required fallback when location is unavailable** (first launch, permission denied, indoors with no fix): return the query unchanged so the geocoder fails loud and the user is prompted to type 市. Do NOT silently default to the first city in the lookup table — that recreates the original first-match-wins bug.

**Border-zone edge case:** a user in southern 基隆 may be physically closer to 台北's 中山區 centroid than 基隆's own 中山區 centroid. Mitigation when this becomes a real complaint: rank by nearest-known-parking-lot distance using `MncplParkItem` coordinates rather than by city centroid.

**Destination-search edge case:** a user driving from 台北 toward 台中 while typing `信義區` will be routed to 台北 (their current location) instead of 台中 (their destination). The 市/縣 escape hatch handles power users (`台中市信義區` overrides). If this becomes a frequent complaint, a "you might also mean…" affordance in the suggestion list is the next escalation.

The full warning is mirrored as a MARK block in `AddressSearchObs.swift`.

## Starting a poller must also fire one immediate fetch

**Rule:** Any code path that starts or restarts a repeating timer must **also kick one immediate fetch**. A timer only guarantees the *second* data delivery — the first interval is dead air. If a screen renders from that data, it renders empty for the whole interval.

```swift
// wrong — first data arrives one full interval late
func activate() {
    isActive = true
    startTimerRetrievDaily()
    setMinutelyTimer(mg0: 15)
}

// right — timer governs the cadence, not the first delivery
func resumePolling() {
    guard isActive else { return }
    startTimerRetrievDaily()
    setMinutelyTimer()
    Task.detached { [weak self] in await self?.minuteFlow() }   // ← the kick
}
```

**Why it hides:** a warm cache masks it completely. If startup seeds display state from disk before the first tick, the dead air is invisible — until the cache is absent or expired, at which point it looks like a *different* bug ("only broken on first run"). It also produces the classic misleading workaround: force-quit and relaunch "fixes" it, because relaunch repopulates the cache.

**Audit prompt:** whenever there are two entry points into the same polling machinery (cold `activate()` vs. warm `resumePolling()`, or init vs. foreground resume), **diff them**. An immediate-fetch call present in one and absent in the other is almost always an oversight rather than a deliberate asymmetry — the paths get written months apart.

**Related:** pair this with a cache-freshness threshold you can actually justify. A 24h expiry (`Municipal+Cache.swift`) sounds generous, but for episodic use (a parking app opened when you drive somewhere) *most* sessions land on the cold path, so the dead air becomes the common case rather than the edge case.

Incident: [[cyclops-first-run]] — `activate()` (`Mu1Base+Ext.swift:15–49`) had no kick while `resumePolling()` (`:78`) did; ≥16s of 🕐 on every cache-less launch.

## Combine: send to the subject you meant, especially in cold-start branches

**Rule:** When a type holds several `CurrentValueSubject`s of the **same element type** (`allFencesVbj` / `activeFencesVbj`, both `[MunicipalFence]`), the compiler cannot help you — sending to the wrong one type-checks perfectly. Re-read every `.send()` in a "first time through" branch with particular suspicion; those branches run once per launch and are the least exercised in day-to-day testing.

**The damage is worse than a missed update** when the wrong subject is an *input* to the computation:

```swift
if activeFencesVbj.value.count == 0 {                    // cold-start branch
    let enclosing = allFencesVbj.value.filter { ... }    // reads allFences
    allFencesVbj.send(enclosing)                         // ← overwrites its own input
}
```

This doesn't just fail to populate `activeFencesVbj` — it **destroys the source of truth**, narrowing the full list to a subset with no way back short of relaunch. Downstream set arithmetic (`allFences − activeFences`) then silently computes on a corrupted base.

**Smell test:** a `.send()` whose argument was derived from `.value` of that *same* subject is nearly always wrong. Either it's a genuine accumulate (rare — and should be written to make that obvious) or it's a typo'd destination.

**Guard:** prefer distinguishable names over near-homographs (`allFencesVbj` / `activeFencesVbj` differ by three characters mid-token), and consider `private(set)` or a dedicated mutator for subjects that should only ever be written from one place.

Incident: [[cyclops-first-run]] (Finding 2) — `Municipal+Ext.swift:135`.
