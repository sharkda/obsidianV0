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
