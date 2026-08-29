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

## 2026-08-20 — `CLAUDE.md` claims park IDs are `tpe_`/`ntpc_` prefixed; no code does that
**Symptom:** Not a runtime bug — a **documentation trap** that has already cost real investigation time. `CLAUDE.md` ("Taipei Parking ID Note") states: *"`MncplParkItem` IDs are prefixed: `"tpe_..."` for Taipei, `"ntpc_..."` for New Taipei City."* `AGENTS.md` carries the same text. **This is not true of the current code.**
**Root cause:** The prefix convention exists only as an unused helper. `String.municipalityFromPidPrefix` (`MunicipalEnum.swift:44–48`) is the sole code that knows about `tpe_`/`ntpc_`, and it has **zero callers** — the only grep hit is its own definition. Nothing applies a prefix:
- `MncplParkItem.id` ← `MncplParkItem.swift:173` passes `id: p0.id` straight through from the source record.
- `MncplParkItemAvail.parkId` ← `TaipeiObs.swift:59` (`parkId: $0.id`) and `NewTaipeiCityObs.swift:62` (`parkId: fields[0]`).

Both sides are raw feed IDs. Whether the convention was planned-and-never-built or built-and-later-removed is unknown; either way the doc describes an intention, not the code.
**Why it matters:** this doc line is what seeded the "unverified assumption" flagged in [[cyclops-first-run]] and [[bugs]] on 2026-08-07 — recorded as possibly *"a larger bug than any of the above"* and made the gate on the whole Cyclops fix plan. It cost a cycle. Cleared 2026-08-20 by grep: raw-to-raw, no mismatch, plan unchanged.
**Fix / workaround:** none applied to code — nothing is broken. **`CLAUDE.md` + `AGENTS.md` should be corrected** (Jim's call — they're his instruction files). Either delete the prefix sentence, or rewrite it as *"IDs are raw source IDs; a `municipalityFromPidPrefix` helper exists but is unused."* Deciding whether to actually adopt the prefix convention is a separate design question — it would need a real reason, since municipality is already carried explicitly on `MncplParkInfo.mncplt` / `MncplParkAvPack.municipal`.
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
