# HootOwl — Unfinished

Standing list of things deliberately left undone. **Not** a bug list ([[bugs]]) and **not** a decision log ([[decisions]]) — this is "we knowingly stopped here and must come back."

Newest at top within each section. Delete an item when it's genuinely done, don't just tick it.

> [!info] Release-blocking items that need **Jim** live in [[jim-actions]], not here. This note stays engineering-side.

---

## 🔴 Must do before commit / release

### ~~Strip the temporary diagnostics~~ — done 2026-09-05 (`c6e758f`)
All four markers (`🎨` `🏠` `🦵` `🪟`) removed, and the log levels raised on 09-02 restored. Deletions only; the `@State items` + `uiKickSbj` fix and the freshness clock are untouched. Tested on device before commit.

**Worth keeping from this:** `ffl` routes `.debug`/`.info` through `print()`, which only exists while the Xcode debugger is attached. To observe anything on a real device, use `.notice` or above — that goes to OSLog and shows in Console.app. This cost most of a day when device logs went silent while the simulator looked fine.

### ~~Build + commit the stacked changes~~ — done 2026-09-04
Committed as three commits and **pushed to `origin/main`** (`b069eb2`, `4f6dfd2`, `14ceac7`), split by layer so each compiles standalone:
1. freshness clock (`converted` → `lastConfirmed`) + the main-thread hop
2. `@Binding` → value across all six `CyclopsView` call sites
3. `@State items` + `uiKickSbj` explicit invalidation

Battery #5 turned out to be already committed in `f069086 Aug31a`.
**Still true:** the CLI can't build this project (`Package.resolved` gitignored → SPM re-resolves `ConcaveHull` over the network), so verification remains Xcode-only.

### ~~Jim's call: `.primary` vs literal white~~ — **decided 2026-09-06: keep `.primary`.**
Spec (2026-08-31) said the 5–30 min freshness state should be **white**; it shipped as `.primary`. Jim confirmed `.primary` after the evidence: the app sets `preferredColorScheme` **nowhere** (grep returns zero hits), so it follows the phone's Light/Dark setting, and the only forced dark is `MncplCyclopsScreen.swift:164` while `pinningScreen` is on. Literal white would therefore be invisible on a Light-mode phone everywhere else, and in Dark mode `.primary` already resolves to near-white — so nothing is lost. Applies to both `AvailFreshness.heroColor` (`CyclopsModel.swift:72`) and the onboarding headlines (`LandingScreen.swift:106` and the two new screens).

---

## 🟡 Owed verification

- [x] ~~**Launch-hang test**~~ — **done 2026-09-05, no hang.** Daily transform ran in full (`WgsNoPre` 1417 + 1756, ~3,173 lots) with the `ffl` threshold back at 4, log continuous, no stall. The hang was my own 09-02 threshold change enabling per-item `.debug` logging on the launch path; the revert fixed it. See [[01-launch-hang]].

- [x] ~~**Freshness stale path never exercised**~~ — **covered 2026-09-01 (logs6) and again 09-04:** a 3.7 h cache showed STALE → grey, then recovered to normal once a fetch landed. Working as designed.
- [ ] **Phase 3 device test** — committed `aa6b02a` (2026-06-26) without ever being run. Background/foreground refresh, lock/unlock no-thrash, `.inactive` no-op, app-switcher resume.
- [ ] **Cyclops 🕐 checklist** — does the clock clear after ~15–20s or never, on a cache-less launch. Capture `🐎 minutelyAvailable`, `📦 minutely Received`, `📛 <512bytes`, `previousHash not changed`.
- [ ] **Post-launch Energy Impact measurement** — still confounded: `ActDeActOnes` has zero callers, so every proto polls for every user regardless of location. Control for that first or the number means nothing.

---

## 🟢 Queued — subscription reach (2026-09-08)

- [x] ~~Subscribe button in the toolbar of the major screens~~ — **done 2026-09-08 (`9b87c1c`).** Top-left on All/Nbs/Options, top-right on Cyclops (`infoBar` owns top-left), sheet not tab switch, hides once subscribed.
- [x] ~~Subscription as onboarding screen `ob3`~~ — **dropped on purpose.** The offer is weakest exactly there: nothing is unlocked, and the user has not seen an ad yet. Replaced by a one-line mention (`onb_ads_note`) on the last onboarding screen. Reasoning: [[tasks#ob3-was-dropped-deliberately]].
- [x] ~~Pick the subscribe icon~~ — **`creditcard.circle`, icon + label, decided 2026-09-08.** Shared by the tab and the toolbar button via `SubscribeAffordance.icon`.
- [ ] **Eyeball the toolbar on device** — icon + label is wider than icon-only, and on `MncplAllScreen` and `NbsScreen` the search field sits in `.principal` right next to it. If it squeezes the search field, `.labelStyle(.iconOnly)` on that one screen is the fix.

## 🟠 Found but not chased (from the 2026-09-01 logs)

> [!danger] ⚠️ **2026-09-24 — this stopped being theoretical.** The app aborted on every clean launch once the second city's daily feed landed: `actParkInfos[p0.mncplt] = p0` died inside `Dictionary._Variant.setValue` with `doesNotRecognizeSelector`, the selector hitting a different random type each run. `dailyVbj` publishes off-main and `actWire`'s sink mutated `Municipal` from there. Patched at the boundary (`80a792a`) — **all three `actWire` sinks now hop to main** — but the structural item below still stands, and the note's own words were right about why. [[bugs#2026-09-24--municipal-mutated-off-the-main-thread-the-app-aborted-on-the-second-citys-feed-fixed]]

- [ ] **Mark `Municipal` `@MainActor` — before the next municipality is added.** Audit done 2026-09-02: **all four `fetch(...)` sink sites now hop to main correctly**, so there is no live bug. (My earlier claim that `SourceBase.swift:180` was unhopped was wrong — that's the `fetch` *definition*; its call site at `:103` hops fine.) The risk is structural, not present: the hop is a per-call-site convention with **zero enforcement**, and `minuteFlow()` lost it by being copy-pasted from a sibling that had it. Every new zone adds another flow written the same way. `@MainActor` turns a silent runtime failure into a compile error. Do it standalone. Full reasoning + alternatives: [[00-why-municipal-should-be-mainactor]].
- [ ] **Move feed parsing off the main thread.** The `.receive(on:)` hop sits *before* the sink, so `JSONDecoder` decodes ~1,400 lots **on the main thread** every ~120s per active zone. Not a correctness bug; a hitch risk that grows with each municipality. Bigger refactor (the sink interleaves parsing, hash checks, timers, earcons, DQI). Do it when polling is next touched — and note it's directly relevant to the deferred Energy Impact measurement in [[battery]].

- [x] ~~**`fences` file missing from the app bundle.**~~ — **fixed 2026-09-15 (`88c5b4b`), re-verified 09-17.** It was one of three independent faults that meant the geofence system had never run on iOS at all. Both cities now deserialize at launch (taipei 13 points, newTaipeiCity 10) and `recomputeCoverage()` answers correctly on both sides of the border. See [[bugs]].
- [ ] **`▶️ app → active: resuming GPS + 0 active proto timer(s)`.** Phase 3's resume handler fires but finds **zero** active protos — resume may not be restarting polling at all. Check during the Phase 3 test.
- [ ] **New Taipei feed quality:** `noSignal:1001 / live:433 / coverage:30%`. 70% of NTP lots return −9. Product question (hide them? label them?) rather than a bug — lots of clown faces.
- [ ] **Duplicate parkIds in the NTP feed** (`060085`, `170120`, 11 total). Handled defensively (first-wins) in `CyclopsModel`, but the feed itself is wrong and other consumers may not be defensive.
- [ ] **`uiKick` hack in `MncplCyclopsScreen0000.swift`** — a forced-`.id()` workaround for the re-render bug that's now properly fixed. Likely removable; verify that screen is even still reachable first.

---

- [ ] ⚠️ **CORRECTED 2026-09-19: `SubscriptionStoreScreen` is NOT unreferenced.** It is live via `AppScreen.swift:89 → MncplCyclopsScreen → toolbar0 → ToolbarPrinciple → SubButtons → NavigationLink`. The 09-08 note was written from `AppScreen.swift:112`, where a *direct* call is commented out, and missed the toolbar route. **The cost was real:** its bare English `Link("Privacy Policy")` stayed English on a Chinese device for eleven days while this note said the screen was dead — fixed in `327bf08`. **`EntitledView` has not been re-checked the same way; do that before E-16 deletes anything.** [[sessions/older/2026-09-19/01-terms-of-use|the trace]]
- [ ] **`EntitledView.swift` is unreferenced** (2026-09-08, unverified since). Kept deliberately — `EntitledView` is a usable debug surface (receipt dump + tier state) and Jim asked for it to stay in the tree. If a debug entry point is ever wanted again, wire it somewhere `#if DEBUG`, not into a shipping tab.

## 🔵 Documentation / hygiene

- [ ] **`CLAUDE.md` + `AGENTS.md` claim park IDs are `tpe_`/`ntpc_` prefixed. No code does this** — the helper has zero callers. Cost a full investigation cycle on 2026-08-07. Jim's files to correct. See [[bugs#2026-08-20-claudemd-claims-park-ids-are-tpe-ntpc-prefixed-no-code-does-that]].
- [ ] **`CLAUDE.md` `fileprivate(set)` guidance** is right only for properties written **in the same file**. `Municipal` is written from four extension files, so it rarely applies there. Worth half a sentence.
- [ ] **Onboarding — all three screens now exist** (2026-09-06). Strings, ob0, ob1, ob2 and the feedback transport are all done; **onboarding is no longer the release blocker.** Left: the 中文 pass on the 17 new keys, and one device run of the flow. See [[00-onboarding-strings-batch]] · [[01-landingscreen-wired]] · [[02-ob1-ob2-built]].
- [ ] **Does the location dialog fire on screen 1 instead of screen 3?** `Municipal+Loc.swift:31-33` auto-requests on `.notDetermined` as soon as the location manager wires at launch, which would land the iOS prompt while the user is still on onboarding screen 1 — losing the pre-priming that screen 3 exists for. Design question, not a bug; screen 3 already handles the already-denied case. Check on the device run.
- [ ] **`onb_s1_body` hardcodes the live city list** ("Taipei and New Taipei City today — more cities soon", 2026-09-07). **When a third municipality ships, this string must be updated in en *and* 中文** or onboarding understates our own coverage on the first screen. Pair it with the `Municipal.loadOnStart()` change that adds the city. See [[onboarding#screen-1--what-it-is]].
- [ ] **Optional: add `"tutorial": "https://youtu.be/…"` to the same Gist** once a how-it-works video exists. Onboarding screen 2 shows a "Watch how it works →" button only while it is set, so there is nothing to do until then and nothing to remove if the video is retired. Built 2026-09-07; screenshots deliberately not used — see [[01-tutorial-video-and-screenshots]].
- [x] ~~🔴 **The contact Gist is still all `example.com` placeholders**~~ — **fixed 2026-09-09.** Both cities carry real values from their own open-data portals. The `support` placeholder was **deleted rather than replaced**, because a working button to a dead domain is worse than a hidden one — so what remains is not a placeholder but an unanswered question: where should "request a city" go. Tracked as **R-02**. See [[data-sources]].
- [ ] 🔴 **Add `"support": { "email": "…" }` to the contact Gist** — Jim's to do, outside the repo. **Promoted to a release item 2026-09-07:** screen 1's copy now *is* "tell us where you need it — we'll head there next", so without an address users read the offer and have nothing to tap. Gist: `ContactConfig.gistRawURL`. See [[00-req-taipei2Taiwan]].
- [ ] **`UserGuide.swift`, `OnboardTab0.swift` and `OnboardDebug.swift` are now unreferenced** (2026-09-06, when ob0/ob1 were rewritten). Deletion candidates. Nothing is lost — `OnboardDebug` was only `IapReceiptView()` + `OptionScreen()`, both reachable from `EntitledView.swift:68` and `AppScreen.swift:112` — **but if Jim used ob1 as a quick debug surface, that shortcut is gone.** Deleting also means removing their `project.pbxproj` entries (6 per file; see [[02-ob1-ob2-built]] for the exact shape).
