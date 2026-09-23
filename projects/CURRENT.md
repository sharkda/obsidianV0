# Current Project Context

Active focus across projects. Update at session END.

---

> [!important] 🔁 Claude: check [[data-sources]] at session START
> The municipal contact details in the Gist are scraped from open-data portals and point at named individuals, so they rot silently. **Re-check when the "last checked" date there is over ~30 days old, and always before a release. This is my job, not Jim's.** Next due: **2026-10-09**.

> [!important] 🗺️ Lost? [[INDEX]] maps the whole HootOwl folder
> Which note answers which question, and where each finding was filed. Added 2026-09-10.

> [!important] 🚀 Releasing? Read [[release-strategy]] first
> TestFlight-vs-straight-to-release, the order of operations, and the reviewer-in-California problem that is the likeliest rejection. Added 2026-09-10.

> [!important] 👉 Your action list is [[jim-actions]]
> Everything waiting on **you** — Gist edits, device tests, decisions, App Store Connect — in one short note, tickable one at a time. Added 2026-09-07.

> [!important] Operational how-to and the **release checklist** live in [[operations]]
> Anything you change **outside the code** — the contact Gist, the tutorial video, contact phone/email — is a step-by-step runbook there, with exact URLs and how to check it worked. [[operations#2-release-checklist]] is the single list of everything that must be true before submitting. Added 2026-09-07.

## Active project
**HootOwl** — SwiftUI iOS/macOS app for Taiwan urban mobility (real-time bus + parking).

> [!tip] Long-form reading lives in `projects/HootOwl/sessions/YYYY-MM-DD/`
> This note stays short and current-state-only. Every session gets its own **dated working folder** — created by default, no need to ask — holding that day's briefings, investigations, and extended reasoning as numbered notes (`00-` is always the where-we-left-off note). Append-only, never edited after the fact.
> Most recent: [[sessions/2026-09-20/00-state-of-play|sessions/2026-09-20/]]. Convention: [[decisions#2026-08-31-every-session-gets-a-dated-working-folder-created-by-default]].
> **Anything older than two days lives in `sessions/older/`** (2026-09-17) — the top level shows only what is current. Wikilinks resolve by note name, so the move breaks nothing.

> [!success] ✅ The macOS update is behind us — **re-verified 2026-09-17**
> Xcode did **not** change (27.0 / 27A266a / Swift 6.4), so the 09-15 verification stands. All five builds pass and the app was run on the simulator: no launch crash, fences load, coverage flips `outside` ↔ `covered`. The standing rule still holds for next time — a toolchain upgrade expires every build verification written down here: [[swift-patterns#a-toolchain-upgrade-expires-every-build-verification-you-have-written-down]].

> [!important] 💻 **On a different machine? Start at [[working-agreements]].**
> Claude Code's own memory is local to one laptop and does not sync with this vault, so a second instance starts blind without it. It carries how Jim works, the project conventions that are invisible in the code, the verification standards, and **the rule that a wrap-up pushes both repos** — this vault *and* `sharkda/hootOwl`.
>
> **It also covers what differs per machine.** The **vault is standardised at `~/obsidianV0` everywhere** (Jim's call, 2026-09-20), so `CLAUDE.md` is correct on both Macs. The **app repo's location still differs**, which is fine — every command runs from `git rev-parse --show-toplevel`. The one thing that does not sync is **`.claude/settings.local.json`**: it is gitignored, and without it every vault write stops for approval. → [[working-agreements#paths-differ-per-machine]]

👉 **Resuming? Start at [[sessions/2026-09-20/00-state-of-play|sessions/2026-09-20/00-state-of-play]].** Every open item in one table, with a stable ID per row, checked against the repo rather than copied from these notes. The 09-15 handoff and its re-verify commands are still at [[sessions/2026-09-15/02-pick-up-here|sessions/2026-09-15/]].

**`main` = `origin/main` = `42ed13b`. Working tree clean. Both repos pushed 2026-09-23.**
✅ **`destination-mode` is merged — it ships in build 1.** Jim's call: *"we need to let our potentional users test the app before they are in the zone."* Twelve commits, fast-forward; all four configurations build on `main` and a clean out-of-zone first run reaches the picker with the three default pins seeded. Outside Taipei the app no longer refuses: it asks *"where are you heading?"*, and choosing a city makes everything work from there. Five rounds of Jim's testing have since added service-area awareness, auto-search on settle, a 0.004 sweet-spot zoom, and a camera that survives tab switches. **Reversible by construction** — with no destination set, `effectiveCentre` *is* the GPS fix, so the old path is the default path. Each commit reverts independently; `git checkout main` drops all of it. → **[[destination-mode]]**

> [!tip] 🔄 Picking this up again
> **Nothing needs restoring — both repos are pushed.** `git checkout destination-mode` in the app repo and carry on.
>
> **The simulator was wiped deliberately on 2026-09-22** (iPhone 18 Pro, `2DEBB183`) so Jim could see a genuine first run: no preferences, no cached data, location pre-granted, sitting in Cupertino. The first launch will download data rather than seed from cache — that *is* the first-run experience.
>
> **If the update brings a new Xcode, every "it builds" claim here expires** — the standing rule. Re-run the four builds and run the app: [[operations#3-building-and-testing]].
Latest: the **AdMob SDK went 13.3.0 → 13.10.0** (`5d4d794`). Checksum matched Google's published value, signature is team `EQHXZ8M8AV` as the project pins, **no source change was needed**, all four configurations build, and a test banner loaded on the simulator (`🟢 bannerViewDidReceiveAd`). How it is wired and how to do it again: **[[admob-sdk]]**.
`55197b4` is Jim's own *"sep20"*, committing an Xcode rewrite: the 09-16 `Info.plist` → build-settings migration redone, plus a whole-file `.xcstrings` reformat. **Audited before it landed: no string content changed across 338 keys, `sub_terms_of_use` intact, and the deployment target was NOT touched this time.** The only loss is the export-compliance comment block; the declaration itself survives as a build setting.
**Session of 09-18 — no code written, three things settled.** Privacy policy round 3: the last 🔴 on the page closed, and Jim deleted the dead terms sentence. That question exposed a real one — **there is no Terms of Use anywhere**, so **E-28** (a `termsOfService` link in both subscription screens, ~4 lines each) is now **the last compliance item that must be inside the binary**, and it blocks the re-archive. Then: *how does a reviewer in California check the app?* — **no code needed**, the All tab is not location-filtered, so the app already works anywhere; the notes just have to say *type `TPE` in capitals*. That turned up `tpe` → 0 matches, promoting Jim's June search bug to **R-21**.

**09-19: E-28 landed (`327bf08`)** — both subscription screens now offer Terms of Use beside the privacy policy, pointing at Apple's standard EULA. **R-05 closes with it and R-01 is unblocked.** Wiring it found that `SubscriptionStoreScreen` was **never** unreferenced, so a live English-only string had been sitting in a shipping screen for eleven days behind a wrong "dead code" note.

**09-19 also closed R-21 (`9285a47`)** — search was case-sensitive, so `tpe0155` matched **0 of 1,773** lots while `TPE0155` matched one. Jim's June bug, and urgent because the review notes now tell reviewers to type `TPE`. Measured over the live feed rather than reasoned about; the Chinese terms are unchanged.

**09-19 also answered the California reviewer question properly.** No code needed: the map screen's address search calls `search(mapMode: .mapTap, loc0:)`, which has **no reference to the user's location** and biases to Taiwan — verified against the live geocoder, and **English resolves** (`Taipei 101` → 25.0336, 121.5648). So a reviewer types an address and sees the real map with live pins. The review notes were rewritten to lead with that; the All tab is the second route. A *"Preview Taipei"* button was considered and **rejected as unnecessary**. → [[sessions/2026-09-19/02-reviewer-scope-and-testing|02]]

**Next: R-01 (archive and upload), then R-20 (paste the review notes).** Every release blocker is Jim's; nothing is waiting on me — today's audit closed the last 🔴 that was mine (R-12, already shipped 09-15).

**The open scope gap is R-10:** the App Store **description is unwritten**, and it is the only place a reviewer learns the coverage before installing. The name says *TW*; the app covers **Greater Taipei**. The cities belong in the opening clause, as the subtitle does it.

Carry into the device pass (R-14): confirm **both** policy buttons render in the Subscribe sheet (never seen — this Xcode ships no Simulator.app), and type `tpe` in the All tab.

## State (2026-09-15 — merged, and the toolchain moved under us)

👉 **Start at [[01-session-wrap|sessions/2026-09-15/]].**

**`main` is at `fb28765`, seven commits ahead of `origin/main`. Nothing is pushed.** Working tree clean. `icon-replacement` merged as a fast-forward; `backup/icon-replacement-pre-fold` deleted as planned.

```
fb28765  Explain what the app shows outside its coverage area
88c5b4b  Make the geofence test correct and the fence data decodable
2c3dbb4  Stop applying .commands on iOS, which crashed the app at launch
391d784  Fix a FanceMapView01 init that Swift 6.4 rejects
a4a005b  Delete the dangling ConcaveHull package reference
98f1253  ← icon-replacement merged here
```

> [!warning] **Xcode 26.6 → 27.0 happened between 09-14 and 09-15, and it expired every build verification in this vault.**
> Two hard failures, neither caused by an edit: a **Swift 6.4 definite-initialization error** in a file untouched since March, and — far worse — **the app could not launch at all**. `.commands { #if os(macOS) … #endif }` leaves iOS an *empty* `@CommandsBuilder` closure; it compiles silently and SwiftUI cannot resolve the witness, so the binary aborts in `AppGraph.init(app:)` before drawing. The 09-14 Archive contains that binary.
> **Consequence: that archive is dead. Re-archive before uploading.** Patterns: [[swift-patterns#an-empty-result-builder-closure-is-a-runtime-crash-not-a-no-op]], [[swift-patterns#a-toolchain-upgrade-expires-every-build-verification-you-have-written-down]].

**The empty state shipped** — the rejection I would have bet on is closed. `Municipal.coverage` is one state read by every screen (`locating` / `denied` / `outside` / `waiting` / `covered`); it answers only "is there anything to show, and if not, why", leaving **age** to `AvailFreshness`. Outside coverage names the cities and offers the city request; staleness keeps the numbers visible with a banner rather than blanking them. Open-data attribution rides along on Options. 16 strings, English and 中文. [[decisions#2026-09-15-coverage-is-one-state-on-municipal-and-it-never-answers-questions-about-age]]

**Building it exposed that the geofence system has never run on iOS** — three independent faults, each sufficient alone: the `fences/` folder was only in **`hootmac`'s** Resources phase; the bundled JSON predates `IdWgs.carCap` so it could not decode; and `convexEnclosing` does its geometry on **`Int`-truncated** degrees, which places Banqiao inside Taipei. Plus the long-recorded `allFencesVbj.send` bug, which turns out to *erase* the fence list rather than narrow it whenever the user is outside coverage — the App Review case exactly. All fixed. [[bugs#2026-09-15-the-geofence-system-has-never-run-on-ios-fixed]]

**Verified by running it.** iPhone 17 Pro simulator, round trip: Cupertino → `coverage locating → outside` and the card appears; Taipei 101 → `outside → covered`, card gone, live pins with real counts. iOS Debug, iOS Release and `hootmac` Release all build clean. **Not visually checked:** the `.denied` state and the two list screens.

**One thing waiting on Jim:** the outside-coverage ask line renders only when a city-request destination is configured, and the Gist has none. **Updated later the same day — it no longer has to be an email**: the config now takes `support.url` (hosted form or page, preferred) as well as `support.email`, with the URL winning, and requests carry `?src=onboarding` / `?src=coverage` so demand can be attributed to the screen that produced it. Recommendation is a Wix form; a Facebook page works only if it describes *this* app. [[decisions#2026-09-15-a-city-request-goes-to-a-url-not-a-mailto]] Today the screen degrades to *"We're not here yet / Right now we cover Taipei and New Taipei"* — honest, but the city-request payoff is missing. That Gist item now gates two screens.

**Later the same session (into 09-16):** a long product thread on where a city request should go, ending with `support.url` in the remote config (URL beats mailto; requests carry `?src=onboarding` / `?src=coverage`). Landed: **no custom domain is needed** — the free `jimhsuyc.wixsite.com` site already hosts the privacy policy the app ships, and a contact form / Messenger link on it *is* the relay Jim wanted, so no personal address is ever published. Facebook can be the user-facing channel but **cannot replace email entirely** — ASC's App Review Information requires a contact address; use a dedicated mailbox. `facebook.com/tataroApp` is not usable until it describes *this* app rather than Bopomofo. [[decisions#2026-09-16-no-custom-domain-the-relay-is-a-form-on-the-site-that-already-exists]]

**Privacy policy is mid-revision, two rounds reviewed.** Round 2 closed the location gap; **three findings remain open**, and the top one got *worse* — the policy now contradicts its own ATT prompt two paragraphs apart. Everything, including a table of what the app actually does with data verified against the source, is in [[privacy-policy]].

**Next:** ① ~~push~~ done; ② **re-verify after the macOS update** (see the callout above); ③ **re-archive** — the 09-14 archive cannot launch — and upload; ④ finish the privacy policy; ⑤ decide the city-request destination, then one line in the Gist; ⑥ the device pass, now including the coverage states.

## State (2026-09-11→14 — the first Archive, and everything it shook loose)

👉 **Start at [[01-session-wrap|sessions/2026-09-11/]].** The briefing that opened it: [[00-resume-here|sessions/2026-09-11/]].

**`main` is untouched at `5048976`. All work is on branch `icon-replacement` (6 commits).** Working tree carries **one uncommitted change** as of 2026-09-14: the `ConcaveHull` removal in `project.pbxproj` (13 lines deleted).

```
98f1253  Stop tracking .DS_Store
5eef4fc  Delete the legacy app icon sets
7ab9cf0  Adopt an Icon Composer icon and point both targets at it
eaf1acb  Strip the alpha channel from the legacy app icons
85e4a45  Fix three Release-only breakages that Debug never compiled
```

Each commit reverts independently; the deletion touches nothing else. Safety ref at `backup/icon-replacement-pre-fold` — delete once merged.

**The plan was the empty state. It did not get written.** The first Archive was attempted instead, failed, and kept failing in different ways — which was the better use of the time.

**Three Release-only compile errors**, all in the `#else` half of an `#if DEBUG` — code no Debug build had ever type-checked. Plus a **near-miss that would have shipped**: the first fix set `debugForceAd = true` in Release, which would have forced ads on for **paying subscribers**. It would have compiled. The compile errors were the lucky ones.

**The app icon took two failures.** `ITMS-90717` blocked the upload (all 20 icons had alpha; the 1024 was 26% transparent). Replaced with `FindParkingTw.icon` via Icon Composer — and the replacement **silently did nothing**, because adding a `.icon` file does not make it the icon. Everything about icons now lives in [[app-icon]].

**Theme:** *the tooling you use every day does not exercise the thing you are about to ship.* Conditional compilation, asset validation and the icon setting all fail without a warning, and all three are found by doing the real thing. Consequence, now written down: **archive early** — uploading is not submitting, and an Archive is the only thing that type-checks half your conditional code. [[operations#2d-archiving-and-distributing--2026-09-11]]

> [!success] **Compile-verified 2026-09-14** — this caveat is now closed for iOS
> An Archive requires a successful **Release** build, and `hootowl 2026-9-14, 5.38 PM.xcarchive` was built two days after the last source change on this branch (`ContentView.swift`, 09-12 16:43). It carries `CFBundleIconName = FindParkingTw`, which exists **only** on `icon-replacement` — so it was built from the branch, in Release, successfully. **All three `#if DEBUG` fixes and the icon wiring are proven.**
> **Still unproven: the `hootmac` target.** An iOS archive says nothing about whether macOS compiles, and `hootmac` had its own icon set that now shares the `.icon` file.

**Next:** ~~① confirm `hootmac` compiles~~ — **done 2026-09-14: Debug and Release both `** BUILD SUCCEEDED **`.** Getting there required deleting a **dangling `ConcaveHull` package reference** that had blocked every command-line build since June and was misdiagnosed in this vault as a network/`Package.resolved` problem — it is uncommitted in the working tree, see [[bugs#2026-09-14-a-dangling-concavehull-package-reference-blocked-every-command-line-build]]. **`xcodebuild` now works on this project.** Then ② `git checkout main && git merge icon-replacement`, then delete the backup ref; ③ upload — the `Upload Symbols Failed` warning is expected forever and unfixable ([[operations#the-upload-symbols-failed-warning--ignore-it-permanently]]) — **every App Store Connect field is drafted and paste-ready in [[app-store-connect]]** (new 2026-09-14 — the one page for all ASC copy); ④ **then the empty state**, still the highest-value remaining code task and still the likeliest rejection. Its two design calls are **still unanswered** — see [[00-resume-here|sessions/2026-09-11/]].

## State (2026-09-10 — named, localised, and out of code-blocking work)

**`origin/main` is current. Working tree clean.** 👉 Start at [[01-session-wrap|sessions/2026-09-10/]].

**The app has a name: `Find Parking TW` / `找車位`**, localised in `InfoPlist.xcstrings` so English and 中文 differ deliberately. That closed the last user-visible English in a Chinese build — both system permission prompts are localised, and the three stale names (`Park-Chia`, `車停對`, "Hootowl uses your location…") are gone.

**Map pins now fade with age** — the map had no freshness concept at all, which was the Cyclops disease in a purer form. Alpha carries it (0.9 / 0.7 / 0.45) on the same 5- and 30-minute thresholds, reusing `AvailFreshness` and `Municipal.lastConfirmed`.

**Three bugs this session shared one shape:** something true once that quietly stopped being true — a banner selling a capability removed in June, a permission string naming a permission no longer requested, and a boolean that meant "fetched at some point" and never expired. All found by looking at the running app, not by reading code. Patterns in [[swift-patterns]].

**Nothing is blocked on code now.** What remains is the Gist (`support.email`, real tutorial video), App Store Connect (name, subtitle, availability, subscription 中文, privacy labels, screenshots, age rating), a device pass and a TestFlight pass — plus two product questions: whether a subscription should do more than remove ads, and what a user sees when the feed is down (currently nothing). 👉 [[jim-actions]].

**Six commits since the last Xcode build** (`016f852`, 09:12). Everything before that is compile-verified and was seen running; the six since are parse-checked only.

## Previous state (2026-09-08 — onboarding, ads and subscriptions shipped to `main`)

**`origin/main` = `37a39f8`.** Six commits, built clean in Xcode on the first attempt and pushed. Working tree clean.

**Onboarding is no longer the release blocker** — all three screens exist and carry the final copy. Also landed: the Gist-backed remote config now serves the support inbox and the tutorial video (both changeable with no release, and decoding degrades field by field); ATT asks for IDFA on the second launch; the app finally has a `PrivacyInfo.xcprivacy`; and the `.entitle` tab shows a real subscription screen instead of `EntitledView`'s receipt dump, with tier two removed entirely.

**What is left is not code.** 👉 [[jim-actions]] is the single list: the Gist still holds `example.com` placeholders (a user can dial a fake number), the 中文 pass on ~30 new strings, App Store Connect availability set by hand to Taiwan/US/Japan/HK/Macau, and the device checklists. Operational how-to and the full release checklist: [[operations]].

**One open product question:** a subscription currently changes nothing except turning off ads — on iOS every tier gets the same tabs. The copy is honest about that now, but if subscribers were meant to get more, that gating was never built.

## Previous state (session 2026-09-05/06 — Cyclops done; onboarding is the only blocker left)

**Everything is committed and pushed.** `origin/main` = `43ac0a0`, working tree clean, nothing unbuilt. Seven commits over three days.

**The Cyclops "grey numbers" arc is closed** — it was never a colour bug. The numbers had not been updating for a long time and nobody could see it, because a stale parking number is indistinguishable from a quiet car park. Attaching a freshness clock made the failure loud. Four bugs came out of it (one mine, three pre-existing), then the All-screen keyboard trap (open since 2026-06-15), a fresh-install watch-list disagreement, and a three-card layout off-by-one. All fixed and tested on device.

**Cyclops first-run now works out of the box:** landmark defaults (台北101 / 大安森林公園 / 府前廣場) from a single source on `Municipal`.

**Still unexplained:** why `@Observable` invalidation doesn't reach `MncplCyclopsScreen` on device. `14ceac7` routes around it. **Three screens now carry the same workaround**, so it's structural — `AppTabView`'s dynamic `ForEach` is the suspect. Not blocking; deserves its own session.

**Next:** **onboarding is the only release blocker.** Lane 3 copy is final in [[onboarding]]; the immediate action is the `Localizable.xcstrings` batch, which needs no decision. Then wiring ob0/ob1/ob2. Everything else outstanding is verification (two device checklists) or hygiene (`@MainActor` before the next city).

👉 **Resume from [[01-resume-here]]** — full handoff, including what I got wrong so it isn't re-derived. Standing list: [[unfinished]].

## Previous state (session 2026-08-31 — Cyclops freshness colouring added)

**Working tree now carries two uncommitted, unbuilt changes:** battery #5 (`Municipal.swift`, from 2026-08-20) and the new **Cyclops cache-freshness colouring** (4 files). Both need one Xcode build — the CLI still can't compile this project (`Package.resolved` gitignored → SPM re-resolves `ConcaveHull` over the network).

Cyclops numbers now colour by age of the backing feed: `<5 min` unchanged, `5–30 min` `.primary`, `≥30 min` `.secondary`. Derived from `MncplParkAvPack.converted` (already cached — no new persistence), per-lot, ticked by `TimelineView(.everyMinute)`. **One deviation awaiting Jim's call:** spec said "white", implemented as `.primary` so it isn't invisible in light mode. Full write-up: [[01-cyclops-cache-freshness]]; decision: [[decisions#2026-08-31-cyclops-availability-freshness-is-derived-from-mncplparkavpackconverted-never-from-the-trail]].

Adds one item to the owed device run: force-quit, wait >30 min, relaunch → numbers should appear grey then flip to `.fern` within ~15s.

## Previous state (session 2026-08-20 — #5 applied; battery shortlist closed)

**First code change since 2026-07-03.** #5 (`CLLocationManager` dedupe) applied to the working tree — one line deleted from `wire0()` in `Municipal.swift`, plus a WHY comment. The app now creates exactly one `CLLocationManager`. **Not committed and not compile-verified** — build it in Xcode before trusting it; the CLI can't build this project (gitignored `Package.resolved` → SPM tries to re-resolve `ConcaveHull` over the network). Detail + caveat in [[battery]], atomic entry in [[decisions#2026-08-20-cllocationmanager-dedupe-battery-5]].

**That closes the pre-release battery shortlist.** All five picks (#1, #6, #9, #2+#3, #5) are implemented. Nothing left to *build*; what remains is verification — the owed Phase 3 device test and the deferred, still-confounded Energy Impact measurement.

**Also logged:** `CLAUDE.md` / `AGENTS.md` claim `MncplParkItem` IDs carry `tpe_`/`ntpc_` prefixes. **No code does this** — the helper has zero callers. That doc line is what seeded the 2026-08-07 "unverified assumption" scare. New entry in [[bugs]]; the instruction files are Jim's to correct.

**Previous state (2026-08-17 status reset)** — HEAD `860f82d` (2026-07-03), tree otherwise clean; every code claim in the vault re-grepped against source and all held.

This session verified the vault a level deeper than 2026-08-13: each battery and Cyclops claim was checked against the working tree source, not only against commit history. **Everything held** — see the table in [[battery#re-verification--2026-08-17]]. Full briefing: [[2026-08-17-status-reset]].

**One real advance: the `parkId` gate is cleared.** The check that was blocking the whole Cyclops plan was run. Neither side of `CyclopsModel.swift:112` carries a `tpe_`/`ntpc_` prefix — the prefix helper (`MunicipalEnum.swift:44–48`) has **zero callers**, and both `MncplParkItemAvail.parkId` and `MncplParkItem.id` pass raw feed IDs straight through. Raw-to-raw, no mismatch. **The plan does not reorder; Finding 1 is still the main cause.** The only gate left before the two one-line fixes is the device run. Residual to eyeball there: the `TPE####` hardcoded watchList seeds (`MncplAllScreen.swift:47`).

Small corrections applied to [[bugs]] (2 stale entries), [[battery]] (#1's line ref `:163` → `:172`), [[cyclops-first-run]] (assumption cleared). **#5's target lines `Municipal.swift:127` + `:169` re-verified exact — unchanged.**

**Everything below is carried forward from the 2026-08-07 → 08-13 sessions and is still accurate.**

> [!abstract] Previous session (2026-08-07 → 08-08)
> No code changes either. Investigation + documentation: traced the Cyclops 🕐 bug to root cause, found two further bugs on the way, corrected stale status across the vault. Produced [[cyclops-first-run]] (new), plus updates to [[bugs]], [[battery]], [[decisions]] (3 entries), [[swift-patterns]] (2 patterns).

> [!info] Corrected 2026-08-07
> The previous version of this note (2026-07-12) said Phase 3 was *"implemented, still uncommitted, awaiting device test"* and gave #5's target as `Municipal.swift:122` + `:160`. Both were wrong. Verified against `git log`:
> - **Phase 3 is committed** — `aa6b02a` (2026-06-26), including `Municipal+Lifecycle.swift` and the `project.pbxproj` target-membership fix.
> - **Last commit is `860f82d`** (2026-07-03), not `61eec92`.
> - **#5's target is now `Municipal.swift:127` + `:169`** — the file shifted.
>
> **Working tree is clean** apart from an untracked `AGENTS.md`. Repo has been idle since 2026-07-03.

**All four pre-release battery picks (#1, #6, #9, #2+#3) are implemented and committed.** Only #5 (trivial `CLLocationManager` dedupe) remains from the shortlist, plus the deferred post-launch measurement.

**Phase 3 was committed without the device test.** Not a blocker anymore (it's in), but the behaviour is still unverified: background/foreground refresh, lock/unlock no-thrash, `.inactive` no-op, app-switcher resume.

**Onboarding copy** — drafted in [[onboarding]] (3 screens, parking-only, owl-mascot voice, no app name, freshness-honest) plus a compliant ratings loop. **Copy only — no code yet.** `hootowl/UI/onboard/` is still the 2024 scaffolding (`LandingScreen.swift`, `OnboardScreen.swift`, `OnboardTab0.swift`, `UserGuide.swift`). Decision: [[decisions#2026-07-12-onboarding-copy--feedback--ratings-strategy]].

Commit chain:
- `860f82d` 2026-07-03 — 4-line touch to `OnboardScreen.swift`. **← HEAD**
- `aa6b02a` 2026-06-26 — Phase 3 (#2+#3) scenePhase pause/resume + target-membership fix.
- `61eec92` 2026-06-24 — Phase 2 (Layer B1) disk cache.
- `2d5eb13` 2026-06-23 — sync (post Phase 1b).
- `392fa82` 2026-06-18 — sync (post Phase 1b initial work).
- `04e2165` 2026-06-16 — #9 / macOS auth split / dead-code cleanup.
- `837cbef` 2026-06-15 — #1 + #6 + cleanup waves.
- `08c5816` 2026-06-13 — first cleanup wave (Obs-framework dedup).

## Where we are in the battery partition plan

Full plan + status lives in [[battery]]. Quick map:

| Phase | What | Status |
|---|---|---|
| #1 — GPS Best → HundredMeters | mechanical at 5 sites (reduced to 1 by cleanup) | ✓ committed `837cbef` |
| #6 — Timer.publish tolerance | 5 active sites + cleanup waves | ✓ committed `837cbef` |
| #9 — Drop Always-auth + Info.plist cleanup | iOS escalation removed, macOS preserved | ✓ committed `04e2165` |
| 1 (Layer A) — Cyclops state → Municipal singleton | `Municipal+Cyclops.swift`; thin view | ✓ committed |
| 2 (Layer B1) — Disk cache for cold-launch / jettison | `Municipal+Cache.swift`, 24h stale threshold | ✓ committed `61eec92` |
| 3 (#2 + #3) — scenePhase handler | pause GPS + proto timers on `.background`, resume + immediate `minuteFlow()` on `.active` | ✓ **committed `aa6b02a`** (device test still owed) |
| 4 (Layer B2) — Cyclops trail history persistence | optional / deferrable | not started |
| 5 — Dedupe `CLLocationManager` at `Municipal.swift:127` + `:169` | delete the `:169` assignment, keep the config lines | not started |

## Cyclops 🕐 bug — investigated 2026-08-07, no code changed

Jim's backlog item 2026-06-29 ("cyclops keeps the clock forever until kill and restart") was traced. Full write-up: [[cyclops-first-run]]. Summary:

- **Not a first-run bug.** The 🕐 opens on any launch without a usable cache — including **cache older than 24h**, which is routine for episodic parking use.
- **Main cause:** `activate()` starts a 15s timer but fires no immediate fetch, while `resumePolling()` does (`Mu1Base+Ext.swift:78`). Cache-less launch = **≥16s of clocks, guaranteed**. Relaunch looks instant because `seedFromCache()` fills `parkAvPack` synchronously in `Municipal.init`.
- **Two more bugs found:** `Municipal+Ext.swift:135` sends enclosing fences to `allFencesVbj` instead of `activeFencesVbj` (destructively narrows the fence list, unrecoverable without relaunch); and the fence→activation link (`ActDeActOnes`) was never wired, so every proto polls for every user regardless of location.
- **Still unproven:** the ≥16s window is certain; *"forever"* is not. Needs one fresh-install device run.

Fix sequencing was made an explicit decision (verify assumption → device run → then edit): [[decisions#2026-08-07-cyclops-fix-sequencing-verify-assumption-device-run-before-any-edit]]. Fence-driven activation logged as an open design decision, deliberately not patched: [[decisions#2026-08-07-fence-driven-zone-activation-is-an-open-design-decision-not-a-patch]]. Two reusable patterns extracted: [[swift-patterns#starting-a-poller-must-also-fire-one-immediate-fetch]] and [[swift-patterns#combine-send-to-the-subject-you-meant-especially-in-cold-start-branches]].

## Open bugs

- [[bugs]] 2026-08-07 — Cyclops 🕐 on cache-less launch. Open, investigated, not fixed.
- [[bugs]] 2026-06-15 — IME blocks UI on All-screen search. Open, deferred.

## Next steps (when Jim resumes)

**Recommended first move (updated 2026-08-20):** #5 is applied and the `parkId` grep is done, so **one device sitting now clears everything that's outstanding** — fresh install, run the Cyclops 🕐 checklist and the owed Phase 3 checklist together, and build #5 in Xcode while you're there. After that the only open item is the activation-policy design decision.

**Cyclops bug (Jim is reviewing the code himself before any edit):**
- [x] ~~Verify the unchecked assumption first~~ — **done 2026-08-17, cleared.** Neither side is prefixed; the `tpe_`/`ntpc_` helper has zero callers. No mismatch, plan unchanged. See [[2026-08-17-status-reset]].
- [ ] One fresh-install device run — does the clock clear after ~15–20s or never? Capture `🐎 minutelyAvailable`, `📦 minutely Received`, `📛 <512bytes`, `previousHash not changed`.
- [ ] Then apply: immediate `minuteFlow()` in `activate()` (one line) + `allFencesVbj.send` → `activeFencesVbj.send` (one word).
- [ ] Decide fence-driven activation policy — design decision, log in [[decisions]], don't patch blind.

**Battery — shortlist now fully implemented; only verification left:**
- [x] ~~#5 dedupe at `Municipal.swift:127` + `:169`~~ — **done 2026-08-20.** Working tree, **not committed, not compile-verified** (see below). Decision: [[decisions#2026-08-20-cllocationmanager-dedupe-battery-5]].
- [ ] **Build once in Xcode** to confirm #5 compiles. CLI `xcodebuild` can't run here — `Package.resolved` is gitignored so SPM re-resolves `ConcaveHull` from the network and fails. Pre-existing, unrelated to the edit.
- [ ] Device-test Phase 3 behaviour (already committed, still unverified).
- [ ] Post-launch Energy Impact measurement — **control for the unconditional all-zone polling first**, or the reading is confounded. See the warning in [[battery]].

**Onboarding (see [[onboarding]] for full TODO):**
- [ ] Jim to pick the final screen-1 headline lane (currently playful owl).
- [ ] Produce `Localizable.xcstrings` batch (English filled, 中文 blank). Note: `hootowl/Localizable.xcstrings` already exists.
- [ ] Wire strings into `LandingScreen` (ob0) + build out `ob1`/`ob2`.
- [ ] Decide feedback transport (mailto first vs. hosted form); implement `requestReview` win-moment trigger + Settings "Request a city" / "Rate the app".

## Open questions / blockers
- None blocking. Cyclops fix is paused on Jim's own code review + one device run. Onboarding needs Jim's headline pick and a go-ahead to produce the xcstrings batch.
