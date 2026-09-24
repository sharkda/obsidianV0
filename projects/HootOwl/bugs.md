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

## 2026-09-24 — `Municipal` mutated off the main thread; the app aborted on the second city's feed (fixed)
**Symptom:** reliable abort a few seconds after launch, once the **second** city's daily data arrived.
```
*** 'NSInvalidArgumentException': -[__NSTaggedDate count]: unrecognized selector
    Municipal.actDaily(p0:)   Municipal.swift:134
```
That line is one statement: `actParkInfos[p0.mncplt] = p0`.
**The tell that it was not a type error:** the stack ran `Dictionary._Variant.setValue` → `___forwarding___` → `doesNotRecognizeSelector`, and the selector landed on **`__NSTaggedDate` on one run and `__NSCFNumber` on the next**. **A different random type each time is memory corruption, not a wrong type** — a genuine type mistake fails identically every time.
**Root cause:** `dailyVbj` is sent from `dailyRetrieveFlow` inside an async `Task` with **no hop to main** (`Mu1Base.swift:290`), and `Municipal.actWire`'s sink mutated `Municipal` straight from that thread. `Municipal` is `@Observable` and `actParkInfos` is a plain Swift `Dictionary` with no synchronisation, so two cities landing close together raced into the same storage.
**Why it survived this long:** `minuteFlow()` was given exactly this hop on **2026-09-01**, after the same class of failure, with a comment explaining why. **The fix went to that one flow.** `dailyVbj` kept the bug, and `actWire` — where the mutation actually happens — was never guarded at all. It only became fatal now because both cities' daily feeds reliably land together on a clean install.
**Fix:** all three `actWire` sinks `.receive(on: DispatchQueue.main)`. **Guarding the boundary rather than the caller** — a future proto that publishes from its own thread cannot reintroduce it. Commit `80a792a`.
**Proved pre-existing before touching it:** stashed the working tree, rebuilt at `ea9ce8f` and watched it abort identically. Worth the two minutes — the crash first appeared right after an unrelated UI change, and the obvious suspect was wrong.
**Verified:** clean install, both feeds land, `actParkInfos` holds taipei and newTaipeiCity together, zero uncaught exceptions.
**This was E-10.** [[unfinished]] filed it on 2026-09-02 as *"mark `Municipal` `@MainActor` before the next municipality is added"* — **structural, not present.** It was present; it just needed both feeds to arrive at once. The full `@MainActor` change is still worth doing.
**Files:** `hootowl/Municipalities/framework/Municipal+Ext.swift:80-100`, `Municipal.swift:134`, `Mu1Base.swift:290`.

## 2026-09-22 — The map dropped the user's destination on every tab return (fixed)
**Symptom:** jump to Taipei, switch to the watch list or the All tab, switch back — **the map is in Cupertino again**, while the bar still says *"Showing 台北市 — you're not there"*. The destination itself survived; only the camera forgot.
**First fix, which did not work:** restoring the camera in `onAppear` (`ca3d85e`). It ran, and was overruled a beat later. That is what made it look like the restore was broken.
**Root cause:** `cameraPosition` is `@State`, so a tab switch destroys it — but the reason the *restore* lost is separate and more interesting. **Four places snapped the camera straight to `userLoc2dVbj`** (the iOS auth sink, the macOS auth sink, the location sink, and an explicit "snap if already known"), and **all four ran on every tab return**, because:

> `wire0` re-subscribes each time the view appears, and **`locAuthStateVbj` and `userLoc2dVbj` are `CurrentValueSubject`s — subscribing replays the current value.** So the sinks fire instantly with "authorized" and "here is your fix", which is the device's location.

**The general lesson:** a `CurrentValueSubject` sink is not only a change notification — it is **an immediate callback with whatever is already stored**. In an `onAppear`, inside a `TabView` that recreates its children, that becomes "do this again, now" on every navigation. Pattern: [[swift-patterns#re-subscribing-to-a-currentvaluesubject-on-onappear-replays-the-old-value-as-if-it-were-new]].
**Fix:** all four route through one `snapCameraToDevice(_:animated:)` that stands down when a destination is set. **One guard rather than four patches** — patching each would have left the next "snap to me" line free to reintroduce it. Commit `7f4113c`.
**Verified** with a destination set and the device in Cupertino:
```
📍 returning to 台北市 — camera was reset by the tab switch
📍 ignoring device-location snap — showing 台北市      ×4
```
**Also removed a log that lied:** the location sink announced *"centering on <device>"* **before** the guard refused the move, so the console claimed the camera had gone somewhere it had not.
**Status:** fixed, merged to `main` in `42ed13b`.
**Files:** `hootowl/Municipalities/Nbs/NbsScreen.swift` — `snapCameraToDevice`, `wire0`.

## 2026-09-19 — Search only matched capitals, so `tpe0155` found nothing (fixed)
**Symptom:** typing a lot id in lower case returned an empty list. `TPE0155` worked; `tpe0155` did not. Reported by Jim in June ([[Jim's backlog]] item 1) and lived as a usability nicety until the App Store review notes started telling reviewers to search for `TPE`.
**Root cause:** `MncplAllScreen.filtered(avMap:)` used a plain `String.contains`, which is case-sensitive. The haystack is `"\(id) \(name) \(address) \(area)"` and **every Taipei id is capitalised** (`TPE0001`…), so any lower-case English query matched zero rows out of 1,773.
**Why it became urgent:** the 09-18 review notes instruct a reviewer to open the All tab and type `TPE`. **A reviewer who types it in lower case sees an empty list and concludes the app does not work** — the cheapest possible rejection, from a one-line bug.
**Fix:** `localizedStandardContains`. Commit `9285a47`.
**Measured**, not reasoned about — the new rule run over the live 1,773-lot Taipei feed:

| query | before | after |
|---|---|---|
| `TPE` | 1773 | 1773 |
| `tpe` | **0** | **1773** |
| `Tpe` | **0** | **1773** |
| `tpe0155` | **0** | **1** |
| 信義 | 158 | 158 |
| 大安 | 246 | 246 |

The Chinese terms are unchanged, so nothing shifts for the primary market.
**What the same measurement disproved:** standard comparison **did not fold full-width** here — `ＴＰＥ` from a Chinese IME still matches nothing, despite the documentation implying width-insensitivity. Left as-is deliberately (nobody types a lot id in full-width), and the code comment records the measurement rather than the assumption.
**Scope, traced not assumed:** two other files use the same `contains(searchText)` pattern. `AllTpeParkingScreen` is unreachable — `.allTpe` appears in no array `AppScreen.sorted()` returns — and `zzParkInfoScreen` has no callers. Only the All tab ships.
**Status:** fixed, pushed.
**Files:** `hootowl/UI/mncplAll/MncplAllScreen.swift:77`.

## 2026-09-19 — A shipping screen showed English on a Chinese device, because a note said it was dead (fixed)
**Symptom:** `SubscriptionStoreScreen`'s policy link rendered **"Privacy Policy"** in English regardless of device language.
**Root cause, two layers.** The literal itself:
```swift
Link("Privacy Policy", destination: URL(string: "…")!)
```
is the same bug fixed in `SubscriptionScreen` on 2026-09-09 — but *that* fix did not reach this file, because [[unfinished]] had recorded on 09-08 that **this screen was unreferenced**, so nobody looked at it again.
**The note was wrong.** The screen is reachable: `AppScreen.swift:89 → MncplCyclopsScreen → toolbar0 → ToolbarPrinciple() → SubButtons() → NavigationLink(destination: SubscriptionStoreScreen())`. The 09-08 claim was presumably made from `AppScreen.swift:112`, where a *direct* call is commented out; the toolbar route was missed.
**Why it hid for eleven days:** a wrong "this is dead code" note is worse than no note — it removes a file from every future sweep. The 09-09 localisation pass would have caught this had the file been in scope.
**Fix:** uses `sub_privacy_policy`, the same key as its sibling. Commit `327bf08`.
**Status:** fixed. **Related risk still open:** the same note calls `EntitledView` unreferenced, and **E-16** proposes deleting three more files on notes of the same vintage — re-verify by tracing callers first (**E-29**).
**Files:** `hootowl/iAp/subUi/SubscriptionStoreView.swift`, `hootowl/iAp/subUi/SubButtons.swift:23`, `hootowl/UI/ToolbarPrinciple.swift:12`.

## 2026-09-16 — New Taipei City availability is dead: the bulk CSV is WAF-rejected (open)
**Symptom:** every minutely poll for `newTaipeiCity` aborts. The app logs
`📛 newTaipeiCity <html><head><title>Request Rejected</title></head>… < 512bytes, will abort`.
Availability for NTPC never refreshes — one of the two covered cities silently serves stale numbers, and the pins fade (`5048976`) with nothing telling the user why.
**Root cause:** `data.ntpc.gov.tw` now returns an **F5 WAF rejection page with HTTP 200** for
`/api/datasets/e09b35a5-a738-48cc-b0f5-570b67ad9c78/csv/file` — the availability dataset's bulk download.
Verified from curl, outside the app, so it is not the app's request shaping:
- persistent across retries, and unaffected by User-Agent, `Referer`, a real session cookie, or HTTP/1.1.
- **path-specific, not IP- or account-wide**: the *daily* description dataset `b1464ef0…/csv/file` still returns 375 KB from the same machine, same second.
- **the same dataset's other representations still work**: `…/json?page=0&size=1000` and `…/csv?page=0&size=1000` both return real rows.
**When it broke:** within hours. The on-disk cache was written at **12:04 today with a full ∑1411**, and the endpoint was already rejecting by ~13:55.
**The catch in the working endpoints:** they cap at **1000 rows per page** (`size=2000` and `size=5000` both return 1000), and NTPC currently has **1411 rows / 1400 unique ids**. So a fix must paginate — page 0 gives 1000, page 1 gives 411, page 2 is empty. (The 11-row gap is the known duplicate-parkId warning, and it reconciles exactly.)
**Fix:** `Mu1Base` gained an overridable `fetchMinutely()` (default: the old single `fetch(url:urlMinutely)`, so no other city changes), and `NewTaipeiCityObs` overrides it to walk `…/csv?page=N&size=1000` until a short page, emitting page 0's header followed by every data row. `oParseMinute` is untouched and unaware — the paginated CSV is byte-shaped like the file download (`"ID","AVAILABLECAR"`). Paging is unconditional rather than probing `/csv/file` first: it is correct whether or not NTPC restores the download, and a probe would cost every user a rejected request forever.
Two details worth keeping:
- **Page 0 with no rows is passed through untouched**, not thrown. Upstream's `<512 bytes` guard then logs the body verbatim — which is the only reason the WAF page was ever readable.
- **The seam is a race** in principle: separate requests against a live dataset can duplicate or skip one lot between pages. Benign — the feed already ships ~11 duplicate parkIds of its own and consumers dedupe, and a lot missing from one 6-minute cycle keeps its previous number. Checked empirically: the seam (`110092` → `110094`, and `110093` does not exist) is stable across refetches.
**Verified:** built and run on the iPhone 18 Pro / iOS 27.0 simulator from Taipei 101 —
`📄 newTaipeiCity minutely: 2 page(s), 1410 rows` then `🐎 minutelyAvailable ["newTaipeiCity ⏳16 21:52 ∑1410", …]`, live and current rather than the 14:42 cache. No `📛`, no `❌`, no abort. All four builds pass (iOS Debug/Release, hootmac Debug/Release).
**Status:** fixed, committed as **`e45051c`** — *Page through New Taipei City's availability feed*. Re-verified after the project-file revert below: on the iPhone 17 Pro / iOS 26.5 simulator the stale 15:19 cache was replaced by a live `∑1410` at 22:33.
**Files:** `hootowl/Municipalities/Zone2/NewTaipeiCityObs.swift:21-105`, `hootowl/Municipalities/framework/Mu1Base.swift:385-397`, `hootowl/Municipalities/framework/Mu1Base+Ext.swift:124,230`.
**One extra import:** `AVFoundation` in `NewTaipeiCityObs.swift`, for `SystemSoundID`. Xcode 27 turns on `SWIFT_UPCOMING_FEATURE_MEMBER_IMPORT_VISIBILITY`, so it no longer arrives transitively — expect this error shape on any new file using the simulator earcons. See [[swift-patterns]].

## 2026-09-16 — Xcode rewrote the project file mid-session, including the deployment target (open)
**Symptom:** an `xcodebuild` command that had **succeeded 30 minutes earlier** started failing with
`iPhone 17 Pro's iOS Simulator 26.5 doesn't match hootowl.app's iOS Simulator 26.6 deployment target`.
Nothing in the checkout had been edited but three Swift files.
**Root cause:** `hootowl.xcodeproj/project.pbxproj` and `hootowl/Info.plist` were modified on disk at 14:06 and 14:03 while Xcode.app was running. The tree was **clean at session start**, so these arrived during the session. Three separate changes:
1. **`IPHONEOS_DEPLOYMENT_TARGET` 26.0 → 26.6**, on both the Debug and Release configs of the app target. This is the one that matters — it is a **product decision, not a build detail**: it drops every device on iOS 26.0–26.5.
2. **Info.plist keys migrated into build settings.** `ITSAppUsesNonExemptEncryption`, `NSLocationWhenInUseUsageDescription` and `NSUserTrackingUsageDescription` were **deleted from Info.plist** and re-added as `INFOPLIST_KEY_*` in the pbxproj. Functionally equivalent at build time — but it silently discards the comment block commit `5411f69` added explaining *why* export compliance is `false`, and the note that the usage strings are localised in `InfoPlist.xcstrings`.
3. Harmless reordering of `PBXBuildFile` / `PBXFileReference` entries.
**Fix:** Jim's call was to keep 26.0. Xcode was quit first so it could not re-apply, then `git checkout --` restored both files. Deployment target is back to **26.0** on both configs, the three Info.plist keys and their comments are back, and all five builds pass — including the iOS 26.5 simulator destination that had started failing, which confirms the deployment target was the whole cause.
**Status:** resolved. Worth knowing: plain `xcodebuild` does **not** touch the project file — the tree stayed clean across five builds afterwards. It was Xcode.app, running with the project open.
**Watch for:** this is the same family as the Xcode 26.6 → 27.0 surprise of 09-15 — the toolchain changing the project underneath a verification. `git status` before trusting any build result.

## 2026-09-15 — The app could not launch under Xcode 27: an empty `.commands` closure (fixed)
**Symptom:** `SIGABRT` on every launch, before anything drew:
```
failed to demangle witness for associated type 'Body' in conformance
'hootowl.hootowlApp: App' - subject type qd__ does not conform to protocol Commands
```
Crash frame: `swift_getAssociatedTypeWitnessSlowImpl` ← `AppGraph.init<A>(app:)`.
**Root cause:** the **shape** of a conditional, not its contents.
```swift
.commands{
#if os(macOS)
    DocCommands()
    OpenDataCommands()
#endif
}
```
On iOS this is a `.commands` call with an **empty `@CommandsBuilder` closure**. It compiles with no warning; SwiftUI then cannot resolve the `Commands` witness for the generic it produced. Xcode 26 tolerated it, Xcode 27 does not.
**Fix:** move the `#if` **outside** the modifier so iOS never applies `.commands` at all — which is what was intended; it is a menu-bar concept with nothing to do on iPhone. Commit `2c3dbb4`.
**Proved not to be a regression:** stashed all work, built and ran the parent commit unchanged, watched it crash identically, restored.
**Why it matters more than the Archive's three:** those were *compile* errors, and a compile error stops you. This compiled and produced a shippable binary that could not start. Same family — a branch the everyday build never exercises — one degree worse. Pattern: [[swift-patterns#an-empty-result-builder-closure-is-a-runtime-crash-not-a-no-op]].
**Status:** fixed, verified running on the iPhone 17 Pro simulator.
**Files:** `hootowl/App/hootowlApp.swift:67-88`.

## 2026-09-15 — The geofence system has never run on iOS (fixed)
**Symptom:** none visible. `allFencesVbj` was always empty, so `assessFences` always threw `.noFences`, `activeFencesVbj` stayed `[]`, and nothing downstream complained. Discovered only because the coverage feature needed a trustworthy "am I inside a supported city" answer.
**Three independent root causes, each sufficient on its own:**
1. **The data was never in the iOS app.** `fences/` is a folder reference in **`hootmac`'s Resources build phase and no other**. The iPhone app has never carried `taipei.json` / `newTaipeiCity.json`. A third variant of [[swift-patterns#adding-a-file-to-the-project-is-not-the-same-as-the-project-using-it]] — in the project *and* in a build phase, just not in **every target's**.
2. **The data could not decode.** Both JSONs were written Nov 2025, before `carCap` was added to `IdWgs`. Synthesised `Decodable` throws `keyNotFound` for a missing key on a non-optional property.
3. **The polygon test read truncated integers.** `IdWgs.longitude` / `.latitude` are declared **`Int`**, so `convexEnclosing` does geometry on whole degrees and Taipei's 13-point hull collapses onto two or three lattice points. Measured against the real files: it places **Banqiao inside Taipei**. It gets far-away points right by luck, which is why nothing caught it.
**Fixes:** `fences` added to the iOS target's Resources phase; `IdWgs` decodes `carCap` as 0 when absent (on the **decoder**, not in the JSON — the loader prefers the user's `Documents/fence/` copy when newer, so installs holding an old file would keep failing); new `MunicipalFence.encloses(_:)` doing ray casting over real `Double`s, with the `assessFences` call sites moved to it. Commits `88c5b4b`, `fb28765`.
**Deliberately not fixed:** `convexEnclosing` itself. It is inert — nothing outside `Municipal` reads `activeFencesVbj` — and the fence-driven activation policy it feeds is still an open design decision ([[decisions#2026-08-07-fence-driven-zone-activation-is-an-open-design-decision-not-a-patch]]).
**Status:** fixed. Verified on the simulator: taipei 13 points, newTaipeiCity 10 points, both deserialize, enclosing answers correctly for Cupertino and Taipei 101.
**Files:** `hootowl/Municipalities/framework/Mu1Proto.swift`, `Municipal+Ext.swift`, `hootowl.xcodeproj/project.pbxproj`.

## 2026-09-15 — `assessFences` overwrote its own input, and outside coverage that wiped every fence (fixed)
**Symptom:** after one GPS fix outside any supported city, every later location update threw `FenceError.noFences`, unrecoverable short of a relaunch that did the same thing again.
**Root cause:** the long-recorded one-word bug, now applied — but worse than written up. The cold-start branch computed the enclosing subset of `allFencesVbj` and sent that subset **back to `allFencesVbj`**, narrowing the master list. **Outside coverage the subset is empty**, so the list was not narrowed but erased.
**Why this was never seen:** the worst case is precisely the case nobody in Taipei can reproduce — and it is exactly the App Review case.
**Fix:** `activeFencesVbj.send(enclosing)`, the destination always intended. Commit `88c5b4b`.
**Status:** fixed. Pattern already recorded: [[swift-patterns#combine-send-to-the-subject-you-meant-especially-in-cold-start-branches]].
**Files:** `hootowl/Municipalities/framework/Municipal+Ext.swift:141-150`.

## 2026-09-15 — Xcode 27 / Swift 6.4 broke the build on `main` (fixed)
**Symptom:** every configuration failed to compile — iOS Debug (simulator), iOS Release (device) and `hootmac` Release — on a single error:
```
FanceMapView01.swift:69:9: error: variable 'self._allLots' used before being initialized
```
**Root cause:** not a regression. `FanceMapView01.swift` has been untouched since March, and the code was accepted by every compiler until now. **Xcode was upgraded from 26.6 to 27.0 (Swift 6.4) between 2026-09-14 and 2026-09-15**, and 6.4 enforces definite initialization through property wrappers where earlier versions did not.

The init assigned through the wrapped value:
```swift
self.inws = fPoints        // ← a SETTER call: `inws` already has a default
self.allLots = allLot      //   from its declaration, so this is mutation
```
A setter requires `self` to be fully initialized, and at that line `allLots`, `coordinates` and `region` still were not. The diagnostic names `_allLots` — the backing store — which is what makes it read as nonsense at first glance: the error points at line 69 and blames a variable assigned on line 70.
**Fix:** seed every `@State` through its backing store (`_x = State(initialValue:)`) instead of assigning the wrapped value. Sidesteps the ordering question entirely and is the idiomatic form; `_region` was already written that way. Behaviour identical. Commit `391d784`.
**Status:** fixed. All three configurations verified `** BUILD SUCCEEDED **` on Xcode 27.0 / Swift 6.4.
**Why it matters beyond this one file:** the 2026-09-14 verification — the archive, and the `hootmac` command-line build — was done on **Xcode 26.6**. Nothing about it carried over. A toolchain upgrade invalidates a build verification as completely as a source change does, and says nothing about it at the time.
**Files:** `hootowl/Municipalities/UI/FanceMapView01.swift:64-79`.

## 2026-09-05 — Fresh install: All screen showed 3 pinned lots, Cyclops showed none (fixed)
**Symptom:** On a clean install, `MncplAllScreen` displayed three lots as pinned while the Cyclops tab showed the empty `CyclopsInstructorView`. The two screens disagreed about the same watch list.
**Root cause:** the first-run seed lived as a **literal in two view files** (`MncplAllScreen.swift:47`, `AllTpeParkingScreen.swift:28`) while `Municipal.watchList` — which is what Cyclops actually renders — defaulted to `[]` and was only assigned on a *successful* decode (`loadWatchListFromStorage`). With nothing stored yet the decode fails, so Municipal stayed empty while the screens used their own hardcoded copy. Nothing was ever written to storage until the user pinned something, so Cyclops never saw a default at all.
**Fix:** `Municipal.defaultWatchList` is now the single source; `loadWatchListFromStorage()` falls back to it when nothing is stored. `MncplAllScreen` no longer writes `@AppStorage` directly — it routes through `municipal.setWatchList()`, making Municipal the only writer and demoting the `UserDefaults.didChangeNotification` observer from load-bearing to belt-and-braces.
**Deliberate distinction kept:** an **empty stored list is respected**. Unpin everything and you get the instructor view back; only a *missing* list seeds. Resurrecting defaults under a user who cleared them would be worse than an empty screen.
**Also:** defaults changed from three 文山區 lots (興隆市場 / 萬興國小 / 萬芳醫院 — our neighbourhood, opaque to anyone else) to landmarks: 台北101 `TPE0374`, 大安森林公園 `TPE0095`, 府前廣場 `TPE0096`.
**Status:** fixed, tested on a clean install, committed `881652b`.
**Files:** `Municipal+Cyclops.swift`, `MncplAllScreen.swift`, `AllTpeParkingScreen.swift`.

## 2026-09-05 — Three Cyclops cards under-filled the screen (fixed)
**Symptom:** with exactly 3 pinned lots the cards looked short and cramped; 2 and 4 looked right.
**Root cause:** an off-by-one between the sizing table and the layout branch. `case 3..<5: geoRh = 0.43` is calibrated for the **two-column grid**, but the layout branch is `items.count <= 3` → **single column**, which halves geoRh again. So three cards rendered at `0.215` of available height each and filled ~64%, where 2 filled 85% and 4 filled 86%. Three was the only count taking the grid's constant while rendering in the list.
**Fix:** `case 3` gets its own value (`0.54` → `0.27` per card, ~86% filled), and the ranges are spelled out per count. `3..<5` *read* like "3 and 4 behave the same" when they render in different layouts and cannot share a constant. `VStack(spacing: 16)` for wider gaps.
**Status:** fixed, tested, committed `43ac0a0`.
**Files:** `MncplCyclopsScreen.swift`.

## 2026-09-04 — Keyboard could not be dismissed on the All screen; user trapped (fixed)
**Symptom:** Type in the All-screen search (to add lots to the Cyclops watch list) → software keyboard appears and **never hides**. It lifts the floating tab-restore pill but not the tab bar, so every other tab becomes unreachable and the user is stuck on that screen. Reported by Jim 2026-09-04; originally logged 2026-06-15 and deferred.
**Root cause — three compounding faults:**
1. **`onSubmit` never released focus.** `MncplAllScreen.swift` inserted the token and returned; nothing set `searchFocused = false`. Pressing Return left the keyboard up.
2. **The only dismiss control was unreachable.** It was `ToolbarItem(placement: .automatic)` gated on `if searchFocused`. With a `.principal` `TextField` filling an `.inline` nav bar, `.automatic` has nowhere reliable to place it — and conditionally-inserted toolbar items are unreliable in SwiftUI regardless.
3. **The escape hatch was under the keyboard.** `AppTabView` auto-hides the tab bar after 5 s; the floating pill restores it — **at the bottom, beneath the keyboard**. So even discovering the pill didn't free the user.
Any one alone is survivable. Together they are a trap with no exit.
**Fix (three independent escape routes, deliberately):**
- `ToolbarItemGroup(placement: .keyboard)` with a Done button — attached to the keyboard's own accessory bar, so it **cannot be occluded by the keyboard**. Replaces the nav-bar item.
- `defer { searchFocused = false }` in `onSubmit`, plus `.submitLabel(.search)` — Return now closes the keyboard whether or not a token is inserted.
- `.scrollDismissesKeyboard(.immediately)` on the `List` — the gesture users reach for first.
**Also hardened:** `AllTpeParkingScreen.swift` (legacy Taipei screen) had the same `onSubmit`-without-dismiss and a conditional Done button. Lower severity — its button is inline and visible rather than in a toolbar — but the same class, so both screens now match.
**Audited, no change needed:** `NbsScreen` already dismisses via `.onTapGesture` and in its submit handlers. `Municipal_Screen` / `TpeParkTools` are debug/kitchen screens.
**Status:** fixed, tested on device, committed `0f863ed`.
**Files:** `MncplAllScreen.swift`, `AllTpeParkingScreen.swift`.

## 2026-09-01 — `minuteFlow()` published into `@Observable` state from a background thread (fixed)
**Symptom:** Cyclops numbers frozen while the model updated correctly. Worst observed: view stuck on `car:20` for **98 minutes** (logs4) across 84 model refreshes. Only a background→foreground round trip ever refreshed the cells. **Behaved differently on an iPhone 15 device vs an iPhone 17 Pro simulator** — the tell for a thread race.
**Root cause:** `Mu1Base.fetch(url:)` returns `URLSession.dataTaskPublisher`, which delivers on a URLSession background queue. `minuteFlow()` sinks that publisher **without `.receive(on: DispatchQueue.main)`**, so `availableVbj.send(parsed)` → `Municipal.actMinutely` → `refreshCyclops()` → `cyclopsMod = …` all ran off-main. Mutating `@Observable` state off the main thread leaves SwiftUI's invalidation unreliable: the model advances, the view is never told.
**Proof it was an omission, not a design choice:** its sibling `minutelyRetrieveFlow()` (`Mu1Base+Ext.swift:221`) has the identical chain **with** `.receive(on:DispatchQueue.main)`. `minuteFlow()` was copied from it and the hop was dropped.
**Also violates the project's own rule** in `CLAUDE.md`: *"Use `@MainActor` explicitly where UI updates occur."* Nothing enforces it — neither `Municipal` nor its methods are `@MainActor`.
**Fix:** added `.receive(on:DispatchQueue.main)` before the sink in `minuteFlow()`.
**Verified (logs7):** the new `🏠` body-eval diagnostic fires after each fresh `🎨` with `firstObs:0s`; `🖌 obsNow` sawtooths 156s → 0s → 4s **without** any backgrounding; zero freshness overrides.
**Correction (2026-09-02 audit):** my claim that `SourceBase.swift:180` was unhopped was **wrong** — that line is the `fetch` *definition*; its call site at `:103` hops correctly. All four sink sites are correct today. The risk is structural, not present — see [[00-why-municipal-should-be-mainactor]].
**Files:** `Mu1Base+Ext.swift` (`minuteFlow`). Full narrative: [[02-postmortem-what-went-wrong-and-why]].

## 2026-09-01 — Cyclops cells never re-rendered: a read-only `@Binding` (fixed)
**Symptom:** Cyclops parking numbers never updated — model `car:20`, cell displayed `19`, indefinitely. Long-standing; predates the freshness feature.
**Root cause:** `CyclopsView` held `@Binding var item` but **never wrote through it** (`$item` appears nowhere). SwiftUI decides whether to re-run a child's `body` by comparing its stored properties, and **a `Binding`'s identity is its storage location, not its value** — so it compares equal on every parent update and the child body is skipped.
**Why it went undiagnosed:** a stale parking number is indistinguishable from a quiet parking lot. Someone had already felt it and worked around it with `.id("\(pid)-\(uiKick)")` in `MncplCyclopsScreen0000` rather than diagnosing it. The freshness colouring is what exposed it — a frozen *timestamp* ages on its own and eventually changes colour, whereas a frozen *number* hides.
**Fix:** `@Binding var item` → `let item`; `ForEach($…cyclopsMod.items)` → `ForEach(municipal.cyclopsMod.items)` at all six call sites across three screens. Removed the now-unneeded `@Bindable`.
**Rule:** use `@Binding` only when the child writes back. A read-only `@Binding` actively suppresses updates. Pattern recorded in [[swiftui-state-and-identity]].
**Files:** `CyclopsView.swift`, `MncplCyclopsScreen.swift`, `CyclopsScreen2.swift`, `MncplCyclopsScreen0000.swift`.

## 2026-09-01 — `MncplParkAvPack.converted` means "last changed", not "last confirmed" (fixed)
**Symptom:** Cyclops freshness colouring (added 2026-08-31) showed every number grey forever, while the toolbar feed time kept updating normally. Reported by Jim ~10:43, 2026-08-31.
**Root cause:** `minuteFlow()` (`Mu1Base+Ext.swift`) bails out with `return` when the fetched payload hashes identical to the previous one — before `oParseMinute`, which is where `converted: Date.now` is stamped (`TaipeiObs.swift:58`). So `converted` freezes at the moment the content last **changed**, not when the feed was last **confirmed current**. Parking availability legitimately returns identical bytes for 30+ minutes, so confirmed-current numbers aged into the stale bucket.
**Why the toolbar disagreed — this was the diagnostic tell:** the toolbar reads `availableTime` = **max** `converted` across all zones, cells read their own zone's `converted`. A max keeps advancing as long as *any* zone republishes, so one frozen zone was invisible there.
**Same trap, one level up:** the 2026-08-31 note explicitly rejected `carTrail.last?.time` because it only advances on *change* — then used `converted`, which has the identical defect at pack level. On this codebase "when did this last change" and "when did we last confirm this" are different clocks in several places; freshness always wants the second.
**Fix:** new `minutelyConfirmedVbj` on `Mu1Proto`/`Mu1Base`, sent on **every** successful retrieval (both the unchanged-bail branch and the parsed branch). `Municipal.lastConfirmed[zone]` records it; `refreshCyclops()` stamps each lot with `max(pack.converted, lastConfirmed[zone])`.
**Battery regression avoided:** the first attempt reused the existing `minutelyUpdateVbj`, which feeds `secSincePrevRetrival` → `resumePolling()`'s no-arg `setMinutelyTimer()`, choosing 60s vs 210s. That would have tripled poll frequency after every foreground resume on a quiet feed. Backed out; confirmation got its own subject.
**Preserved deliberately:** the `< 512 bytes` guard returns *before* the hash check and sends no confirmation, so a genuinely failing feed still ages to grey — as does a cache-seeded cold launch before the first fetch. That's the feature's original purpose and it still works.
**Status:** fixed in working tree, **not committed, not compile-verified.**
**Still open — could look identical on screen:** if the watched pids don't match the live feed's ids, cells grey for a different reason (stale trail number, `observedAt[pid]` nil). Prime suspect is the `TPE####` seed residual below. **Log test:** a zone repeating `previousHash not changed` / `availble w/o update, this round over` every poll = this bug; a zone republishing `🐎 minutelyAvailable` while cells stay grey = id mismatch.
**Files:** `Mu1Base+Ext.swift`, `Mu1Proto.swift`, `Mu1Base.swift`, `mocks.swift`, `Municipal.swift`, `Municipal+Ext.swift`, `Municipal+Cyclops.swift`. Full write-up: [[00-freshness-grey-forever-root-cause]].

## 2026-09-10 — The map showed no data freshness at all
**Symptom:** Jim asked whether the map shares the staleness problem the Cyclops screens had. It does — in a purer form.
**Root cause:** `CustomButton` (the map pin) took **`availFetched: lot.aItem != nil`**, meaning *"we joined an availability record at some point"*. It **never expires**. A count fetched an hour ago rendered identically to one fetched ten seconds ago — the same failure the whole Cyclops arc turned out to be: *a stale parking number is indistinguishable from a quiet car park.* Worse than Cyclops pre-fix, which at least had a `converted` timestamp to be wrong about; the map had no time concept whatsoever.
**Fix — alpha, on Jim's suggestion, and it is the right channel here.** Colour on that badge already carries **two** meanings: scarcity (maroon ≤3 / dodger >3) and no-signal (gray). A third would collide. Alpha was already doing something adjacent — `0.45` meant "provisional, waiting" — so age *extends* an existing visual idea instead of introducing one.

| age | opacity |
|---|---|
| `<5 min` | 0.9 |
| `5–30 min` | 0.7 |
| `≥30 min` | 0.45 |
| unknown | 0.9 — no clock yet, so do not imply staleness we cannot prove |

**The floor is deliberately 0.45**, the value "provisional" already used, so nothing becomes less legible than the dimmest state the pin could already reach on a busy map. **Confirmed by Jim 2026-09-10** — *"keep 0.45 for now, 30 min is a long time ago"*: at half an hour the number has stopped being information and the dimness is the point, so legibility matters less than the signal that it is old. The number fades with the badge — a solid white digit on a faded badge still reads as fresh.
**Reuses `AvailFreshness` and `Municipal.lastConfirmed`** rather than inventing a second freshness model, and `lastConfirmed` specifically: "last **changed**" was the exact trap that cost a session on 2026-09-01.
**Found while wiring it — a dead field:** `MunicipalAvail.availableUpdated: Date?` looks like precisely the right hook and is **never assigned**, only ever cleared (`MunicipalAvail.swift:54`). Someone intended per-lot map freshness and did not finish it. Left in place; the zone-level clock is the better source anyway.
**Why a plain timer, not `TimelineView`:** `TimelineView` would rebuild the entire `Map` every minute, and MapKit is the most expensive thing on that screen. A 60 s `Timer.publish` with `tolerance: 6` (the battery #6 convention) ticks only the pins.
**Status:** implemented, not yet built or seen on device.
**Files:** `hootowl/constructing/CustomButton.swift`, `hootowl/Municipalities/Nbs/NbsScreen.swift`.

## 2026-09-11/12 — Three Release-only breakages that no Debug build ever compiled
**Symptom:** The first-ever Archive for App Store Connect failed to build. Debug builds had been clean for months.
**Root cause — one shape, three instances.** All three lived in the `#else` half of an `#if DEBUG`. **Xcode never type-checks the half that is not active**, so a project can build cleanly forever while carrying broken Release-only code. The first Archive is the first time that code is compiled at all.
1. **`iAp/StoreObs.swift:270`** — the `.malformed21002` case called the `async` `revokeEntitlment(rcpVld0:)` with **no `await` and no `Task`**. The enclosing context is a Combine `.sink(receiveValue:)` closure — synchronous, non-async, escaping — so it cannot be awaited there at all; the work must be handed to a `Task`. **The other nine cases in the same switch already did exactly that**; this one did not.
2. **`Backyard Birds/ContentView.swift`** — `debugForceAd` was declared only under `#if DEBUG` while **two** Release code paths referenced it (`if showAd || debugForceAd` and the `.environment(\.adBannerHeight, …)` modifier), so Release could not resolve the symbol.
3. **`Municipalities/Nbs/NbsObsM.swift:120`** — a `locUpdateMeters` reset that needed a `#if DEBUG` guard.
**A near-miss worth recording.** The first attempt at (2) put `debugForceAd = true` in the Release branch. Since the use site is `if showAd || debugForceAd`, that would have **forced the ad banner on for every user including paying subscribers** — breaking the only thing a subscription buys, and precisely what App Review tests when it subscribes in the sandbox. The second attempt guarded the *use sites* instead but missed the `.environment` line one row below, so it still did not compile.
**Fix:** all three guarded correctly, committed as `85e4a45`. For (2) the declaration is guarded in **both** halves (`false` in Release) rather than guarding each use site — one place to get right instead of every current and future reference. The compiler folds `showAd || false` away, so subscribers still lose the banner.
**Status:** ✅ fixed **and compile-verified 2026-09-14** — `hootowl 2026-9-14, 5.38 PM.xcarchive` built successfully in Release from this branch, two days after the last source change. An Archive is the only thing that compiles these lines at all; a Debug build exercises none of them.
**Pattern:** [[swift-patterns#if-debug-else-means-half-your-code-is-never-type-checked]]
**Files:** `hootowl/iAp/StoreObs.swift`, `hootowl/Backyard Birds/ContentView.swift`, `hootowl/Municipalities/Nbs/NbsObsM.swift`.

## 2026-09-11 — App icon carried an alpha channel; ITMS-90717 blocked the first ASC upload
**Symptom:** First-ever archive upload to App Store Connect rejected: *"Invalid large app icon. The large app icon in the asset catalog in 'hootowl.app' can't be transparent or contain an alpha channel."* (`code = 90717`).
**Root cause:** **All 20 PNGs** in `hootowl/Assets.xcassets/AppIcon.appiconset` carried an alpha channel, and `Icon1024.png` was genuinely transparent, not merely 4-channel — **26.01% of pixels fully transparent**, 25,127 partially so, all four corners `rgba(0,0,0,0)`. The art is an owl shape floating on nothing. Apple requires the 1024 marketing icon to be fully opaque.
**Fix:** Flattened onto white (art unchanged) for the 13 icons referenced by the `iphone` / `ipad` / `ios-marketing` idioms — `Icon1024/180/167/152/120/87/80/76/60/58/40/29/20`. Written via CoreGraphics with `CGImageAlphaInfo.noneSkipLast`, so the output PNG has **no alpha channel** rather than an opaque one. Verified `sips -g hasAlpha` → `no` on all 13. The six `mac`-idiom-only icons keep their transparency deliberately (macOS icons are free-form). `Iconwatch.png` is referenced by nothing.
**Status:** ✅ fixed — the upload blocker is cleared.
**Left open, and more important than the bug:** the icon **should not ship**. It draws its own rounded corners while iOS applies its own squircle mask, so **the ear tufts will be clipped**; it has **`yuchinghsu`** written across it in near-illegible pink-on-pink; and it is an **owl**, the retired placeholder identity, on an app now called `Find Parking TW` / `找車位`. Jim started a replacement 2026-09-11. Tracked in [[jim-actions]]; icon workflow recorded in [[operations#2e-app-icons--2026-09-11]].
**Files:** `hootowl/Assets.xcassets/AppIcon.appiconset/*.png`.

## 2026-09-09 — The subscription sheet rendered English on a Chinese device
**Symptom:** Jim, on a Chinese-language build: *"when I click the creditCard icon in Chinese, it load a screen with only English on it."*
**Root cause — the interesting one:** the StoreKit product localisation was **`zh_CN`**. The app's `knownRegions` are `en` and **`zh-Hant`**, so a Traditional Chinese device never matched `zh_CN` and StoreKit fell back to `en_US`. The plan name and description — which are most of what `SubscriptionStoreView` renders — came out English on an otherwise-Chinese sheet. **Simplified is not a fallback for Traditional**; they are separate locales as far as matching is concerned.
**Second cause:** the privacy-policy link inside `.subscriptionStorePolicyDestination` was a bare `Link("Privacy Policy", …)` literal, so it stayed English at any locale. Now `sub_privacy_policy` in the catalogue.
**Why our own header still looked right:** `sub_paywall_title` / `sub_paywall_body` were correctly localised all along. The English was coming from **StoreKit's own content**, not from ours — worth knowing, because it means "the screen is in English" can have a cause entirely outside the string catalogue.
**Fixed alongside:** the product description read *"Complete Features, no Ad. A little cost."* — the same overclaim deleted from the paywall copy on 09-08. Nothing is gated behind the subscription; only the ads go. Both locales now say that.
> [!warning] The code fix is only half of it
> `hootowl/iAp/hootowl.storekit` governs **local testing only**. The same Traditional Chinese localisation must be added to the product in **App Store Connect**, or real users see exactly this bug on a real build. Tracked in [[jim-actions]].

> [!bug] The zh_CN fix was necessary but **not sufficient** — found 2026-09-10
> Jim retested on a zh-Hant-TW simulator and **both the screen and the sheet were still entirely English.** The real cause was one level up, in the same file's `settings` block:
> ```json
> "_locale": "en_US",  "_storefront": "USA"
> ```
> **StoreKit Testing renders product names, descriptions, prices and the store view's own chrome from *that* locale, not from the device language.** So no amount of device-language or string-catalogue work could have changed it — and it masked the `zh_CN` problem underneath, because neither localisation was ever consulted.
> Now `zh_TW` / `TWN`, which is also just the right default for the primary market. `displayPrice` moved `2.99` → `90`: 2.99 was a USD figure and renders as **NT$2.99** under a Taiwan storefront, which is not a plausible number to be looking at while testing.
> **Test configuration only.** In production the storefront and locale come from the user's Apple Account — so this particular symptom would *not* have shipped, but the ASC localisation gap underneath it would have.

**How it was diagnosed, since guessing failed twice:** `DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer` makes `xcodebuild` and `simctl` usable from here even though `xcode-select` points at CommandLineTools. That allowed reading the simulator's `AppleLanguages` (correctly `zh-Hant-TW`), confirming no per-app language override, dumping the **installed** bundle's compiled `zh-Hant.lproj/Localizable.strings` (which did contain 廣告養活這個 App), and finally launching the app and screenshotting it. The screenshot settled the question: 自動更新 and 更多 rendered in Chinese while "Near Me!", "all" and "options" stayed English — those keys simply have no 中文 — proving the app's localisation machinery was fine and the fault had to be inside StoreKit.

**Status:** fixed for local testing; **App Store Connect localisation still owed.**
**Files:** `hootowl/iAp/hootowl.storekit` (product localisation *and* `settings._locale`/`_storefront`), `hootowl/iAp/subUi/SubscriptionScreen.swift`.

## 2026-09-09 — The map screen offered "background nearby search", which the app cannot do
**Symptom:** Jim, looking at the running app: *"there is an 'Enable always for background nearby Search' at the bottom of the mapView."* A banner with an **Upgrade** button, sitting at the bottom of `NbsScreen`.
**Why it mattered more than a stray string:** it was shown to **every iOS user, permanently**. The banner fires on `case .authorizedWhenInUse`, and since battery pick #9 (2026-06-15) removed the Always escalation, `.authorizedWhenInUse` is the **permanent end state for every iOS user**. So this was not an edge case — it was on screen for everyone, on the map, since June.
**Three separate faults:**
1. **The button was dead.** `municipal.requestLocationPermission()` on iOS hits the `#if os(iOS)` branch that logs *"already at WhenInUse — no Always escalation per #9"* and returns. Tapping Upgrade did nothing at all — no dialog, no state change.
2. **It promised something the app cannot do.** There is no `UIBackgroundModes` in `Info.plist`, and `pauseForBackground()` calls `stopUpdateLocation()` outright. Background nearby search does not exist and could not have worked.
3. **It contradicted our own shipping copy.** Onboarding screen 3 says location is *"used only while the app is open — never in the background"*, and the 中文 says **切入背景就停止**. The map screen said the opposite. Both cannot be true, and the audit in [[00-location-privacy-audit]] had confirmed the copy — so the banner was the wrong one.
**Also a review risk:** a control that promises background location, has no matching Info.plist key, and does nothing when tapped is the kind of thing a reviewer opens a question about.
**Fix:** `EmptyView()` on iOS. **macOS keeps the banner** — `locAuthorized` there accepts only `.authorizedAlways` and the macOS branch genuinely still escalates, so the nudge is accurate on that platform.
**How it survived:** #9 changed the *behaviour* and left the *UI* that advertised it. Worth remembering as a class: when a capability is removed, grep for the strings that sold it, not just the code that implemented it.
**Status:** fixed, not yet built.
**Files:** `hootowl/Municipalities/Nbs/NbsScreen.swift` (`locAuthBanner()`).

## 2026-09-09 — Tapping a contact number dialled it without the extension
**Symptom:** Jim asked for the phone numbers to be tappable *including the extension*. Checking what the code produced showed the extension was already being thrown away.
**Root cause:** `MunicipalContactButton.resolvedTelURL` rewrote `#` as `;`, producing `tel:0227590666;6543`. **In RFC 3966 a semicolon begins a URI parameter**, so iOS parsed `;6543` as a parameter named "6543", placed the call to the base number and discarded the rest. Nothing failed visibly — the call connected, to a switchboard, with no extension sent. Taipei's published contact is `02-27590666#6543`, so this affected the one number we ship.
**Fix:** `#` and `;` both become `,,`. Commas are *pauses*, and digits following a pause are sent as DTMF — the actual mechanism for reaching an extension. Two commas is roughly four seconds, enough for a greeting to begin.
**Handled alongside, but made opt-in — national numbers do not dial on a foreign SIM.** A visitor roaming on a home SIM cannot dial a Taiwanese national number, which matters because the app ships to the US, Japan, Hong Kong and Macau **precisely because those people visit Taiwan**. The rewrite `02…` → `+886 2…` therefore exists, but **defaults to off** on Jim's call: nearly every user is in Taiwan on a local SIM where the published number already works, and rewriting it by default would change behaviour for the many to serve the few. It is a toggle in **Options → Advanced**, captioned by *who it is for* ("turn this on if your phone uses a SIM from outside Taiwan") rather than by mechanism. Short service codes (`1999`) and toll-free `0800` ranges are national-only by nature and are never rewritten either way.

**The extension handling is unconditional** — dropping the extension was a bug, not a preference.
**Verified** against ten inputs before committing — both extension markers, a mobile, an already-international number, punctuation-heavy lot numbers, junk (yields nil, so the button hides), and the two live Gist values.
**Deferred deliberately (Jim, 2026-09-09):** whether four seconds is long enough for these switchboards can only be settled by a real call, and it is not worth blocking on. Calling a car park is a rare action, and the confirmation dialog displays the number in full (`ContactView.swift:158`), so a user who needs the extension can read it and dial by hand. **The failure mode is mild and self-reporting** — if the DTMF fires during the greeting, someone says so, and a third comma fixes it. Watch for it in feedback rather than spending a device session on it.
**Status:** fixed, needs the device check above.
**Files:** `hootowl/UI/ContactView.swift` (`telURL(from:)`).

## 2026-09-07/09-08 — A subscribed user was left a white circle in the toolbar
**Symptom:** Jim, on the map screen: subscribe, the Subscribe button disappears as intended, **but a white circle stays behind where it was.**
**Root cause:** mine, and the comment I wrote is the confession. `SubscribeToolbarButton`'s "already subscribed" branch rendered a zero-sized `Color.clear`, reasoning that an empty item would stop the toolbar reshuffling its other items the instant a purchase completed. That reasoning is wrong twice over: **a toolbar item draws its own circular background behind whatever content it holds**, and `Color.clear` is still content — zero-sized or not. So the item stayed, lost its label, and rendered as bare chrome.
**Fix:** no `else` branch at all. `body` is an implicit `@ViewBuilder`, so an `if` with no `else` yields nothing and the toolbar item genuinely disappears. The wire that lived in the removed branch is not needed — reaching that state means the button was already on screen and already subscribed to the relay.
**Also fixed alongside:** `tier` now seeds from `entitledSubscriptionTeirRelay.value` instead of defaulting to `.none`, so an already-subscribed user does not get a flash of the button every time a screen appears.
**Rule worth keeping:** *"render a placeholder so the layout does not jump"* is a habit from stack and grid layouts. **In a toolbar it backfires** — the container, not the content, supplies the visible chrome, so the only way to remove a toolbar item is to not produce it.
**Status:** fixed, not yet built.
**Files:** `hootowl/iAp/subUi/SubscribeToolbarButton.swift`.

## 2026-09-07 — No privacy manifest; ATT never requested (AdMob is staying)
> [!warning] Corrects an earlier version of this entry
> The first version of this entry claimed AdMob was "linked but never used" and that no ad was ever initialised. **That was wrong.** It came from grepping for the legacy symbol `GADMobileAds`, which the Google SDK renamed to `MobileAds` in v12 — so the grep missed every real call site. Banner ads are properly built and wired. The privacy-manifest and ATT findings below survive; the "dead weight, decide keep-or-drop" framing does not. Corrected the same day, before Jim acted on it.

**What is actually true — banner ads are working:**
- `hootowlApp.swift:78-79` — `gAdConfig()` + `MobileAds.shared.start()` at app init, `#if os(iOS)`.
- `AdMob/BannerView.swift` — `AdBannerView`, a `UIViewRepresentable` wrapper. **Test ad unit in DEBUG, real unit in release** (`GadCon.banner_Test` / `banner0_Id`) — correct practice, and it means dev traffic never hits the real unit.
- `Backyard Birds/ContentView.swift:58` — placed via `.safeAreaInset(edge: .top)`, gated on `showAd`.
- `iAp/StoreObs.swift:356` — `showAdRelay` is driven by subscription tier, so paying users lose the banner. A `debug_force_ad` toggle exists for testing.
- Banner height is published through `\.adBannerHeight` and **honoured by every main screen** — `MncplCyclopsScreen` (including its card-size arithmetic at `:102`), `MncplAllScreen`, `NbsScreen`, `AppTabView`.

**Bug 1 — the app target has no `PrivacyInfo.xcprivacy`.** The only one in the tree ships inside `GoogleMobileAds.framework`. With ads staying, this is not optional: the manifest needs `NSPrivacyTracking`, `NSPrivacyTrackingDomains`, and the accessed-API reasons (`UserDefaults`, `CA92.1`, used by `@AppStorage`, the snapshot cache and the config cache). **iOS 17+ blocks connections to tracking domains that are not declared**, and an undeclared required-reason API draws Apple's ITMS-91053 notice.

**Bug 2 — ATT is never requested, so ads are non-personalised.** `NSUserTrackingUsageDescription` is **absent** from `Info.plist`, and `AdMob/ATTWarmup.swift`'s `barebackAtt()` / `AttModel` have **zero callers**. Consequences both ways:
- As-is: no IDFA is ever requested, so every impression is non-personalised — materially lower eCPM. **Revenue is being left on the table by omission, not by choice.**
- If anything calls `requestTrackingAuthorization` before the Info.plist key exists, **it is an immediate crash.**

**Bug 3 — interstitials do not exist in the build.** `AdMob/Interstitials.swift` and `AdMob/GadHostV.swift` appear in the project navigator (`PBXFileReference` + group entry) but have **no `PBXBuildFile` and no Sources-phase entry in any target** — they are not compiled. `Interstitials.swift` still uses the pre-v12 symbol `GADInterstitialAd`, which is presumably why: it would not compile against the current SDK. `AdMob/gAdBannerView.swift` is worse — **not in the project file at all**, and it declares a `BannerView` that would collide with the SDK type if it were ever added.

**Status:** open. Manifest + ATT are release items; the dead ad files are cleanup. Tracked in [[jim-actions]] and [[operations#c-app-store-submission]].
**Files:** `hootowl.xcodeproj` (no app-target privacy manifest), `hootowl/Info.plist`, `hootowl/AdMob/ATTWarmup.swift`, `hootowl/AdMob/Interstitials.swift`, `hootowl/AdMob/GadHostV.swift`, `hootowl/AdMob/gAdBannerView.swift`.

## 2026-09-07 — The contact Gist is still all example.com placeholders (release blocker)
**Symptom:** Not a crash — the app would ship pointing users at fake contact details. Fetched the live config at `ContactConfig.gistRawURL` and it is still the sample content from the file's own doc comment, unchanged since the mechanism was built:
```json
{ "version": 1, "contacts": {
    "taipei":        { "email": "taipei@example.com", "phone": "+886-2-1234-5678" },
    "newTaipeiCity": { "email": "ntpc@example.com",   "phone": "+886-2-8765-4321" } } }
```
**Why it matters:** `MunicipalContactButton` defaults to `showPhone: true`. `resolvedPhone` prefers the lot's own `parkTel` and **falls back to `contact.phone`** — so any lot with no telephone of its own offers users **`+886-2-1234-5678`** to dial. The email path (`showEmail`, reserved for lots with no online availability) sends to `@example.com`, which bounces. Neither fails loudly; both look like working buttons.
**Root cause:** the Gist was created with the example JSON and never filled in. Nothing in the code can detect this — an address is either present or absent, and these are present.
**Fix:** replace the Gist contents with real values (Jim's, outside the repo). While editing, `support` and `tutorial` want adding too — see [[01-tutorial-video-and-screenshots]]. **No app release needed for any of it**, which is the point of the mechanism.
**Worth considering:** the code cannot distinguish placeholder from real, but it *could* refuse obvious sentinels — treating a `@example.com` address or a `1234-5678` phone as absent would make this class of mistake impossible to ship. Not implemented; would be ~4 lines in `ContactConfig`.
**Status:** ✅ **fixed 2026-09-09.** Both cities now carry real values pulled from their own open-data portals and pushed to the Gist over SSH — Taipei `sb0457@gov.taipei` / `02-27590666#6543`, New Taipei `ae8131@ntpc.gov.tw` / `02-29702960`. The `support` placeholder was deleted rather than replaced, because a *working* button to a dead domain is worse than a hidden one. Sources, values and the recurring re-check now live in [[data-sources]].
**Files:** the Gist itself; `hootowl/network/ContactConfig.swift`, `hootowl/UI/ContactView.swift` (consumers).

## 2026-08-20 — `CLAUDE.md` claims park IDs are `tpe_`/`ntpc_` prefixed; no code does that
**Symptom:** Not a runtime bug — a **documentation trap** that has already cost real investigation time. `CLAUDE.md` ("Taipei Parking ID Note") states: *"`MncplParkItem` IDs are prefixed: `"tpe_..."` for Taipei, `"ntpc_..."` for New Taipei City."* `AGENTS.md` carries the same text. **This is not true of the current code.**
**Root cause:** The prefix convention exists only as an unused helper. `String.municipalityFromPidPrefix` (`MunicipalEnum.swift:44–48`) is the sole code that knows about `tpe_`/`ntpc_`, and it has **zero callers** — the only grep hit is its own definition. Nothing applies a prefix:
- `MncplParkItem.id` ← `MncplParkItem.swift:173` passes `id: p0.id` straight through from the source record.
- `MncplParkItemAvail.parkId` ← `TaipeiObs.swift:59` (`parkId: $0.id`) and `NewTaipeiCityObs.swift:62` (`parkId: fields[0]`).

Both sides are raw feed IDs. Whether the convention was planned-and-never-built or built-and-later-removed is unknown; either way the doc describes an intention, not the code.
**Why it matters:** this doc line is what seeded the "unverified assumption" flagged in [[cyclops-first-run]] and [[bugs]] on 2026-08-07 — recorded as possibly *"a larger bug than any of the above"* and made the gate on the whole Cyclops fix plan. It cost a cycle. Cleared 2026-08-20 by grep: raw-to-raw, no mismatch, plan unchanged.
**Fix / workaround:** none applied to code — nothing is broken. **`CLAUDE.md` + `AGENTS.md` should be corrected** (Jim's call — they're Jim's instruction files). Either delete the prefix sentence, or rewrite it as *"IDs are raw source IDs; a `municipalityFromPidPrefix` helper exists but is unused."* Deciding whether to actually adopt the prefix convention is a separate design question — it would need a real reason, since municipality is already carried explicitly on `MncplParkInfo.mncplt` / `MncplParkAvPack.municipal`.
**Residual, unverified:** the hardcoded watchList seeds `["TPE0080", "TPE0835", "TPE0270"]` (`MncplAllScreen.swift:47`, `AllTpeParkingScreen.swift:28`) use an uppercase `TPE####` shape matching neither the raw feed format nor the `tpe_` convention. Note the Sep-2024 Taipei ID overhaul recorded in `CLAUDE.md` (`"326"` → `"TPE0080"`) — so `TPE####` may be a genuine current Taipei format and the raw feed IDs seen elsewhere (`020060`, `060105`) may be New Taipei's. **Not resolved.** If a *default* pin never resolves while a *user-added* pin does, this is the explanation. Worth one glance during the device run.
**Status:** open (documentation), no code change needed.
**Files:** `CLAUDE.md` + `AGENTS.md` (Taipei Parking ID Note), `MunicipalEnum.swift:44–48` (dead helper).

## 2026-08-07 — Cyclops shows 🕐 on every cache-less launch (investigated, not fixed)
**Symptom:** Open Cyclops after launch → every watched lot shows 🕐 and never resolves. Force-quit + relaunch → Available numbers appear immediately. Originally reported by Jim 2026-06-29 as a "first run" bug.
**Not just first run:** the 🕐 window opens on any launch without a usable cache — fresh install, **cache older than 24h** (`Municipal+Cache.swift:47`), or iOS purging `Library/Caches`. The 24h path is the common one: parking use is episodic, so a user who parks twice a week hits it *every time*.
**Root cause (partially confirmed, static reading only):** `activate()` starts a 15s minutely timer but **fires no immediate fetch**, while `resumePolling()` (added in Phase 3) does — `Mu1Base+Ext.swift:78`. With `loadOnStart` activating protos at +1.2s, a cache-less launch shows 🕐 for **≥16s guaranteed**. Relaunch appears instant because `seedFromCache()` fills `parkAvPack` synchronously in `Municipal.init` (`:133`) before `wireCyclops()` (`:134`).
**Two further bugs found during the trace:**
- `Municipal+Ext.swift:135` — cold-start branch of `assessFences` sends enclosing fences to `allFencesVbj` instead of `activeFencesVbj`, **destructively narrowing the full fence list**. User outside all fences → `allFencesVbj` becomes `[]` → every later `assessFences` throws `.noFences` permanently. Latent today; becomes a hard failure the moment activation goes fence-driven.
- `Municipal+Ext.swift:158` `activeIds` unused, `:165–175` `ActDeActOnes` has **zero callers** — the fence→activation link was never wired, so every proto polls for every user regardless of location. Interacts with the deferred battery measurement in [[battery]].
**Fix / workaround:** none applied — Jim requested investigation only. Proposed: (1) immediate `minuteFlow()` in `activate()`, one line; (2) `allFencesVbj.send` → `activeFencesVbj.send`, one word; (3) fence-driven activation = design decision, not a patch.
**Status:** open. Investigated 2026-08-07, **no code changed**, not device-verified.
**Still unknown:** the ≥16s window is proven; "forever" is not. Needs one fresh-install device run to see whether the clock clears on its own after ~15–20s or genuinely never — that splits Finding 1 from the silent `minuteFlow` bail-outs at `Mu1Base+Ext.swift:144–177`.
**~~Unverified assumption worth checking first~~ — checked 2026-08-17, cleared.** `CyclopsModel.swift:112` compares raw-to-raw: neither `MncplParkItemAvail.parkId` (from `TaipeiObs.swift:59` / `NewTaipeiCityObs.swift:62`) nor `MncplParkItem.id` (`MncplParkItem.swift:173`) carries a prefix, and the `tpe_`/`ntpc_` helper (`MunicipalEnum.swift:44–48`) has **zero callers**. No mismatch; the plan does not reorder. Residual: the hardcoded `TPE####` watchList seeds at `MncplAllScreen.swift:47`. Detail in [[cyclops-first-run]].
**Files:** full investigation with all file:line references in [[cyclops-first-run]] (standalone topic note).

## 2026-07-12 — Misleading `onChange` "expects 0/1 arguments" error was a missing target membership
**Symptom:** Build error on `hootowlApp.swift:51` at the `scenePhase` handler: *"Contextual closure type '() -> Void' expects 0 arguments, but 1 was used"* — and after tweaking the closure, it flipped to *"'(ScenePhase) -> Void' expects 1 argument, but 2 were used."* The error message **shifted between overloads** across edits even though the closure was correct.
**Root cause:** The new file `Municipal+Lifecycle.swift` (Phase 3, written to disk directly, not via Xcode's "Add Files") was **never added to any target** — it appears nowhere in `project.pbxproj` (no `PBXFileReference`, no `PBXBuildFile`, no Sources-phase entry). So the compiler never saw `pauseForBackground()` / `resumeForForeground()`; `municipal.resumeForForeground()` inside the `.onChange` trailing closure was an unresolved symbol. Because `onChange` is **overloaded**, Swift couldn't anchor the closure, failed against every candidate, and reported an arg-count mismatch on whichever overload it deemed "closest" — hence the shifting, misleading message *at the call site* instead of a clean "no such member."
**Fix:** Add `Municipal+Lifecycle.swift` to Target Membership — **both** the iOS and macOS app targets (committed sibling files like `Municipal+Cache.swift` / `Municipal+Cyclops.swift` each appear **twice** in the Sources phase, once per target). In Xcode: select file → File Inspector (⌥⌘1) → tick both Target Membership boxes; or right-click the group → Add Files → check both targets. No change to `hootowlApp.swift` or the lifecycle file was needed.
**Diagnosis tip:** `grep -n "MyNewFile.swift" *.xcodeproj/project.pbxproj` — if it returns nothing, the file isn't in the build. Confirmed here by comparing against the two committed `Municipal+*` files.
**Status:** fixed.
**Files:** `hootowl/Municipalities/framework/Municipal+Lifecycle.swift` (was orphaned), `hootowl/App/hootowlApp.swift:51` (innocent — the reported line). Pattern captured in [[swift-patterns#new-swift-file-must-be-added-to-target-membership]].

> [!info] Timeline doesn't match git — noted 2026-08-17
> The dated entry above is left as written, but the repo tells a different story about *when* the membership was added. `Municipal+Lifecycle.swift` appears **6 times** in `project.pbxproj` today (1 `PBXFileReference`, 2 `PBXBuildFile`, 1 group entry, 2 Sources-phase entries = both targets), and `git show aa6b02a:hootowl.xcodeproj/project.pbxproj` already contains all 6 — while `61eec92` (2026-06-24) contains **zero**. No commit after `aa6b02a` (2026-06-26) touches `project.pbxproj`, and the working tree is clean.
>
> So the file entered the project **fully target-linked in `aa6b02a` on 2026-06-26**, two weeks before this entry's date. Either the membership was added in Xcode just before that commit and this entry re-diagnosed an already-fixed build, or the diagnosing grep was run from the wrong directory (`*.xcodeproj/project.pbxproj` silently matches nothing outside the repo root) and returned a false negative.
>
> **What is verified today:** the membership is correct and committed. The *cause* narrative is the part in doubt, not the outcome. The [[swift-patterns#new-swift-file-must-be-added-to-target-membership]] pattern is still sound advice independent of this timeline.

## 2026-06-09 — District-prefixed Taiwan addresses silently dropped by Apple geocoder
**Symptom:** Typing `北投區中央北路2段350巷66號` in the Nbs address search returned zero results. The same address without the district prefix (`中央北路2段350巷66號`) worked.
**Root cause:** `MKLocalSearchCompleter` and `CLGeocoder` return nothing for Taiwan addresses that lead with a 區 but no 市/縣 prefix. Prepending the city (`台北市…`) resolves them.
**Fix:** Pre-normalize the query via `AddressSearchObs.normalized(_:)` — prepend `台北市` / `新北市` when the query starts with a known district and has no 市/縣 marker. The user-visible search bar is unchanged.
**Status:** fixed and committed. ~~working tree, not yet committed~~ — corrected 2026-08-17: `normalized(_:)` is present at `AddressSearchObs.swift:139` and the file's last commit is `08c5816` (2026-06-13). Working tree is clean, so this landed long ago; the "not yet committed" note was stale for ~2 months.
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

## 2026-09-14 — A dangling `ConcaveHull` package reference blocked every command-line build
**Symptom:** any `xcodebuild` invocation on `hootowl.xcodeproj` — even `-list` — died before doing anything:
`xcodebuild: error: Could not resolve package dependencies: the package manifest at '/Package.swift' cannot be accessed`.
The vault has recorded this since June as *"the CLI can't build this project — `Package.resolved` is gitignored so SPM re-resolves `ConcaveHull` over the network"*. **That diagnosis was wrong**, and it has been quietly costing every session the ability to compile anything outside Xcode.
**Root cause:** the project carried an `XCRemoteSwiftPackageReference` to `https://github.com/Syncheo/ConcaveHull`, pinned `upToNextMajorVersion` from `1.3.0`. **Tag `1.3.0` of that repository contains no `Package.swift`** — it is a CocoaPods-era release; the manifest only exists on `master`. So resolution can never succeed at any version the requirement allows. It is not a network problem and not a missing `Package.resolved`; it fails identically offline, online and with the sandbox off.
It never mattered in Xcode because **nothing depends on the product**: no Swift file imports `ConcaveHull`, and `packageProductDependencies` is empty on `hootowl`, `hootmac` and `hoot_test_ui`. Xcode reports the resolution failure in the issue navigator and builds anyway. `xcodebuild` treats it as fatal.
**Fix:** delete both references to `B2B843552EB3478700A6ACCE` from `project.pbxproj` — the entry in the project's `packageReferences` list and the whole `XCRemoteSwiftPackageReference` section. 13 lines, no other change. `plutil -lint` clean afterwards, and `xcodebuild -list` then works.
**Consequence:** `xcodebuild` now builds this project from the command line. That is how `hootmac` was finally verified the same day — Debug *and* Release, both `** BUILD SUCCEEDED **`.
**Status:** fixed in the working tree on `icon-replacement`, **not committed** as of writing.
**Files:** `hootowl.xcodeproj/project.pbxproj` (was lines 1436–1438 and 2283–2292).
**Lesson, and it is the same one as the rest of this branch:** a failure you have written down an explanation for stops being investigated. The explanation was plausible, cited a real gitignored file, and was wrong for three months.
