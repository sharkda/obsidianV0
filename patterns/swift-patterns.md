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


---

## `ffl` levels decide whether you can see anything on a real device

`ffl` routes `.debug` and `.info` through `print()`, and only `.notice` / `.error` / `.fault` through `logger` (OSLog).

**`print()` output exists only while the Xcode debugger is attached.** It is not recorded on the device and cannot be read back later. So a log line at `.debug`/`.info` disappears the moment the debug session drops — the app keeps running perfectly, the log just goes silent.

That cost most of a day on 2026-09-03/04: device logs stopped mid-session while the simulator looked fine, and it read like an app hang. It was a detached debugger.

**Rules:**
- To observe anything on a real device — especially over minutes, or across background/foreground — log at **`.notice` or above** and read it in **Console.app** (device selected, filter category `ffl`). It persists and survives detachment.
- `.debug` is additionally gated by the per-file threshold in `fileDubugLevelDict` (`classDebugFilter`, `debugThreashold = 2`). A file set to `4` prints no `.debug` at all, whatever Xcode's console filter says. Check that before concluding a line "isn't firing".
- **Don't lower a file's threshold without checking what it logs per item.** `Mu1Base+Ext` carries per-item `.debug` lines over ~1,400–1,750 lots in the daily transform path; lowering it to `1` produced thousands of synchronous `print()` calls at launch and a ~5 minute freeze that looked like a real hang. See [[01-launch-hang]].

---

## A sizing constant can only be shared by views that share a layout

`MncplCyclopsScreen` sized its cards from a `switch` on item count, but the *layout* branched separately:

```swift
switch items.count {
case 3..<5: geoRh = 0.43     // calibrated for the 2-column grid
}
...
} else if items.count <= 3 {  // ...but 3 renders in a SINGLE COLUMN, which halves geoRh again
```

Three was the only count taking the grid's constant while rendering in the list, so it filled ~64% of the screen where 2 filled 85% and 4 filled 86%.

**The range notation is what hid it.** `3..<5` *reads* as "3 and 4 behave the same" — true of the constant, false of the layout. Spelling the cases out per count (`1...2`, `3`, `4`, …) makes the boundary visible at the point where it matters.

**Rule:** when a layout branches on the same value a sizing table switches on, make the case boundaries line up with the *layout* boundaries, not with convenient ranges. If a value sits on a layout boundary, give it its own case even when the number would otherwise be shared.

---

## A toolbar item is removed by not producing it, never by emptying it

**Rule:** to hide a toolbar item conditionally, the `if` must yield **no view**. Do not substitute an "invisible" placeholder.

```swift
// wrong — the item survives, and the toolbar draws its chrome behind the empty content
if subscribed {
    Color.clear.frame(width: 0, height: 0)
} else {
    Button { … } label: { Label(…) }
}

// right — body is an implicit @ViewBuilder, so an `if` with no `else` produces nothing
if !subscribed {
    Button { … } label: { Label(…) }
}
```

**Why it bites:** "render a placeholder so the layout doesn't jump" is sound advice in stacks and grids, where the content *is* what you see. A toolbar item is the opposite — **the container supplies the visible chrome** (on recent iOS, a circular backdrop) and the content only fills it. An empty item is therefore not invisible; it is a bare circle.

**The tell:** a control disappears "correctly" but leaves a plain circle or capsule exactly where it was.

Incident 2026-09-08: subscribing removed the Subscribe button from the map screen and left a white circle. See [[bugs#2026-09-0709-08-a-subscribed-user-was-left-a-white-circle-in-the-toolbar]].

---

## Removing a capability means deleting the strings that sold it

**Rule:** when a feature or permission is dropped, `grep` the **string catalogue and the UI copy**, not just the code that implemented it. Behaviour and the text advertising it live in different files and get removed at different times — usually meaning the text never gets removed at all.

Two instances surfaced within two days, both from the same June change (battery #9, which stopped escalating to Always on iOS):

- A map banner offering **"Enable Always for background nearby search"** with an Upgrade button. Because the escalation was gone, `.authorizedWhenInUse` became the permanent state for every iOS user — so the banner was shown to **everyone, forever**, its button was a no-op, and it promised background location the app cannot perform.
- A denied-location message reading *"requires location permission **(While Using or Always)**"*, naming a permission no longer requested.

**Why this class is nastier than a normal stale comment:** the app was actively telling users something contradicted by its own privacy copy. A privacy promise is broken by the copy just as effectively as by the implementation — and an audit of the *code* will pass while the app still lies on screen.

**Audit prompt:** after removing a permission, an entitlement, or a background mode, search the catalogue for the feature's vocabulary ("always", "background", "location", the feature's name) before considering the removal finished.

## "Has been fetched" is not a freshness signal

**Rule:** a `Bool` that means *"we got data at some point"* never expires, so it cannot express age. If a view uses one to decide how confident to look, it will look equally confident at ten seconds and at ten hours.

```swift
// wrong — never becomes false, so old data renders as new
var availFetched: Bool          // aItem != nil
private var opacity: Double { availFetched ? 0.9 : 0.45 }

// right — an injected clock and a timestamp, so age is derivable
var observed: Date?             // last CONFIRMED, not last changed
var now: Date                   // ticked by a timer
private var opacity: Double {
    switch AvailFreshness(observed: observed, now: now) { … }
}
```

**Why it hides:** the boolean is *correct* — data really was fetched. Nothing is wrong until you ask "how long ago", which the type cannot answer. On live-data screens that question is the whole product.

Incidents: `CustomButton` map pins (2026-09-10) and, in a different form, the Cyclops cells that spent a week looking plausible while frozen. Both fixed by reusing one `AvailFreshness` model driven by `Municipal.lastConfirmed`.

**Pair with:** the "last confirmed vs last changed" distinction — a feed that keeps re-confirming an unchanged number is fresh; a frozen feed is not.

## A localisation bug can live entirely outside the string catalogue

**Rule:** when a screen renders in the wrong language, check what is drawing the text before auditing your own strings. Content supplied by a framework is localised by *its* rules, not the device's.

`SubscriptionStoreView` renders product names, descriptions and prices from **StoreKit**, and under a StoreKit test configuration those come from that file's `settings._locale` / `_storefront` — **overriding the device language entirely**. A `zh-Hant-TW` simulator with a fully translated catalogue still showed an English paywall, because the test config was pinned to `en_US` / `USA`.

**Diagnostic order that worked**, after two wrong guesses:
1. `xcrun simctl spawn <udid> defaults read -g AppleLanguages` — is the device even in the language you think?
2. Check for a per-app override in the app container's preferences plist.
3. Dump the **installed** bundle's compiled table: `plutil -convert json -o - <app>/zh-Hant.lproj/Localizable.strings`. If the value is there, your catalogue is fine.
4. Launch and screenshot it. A screen mixing translated and untranslated text proves the machinery works and narrows the fault to whatever supplied the untranslated part.

`export DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer` makes `xcodebuild` and `simctl` usable even when `xcode-select` points at CommandLineTools.

## Adding a file to the project is not the same as the project using it
**Rule:** For anything the build selects **by name** — app icons (`ASSETCATALOG_COMPILER_APPICON_NAME`), launch screens, entitlements, Info.plist — adding the file to the project and to a target's build phase does **not** make the build use it. A second, separate step points the build setting at it.

**Why it matters — the failure is silent.** There is no warning, no error, no red in the navigator. The file is present, correctly targeted, visible, and simply ignored while the old one keeps building. You discover it by looking at the running app, not by reading the project.

**Incident (2026-09-12):** `FindParkingTw.icon` was added to `hootowl/resources/` and to both targets' Resources phase, while all four build configurations still read `ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon`. The legacy appiconset kept shipping. Deleting the old icons at that point would have produced an app with no icon.

**Diagnosis:** `grep -n "ASSETCATALOG_COMPILER_APPICON_NAME" *.xcodeproj/project.pbxproj` — the value is the truth, not the navigator.

**Family resemblance:** this is [[swift-patterns#new-swift-file-must-be-added-to-target-membership]] one level up. That one is *on disk but not in the build*; this one is *in the build but not selected*. Both fail without saying so. Detail: [[app-icon]].

## `#if DEBUG` / `#else` means half your code is never type-checked
**Rule:** Xcode only compiles the **active** branch of a conditional-compilation block. The `#else` half of every `#if DEBUG` is **real code that your everyday build never type-checks** — it is first compiled when you build Release or Archive, which for a new app is the day you try to ship.

**Why it matters:** a project can build cleanly for months while carrying Release-only compile errors, and there is no warning of any kind. Three surfaced in one Archive on 2026-09-11/12 ([[bugs#2026-09-1112--three-release-only-breakages-that-no-debug-build-ever-compiled]]).

**Two failure modes, and they need different fixes:**
1. **Symbol not declared in the inactive half.** A `#if DEBUG`-only property referenced by unguarded code. → **Guard the declaration in both halves, not each use site.** One place to get right instead of every current and future reference. Guarding use sites is how the `debugForceAd` fix missed a second reference one line below the first.
2. **Logic that is wrong rather than absent.** The Release half compiles but behaves incorrectly. Worse than a compile error, because nothing stops it shipping — `debugForceAd = true` in Release would have forced ads on for **paying subscribers**.

**When you write a `#else` branch, remember the value is the *shipping* one.** Debug is the branch you can test; Release is the branch users get.

**Diagnosis:** you cannot grep your way to confidence — **build Release**. `xcodebuild -configuration Release` or Product → Archive. For this project only Xcode can do it (`ConcaveHull` blocks the CLI — [[operations#3-building-and-testing]]).

**Habit worth keeping:** archive **early**, long before the app is "finished". An Archive is the only thing that type-checks these branches, and it also runs Xcode's upload validation (icons, entitlements, privacy manifest). Uploading is not submitting, so a throwaway archive costs nothing. See [[app-icon]] and [[operations#2d-archiving-and-distributing--2026-09-11]].



---

## An empty result-builder closure is a runtime crash, not a no-op

**Rule:** when a modifier takes a result builder, put the `#if` **around the modifier**, never around the whole of its contents. A builder closure that compiles to nothing is not "nothing" — it is a generic the runtime may be unable to resolve.

```swift
// wrong — on iOS this is `.commands { }`, an EMPTY @CommandsBuilder closure
.commands {
#if os(macOS)
    DocCommands()
    OpenDataCommands()
#endif
}

// right — iOS never applies the modifier at all
#if os(macOS)
.commands {
    DocCommands()
    OpenDataCommands()
}
#endif
```

**What it costs:** `SIGABRT` at launch, before anything draws.

```
failed to demangle witness for associated type 'Body' in conformance
'MyApp: App' — subject type qd__ does not conform to protocol Commands
```

**Why it is worse than the `#if DEBUG` family:** those produce *compile* errors, and a compile error stops you. This compiles clean, with no warning, and ships a binary that cannot start. It also survived a full Archive on the older toolchain, so "it archived" is not evidence.

**The tell:** a crash in `AppGraph.init(app:)` / `swift_getAssociatedTypeWitnessSlowImpl` naming an associated type you never wrote — the type is the builder's output, and the empty closure is why it has no name.

**Diagnosis:** the generic placeholder (`qd__`) tells you it is a builder result, not your code. Grep for result-builder modifiers whose body is entirely inside a `#if`: `.commands`, `.toolbar`, `.contextMenu`, `@SceneBuilder` bodies.

Incident 2026-09-15: [[bugs#2026-09-15-the-app-could-not-launch-under-xcode-27-an-empty-commands-closure-fixed]].

---

## A toolchain upgrade expires every build verification you have written down

**Rule:** "compile-verified", "archived successfully", "builds clean" are claims about a **compiler version**, not about the source. Record the Xcode version alongside the claim, and re-verify after any upgrade before trusting a note.

On 2026-09-15 an Xcode 26.6 → 27.0 bump alone produced:
- a **definite-initialization error** in a file untouched since March (`@State` assigned through its wrapped value before all stored properties were initialized);
- a **launch crash** from an empty result-builder closure that had shipped in a successful Archive two days earlier.

Neither was caused by an edit. Both broke every configuration. The vault said the branch was verified; the verification had silently expired.

**Corollary for this project:** an Archive is the only thing that type-checks the `#else` half of a conditional — and it only proves it for the toolchain that built it.

**Habit:** when writing "verified", write *what* verified it: `Xcode 27.0 / Swift 6.4, iOS Debug + Release + hootmac Release`. A bare "builds clean" ages into a false statement without changing a character.

---

## Target membership is per target, and "in a build phase" is not "in every build phase"

**Rule:** a resource or source file can be correctly added to the project, correctly added to *a* build phase, and still be missing from the app you ship — because it is in the **other** target's phase.

The `fences/` folder reference sat in `hootmac`'s Resources phase and no other. The iPhone app had never carried the geofence data, and the loader's failure path logged and returned `[]`, so nothing said so.

**Diagnosis** — count the entries, don't trust the navigator. A file in both targets has **two** `PBXBuildFile` entries and **two** phase entries:

```sh
grep -c "MyFile.swift" *.xcodeproj/project.pbxproj   # expect 6 for a dual-target source file
```

For a resource, check *which* phase by mapping the phase UID back to its `PBXNativeTarget`.

**Family:** this is the third variant of the same failure.
- [[swift-patterns#new-swift-file-must-be-added-to-target-membership]] — on disk, not in the build.
- [[swift-patterns#adding-a-file-to-the-project-is-not-the-same-as-the-project-using-it]] — in the build, not selected.
- This one — in the build, for the wrong target.

All three are silent. All three are found by running the thing, not by reading the project.

Incident 2026-09-15: [[bugs#2026-09-15-the-geofence-system-has-never-run-on-ios-fixed]].

---

## A struct's `Int` accessor will quietly destroy your geometry

**Rule:** before using a coordinate accessor in arithmetic, check its **type**. A `var longitude: Int { Int(wgs84.longi) }` looks like a convenience and is a truncation.

`MunicipalFence.convexEnclosing` did point-in-polygon on `IdWgs.longitude` / `.latitude`, both `Int`. Across Taiwan every vertex became lat 24–25, lon 121–122, so a 13-point hull collapsed onto three lattice points and the cross products were arithmetic noise. It placed **Banqiao inside Taipei** — while still rejecting Tokyo and California, which is exactly why it read as working.

**The tell:** a geometric predicate that is right for far-away inputs and wrong for near ones. Coarse-grained truth is what truncation leaves behind.

**Check it against real data, not intuition.** Reimplementing both versions in a throwaway script over the actual fence JSON, with a table of known points, settled it in two minutes:

| Point | correct | truncated |
|---|---|---|
| Taipei 101 | in Taipei | in Taipei ✓ |
| Banqiao | New Taipei only | **in Taipei ✗** |
| Cupertino | outside | outside ✓ |

**Prefer ray casting** over a convex half-plane test unless the polygon is guaranteed convex forever — it costs the same and keeps working when a hull is replaced by a real boundary.

Incident 2026-09-15: [[bugs#2026-09-15-the-geofence-system-has-never-run-on-ios-fixed]].

## `SystemSoundID` needs an explicit `import AVFoundation` under Xcode 27

The project sets `SWIFT_UPCOMING_FEATURE_MEMBER_IMPORT_VISIBILITY = YES`, so a type no longer
arrives transitively through another module's import. `Earcon.ps(SystemSoundID(1109))` — the
simulator-only earcon that pairs with every `ffl(.error)` — compiles only in files that import
`AVFoundation` (or `AudioToolbox`) themselves.

**Symptom:** `error: cannot find 'SystemSoundID' in scope`, in a file that changed nothing about
sound. Expect it on any *new* file adopting the earcon idiom.

**Seen:** 2026-09-16, adding the paginated NTPC fetch to `NewTaipeiCityObs.swift` (`e45051c`).

## Edit `.xcstrings` textually, never by re-serialising it

Adding one key by `json.load` → insert → `json.dumps(indent=2)` rewrites **the entire catalogue**: Xcode writes `" : "` with spaces around the colon, and its key order is not Python's `sorted()`. The result was a **652-line diff for one string** — in a file where the diff is how you see what a session changed about user-facing copy.

Insert the block as **text**, at the right alphabetical position, matching the surrounding formatting: **18 lines, all additions.**

**Seen:** 2026-09-19, adding `sub_terms_of_use` (`327bf08`).

## User-facing search wants `localizedStandardContains`, not `contains`

`String.contains` is an exact, case-sensitive, ASCII-literal match. In a search field that is a trap whenever the data carries capitalised identifiers: HootOwl's lot ids are `TPE0155`, so `tpe0155` matched **0 of 1,773** rows and the list came back empty.

`localizedStandardContains` is the Finder-style comparison — case- and diacritic-insensitive, locale-aware — and is what a person typing into a search box expects.

**Measure the fold you are claiming.** Standard comparison is documented as width-insensitive too, but measured here it did **not** match full-width `ＴＰＥ` against `TPE`. The comment in the code says what was measured; do not write down what the documentation implies.

**Seen:** 2026-09-19 (`9285a47`), fixing a bug Jim reported in June.
