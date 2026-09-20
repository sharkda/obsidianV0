
## jim's request table for onboarding

| id            | request                                                                                                                                                                                                                                                                                 | rational                                                                                                                                                                            | status                    | AI response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| taipei2Taiwan | in the current build it is Taipei only, it will cover more cities later, eventually all of Taiwan if users request. * i mean we need to revise the wording in the onboarding, don't say we are two cities, we need to send the messages, let us know where you want and we will diiver* | to let users feedback if they want other cities, so we can prioritize, currently only Taipei and new Taipei city. one of the reasons is other city they park anywhere they like.... | done, needs Gist address | **Done — final copy 2026-09-07, all three of your beats.** Screen 1: *"Live parking. Right now. / **Taipei and New Taipei City today — more cities soon.** / Tell us where you need it most — we'll adjust our priorities. / **Request your city →**"* Coverage stated, expansion signalled, ask made. Values only in `Localizable.xcstrings`; no code change for the copy. **Two things now depend on this:** (1) the Gist `support` address is a release item — the prompt renders even without it, so users would read the offer and have nothing to tap; (2) `onb_s1_body` **names the live cities**, so shipping a third municipality means updating that string in en *and* 中文 or the first screen understates our coverage. Both logged in [[unfinished]]. One flag, then it's yours: **"soon" is a timing commitment** where "expanding" was not — it's the one word here a reviewer or an annoyed user could hold us to. Kept because you asked for it. Full trail: [[00-req-taipei2Taiwan]] |
|               |                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                     |                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

# HootOwl — Onboarding & First-Run Copy

Standalone topic note for the onboarding flow copy + the feedback/ratings loop. Living artifact — iterate here. Decision + rationale captured atomically in [[decisions#2026-07-12-onboarding-copy--feedback--ratings-strategy]].

**Status:** copy drafted 2026-07-12 (English). Not yet wired into the UI or localized. 中文 pending (very different from English name/voice — see naming note below).

---

## Framework it targets

`hootowl/UI/onboard/` — a 3-page swipeable `TabView` (page style, custom pill indicator, eject/exit button). Pages map via `OnboardTab` enum: `ob0 → LandingScreen`, `ob1 → OnboardDebug`, `ob2 → ContentUnavailableView` ("under construction"). The three screens below are meant to replace ob0/ob1/ob2 content.

Design intent (per Jim): **nobody reads docs.** The onboarding is the forced "scroll-next" surface, so every screen must earn its swipe with minimal text (headline + one line + one owl aside).

---

## Copy constraints (locked 2026-07-12)

- **Scope: parking only.** Bus tracking exists in the app but is NOT sold here. Launch is Taipei + New Taipei (80/20); more cities *maybe*, gated on user feedback — so coverage copy is present-tense and honest, never a promise.
- **No app name in copy.** "HootOwl" is a working/project name that will likely change and will have a *very different* Chinese name. Use a `{APP}` placeholder if a name slot is unavoidable; prefer copy that needs no name at all. See [[app-name-is-a-placeholder]] (auto-memory).
- **Voice: playful owl mascot** — nocturnal, watchful, a little smug, privacy-respecting *in character*. The owl never says the app name, so it survives a rename.
- **Freshness honesty:** never claim a fixed update cadence. Source (city open data) publishes every ~2–5 min and publish timing is beyond our control. Copy ties freshness to *"the moment the city publishes"*, not to a clock. Protects against bad-faith "this is wrong/fraud" complaints.

---

## ⭐ REVISED 2026-09-05 — lane 3 chosen, and Cyclops promoted

**Jim's pick: lane 3, blunt/utilitarian.** His reasoning went further than tone:

> *"most of the app out there using Map, we do that too, but Cyclops is our differential feature (if it clicks, there will be clones, but that's life). 2 is OK too, but not Cyclops highlighting enough."*

That is a **structural** note, not just a voice note. In the earlier draft Cyclops appeared as four words on screen 2 ("Pin your regulars and I'll keep watch") — the differentiator buried inside a freshness message, while screen 1 sold coverage, which every competitor also has. So screen 2 is rewritten to be *about* Cyclops.

The owl asides mostly go with the playful lane. The two jobs they were doing are preserved as plain lines: freshness honesty moves into the Cyclops screen (where it now also describes the dimming behaviour shipped 2026-09-04), and the privacy reassurance becomes a short clause on screen 3. **The owl remains the app's identity elsewhere** — it is only out of the onboarding copy.

### Screen 1 — what it is
**Revised twice on 2026-09-07.** First pass dropped the city names on Jim's *"don't say we are two cities"*; he then corrected that it must still be clear where we are today: *"We cover Taipei and New Taipei City now, we will expand to other cities soon, and you can tell us where you need mostly. we will adjust our priorities."* Final copy carries **three beats — coverage now, expansion, the ask.**

> **Live parking. Right now.**
> Taipei and New Taipei City today — more cities soon.
> Tell us where you need it most — we'll adjust our priorities.
> **Request your city →**

⚠️ **`onb_s1_body` names the live cities**, so it is a maintenance dependency: shipping a third municipality means updating this string in **both** en and 中文, or the app understates its own coverage on its first screen.

**Superseded, in order:**
- *(2026-09-05)* Real-time space counts across Taipei and New Taipei. / — Not your city yet? **Tell us where to go next →**
- *(2026-09-07, first pass — no city names)* Live space counts, expanding city by city. / Tell us where you need it — we'll head there next.

### Screen 2 — why this one (the differentiator)
> **Your car parks. One screen.**
> Pin the lots you actually use. Open the app and every count is already there — no search, no map, no tapping around.
> Numbers fade as the data ages, so you always know how current they are.
> **▶ Watch how it works on YouTube →**  *(appears only while `tutorials.onboarding` is set in the remote config)*

*(Second line is the freshness-honesty message, now doing double duty: it describes the age-based colouring built 2026-09-04, so the copy and the app agree.)*

### Screen 3 — location + go
> **Find what's near you**
> Turn on location and the closest lots come first. Used only while the app is open — never in the background.
> **Enable Location**   ·   Not now

### Notes
- No app name anywhere — still a placeholder, and the 中文 name will differ. "us"/"we" carries it.
- **This is the English lane only.** 中文 is a separate call; a blunt English line does not force a blunt Chinese one.
- Screen 1's feedback link and the ratings loop below are unchanged.

---

## Superseded draft (playful lane, 2026-07-12)

## The three screens (final draft — owl voice)

### Screen 1 — hook + coverage/feedback
> **I keep an eye on every car park**
> Live spaces across Taipei & New Taipei — so you never circle the block again.
> 🦉 *Eyes open all night. You're welcome.*
> — Not your city yet? **Tell me where to fly next →**

Spicier headline option (use sparingly): **"Hoo still circles the block?"**

### Screen 2 — the value (freshness-honest)
> **Always the latest count**
> I grab each lot's newest numbers the moment the city publishes them. Pin your regulars and I'll keep watch.
> 🦉 *As fresh as the source allows.*

(The owl aside does the expectation-setting work; aligns with the in-app "Updated" timestamp / DQI a skeptic will see when they tap in.)

### Screen 3 — location + go
> **Point me at what's near you**
> Switch on location and I'll spot the closest parking first. Only while you're here — I don't follow you home.
> **Enable Location**   ·   Not now
> 🦉 *Night vision: on.*

("Only while you're here / I don't follow you home" = the privacy reassurance, in character, and literally true: `WhenInUse`, no `UIBackgroundModes`. Pre-priming the benefit + privacy right before the system dialog lifts opt-in.)

### Headline tone alternates (screen 1 sets the lane)
| Tone | Headline |
|---|---|
| Playful (chosen) | I keep an eye on every car park |
| Confident/clean | Know there's a space before you go |
| Blunt/utilitarian | Live parking. Right now. |

---

## Feedback channel — where "Tell me where to fly next →" goes

A path **Jim owns**, NOT App Store reviews. Simplest to ship first: `mailto:` (upgrade to a form if volume grows).

- **Subject (prefilled):** `City request`
- **Body (prefilled):**
  > Which city or district do you want parking for?
  >
  > Anything else you'd like the owl to do?
- **Owl confirmation after send:** 🦉 *Noted. I'll flap over when I can.*

Mirror in **Settings** so it's always reachable: **Request a city** (same mail) + **Send feedback** (general).

---

## Ratings loop — the App-Store-compliant version

Jim's original instinct was "suggest 5-star, collect city requests inside the review, and prioritize cities for 5-star reviewers." **That version is not viable** — it violates App Store rules (can't steer to 5 stars; can't offer incentives/priority in exchange for reviews = incentivized/gated reviews) and reviews are a terrible request inbox (no private reply/follow-up). Being "honest about it in onboarding" would just be documented evidence for a rejection.

**Compliant loop that gets the same outcome (decouple the two goals):**

| Goal | Channel | When |
|---|---|---|
| More 5-star ratings | Native review sheet (`@Environment(\.requestReview)` / `SKStoreReviewController`) — no custom text, no preset stars | A **win moment**, e.g. 3rd time a pinned lot shows available spaces. **Never in onboarding** (too early; burns one of ~3 prompts/year; drags average down). |
| City/feature requests | Owned channel (mailto/form) captured in Jim's inbox | The onboarding **Tell us →** nudge + Settings items |

- **Settings manual rate:** "Rate the app" → App Store write-review URL. Allowed, neutral, never gated.
- **The real lever:** prioritize cities by **counting demand** in the inbox (not by star rating), ship the most-requested, then **close the loop** with a one-time, non-gating notice:
  > 🦉 *You asked for Taichung. It's live — go take a look.*

  "You asked, we shipped" earns 5-stars far more reliably than asking, and is fully above board.

See [[app-store-ratings-and-feedback-policy]] (auto-memory) for the stance.

---

## Open / next

- [x] ~~Jim to confirm final screen-1 headline lane~~ — **lane 3 (blunt/utilitarian) chosen 2026-09-05**, with Cyclops promoted to its own screen. See the REVISED section at the top.
- [x] ~~Produce `Localizable.xcstrings`-ready key/value list (English filled, 中文 blank)~~ — **done 2026-09-06, written straight into `hootowl/Localizable.xcstrings`.** 17 keys (`onb_*` + `settings_*`), `extractionState: manual`, no `zh-Hant` object so Xcode shows them as untranslated. Two wording deviations from this note (the owl removed from the feedback body + confirmation, since lane 3 took the owl out of onboarding) — see [[00-onboarding-strings-batch]].
- [x] ~~Wire strings into `LandingScreen` (ob0)~~ — **done 2026-09-06.** Screen 1 renders `onb_s1_*` and the city-request link; `appDescription`, `UserGuide()`, and two pieces of dead view state removed. See [[01-landingscreen-wired]].
- [x] ~~Build out `ob1` (screen 2, Cyclops) and `ob2` (screen 3, location)~~ — **done 2026-09-06.** `OnboardPinsScreen` + `OnboardLocationScreen`, both wired into `project.pbxproj` for both targets. Screen 3's buttons exit through `OnboardScreen`'s own `onboardExit`, and retarget to **Open Settings** when location is already denied. See [[02-ob1-ob2-built]].
- [ ] **Device run of the three-screen flow** — in particular: does the iOS location dialog appear on screen 1 (because `handleAuthChange` auto-requests on `.notDetermined`) instead of on screen 3 where the copy sets it up? If so, screen 3's pre-priming is doing nothing. **← the open design question.**
- [ ] 中文 for the 17 new `onb_*` / `settings_*` keys.
- [x] ~~Decide feedback transport~~ — **`mailto:` 2026-09-06**, address served from a new optional `support` key in the Gist-backed `ContactConfig` (no hardcoded address, changeable without a release). **Jim owes:** add `"support": { "email": "…" }` to the Gist. See [[decisions#2026-09-06-city-request-feedback-rides-the-existing-gist-contact-config]].
- [ ] Implement the win-moment trigger for `requestReview` + the Settings "Request a city" / "Rate the app" entries.
