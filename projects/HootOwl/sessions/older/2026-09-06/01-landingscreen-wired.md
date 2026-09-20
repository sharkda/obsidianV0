# 2026-09-06 — `LandingScreen` (ob0) rewritten to the lane-3 copy

Continues [[00-onboarding-strings-batch]]. The strings existed; now screen 1 actually renders them.

**Working tree only, not committed, not compile-verified** — the CLI still cannot build this project (`Package.resolved` gitignored → SPM re-resolves `ConcaveHull` over the network). Four files, no new files, so no target-membership trap.

---

## What screen 1 is now

App name + parking symbol, then the copy, then the city-request nudge, then the paging footer:

> **Live parking. Right now.**
> Real-time space counts across Taipei and New Taipei.
>
> Not your city yet?
> **Tell us where to go next →**

## What came out

- **`appDescription`** — the 2024 paragraph ("An app that checks and monitor s available parking spaces in near real time…"). Replaced by `onb_s1_title` + `onb_s1_body`.
- **`UserGuide()`** — a scrolling `ugTitle`/`ugBody` block. The design intent in [[onboarding]] is explicit that nobody reads docs and each screen must earn its swipe; a scroll view of prose on the first screen is the opposite of that.
- **`@Environment(Interconnect.self) var interconnect`** — declared, never read.
- **`@State var tabId: Int?`** — an init parameter stored in `@State`, which SwiftUI ignores after first render, and unread anyway. Removing it meant one edit at the only call site (`onboardTabEnum.swift:34`, now `LandingScreen()`). The macOS call site (`AppScreen.swift:77`) already used `LandingScreen()`.

## What stayed, deliberately

- **The app-name hero**, with its `#warning("chinese app name ")` and the `zh → 車停對` override. The [[onboarding]] constraint is that no onboarding *copy* names the app — this is the identity block on the landing screen, not copy, and a landing screen with no identity at all reads as broken. The `#warning` still marks it as a placeholder.
- **`lnd_instruct_scroll_right` / `lnd_instruct_eject`** — they describe real, current affordances of `OnboardScreen`'s paged `TabView`, and lane 3 does not replace them.

## Two judgement calls worth knowing about

**1. The footer is now `#if os(iOS)`.** `LandingScreen` is not onboarding-only: `AppScreen.destination` renders it as the *entire* `.onboard` destination on macOS, where there is no paged `TabView` and no eject toolbar button. So on macOS both footer lines were instructions for controls that do not exist. Splitting on `os(iOS)` is the codebase's normal idiom (cf. [[feedback-clauthorization-platform-split]]) and this is the narrowest possible fix. It is still a behaviour change on macOS, which is why it is written down here.

**2. Headline is `.primary`, not white.** The existing footer on this screen uses `.white` and the gradient runs `primaryM → primaryContainer → surfaceContainerLowest`, which is light at the top — a white headline at `.largeTitle` risks disappearing in light mode. This is deliberately **the same call already made for `AvailFreshness.heroColor`**, which is still open for Jim ([[unfinished]] 🔴). If Jim picks literal white there, this line should follow it, and vice versa — they should not diverge.

## Feedback transport: decided, and it needed no new address

The link opens a `mailto:` draft. The address is **not** hardcoded — it comes from a new optional `support` key in the Gist-backed `ContactConfig`, the same mechanism already carrying the per-municipality data-quality contacts. Editable without an app release, cached offline, and it means no personal address is baked into the binary. Full rationale, alternatives, and the `Decodable` optionality trap: [[decisions#2026-09-06-city-request-feedback-rides-the-existing-gist-contact-config]].

Subject and body come from `String(localized:)` rather than `LocalizedStringKey`, because a `mailto:` needs a resolved `String` — which also means the 中文 values apply automatically once filled, with no second code path. (`MunicipalContactButton` solves the same problem with paired `@AppStorage` en/zh templates; that predates the string catalogue and is not worth copying.)

**Jim owes one thing:** add `"support": { "email": "…" }` to the Gist. Until then the nudge is hidden in release builds — `#if DEBUG` carries a `test-support@example.com` so it is always visible while developing, and a `.notice` fires after the fetch when the key is absent.

## Also called `fetchIfNeeded()` from here

`ContactStore.fetchIfNeeded()` was only called from `MncplCyclopsScreen` and `NbsScreen`. Onboarding can be the **first** screen a new install ever shows, so on a fresh launch the config would still be empty and the nudge would hide for the wrong reason. It is idempotent (`hasFetched` guard), so a third caller is free.

## Not done

- **ob1 / ob2 are untouched** — still `OnboardDebug` (IAP receipt + options) and a "under construction" `ContentUnavailableView`. Screens 2 (Cyclops) and 3 (location) are the next two.
- **`UserGuide.swift` and `OnboardTab0.swift` are now unreferenced.** Both are deletion candidates, but deleting means editing `project.pbxproj` target membership, which is Jim's to do in Xcode — hand-editing that file is how the 2026-07-12 phantom-build-error incident happened ([[bugs#2026-07-12-misleading-onchange-expects-01-arguments-error-was-a-missing-target-membership]]). Left in place.
- **`OnboardScreen` still uses the deprecated `NavigationView`** (`OnboardScreen.swift:26`), against the `NavigationStack` convention in `CLAUDE.md`. Out of scope for this change; worth doing when ob1/ob2 are built, since that file is about to be edited anyway.

## Related
- [[00-onboarding-strings-batch]] — the strings this consumes
- [[onboarding]] — copy source, REVISED section
- [[decisions#2026-09-06-city-request-feedback-rides-the-existing-gist-contact-config]]

---

## Added after Jim's review, same day

**macOS is not a shipping surface.** Jim, verbatim: *"the app is for iOS, we can ignore the macOS ones, just try to minimize any erros complaints for macOS will be fine."* So the `#if os(iOS)` footer split above is the right shape and the right amount of effort — keep macOS compiling, do not design for it, and do not raise macOS layout as a question. Applies to ob1/ob2 as they get built. Saved as an auto-memory (`feedback-ios-is-the-target`). This does **not** relax [[feedback-clauthorization-platform-split]].

**The `.primary` vs white question, resolved with evidence rather than taste.** Jim asked what the question even was, so it was checked rather than re-asked:

- `grep -rn "preferredColorScheme"` over the whole project returns **zero hits** — the app follows the phone's Light/Dark setting everywhere.
- The only forced dark scheme is `MncplCyclopsScreen.swift:164` (and its two sibling copies), and only while `pinningScreen` is true.

So literal white is safe only inside pinned Cyclops. Everywhere else — including onboarding — a white headline on the light end of the `primaryM → surfaceContainerLowest` gradient is white-on-light. And in Dark mode `.primary` already resolves to near-white, so choosing `.primary` costs nothing in the case the spec was actually picturing. **Recommendation recorded in [[unfinished]]: keep `.primary` in both places and close the item.** Reversing it later is one line in each of `CyclopsModel.swift:72` and `LandingScreen.swift:109`.
