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
