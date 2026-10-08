# State of play — 2026-10-08

> [!info] What this note is
> **One table, every open item, with a stable ID.** Carried forward from [[sessions/older/2026-10-05/00-state-of-play|2026-10-05]]. The IDs do not change — only **State** and **Moved** move, so an item cannot quietly disappear and "didn't we fix that?" has an answer.

**Repo:** `main` = **`b907798`**, working tree clean. `origin/main` was at `7afc3fa`; **today's commit is being pushed with this note.**
**Toolchain:** Xcode 27.0 / Swift 6.4, macOS 27.0.

**Since 10-05, three things closed and one opened:**

- ✅ **The floating restore pill** — the 10-05 open question. Jim: *"stop mirroring the tab entirely."* `7afc3fa`.
- ✅ **The App Store listing copy** — English and 繁體中文, all five fields, promotional text **option C** adopted in both languages. `R-10` is now screenshots + Jim's wording pass only.
- ✅ **Cyclops colour** — one green for every count; colour now means freshness and nothing else. `b907798`. **New today.**
- ❓ **D-07** — and that change opened a cross-screen question. See below.

---

# Where this stands, in plain words

**Nothing in code blocks the release.** `main` is shippable. What is left is Jim's: the 中文 wording pass, the device pass, then the archive and the App Store Connect fields.

## ✅ Closed today — the Cyclops hero number is one green

Jim, looking at a lot with plenty of spaces: *"that color is a bit like telling the data is out-dated, confusing."*

**He was reading the screen correctly, and the bug was exactly the one he described.** `CyclopsView.normalModeView` overrode the number's colour to `.primaryM` for **10–19 spaces only** — alone among the ranges, with 0–9 and 20+ both left green. `.primaryM` sits a shade from `.primary`, which is what `AvailFreshness.heroColor` returns for **aging** data. Two near-identical colours meant *"this lot has 10–19 spaces"* and *"this number is going stale."*

Jim's call — *"change them to green too"* — leaves the cell with one meaning per channel:

| Channel | Means | Values |
|---|---|---|
| **Colour** | **freshness** | fresh → `.fern` · aging → `.primary` · stale → `.secondary` |
| **Size** | **scarcity** | ×1.2 under 10 · ×1.1 for 10–19 and 20–99 · ×1.0 for 100–999 · ×0.6 over 1000 |

Nothing was lost — size already carried scarcity across the whole range, not one band in the middle. → [[decisions#2026-10-08--on-the-cyclops-cell-colour-means-freshness-and-nothing-else]]

> [!success] ✅ D-07 — opened by that change, and **closed the same day: accepted**
> **The map pins still encode scarcity in colour.** `CustomButton.badgeColor` is **maroon ≤3 / dodger >3**, with **alpha** carrying age (0.9 fresh / 0.7 aging / 0.45 stale). So from today the two surfaces use colour for different things: on the Cyclops cell colour means freshness, on a map pin it means scarcity.
>
> **I have not changed it, because the pin's constraint is real.** That badge is ~12pt on a potentially crowded map — it has no size channel to spare the way the Cyclops hero number does, and its own comment already reasons about this: *"colour on this badge already carries scarcity (maroon ≤3 / dodger >3) and no-signal (gray). A third meaning would collide."*
>
> So the honest options are:
> 1. **Leave it.** Accept that a pin and a list cell are different reading tasks — you scan pins for *which one*, you read a cell for *how many, and can I trust it*. Costs cross-screen consistency; costs nothing in use.
> 2. **Make the pin match** — one colour, with alpha for age and scarcity dropped or moved. Consistent, but deletes the at-a-glance "nearly full" signal that is the pin's whole job on a busy map.
> 3. **Make the cell match the pin instead** — i.e. undo today's change. Not recommended; it is the version Jim just rejected, for good reason.
>
> **Jim chose 1, agreeing with the recommendation:** *"map pin and cyclops serves different purpose, their differences are acceptable."* The reasoning now lives **in the code**, next to `CustomButton.badgeColor` (`06dc918`) — because the risk here was never a confused user, it was a future edit unifying an inconsistency that looked accidental and deleting the pin's "nearly full" signal in the process. Related: **E-19**, the same badge's alpha floor, still awaiting a device look.

## E-10 is closed

`Municipal` **and** `NbsObsM` are `@MainActor` (`319654b`). Two annotations; zero concurrency diagnostics of any severity across all four configurations; verified at runtime as well as compiled. Written up for a non-Swift reader in [[main-thread-explained]].

---

## Legend

| Column | Means |
|---|---|
| **ID** | Permanent. `R` release-blocking · `E` engineering · `J` needs Jim personally · `D` decision only Jim can make |
| **P** | 🔴 blocks release · 🟠 should ship with it · 🟡 wanted · 🐢 someday |
| **State** | `open` · `in progress` · `blocked` · `verify` (built, never run) · `done` |
| **Moved** | The date this row's State last changed |

---

## 🔴 Release-blocking

**Audited row by row against the repo, the live Gist and the live policy page — 2026-09-19.** Four rows were wrong; see *Table corrections* below.

*In the order I would do them. Every one of these is Jim's; nothing here is waiting on me.*

| ID | Item | Owner | State | Moved | Detail |
|---|---|---|---|---|---|
| **R-01** | **Re-archive and upload.** The 09-14 archive contains the `.commands` launch crash — it cannot start. Burn a build number. **Fully unblocked:** E-28 and R-21 are both in `origin/main` at `9285a47`. | Jim | **open — do this first** | 09-19 | [[jim-actions]] · [[app-store-connect]] |
| **R-20** | **Paste the App Review Notes.** Rewritten again today to lead with the **map**: a reviewer types `Taipei 101` into the address bar on the first tab and the map fills with live pins — **verified against the live geocoder**, English works, no simulator or faked location. The All tab is the second route. Opens with an explicit Greater-Taipei coverage statement. | Jim | **ready to paste** | 09-19 | [[sessions/older/2026-09-19/02-reviewer-scope-and-testing\|02]] · [[app-store-connect#34-beta-app-review-information--paste-ready]] |
| **R-14** | **Device pass.** The three onboarding screens · the mail link (hardware only) · ATT on 2nd launch · the Subscribe tab · coverage states (outside Taiwan, and location denied once). **Three new checks:** confirm **both** policy buttons render in the Subscribe sheet — E-28's one unverified part, since this Xcode ships no Simulator.app · **type `tpe` in the All tab** and watch ~1,700 lots appear · and **watch the Cyclops numbers actually move on device** after `319654b`. That last one is not paranoia: the 09-01 bug was `@Observable` invalidation going unreliable when state was mutated off-main, and it **behaved differently on device than in the simulator**. `319654b` changes exactly that machinery, in the right direction — but the one place this project has been bitten by device-only behaviour is the one place it touches. | Jim | open | 09-19 | [[sessions/older/2026-09-19/01-terms-of-use\|01]] |
| **R-02** | **City-request destination**, then one line in the Gist. **Re-checked today: the live Gist still has no `support` key at all** (`version: 5`, keys are `version`/`contacts`/`tutorials`). So the outside-coverage screen ends at a statement and onboarding's prompt has nothing to tap. Gates **two** screens. | Jim | open — **verified still missing** | 09-19 | [[operations#support--which-transport-and-why-url-wins]] |
| **R-06** | **Set availability manually in ASC.** Defaults to *all* territories, which drops you into the EEA with no consent platform. Set exactly: Taiwan, US, Japan, Hong Kong, Macau. | Jim | open | 09-10 | [[operations#gate-table--read-this-before-adding-any-territory]] |
| **R-07** | **Age-rating questionnaire** in ASC. Required, and nothing in Xcode mentions it. | Jim | open | 09-10 | [[jim-actions]] |
| **R-08** | **Traditional Chinese on the subscription product in ASC.** The local fix is done; ASC still has the `zh_CN`-not-`zh_Hant` problem, and that is the one real users hit. | Jim | open | 09-09 | [[bugs]] |
| **R-09** | **Privacy nutrition labels.** Evidence already gathered — precise location, app functionality, foreground-only, never tracking. | Jim | open | 09-10 | [[sessions/older/2026-09-09/00-location-privacy-audit\|location audit]] |
| **R-10** | **Screenshots + description.** ✅ **Description and keywords drafted 2026-10-05** — 1,707/4,000 and 58/100, paste-ready in [[app-store-connect#23-description--english--paste-ready]], with the basis for every claim and what was deliberately left unsaid. The opening sentence carries the coverage, which closes the scope gap. ✅ **中文 drafted 2026-10-06 — all five fields**, written as Chinese rather than translated, with the app's own vocabulary (§2.5). ✅ **Promotional text settled 2026-10-07** — option C, both languages, the one field that changes without a build. **Still owed: Jim's wording pass, and screenshots.** | Jim | open — **screenshots + 中文 pass** | 10-07 | [[app-store-connect]] · [[zh-review]] |
| **R-11** | **A TestFlight pass.** The only way to exercise sandbox purchases, the real ATT prompt, real ads, and the actual `tel:`/`mailto:` handoffs. | Jim | open | 09-10 | [[release-strategy]] |
| **R-13** | **Record the real tutorial video**, then set `tutorials.onboarding`. **Re-checked today: the Gist still points at the test clip** (`youtube.com/shorts/PG4CUrdkb6k`). **Downgraded from load-bearing to belt-and-braces** for review purposes — the map and list routes stand on their own — but still owed, and still the strongest single artifact for a geo-restricted app. | Jim | open | 09-19 | [[sessions/older/2026-09-19/02-reviewer-scope-and-testing\|02]] |

### Second machine — setup, not release

Neither blocks the release; both block the *other* instance from being useful.

| ID | Item | Owner | State | Moved | Detail |
|---|---|---|---|---|---|
| **M-01** | **Move the Air's vault to `~/obsidianV0`** — the same absolute path as here. Jim's call today: standardise rather than make every note path-agnostic. Makes `CLAUDE.md`'s vault line correct on both machines with no edit, and lets the settings file below be copied verbatim. | Jim | open | 09-20 | [[decisions#2026-09-20-the-vault-lives-at-obsidianv0-on-every-machine]] |
| **M-02** | **Create `.claude/settings.local.json` on the Air.** Gitignored, so it does not sync. Without it **every vault write stops for approval** and the "write it to Obsidian" convention is unusable. After M-01 it copies across verbatim. | Jim | open | 09-20 | [[jim-actions#second-machine--the-macbook-air]] |

### Privacy policy — open, but **not** release-blocking

All four re-checked against the live page today; all still present. None of these is a compliance risk any more — the 🔴 (the ATT contradiction) closed on 09-18 and Terms of Use closed on 09-19. **R-04 is the one worth doing**, because it is a false statement about the app in the first line a reviewer reads.

| ID | Item | P | Owner | State | Moved | Detail |
|---|---|---|---|---|---|---|
| **R-04** | **The headline claim is still Bopomofo's.** *"collects only 'name'"* opens *Information Collection and Use* and is **false for this app**. Worse: the opening paragraph lists `FindParkingTW` under *both* Commercial and Ad-supported, so the "paid edition lets you input a name" paragraph reads as applying here. | 🟠 | Jim | open — **verified still there** | 09-19 | [[privacy-policy#round-3--2026-09-18-after-jims-second-revision]] |
| **R-18** | **Retention still describes "the paid edition."** This app's concrete fact is better: the location cache is discarded after 24 h and goes when the app is deleted. | 🟡 | Jim | open — **verified still there** | 09-19 | [[privacy-policy]] |
| **R-19** | **Polish.** Name it `Find Parking TW` as the Store will (page says `FindParkingTW`) · delete the now-duplicated AdMob sentence · fix "personal identical" → identifiable and "that that you" · add an effective date · 中文 version. **All five re-checked today, all still present.** | 🟡 | Jim | open — **verified still there** | 09-19 | [[privacy-policy]] |

### Table corrections — what this audit found

| Row | Was | Actually |
|---|---|---|
| **R-12** | 🔴 open since 09-10, **owned by Claude** — *"the app credits the data sources nowhere"* | **The in-app half shipped four days ago** in `fb28765`. `OptionsScreen.swift:166` has a *Data source* section, with `opt_attribution_title` / `opt_attribution_body` translated in **en and zh-Hant**, naming both city governments and 政府資料開放授權條款－第1版. **Only the App Store description line is still owed → folded into R-10.** This was the last 🔴 with my name on it, and it was already done. |
| **R-04 · R-18 · R-19** | Filed **inside** the 🔴 Release-blocking table while carrying 🟠/🟡 priorities | Contradictory — a release-blocking table should hold release blockers. Moved to their own block above, which also makes the real point visible: **nothing about the policy page blocks release any more.** |
| **R-21** | Listed in the main table *and* in *Closed today* | Closed rows belong in *Closed* only, the way E-28 and R-05 were handled. Removed from the main table. |
| *order* | Scrambled — R-01, R-02, R-04, R-18, R-19, R-06, R-07… R-20, R-21, R-11 | Re-ordered into the sequence I would actually do them in. |

## 🟠 Should ship with it

| ID | Item | P | Owner | State | Moved | Detail |
|---|---|---|---|---|---|---|
| **E-01** | **Nothing tells a user when the feed is down.** No user-facing error state for a failed municipal fetch — counts just stay stale. For a *live numbers* app this is the likeliest "it doesn't work" review. **R-15 below makes this concrete.** | 🟠 | Claude | open | 09-10 | [[jim-actions]] |
| **R-15** | **Tell NTPC their bulk download is blocked.** 張先生 / `ae8131@ntpc.gov.tw` owns the catalogue entry, and there is already an open question for that bureau. Ask whether it was withdrawn or is a WAF misfire. | 🟠 | Jim | open | 09-17 | [[data-sources]] |
| **R-16** | **Confirm 02-29702960 is the right New Taipei destination**, and whether extension 8607 sits on it. One call settles both; either answer is a one-line Gist edit. | 🟠 | Jim | open | 09-09 | [[data-sources#the-phone--resolved-2026-09-09]] |
| **E-02** | **No crash visibility.** No Crashlytics/Sentry. Organizer shows only opted-in users, partial and delayed. Decide **before** launch. | 🟠 | Jim | open | 09-10 | [[jim-actions]] |
| **R-17** | **App Store listing in 繁體中文** — description, keywords, screenshots. Separate from the app's own strings. | 🟠 | Jim | open | 09-10 | [[jim-actions]] |
| **E-03** | **`TpeParkDescInfo.json` is missing from the iOS bundle.** Logged at every launch — **confirmed again in today's run**. Never investigated; likely the same missing-target-membership shape the `fences` folder had. | 🟠 | Claude | open | 09-17 | [[bugs]] |
| **E-04** | **Reject placeholder config values** — treat `@example.com` or `1234-5678` as absent so that class of mistake cannot ship. ~4 lines. | 🟠 | Claude | open | 09-07 | [[jim-actions]] |
| **E-05** | **Localise the two Info.plist prompts.** Location and tracking are English-only, so a Chinese-locale user reads English in both system alerts. | 🟠 | Claude | open | 09-10 | [[jim-actions]] |

## 🟡 Engineering — open

| ID | Item | P | Owner | State | Moved | Detail |
|---|---|---|---|---|---|---|
| **E-06** | **`ActDeActOnes` has zero callers** — *verified again today, only its own definition exists*. Every proto polls for every user regardless of location. Confounds any battery measurement. | 🟡 | Claude | open | 09-17 | [[battery]] · `Municipal+Ext.swift:179` |
| **E-07** | **Post-launch Energy Impact measurement.** Blocked by E-06 — control for it first or the number means nothing. | 🟡 | Claude | **blocked** | 09-17 | [[battery]] |
| **E-08** | **Phase 3 lifecycle device test.** Committed `aa6b02a` in June and never run. Watch for `▶️ app → active: resuming GPS + 0 active proto timer(s)` — **zero** means resume never restarts polling. | 🟡 | Jim | open | 09-10 | [[unfinished]] |
| **E-09** | **Cyclops 🕐 on a cache-less launch** — does the clock clear after ~15–20 s, or never. | 🟡 | Jim | open | 08-07 | [[cyclops-first-run]] |
| **E-10** | ~~Mark `Municipal` `@MainActor`.~~ ✅ **Done `319654b`** — `Municipal` **and** `NbsObsM`, two annotations, zero concurrency diagnostics of any severity left across all four configurations. | 🟠 | Claude | ✅ **done** | 09-29 | [[decisions#2026-09-29-municipal-and-nbsobsm-are-main-actor-isolated]] |
| **E-11** | **Feed parsing runs on the main thread** — ~1,400 lots decoded per zone per poll. A hitch risk that grows per municipality. Do it when polling is next touched. | 🟡 | Claude | open | 09-02 | [[unfinished]] |
| **E-12** | **`convexEnclosing` is integer-truncated and wrong.** ⚠️ **No longer inert** — *re-verified 09-29, `Int(next.longitude)` is still there and it now has **four** call sites, including `isInServiceArea` (`Municipal+Coverage.swift:128`)*. So the truncation now decides the search button's green/grey and whether a destination counts as covered. Masked in practice by the 1 km tolerance. | 🟠 | Claude | open — **raised** | 09-29 | [[unfinished]] · `Mu1Proto.swift:307` |
| **E-13** | **Duplicate parkIds in the NTPC feed** (11 today, `060085`, `170120`, …). Handled first-wins in `CyclopsModel`; the feed itself is wrong and other consumers may not be defensive. | 🟡 | Claude | open | 09-17 | [[unfinished]] |
| **E-14** | **`hoot_test_ui` does not build.** Proven pre-existing, no scheme, in no verification. Wire it or delete it — it blocks nothing. | 🐢 | Claude | open | 09-15 | [[sessions/older/2026-09-15/01-session-wrap\|09-15 wrap]] |
| **E-15** | **The privacy-policy URL is hardcoded.** Halved today: both screens now read `LegalLink.privacyPolicy`, so it is **one constant instead of two literals** — but it is still in the binary rather than the Gist, which is the actual item. | 🟡 | Claude | open | 09-19 | [[privacy-policy]] · `AppPid.swift:16` |
| **E-16** | **Delete four unreferenced files** (`UserGuide`, `OnboardTab0`, `OnboardDebug`, `EntitledView`) + their 6 pbxproj entries each. ✅ **All four traced on 09-29 and confirmed genuinely unreferenced** — each one's only call site is its own `#Preview`. That clears the E-29 caution, which was about `SubscriptionStoreScreen` specifically. **`OnboardDebug` was Jim's quick route to the IAP receipt and options screens**, and that shortcut goes with it. | 🐢 | Claude | **ready** | 09-29 | [[unfinished]] |
| **E-29** | **`SubscriptionStoreScreen` is NOT unreferenced**, contrary to the 09-08 note. It is live via `AppScreen:89 → MncplCyclopsScreen → toolbar0 → ToolbarPrinciple → SubButtons → NavigationLink`. Its bare English `Link("Privacy Policy")` was therefore **user-visible and stayed English on a Chinese device** — fixed in `327bf08`. **The lesson is the list, not the file:** the same 09-08 note calls `EntitledView` unreferenced, and that should be re-verified the same way before E-16 deletes anything. | 🟠 | Claude | **new** | 09-19 | [[sessions/older/2026-09-19/01-terms-of-use\|01]] |
| **E-17** | **`uiKick` hack in `MncplCyclopsScreen0000.swift`** — workaround for a bug now properly fixed. Likely removable; check that screen is even reachable first. | 🐢 | Claude | open | 09-01 | [[unfinished]] |
| **E-18** | **Toolbar squeeze on device** — Subscribe is icon + label next to the `.principal` search field on All/Nbs. If it squeezes, `.labelStyle(.iconOnly)` on that screen. | 🐢 | Jim | verify | 09-08 | [[unfinished]] |
| **E-19** | **Map pins fade with age** — 0.45 beyond 30 min. Judgement call on legibility over busy map detail; one number in `CustomButton.badgeOpacity`. **Now paired with D-07** — same badge, and if the pin's colour channel is ever reassigned this number moves with it. Look at both in the one device pass. | 🟡 | Jim | verify | 10-08 | [[jim-actions]] |
| **E-20** | **Dynamic Type** — fixed `.system(size:)` in onboarding/subscription. Mostly icons; the app name at 34 and 50 is what a large-text user notices. | 🐢 | Claude | open | 09-10 | [[jim-actions]] |
| **E-21** | **Two latent Swift-6-mode warnings** — `AVAudio.swift` attribute whitespace, `any Mu1Proto` existentials. Not urgent. | 🐢 | Claude | open | 09-15 | [[sessions/older/2026-09-15/01-session-wrap\|09-15 wrap]] |
| **E-22** | **Docs: `CLAUDE.md` / `AGENTS.md` claim park IDs are `tpe_`/`ntpc_` prefixed.** No code does this; the helper has zero callers. Cost a full investigation cycle once. Jim's files to correct. | 🟡 | Jim | open | 08-20 | [[bugs]] |
| **E-23** | **Docs: `CLAUDE.md` `fileprivate(set)` guidance** only holds for same-file writes. `Municipal` is written from four extension files. Half a sentence. | 🐢 | Jim | open | 09-10 | [[unfinished]] |
| **E-24** | **`onb_s1_body` hardcodes the city list.** When a third municipality ships this string must change in **en and 中文**, or onboarding understates coverage on screen 1. Pair it with the `loadOnStart()` change. | 🟡 | Claude | open | 09-07 | [[onboarding#screen-1--what-it-is]] |
| **E-25** | **Does the location dialog fire on screen 1 instead of screen 3?** `Municipal+Loc.swift:31-33` auto-requests as soon as the manager wires — which would land the prompt during onboarding screen 1 and waste screen 3's pre-priming. | 🟡 | Jim | open | 09-06 | [[unfinished]] |

## ❓ Decisions only Jim can make

| ID | Item | P | State | Moved | Detail |
|---|---|---|---|---|---|
| **D-01** | **Is there any reason to subscribe?** `AppScreen.sorted()` returns the same tabs for every tier — the only thing a subscription changes is the ad banner. If subscribers were meant to get more, that gating was never built. | 🔴 | open | 09-08 | [[sessions/older/2026-09-08/00-subscription-screen\|the finding]] |
| **D-02** | **New Taipei's −9 lots.** The portal explains it: those lots are **mid-operator-change**, not broken. Label them or hide them — labelling beats hiding, and the rate should fall on its own. | ❓ | open | 09-09 | [[data-sources#-this-dataset-answers-the-open-9-question]] |
| **D-03** | **Mainland China** — recommendation is drop it (ICP filing, AdMob blocked, wrong parking data). **HK + Macau have none of those problems** and already get 中文. | ⚠️ | open | 09-07 | [[operations#gate-table--read-this-before-adding-any-territory]] |
| **D-04** | **iOS 26.0 minimum** — worth pricing deliberately for a commuter utility, where some of the audience is on older hardware. *(Related: today something bumped this to 26.6 in the project file and it was reverted — E-26.)* | ❓ | open | 09-10 | [[jim-actions]] |
| **D-05** | **Full corrected privacy policy, English + 中文?** Offered twice, deliberately not written — it is Jim's document to own. Say the word. | ❓ | open | 09-16 | [[privacy-policy]] |
| **D-06** | **Watch early reviews for the ad-expectation line.** "There will be more of them over time" is deliberate pre-framing but can read as a threat. One string to soften. | ⚠️ | open | 09-10 | [[jim-actions]] |
| **D-07** | ~~Colour means two different things on two screens.~~ ✅ **Accepted, same day.** The Cyclops cell uses colour for freshness, the map pin for scarcity — *"different purpose, their differences are acceptable"*. Reasoning recorded at `CustomButton.badgeColor` so a later edit does not unify them. `06dc918`. | 🟡 | ✅ **done** | 10-08 | [[decisions#2026-10-08--the-map-pin-and-the-cyclops-cell-may-disagree-about-colour]] |

## 🐛 Jim's own backlog — not yet worked

*From [[Jim's backlog]]. These have had no investigation; they are listed so they stop being invisible.*

| ID | Item | State | Moved |
|---|---|---|---|
| **J-01** | ~~Search is case-sensitive — `TPE0155` works, `tpe0155` does not~~ | ✅ **fixed `9285a47`** — measured: `tpe0155` 0 → 1 match | 09-19 |
| **J-02** | Why is `0080` grey while others are green, and `0155`'s clown face never clears? | open | 06-29 |
| **J-03** | IME blocks tab switching on the All screen | open | 06-15 |
| **J-04** | "Subscription is shit" — needs unpacking into specifics | open | 06-29 |
| **J-05** | Opening a tab, and launch | open | 06-29 |

---

## ✅ Closed since 10-05

| Item | How it closed |
|---|---|
| **The Cyclops hero number read as stale when spaces were plentiful** | `b907798`. One green for every count. The cause was a single `.primaryM` override on the 10–19 band, a shade from the colour `AvailFreshness.heroColor` uses for aging data — so the screen was spending its freshness channel on scarcity. **Size keeps scarcity; colour keeps freshness.** → [[decisions#2026-10-08--on-the-cyclops-cell-colour-means-freshness-and-nothing-else]] |
| **The floating restore pill showed the wrong glyph** | `7afc3fa`. The 10-05 open question, answered by Jim: *"stop mirroring the tab entirely."* One fixed `chevron.up`, and `AppScreen.systemImageName` — the table that had drifted twice — is deleted. → [[tab-restore-pill]] |
| **App Store listing copy** | All five fields in English **and** 繁體中文, written as Chinese rather than translated; promotional text option C in both. Folded into **R-10**, which is now screenshots + Jim's wording pass. → [[app-store-connect]] |
| **D-07 — the two surfaces spend colour differently** | Opened and closed the same day. Jim accepted the difference; `06dc918` records why at the property a future reader would change. → [[decisions#2026-10-08--the-map-pin-and-the-cyclops-cell-may-disagree-about-colour]] |
| **繁體中文 now leads wherever both languages share a page** | Jim's standing rule, applied to the support page the same hour. Ordering, not cutting: English stays complete below with a one-tap jump, and the Latin app name stays in the `<h1>`. Audited the app too — `.xcstrings` are per-device, so there is no co-existence there to fix. → [[decisions#2026-10-08--繁體中文-leads-wherever-both-languages-share-a-surface]] |
| **The Support URL never named the app** | Built a real one: `https://sharkda.github.io/findparkingtw/support/`, live and verified. Jim's premise was wrong in a useful way — the old page **does not** redirect to Facebook and its form works; what it never did was mention *Find Parking TW*, which is the Guideline 1.5 risk. **Also unblocks R-02** — the same URL is the Gist's `support.url`, and the page has a card written for that arrival. → [[operations#-settled-2026-10-08--jim-chose-option-1-and-it-is-built]] |
| **The Marketing URL served `hello world`** | Those 12 bytes were the whole of `index.html`, from `5dd93fd`, the Pages repo's first commit — a placeholder from before the domain was used, not a fault. Replaced with a real home page, 中文 first, no invented App Store link. **The domain is load-bearing:** `app-ads.txt` must sit at the root of whatever domain the listing names, so this page cannot be traded for a prettier URL. |
| **`app-ads.txt` was on a domain we do not own** | Moved to `https://sharkda.github.io/app-ads.txt`, live and `text/plain` (`5845d7e` in `sharkda/sharkda.github.io`). The Tappx line dropped — no Tappx anywhere in the app. **Jim owes one ASC field:** Marketing URL → that domain, or the file is never crawled. → [[decisions#2026-10-08--app-adstxt-is-hosted-on-our-own-github-pages-site]] |

## ✅ Closed earlier, kept one more day for context

| Item | How it closed |
|---|---|
| **E-10 — `Municipal` had no actor isolation** | `319654b`. `Municipal` **and** `NbsObsM` are `@MainActor`. Two annotations, zero diagnostics, verified at runtime. The estimate was wrong twice on the way — see [[decisions#2026-09-29-municipal-and-nbsobsm-are-main-actor-isolated]] for why an error count from a *failed* build is a floor, not a total. |
| **E-16 unblocked** | All four files traced; each one's only call site is its own `#Preview`. Ready to delete whenever. |

## 🧹 Stale rows

**One, and it was load-bearing.** [[unfinished]] has said since 09-08 that `SubscriptionStoreScreen` is unreferenced. **It is not** — it is reachable from the Cyclops toolbar, which means a live English-only string had been sitting in a shipping screen for eleven days while the note said the screen was dead. Corrected in `unfinished.md`, and tracked as **E-29** because the same note makes the same claim about `EntitledView`.

Earlier corrections: [[sessions/older/2026-09-17/00-state-of-play|09-17 § Stale rows]].

## How to keep this going

1. Each session gets `sessions/YYYY-MM-DD/00-state-of-play.md`, seeded by copying **this table forward**.
2. **Only the State and Moved columns change.** An ID is never reused and never deleted — closed rows move to *Closed today* on the day they close, and drop off the next day's table.
3. A new item takes the next free number in its letter.
4. Sessions older than two days live in `sessions/older/`. Wikilinks resolve by note name, so moving a folder does not break them — the one exception is a **duplicated** note name (`01-session-wrap` exists three times), which is why the two links pointing at older copies now spell out their full path.

## Related
[[jim-actions]] · [[bugs]] · [[unfinished]] · [[decisions]] · [[data-sources]] · [[privacy-policy]] · [[release-strategy]] · [[INDEX]] · [[app-store-connect]] · [[tab-restore-pill]] · [[main-thread-explained]] · [[sessions/older/2026-10-05/00-state-of-play|the 10-05 note]] · [[sessions/older/2026-09-15/02-pick-up-here|the 09-15 handoff]]

---

# Session wrap — saved 2026-10-08

**Code:** `main` = **`06dc918`**, working tree clean, pushed. Two commits this session:

| Commit | What |
|---|---|
| `b907798` | Cyclops: one green for every count — colour now means freshness only |
| `06dc918` | Record why the map pin's colour channel differs from Cyclops' (comment only) |

**Verified before committing:** iOS Debug · iOS Release · macOS Debug · macOS Release all build; the app ran on the iPhone simulator with the location set to Taipei, rebuilt the Cyclops cells twice (`👁 cyclops rebuilt: 3 of 3 watched`), and took **zero** uncaught exceptions. `grep` confirms `.primaryM` is gone from every scarcity path.

**Vault:** `decisions.md` (one entry), this note, `CURRENT.md`, `INDEX.md`. `2026-10-05/` moved to `older/` per the two-day rule, and the five path-prefixed wikilinks that pointed into it were rewritten — see [[swift-patterns]] on why a path-prefixed link is the one kind that breaks on a move.

**Noticed, not touched:** `app-store-connect.md` has a stray `## misilinous` heading above *Part 3 — TestFlight*, added outside this session. Left as-is — it is Jim's file and his word.

**Also today, outside the code:** `app-ads.txt` moved off Tappx's domain onto Jim's own GitHub Pages site. **The reported fault was a false alarm** — the old URL returns 200 with the correct content, so this was ownership rather than repair; worth writing down, because "I can't reach it" and "it is down" are different claims and only one of them was true. Three new rows in [[jim-actions]] follow from it, the load-bearing one being **the Marketing URL** — the file is only ever found via the domain in the store listing.

**Three URLs are now paste-ready for App Store Connect** — Support, Marketing and Privacy Policy, all three verified `200` today, in [[app-store-connect#-the-three-url-fields--paste-ready-all-three-verified-live-2026-10-08]]. Support and Marketing are **per localisation**, so each needs en *and* zh-Hant.

**Where to pick up:** the 🔴 table — **R-01, archive and upload**, then **R-20, paste the review notes**. Every 🔴 is Jim's; nothing is waiting on me. **D-07**, the only thing I opened today, closed the same day.
