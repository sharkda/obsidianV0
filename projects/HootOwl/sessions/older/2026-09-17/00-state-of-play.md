# State of play — 2026-09-17

> [!info] What this note is
> **One table, every open item, with a stable ID.** Built by reading every note in this folder and then **checking each claim against the repo** — several items the notes still listed as open are in fact done, and they are called out below rather than silently dropped.
>
> The IDs (`R-`, `E-`, `J-`, `D-`) are the point. They do not change. Tomorrow's session copies this table forward and only the **State** column moves, so an item cannot quietly disappear and "didn't we fix that?" has an answer.

**Repo:** `main` = `origin/main` = **`e45051c`**, working tree clean, nothing unpushed.
**Toolchain:** Xcode 27.0 (27A266a) / Swift 6.4, macOS 27.0. All five builds pass; the app runs on the simulator.

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

| ID | Item | P | Owner | State | Moved | Detail |
|---|---|---|---|---|---|---|
| **R-01** | **Re-archive and upload.** The 09-14 archive contains the `.commands` launch crash — it cannot start. Burn a build number. | 🔴 | Jim | **open — next up** | 09-17 | [[jim-actions]] · [[app-store-connect]] |
| **R-02** | **City-request destination**, then one line in the Gist. Code is done and dormant; `support.url` beats `support.email`. Gates **two** screens — onboarding and the new outside-coverage state. | 🔴 | Jim | open | 09-16 | [[operations#support--which-transport-and-why-url-wins]] |
| **R-03** | **Privacy policy — scope the AdMob sentence.** "I do not, and will not share any information…" now sits two paragraphs from the IDFA line and contradicts both it and your own ATT prompt. Paste-ready wording exists. | 🔴 | Jim | open | 09-16 | [[privacy-policy]] |
| **R-04** | **Privacy policy — the headline claim is still Bopomofo's.** "collects only 'name'" is the first line under *Information Collection and Use* and is false here. | 🟠 | Jim | open | 09-16 | [[privacy-policy]] |
| **R-05** | **Privacy policy — terms link is not a link.** This page is what the subscription sheet opens; Guideline 3.1.2 wants working privacy *and* terms links. | 🟠 | Jim | open | 09-16 | [[privacy-policy]] |
| **R-06** | **Set availability manually in ASC.** It defaults to *all* territories, which drops you into the EEA with no consent platform. Set exactly: Taiwan, US, Japan, Hong Kong, Macau. | 🔴 | Jim | open | 09-10 | [[operations#gate-table--read-this-before-adding-any-territory]] |
| **R-07** | **Age-rating questionnaire** in ASC. Required, and nothing in Xcode mentions it. | 🔴 | Jim | open | 09-10 | [[jim-actions]] |
| **R-08** | **Traditional Chinese on the subscription product in ASC.** The local fix is done; ASC has the same `zh_CN`-not-`zh_Hant` problem and that is the one real users hit. | 🔴 | Jim | open | 09-09 | [[bugs]] |
| **R-09** | **Privacy nutrition labels.** Location evidence is already gathered — precise, app functionality, foreground-only, never tracking. | 🔴 | Jim | open | 09-10 | [[sessions/older/2026-09-09/00-location-privacy-audit\|location audit]] |
| **R-10** | **Screenshots + description**, and the App Store name `Find Parking TW` / subtitle. Promotional text is drafted and paste-ready. | 🔴 | Jim | open | 09-14 | [[app-store-connect]] |
| **R-11** | **A TestFlight pass.** The only way to exercise sandbox purchases, the real ATT prompt, real ads, and the actual `tel:`/`mailto:` handoffs. | 🔴 | Jim | open | 09-10 | [[release-strategy]] |
| **R-12** | **Credit the data sources.** 政府資料開放授權條款-第1版 **requires attribution** and the app credits them nowhere. Licence compliance, not App Review. | 🔴 | Claude | open | 09-10 | [[data-sources]] |
| **R-13** | **Record the real tutorial video**, then set `tutorials.onboarding`. What is live now is a personal test clip. | 🔴 | Jim | open | 09-07 | [[jim-actions]] |
| **R-14** | **Device pass** — the three onboarding screens, the mail link (hardware only), ATT on 2nd launch, the Subscribe tab, **plus the new coverage states**: outside Taiwan, and location denied once. | 🔴 | Jim | open | 09-15 | [[jim-actions]] |

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
| **E-15** | **The privacy-policy URL is hardcoded in two Swift files** — `SubscriptionStoreView.swift` and `SubscriptionScreen.swift`. The only remote-configurable thing not in the Gist. *Confirmed today.* | 🟡 | Claude | open | 09-17 | [[privacy-policy]] |
| **E-16** | **Delete three unreferenced files** (`UserGuide`, `OnboardTab0`, `OnboardDebug`) + their 6 pbxproj entries each. **`OnboardDebug` was Jim's quick route to the IAP receipt and options screens** — that shortcut goes with it. | 🐢 | Claude | open | 09-06 | [[unfinished]] |
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
| **J-01** | Search is case-sensitive — `TPE0155` works, `tpe0155` does not | open | 06-29 |
| **J-02** | Why is `0080` grey while others are green, and `0155`'s clown face never clears? | open | 06-29 |
| **J-03** | IME blocks tab switching on the All screen | open | 06-15 |
| **J-04** | "Subscription is shit" — needs unpacking into specifics | open | 06-29 |
| **J-05** | Opening a tab, and launch | open | 06-29 |

---

## ✅ Closed today

| ID | Item | How it closed |
|---|---|---|
| **E-26** | **NTPC availability was dead** — the bulk CSV began returning an F5 rejection page with HTTP 200. Half the coverage area silently served stale numbers. | Fixed and pushed, **`e45051c`**. `Mu1Base` gained an overridable `fetchMinutely()`; NTPC pages through `?page=N&size=1000`. Verified live: 2 pages, 1410 rows, `∑1410` at 22:33 against a 15:19 cache. [[bugs]] |
| **E-27** | **Xcode rewrote the project file mid-session**, bumping `IPHONEOS_DEPLOYMENT_TARGET` 26.0 → 26.6 and migrating three Info.plist keys into build settings. | Xcode quit, both files reverted, all five builds re-run. Plain `xcodebuild` does **not** do this — it was Xcode.app with the project open. [[bugs]] |
| **—** | **Re-verify after the macOS update** — the whole reason 09-15 left a warning. | Xcode unchanged (27.0 / 27A266a). Five builds pass; app launches, fences load, coverage flips `outside` ↔ `covered`. |

---

## 🧹 Stale rows found while building this table

**The notes said these were open. The repo says otherwise.** Corrected in place, and listed here so the correction itself is visible rather than silent.

| Was listed as open in | Claim | Actually |
|---|---|---|
| [[jim-actions]] | `ITSAppUsesNonExemptEncryption` is absent from `Info.plist` | **Present** — added in `5411f69`, and restored today when the Xcode rewrite was reverted |
| [[jim-actions]] | Ship an "outside coverage" empty state | **Shipped** in `fb28765`, and exercised on the simulator today |
| [[jim-actions]] | Merge `icon-replacement` into `main` | **Merged** at `98f1253`, fast-forward |
| [[unfinished]] | `fences` file missing from the app bundle | **Fixed** 09-15 (`88c5b4b`) — the folder loads, both cities deserialize |
| [[unfinished]] | The contact Gist is all `example.com` placeholders | **Fixed** 09-09 — both cities carry real values. Only the `support` key remains, which is **R-02** |

---

## How to keep this going

1. Each session gets `sessions/YYYY-MM-DD/00-state-of-play.md`, seeded by copying **this table forward**.
2. **Only the State and Moved columns change.** An ID is never reused and never deleted — closed rows move to *Closed today* on the day they close, and drop off the next day's table.
3. A new item takes the next free number in its letter.
4. Sessions older than two days live in `sessions/older/`. Wikilinks resolve by note name, so moving a folder does not break them — the one exception is a **duplicated** note name (`01-session-wrap` exists three times), which is why the two links pointing at older copies now spell out their full path.

## Related
[[jim-actions]] · [[bugs]] · [[unfinished]] · [[decisions]] · [[data-sources]] · [[privacy-policy]] · [[release-strategy]] · [[INDEX]] · [[sessions/2026-09-15/02-pick-up-here|the 09-15 handoff]]
