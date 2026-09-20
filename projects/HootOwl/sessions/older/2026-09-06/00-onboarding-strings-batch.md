# 2026-09-06 — Onboarding strings landed in `Localizable.xcstrings`

First item off the onboarding list from [[01-resume-here]]. **Copy only — no UI wired yet.** This was the action that needed no decision from Jim, so it was taken directly.

---

## What changed

`hootowl/Localizable.xcstrings` — **17 new keys, English filled, 中文 deliberately absent.** 204 insertions, zero deletions; no existing entry touched.

| Key | English |
|---|---|
| `onb_s1_title` | Live parking. Right now. |
| `onb_s1_body` | Real-time space counts across Taipei and New Taipei. |
| `onb_s1_feedback_prompt` | Not your city yet? |
| `onb_s1_feedback_link` | Tell us where to go next → |
| `onb_s2_title` | Your car parks. One screen. |
| `onb_s2_body` | Pin the lots you actually use. Open the app and every count is already there — no search, no map, no tapping around. |
| `onb_s2_freshness` | Numbers fade as the data ages, so you always know how current they are. |
| `onb_s3_title` | Find what's near you |
| `onb_s3_body` | Turn on location and the closest lots come first. Used only while the app is open — never in the background. |
| `onb_s3_cta_enable` | Enable Location |
| `onb_s3_cta_skip` | Not now |
| `onb_feedback_subject` | City request |
| `onb_feedback_body` | Which city or district do you want parking for?\n\nAnything else we should add? |
| `onb_feedback_sent` | Noted. We'll get to it when we can. |
| `settings_request_city` | Request a city |
| `settings_send_feedback` | Send feedback |
| `settings_rate_app` | Rate the app |

Copy is verbatim from the **REVISED 2026-09-05** section of [[onboarding]] (lane 3, blunt/utilitarian, Cyclops promoted to its own screen), with the two deviations noted below.

## Choices made while transcribing

- **Key shape follows the existing catalogue.** `lnd_instruct_eject` / `lnd_instruct_scroll_right` already establish `prefix_snake_case` semantic keys read through `LocalizedStringKey("…")` in `LandingScreen.swift`. `onb_` / `settings_` continue that. The other 285 keys are auto-extracted English literals — not a convention to copy for new UI copy.
- **`extractionState: "manual"`** on every new entry. This is what keeps Xcode from marking them stale while no code references them yet — which is the case for all 17 today.
- **No `zh-Hant` localization object at all**, rather than an empty one. Xcode's catalogue editor then shows each as untranslated for 中文, which is the state Jim wants to work through. [[onboarding]] is explicit that 中文 is a separate call and a blunt English line does not force a blunt Chinese one.
- **Every key carries a `comment`.** Two of them exist to protect constraints that are easy to break in translation: `onb_s1_body`'s says coverage is present-tense and never a promise of future cities, and `onb_s2_freshness`'s says never to state a fixed update interval — the city controls publish timing.
- **Written byte-exactly in Xcode's own format.** Xcode's `.xcstrings` writer uses `"key" : {`, two-space indent, a blank line inside empty objects, and **no trailing newline**. A plain `json.dumps` reformats all 285 existing entries and buries the real change. The serializer used here was verified byte-identical against the untouched file before anything was added.

## Two deviations from the note, both small

1. **`onb_feedback_body`'s second question.** [[onboarding]] has *"Anything else you'd like the owl to do?"* — that line comes from the superseded playful lane. Lane 3 took the owl out of onboarding copy, so it reads **"Anything else we should add?"**. Same for `onb_feedback_sent`: the note's 🦉 *"Noted. I'll flap over when I can."* became **"Noted. We'll get to it when we can."** The owl is still the app's identity elsewhere — it is only out of this surface.
2. **The three `settings_*` keys were included** even though the feedback transport is still undecided. They are strings, not plumbing: [[onboarding]] already specifies the Settings mirror ("Request a city" / "Send feedback") and the neutral "Rate the app" entry, and the wording does not change between `mailto:` and a hosted form. That was the argument for picking `mailto:` first too.

## Not done

- **Nothing is wired.** `hootowl/UI/onboard/` is still the 2024 scaffolding — `LandingScreen` (ob0) shows `appDescription` + `UserGuide`, `ob1` is `OnboardDebug`, `ob2` is a "under construction" `ContentUnavailableView`. None of the 17 keys is referenced yet.
- **Feedback transport still undecided** — the standing recommendation is `mailto:` for v1. `onb_feedback_subject` / `onb_feedback_body` are ready for either.
- **Not compile-verified.** As always, the CLI cannot build this project (`Package.resolved` gitignored → SPM re-resolves `ConcaveHull` over the network). A string catalogue is data, not code, so the risk is a parse failure at build time; the file was re-parsed as JSON after writing, and the diff is purely additive.
- **Not committed.** Working tree change only.

## Related
- [[onboarding]] — the copy source, REVISED section
- [[01-resume-here]] — the 09-05 handoff this continues
- [[unfinished]] — standing list
