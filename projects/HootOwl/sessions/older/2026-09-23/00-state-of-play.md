# State of play — 2026-09-23

> [!info] What this note is
> **One table, every open item, with a stable ID.** Built by reading every note in this folder and then **checking each claim against the repo** — several items the notes still listed as open are in fact done, and they are called out below rather than silently dropped.
>
> Carried forward from [[sessions/older/2026-09-20/00-state-of-play|2026-09-20]]. The IDs do not change — only **State** and **Moved** move, so an item cannot quietly disappear and "didn't we fix that?" has an answer.

**Repo:** `main` = `origin/main` = **`42ed13b`**, working tree clean, both repos pushed.
**Toolchain:** Xcode 27.0 (27A266a) / Swift 6.4, macOS 27.0 — **unchanged by the machine update**, so the 09-20 verification still stands.

**Since 09-20: `destination-mode` was tested across seven rounds and is now merged — it ships in build 1.** Everything about it, including how to undo it: [[destination-mode]].

---

# Where this stands, in plain words

**The app now works outside Taipei.** Someone in California — a reviewer, or a Taiwanese user planning a trip home — opens it, is asked *"Where are you heading?"*, taps **Go to Taipei**, and gets the real product: live space counts, pins, distances, all measured from there. A slim bar keeps saying *"Showing 台北市 — you're not there"* so nobody is confused about whose location the numbers describe.

That took seven rounds of Jim's testing, and the interesting part is how little new code it needed. **The app was never location-bound — the refusal was.** Three lines computed everything from the GPS fix; routing them through one `effectiveCentre` made the rest follow.

**It is merged and it ships in build 1.** Jim's reason is the product one rather than the review one: *"we need to let our potentional users test the app before they are in the zone."*

## What is left before you can archive

1. **Your 中文 pass** — 26 strings marked `needs_review`, nine of them new this week. The one worth a look is **`dest_bar_showing` → 「顯示 %@ — 你不在這裡」**, because that bar is on screen constantly and the Chinese may land harsher than the English.
2. **A device pass** — including the parts nobody has tapped: the grey/green search button and its "no data here yet" alert, the auto-search 1.2 s after the map settles, and **Clear** vanishing outside the zone. Plus the older list: a real ad banner (13.10.0 has never served a live impression), both policy buttons in the Subscribe sheet, and `tpe` in the All tab.
3. **R-01 archive and upload**, then **R-20 paste the review notes** — both paste-ready.

## One known risk, carried deliberately

**E-12 went from inert to load-bearing.** `convexEnclosing` is integer-truncated and has been known-wrong for weeks; nothing used it in anger. **`isInServiceArea` now does**, so a point near a fence boundary could resolve wrongly — a green button where there is no data, or grey where there is. The 1 km tolerance masks it in practice, which is why nothing has surfaced. Worth fixing before a third city, when the boundaries stop being one convex blob.

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
| **R-14** | **Device pass.** The three onboarding screens · the mail link (hardware only) · ATT on 2nd launch · the Subscribe tab · coverage states (outside Taiwan, and location denied once). **Two new checks from this week:** confirm **both** policy buttons render in the Subscribe sheet — E-28's one unverified part, since this Xcode ships no Simulator.app — and **type `tpe` in the All tab** and watch ~1,700 lots appear. | Jim | open | 09-19 | [[sessions/older/2026-09-19/01-terms-of-use\|01]] |
| **R-02** | **City-request destination**, then one line in the Gist. **Re-checked today: the live Gist still has no `support` key at all** (`version: 5`, keys are `version`/`contacts`/`tutorials`). So the outside-coverage screen ends at a statement and onboarding's prompt has nothing to tap. Gates **two** screens. | Jim | open — **verified still missing** | 09-19 | [[operations#support--which-transport-and-why-url-wins]] |
| **R-06** | **Set availability manually in ASC.** Defaults to *all* territories, which drops you into the EEA with no consent platform. Set exactly: Taiwan, US, Japan, Hong Kong, Macau. | Jim | open | 09-10 | [[operations#gate-table--read-this-before-adding-any-territory]] |
| **R-07** | **Age-rating questionnaire** in ASC. Required, and nothing in Xcode mentions it. | Jim | open | 09-10 | [[jim-actions]] |
| **R-08** | **Traditional Chinese on the subscription product in ASC.** The local fix is done; ASC still has the `zh_CN`-not-`zh_Hant` problem, and that is the one real users hit. | Jim | open | 09-09 | [[bugs]] |
| **R-09** | **Privacy nutrition labels.** Evidence already gathered — precise location, app functionality, foreground-only, never tracking. | Jim | open | 09-10 | [[sessions/older/2026-09-09/00-location-privacy-audit\|location audit]] |
| **R-10** | **Screenshots + description**, plus the App Store name and subtitle. Promotional text is paste-ready. Also carries the data-source attribution line (the in-app half shipped 09-15). **Raised in weight today:** the description is **the only place a reviewer learns the scope before opening the app**, and it is unwritten. The app name says *TW* — Taiwan — while coverage is **Greater Taipei**, so the cities belong in the opening clause, the way the subtitle does it. | Jim | open — **the scope gap** | 09-19 | [[sessions/older/2026-09-19/02-reviewer-scope-and-testing\|02]] · [[app-store-connect]] |
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
| **E-10** | **Mark `Municipal` `@MainActor`** before the next municipality is added. No live bug — the risk is structural: the main-thread hop is a per-call-site convention with zero enforcement, and `minuteFlow()` already lost it once by copy-paste. | 🟡 | Claude | open | 09-02 | [[sessions/older/2026-09-02/00-why-municipal-should-be-mainactor\|the reasoning]] |
| **E-11** | **Feed parsing runs on the main thread** — ~1,400 lots decoded per zone per poll. A hitch risk that grows per municipality. Do it when polling is next touched. | 🟡 | Claude | open | 09-02 | [[unfinished]] |
| **E-12** | **`convexEnclosing` is integer-truncated and wrong.** Inert today; left alone pending the fence-activation design call. | 🟡 | Claude | open | 09-15 | [[unfinished]] |
| **E-13** | **Duplicate parkIds in the NTPC feed** (11 today, `060085`, `170120`, …). Handled first-wins in `CyclopsModel`; the feed itself is wrong and other consumers may not be defensive. | 🟡 | Claude | open | 09-17 | [[unfinished]] |
| **E-14** | **`hoot_test_ui` does not build.** Proven pre-existing, no scheme, in no verification. Wire it or delete it — it blocks nothing. | 🐢 | Claude | open | 09-15 | [[sessions/older/2026-09-15/01-session-wrap\|09-15 wrap]] |
| **E-15** | **The privacy-policy URL is hardcoded.** Halved today: both screens now read `LegalLink.privacyPolicy`, so it is **one constant instead of two literals** — but it is still in the binary rather than the Gist, which is the actual item. | 🟡 | Claude | open | 09-19 | [[privacy-policy]] · `AppPid.swift:16` |
| **E-16** | **Delete three unreferenced files** (`UserGuide`, `OnboardTab0`, `OnboardDebug`) + their 6 pbxproj entries each. **`OnboardDebug` was Jim's quick route to the IAP receipt and options screens** — that shortcut goes with it. **Re-check the list before deleting** — see E-29. | 🐢 | Claude | open | 09-06 | [[unfinished]] |
| **E-29** | **`SubscriptionStoreScreen` is NOT unreferenced**, contrary to the 09-08 note. It is live via `AppScreen:89 → MncplCyclopsScreen → toolbar0 → ToolbarPrinciple → SubButtons → NavigationLink`. Its bare English `Link("Privacy Policy")` was therefore **user-visible and stayed English on a Chinese device** — fixed in `327bf08`. **The lesson is the list, not the file:** the same 09-08 note calls `EntitledView` unreferenced, and that should be re-verified the same way before E-16 deletes anything. | 🟠 | Claude | **new** | 09-19 | [[sessions/older/2026-09-19/01-terms-of-use\|01]] |
| **E-17** | **`uiKick` hack in `MncplCyclopsScreen0000.swift`** — workaround for a bug now properly fixed. Likely removable; check that screen is even reachable first. | 🐢 | Claude | open | 09-01 | [[unfinished]] |
| **E-18** | **Toolbar squeeze on device** — Subscribe is icon + label next to the `.principal` search field on All/Nbs. If it squeezes, `.labelStyle(.iconOnly)` on that screen. | 🐢 | Jim | verify | 09-08 | [[unfinished]] |
| **E-19** | **Map pins fade with age** — 0.45 beyond 30 min. Judgement call on legibility over busy map detail; one number in `CustomButton.badgeOpacity`. | 🟡 | Jim | verify | 09-14 | [[jim-actions]] |
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

## ✅ Closed since 09-20

| ID | Item | How it closed |
|---|---|---|
| **—** | **`destination-mode`, seven rounds of it** | Merged to `main` as a fast-forward, `42ed13b`. Verified **on `main`**, not the branch: four configurations build, clean out-of-zone install reaches the picker, `👁 cyclops rebuilt: 3 of 3 watched`. |
| **—** | **The map dropped the destination on every tab return** | Four sinks snapped to the device location on every appear, because `wire0` re-subscribes and `CurrentValueSubject` replays. One guard instead of four patches — `7f4113c`. [[bugs]] |
| **—** | **The picker offered a choice that made no difference** | One button, "Go to Taipei". `destinationChoices` stops deriving from fences — `42ed13b`. [[decisions]] |

## 🧹 Stale rows

**One, and it was load-bearing.** [[unfinished]] has said since 09-08 that `SubscriptionStoreScreen` is unreferenced. **It is not** — it is reachable from the Cyclops toolbar, which means a live English-only string had been sitting in a shipping screen for eleven days while the note said the screen was dead. Corrected in `unfinished.md`, and tracked as **E-29** because the same note makes the same claim about `EntitledView`.

Earlier corrections: [[sessions/older/2026-09-17/00-state-of-play|09-17 § Stale rows]].

## How to keep this going

1. Each session gets `sessions/YYYY-MM-DD/00-state-of-play.md`, seeded by copying **this table forward**.
2. **Only the State and Moved columns change.** An ID is never reused and never deleted — closed rows move to *Closed today* on the day they close, and drop off the next day's table.
3. A new item takes the next free number in its letter.
4. Sessions older than two days live in `sessions/older/`. Wikilinks resolve by note name, so moving a folder does not break them — the one exception is a **duplicated** note name (`01-session-wrap` exists three times), which is why the two links pointing at older copies now spell out their full path.

## Related
[[jim-actions]] · [[bugs]] · [[unfinished]] · [[decisions]] · [[data-sources]] · [[privacy-policy]] · [[release-strategy]] · [[INDEX]] · [[sessions/older/2026-09-19/01-terms-of-use|01 — today's write-up]] · [[sessions/older/2026-09-18/00-state-of-play|yesterday]] · [[sessions/older/2026-09-15/02-pick-up-here|the 09-15 handoff]]

---

# Session wrap — saved 2026-09-20

**Code:** `main` = **`55197b4`**, working tree clean. **One commit unpushed** — `55197b4 "sep20"`, Jim's own, committing the Xcode rewrite described below. `origin/main` is at `9285a47`.

Four commits this stretch: `e45051c` (NTPC paging), `327bf08` (Terms of Use), `9285a47` (case-insensitive search), `55197b4` (Xcode's project normalisation, Jim's).

> [!success] ✅ Resolved while this was being written — Jim committed it as `55197b4`
> The section below was written when the tree was dirty. **It is now committed**, and the audit it records still stands, key for key. **Nothing to undo; one thing to push.**

> [!note] What `55197b4` contains — audited before it was committed
> Xcode is **open** and has rewritten three files. **Nothing is broken, and nothing of mine is at risk** — checked key by key:
>
> | File | What Xcode did | Verdict |
> |---|---|---|
> | `Info.plist` | Migrated `ITSAppUsesNonExemptEncryption`, `NSLocationWhenInUseUsageDescription`, `NSUserTrackingUsageDescription` out to `INFOPLIST_KEY_*` build settings — **the same migration as 09-16**, which you chose to revert then | Functionally identical (both keys present twice in the pbxproj, Debug + Release). **What is lost is the comment block** explaining *why* export compliance is `false` |
> | `Localizable.xcstrings` | Reformatted and reordered the whole file — a 654-line diff | **Zero content changes** across 338 shared keys, and `sub_terms_of_use` survives intact with both locales |
> | `project.pbxproj` | Entry reordering + the `INFOPLIST_KEY_*` additions | **No `IPHONEOS_DEPLOYMENT_TARGET` change this time** — unlike 09-16, the 26.0 floor is untouched |
>
> **One removal is actually good news.** The catalogue lost the auto-extracted key `"Privacy Policy"` — the English literal that used to live in `SubscriptionStoreView.swift`. Xcode garbage-collected it **because the literal is genuinely gone**, which independently confirms the E-28 fix.
>
> **The one real loss is the comment block** in `Info.plist` explaining why export compliance is `false` — the rationale from `5411f69`. The *declaration* survives as `INFOPLIST_KEY_ITSAppUsesNonExemptEncryption` in both configurations, so App Store Connect still stops asking; only the explanation is gone from the file a future reader would open. It is preserved here and in [[bugs#2026-09-16--xcode-rewrote-the-project-file-mid-session-including-the-deployment-target-open]] if it is ever wanted back.

**Vault: saved.** Written or updated this session — `bugs.md` (3 entries), `decisions.md` (2), `unfinished.md` (a correction), `patterns/swift-patterns.md` (3 patterns), `privacy-policy.md`, `data-sources.md`, `app-store-connect.md`, `jim-actions.md`, `Jim's backlog.md`, `INDEX.md`, `CURRENT.md`, and three session notes here.

**Where to pick up:** **push `55197b4`**, then the 🔴 table above — **R-01, archive and upload**, then **R-20, paste the review notes.** Every 🔴 is yours; nothing is waiting on me.
