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

- [ ] Jim to confirm final screen-1 headline lane (currently playful owl).
- [ ] Produce `Localizable.xcstrings`-ready key/value list (English filled, 中文 blank) — offered, not yet done.
- [ ] Wire strings into `LandingScreen` (ob0) + build out `ob1` / `ob2` (currently `OnboardDebug` / "under construction").
- [ ] Decide feedback transport: `mailto:` first vs. a hosted form.
- [ ] Implement the win-moment trigger for `requestReview` + the Settings "Request a city" / "Rate the app" entries.
