# 2026-09-15 — The toolchain moved under us, and the geofence system had never run

**Session goal:** merge `icon-replacement`, then build the empty state.
**Both done.** What was not expected is that neither could have shipped as they stood — the app did not launch at all under the new Xcode, and the feature the empty state depends on had never worked on iOS.

---

## The one-line version

> **Xcode upgraded from 26.6 to 27.0 between 09-14 and today, and it invalidated every build verification in this vault.** Two hard failures came out of that, one of which shipped a binary that could not launch. Separately, building the empty state exposed that the geofence system — fences, activation, all of it — has never run on iOS, for three independent reasons.

Everything is fixed, committed, and verified by running the app.

---

## Where the code is

**`main` is now at `fb28765`, seven commits ahead of `origin/main`. Nothing is pushed.** Working tree clean.

```
fb28765  Explain what the app shows outside its coverage area
88c5b4b  Make the geofence test correct and the fence data decodable
2c3dbb4  Stop applying .commands on iOS, which crashed the app at launch
391d784  Fix a FanceMapView01 init that Swift 6.4 rejects
a4a005b  Delete the dangling ConcaveHull package reference
98f1253  ← icon-replacement merged here (fast-forward)
5048976  ← where main was this morning
```

`icon-replacement` merged cleanly as a fast-forward. `backup/icon-replacement-pre-fold` is deleted, as planned. The branch ref `icon-replacement` still exists and can go too.

---

## Part 1 — The toolchain moved

The 2026-09-14 verification (the Archive, the `hootmac` command-line build) was done on **Xcode 26.6**. This machine now runs **Xcode 27.0 / Swift 6.4**. None of that verification carried over, and there was no signal that it had expired.

### 1a. A Swift 6.4 definite-initialization error — `391d784`

`FanceMapView01.swift:69`, untouched since March, stopped compiling:

```
error: variable 'self._allLots' used before being initialized
```

`self.inws = fPoints` is a **setter** call — `inws` already carries a default from its declaration — and a setter needs `self` fully initialized, which it is not while `allLots`, `coordinates` and `region` are still empty. Earlier compilers let it through; 6.4 does not.

Fixed by seeding every `@State` through its backing store (`_x = State(initialValue:)`), which is the idiomatic form and sidesteps ordering entirely. `_region` was already written that way.

**It broke every configuration** — iOS Debug, iOS Release, `hootmac`. So the branch that was "compile-verified two days ago" did not compile at all.

### 1b. The app could not launch — `2c3dbb4`

This is the serious one.

```
failed to demangle witness for associated type 'Body' in conformance
'hootowl.hootowlApp: App' - subject type qd__ does not conform to protocol Commands
```

`SIGABRT` in `AppGraph.init(app:)`, before a single pixel. Every launch.

The cause is the **shape** of a conditional, not its contents:

```swift
.commands{
#if os(macOS)
    DocCommands()
    OpenDataCommands()
#endif
}
```

On iOS that is a `.commands` call with an **empty `@CommandsBuilder` closure**. It compiles silently, and SwiftUI cannot resolve the `Commands` witness for the generic it produces. Moving the `#if` **outside** the modifier fixes it — iOS never applies it, which is what was meant, since `.commands` is a menu-bar concept.

**This is the `#if DEBUG` lesson from the Archive session, one turn of the screw worse.** Those three were compile errors; a compile error stops you. This one compiled and produced a binary that could not start.

> I verified it is not mine: stashed everything, built and ran the parent commit unchanged, watched it crash identically, restored. Worth the five minutes — the alternative was assuming.

---

## Part 2 — The geofence system had never run on iOS

Coverage detection needs one question answered: *is the user inside a supported city?* Answering it turned up three independent faults, each sufficient on its own. Commit `88c5b4b`, plus the `fences` resource in `fb28765`.

### 2a. The iOS app never shipped the fence data

`fences/` is a folder reference in the project. It is in **`hootmac`'s Resources build phase and no other**. The iPhone app has never carried `taipei.json` or `newTaipeiCity.json`.

`checkBundleAndDeserilize()` logs the failure and returns `[]`, so `allFencesVbj` stayed empty and nothing downstream complained.

This is [[swift-patterns#adding-a-file-to-the-project-is-not-the-same-as-the-project-using-it]] again, in its third variant — the file was in the project *and* in a build phase, just **not in every target's** build phase.

### 2b. The bundled data could not decode anyway

Both JSONs were written Nov 2025, before `carCap` was added to `IdWgs`. Synthesised `Decodable` throws `keyNotFound` for a missing key on a non-optional property, so both files failed even once they shipped.

Fixed on the **decoder** (`carCap` defaults to 0 when absent) rather than in the JSON, because the loader prefers the user's `Documents/fence/` copy when it is newer — installs holding an old file would keep failing however clean the bundle got.

### 2c. The point-in-polygon test read truncated integers

`IdWgs.longitude` and `.latitude` are declared **`Int`**. So `convexEnclosing` does its geometry on whole degrees, and Taipei's 13-point hull collapses onto two or three lattice points.

Measured against the real fence files:

| Point | correct | `convexEnclosing` |
|---|---|---|
| Taipei 101 | in Taipei | in Taipei ✓ |
| **Banqiao** | **New Taipei only** | **in Taipei ✗** |
| Cupertino | outside | outside ✓ |
| Tokyo | outside | outside ✓ |

It gets far-away points right by luck, which is why nothing caught it. Added `MunicipalFence.encloses(_:)` — ray casting over real `Double`s — and moved the `assessFences` call sites to it. `convexEnclosing` is **left in place**: the fence-driven activation policy it feeds is still an open design decision, and coverage should not wait on that.

### 2d. `assessFences` destroyed its own input

The one-word fix already written up in this vault, now applied — and it turns out to matter more than recorded:

```swift
if activeFencesVbj.value.count == 0 {
    let enclosing = allFencesVbj.value.filter { ... }
    allFencesVbj.send(enclosing)     // ← its own input
```

Outside coverage the subset is **empty**, so one GPS fix in California wiped every fence, and every later update threw `.noFences` — unrecoverable short of a relaunch that wiped them again. **The reviewer-in-California case was the worst case for this bug**, which is exactly the case nobody could test.

---

## Part 3 — The empty state

Jim's two design calls, both answered with the recommendation:
1. **Outside coverage** → honest + useful: name the cities, offer the city request.
2. **Feed down** → keep the numbers visible but visibly stale, with a banner.

### Shape

`Municipal.coverage` — **one state, read by every screen**, so the three surfaces cannot disagree. That is the mistake the watch list made before `defaultWatchList` became its single source.

```
locating · denied · outside · waiting · covered
```

It answers only *"is there anything to show, and if not, why"*. It says **nothing about age** — that stays `AvailFreshness`, driven by a clock in the view. Keeping them apart is what stops a third freshness vocabulary appearing.

A **stored `var`, not a computed property**: the inputs are `CurrentValueSubject`s, and reading `.value` from a computed property registers no dependency with `@Observable`, so no view would ever invalidate. Recomputed at the four points that can change the answer — location sink, auth sink, fence load, first availability pack. Logged at `.notice`, so a device sitting can read the transitions in Console.app.

### Surfaces

- **Map** (the first tab, so what a reviewer sees): a **compact** card, for `.denied` and `.outside` only. The transient states are excluded deliberately — a card that flashed on every cold launch while the first fix landed would train people to dismiss it. The map stays pannable behind it.
- **List / Cyclops**: full `ContentUnavailableView`, but only when they have nothing of their own to draw, and **never** when a search simply matched nothing. Cyclops shows the notice instead of "pin a car park", which is an instruction that user cannot follow.
- **Stale**: `StaleDataBanner` sits *over* content that stays visible, reusing `AvailFreshness` and the existing `freshnessTick` timer rather than adding a clock.

### One thing Jim should know

The ask line — *"tell us where you need it"* — renders **only when `support.email` is configured**. It is still a placeholder in the Gist, so today the screen degrades to:

> **We're not here yet**
> Right now we cover Taipei and New Taipei.

Honest and complete, but the city-request payoff — the reason this state was designed this way — is not there. That Gist item was already on [[jim-actions]] for onboarding; **it now gates this screen too.**

---

## Verified by running it, not by reading it

iPhone 17 Pro simulator, full round trip:

| Location | Log | Screen |
|---|---|---|
| Cupertino (37.323, −122.032) | `🗺️ coverage locating → outside` | card: "We're not here yet / Right now we cover Taipei and New Taipei." |
| Taipei 101 (25.034, 121.565) | `🗺️ coverage outside → covered` | card gone, live pins with real counts (181, 65, 41, 11, 7, 2) |

iOS Debug, iOS Release and `hootmac` Release all `** BUILD SUCCEEDED **`.

**Not visually checked:** the `.denied` state, and the two list screens. Same state, same view, but not seen.

### Notes on driving the simulator from the CLI

- `xcodebuild … ENABLE_DEBUG_DYLIB=NO` — without it the preview dylib adds its own launch failures outside Xcode.
- `xcrun simctl location <udid> set <lat>,<lon>` is what makes this testable at all.
- **The ATT prompt is a trap.** Once presented and unanswered it becomes a zombie SpringBoard alert that survives terminate, reinstall, and TCC edits, and this Xcode ships **no Simulator.app** to click it with. The way through is `simctl erase` — a *first* launch never prompts, since the gate is launch count ≥ 2.
- `simctl spawn … defaults write` does not reliably reach the app's real preferences; those live in the container plist, and `cfprefsd` caches them.

---

## Next

1. **Push.** `main` is seven commits ahead of `origin/main` and none of it is on the remote.
2. **Re-archive.** The 09-14 archive was built by the old toolchain and contains an app that cannot launch under the new one. That build number is spent; upload a new one.
3. **The Gist `support.email`** — now blocks two screens.
4. Device pass: everything on [[jim-actions]], plus the new coverage states.

## Loose ends

- `convexEnclosing` is still there and still wrong. Inert — nothing outside `Municipal` reads `activeFencesVbj` — and deliberately left for the fence-activation design decision.
- `ActDeActOnes` still has zero callers, so every proto still polls for every user. Unchanged, still confounds any battery measurement.
- `TpeParkDescInfo.json` is missing from the iOS bundle too (logged at every launch). Not investigated — possibly the same missing-target-membership shape as `fences`.
- `icon-replacement` branch ref can be deleted now it is merged.

## Related
[[CURRENT]] · [[bugs]] · [[decisions]] · [[jim-actions]] · [[swift-patterns]] · [[app-icon]] · [[operations]]

---

## Addendum — how complete is the Xcode 27 migration? (asked 2026-09-15, after the wrap)

Fair question, and the honest answer is *"I fixed what surfaced; here is what I then went and checked."*

### Clean

| Configuration | Result |
|---|---|
| `hootowl` iOS Debug (simulator) | ✅ |
| `hootowl` iOS Release (device) | ✅ |
| `hootmac` Debug | ✅ (not built before this check) |
| `hootmac` Release | ✅ |
| App launches and runs | ✅ iPhone 17 Pro simulator |

### Swept for the same shape as the launch crash

Scanned every result-builder modifier whose body opens with `#if` — `.commands`, `.toolbar`, `.contextMenu`, `.sheet`, `.overlay`, and the rest. **Five hits, all `.toolbar`, all with populated `#else` branches** (`MncplCyclopsScreen:150`, `NbsScreen:166`, `OptionsScreen:190`, `MncplAllScreen:125`, `SubscribeToolbarButton:80`). `.commands` was the only one-sided one. Nothing else can produce an empty builder.

### Broken, and NOT Xcode 27's doing

**`hoot_test_ui` does not build.** `cannot find 'AdBannerView' in scope`, `EnvironmentValues has no member 'adBannerHeight'`, and key-path inference failures — app sources being compiled without the iOS-only AdMob files.

**Proved pre-existing:** built it in a detached worktree at `a4a005b` — ConcaveHull already removed, none of the Xcode 27 fixes applied — and it fails with the identical 20 errors. Also worth knowing: at `5048976` it cannot even resolve packages, so this target has been unbuildable from the CLI since June for the ConcaveHull reason on top of its own.

It has **no scheme**, and appears in no verification anywhere in this vault. Treat it as an abandoned target: either wire its target membership properly or delete it, but it is not migration fallout and it does not block a release.

### Not verified — the honest gaps

- **A real Archive.** Compiling is not archiving; the Archive also runs Xcode's upload validation. Must happen before the next upload anyway, since the 09-14 archive is dead.
- **A real device.** Everything here is simulator.
- **The macOS app running.** `hootmac` compiles; it has not been launched.
- **Screens I never opened.** This is the one that matters. The `.commands` crash was invisible at compile time — only launching found it. I walked the **map tab only**. Onboarding, Cyclops, the list, subscription and Options have not been opened under Xcode 27. A device pass covers this, and one is already owed.

### Warning inventory (nothing blocking, two worth a look)

| Warning | Count | Note |
|---|---|---|
| `'+' was deprecated in iOS 26` on `Text` | 48 | use string interpolation |
| `extraneous whitespace between attribute name and '('` | 24 | **"this is an error in the Swift 6 language mode"** — `AVAudio.swift:23,27,32` |
| `use of protocol 'Mu1Proto' as a type must be written 'any Mu1Proto'` | ~12 | **"error in a future Swift language mode"** |
| `"mint" color asset conflicts with Color symbol "mint"` | 44 | rename the asset |
| `init(contentsOf:)` deprecated in iOS 18 | 9 | use `init(contentsOf:encoding:)` |
| `unstructured throwing task … is not used, which may accidentally ignore errors` | 8 | worth a real look — silent error swallowing |
| unused locals, `fontSize` written but never read | ~30 | noise |

The project builds at `-swift-version 5`, so the two "error in Swift 6 language mode" rows are **latent, not urgent** — they become blocking the day the language mode moves, which is a separate, deliberate migration.
