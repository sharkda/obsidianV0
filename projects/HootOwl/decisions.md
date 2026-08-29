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

## 2026-08-20 — `CLLocationManager` dedupe (battery #5)
**Decision:** `Municipal` creates exactly one `CLLocationManager`. The assignment in `init()` (`Municipal.swift:127`) is the canonical one; `wire0()` configures that instance rather than replacing it. The redundant `self.locationMan = CLLocationManager()` at the top of `wire0()` is deleted, with a WHY comment left in its place.
**Why:** `locationMan` is a non-optional `var` (`Municipal.swift:44`), so it *must* be assigned before `super.init()` — that constraint is real and the `init()` assignment can't simply be removed instead. `wire0()` then threw that instance away and built a second, which received all the configuration (`delegate`, `desiredAccuracy`, `distanceFilter`). The discarded one was never configured and never started, so this was pure waste, but it also left genuine ambiguity about which manager the lifecycle calls (`startUpdateLocation()` / `stopUpdateLocation()`, added in Phase 3) were acting on. Closing the last item on the pre-release shortlist.
**Alternatives considered:**
- Make `locationMan` optional / lazy so only `wire0()` creates it — rejected as a larger change touching every use site, for no behavioural gain.
- Leave it alone — rejected; it was already logged as the last shortlist item, and the Phase 3 lifecycle work made the ambiguity worth removing.
**Impact:**
- `hootowl/Municipalities/framework/Municipal.swift` — one line deleted from `wire0()`, two comment lines added. Exactly one `locationMan =` site remains project-wide (was two).
**Status:** Working tree only, **not committed, not compile-verified.** `xcodebuild` can't build from the CLI here — `Package.resolved` is gitignored, so SPM tries to re-resolve `ConcaveHull` over the network and fails (pre-existing since `dfa738f`, unrelated). Build once in Xcode. Full caveat in [[battery#decision-log-append-as-decisions-are-taken]].
**Battery note:** this is **code-health, not a battery win** — the GPS chip is shared, so two managers never drew double power. Recorded under #5 because that's where the shortlist tracked it.

See [[battery]] for the shortlist this closes.

## 2026-08-13 — Long-form output goes in the vault; dated session notes get their own folder
**Decision:** Long explanations — session briefings, investigations, plans, option menus — are **written into the vault**, not delivered as terminal output. The terminal reply is reduced to a short summary plus a pointer to the note. New folder `projects/HootOwl/sessions/` holds dated session notes named `YYYY-MM-DD-<topic>.md`. First note: [[2026-08-13-session-start]]. Jim also encouraged creating folders freely rather than piling new content into existing files.
**Why:** Jim's request, verbatim: *"I prefer you to write long statement into Obsidian for me to read, you can organize them into folders too."* The terminal is not his reading surface — long output scrolls away, isn't searchable later, and doesn't survive the session. The vault is what he actually reads and what the next session loads at START.
**Why a separate folder rather than growing `CURRENT.md`:** [[CURRENT]] must read as *current*. Accumulating narrative inside it is precisely the mechanism that produced the stale Phase-3 and #5 claims corrected in the 2026-08-07 reconciliation — a status note that has become a journal stops being trustworthy as status. Dated session notes are append-only and can't become wrong later, so they can be as long as they need to be. This is the same principle already recorded in [[decisions#2026-08-07-vault-correction-convention-fix-forward-looking-status-preserve-dated-entries]], applied to a new content type.
**Division of labour across the vault:**
- `projects/HootOwl/sessions/` — dated briefings, investigations, long-form reasoning. **Immutable after writing.**
- [[CURRENT]] — short, current-state-only. Overwritten as things change. Now carries a pointer callout to the sessions folder.
- [[battery]], [[onboarding]], [[cyclops-first-run]] — standalone topic notes, updated **inline as work happens** (existing convention, unchanged).
- [[decisions]] / [[bugs]] — atomic entries, newest at top.
**Alternatives considered:**
- Keep writing long summaries to the terminal and let the vault hold only structured notes — rejected, this is the behaviour Jim asked to change.
- Put session briefings in `CURRENT.md` — rejected per the drift argument above.
- One rolling `sessions.md` file instead of one file per session — rejected; it would grow unbounded and lose the property that each note is a self-contained snapshot readable on its own.
**Impact:** No code. New folder `projects/HootOwl/sessions/` + first note; pointer callout added near the top of [[CURRENT]]. Saved to auto-memory as `feedback-longform-to-obsidian`.
**Tooling note:** MCP `create-note` stalled past 120s writing the first session note and had to be `TaskStop`ped; the note was written with the normal file tools instead. Reads via MCP were fine in the same session. **Writes are the stall-prone MCP operation** — go straight to direct file access for creates/edits, and `mkdir -p` parent folders yourself. Recorded in auto-memory `feedback-obsidian-mcp-config`.

## 2026-08-07 — Cyclops 🕐 fix sequencing: verify assumption + device run before any edit
**Decision:** The Cyclops first-run 🕐 bug was traced to root cause, but **no code was changed**. Fixes are gated behind two checks, in this order: (1) confirm `MncplParkItemAvail.parkId` carries the same `tpe_`/`ntpc_` prefix the watchList uses (`CyclopsModel.swift:112`); (2) one fresh-install device run to see whether the clock clears after ~15–20s or genuinely never. Only then apply the two one-liners.
**Why:** Static reading proves a **≥16s** blank window on any cache-less launch. It does **not** prove the reported *"forever"*. Shipping the fix and closing the bug without the device run risks declaring victory over 16 seconds while an indefinite stall (a `minuteFlow` bail-out at `Mu1Base+Ext.swift:144–177`) survives. Jim also chose to read the code himself before edits.
**The two staged fixes:**
- **Immediate `minuteFlow()` at the end of `activate()`** (`Mu1Base+Ext.swift:15–49`), mirroring what `resumePolling()` already does at `:78`. One line.
- **`allFencesVbj.send(enclosing)` → `activeFencesVbj.send(enclosing)`** (`Municipal+Ext.swift:135`). One word.
**Why fix #2 now despite being latent:** nothing currently reads `activeFencesVbj` for activation, so it does no damage today. But it *destructively narrows* the full fence list — a user outside all fences collapses `allFencesVbj` to `[]`, after which every `assessFences` throws `.noFences` permanently. It is a landmine directly under the planned multi-city expansion, and would surface as *"the new city doesn't work."* Cheap insurance.
**Alternatives considered:**
- Apply both fixes immediately and move on — rejected; would likely mask rather than resolve, and Jim wanted to review first.
- Fix only the clock and leave the fence typo — rejected; one word now vs. a confusing regression later.
- Treat it as a first-run-only cosmetic issue — rejected once the 24h cache expiry (`Municipal+Cache.swift:47`) showed it recurs routinely for episodic parking use.
**Impact:** No files changed. Full investigation: [[cyclops-first-run]]. Bug entry: [[bugs#2026-08-07-cyclops-shows-on-every-cache-less-launch-investigated-not-fixed]].

## 2026-08-07 — Fence-driven zone activation is an open design decision, not a patch
**Decision:** `ActDeActOnes(ids:)` (`Municipal+Ext.swift:165–175`) has **zero callers** and `activeIds` at `:158` is computed and discarded — the fence→activation link its own comment promises was never wired. **Do not wire it opportunistically.** Log it as an open decision and settle the activation policy deliberately.
**Why:** Turning it on changes *which zones fetch for whom* — a behavioural change with correctness, coverage, and battery consequences. It is not a bug fix. Wiring it while `Municipal+Ext.swift:135` is still broken would immediately break users outside covered fences.
**Current behaviour:** all protos activate unconditionally via `loadedProtos.map({ $0.activate() })` at `Municipal+Ext.swift:43`, so every user polls every zone regardless of location.
**Cost of leaving it:** (a) works against the #1/#6/#9/Phase-3 battery wins and **confounds the deferred Energy Impact measurement** — some measured drain is zones the user isn't in; (b) cost is linear in cities — tolerable at two, meaningful at six, plus multiplied load on public open-data endpoints that may rate-limit.
**Open questions to settle before implementing:** what activates a zone when location is unknown or permission is denied? Does a user near a boundary keep both zones warm? Is there a manual override for someone checking a destination city remotely?
**Sequencing:** fix `Municipal+Ext.swift:135` first — fence-driven activation is unsafe until `activeFencesVbj` is actually populated.
**Impact:** No files changed. Context: [[cyclops-first-run]] (Finding 3); confound warning added to [[battery]]'s measurement log.

## 2026-08-07 — Vault correction convention: fix forward-looking status, preserve dated entries
**Decision:** When vault notes drift from reality, correct **status and forward-looking claims** in place, but leave **dated journal/decision entries as originally written**. Record the discrepancy in a dated reconciliation section rather than editing history.
**Why:** Dated entries are a record of what was known and true on that date. Silently rewriting them destroys the ability to reconstruct how a decision was reached, and makes the notes untrustworthy in a subtler way than being out of date. Status claims, by contrast, are read as *current* and are actively harmful when stale — `CURRENT.md` telling the next session that Phase 3 was uncommitted would have caused real re-tread.
**Applied 2026-08-07/08 after verifying against `git log`:** Phase 3 committed `aa6b02a` (not uncommitted); #9 committed `04e2165` (not uncommitted); #5 target is `Municipal.swift:127` + `:169` (not 122/160 — file shifted); HEAD is `860f82d`, not `61eec92`.
**Impact:** [[CURRENT]] rewritten; [[battery]] status + option table + shortlist corrected, with a `[!info]` callout and a dated **Reconciliation — 2026-08-07** section; [[decisions]] defer-list line numbers; auto-memory `project_battery_drain.md` + `MEMORY.md` index hook (both would otherwise have re-seeded the error into future sessions). Dated Decision-log entries in [[battery]] left untouched by design.

## 2026-07-12 — Onboarding copy + feedback + ratings strategy
**Decision:** Author the 3-page onboarding flow (the `hootowl/UI/onboard/` swipe framework) as **parking-only**, **playful owl-mascot voice**, **no app name baked into copy**, with **freshness-honest** wording, plus a **compliant ratings/feedback loop** that decouples App Store ratings from feature requests. Full living copy in [[onboarding]].
**Why:** First-run is the only surface most users actually read ("nobody reads docs" — Jim), so it must be tight and do the persuasion + permission-priming + expectation-setting all at once, without over-promising.
**Key sub-decisions:**
- **Scope = parking only.** Bus tracking exists but is not sold in onboarding. Launch = Taipei + New Taipei (80/20); expansion is *maybe*, gated on feedback — so coverage copy is present-tense and honest ("Now live: Taipei & New Taipei"), never a promise.
- **Coverage limitation reframed as a request:** "Not your city yet? Tell me where to fly next →" turns "we don't cover you" into user agency + a demand signal.
- **No app name in user-facing copy.** "HootOwl" is a working name that will likely change and will have a *very different* Chinese name. Owl voice never says the name, so it survives a rename. Use `{APP}` placeholder only if a name slot is unavoidable. Saved to auto-memory as [[app-name-is-a-placeholder]].
- **Voice = owl mascot** (nocturnal, watchful, smug, privacy-respecting in character). Playful OK per Jim.
- **Freshness honesty (important):** never claim a fixed cadence. Rejected "Fresh numbers, every minute" — the source (city open data) publishes every ~2–5 min and publish timing is beyond us. Chosen: "Always the latest count / I grab each lot's newest numbers the moment the city publishes them" + owl aside "As fresh as the source allows." Protects against bad-faith "this is fraud" complaints and aligns with the in-app "Updated"/DQI timestamp.
- **Location screen** pre-primes benefit + privacy right before the system dialog ("Only while you're here — I don't follow you home"), which is literally true (`WhenInUse`, no `UIBackgroundModes`).
**Ratings/feedback — rejected vs. chosen:**
- **Rejected (Jim's initial instinct):** suggest 5-star, collect city requests inside the App Store review, prioritize cities for 5-star reviewers, and state this in onboarding. This violates App Store rules — you can't steer users to 5 specifically, must use the native review sheet (can't preset stars), and **can't offer incentives/priority in exchange for reviews** (incentivized/gated reviews). Reviews are also a poor request inbox (no private reply/follow-up). Documenting the deal in onboarding would be evidence for rejection.
- **Chosen (decouple the two goals):** (1) Ratings via native `@Environment(\.requestReview)` / `SKStoreReviewController` at a **win moment** (e.g. 3rd time a pinned lot shows spaces), **never in onboarding**; no custom text, no preset stars. (2) City/feature requests via an **owned channel** (mailto → later a form), captured in Jim's inbox. (3) Prioritize cities by **counting demand**, not by star rating, then **close the loop** ("You asked for Taichung — it's live") which earns 5-stars honestly. Settings gets "Request a city", "Send feedback", and a neutral "Rate the app". Saved to auto-memory as [[app-store-ratings-and-feedback-policy]].
**Impact:** No code yet — copy + strategy only. When implemented: `hootowl/UI/onboard/` (`LandingScreen`/ob0, build out `ob1`/`ob2`), a `Localizable.xcstrings` batch (English + blank 中文), a feedback transport (mailto/form), the `requestReview` win-moment trigger, and Settings entries.
**Status:** copy drafted, awaiting Jim's final headline-lane pick + the xcstrings batch. See [[onboarding]] for the living copy and open TODOs.

## 2026-06-25 — scenePhase pause/resume handler (Phase 3 — #2 + #3)
**Decision:** Pause GPS and the active protos' daily/minutely timers on `scenePhase == .background`, and resume them (plus one immediate availability fetch) on `.active`. `.inactive` is a deliberate no-op. Implemented per all four recommended answers from the 2026-06-24 pre-implementation brief: (1) `ReceiptObs.timer` left running, (2) immediate refresh on `.active` = yes, (3) wiring = direct calls from App root, (4) #2 + #3 shipped together. Closes the foreground-idle drain window (screen dimmed, app still foreground, GPS + timers running until iOS suspends ~5–30s; no `UIBackgroundModes` declared).
**Why:** The drain hypothesis is foreground-idle, not true background. #1 (GPS accuracy) and #6 (timer tolerance) reduced the per-tick cost; Phase 3 eliminates the wasted ticks entirely while the app is backgrounded. Pairs with Phase 2's cache: cold/resumed launches now seed from disk *and* kick an immediate live fetch on `.active`.
**Scope narrowed vs. the 2026-06-24 brief — only the Municipal-owned live path is touched (GPS + the active protos `TaipeiObs` / `NewTaipeiCityObs`).** The brief had proposed also adding pause/resume to `CyclopsObs` and `SourceBase`; on implementation both were deliberately left out:
- `CyclopsObs` drives the debug `CyclopsScreen2` and `Zone2 SourceBase` drives `ZoneRetrieveScreen` — both are view-local, only tick while their screen is visible, and are **not reachable from the app root**, so there's no handle to pause them from the lifecycle handler.
- Cyclops *display* refresh is driven by `parkInfoVbj` / `parkAvailVbj`, so pausing the proto timers already stops the cyclops network work indirectly.
**Alternatives considered:**
- Tear down on `.inactive` — rejected. `.inactive` fires transiently for alerts / Notification Center pull-down / multitasking; tearing down there causes thrash. Only `.background` tears down.
- NotificationCenter broadcast or a central `AppLifecycle` observable (brief options b/c) — rejected per recommendation (a). Phase 1b already made `Municipal` the central orchestrator; one `.onChange` covers GPS + the active protos' timers.
- Pause `ReceiptObs.timer` too — rejected (decision #1). Left running so StoreKit purchase retries can still validate during the brief background-before-suspension window; cost is a few timer fires.
- Skip the immediate `.active` refresh and let the next regular tick handle it — rejected (decision #2). Even with Phase 2's cache softening staleness, a resume fires one immediate fetch so counts are live, not up-to-a-minute old.
- Split #2 and #3 into separate changes — rejected (decision #4). They share the same handler; splitting doubles scaffolding for marginal safety.
**Implementation:**
- **New file** `hootowl/Municipalities/framework/Municipal+Lifecycle.swift` — `pauseForBackground()` (calls `stopUpdateLocation()`, then `activeProtos.forEach { $0.pausePolling() }`) and `resumeForForeground()` (calls `startUpdateLocation()`, then `activeProtos.forEach { $0.resumePolling() }`). Both log via `ffl(…,.info)`. File header documents the scope-narrowing rationale.
- `hootowl/Municipalities/framework/Mu1Proto.swift:72-76` — added `pausePolling()` / `resumePolling()` to the `Mu1Proto` protocol (default impls in `Mu1Base+Ext.swift`), so the lifecycle handler can iterate `activeProtos` generically.
- `hootowl/Municipalities/framework/Mu1Base+Ext.swift` — `pausePolling()`: `dailyTimerSubscription?.cancel()` + `minutelyTimerCancellable?.cancel()` then `minutelyTimerCancellable = nil` (so `setMinutelyTimer()`'s nil-guard re-creates it on resume); does **not** touch `isActive`/fence state; idempotent for rapid background→foreground cycles. `resumePolling()`: guards `isActive` (skips if inactive), then `startTimerRetrievDaily()` + `setMinutelyTimer()` + `Task.detached { await minuteFlow() }` for the immediate fetch.
- `hootowl/App/hootowlApp.swift` — added `@Environment(\.scenePhase) private var scenePhase` and a `.onChange(of: scenePhase)` on the root scene: `.active → municipal.resumeForForeground()`, `.background → municipal.pauseForBackground()`, `.inactive → break`, `@unknown default → break`.
- Immediate-refresh path uses the existing `minuteFlow()` (not `Repository.shared.netRetrieve(...)` as the brief had guessed) — `minuteFlow()` is the proto's own availability-fetch entry point.
**Idempotency / races:** `pausePolling()` is safe to call twice (double `?.cancel()` is harmless). `resumePolling()` is safe because the timer-start helpers already begin with `?.cancel()` (de-dup pattern). The `isActive` guard in `resumePolling()` prevents resuming a proto that was never started.
**Defer-list:** Phase 4 (Layer B2 — cyclops trail history persistence) and #5 (dedupe `self.locationMan = CLLocationManager()` at `Municipal.swift:127` + `:169` — line numbers re-verified 2026-08-07, previously recorded as 122/160) remain not started, both deferrable to post-launch.
**Validation:** Working tree only — **not committed**. New file `Municipal+Lifecycle.swift` is untracked; `hootowlApp.swift`, `Mu1Base+Ext.swift`, `Mu1Proto.swift` modified. Manual test plan before commit:
- Background for 30s → foreground → counts refresh visibly (immediate fetch fires).
- Lock → unlock quickly → no thrash, no torn-down state.
- Tap an alert / pull down Notification Center (`.inactive` fires) → nothing tears down.
- App switcher → return → GPS + timers resume.
- Force-quit + relaunch → clean cold-start path (no scenePhase fires; Phase 2 cache seeds).

See [[battery]] partition plan; supersedes [[battery#2026-06-24--phase-3-pre-implementation-brief-asked-jim-awaiting-answers]].

## 2026-06-24 — Disk cache for cold-launch / jettison recovery (Phase 2 — Layer B1)
**Decision:** Persist the latest user location and per-municipality `MncplParkAvPack` snapshot to `Library/Caches/hootowl-snapshot.json`. On Municipal init (before `wireCyclops()`), seed the in-memory `parkAvPack` dict and `userLoc2dVbj` from cache if the snapshot is < 24h old. Phase 2 of the battery investigation partition plan; entirely additive (no UI change, no behavior change for warm-starts).
**Why:** Phase 1b fixed warm switches (state survives view re-mount). But cold launches and post-jettison resumes still show empty cells because `parkAvPack` starts empty and the first availability fetch takes ≥1s. With cache, the user sees real numbers immediately; fresh data fades in seconds later. Foundation for Phase 3's `.active` re-read story.
**Alternatives considered:**
- `@AppStorage` / UserDefaults — rejected. Apple discourages larger blobs (parkAvPack can be 10-50KB per municipality); semantically wrong (this is regenerable cache, not preferences).
- `Library/Application Support/` — rejected for now. Survives iOS purges under storage pressure, but the data is regenerable and a parking app on a low-storage device has bigger problems than a re-fetch.
- Cache `actParkInfos` (static daily data) too — deferred. Large, changes rarely, daily timer re-fetches on next foreground tick. Separate decision.
- Write only on `.background` — rejected. Simpler to write on every update (one small write per minute); survives crashes; cost is negligible.
- Stale threshold of 1h / 7d instead of 24h — 24h chosen per Jim's call. Aligns with "user opens HootOwl ~once a day" intuition; tunable later if numbers feel stale or refreshes feel wasteful.
- Staleness badge UI — deferred per Jim's call. Cache infrastructure ships clean; badge ships later once Jim has felt the actual age distribution in real use.
**Implementation:**
- **New file** `hootowl/Municipalities/framework/Municipal+Cache.swift` — `wireCacheAndSeed()` (called from Municipal.init), `noteAvailabilityChanged()` (hook for actMinutely), `wireLocationPersistence()` (throttled 30s userLoc2dVbj sink), `writeSnapshot()`, `seedFromCache()`, `cacheFileURL()`. Plus `CachedSnapshot` + `CachedLocation` envelope types.
- `hootowl/Municipalities/framework/ParkAvailv02.swift` — added `Codable` to the `MncplParkItemAvail` and `MncplParkAvPack` struct declarations directly. Originally written as one-line empty extensions in `Municipal+Cache.swift`, which Xcode rejected: Swift only auto-synthesizes `Codable` when the conformance is declared in the same file as the type. Corrected 2026-06-24 in response to Jim's first compile pass. All members were already primitive Codable types, so no further work needed.
- `hootowl/Municipalities/framework/Municipal.swift:110` — `actMinutely(p0:)` ends with `noteAvailabilityChanged()` to persist on every availability update.
- `hootowl/Municipalities/framework/Municipal.swift:131` — init calls `wireCacheAndSeed()` *before* `wireCyclops()` so the cyclops Combine pipeline sees the seeded data on its first refresh.
- Disk format example: `{ "written": ..., "location": { "lat": ..., "lng": ..., "captured": ... }, "packs": [ { "converted": ..., "published": ..., "municipal": "tpe", "items": [{"parkId": ..., "cars": ..., "chargers": ...}, ...] }, ... ] }`. Written via `Data.write(to:options:.atomic)` to avoid torn-file reads.
- `cacheMaxAge: TimeInterval = 24 * 60 * 60`. Stale snapshots are silently discarded (logged at `.info`).
- `locationWriteThrottle: TimeInterval = 30`. The userLoc2dVbj sink uses Combine's `.throttle(for:scheduler:latest:)` to coalesce rapid GPS updates into one write per ~30s.
**Defer-list:**
- Staleness badge UI (`MncplCyclopsScreen` infoBar augmentation, `MncplAllScreen` row badging) — separate change, requires Jim's visual call + Localizable.xcstrings entries.
- `actParkInfos` (static daily data) caching — separate decision.
- On-`.active` re-read trigger — slots into Phase 3 (`scenePhase` handler). Currently the seed only happens at init (cold launch).
**Validation:** Working tree only, not committed. Pre-existing SourceKit index noise unchanged; the new file inherits the same `Cannot find type 'MncplParkItemAvail' / 'MncplParkAvPack' / 'Municipal' in scope` noise that all Municipal-area edits trigger this session, and downstream `Codable conformance` diagnostics are caused by those misses (not real issues). Manual test plan before commit:
- Cold launch with cached data present: verify counts appear immediately (no flash of empty) and refresh from network shortly after.
- Cold launch with no cache file: verify silent no-op, then normal first-fetch flow.
- Set system clock forward >24h, relaunch: verify cache is treated as stale (no seed), then normal first-fetch flow.
- Move the device significantly between launches: verify last cached location is used briefly until GPS gives a fresh fix.
- Pin/unpin during use: verify cache is written on next `actMinutely` tick (not lost on next launch).

See [[battery]] partition plan for context.

## 2026-06-17 — Cyclops state lifted to Municipal singleton (Phase 1b — Layer A)
**Decision:** Move `cyclopsMod`, `availableTime`, and `watchList` from `MncplCyclopsScreen`'s `@State` onto the `Municipal` `@Observable` singleton. `MncplCyclopsScreen` becomes a thin view that reads from `municipal.*` via `@Bindable` and pushes watchlist edits through `municipal.setWatchList(_:)`. This is Phase 1b of the battery investigation partition plan.
**Why:** The pre-fix `MncplCyclopsScreen` held all display state in `@State`, including the trail-bearing `cyclopsMod`. SwiftUI loses view identity when the host re-renders — `AppTabView` hosts tabs via dynamic `ForEach(AppScreen.sorted(subTier:))` and an auto-hide tab bar that re-renders body every 5s — wiping `@State` to defaults. The result was the user-visible "screen goes empty on quick switch out/in" bug. Lifting display state to the singleton eliminates the dependency on view identity entirely. Background: [[swiftui-state-and-identity]] in the patterns vault.
**Alternatives considered:**
- New `@Observable CyclopsBuilder` class injected separately — rejected per Jim's call: keeping it on `Municipal` is one fewer file, one fewer environment injection, and the cyclops concerns are already coupled to Municipal's data flow.
- Leave `watchList` on the view (`@AppStorage`-backed already survives @State reset) — rejected per Jim's call: consolidate the source of truth on Municipal even though it doesn't strictly need to move. Cleaner data flow and simpler future cache logic in Phase 2.
- Refactor `MncplAllScreen` at the same time — deferred. MncplAllScreen doesn't have the bug (it reads `municipal.actParkInfos` / `parkAvPack` directly). Its existing `@AppStorage saveWatchList` write pattern routes through UserDefaults, which Municipal now observes — so cross-screen pin/unpin keeps working without modification.
**Implementation:**
- **New file** `hootowl/Municipalities/framework/Municipal+Cyclops.swift` — `wireCyclops()` (called from Municipal init), `refreshCyclops()`, `setWatchList(_:)`, `loadWatchListFromStorage()`, `reloadWatchListIfChanged()`. Subscriptions stored in the existing `Municipal.cancelBag`. UserDefaults observed via `NotificationCenter.default.publisher(for: UserDefaults.didChangeNotification)` so writes from any screen flow into Municipal.
- `hootowl/Municipalities/framework/Municipal.swift:76-79` — added 3 stored properties: `cyclopsMod: CyclopsModel = .Zero`, `availableTime: Date? = nil`, `watchList: [String] = []`.
- `hootowl/Municipalities/framework/Municipal.swift:130` — added `wireCyclops()` call at the end of init.
- `hootowl/Municipalities/UI/MncplCyclopsScreen.swift` — rewritten. Removed `@State cyclopsMod`, `@State watchList`, `@State availableTime`, `@State cancellables`, `wire()`, `unwire()`, `loadWatchList()`, `refreshCyclops()`. Body reads `municipal.*` directly. `@Bindable var bindable = municipal` for `CyclopsView`'s `@Binding<CyclopsItem>` requirement. Reorder sheet extracted to `fileprivate struct ReorderSheet` with a local mutable list + push-on-edit via `municipal.setWatchList()`.
- `MncplAllScreen.swift` — unchanged.
**Validation:** Working tree only, not committed. Pre-existing SourceKit index noise unchanged; none of the diagnostics reference the new code. Manual test plan to run before commit:
- Open Cyclops with at least one pin → wait for parking counts to load.
- Switch to another tab → return within 5 min → counts should still be visible (the bug).
- Switch to another tab → wait > 5s (auto-hide tab bar trigger) → return → counts should still be visible.
- Background the app → return after a minute → counts should still be visible.
- Reorder sheet: move and delete should still persist across sessions.
- `MncplAllScreen` swipe-to-pin/unpin should still work, and the change should reflect in Cyclops immediately (Municipal observes UserDefaults).

See [[battery]] partition plan and [[swiftui-state-and-identity]] for the underlying SwiftUI behavior.

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
