# State of play — 2026-09-19

> [!info] What this note is
> **One table, every open item, with a stable ID.** Built by reading every note in this folder and then **checking each claim against the repo** — several items the notes still listed as open are in fact done, and they are called out below rather than silently dropped.
>
> Carried forward from [[sessions/2026-09-18/00-state-of-play|2026-09-18]]. The IDs do not change — only **State** and **Moved** move, so an item cannot quietly disappear and "didn't we fix that?" has an answer.

**Repo:** `main` = `origin/main` = **`9285a47`**, working tree clean, **everything pushed.**
**Toolchain:** Xcode 27.0 (27A266a) / Swift 6.4, macOS 27.0. All four configurations build.

---

# Today in plain words

**Three things, all done and pushed.** The first two are `327bf08`; the third is `9285a47`. The second was found by accident while doing the first.

## 1. The subscription screen was missing a required link

**What was wrong.** Before someone can subscribe, Apple wants two links on the screen: a **privacy policy** and **terms of use**. Our screen showed buttons for both — but only the privacy one led anywhere. The terms button had nothing behind it. This had been true the whole time; nobody had noticed because the button looks fine until you press it.

**Why it came up now.** Jim asked where the policy page's terms sentence was. That sentence turned out to point at a page that does not exist — and checking that led to the app, where the link was missing altogether.

**What we fixed.** Both subscription screens now link terms of use. It points at **Apple's own standard subscription agreement** — because we never wrote terms of our own, and when you don't, Apple's is the agreement that legally applies. So it is the right answer, not a stand-in.

**Is it solved?** **Yes, in the code.** One thing is unchecked: **nobody has actually seen the button appear.** This version of Xcode has no Simulator app, so there is no way to tap through to that screen here. The code is written exactly like the privacy button next to it, which works — but that is reasoning, not seeing. **Please check it on your phone**: open Subscribe, look for *both* buttons, tap both. That is now part of the device pass (**R-14**).

## 2. A screen we believed was dead was actually live — and it was showing English to Chinese users

**What was wrong.** On **8 September** a note was written saying one of the two subscription screens was no longer used by anything. **That note was wrong.** The screen is reachable — from the Cyclops toolbar, through the subscribe icon.

**Why that mattered.** On **9 September**, the day after, we fixed a bug where a screen showed the English words "Privacy Policy" to a user with a Chinese phone. That fix was applied to the *other* subscription screen. **This one was skipped — because the note said it was dead.**

So for **eleven days**, a Chinese-speaking user who tapped the subscribe icon saw English.

**What we fixed.** Same commit. That screen now uses the same translatable text as its sibling. The wrong note is corrected in [[unfinished]].

**Is it solved?** **Yes — but the wider risk is not.** The same 8 September note *also* says `EntitledView` is unused, and **we have not checked that one.** More importantly, there is a planned cleanup (**E-16**) to **delete three files** on the strength of notes from the same week. **Do not delete them until each one is traced the way this one was.** Logged as **E-29**.

---

## 3. Searching for a car park only worked if you used capitals

**What was wrong.** Every Taipei car-park id looks like `TPE0155`. The search compared text exactly, capitals included — so typing `tpe0155` found **nothing** and the list came back empty. This is the bug Jim reported back in June.

**Why it mattered more than it looked.** The App Store review notes now tell a reviewer to **search for `TPE`**. A reviewer who types it in lower case out of habit gets an empty list, and concludes the app is broken. It went from a small annoyance to the cheapest possible rejection.

**What we fixed.** One line. Measured against the live 1,773-lot Taipei feed before and after:

| You type | Before | After |
|---|---|---|
| `TPE` | 1773 | 1773 |
| `tpe` | **0** | **1773** |
| `tpe0155` | **0** | **1** |
| 信義 | 158 | 158 |
| 大安 | 246 | 246 |

**The Chinese searches are untouched** — this changes nothing for the market the app is actually for. It only stops the English ids from being a trap.

**Is it solved?** **Yes**, and unlike the other two it was *measured*, not reasoned about — the numbers above come from running the new rule over the real feed.

**One thing the measurement disproved:** a full-width `ＴＰＥ` from a Chinese IME still matches nothing. The documentation implies standard comparison folds width; here it did not. Left alone deliberately — nobody types a car-park id in full-width — and the code comment now says what was measured rather than what was assumed.

---

## So: is everything solved?

| Question | Answer |
|---|---|
| Is the terms-of-use link done? | **Yes** — in the code, builds on all four configurations, committed `327bf08`. |
| Is anything about it still unproven? | **One thing.** The button has never been *seen*. Check on your phone. |
| Is the English-on-Chinese bug fixed? | **Yes**, same commit. |
| Is that whole class of problem closed? | **No.** Other "this file is unused" notes from the same week are unverified. Don't act on them yet. |
| Does the privacy policy page still need work? | **Yes**, but nothing urgent — the false "collects only 'name'" line (**R-04**) is the one worth fixing. |
| Is the search fixed? | **Yes**, and proved by measurement — `tpe` went from 0 matches to 1,773. |
| Can we archive and upload now? | **Yes — nothing is blocking it.** Both items worth putting in the binary are in and pushed. |
| Is anything still waiting on me (Claude)? | **No.** The last 🔴 with my name on it was R-12, the data-source credit — and today's audit found it **already shipped on 15 September**. Everything release-blocking is now yours. |

## What to do next

**R-01 — archive and upload**, then **R-20** — paste the App Review Notes. Those two are the front of the queue; the rest of the 🔴 table is App Store Connect form-filling that follows from them.

Two things to carry into the device pass (**R-14**):
- **Confirm both policy buttons appear** in the Subscribe sheet and open. The one part of this week that was never *seen*, only reasoned about.
- **Try `tpe` in the All tab** and watch ~1,700 lots appear.

**Nothing is waiting on me.** Today's audit closed the last 🔴 that was mine (R-12 — already shipped on 15 September, the table just had not caught up).

Detail on today's work: [[sessions/2026-09-19/01-terms-of-use|01 — Terms of Use]] · [[sessions/2026-09-19/02-reviewer-scope-and-testing|02 — the California reviewer]].

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
| **R-20** | **Paste the App Review Notes.** Rewritten again today to lead with the **map**: a reviewer types `Taipei 101` into the address bar on the first tab and the map fills with live pins — **verified against the live geocoder**, English works, no simulator or faked location. The All tab is the second route. Opens with an explicit Greater-Taipei coverage statement. | Jim | **ready to paste** | 09-19 | [[sessions/2026-09-19/02-reviewer-scope-and-testing\|02]] · [[app-store-connect#34-beta-app-review-information--paste-ready]] |
| **R-14** | **Device pass.** The three onboarding screens · the mail link (hardware only) · ATT on 2nd launch · the Subscribe tab · coverage states (outside Taiwan, and location denied once). **Two new checks from this week:** confirm **both** policy buttons render in the Subscribe sheet — E-28's one unverified part, since this Xcode ships no Simulator.app — and **type `tpe` in the All tab** and watch ~1,700 lots appear. | Jim | open | 09-19 | [[sessions/2026-09-19/01-terms-of-use\|01]] |
| **R-02** | **City-request destination**, then one line in the Gist. **Re-checked today: the live Gist still has no `support` key at all** (`version: 5`, keys are `version`/`contacts`/`tutorials`). So the outside-coverage screen ends at a statement and onboarding's prompt has nothing to tap. Gates **two** screens. | Jim | open — **verified still missing** | 09-19 | [[operations#support--which-transport-and-why-url-wins]] |
| **R-06** | **Set availability manually in ASC.** Defaults to *all* territories, which drops you into the EEA with no consent platform. Set exactly: Taiwan, US, Japan, Hong Kong, Macau. | Jim | open | 09-10 | [[operations#gate-table--read-this-before-adding-any-territory]] |
| **R-07** | **Age-rating questionnaire** in ASC. Required, and nothing in Xcode mentions it. | Jim | open | 09-10 | [[jim-actions]] |
| **R-08** | **Traditional Chinese on the subscription product in ASC.** The local fix is done; ASC still has the `zh_CN`-not-`zh_Hant` problem, and that is the one real users hit. | Jim | open | 09-09 | [[bugs]] |
| **R-09** | **Privacy nutrition labels.** Evidence already gathered — precise location, app functionality, foreground-only, never tracking. | Jim | open | 09-10 | [[sessions/older/2026-09-09/00-location-privacy-audit\|location audit]] |
| **R-10** | **Screenshots + description**, plus the App Store name and subtitle. Promotional text is paste-ready. Also carries the data-source attribution line (the in-app half shipped 09-15). **Raised in weight today:** the description is **the only place a reviewer learns the scope before opening the app**, and it is unwritten. The app name says *TW* — Taiwan — while coverage is **Greater Taipei**, so the cities belong in the opening clause, the way the subtitle does it. | Jim | open — **the scope gap** | 09-19 | [[sessions/2026-09-19/02-reviewer-scope-and-testing\|02]] · [[app-store-connect]] |
| **R-11** | **A TestFlight pass.** The only way to exercise sandbox purchases, the real ATT prompt, real ads, and the actual `tel:`/`mailto:` handoffs. | Jim | open | 09-10 | [[release-strategy]] |
| **R-13** | **Record the real tutorial video**, then set `tutorials.onboarding`. **Re-checked today: the Gist still points at the test clip** (`youtube.com/shorts/PG4CUrdkb6k`). **Downgraded from load-bearing to belt-and-braces** for review purposes — the map and list routes stand on their own — but still owed, and still the strongest single artifact for a geo-restricted app. | Jim | open | 09-19 | [[sessions/2026-09-19/02-reviewer-scope-and-testing\|02]] |

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
| **E-14** | **`hoot_test_ui` does not build.** Proven pre-existing, no scheme, in no verification. Wire it or delete it — it blocks nothing. | 🐢 | Claude | open | 09-15 | [[sessions/2026-09-15/01-session-wrap\|09-15 wrap]] |
| **E-15** | **The privacy-policy URL is hardcoded.** Halved today: both screens now read `LegalLink.privacyPolicy`, so it is **one constant instead of two literals** — but it is still in the binary rather than the Gist, which is the actual item. | 🟡 | Claude | open | 09-19 | [[privacy-policy]] · `AppPid.swift:16` |
| **E-16** | **Delete three unreferenced files** (`UserGuide`, `OnboardTab0`, `OnboardDebug`) + their 6 pbxproj entries each. **`OnboardDebug` was Jim's quick route to the IAP receipt and options screens** — that shortcut goes with it. **Re-check the list before deleting** — see E-29. | 🐢 | Claude | open | 09-06 | [[unfinished]] |
| **E-29** | **`SubscriptionStoreScreen` is NOT unreferenced**, contrary to the 09-08 note. It is live via `AppScreen:89 → MncplCyclopsScreen → toolbar0 → ToolbarPrinciple → SubButtons → NavigationLink`. Its bare English `Link("Privacy Policy")` was therefore **user-visible and stayed English on a Chinese device** — fixed in `327bf08`. **The lesson is the list, not the file:** the same 09-08 note calls `EntitledView` unreferenced, and that should be re-verified the same way before E-16 deletes anything. | 🟠 | Claude | **new** | 09-19 | [[sessions/2026-09-19/01-terms-of-use\|01]] |
| **E-17** | **`uiKick` hack in `MncplCyclopsScreen0000.swift`** — workaround for a bug now properly fixed. Likely removable; check that screen is even reachable first. | 🐢 | Claude | open | 09-01 | [[unfinished]] |
| **E-18** | **Toolbar squeeze on device** — Subscribe is icon + label next to the `.principal` search field on All/Nbs. If it squeezes, `.labelStyle(.iconOnly)` on that screen. | 🐢 | Jim | verify | 09-08 | [[unfinished]] |
| **E-19** | **Map pins fade with age** — 0.45 beyond 30 min. Judgement call on legibility over busy map detail; one number in `CustomButton.badgeOpacity`. | 🟡 | Jim | verify | 09-14 | [[jim-actions]] |
| **E-20** | **Dynamic Type** — fixed `.system(size:)` in onboarding/subscription. Mostly icons; the app name at 34 and 50 is what a large-text user notices. | 🐢 | Claude | open | 09-10 | [[jim-actions]] |
| **E-21** | **Two latent Swift-6-mode warnings** — `AVAudio.swift` attribute whitespace, `any Mu1Proto` existentials. Not urgent. | 🐢 | Claude | open | 09-15 | [[sessions/2026-09-15/01-session-wrap\|09-15 wrap]] |
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

## ✅ Closed today

| ID | Item | How it closed |
|---|---|---|
| **E-28** | **No Terms of Use link in either subscription screen.** Both set `.storeButton(.visible, for: … .policies …)`, so the sheet advertised two policy buttons with one destination supplied. `grep termsOfService` returned nothing project-wide. | **`327bf08`.** Both screens now offer it, pointing at Apple's standard EULA — the agreement that actually governs the subscription absent a custom one. New localised key `sub_terms_of_use` (en *Terms of Use* / zh-Hant *使用條款*), verified present in **both** `.lproj` of the built app. All four configurations build. |
| **R-05** | **No Terms of Use anywhere** — page, site, or app. | Both halves done: Jim deleted the dead *"accessible at bopomofo"* sentence on 09-18, and the working link landed today. **Caveat: rendering is unverified** — this Xcode ships no Simulator.app, so the button was never seen. Folded into **R-14**. |
| **R-21** / **J-01** | **Search only matched capitals.** `TPE0155` worked, `tpe0155` returned nothing. Jim's June bug report, promoted on 09-18 when the review notes started telling reviewers to type `TPE`. | **`9285a47`** — one line, `localizedStandardContains`. **Measured over the live 1,773-lot feed**, not reasoned about: `tpe` 0 → 1773, `tpe0155` 0 → 1, 信義 158 → 158 unchanged. Only this call site ships — the two others were traced and are unreachable. |

> [!note] Where the subscription flow stands
> Privacy policy **and** Terms of Use are now both reachable before purchase, which is what Guideline 3.1.2 asks for. What is left on the policy *page* is accuracy and polish, not compliance risk — with the caveat that **R-04 is an outright false statement about this app**, and it is the first line under its heading.

## 🧹 Stale rows

**One, and it was load-bearing.** [[unfinished]] has said since 09-08 that `SubscriptionStoreScreen` is unreferenced. **It is not** — it is reachable from the Cyclops toolbar, which means a live English-only string had been sitting in a shipping screen for eleven days while the note said the screen was dead. Corrected in `unfinished.md`, and tracked as **E-29** because the same note makes the same claim about `EntitledView`.

Earlier corrections: [[sessions/2026-09-17/00-state-of-play|09-17 § Stale rows]].

## How to keep this going

1. Each session gets `sessions/YYYY-MM-DD/00-state-of-play.md`, seeded by copying **this table forward**.
2. **Only the State and Moved columns change.** An ID is never reused and never deleted — closed rows move to *Closed today* on the day they close, and drop off the next day's table.
3. A new item takes the next free number in its letter.
4. Sessions older than two days live in `sessions/older/`. Wikilinks resolve by note name, so moving a folder does not break them — the one exception is a **duplicated** note name (`01-session-wrap` exists three times), which is why the two links pointing at older copies now spell out their full path.

## Related
[[jim-actions]] · [[bugs]] · [[unfinished]] · [[decisions]] · [[data-sources]] · [[privacy-policy]] · [[release-strategy]] · [[INDEX]] · [[sessions/2026-09-19/01-terms-of-use|01 — today's write-up]] · [[sessions/2026-09-18/00-state-of-play|yesterday]] · [[sessions/older/2026-09-15/02-pick-up-here|the 09-15 handoff]]
