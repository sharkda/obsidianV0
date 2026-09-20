# HootOwl — Operations Guide

**Runbook for things you change *outside* the code.** Written to be followed cold, months later, without remembering any of it. Each section is self-contained: the exact URL, the exact steps, how to check it worked, and what happens if it goes wrong.

If you only read one line: **the remote config lets you change contact details and the tutorial video without an App Store release.**

---

# 1. The remote config (GitHub Gist)

## What it is

One small JSON file on a GitHub Gist that you own. The app downloads it **once per launch**, caches it, and works offline from the cache. Editing it changes the running app **with no build, no App Store review, and no release**.

- **Edit here:** https://gist.github.com/sharkda/1abaa9806dae0f34205725b51f21ad87
- **The app reads:** https://gist.githubusercontent.com/sharkda/1abaa9806dae0f34205725b51f21ad87/raw
- **In code:** `ContactConfig.gistRawURL` — `hootowl/network/ContactConfig.swift`

> [!info] Where the contact values come from
> The municipal contacts are published by each city's open-data portal and point at named civil servants, so they go stale silently. **Sources and a one-command re-check: [[data-sources]].**

## What it controls

| Key | Controls | If missing |
|---|---|---|
| `contacts.taipei` / `contacts.newTaipeiCity` | The phone + email behind the contact button on a parking lot (report bad data). Phone is a **fallback** — a lot's own number wins. | Button offers nothing |
| `support.url` | **Preferred.** Where **"Request a city"** goes — onboarding, and the outside-coverage screen. A hosted form or page. Opens in Safari. | Falls back to `support.email` |
| `support.email` | **Fallback only.** Same button, as a `mailto:`. Use if there is no form. | Link hides; on the coverage screen the ask line hides with it |
| `tutorials.onboarding` | Onboarding screen 2 **"▶ Watch how it works →"** | Button hides entirely |

## How to edit it — step by step

1. Sign in to GitHub as **sharkda**.
2. Open https://gist.github.com/sharkda/1abaa9806dae0f34205725b51f21ad87
3. Click **Edit** (top right).
4. Replace the contents with the block below, changed as you need.
5. Click **Update gist**.
6. Check it worked — paste the **raw** URL in a browser, or run:
   ```
   curl -sS -L "https://gist.githubusercontent.com/sharkda/1abaa9806dae0f34205725b51f21ad87/raw"
   ```
   You should see exactly what you just saved.

## The whole file — copy, paste, edit

```json
{
  "version": 2,
  "contacts": {
    "taipei":        { "email": "taipei@your-domain.com", "phone": "+886-2-..." },
    "newTaipeiCity": { "email": "ntpc@your-domain.com",   "phone": "+886-2-..." }
  },
  "support":  { "url": "https://your-form-url", "email": "you@your-domain.com" },
  "tutorials": {
    "onboarding": "https://youtube.com/shorts/PG4CUrdkb6k"
  }
}
```

`version` is only for your own tracking — bump it so you can tell at a glance which edit is live.

### `support` — which transport, and why `url` wins

Set **either or both**. When both are present the app uses `url` and ignores `email`.

**Prefer a hosted form.** `mailto:` needs a configured Mail account on the device; someone who uses only Gmail's app taps the button and *nothing happens*. That is the same dead affordance the placeholder address was pulled for, arriving by a different route. A form also gives you **countable rows** instead of free text in an inbox — and ranking cities by demand means counting.

**The app appends the screen that sent the user**, so requests can be told apart:

| Screen | URL the app opens |
|---|---|
| Onboarding screen 1 | `<your url>?src=onboarding` |
| Outside-coverage notice | `<your url>?src=coverage` |

`src=coverage` is the one to weight. That person opened the app **where it does not work yet** — a far stronger signal than a curious tap during onboarding. Anything that does not read the parameter ignores it harmlessly.

The `mailto:` fallback carries the same marker as a trailer in the body (`src: coverage`), a mail composer having nowhere else to put it.

> [!tip] A Facebook page is a valid `url`, with one caveat
> It must describe **this app**. A page whose title and description are about a different product reads, to a user who just tapped "Request a city", as the wrong place — and to an App Review reviewer, as unrelated to the app under review. Checked 2026-09-15: `facebook.com/tataroApp` returns 200 logged-out with no login wall, but its description is *"Tataro is the software company that created the Bobomofo Application"*. Fix the page identity before pointing the app at it. Reasoning: [[decisions#2026-09-15-a-city-request-goes-to-a-url-not-a-mailto]].

> [!warning] Not the same thing as the App Store Connect **Support URL**
> That is a separate field you fill in by hand in ASC, and it should point at something you own that renders for a logged-out stranger. A social page behind a login prompt is a bad answer to a field a reviewer will click.

### Why `tutorials` is keyed by name, not numbered

Videos are keyed by **where the button appears**, not `tutorial1` / `tutorial2`. A number tells neither you nor the app which video it is — and this file gets edited months apart. `"onboarding"` says exactly where it shows up.

To add a second video later, add another key:

```json
"tutorials": {
  "onboarding": "https://youtu.be/AAAAAAA",
  "cyclops":    "https://youtu.be/BBBBBBB"
}
```

⚠️ **The button says "on YouTube".** `onb_s2_tutorial_cta` names the destination so users know they are leaving the app — which means the copy asserts something the Gist controls. If a slot is ever pointed at Vimeo, a web page, or anything else, **the string must change with it** (English *and* 中文). Keep tutorial URLs on YouTube, or ask for the copy to be updated in the same change.

**The limit, so it does not surprise you:** a video only appears where the *code* asks for that key. Today the only slot that exists is `"onboarding"`. Swapping the video in an existing slot is pure config; putting a video somewhere *new* needs a small code change and a release. Ask for the slot to be added, then fill it in here.

## When does the change reach users?

- **Next app launch.** The fetch runs once per launch, so a user with the app already open keeps the old values until they relaunch.
- **Allow a few minutes.** GitHub's raw CDN can serve the previous copy briefly. If `curl` still shows the old file, wait and try again — it is not the app's fault.

## What happens if you get it wrong

**You cannot break one field by leaving another out.** Every key is optional and degrades on its own: omit `tutorial` and only that button disappears; omit `support` and only that link does. Unknown extra keys are ignored.

> This was **not** true until 2026-09-07. Swift's synthesized decoder demanded every key, so `"support": { "email": "…" }` with no `"phone"` threw and threw away **the entire config** — including the parts that were correct — leaving the app on stale cached values with nothing on screen to say so. Now hand-decoded field by field. See [[decisions#2026-09-07-the-remote-config-decodes-leniently-field-by-field]].

The one thing that still breaks everything: **invalid JSON** — a missing comma, a smart quote, an unclosed brace. Then the download fails to parse, the app logs an error, plays the error earcon, and keeps the last good cached copy.

**So: paste your JSON into a validator before saving.** https://jsonlint.com — or run `python3 -m json.tool` on it.

## Changing the tutorial video later

You cannot choose a YouTube URL, so changing the video means changing the link:

1. Upload the new video to YouTube.
2. Copy its URL. **Strip any `?feature=share`** — that is share-sheet tracking, not part of the address.
3. Replace the URL on the `"onboarding"` line, save the Gist, done.

To **remove** the video, delete that line (or the whole `"tutorials"` block). The button disappears; nothing else changes.

> If you ever want one link you can also put in the App Store description, on a poster, or in a QR code, use a redirect service for *that* link and put the redirect URL in `tutorial`. Never put a redirect in the app itself — the whole point of the Gist is that no link needs a release to change.

## Current status — 2026-09-09 (live Gist)

**Updated directly over SSH on 2026-09-09** (a Gist is a git repo; `git@gist.github.com:1abaa9806dae0f34205725b51f21ad87.git`). Every edit is a commit, so any change here is revertible from the Gist's own revision history.

```json
{ "version": 3,
  "contacts": { "taipei": { "email": "sb0457@gov.taipei", "phone": "02-27590666#6543" } },
  "tutorials": { "onboarding": "https://youtube.com/shorts/PG4CUrdkb6k" } }
```

| | Status |
|---|---|
| `contacts.taipei` | ✅ **real**, from the city's own dataset page — see [[data-sources]] |
| `contacts.newTaipeiCity` | ✅ **real** — `ae8131@ntpc.gov.tw` / `02-29702960` (the bureau's published parking line). See [[data-sources]] |
| `support.email` | **removed, not replaced.** `REPLACE-you@your-domain.com` shipped a *working* mail button to a domain that does not exist — a request would be written, sent, and vanish. Absent hides the link. ⚠️ **The onboarding prompt still renders**, so a user reads "tell us where you need it most" with nothing to tap. Owed |
| `tutorials.onboarding` | live, still Jim's personal test clip |

**Why the two were deleted rather than left:** a placeholder that *works* is worse than a missing key. The code was built to degrade field by field precisely so that absent means "hide the affordance", and that is the honest state until real values exist.

---

# 2. Release checklist

> [!tip] Only want the parts that need you? → [[jim-actions]]
> That note is the same items filtered to your accounts, your device, and your judgement, ordered so you can work through them one at a time. This section is the complete list, including everything I can do.

**Nothing here is done until it is ticked.** Items marked ✅-checked were verified against the repo on 2026-09-07; items marked ❓ need your judgement, not mine. Anything with 🔴 will get the build rejected or will actively mislead a user.

## A. Remote config — the Gist

*Editable without a release, so these can be done last — but they must be done.*

- [x] ~~Real municipal contact emails and phones~~ — **done 2026-09-09, live in the Gist.** Both cities carry real, sourced values; the fake numbers a user could dial are gone. Sources and re-check schedule: [[data-sources]].
- [ ] 🔴 **A city-request destination — `support.url` (preferred) or `support.email`.** ⬆️ **Updated 2026-09-15: `support.url` now exists, so this no longer has to be an email address.** A hosted form is the better answer; see the transport section above. Until one of the two is set, the "Request a city" button does not render anywhere, and the outside-coverage screen degrades to *"We're not here yet / Right now we cover Taipei and New Taipei."* — honest, but with nothing to act on.
- [ ] ~~🔴 **Real `support.email`.**~~ superseded by the row above. ✅-checked: still the literal `REPLACE-you@your-domain.com`. This is worse than leaving it blank — blank hides the link, a placeholder ships a *working* button that opens a draft to a domain that does not exist, so every city request silently bounces.
- [ ] 🔴 **The real tutorial video.** ✅-checked: `tutorials.onboarding` currently points at a personal test video, used to try the user experience. **Replace with the real how-it-works content before release.** Removing the key entirely is a safe fallback — the button just disappears.
- [ ] ❓ Bump `version` so you can tell at a glance which edit is live.

## B. Copy and localisation

- [ ] 🔴 **中文 for the 18 new onboarding strings.** ✅-checked: `onb_*` and `settings_*` keys are English-only; no `zh-Hant` object, so Xcode shows them as untranslated. A Chinese-locale user currently sees English onboarding.
- [ ] 🔴 **The app name.** ✅-checked and this one is subtle: `NSLocationWhenInUseUsageDescription` in `hootowl/Info.plist` reads *"**Hootowl** uses your location to find nearby parking lots."* That string is shown **by iOS in the permission dialog** — it is user-facing copy carrying a name you have said is a placeholder and whose Chinese version will differ. Onboarding was written to avoid naming the app; this string was missed. It is also **not localised** — Chinese users see an English system prompt.
- [ ] ❓ **`onb_s1_body` names the live cities** ("Taipei and New Taipei City today"). Correct today; must change the moment a third city ships.
- [ ] ❓ **`onb_s2_tutorial_cta` says "on YouTube".** Correct only while the tutorial URL is a YouTube link.

## C. App Store submission

*AdMob is staying (decided 2026-09-07), which settles the shape of this section. Banner ads are already built and working — test ad unit in DEBUG, real unit in release, hidden for subscribers. What is missing is the paperwork and the IDFA prompt.*

- [x] ~~Add `PrivacyInfo.xcprivacy` to the app target~~ — **done 2026-09-07.** `hootowl/PrivacyInfo.xcprivacy`, wired into the Resources phase of **both** targets. Contents were derived by auditing the source, not from a template:
      - `NSPrivacyTracking = true` — the app requests ATT and uses the IDFA for personalised ads when allowed.
      - `NSPrivacyAccessedAPICategoryUserDefaults` / **CA92.1** — `@AppStorage`, the snapshot cache, the config cache, the ATT counter; ~32 files, all this app's own data.
      - `NSPrivacyAccessedAPICategoryFileTimestamp` / **C617.1** — found by audit, not guessed: `Municipal+Fence.swift:70-71` compares `.modificationDate` to decide whether to re-copy the bundled `fences` file.
      - Audited and **absent**, so deliberately not declared: disk space, system boot time, active keyboards.
      **Two judgement calls recorded in the file itself, worth knowing:** `NSPrivacyTrackingDomains` is **deliberately empty** — iOS *blocks* requests to any domain listed there when ATT is denied, so listing Google's ad domains would stop even the non-personalised ads that should keep serving; Google's SDK handles this through its own manifest. And `NSPrivacyCollectedDataTypes` is empty because the app has no backend — **that is not the same as the App Store Connect nutrition labels**, which still have to account for what AdMob collects.
      **Verify before submitting:** Product → Archive → *Generate Privacy Report*, which merges this with GoogleMobileAds' own manifest.
- [ ] 🔴 **Wire ATT, or knowingly accept non-personalised ads.** ✅-checked: `NSUserTrackingUsageDescription` is **absent** from `Info.plist`, and `barebackAtt()` / `AttModel` in `ATTWarmup.swift` have **zero callers** — so the IDFA prompt never appears and every impression is non-personalised, at a materially lower eCPM. **Revenue is being lost by omission rather than by choice.** Two decisions: whether to prompt at all, and if so **when** — after onboarding, at a moment the user understands, never during it. ⚠️ Calling ATT before the Info.plist key exists is an **immediate crash**. *I can wire it once you pick the moment.*
- [ ] ❓ **Consent for EEA/UK users (Google UMP).** ✅-checked: no consent SDK present. Google requires a certified CMP to serve ads to EEA/UK users. Irrelevant if you restrict availability to Taiwan; required if you ship worldwide — so **decide your territories and this answers itself.**
- [ ] 🔴 **Privacy nutrition labels** in App Store Connect: precise location for app functionality, plus the advertising/tracking answers the AdMob integration implies.
- [ ] ❓ **Screenshots and description.** Coverage (Taipei + New Taipei City) belongs here — this is the surface a user reads *before* installing, and the reason onboarding does not have to carry the full disclosure.
- [ ] ❓ Version and build number. ✅-checked: `MARKETING_VERSION = 1.0`, `CURRENT_PROJECT_VERSION = 1`.
- [ ] ❓ Support / marketing URL and the privacy policy URL App Store Connect requires.

## D. Device verification still owed

*None of these have ever been run on hardware.*

- [ ] **The whole onboarding flow.** Three screens; "Request your city" opens Mail with the prefilled subject **(must be tested on a real device — Simulator has no Mail account)**; the video link opens YouTube; **Enable Location** and **Not now** both land in the app.
- [ ] **Where the location dialog actually appears.** `Municipal+Loc.swift:31-33` requests on `.notDetermined` as soon as the location manager wires at launch, which likely puts the iOS prompt on **screen 1** — before the screen 3 copy that exists to set it up. If so, screen 3 is a repair screen, not a primer. Decide whether that is acceptable.
- [ ] **Phase 3 lifecycle** — committed `aa6b02a` (2026-06-26) and never run: background/foreground refresh, lock/unlock no-thrash, `.inactive` no-op, app-switcher resume. Watch for `▶️ app → active: resuming GPS + 0 active proto timer(s)` — **zero** would mean resume is not restarting polling at all.
- [ ] **Cyclops 🕐 on a cache-less launch** — does the clock clear after ~15–20 s, or never.
- [ ] Log at `.notice` or above and read Console.app, or you will see nothing once the debugger detaches.

## E. Decisions to make before release (not necessarily fixes)

- [ ] ❓ **New Taipei's feed is ~30% live** — roughly 1,000 of 1,400 lots return −9 and render as no-signal. A 新北 user can open the app to a screen of blanks. Hide those lots, label them, or ship as-is? This is the single most likely source of "it doesn't work" reviews.
- [ ] ❓ **Every zone polls for every user.** `ActDeActOnes` has zero callers, so a Taipei user also polls New Taipei continuously. Costs battery and muddies any energy measurement. Tolerable at two cities; not at six.
- [ ] ❓ **`fences` file missing from the bundle** — `Municipal+Fence 92 — the file "fences" couldn't be opened`, repeating.
- [ ] ❓ **Ratings prompt is not implemented.** No `requestReview` anywhere. The agreed design is a native prompt at a win moment, never in onboarding.
- [ ] ❓ Subscription / IAP state — flagged as unsatisfactory in [[Jim's backlog]] and untouched this cycle.

## F. Cleanup (optional, none of it blocking)

- [ ] `UserGuide.swift`, `OnboardTab0.swift`, `OnboardDebug.swift` are unreferenced since the onboarding rewrite. Deleting them means removing their `project.pbxproj` entries too.
- [ ] **Three dead AdMob files.** ✅-checked: `Interstitials.swift` and `GadHostV.swift` are in the project navigator but in **no target's Sources phase**, so interstitials do not exist in the build — `Interstitials.swift` still uses the pre-v12 `GADInterstitialAd` symbol, which is likely why. `gAdBannerView.swift` is **not in the project file at all** and declares a `BannerView` that would collide with the SDK type. Delete them, or port `Interstitials.swift` deliberately if interstitials are wanted.
- [ ] `OnboardScreen.swift:26` still uses the deprecated `NavigationView`.
- [ ] The macOS target's Info.plist keys still carry Always-location strings, one of which is set to the **number** `1.0` rather than a string (`INFOPLIST_KEY_NSLocationUsageDescription`). macOS is not a shipping surface, so this is cosmetic — but it is wrong.
- [ ] Consider making the config reject obvious placeholders (an `@example.com` address, a `1234-5678` phone) so this class of mistake cannot ship again. ~4 lines in `ContactConfig`.

---

# 2b. Ads, IDFA and territories

## What the IDFA prompt actually is

**IDFA** is the advertising ID Apple gives each iPhone. Since iOS 14.5 an app must ask before using it, through **ATT (App Tracking Transparency)**.

The user sees a **system alert you cannot restyle**:

> Allow "…" to track your activity across other companies' apps and websites?
> **[ Ask App Not to Track ]   [ Allow ]**

The one line of explanation inside that alert is `NSUserTrackingUsageDescription` in `Info.plist` — **currently missing**, which is why the prompt can never be shown, and why calling ATT today would crash.

| Outcome | Effect |
|---|---|
| **Allow** | AdMob may use the IDFA → personalised ads → higher pay per impression |
| **Ask App Not to Track** | Ads still show and still earn — just non-personalised, worth less. **Nothing breaks.** |
| **Never asked (today)** | Same as denied for revenue, with none of the upside |

So the app is **already living in the worse case**. Expect a partial uplift from asking, not a transformation — a minority of users say yes.

**It shows once per install.** Decline is final unless the user goes to Settings, so the moment matters. To retest during development you must delete and reinstall.

**Apple's rules:** you may not gate app features on the answer, may not offer any incentive for allowing, and a "pre-prompt" screen explaining why is allowed only if it is not misleading and does not imitate the system alert.

**Moment: second launch — approved and built 2026-09-07.** The location prompt already fires on first launch (`Municipal+Loc.swift:31-33`), and stacking two system dialogs on a first-time user damages both. Second launch means they have seen the app work before being asked.

### How it is wired

| Where | What |
|---|---|
| `hootowl/Info.plist` | `NSUserTrackingUsageDescription` — the line shown *inside* the system alert |
| `AdMob/ATTWarmup.swift` | `attRequestIfDue()` — owns the launch counter and every guard |
| `App/hootowlApp.swift` | called on `scenePhase == .active`, `#if os(iOS)` |

Called on `.active` rather than at `init` because **iOS ignores the request unless the app is actually active**. It is safe to call repeatedly: it counts once per process (`attCountedThisLaunch`) and asks at most once per install.

**To change the moment**, move the call site or change `attPromptDueOnLaunch` — nothing else depends on the timing.

**To retest, delete and reinstall.** The prompt is once per install; after that the counter and the system's own answer both persist. Watch for `🎯 ATT:` in the log — it says on every launch whether it is waiting, asking, or already settled (logged at `.notice`, so it shows in Console.app on a device).

### The copy in the alert

> *This lets us show more relevant ads, which is what keeps the app free. Parking data works exactly the same either way.*

Deliberately says what the user gets and what does **not** change. Apple rejects vague wording, and forbids offering any incentive for allowing. ⚠️ **Not yet localised** — a Chinese-locale user sees this in English. Info.plist strings need an `InfoPlist.xcstrings`, which is the same change that fixes the location string, so the two are best done together once the app name is settled.

## Territories — where the app is sold

**Decided 2026-09-07/08. Ship to: Taiwan, US, Japan, Hong Kong, Macau.** (HK/Macau added 2026-09-08.) **Do not add EEA/UK or mainland China without doing the work in the gate table below first.**

⚠️ **App Store Connect defaults to *all* territories.** Availability must be set by hand, or the app ships into the EEA with no consent platform — the exact thing this decision avoids.

### "Can't I just ship everywhere and let it be blocked where it doesn't work?"

**No — and this is the question most likely to come back, so here is the answer in full.** Shipping everywhere is not a graceful degradation. Each excluded region fails differently:

| | What you might assume | What actually happens |
|---|---|---|
| **EEA / UK** | Ads quietly don't serve there | **A Google policy violation.** Since Jan 2024 Google requires a certified consent platform (CMP) to serve ads to EEA/UK users. Best case you lose revenue you never had; realistic worst case is **AdMob policy enforcement on the account — and account action is not scoped to the region that caused it.** Ads stopping *everywhere* is a far worse day than ads never starting in Europe. Separately, **GDPR applies to you as the publisher**, not only to Google. |
| **Mainland China** | Ships, ads don't load | **It does not ship at all.** Apple requires an **ICP filing (备案)** for apps on the China mainland App Store. It is a submission gate, not a runtime one. |

### The argument that actually settles it

**Including those regions buys nothing.** The app shows Taipei and New Taipei parking. Someone in Germany or Chengdu has no use for it — so you would be taking on policy and legal exposure in exchange for approximately zero downloads. It is not a cheap risk worth taking; it is a risk with no matching reward.

And excluding them costs nothing, because **availability is changed any time in App Store Connect with no new build.** Nothing is locked in.

### Gate table — read this before adding any territory

*Written for the version of you who has forgotten all of the above and is about to tick some boxes.*

| Want to add | Do this **first** | Needs a new build? |
|---|---|---|
| **Hong Kong / Macau** | ~~Nothing. Go ahead.~~ — **added 2026-09-08** | No |
| **EEA / UK** | Integrate **Google UMP** (a certified CMP) and ship a build containing it. Only then enable the territories. | **Yes** |
| **Mainland China** | Obtain an **ICP filing (备案)** — needs a Chinese entity or a filing agent. Note it earns nothing anyway: **Google is blocked in mainland China, so AdMob serves no ads there.** | No, but the filing gates submission |
| **Anywhere else** | Check two things: does that region have a consent regime, and does AdMob serve there? | Depends |

**Hong Kong and Macau are separate App Store territories from mainland China** — no ICP, AdMob works normally, and they already read your 中文. If Chinese-speaking reach is the goal, those are the ones to add; mainland China is not.

**Before adding anywhere, ask the honest question:** who there can actually use a Taipei parking app? If the answer is "nobody yet", the territory is adding risk and support burden for no users. Coverage should lead availability, not the other way round.

### Note on Hong Kong / Macau — added 2026-09-08

Genuinely zero-cost: no consent platform (Google's CMP requirement is EEA/UK-specific), no ICP, AdMob serves normally, and **`zh-Hant` already covers both** — iOS falls back from `zh-HK` to the Traditional Chinese strings.

Two small things, neither blocking:
- **Vocabulary differs slightly** between Taiwan and Hong Kong Chinese, so the strings will read as Taiwanese-flavoured. Understandable, not wrong — worth knowing if HK feedback ever mentions it.
- **The audience is travellers, not residents.** Taiwan is a major destination for Hong Kong visitors, which makes this arguably a *stronger* non-Taiwan market than US or Japan — it passes the "who there can use a Taipei parking app" test more convincingly. Expect some feedback in Cantonese-influenced Chinese.

The App Store listing falls back to the primary language in these storefronts unless a `zh-Hant` description is supplied — worth doing when the listing is written; not a blocker for availability.

### If ads ever stop everywhere

Check the **AdMob policy centre** first, before assuming a code bug. Region-triggered policy enforcement presents as ads dying globally, which looks nothing like its cause.

---

# 2c. Version and build numbers

**Version** = `MARKETING_VERSION` / `CFBundleShortVersionString` — user-facing, shown on the App Store.
**Build** = `CURRENT_PROJECT_VERSION` / `CFBundleVersion` — internal, seen in TestFlight and crash reports.

## The rules

| | |
|---|---|
| **Build never resets** | One integer, counting up for the app's whole life. `0.9` builds 1–6, then `1.0` continues at 7 |
| **Build has no leading zeros** | `1`, never `01`. `CFBundleVersion` wants plain integers |
| **A (version, build) pair is burned forever** | Even if the build is rejected, deleted or never used. Reuse gives *"The bundle version must be higher than the previously uploaded version."* |
| **Version only ever increases** | You cannot go back |

**Apple only *requires* build uniqueness within one version** — resetting across versions is technically legal. **Do not.** The case that bites: reset at `1.1`, then production breaks and you need `1.0.1` urgently. Builds 1–6 in that train are already burned, your counter says 3, and the upload is rejected at the exact moment you can least afford to think about it. A monotonic counter cannot reach that state.

## Jim's 0.9-for-TestFlight approach — 2026-09-11

**`0.9` while testing, jump to `1.0` for release. This works**, and the usual objection (*"0.9 looks unfinished"*) does **not** apply, because nothing below 1.0 ever reaches the App Store — only internal TestFlight sees it.

**The one real cost:** a TestFlight build can be **promoted directly to App Store review** — same binary, no re-upload, so the bytes you validated are the bytes you ship. Changing the version forfeits that: the `1.0` binary is a fresh build that nobody has tested.

Small risk, but non-zero — a rebuild picks up whatever else changed in the project meanwhile, which is exactly the class of problem this codebase keeps producing.

**So if keeping 0.9, do one short TestFlight pass on the actual `1.0` build before submitting.** The alternative is to use `1.0` throughout and promote the good build straight to review — simpler, and nothing untested ever ships. Either is defensible; the phase-signal of 0.9 has genuine value if it helps keep the stages separate.

## Expect to burn build numbers

Every TestFlight upload is a build. Every rejection needing a code change is a build. **Ten builds before a first release is normal.** They are free; do not be precious.

---

# 2d. Archiving and distributing — 2026-09-11

**There is only one upload destination: App Store Connect.** TestFlight is not a separate archive target; it is one of two things you can do with a build that is *already* in ASC. Same binary, same upload, no re-archive in between.

```
Archive → Organizer → Distribute App → App Store Connect → Upload
                              │
                     build processes (minutes–1hr)
                              │
              ┌───────────────┴───────────────┐
     TestFlight internal              attach to a version
     (no review, immediate)           → Submit for Review
```

**Uploading is not submitting.** Nothing reaches App Review until a build is explicitly attached to a version and Submit is pressed. A build that lands in ASC and sits there costs nothing and commits to nothing.

## ⚠️ The distribution menu trap

Xcode 26.6's *Distribute App* sheet contains **both** of these. They are not the same:

| Option | What it means |
|---|---|
| **App Store Connect**<br>*"Distribute on TestFlight and the App Store."* | ✅ **Use this.** Usable for internal TestFlight, external TestFlight, **and** App Store submission. |
| **TestFlight Internal Only** | ❌ The build is **permanently locked** to internal testers. Never external, never submittable. |

**"Internal only" is a decision about who receives the build** — made in App Store Connect by not adding an external group — **not a decision made at upload time.** Picking *TestFlight Internal Only* means a build that turns out to be good still cannot be shipped; it must be re-archived under a new build number for no reason but the menu choice. That option is for knowingly-throwaway builds.

This interacts directly with [[operations#jims-09-for-testflight-approach--2026-09-11]]: the value of promoting a tested TestFlight build straight to review only exists if the build was uploaded via **App Store Connect**, not *TestFlight Internal Only*.

## The `Upload Symbols Failed` warning — ignore it, permanently

Every upload produces this, and it will never stop:

> **Upload Symbols Failed.** The archive did not include a dSYM for the GoogleMobileAds.framework with the UUIDs […]. Ensure that the archive's dSYM folder includes a DWARF file for GoogleMobileAds.framework with the expected UUIDs.

**It is not an error and it does not block anything.** It comes from the *symbol upload* step, which runs **after** the binary has already been accepted. The build reaches App Store Connect and processes normally.

### Why there is no dSYM — Google ships none

*How the framework got here in the first place, and how to update it: [[admob-sdk]].*

Checked directly in `GoogleMobileAds.xcframework` (2026-09-14):
- **No `.dSYM`, no `.bcsymbolmap`, no DWARF anywhere** in the xcframework.
- The device slice is a **13 MB static `ar` archive** with **zero debug-map entries** — stripped.

There is no DWARF file in existence for this framework. The warning asks for something that was never shipped.

### Why it can never be satisfied, even in principle

The `GoogleMobileAds.framework` inside the app is **not** the prebuilt binary — it is a **~50 KB dynamic wrapper generated at build time** around Google's static library (it also carries the SDK's `PrivacyInfo.xcprivacy`, which is why the bundle exists at all). Its UUID is therefore **fresh on every single build**:

| Archive | GoogleMobileAds UUID |
|---|---|
| 2026-09-11 | `B2A2D1E5-2D93-34C9-B9AB-B2AD28FAB938` |
| 2026-09-12 | `A20F3F70-B1D3-34D7-868A-8C596901B9D4` |
| 2026-09-14 | `1FE6AE37-7368-3E14-946E-505B2B1C13D6` |

So even if Google published dSYMs tomorrow, they could not match — **the UUID the warning names did not exist until the moment you pressed Archive.** This is structural, not a misconfiguration.

### Nothing is wrong on our side

- `DEBUG_INFORMATION_FORMAT = dwarf-with-dsym` for Release — correct.
- **`hootowl.app.dSYM` is generated in every archive** (11 MB, UUID verified against the app binary). Our own code symbolicates fine.

### What it actually costs

If a crash happens **inside the ad SDK**, those stack frames show raw addresses instead of function names. Our own frames are unaffected. Since the SDK is Google's and its internals are not actionable anyway, the practical cost is close to zero.

### ⚠️ Do not "fix" it by unchecking *Upload your app's symbols*

That silences the warning by discarding symbolication for **our** code as well — trading something valuable for the absence of a message about someone else's library. Especially bad here: Xcode Organizer is currently the **only** crash channel (no Crashlytics or Sentry — see [[jim-actions]]).

**Verdict: expected output, every time, forever. Ignore it.**

---

## The sequence

1. Archive
2. Distribute App → **App Store Connect** → Upload
3. Wait for processing
4. ASC → TestFlight → add **yourself** as an internal tester → install
5. Do the metadata **in parallel** while it processes — see [[release-strategy#order-of-operations]]
6. Submission stays a separate, later, explicit decision

## Before pressing it

- **Export compliance should now be silent** thanks to `ITSAppUsesNonExemptEncryption` (committed `5411f69`). **If ASC still asks on this upload, the key did not take** — worth knowing immediately.
- **Internal testers** must be ASC team members with Admin / App Manager / Developer / Marketing role, up to 100.
- **Not parallelizable:** the **first subscription group is reviewed alongside an app version**, so the subscription's Traditional Chinese localisation in ASC is on the critical path for the real submission — though not for a plain upload.

## Why archive early, before the app is "finished"

An Archive is the only thing that type-checks the `#else` half of every `#if DEBUG`. On 2026-09-11 exactly that surfaced a Release-only compile error that every Debug build had silently skipped — `StoreObs.swift:270`, see [[bugs]]. Xcode also validates icons, entitlements and the privacy manifest at upload. All cheap early, all annoying late.

---

# 2e. App icons

> [!important] 👉 **The whole subject lives in [[app-icon]].**
> The alpha rule (`ITMS-90717`), the iOS squircle mask, the Icon Composer workflow, the **wiring step that makes a `.icon` file actually take effect**, verification commands and a troubleshooting table.

**The two-line version, so this page is not a dead end:**
- **The 1024 marketing icon must have no alpha channel.** `sips -g hasAlpha …/Icon1024.png` → must say `no`. macOS icons and Icon Composer layers are the **opposite** — transparency is expected there.
- **Adding a `.icon` file does not make it the icon.** `ASSETCATALOG_COMPILER_APPICON_NAME` must be changed too, for **both** targets. Nothing warns you.

---

# 3. Building and testing

> [!success] ✅ **Corrected 2026-09-20 — the command line CAN build this project, and has been able to since `a4a005b` (2026-09-14).**
> Everything below this callout used to say *"all builds are still Jim, in Xcode"*. **That is no longer true and has not been for a week** — every build of the 09-15 → 09-20 sessions was run from the CLI. The blocker was the dangling `ConcaveHull` package reference, and deleting it removed the last SPM dependency from the project. **There are now zero `XCRemoteSwiftPackageReference` entries**, so nothing has to resolve over the network, and a fresh clone builds. Ads are a vendored xcframework, not a package → [[admob-sdk]].

## The one environment line you need

```sh
export DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer
```

`xcode-select` points at `/Library/Developer/CommandLineTools`, so without this `xcodebuild` reports *"tool 'xcodebuild' requires Xcode"* and `simctl` appears missing. **No sudo needed.** Put it at the top of any script.

## The four builds

```sh
xcodebuild -project hootowl.xcodeproj -scheme hootowl -configuration Debug   -destination 'generic/platform=iOS Simulator' build
xcodebuild -project hootowl.xcodeproj -scheme hootowl -configuration Release -destination 'generic/platform=iOS' build
xcodebuild -project hootowl.xcodeproj -scheme hootmac -configuration Release -destination 'platform=macOS' build
xcodebuild -project hootowl.xcodeproj -scheme hootmac -configuration Debug   -destination 'platform=macOS' build
```

**Run the macOS ones even for an iOS-only change.** They are what prove the `#if os(iOS)` guards still hold — the AdMob xcframework has no macOS slice, so a dropped guard breaks `hootmac` and nothing else.

## Compiling is not enough — run it

This is not a stylistic preference. On 2026-09-15 an empty `@CommandsBuilder` closure **compiled clean and aborted at launch**, and the archive built from it was uploadable and unrunnable ([[bugs]]).

```sh
UDID=$(xcrun simctl list devices available | grep -m1 "iPhone 1[78]" | grep -oE '[0-9A-F-]{36}')
xcodebuild -project hootowl.xcodeproj -scheme hootowl -configuration Debug \
  -destination "id=$UDID" -derivedDataPath DerivedData/sim ENABLE_DEBUG_DYLIB=NO build
xcrun simctl boot "$UDID"; xcrun simctl bootstatus "$UDID" -b
xcrun simctl install "$UDID" DerivedData/sim/Build/Products/Debug-iphonesimulator/hootowl.app
xcrun simctl privacy "$UDID" grant location com.sharkda.hootowl
xcrun simctl location "$UDID" set 25.0340,121.5645          # Taipei 101 → covered, live pins
xcrun simctl location "$UDID" set 37.3230,-122.0322         # Cupertino → "We're not here yet"
xcrun simctl launch --console-pty "$UDID" com.sharkda.hootowl
```

**`ENABLE_DEBUG_DYLIB=NO` is required** — the preview dylib adds its own launch failures outside Xcode.

**Derive the UDID, never hardcode one.** Device ids differ per machine, and the available runtimes change with every Xcode update.

## Simulator gotchas, learned the hard way

- **This Xcode ships no `Simulator.app`.** `/Applications/Xcode.app/Contents/Developer/Applications/Simulator.app` does not exist, so there is **no way to tap the UI** from the CLI — you can install, launch and read the console, and that is all. Anything that needs a tap (the subscription sheet's policy buttons, the ATT prompt) has to go on Jim's device-pass list instead of being claimed as verified.
- **The ATT prompt becomes a zombie** once presented and unanswered: it survives terminate, reinstall and TCC edits, and with no Simulator.app there is nothing to click it with. `simctl erase` is the way out — a *first* launch never prompts, the gate being launch count ≥ 2.
- **`simctl spawn … defaults write` does not reliably reach the app's real preferences** — they live in the container plist and `cfprefsd` caches them.
- **The runtime set can change under you.** An Xcode or macOS update adds and removes simulator runtimes, so a destination that worked an hour ago can stop matching.

## ⚠️ Xcode.app rewrites the project file while it is open

Twice now (2026-09-16 and 2026-09-20) `project.pbxproj`, `Info.plist` and `Localizable.xcstrings` changed on disk with no human edit, because Xcode was open. On 09-16 it also silently bumped **`IPHONEOS_DEPLOYMENT_TARGET` 26.0 → 26.6**, which would have dropped every device below 26.6.

**`xcodebuild` itself does not do this** — the tree stayed clean across five CLI builds afterwards. It is the GUI.

**So: `git status` before trusting any build result, and again before archiving.** If the diff contains a deployment-target change nobody asked for, that is the signature.

## Other build-and-test facts

- **`mailto:` links do nothing in the Simulator** — no Mail account. Test anything that opens mail **on a real device**.
- **To see logs on a device**, log at `.notice` or above and read them in **Console.app** (select the device, filter category `ffl`). `.debug` and `.info` go through `print()`, which exists only while Xcode's debugger is attached and vanishes the moment it detaches.
- **Testing subscriptions in a non-English locale?** The StoreKit test configuration has its own `settings._locale` and `_storefront` (`hootowl/iAp/hootowl.storekit`). **They override the device language** for everything StoreKit draws. Set to `zh_TW` / `TWN` on 2026-09-10; if the store ever looks English on a Chinese device again, check there first.
- **DEBUG builds start with fake config values** and replace them with the live Gist as soon as the fetch lands. If the Gist lacks those keys you will see buttons **appear and then vanish** a second later. That is expected — fix the Gist, not the code.
- **`hoot_test_ui` does not build**, and has not since June. Pre-existing, no scheme, in no verification. It blocks nothing.
- **Historical note:** a `Package.resolved` in `farms/backup/hootowl` (April 2025) pins GoogleMobileAds and Google UMP — from the era when ads were an SPM dependency. It shows **Google UMP was once integrated here**, which is prior art if EEA/UK is ever opened up (see the gate table).

---

# 4. Adding a new city — not yet written

When a third municipality ships, this section should cover it. Known so far: `Municipal.loadOnStart()` adds and activates the protos, and **`onb_s1_body` in `Localizable.xcstrings` hardcodes the city names** ("Taipei and New Taipei City today") in both English and 中文 — it must be updated in the same change or onboarding understates the app's own coverage.

---

## Related
- [[bugs]] · [[unfinished]] · [[decisions]] · [[onboarding]]
