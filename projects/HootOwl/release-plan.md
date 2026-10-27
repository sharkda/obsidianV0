# Release plan — GM 1.0 · 1.1 · 1.2+

**Every open item in the vault, in one of three buckets.** Built 2026-10-22 from the real IDs in [[00-state-of-play|sessions/2026-10-08]], [[roadmap]], [[unfinished]], [[jim-actions]] and [[Jim's backlog]] — nothing here is invented, and every row keeps the ID it already had.

> [!abstract] The headline, before the tables
> **Nothing in code blocks GM 1.0.** `main` is shippable, and C1 (`9b957e6`) only improved that. **The entire critical path is yours** — App Store Connect fields, screenshots, the 中文 wording pass, and one device run.
>
> Ten items stand between here and submission, and **all ten are yours.** My GM 1.0 list is four items, none of them blocking.

**Naming** ([[working-agreements#Release names: "GM, 1.0" and "1.1" — never "build 1"]]): **GM, 1.0** is the golden master, the first public release. **1.1** is the first update after launch, with its own 1–3 day review. **1.2+** means anything beyond that.

---

## What actually blocks GM 1.0

*In the order I would do them. Every row is Jim's.*

| ID | Item | Why it blocks |
|---|---|---|
| **R-10** | **Screenshots + your wording pass** | Longest lead time of anything here, and the only item that needs you to *make* something rather than paste it. Copy is drafted in both languages — [[app-store-connect]] |
| **R-02** | **Decide the city-request destination, then one line in the Gist** | Gates **two** screens. The live Gist still has no `support` key, so onboarding's "tell us where you need it" prompt has nothing to tap. The URL already exists: `sharkda.github.io/findparkingtw/support/` |
| **R-09** | **Privacy nutrition labels** | Evidence already gathered: precise location · app functionality · **foreground-only** · never tracking |
| **R-06** | **Set territories manually** | Defaults to *all*, which drops you into the EEA with no consent platform. Exactly: Taiwan, US, Japan, Hong Kong, Macau — [[operations#gate-table]] |
| **R-07** | **Age-rating questionnaire** | Required, and nothing in Xcode mentions it |
| **R-08** | **繁體中文 on the subscription product in ASC** | The local fix shipped; ASC still has `zh_CN` not `zh_Hant`, and that is the one real users hit |
| **R-04** | **Fix the privacy policy's opening claim** | *"collects only 'name'"* is **false for this app** and it is the first line a reviewer reads. 🟠 on the old table, but it is a false statement about the app, so I would not ship past it |
| **R-14 + E-25** | **One device pass** | Three onboarding screens · the mail link (hardware only) · ATT on 2nd launch · Subscribe tab · coverage states · **plus the clean-install permission run E-25 still owes** |
| **R-11** | **A TestFlight pass** | The only way to exercise sandbox purchases, the real ATT prompt, real ads, and the `tel:`/`mailto:` handoffs |
| **R-20** | **Paste the App Review Notes** | Written and paste-ready. Leads with the map route, which is the one verified against the live geocoder |
| **R-01** | **Re-archive and upload** | Last, not first. The 09-14 archive contains the `.commands` launch crash and cannot start. Burn a build number |

> [!tip] If you want the shortest path
> **R-10 first** — screenshots are the only thing with a lead time. Everything else is paste-and-tick work you can do in one sitting, and **R-01 is last by definition.**

### Decisions I need from you before GM 1.0

| ID | Decision | Status |
|---|---|---|
| **D-01** | ~~🔴 **Is there any reason to subscribe?**~~ | ✅ **DECIDED 2026-10-27 — ship as "remove ads", and say exactly that.** Jim: *"yes… in the future, if we add subscriber only features we will get back to this."* **No code change, and no copy change either** — both the English and 中文 ASC descriptions were already drafted this way. Reasoning and the reopen trigger: [[decisions#2026-10-27--the-subscription-is-remove-ads-and-the-app-says-exactly-that]] |
| **E-02** | 🟠 **Crash visibility.** No Crashlytics, no Sentry. Organizer shows only opted-in users, partial and delayed | **Launch on Organizer alone, decide a third-party SDK for 1.1.** A crash SDK collects diagnostic data, which is a **declarable nutrition-label category** — the same argument that kept detection out of the app in [[data-schema-lifecycle]]. Adding one now reopens R-09 days before submission. And C1 just removed the crash class we knew about |

### Mine for GM 1.0 — none of it blocking

| ID | Item | State |
|---|---|---|
| **C1** | Stop crashing on a changed feed | ✅ **done `9b957e6`** — iOS Debug + Release clean. **Not yet run**; that is step 1 next session |
| **E-01** | 🟠 *"Nothing tells a user when the feed is down"* | ✅ **substantially closed by C1.** `StaleDataBanner` was already built, already wired, already bilingual — it simply could never be reached, because an unparseable feed crashed the app first. **The remaining half — telling them *why* — is ④ in 1.1** |
| **D-02** | ✅ **Label the 40% of car parks with no live count** — Jim's call 2026-10-27, *"show the label, this need to be done in 1.0"* | ✅ **done `7cebf96`** — sheet, All tab and Cyclops all say it, in both languages; map pin deliberately unchanged. iOS Debug + Release clean, **not yet run**. Measured: **1,053 of 2,592 lots (40.6%)**, and New Taipei is still at 69.4% — this is the steady state, not a transition. [[decisions#2026-10-27--label-the-car-parks-with-no-live-count-d-02]] |
| **E-30** | 🟠 Three permission strings the iOS build never uses, one placeholder with literal quotes | **Recommend doing it.** It contradicts the app's own promise of foreground-only *and* undercuts R-09's evidence. A three-key deletion. **Your call because it changes what the Store sees** |
| **E-03** | 🟠 `TpeParkDescInfo.json` missing from the iOS bundle, logged at every launch, never investigated | **Recommend investigating before submission.** Likely the same missing-target-membership shape the `fences` folder had — and that one meant the geofence system had never run on iOS at all |
| **E-12** | 🟠 `convexEnclosing` is integer-truncated, and now has **four** call sites including `isInServiceArea` | **Recommend fixing in 1.0 if it is the `Int(...)` one-liner it looks like.** It decides the search button's green/grey and whether a destination counts as covered. Masked today by the 1 km tolerance — which is luck, not design |

---

## 1.1 — the first update

**Your J1 answer, and it is a commitment to ship 1.1, not a trigger to wait for a break.**

| ID | Item | Owner |
|---|---|---|
| **④** | **Tell users *why* the data stalled** — the `feedStatus` flag in the existing Gist, plus a banner. Needs **J4** (copy approval) and **J7** (paste one block into the Gist) | mine + yours |
| **⑤** | **Fix a rename without a release** — key-alias map, the `UPDATETIME` format, and the feed URL, all moved into config | mine |
| **⑥** | **Heal running apps** — foreground refetch, refetch-on-break, cache-buster, and a DEBUG path that can read the real Gist | mine |
| **E-15** | Privacy-policy URL into the Gist instead of the binary | mine — **bundle with ⑤**, same mechanism |
| **E-04** | Reject placeholder config values (`@example.com`, `1234-5678`) as absent | mine — **bundle with ⑤**, ~4 lines |
| **E-11** | Feed parsing runs on the main thread — ~1,400 lots per zone per poll | mine. *Do it when polling is next touched, and ⑤ ⑥ touch polling* |
| **E-13** | 11 duplicate parkIds in the NTPC feed | mine |
| **E-02** | Decide a third-party crash SDK, now that R-09 is settled | yours |
| **E-18 · E-19** | Toolbar squeeze · map-pin alpha floor at 30 min — both "built, never looked at on a device" | yours, in the same pass |
| **R-13** | Record the real tutorial video; the Gist still points at a test clip | yours |
| **R-15 · R-16** | The two New Taipei phone calls — the blocked bulk download, and whether 8607 sits on that number | yours, any time |
| **J-02 … J-05** | Your own backlog: the grey `0080` / stuck clown face, the IME tab-switch block, *"subscription is shit"*, and tab/launch | **needs triage with you first** — none has had any investigation |

> [!note] Why E-11 belongs here and not in 1.2+
> It is filed as "do it when polling is next touched." ⑤ and ⑥ *are* touching polling. Doing it separately means reading the same interleaved sink twice.

---

## 1.2+ — beyond 1.1

| ID | Item | Owner |
|---|---|---|
| **F-01** | Let the user pick which map app gets the directions | mine |
| **F-02** | **The next municipality, starting with 基隆** — pair it with **E-24**, or onboarding screen 1 understates our own coverage in both languages | mine |
| — | **The republishing mirror** from [[data-schema-lifecycle#The upper bound]] — documented, deliberately not built. Revisit if a third city arrives or churn exceeds twice a year | mine |
| **E-06 → E-07** | `ActDeActOnes` has zero callers, so every proto polls for every user regardless of location. **E-07 (battery measurement) is blocked until this is fixed** or the number means nothing | mine |
| **E-08 · E-09** | Phase 3 lifecycle device test (committed June, never run) · Cyclops 🕐 on a cache-less launch | yours |
| **E-16** | Delete four unreferenced files + 6 pbxproj entries each. **Re-verify `EntitledView` first (E-29)** — the same note was wrong about `SubscriptionStoreScreen`, and that cost a live English string eleven days on a Chinese device | mine |
| **E-14 · E-17 · E-20 · E-21** | `hoot_test_ui` doesn't build · the `uiKick` hack · Dynamic Type in onboarding/subscription · two latent Swift-6 warnings | mine |
| **E-22 · E-23** | `CLAUDE.md` / `AGENTS.md` claim park IDs are `tpe_`/`ntpc_` prefixed — **no code does that**, and it cost a full investigation cycle once · the `fileprivate(set)` guidance | yours — your files |
| **D-03** | Mainland China — recommendation is **drop it** (ICP filing, AdMob blocked, wrong parking data). HK + Macau have none of those problems and are already in R-06 | yours |
| **D-04** | iOS 26.0 minimum — worth pricing deliberately for a commuter utility where some of the audience is on older hardware | yours |
| **D-05** | A full corrected privacy policy in English + 中文. Offered twice, deliberately not written — **it is your document to own** | yours |
| **D-06** | Watch early reviews for the ad-expectation line. *"There will be more of them over time"* is deliberate pre-framing but can read as a threat. One string to soften | yours |
| **E-05** | ⚠️ **Effectively dropped.** The iOS half is already done (`InfoPlist.xcstrings` ships zh-Hant for both prompts). Only the **macOS** half remains, and per [[working-agreements]] 2026-10-21 macOS is no longer built or verified | — |

---

## Belongs to no release

| Item | Why it has no bucket |
|---|---|
| **③ Detect — C2, the feed-shape detector** | A script and a cron job. **Ships outside the binary**, so it needs no review and no version. It can go live before GM 1.0 or after; it is the next thing I build either way. Waiting on **J5** — is `sharkda/hootOwl` public or private? A 15-minute cron overruns the free private-repo Actions allowance; 30 minutes fits |
| **M-01 · M-02** | Second-machine setup. Blocks the MacBook Air from being useful, blocks no release. Move the Air's vault to `~/obsidianV0`, then copy `.claude/settings.local.json` across |

---

## What I would do next session

1. **Run C1** on a simulator. It compiles; nothing has exercised the new failure path. The standing rule holds — the worst breakage this project has had **compiled clean and crashed at launch**.
2. **E-12**, if it is the one-liner it looks like. It decides coverage correctness and is the cheapest real risk on the board.
3. **E-03** — find out why that JSON is not in the bundle.
4. **C2**, once you answer J5.

And **E-30** the moment you say yes, since it is your call about what the Store sees.

---

## Related

- [[00-state-of-play|sessions/2026-10-08]] — the canonical ID table every row here came from. **Still the source of truth for State and Moved; this page only buckets them**
- [[jim-actions]] — your list, grouped by where you would be sitting
- [[data-schema-lifecycle]] — the ② ③ ④ ⑤ ⑥ stages, and the J/C action tables
- [[release-strategy]] — TestFlight vs straight to release, and the one rejection I would bet on
- [[app-store-connect]] — every ASC field, paste-ready
- [[roadmap]] — the `F-` features in full
