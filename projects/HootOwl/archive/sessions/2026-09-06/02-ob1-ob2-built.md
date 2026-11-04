# 2026-09-06 — ob1 + ob2 built; onboarding is now three real screens

Continues [[01-landingscreen-wired]]. With this, **all three onboarding screens exist** and the copy in [[onboarding]] is fully wired. Onboarding stops being the release blocker.

**Working tree only, not committed, not compile-verified.**

---

## The two new screens

| Tab | File | Struct | Copy |
|---|---|---|---|
| `ob1` | `UI/onboard/OnboardPinsScreen.swift` | `OnboardPinsScreen` | `onb_s2_*` |
| `ob2` | `UI/onboard/OnboardLocationScreen.swift` | `OnboardLocationScreen` | `onb_s3_*` |

**Not named `OnboardCyclops…`** deliberately. There are already three confusingly similar Cyclops screens in this codebase (`MncplCyclopsScreen`, `MncplCyclopsScreen0000`, `CyclopsScreen2`); a fourth would make the search results worse, not better. `OnboardPinsScreen` says what the screen *sells*, and its doc comment names Cyclops so the search still lands.

## Screen 3 has real behaviour, not just copy

Both of its buttons leave onboarding — they are the only exits besides the eject button.

- **Enable Location** → `Municipal.shared.requestLocationPermission()`, then exit.
- **Not now** → exit.

**The exit is passed down, not reimplemented.** `OnboardTab.tabScreen(tabId:)` became `tabScreen(onExit:)`, and `OnboardScreen` passes its own `onboardExit` — the same function the eject button calls, which already does `toggleShowingToolbar()` + `onboardExitRelay.send(lastScreen)` and is proven. Two exit paths that drift apart is exactly the class of bug worth not creating. The `tabId` parameter went with it; nothing read it.

**Denied is handled.** iOS shows the permission dialog once, ever. If the answer was already no, `requestWhenInUseAuthorization()` is a silent no-op and the button would look broken. So when the status is `.denied`/`.restricted` the primary button retargets to **Open Settings** (reusing the existing `Open Settings` catalogue key and the `openSettings()` pattern from `NbsScreen.swift:616`) and the icon flips to `location.slash.fill`.

Auth state is tracked with plain `@State` + `.onReceive(Municipal.shared.locAuthStateVbj)` rather than observation — one enum, and this view lives inside a paged `TabView`'s dynamic `ForEach`, which is precisely where `@Observable` invalidation has been unreliable on device ([[project-cyclops-observable-workaround]]).

## ⚠️ Finding: the system location prompt probably fires *before* screen 3

`Municipal+Loc.swift:31–33` — `handleAuthChange` calls `manager.requestWhenInUseAuthorization()` on `.notDetermined`, and that delegate fires as soon as the location manager is wired at launch. So on a fresh install the iOS dialog very likely appears **while the user is still on screen 1**, and by the time they reach screen 3 the decision is already made.

If so, screen 3's pre-priming does nothing — the "explain the benefit right before the system dialog" lift that motivated the screen is lost. **This is a design question for Jim, not a bug**, and it is not fixed here:

- Leave as-is — screen 3 becomes a status/repair screen (it already handles `.denied` correctly, so it is not useless).
- Or suppress the automatic request until onboarding has been seen, so the dialog lands on screen 3 where the copy sets it up. That is a change to `handleAuthChange`, which is load-bearing for every screen, so it wants its own session.

**Worth one glance during the device run:** does the location dialog appear on screen 1 or screen 3 on a fresh install?

## Shared backdrop

All three screens now paint one `OnboardBackground` (in `onboardTabEnum.swift`) instead of each carrying its own gradient literal, so paging reads as one surface moving under the content rather than three separate cards.

## The project file was wired from here — new capability worth knowing

`hootowl.xcodeproj` is **not** using Xcode 16 file-system-synchronized groups for the app target: only `hoot_test_ui` is a `PBXFileSystemSynchronizedRootGroup`, while the app group carries ~632 explicit `Sources` entries. So the [[feedback-new-swift-file-target-membership]] trap is still fully live — new files are invisible to the compiler until they are in `project.pbxproj`.

Rather than leaving Jim two manual Xcode ticks, both files were wired in directly. The shape, confirmed against `LandingScreen.swift`, is **exactly 6 entries per file**:

| Section | Count | Note |
|---|---|---|
| `PBXFileReference` | 1 | the file itself |
| `PBXBuildFile` | 2 | one per app target, both pointing at the one fileRef |
| `PBXGroup` children | 1 | the `onboard` group |
| `PBXSourcesBuildPhase` | 2 | one per app target |

Verified after writing: `plutil -lint` passes, each new file has 6 entries, and each appears exactly once in each of the two app Sources phases (161 and 159 files). Backup of the original at `scratchpad/pbxproj.bak`; `git checkout` reverts it.

## Now unreferenced (all three, deletion candidates)

`OnboardDebug.swift` (was ob1), `OnboardTab0.swift`, `UserGuide.swift`. Nothing is lost by ob1's replacement: `OnboardDebug` was just `IapReceiptView()` + `OptionScreen()`, and both are reachable elsewhere (`EntitledView.swift:68`, `AppScreen.swift:112`). **If Jim used ob1 as a quick debug surface, that shortcut is gone** — worth knowing before the build.

Deleting them means removing their `project.pbxproj` entries too. That is now demonstrably doable from here; left undone because deleting working files is Jim's call, not a tidy-up to take unasked.

## Still not done

- **中文 for all 17 new keys.**
- **`"support": { "email": "…" }` in the Gist**, or the screen-1 city-request link stays hidden in release.
- **`OnboardScreen` still uses the deprecated `NavigationView`** (`OnboardScreen.swift:26`) against the `CLAUDE.md` convention. That file was edited this session but only by one line; the swap deserves its own look since it changes layout.
- **Device run of the whole three-screen flow**, including the location-dialog timing question above.

## Related
- [[00-onboarding-strings-batch]] · [[01-landingscreen-wired]] · [[onboarding]] · [[unfinished]]
