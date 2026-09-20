# HootOwl — Decisions

Architectural and design decisions, with brief rationale. Newest at top.

---

<!-- Template:
## 2026-09-19 — Terms of Use links Apple's standard EULA, not a page of our own

**Decision:** both subscription screens point `termsOfService` at `apple.com/legal/internet-services/itunes/dev/stdeula/`.

**Why:** the app ships no terms of its own, and **absent a custom EULA that is the agreement that actually governs the subscription** — so this is the correct target, not a placeholder. Guideline 3.1.2 wants privacy *and* terms reachable before purchase; only privacy was ever wired.

**Alternatives rejected:**
- **Write a terms page on the Wix site.** Real work, and it would have to be maintained and localised, to restate what Apple's EULA already says for an app with no unusual terms.
- **Point terms at the privacy-policy page.** What the old policy effectively did — it claimed terms were *"accessible at bopomofo"*, a page that does not exist. Pointing a second button at the privacy page would have been the same evasion with a working URL.
- **Leave it.** `.policies` advertises the button either way; a reviewer finding one of two destinations missing on an auto-renewable subscription is a cheap rejection to avoid.

**Revisit if** custom terms are ever written — one constant, `LegalLink.termsOfUse`.

## YYYY-MM-DD — Short title
**Decision:** What was decided.
**Why:** Constraints/motivation.
**Alternatives considered:** What was rejected and why.
**Impact:** Files/areas affected.
-->

## 2026-09-16 — No custom domain; the "relay" is a form on the site that already exists
**Decision:** do not buy a domain. Keep the **free `jimhsuyc.wixsite.com/tataro` site**, and let a contact form / Messenger link on it be the channel users see. Keep a **dedicated, non-personal mailbox** for Apple only.
**Why the question came up:** Jim wanted users to reach him without his personal address being published — "a relay in the middle, for flexibility and security" — and asked whether that removed the need for a Wix page at all.
**What made it easy:** the Wix page is **not a new thing to add — it is already load-bearing.** `https://jimhsuyc.wixsite.com/tataro/privacy-policy` is hardcoded in `SubscriptionStoreView.swift:43` and `SubscriptionScreen.swift:202` and is what the subscription sheet opens. It returns 200 logged-out. **Apple accepts a `wixsite.com` URL** for both Privacy Policy URL and Support URL; a custom domain buys polish, not compliance. Wix's domain upsell can be ignored.
**Why a form *is* the relay:** the user types, it lands in whatever inbox it points at, and no address is published. Flexible (change the destination any time), secure (nothing to harvest), free, no domain. No separate relay service is needed.
**On replacing email with Facebook entirely — no, and the reason is specific:** App Store Connect's **App Review Information** requires a contact name, phone and **email**; Apple's reviewers use it. So an address exists regardless. The real question is only whether email is the channel *users* see, and there Facebook is defensible: Taiwan's FB/Messenger usage for reaching small businesses is genuinely high, it needs no Mail account, public answers compound, and a "which city next?" post collects +1s a form cannot. Against it: **Meta can disable the page** with no appeal, comments and DMs do not tally into a demand ranking, and a logged-out visitor cannot message.
**What makes the platform risk acceptable:** the destination lives in the Gist, so **the choice is reversible in two minutes with no app release**. If the page dies, repoint `support.url` and every installed copy follows. Without remote config this would be the wrong call.
**Blocked on one thing:** `facebook.com/tataroApp` renders fine logged-out but describes *"Tataro … the Bobomofo Application"*. Pointing a confused parking user at a page about a different product is worse than pointing them nowhere. Fix the page identity, or give the app its own page.
**Impact:** no code change — `support.url` from [[decisions#2026-09-15-a-city-request-goes-to-a-url-not-a-mailto]] already accepts any of these. Runbook: [[operations#support--which-transport-and-why-url-wins]]. Detail: [[privacy-policy]].

## 2026-09-15 — A city request goes to a URL, not a mailto
**Decision:** the remote config gains `support.url` beside `support.email`, and **the URL wins when both are set**. The transport is now an operational choice made in the Gist, not a code change. Requests carry the originating screen as `?src=onboarding` / `?src=coverage`.
**Why not mailto:** it needs a configured Mail account. Someone using only Gmail's app taps the button and nothing happens — the identical dead affordance the placeholder address was pulled for, arriving by a different route. It also produces free text in an inbox that has to be tallied by hand, when the stated goal ([[decisions#2026-07-12-onboarding-copy--feedback--ratings-strategy]]) is to **rank cities by demand** — which means counting.
**Why `?src=`:** a request from the outside-coverage screen comes from someone who opened the app **where it does not work yet**. That is a materially stronger signal than a curious tap during onboarding, and the two are worth telling apart when choosing the next city. Costs nothing; an unknown query parameter is ignored by anything that does not read it.
**Options weighed:**
- **Wix form — recommended.** Structured rows, no Mail-account dependency, does not publish Jim's personal address, and the ASC **Support URL** field needs an owned page anyway, so it does double duty.
- **Facebook page — good, for a different job.** Taiwan's FB usage is genuinely high and a "which city next?" post collects +1s that a form cannot. Rejected as the *primary in-app destination* for two reasons: FB increasingly walls content from logged-out visitors, which would fail hardest for a logged-out App Review reviewer; and `facebook.com/tataroApp` — checked 2026-09-15, returns 200 with no wall — describes **Tataro / Bobomofo**, not this app. Pointing a confused parking user at a page about a different product is worse than pointing them nowhere. **A Wix page can contain a Facebook link; a Facebook page cannot reliably contain a form** — one direction composes, the other does not.
- **Keep mailto only** — rejected for the funnel reasons above.
**Deliberately kept:** `support.email` as a fallback. It costs nothing and means the decision stays reversible from the Gist.
**Consequence:** the outside-coverage ask line renders only when a destination exists, so with neither key set the screen degrades to *"We're not here yet / Right now we cover Taipei and New Taipei."* — complete and honest, just without the payoff.
**Also:** `support` gets its own `SupportConfig` type rather than borrowing `MunicipalContact` — a municipal contact has a phone and no URL, this has a URL and no phone, and sharing meant a meaningless field on one side of every use. The Gist shape is unchanged and the file's lenient hand-decoding convention is followed, so a Gist written before `url` existed still decodes.
**Impact:** `ContactConfig.swift`, `LandingScreen.swift` (its private duplicate of the mailto builder removed), `CoverageNoticeView.swift`. Commit `9a7190c`. Runbook: [[operations#support--which-transport-and-why-url-wins]].

## 2026-09-15 — Coverage is one state on `Municipal`, and it never answers questions about age
**Decision:** `Municipal.coverage` (`locating` / `denied` / `outside` / `waiting` / `covered`) is the single source every screen reads to decide whether to explain itself. It answers **only** *"is there anything to show, and if not, why"*. **Age is not its business** — that stays `AvailFreshness`, computed in the view from an injected clock.
**Why one state:** the map, the list and the watch list were all empty outside coverage, for the same reason, with three different opportunities to disagree about it. That is the mistake the watch list made before `Municipal.defaultWatchList` became its single source ([[bugs#2026-09-05-fresh-install-all-screen-showed-3-pinned-lots-cyclops-showed-none-fixed]]).
**Why the split from freshness:** the app already has one freshness vocabulary (5 / 30 minutes, `AvailFreshness`, `lastConfirmed`) used by the Cyclops cells and the map pins. Folding "how old" into coverage would have produced a second one that could drift. Coverage is event-driven; freshness is clock-driven; keeping them apart keeps each honest.
**Why a stored `var`, not a computed property:** the inputs are `CurrentValueSubject`s. Reading `.value` from a computed property registers **no dependency with `@Observable`**, so no view would ever invalidate. It is recomputed at the four points that can change the answer — the location sink, the auth sink, the fence load, the first availability pack — and logged at `.notice` so a device sitting can read the transitions from Console.app.
**Alternatives considered:**
- **Per-screen checks** — rejected, three chances to disagree and three places to fix.
- **A computed property** — rejected for the invalidation reason above; would have looked correct and updated never.
- **Reading `activeFencesVbj`** — rejected. It is written by `assessFences`, which was destroying its own input, and by the integer-truncating `convexEnclosing`. Coverage reads `allFencesVbj` through the new correct test instead.
**Impact:** new `Municipal+Coverage.swift`, `CoverageNoticeView.swift`; `Municipal`, `Municipal+Fence`, `NbsScreen`, `MncplAllScreen`, `MncplCyclopsScreen`. Commit `fb28765`.

## 2026-09-15 — Outside-coverage names the cities and asks; the ask hides when it cannot be answered
**Decision:** the outside-coverage screen names the cities covered and offers the city request. **The ask line renders only when `support.email` is configured** — unlike `LandingScreen`, which keeps its prompt visible and hides only the link.
**Why the difference from onboarding:** on `LandingScreen` the prompt sits under other content, so a promise with no button is a small wart. On the coverage screen it would be the **last line on an otherwise dead-end screen** — the entire payoff turning out to be another dead end. Without an address it degrades to *"We're not here yet / Right now we cover Taipei and New Taipei"*, which is honest and complete.
**Why name the cities rather than say "Taiwan only":** someone in Kaohsiung is also outside coverage. "Taiwan" would be a lie by omission, and the list is derived from the loaded fences so it updates itself when a zone is added.
**Consequence for Jim:** the Gist `support.email` placeholder now gates **two** screens, not one. Still open on [[jim-actions]].
**Impact:** `CoverageNoticeView.swift`, `ContactConfig.cityRequestURL` (extracted from `LandingScreen` so both surfaces share it).

## 2026-09-15 — The map shows only the coverage states the user can act on
**Decision:** the map card appears for `.denied` and `.outside` only. `.locating` and `.waiting` are excluded there, though the list screens do show them.
**Why:** `.locating` is the state of every cold launch for the second or two before the first fix. A card that flashes on every launch is a card people learn to ignore, and it would be ignored in the one case that matters. The map also already carries its own transient chrome (the 🧊 stale pill, the auth banner).
**Why the list screens differ:** an empty list with no explanation is indistinguishable from a broken list, so there "waiting for live data" is genuinely informative. A map is never blank — it still shows where you are.
**Also decided:** the notice is a **compact card**, not a takeover. `ContentUnavailableView` expands to fill what it is given, which is right for an empty list and wrong floating over a map — it grew to nearly full height and read as an undismissable modal. The map stays pannable behind the card so a curious user can still look at Taipei.
**Impact:** `CoverageNoticeView.compact`, `NbsScreen`.

## 2026-09-14 — Release-risky cleanup goes on a branch, in commits that revert independently
**Decision:** The app-icon replacement and its surrounding cleanup were done on a branch (`icon-replacement`), split so that **each commit can be reverted on its own** — in particular the deletion of the legacy icon sets is its own commit touching nothing else. `main` was left untouched.
**Why:** Jim asked for the cleanup to be reversible. Deleting 41 tracked PNGs is the kind of change that is trivial to undo *if* a restore point exists and unrecoverable if it does not — and at the time nothing in the working tree was committed at all. Committing first turned an irreversible delete into `git revert <sha>`.
**Alternatives considered:**
- **Commit straight to `main`**, as every previous commit in this project has — still reversible via `revert`, but offers no way to abandon the whole line of work in one move while an unproven icon change is in flight.
- **One big commit** — rejected; it welds the delete to the Release-only bug fixes, so undoing the icons would also undo fixes needed to compile at all.
- **A scratch backup of the files** — was taken, but it lives in a session-temporary directory and is not a durable answer.
**Implementation:** five commits (`85e4a45` fixes → `eaf1acb` alpha strip → `7ab9cf0` new icon + wiring → `5eef4fc` delete → `98f1253` `.DS_Store`), plus a safety ref `backup/icon-replacement-pre-fold`. Folding a late fix into the first commit was done by rebuilding the branch with cherry-picks rather than `rebase -i`, which is unavailable in this environment.
**Caveat carried forward:** the branch is **not compile-verified**, and a Debug build exercises none of the fixed lines. Merge only after a successful Xcode **Release/Archive** build.
**Status:** branch open, awaiting that build. Full narrative: [[sessions/older/2026-09-11/01-session-wrap|sessions/2026-09-11/]].

## 2026-09-12 — Replace the owl app icon; adopt Icon Composer over a per-size set
**Decision:** Retire the owl app icon and replace it with `FindParkingTw.icon`, authored in **Icon Composer** and shipped as a `.icon` file, rather than maintaining the 20-PNG `AppIcon.appiconset`.
**Why:** Three independent reasons, only one of which was the upload failure.
- The old icon **drew its own rounded corners** and placed the owl's ear tufts inside the corner-radius zone, so iOS's squircle mask would have **clipped them** on every home screen.
- It carried **`yuchinghsu`** — a personal handle — across the artwork, in pink-on-pink already illegible at 1024px.
- It was an **owl**, the retired placeholder identity, on an app now called `Find Parking TW` / `找車位`. The icon was the last surviving piece of that identity and the most visible surface the app has.
The separate trigger was `ITMS-90717`: all 20 icons carried an alpha channel and `Icon1024.png` was 26% genuinely transparent, which blocked the first ASC upload.
**Why Icon Composer specifically:** the deployment target is **iOS 26.0/26.1**, so every user gets Liquid Glass and a flat legacy PNG would look a generation old. The tool also **owns the mask** — making the clipping failure impossible by construction — and generates dark / tinted / clear variants that would otherwise be drawn by hand.
**Alternatives considered:**
- **Fix the alpha and keep the owl** — rejected. It would have cleared the upload while leaving all three real problems shipping.
- **Single Size (one opaque 1024 PNG, Xcode 14+)** — viable and much simpler, kept documented as the fallback in [[app-icon]]. Rejected as the primary because it forfeits Liquid Glass on an iOS-26-only app.
- **Keep the per-size appiconset** — rejected; it is precisely what let one bad file block an upload.
**Consequence discovered immediately:** adding the `.icon` file does **not** make it the icon. `ASSETCATALOG_COMPILER_APPICON_NAME` must be changed for both targets, and the old set must not be deleted until that is verified. Pattern: [[swift-patterns#adding-a-file-to-the-project-is-not-the-same-as-the-project-using-it]].
**Status:** icon authored; **wiring not yet done** as of 2026-09-12. Full record: [[app-icon]].

## 2026-09-10 — App name: Find Parking TW / 找車位
**Decision:** The app is **`Find Parking TW`** in English and **`找車位`** in Chinese. Scope lives in the **App Store Subtitle**, not the name.
**Why not `Find Parking Taipei`, renamed later:** Jim asked whether to scope the name to Taipei now and widen it on expansion. Rejected for three reasons:
- **Renaming costs most exactly when you can least afford it.** The App Store name is changeable with a version submission, but the search ranking accumulated against the old name is not — and every link, review and word-of-mouth reference still points at it. That bill falls due at the moment of growth.
- **The Chinese name has no city in it.** 找車位 is scope-free, so scoping only the English half would make the two storefronts describe different products and force a rename of half the identity later.
- **The Subtitle field exists for exactly this** — 30 characters, shown under the name in search results, and changeable every release at no brand cost. `Taipei & New Taipei parking` (27/30). Someone searching "Taipei parking" still matches on it, so no traffic is lost.
**"TW" is a market marker, not a coverage claim** — it reads as *the Taiwan edition*, which is why it avoids the over-promise that `Find Parking Taiwan` would carry while covering two cities.
**When this would have gone the other way:** if expansion were expected to take years rather than months, "Taipei" would be honest for long enough to be worth the eventual rename. The New Taipei feed being ~30% dead is a hint that adding cities is not quick, so this is worth revisiting if a third city is still not in sight in a year.
**Implementation — one source of truth:** both names live in the new `hootowl/InfoPlist.xcstrings` as a localised `CFBundleDisplayName`. English and 中文 are deliberately **not** translations of each other. Removed: `Park-Chia` from build settings, the app name from the location permission prompt (iOS already prints the name above that line, so repeating it guaranteed staleness), and `LandingScreen`'s hardcoded 車停對, which was two names out of date and invisible to anyone editing the string catalogue.
**Also fixed by the same change:** `NSLocationWhenInUseUsageDescription` and `NSUserTrackingUsageDescription` are now localised, which was the last user-visible English in a Chinese build.

## 2026-09-08 — Ship to Taiwan, US and Japan only; EEA/UK and mainland China are gated
**Decision:** App Store availability is set by hand to **Taiwan, US, Japan, Hong Kong and Macau** (HK/Macau confirmed 2026-09-08). **EEA/UK and mainland China are excluded**, each behind a documented gate that must be cleared before they are ever enabled.
**Why not "ship everywhere and let it break where it breaks":** Jim's instinct — reasonable on its face — was that the app would simply be blocked where it does not comply, which they could live with. It does not degrade that gracefully:
- **EEA/UK is a Google policy violation, not a quiet block.** Google has required a certified consent platform (CMP) to serve ads to EEA/UK users since January 2024. The optimistic outcome is lost revenue in a region with no users; the outcome worth planning around is **AdMob policy enforcement on the account, which is not scoped to the region that triggered it** — ads stopping globally is a far worse failure than ads never starting in Europe. GDPR also applies to Jim as publisher, independently of Google.
- **Mainland China does not ship at all.** Apple gates submission on an **ICP filing (备案)**, which needs a Chinese entity or agent. It is not a runtime degradation.
**The argument that settled it:** including those regions **buys nothing**. The app shows Taipei and New Taipei parking, so a user in the EEA or mainland China has no use for it — the trade is policy and legal exposure for approximately zero downloads. Risk with no matching reward, rather than a cheap risk worth taking.
**Why excluding costs nothing:** App Store availability is changed at any time with **no new build**. Starting narrow is fully reversible, so there is no option value in shipping wide early.
**Alternatives considered:**
- **Ship worldwide and add UMP later** — rejected: it accepts the enforcement window in exchange for users who cannot use the app.
- **Add UMP now and ship worldwide** — rejected as premature. UMP is a small, well-understood integration; it should be done when an EEA audience actually exists, not speculatively.
- **Include mainland China for Chinese-speaking reach** — rejected; **Hong Kong and Macau are separate territories** with no ICP requirement, working AdMob, and existing 中文 support. They serve that goal without the gate.
**Standing rule recorded for future decisions:** before adding any territory, ask who there can use a Taipei parking app. **Coverage should lead availability, not the other way round.**
**HK/Macau, added 2026-09-08:** zero-cost in the literal sense — no consent platform (Google's CMP requirement is EEA/UK-specific), no ICP, AdMob serves, and `zh-Hant` already covers them via `zh-HK` fallback. Also the best-reasoned non-Taiwan market on the list: Taiwan is a major destination for Hong Kong travellers, which passes the "who there can use a Taipei parking app" test more convincingly than US or Japan do.
**Impact:** no code. App Store Connect availability (⚠️ which **defaults to all territories**), and the gate table in [[operations#gate-table--read-this-before-adding-any-territory]].

## 2026-09-07 — The remote config decodes leniently, field by field
**Decision:** `ContactConfig` and `MunicipalContact` get hand-written `init(from:)` using `decodeIfPresent` with defaults, instead of Swift's synthesized `Decodable`. Every key in the Gist is optional and degrades on its own.
**Why:** Swift's synthesized decoder calls `decode(_:forKey:)` for a non-optional property **even when the property has a default value** — defaults are not consulted. So `"support": { "email": "you@x.com" }` with no `"phone"` threw `keyNotFound`, and because one bad field aborts the whole container it discarded **the entire config**, including the fields that were correct. The app then silently kept serving stale cached values; the only trace was one `ffl(.error)` and an earcon.

This was not theoretical — it is exactly the JSON I handed Jim to paste, verified failing before the fix (`DecodingError.keyNotFound: Key 'phone' not found. Path: support`). It would have looked like "the new onboarding buttons don't work" and cost a debugging session on a config typo.
**Why it matters more than a normal robustness tweak:** this file is edited **operationally** — by hand, in a browser, months apart, by someone who has said plainly they will not remember the schema. An all-or-nothing decoder makes a forgotten key delete the whole configuration. It has to fail one field at a time or the mechanism is a trap.
**Alternatives considered:**
- **Document the required keys and move on** — rejected. It puts the burden on remembering a schema, which is the thing being designed around. The runbook now says "you cannot break one field by leaving another out", which is only honest because the code makes it true.
- **Make every property Optional** — works, but pushes `?? ""` into every call site and changes the public shape of the type for a decoding-only problem.
- **A third-party lenient-decoding helper** — a dependency for four fields.
**Implementation:** both inits live in **extensions**, deliberately: an initializer written in the struct body would suppress the memberwise init that `loadCached()`'s `#if DEBUG` branch uses. `CodingKeys` declared explicitly in each extension rather than relying on synthesis. Same file as the type declarations, per [[feedback-codable-synthesis-same-file]].
**Validation:** five cases verified with a standalone `swift` script before the change was trusted — the JSON handed to Jim, the Gist as it lives today, `{}`, a contacts entry missing `phone`, and the memberwise init still compiling. All pass. **Still not compile-verified inside the app** — the CLI cannot build this project.
**Impact:** `hootowl/network/ContactConfig.swift`. Operational consequences written up in the new [[operations]] runbook.

## 2026-09-06 — City-request feedback rides the existing Gist contact config
**Decision:** The onboarding "Tell us where to go next →" link opens a **`mailto:`** draft, and the address comes from a new optional **`support`** key in the Gist-backed `ContactConfig` — the same file that already carries the per-municipality data-quality contacts.
**Why:** [[onboarding]] left the transport open (`mailto:` vs. a hosted form) with `mailto:` as the standing recommendation because it ships today and migrating later does not change the copy. What was missing was *which address* — and hardcoding one in source means an app release to change it, plus a personal address baked into a shipping binary. `ContactConfig` already solved exactly that problem for the municipal contacts: a JSON blob on a Gist, fetched at launch, cached in `UserDefaults` so it works offline, editable without a release. Reusing it makes the address a config value rather than a code constant, and it costs four lines.
**Alternatives considered:**
- **Constant in `LandingScreen` behind a `#warning`** — matches the file's existing `#warning("chinese app name ")` idiom, but requires an App Store release to change the destination of the app's only feedback channel. Rejected.
- **A hosted form** — better once volume justifies it, but it is infrastructure to stand up and the copy is identical either way. Still the documented upgrade path.
- **Firebase Remote Config** — already rejected for this exact job in `ContactConfig.swift`'s own header comment; nothing has changed.
**Two details that matter:**
- `support` is **`MunicipalContact?`**, not a defaulted non-optional. Swift's synthesized `Decodable` throws `keyNotFound` for a missing key on a non-optional property *even when it has a default value* — so a defaulted `var support: MunicipalContact = .init()` would break decoding of the Gist as it exists today. Optional gets `decodeIfPresent` and stays backward compatible. (The same trap is latent on `version: Int = 0`, which the file's own doc comment shows being omitted in one example.)
- **No address configured → the nudge hides itself**, and a `.notice` fires after the fetch has had its chance. A visible link that opens nothing is worse than no link, but a silently absent affordance with no log is the invisible-failure pattern that cost the whole Cyclops arc. The `#if DEBUG` defaults in `loadCached()` gained a `test-support@example.com` so the link is always present while developing.
**Impact:** `hootowl/network/ContactConfig.swift` (`support`, `supportEmail`, DEBUG defaults, header doc), `hootowl/UI/onboard/LandingScreen.swift` (`cityRequestURL`).
**Owed:** Jim adds `"support": { "email": "…" }` to the Gist. Until then the link is hidden in release builds.
**Validation:** working tree only, not committed, **not compile-verified** — the CLI still cannot build this project.

## 2026-09-05 — Cyclops first-run seed: landmarks, from a single source
**Decision:** `Municipal.defaultWatchList` is the one place the first-run Cyclops watch list is defined, and it holds **landmarks** — 台北101 (`TPE0374`), 大安森林公園 (`TPE0095`), 府前廣場 (`TPE0096`).
**Why landmarks:** these cells are the first thing a new user sees, so their job is to *explain what the screen is*. The previous seed was three 文山區 lots — our neighbourhood, and meaningless to a user in 信義區 or someone visiting. All three replacements are large enough that the counts actually move, and they sit at very different occupancies, so the scarcity colouring visibly does something on first launch instead of showing three similar numbers.
**Why a single source:** the seed was a literal in two view files that could drift apart silently, and Municipal — which owns the list Cyclops renders — had no default at all. That combination produced a real first-run bug; see [[bugs#2026-09-05-fresh-install-all-screen-showed-3-pinned-lots-cyclops-showed-none-fixed]].
**Deliberate distinction:** a **missing** stored list seeds; an **empty** one does not. Unpin everything and the instructor view comes back. Resurrecting defaults under a user who cleared them would be worse than an empty screen.
**Also decided:** `MncplAllScreen` routes writes through `municipal.setWatchList()` rather than writing `@AppStorage` itself, so Municipal is the only writer. The `UserDefaults.didChangeNotification` observer in `Municipal+Cyclops` is now belt-and-braces rather than the actual sync mechanism.
**Not done:** `AllTpeParkingScreen` still takes its live list from `repository.pinnedPidVbj` — a genuinely separate legacy path. Only its seed literal was replaced. Rewiring it is its own job.
**Impact:** `Municipal+Cyclops.swift`, `MncplAllScreen.swift`, `AllTpeParkingScreen.swift`. Committed `881652b`.

## 2026-09-05 — Onboarding goes blunt/utilitarian, and Cyclops gets its own screen
**Decision:** Screen-1 headline lane = **3, blunt/utilitarian** ("Live parking. Right now."), and screen 2 is rewritten to be **about Cyclops** rather than mentioning it in passing. Full copy in [[onboarding]] under the REVISED section.
**Why (Jim):** *"most of the app out there using Map, we do that too, but Cyclops is our differential feature (if it clicks, there will be clones, but that's life). 2 is OK too, but not Cyclops highlighting enough."* The tone pick and the structural pick came from the same insight: the earlier draft sold **coverage** on screen 1 — which every competitor also has — and gave the actual differentiator four words on screen 2. Onboarding should lead with what only this app does.
**What changes beyond the headline:** the playful owl asides go with the playful lane. Their two jobs are preserved as plain copy — freshness honesty moves into the Cyclops screen (where it now also describes the age-based dimming shipped 2026-09-04, so copy and app agree), and the privacy reassurance becomes a clause on screen 3. **The owl remains the app's identity elsewhere**; it is only out of the onboarding.
**Alternatives considered:**
- Lane 1 (playful owl) — rejected by Jim; the mascot voice made the copy charming but left the differentiator unstated.
- Lane 2 (confident/clean, "Know there's a space before you go") — Jim: "OK too, but not Cyclops highlighting enough."
- Keeping Cyclops on screen 2 as a sub-point — rejected; that is what made lanes 1 and 2 feel undifferentiated.
- Leading with Cyclops on screen 1 — not taken. A new user needs the category promise before the twist; screen 1 says what it is, screen 2 says why this one.
**Scope note:** this is the **English** lane only. 中文 is unwritten and is a separate call — a blunt English line does not force a blunt Chinese one.
**Impact:** no code yet. `hootowl/UI/onboard/` is still 2024 scaffolding. Next: `Localizable.xcstrings` batch (English filled, 中文 blank), then wire `LandingScreen` (ob0) and build ob1/ob2. Feedback transport (mailto vs hosted form) is still undecided.

## 2026-08-31 — Cyclops availability freshness is derived from `MncplParkAvPack.converted`, never from the trail
**Decision:** Cache-seeded Cyclops numbers are colour-coded by age: `<5 min` keeps the existing scarcity colour, `5–30 min` → `.primary`, `≥30 min` → `.secondary`. The age comes from **`MncplParkAvPack.converted`**, plumbed per-lot into a new `observed: Date?` on `CyclopsItem` via a `parkId → converted` map built in `refreshCyclops()`. New `AvailFreshness` enum owns the thresholds.
**Why not the obvious source:** `carTrail.last?.time` is wrong in both directions. The trail only appends when the count *changes*, so an unchanged-but-fresh lot reads as old; and `CyclopsModel` isn't cached, so on cold launch `oldTrails` is nil and the trail stamps `Date()` onto disk-loaded data — making hours-old numbers look brand new. That is precisely the bug the feature exists to prevent. Written into the `AvailFreshness` doc comment so it isn't re-derived.
**Why no new persistence:** Jim's ask assumed the saved time needed saving. It already is — `MncplParkAvPack` is `Codable`, the cache stores whole packs, and `seedFromCache()` already restores `availableTime` from `converted`. No cache-format change, so no migration for existing installs.
**Why per-lot, not per-screen:** a watchList spanning Taipei + New Taipei has feeds landing minutes apart. Keyed by which pack actually contained the lot, not by `mncplInfo?.mncpl` — that is nil exactly in the degraded case where the freshness label matters most.
**Why a ticker:** staleness only matters when polling has stopped, which is when nothing emits to redraw. `TimelineView(.everyMinute)` — system-aligned, coalesces across cells, stops on background so it doesn't reopen the battery question.
**Deviation from the literal spec (Jim's call):** spec said "white"; implemented as `.primary`, and "grey" as `.secondary`. `MncplCyclopsScreen` only forces dark mode while *pinned*, so a literal `.white` number is invisible on an unpinned light-mode device. `.primary`/`.secondary` preserve the intended desaturation ramp (coloured → neutral → dimmed) in both schemes. One-line revert in `AvailFreshness.heroColor` if Jim wants literal white.
**Alternatives considered:**
- Add a new `savedAt` field to the cache envelope — rejected, `converted` already carries it per-pack and is strictly more precise than a whole-snapshot write time.
- Colour by `CachedSnapshot.written` — rejected; that's one timestamp for all municipalities and is only set on write, not on live updates.
- Staleness as a badge/label instead of recolouring the number — rejected for now; Jim asked for colour, and the hero number is the only thing read at a glance while driving.
**Impact:** `CyclopsModel.swift` (enum + `observed` + defaulted `observedAt:` param), `Municipal+Cyclops.swift` (the map), `CyclopsView.swift` (TimelineView + colour override), `MncplCyclopsScreen.swift` (toolbar timestamp on the same ramp). All new call-site params are defaulted, so `MncplCyclopsScreen0000` and the two Nbs construction sites compile untouched. **No new files** — `AvailFreshness` lives in `CyclopsModel.swift` to avoid the target-membership trap.
**Status:** working tree, **not committed, not compile-verified** (same `Package.resolved`/`ConcaveHull` CLI blocker as #5). Full write-up: [[01-cyclops-cache-freshness]].

## 2026-08-31 — Every session gets a dated working folder, created by default
**Decision:** Every working session opens a folder `projects/HootOwl/sessions/YYYY-MM-DD/` and writes its long-form output there as numbered notes (`00-where-we-left-off.md`, `01-<topic>.md`, …). **This is now default behaviour — Jim does not have to ask for it.** First folder: `sessions/2026-08-31/`. This supersedes the flat `sessions/YYYY-MM-DD-<topic>.md` file convention from [[decisions#2026-08-13-long-form-output-goes-in-the-vault-dated-session-notes-get-their-own-folder]]; the two existing flat notes (`2026-08-13-session-start.md`, `2026-08-17-status-reset.md`) stay where they are — dated notes are never rewritten.
**Why:** Jim's request, verbatim: *"maybe you can create the working folder using date like 2026-08-31 in the obsidian so I can go back anytime and check, can we make this default behavior in the future?"* Two motivations, both stated: the terminal is not Jim's reading surface for anything long, and they want to **return to it later**. A folder-per-date beats a file-per-date because a session usually produces more than one piece of long-form output, and piling them into one file — or scattering them across the flat `sessions/` list — loses the grouping that makes "what happened that day" answerable at a glance.
**Alternatives considered:**
- Keep one flat dated file per session — rejected; a session with a briefing *and* an investigation *and* an option menu has to either concatenate them or invent three sibling filenames with no visual grouping.
- Ask each session whether to create the folder — rejected; Jim explicitly asked for it to be default.
- Put the folder at vault root rather than under `projects/HootOwl/` — rejected; sessions are project work and other projects (Tesla, Miyazaki Trip) already live under `projects/`.
**Convention:** `00-` is always the session-start / where-we-left-off note. Later notes number upward in the order they were written. Notes are **immutable once written** — corrections go in a later note or in the forward-looking status notes, per [[decisions#2026-08-07-vault-correction-convention-fix-forward-looking-status-preserve-dated-entries]].
**Tooling:** written with direct file tools + `mkdir -p`, not MCP. Reinforced this session — **MCP `read-note` also stalls**, not just writes. Five parallel `read-note` calls hung past 120s and had to be killed; the same reads via `Read`/`grep` on `~/obsidianV0` returned instantly. **Go straight to direct file access for all vault operations, reads included.** Corrects the narrower "writes are the stall-prone operation" note in the 2026-08-13 entry.
**Permissions:** Jim also asked that vault writes happen *without prompting*. Memory alone can't do that — the prompt is a harness permission gate, not a behaviour choice. Added to `.claude/settings.local.json` (project-local, gitignored): `Read`/`Write`/`Edit` on `//Users/jimhsu/obsidianV0/**`, `Bash(mkdir -p|ls|find|grep …/obsidianV0/*)`, and `permissions.additionalDirectories: ["/Users/jimhsu/obsidianV0"]` so the out-of-tree vault is in scope. Previously only three narrow `Read` globs were allowlisted, which is why every write still stopped for approval.
**Impact:** No code. New folder `projects/HootOwl/sessions/2026-08-31/` + first note. Pointer callout in [[CURRENT]] updated. `.claude/settings.local.json` permissions extended. Auto-memory `feedback-longform-to-obsidian` and `feedback-skip-obsidian` updated.

## 2026-08-20 — `CLLocationManager` dedupe (battery #5)
**Decision:** `Municipal` creates exactly one `CLLocationManager`. The assignment in `init()` (`Municipal.swift:127`) is the canonical one; `wire0()` configures that instance rather than replacing it. The redundant `self.locationMan = CLLocationManager()` at the top of `wire0()` is deleted, with a WHY comment left in its place.
**Why:** `locationMan` is a non-optional `var` (`Municipal.swift:44`), so it *must* be assigned before `super.init()` — that constraint is real and the `init()` assignment can't simply be removed instead. `wire0()` then threw that instance away and built a second, which received all the configuration (`delegate`, `desiredAccuracy`, `distanceFilter`). The discarded one was never configured and never started, so this was pure waste, but it also left genuine ambiguity about which manager the lifecycle calls (`startUpdateLocation()` / `stopUpdateLocation()`, added in Phase 3) were acting on. Closing the last item on the pre-release shortlist.
**Alternatives considered:**
- Make `locationMan` optional / lazy so only `wire0()` creates it — rejected as a larger change touching every use site, for no behavioural gain.
- Leave it alone — rejected; it was already logged as the last shortlist item, and the Phase 3 lifecycle work made the ambiguity worth removing.
**Impact:**
- `hootowl/Municipalities/framework/Municipal.swift` — one line deleted from `wire0()`, two comment lines added. Exactly one `locationMan =` site remains project-wide (was two).
**Status:** Working tree only, **not committed, not compile-verified.** `xcodebuild` can't build from the CLI here — `Package.resolved` is gitignored, so SPM tries to re-resolve `ConcaveHull` over the network and fails (pre-existing since `dfa738f`, unrelated). Build once in Xcode. Full caveat in [[battery#decision-log-append-as-decisions-are-taken]].
**Battery note:** this is **code-health, not a battery win** — the GPS chip is shared, so two managers never drew double power. Recorded under #5 because that's where the shortlist tracked it.

See [[battery]] for the shortlist this closes.

## 2026-08-13 — Long-form output goes in the vault; dated session notes get their own folder
**Decision:** Long explanations — session briefings, investigations, plans, option menus — are **written into the vault**, not delivered as terminal output. The terminal reply is reduced to a short summary plus a pointer to the note. New folder `projects/HootOwl/sessions/` holds dated session notes named `YYYY-MM-DD-<topic>.md`. First note: [[2026-08-13-session-start]]. Jim also encouraged creating folders freely rather than piling new content into existing files.
**Why:** Jim's request, verbatim: *"I prefer you to write long statement into Obsidian for me to read, you can organize them into folders too."* The terminal is not Jim's reading surface — long output scrolls away, isn't searchable later, and doesn't survive the session. The vault is what Jim actually reads and what the next session loads at START.
**Why a separate folder rather than growing `CURRENT.md`:** [[CURRENT]] must read as *current*. Accumulating narrative inside it is precisely the mechanism that produced the stale Phase-3 and #5 claims corrected in the 2026-08-07 reconciliation — a status note that has become a journal stops being trustworthy as status. Dated session notes are append-only and can't become wrong later, so they can be as long as they need to be. This is the same principle already recorded in [[decisions#2026-08-07-vault-correction-convention-fix-forward-looking-status-preserve-dated-entries]], applied to a new content type.
**Division of labour across the vault:**
- `projects/HootOwl/sessions/` — dated briefings, investigations, long-form reasoning. **Immutable after writing.**
- [[CURRENT]] — short, current-state-only. Overwritten as things change. Now carries a pointer callout to the sessions folder.
- [[battery]], [[onboarding]], [[cyclops-first-run]] — standalone topic notes, updated **inline as work happens** (existing convention, unchanged).
- [[decisions]] / [[bugs]] — atomic entries, newest at top.
**Alternatives considered:**
- Keep writing long summaries to the terminal and let the vault hold only structured notes — rejected, this is the behaviour Jim asked to change.
- Put session briefings in `CURRENT.md` — rejected per the drift argument above.
- One rolling `sessions.md` file instead of one file per session — rejected; it would grow unbounded and lose the property that each note is a self-contained snapshot readable on its own.
**Impact:** No code. New folder `projects/HootOwl/sessions/` + first note; pointer callout added near the top of [[CURRENT]]. Saved to auto-memory as `feedback-longform-to-obsidian`.
**Tooling note:** MCP `create-note` stalled past 120s writing the first session note and had to be `TaskStop`ped; the note was written with the normal file tools instead. Reads via MCP were fine in the same session. **Writes are the stall-prone MCP operation** — go straight to direct file access for creates/edits, and `mkdir -p` parent folders yourself. Recorded in auto-memory `feedback-obsidian-mcp-config`.

## 2026-08-07 — Cyclops 🕐 fix sequencing: verify assumption + device run before any edit
**Decision:** The Cyclops first-run 🕐 bug was traced to root cause, but **no code was changed**. Fixes are gated behind two checks, in this order: (1) confirm `MncplParkItemAvail.parkId` carries the same `tpe_`/`ntpc_` prefix the watchList uses (`CyclopsModel.swift:112`); (2) one fresh-install device run to see whether the clock clears after ~15–20s or genuinely never. Only then apply the two one-liners.
**Why:** Static reading proves a **≥16s** blank window on any cache-less launch. It does **not** prove the reported *"forever"*. Shipping the fix and closing the bug without the device run risks declaring victory over 16 seconds while an indefinite stall (a `minuteFlow` bail-out at `Mu1Base+Ext.swift:144–177`) survives. Jim also chose to read the code himself before edits.
**The two staged fixes:**
- **Immediate `minuteFlow()` at the end of `activate()`** (`Mu1Base+Ext.swift:15–49`), mirroring what `resumePolling()` already does at `:78`. One line.
- **`allFencesVbj.send(enclosing)` → `activeFencesVbj.send(enclosing)`** (`Municipal+Ext.swift:135`). One word.
**Why fix #2 now despite being latent:** nothing currently reads `activeFencesVbj` for activation, so it does no damage today. But it *destructively narrows* the full fence list — a user outside all fences collapses `allFencesVbj` to `[]`, after which every `assessFences` throws `.noFences` permanently. It is a landmine directly under the planned multi-city expansion, and would surface as *"the new city doesn't work."* Cheap insurance.
**Alternatives considered:**
- Apply both fixes immediately and move on — rejected; would likely mask rather than resolve, and Jim wanted to review first.
- Fix only the clock and leave the fence typo — rejected; one word now vs. a confusing regression later.
- Treat it as a first-run-only cosmetic issue — rejected once the 24h cache expiry (`Municipal+Cache.swift:47`) showed it recurs routinely for episodic parking use.
**Impact:** No files changed. Full investigation: [[cyclops-first-run]]. Bug entry: [[bugs#2026-08-07-cyclops-shows-on-every-cache-less-launch-investigated-not-fixed]].

## 2026-08-07 — Fence-driven zone activation is an open design decision, not a patch
**Decision:** `ActDeActOnes(ids:)` (`Municipal+Ext.swift:165–175`) has **zero callers** and `activeIds` at `:158` is computed and discarded — the fence→activation link its own comment promises was never wired. **Do not wire it opportunistically.** Log it as an open decision and settle the activation policy deliberately.
**Why:** Turning it on changes *which zones fetch for whom* — a behavioural change with correctness, coverage, and battery consequences. It is not a bug fix. Wiring it while `Municipal+Ext.swift:135` is still broken would immediately break users outside covered fences.
**Current behaviour:** all protos activate unconditionally via `loadedProtos.map({ $0.activate() })` at `Municipal+Ext.swift:43`, so every user polls every zone regardless of location.
**Cost of leaving it:** (a) works against the #1/#6/#9/Phase-3 battery wins and **confounds the deferred Energy Impact measurement** — some measured drain is zones the user isn't in; (b) cost is linear in cities — tolerable at two, meaningful at six, plus multiplied load on public open-data endpoints that may rate-limit.
**Open questions to settle before implementing:** what activates a zone when location is unknown or permission is denied? Does a user near a boundary keep both zones warm? Is there a manual override for someone checking a destination city remotely?
**Sequencing:** fix `Municipal+Ext.swift:135` first — fence-driven activation is unsafe until `activeFencesVbj` is actually populated.
**Impact:** No files changed. Context: [[cyclops-first-run]] (Finding 3); confound warning added to [[battery]]'s measurement log.

## 2026-08-07 — Vault correction convention: fix forward-looking status, preserve dated entries
**Decision:** When vault notes drift from reality, correct **status and forward-looking claims** in place, but leave **dated journal/decision entries as originally written**. Record the discrepancy in a dated reconciliation section rather than editing history.
**Why:** Dated entries are a record of what was known and true on that date. Silently rewriting them destroys the ability to reconstruct how a decision was reached, and makes the notes untrustworthy in a subtler way than being out of date. Status claims, by contrast, are read as *current* and are actively harmful when stale — `CURRENT.md` telling the next session that Phase 3 was uncommitted would have caused real re-tread.
**Applied 2026-08-07/08 after verifying against `git log`:** Phase 3 committed `aa6b02a` (not uncommitted); #9 committed `04e2165` (not uncommitted); #5 target is `Municipal.swift:127` + `:169` (not 122/160 — file shifted); HEAD is `860f82d`, not `61eec92`.
**Impact:** [[CURRENT]] rewritten; [[battery]] status + option table + shortlist corrected, with a `[!info]` callout and a dated **Reconciliation — 2026-08-07** section; [[decisions]] defer-list line numbers; auto-memory `project_battery_drain.md` + `MEMORY.md` index hook (both would otherwise have re-seeded the error into future sessions). Dated Decision-log entries in [[battery]] left untouched by design.

## 2026-07-12 — Onboarding copy + feedback + ratings strategy
**Decision:** Author the 3-page onboarding flow (the `hootowl/UI/onboard/` swipe framework) as **parking-only**, **playful owl-mascot voice**, **no app name baked into copy**, with **freshness-honest** wording, plus a **compliant ratings/feedback loop** that decouples App Store ratings from feature requests. Full living copy in [[onboarding]].
**Why:** First-run is the only surface most users actually read ("nobody reads docs" — Jim), so it must be tight and do the persuasion + permission-priming + expectation-setting all at once, without over-promising.
**Key sub-decisions:**
- **Scope = parking only.** Bus tracking exists but is not sold in onboarding. Launch = Taipei + New Taipei (80/20); expansion is *maybe*, gated on feedback — so coverage copy is present-tense and honest ("Now live: Taipei & New Taipei"), never a promise.
- **Coverage limitation reframed as a request:** "Not your city yet? Tell me where to fly next →" turns "we don't cover you" into user agency + a demand signal.
- **No app name in user-facing copy.** "HootOwl" is a working name that will likely change and will have a *very different* Chinese name. Owl voice never says the name, so it survives a rename. Use `{APP}` placeholder only if a name slot is unavoidable. Saved to auto-memory as [[app-name-is-a-placeholder]].
- **Voice = owl mascot** (nocturnal, watchful, smug, privacy-respecting in character). Playful OK per Jim.
- **Freshness honesty (important):** never claim a fixed cadence. Rejected "Fresh numbers, every minute" — the source (city open data) publishes every ~2–5 min and publish timing is beyond us. Chosen: "Always the latest count / I grab each lot's newest numbers the moment the city publishes them" + owl aside "As fresh as the source allows." Protects against bad-faith "this is fraud" complaints and aligns with the in-app "Updated"/DQI timestamp.
- **Location screen** pre-primes benefit + privacy right before the system dialog ("Only while you're here — I don't follow you home"), which is literally true (`WhenInUse`, no `UIBackgroundModes`).
**Ratings/feedback — rejected vs. chosen:**
- **Rejected (Jim's initial instinct):** suggest 5-star, collect city requests inside the App Store review, prioritize cities for 5-star reviewers, and state this in onboarding. This violates App Store rules — you can't steer users to 5 specifically, must use the native review sheet (can't preset stars), and **can't offer incentives/priority in exchange for reviews** (incentivized/gated reviews). Reviews are also a poor request inbox (no private reply/follow-up). Documenting the deal in onboarding would be evidence for rejection.
- **Chosen (decouple the two goals):** (1) Ratings via native `@Environment(\.requestReview)` / `SKStoreReviewController` at a **win moment** (e.g. 3rd time a pinned lot shows spaces), **never in onboarding**; no custom text, no preset stars. (2) City/feature requests via an **owned channel** (mailto → later a form), captured in Jim's inbox. (3) Prioritize cities by **counting demand**, not by star rating, then **close the loop** ("You asked for Taichung — it's live") which earns 5-stars honestly. Settings gets "Request a city", "Send feedback", and a neutral "Rate the app". Saved to auto-memory as [[app-store-ratings-and-feedback-policy]].
**Impact:** No code yet — copy + strategy only. When implemented: `hootowl/UI/onboard/` (`LandingScreen`/ob0, build out `ob1`/`ob2`), a `Localizable.xcstrings` batch (English + blank 中文), a feedback transport (mailto/form), the `requestReview` win-moment trigger, and Settings entries.
**Status:** copy drafted, awaiting Jim's final headline-lane pick + the xcstrings batch. See [[onboarding]] for the living copy and open TODOs.

## 2026-06-25 — scenePhase pause/resume handler (Phase 3 — #2 + #3)
**Decision:** Pause GPS and the active protos' daily/minutely timers on `scenePhase == .background`, and resume them (plus one immediate availability fetch) on `.active`. `.inactive` is a deliberate no-op. Implemented per all four recommended answers from the 2026-06-24 pre-implementation brief: (1) `ReceiptObs.timer` left running, (2) immediate refresh on `.active` = yes, (3) wiring = direct calls from App root, (4) #2 + #3 shipped together. Closes the foreground-idle drain window (screen dimmed, app still foreground, GPS + timers running until iOS suspends ~5–30s; no `UIBackgroundModes` declared).
**Why:** The drain hypothesis is foreground-idle, not true background. #1 (GPS accuracy) and #6 (timer tolerance) reduced the per-tick cost; Phase 3 eliminates the wasted ticks entirely while the app is backgrounded. Pairs with Phase 2's cache: cold/resumed launches now seed from disk *and* kick an immediate live fetch on `.active`.
**Scope narrowed vs. the 2026-06-24 brief — only the Municipal-owned live path is touched (GPS + the active protos `TaipeiObs` / `NewTaipeiCityObs`).** The brief had proposed also adding pause/resume to `CyclopsObs` and `SourceBase`; on implementation both were deliberately left out:
- `CyclopsObs` drives the debug `CyclopsScreen2` and `Zone2 SourceBase` drives `ZoneRetrieveScreen` — both are view-local, only tick while their screen is visible, and are **not reachable from the app root**, so there's no handle to pause them from the lifecycle handler.
- Cyclops *display* refresh is driven by `parkInfoVbj` / `parkAvailVbj`, so pausing the proto timers already stops the cyclops network work indirectly.
**Alternatives considered:**
- Tear down on `.inactive` — rejected. `.inactive` fires transiently for alerts / Notification Center pull-down / multitasking; tearing down there causes thrash. Only `.background` tears down.
- NotificationCenter broadcast or a central `AppLifecycle` observable (brief options b/c) — rejected per recommendation (a). Phase 1b already made `Municipal` the central orchestrator; one `.onChange` covers GPS + the active protos' timers.
- Pause `ReceiptObs.timer` too — rejected (decision #1). Left running so StoreKit purchase retries can still validate during the brief background-before-suspension window; cost is a few timer fires.
- Skip the immediate `.active` refresh and let the next regular tick handle it — rejected (decision #2). Even with Phase 2's cache softening staleness, a resume fires one immediate fetch so counts are live, not up-to-a-minute old.
- Split #2 and #3 into separate changes — rejected (decision #4). They share the same handler; splitting doubles scaffolding for marginal safety.
**Implementation:**
- **New file** `hootowl/Municipalities/framework/Municipal+Lifecycle.swift` — `pauseForBackground()` (calls `stopUpdateLocation()`, then `activeProtos.forEach { $0.pausePolling() }`) and `resumeForForeground()` (calls `startUpdateLocation()`, then `activeProtos.forEach { $0.resumePolling() }`). Both log via `ffl(…,.info)`. File header documents the scope-narrowing rationale.
- `hootowl/Municipalities/framework/Mu1Proto.swift:72-76` — added `pausePolling()` / `resumePolling()` to the `Mu1Proto` protocol (default impls in `Mu1Base+Ext.swift`), so the lifecycle handler can iterate `activeProtos` generically.
- `hootowl/Municipalities/framework/Mu1Base+Ext.swift` — `pausePolling()`: `dailyTimerSubscription?.cancel()` + `minutelyTimerCancellable?.cancel()` then `minutelyTimerCancellable = nil` (so `setMinutelyTimer()`'s nil-guard re-creates it on resume); does **not** touch `isActive`/fence state; idempotent for rapid background→foreground cycles. `resumePolling()`: guards `isActive` (skips if inactive), then `startTimerRetrievDaily()` + `setMinutelyTimer()` + `Task.detached { await minuteFlow() }` for the immediate fetch.
- `hootowl/App/hootowlApp.swift` — added `@Environment(\.scenePhase) private var scenePhase` and a `.onChange(of: scenePhase)` on the root scene: `.active → municipal.resumeForForeground()`, `.background → municipal.pauseForBackground()`, `.inactive → break`, `@unknown default → break`.
- Immediate-refresh path uses the existing `minuteFlow()` (not `Repository.shared.netRetrieve(...)` as the brief had guessed) — `minuteFlow()` is the proto's own availability-fetch entry point.
**Idempotency / races:** `pausePolling()` is safe to call twice (double `?.cancel()` is harmless). `resumePolling()` is safe because the timer-start helpers already begin with `?.cancel()` (de-dup pattern). The `isActive` guard in `resumePolling()` prevents resuming a proto that was never started.
**Defer-list:** Phase 4 (Layer B2 — cyclops trail history persistence) and #5 (dedupe `self.locationMan = CLLocationManager()` at `Municipal.swift:127` + `:169` — line numbers re-verified 2026-08-07, previously recorded as 122/160) remain not started, both deferrable to post-launch.
**Validation:** Working tree only — **not committed**. New file `Municipal+Lifecycle.swift` is untracked; `hootowlApp.swift`, `Mu1Base+Ext.swift`, `Mu1Proto.swift` modified. Manual test plan before commit:
- Background for 30s → foreground → counts refresh visibly (immediate fetch fires).
- Lock → unlock quickly → no thrash, no torn-down state.
- Tap an alert / pull down Notification Center (`.inactive` fires) → nothing tears down.
- App switcher → return → GPS + timers resume.
- Force-quit + relaunch → clean cold-start path (no scenePhase fires; Phase 2 cache seeds).

See [[battery]] partition plan; supersedes [[battery#2026-06-24--phase-3-pre-implementation-brief-asked-jim-awaiting-answers]].

## 2026-06-24 — Disk cache for cold-launch / jettison recovery (Phase 2 — Layer B1)
**Decision:** Persist the latest user location and per-municipality `MncplParkAvPack` snapshot to `Library/Caches/hootowl-snapshot.json`. On Municipal init (before `wireCyclops()`), seed the in-memory `parkAvPack` dict and `userLoc2dVbj` from cache if the snapshot is < 24h old. Phase 2 of the battery investigation partition plan; entirely additive (no UI change, no behavior change for warm-starts).
**Why:** Phase 1b fixed warm switches (state survives view re-mount). But cold launches and post-jettison resumes still show empty cells because `parkAvPack` starts empty and the first availability fetch takes ≥1s. With cache, the user sees real numbers immediately; fresh data fades in seconds later. Foundation for Phase 3's `.active` re-read story.
**Alternatives considered:**
- `@AppStorage` / UserDefaults — rejected. Apple discourages larger blobs (parkAvPack can be 10-50KB per municipality); semantically wrong (this is regenerable cache, not preferences).
- `Library/Application Support/` — rejected for now. Survives iOS purges under storage pressure, but the data is regenerable and a parking app on a low-storage device has bigger problems than a re-fetch.
- Cache `actParkInfos` (static daily data) too — deferred. Large, changes rarely, daily timer re-fetches on next foreground tick. Separate decision.
- Write only on `.background` — rejected. Simpler to write on every update (one small write per minute); survives crashes; cost is negligible.
- Stale threshold of 1h / 7d instead of 24h — 24h chosen per Jim's call. Aligns with "user opens HootOwl ~once a day" intuition; tunable later if numbers feel stale or refreshes feel wasteful.
- Staleness badge UI — deferred per Jim's call. Cache infrastructure ships clean; badge ships later once Jim has felt the actual age distribution in real use.
**Implementation:**
- **New file** `hootowl/Municipalities/framework/Municipal+Cache.swift` — `wireCacheAndSeed()` (called from Municipal.init), `noteAvailabilityChanged()` (hook for actMinutely), `wireLocationPersistence()` (throttled 30s userLoc2dVbj sink), `writeSnapshot()`, `seedFromCache()`, `cacheFileURL()`. Plus `CachedSnapshot` + `CachedLocation` envelope types.
- `hootowl/Municipalities/framework/ParkAvailv02.swift` — added `Codable` to the `MncplParkItemAvail` and `MncplParkAvPack` struct declarations directly. Originally written as one-line empty extensions in `Municipal+Cache.swift`, which Xcode rejected: Swift only auto-synthesizes `Codable` when the conformance is declared in the same file as the type. Corrected 2026-06-24 in response to Jim's first compile pass. All members were already primitive Codable types, so no further work needed.
- `hootowl/Municipalities/framework/Municipal.swift:110` — `actMinutely(p0:)` ends with `noteAvailabilityChanged()` to persist on every availability update.
- `hootowl/Municipalities/framework/Municipal.swift:131` — init calls `wireCacheAndSeed()` *before* `wireCyclops()` so the cyclops Combine pipeline sees the seeded data on its first refresh.
- Disk format example: `{ "written": ..., "location": { "lat": ..., "lng": ..., "captured": ... }, "packs": [ { "converted": ..., "published": ..., "municipal": "tpe", "items": [{"parkId": ..., "cars": ..., "chargers": ...}, ...] }, ... ] }`. Written via `Data.write(to:options:.atomic)` to avoid torn-file reads.
- `cacheMaxAge: TimeInterval = 24 * 60 * 60`. Stale snapshots are silently discarded (logged at `.info`).
- `locationWriteThrottle: TimeInterval = 30`. The userLoc2dVbj sink uses Combine's `.throttle(for:scheduler:latest:)` to coalesce rapid GPS updates into one write per ~30s.
**Defer-list:**
- Staleness badge UI (`MncplCyclopsScreen` infoBar augmentation, `MncplAllScreen` row badging) — separate change, requires Jim's visual call + Localizable.xcstrings entries.
- `actParkInfos` (static daily data) caching — separate decision.
- On-`.active` re-read trigger — slots into Phase 3 (`scenePhase` handler). Currently the seed only happens at init (cold launch).
**Validation:** Working tree only, not committed. Pre-existing SourceKit index noise unchanged; the new file inherits the same `Cannot find type 'MncplParkItemAvail' / 'MncplParkAvPack' / 'Municipal' in scope` noise that all Municipal-area edits trigger this session, and downstream `Codable conformance` diagnostics are caused by those misses (not real issues). Manual test plan before commit:
- Cold launch with cached data present: verify counts appear immediately (no flash of empty) and refresh from network shortly after.
- Cold launch with no cache file: verify silent no-op, then normal first-fetch flow.
- Set system clock forward >24h, relaunch: verify cache is treated as stale (no seed), then normal first-fetch flow.
- Move the device significantly between launches: verify last cached location is used briefly until GPS gives a fresh fix.
- Pin/unpin during use: verify cache is written on next `actMinutely` tick (not lost on next launch).

See [[battery]] partition plan for context.

## 2026-06-17 — Cyclops state lifted to Municipal singleton (Phase 1b — Layer A)
**Decision:** Move `cyclopsMod`, `availableTime`, and `watchList` from `MncplCyclopsScreen`'s `@State` onto the `Municipal` `@Observable` singleton. `MncplCyclopsScreen` becomes a thin view that reads from `municipal.*` via `@Bindable` and pushes watchlist edits through `municipal.setWatchList(_:)`. This is Phase 1b of the battery investigation partition plan.
**Why:** The pre-fix `MncplCyclopsScreen` held all display state in `@State`, including the trail-bearing `cyclopsMod`. SwiftUI loses view identity when the host re-renders — `AppTabView` hosts tabs via dynamic `ForEach(AppScreen.sorted(subTier:))` and an auto-hide tab bar that re-renders body every 5s — wiping `@State` to defaults. The result was the user-visible "screen goes empty on quick switch out/in" bug. Lifting display state to the singleton eliminates the dependency on view identity entirely. Background: [[swiftui-state-and-identity]] in the patterns vault.
**Alternatives considered:**
- New `@Observable CyclopsBuilder` class injected separately — rejected per Jim's call: keeping it on `Municipal` is one fewer file, one fewer environment injection, and the cyclops concerns are already coupled to Municipal's data flow.
- Leave `watchList` on the view (`@AppStorage`-backed already survives @State reset) — rejected per Jim's call: consolidate the source of truth on Municipal even though it doesn't strictly need to move. Cleaner data flow and simpler future cache logic in Phase 2.
- Refactor `MncplAllScreen` at the same time — deferred. MncplAllScreen doesn't have the bug (it reads `municipal.actParkInfos` / `parkAvPack` directly). Its existing `@AppStorage saveWatchList` write pattern routes through UserDefaults, which Municipal now observes — so cross-screen pin/unpin keeps working without modification.
**Implementation:**
- **New file** `hootowl/Municipalities/framework/Municipal+Cyclops.swift` — `wireCyclops()` (called from Municipal init), `refreshCyclops()`, `setWatchList(_:)`, `loadWatchListFromStorage()`, `reloadWatchListIfChanged()`. Subscriptions stored in the existing `Municipal.cancelBag`. UserDefaults observed via `NotificationCenter.default.publisher(for: UserDefaults.didChangeNotification)` so writes from any screen flow into Municipal.
- `hootowl/Municipalities/framework/Municipal.swift:76-79` — added 3 stored properties: `cyclopsMod: CyclopsModel = .Zero`, `availableTime: Date? = nil`, `watchList: [String] = []`.
- `hootowl/Municipalities/framework/Municipal.swift:130` — added `wireCyclops()` call at the end of init.
- `hootowl/Municipalities/UI/MncplCyclopsScreen.swift` — rewritten. Removed `@State cyclopsMod`, `@State watchList`, `@State availableTime`, `@State cancellables`, `wire()`, `unwire()`, `loadWatchList()`, `refreshCyclops()`. Body reads `municipal.*` directly. `@Bindable var bindable = municipal` for `CyclopsView`'s `@Binding<CyclopsItem>` requirement. Reorder sheet extracted to `fileprivate struct ReorderSheet` with a local mutable list + push-on-edit via `municipal.setWatchList()`.
- `MncplAllScreen.swift` — unchanged.
**Validation:** Working tree only, not committed. Pre-existing SourceKit index noise unchanged; none of the diagnostics reference the new code. Manual test plan to run before commit:
- Open Cyclops with at least one pin → wait for parking counts to load.
- Switch to another tab → return within 5 min → counts should still be visible (the bug).
- Switch to another tab → wait > 5s (auto-hide tab bar trigger) → return → counts should still be visible.
- Background the app → return after a minute → counts should still be visible.
- Reorder sheet: move and delete should still persist across sessions.
- `MncplAllScreen` swipe-to-pin/unpin should still work, and the change should reflect in Cyclops immediately (Municipal observes UserDefaults).

See [[battery]] partition plan and [[swiftui-state-and-identity]] for the underlying SwiftUI behavior.

## 2026-06-15 — Drop Always-auth escalation + Info.plist cleanup
**Decision:** Stop auto-escalating from `.authorizedWhenInUse` to `requestAlwaysAuthorization()` on iOS, and remove the misleading `NSLocationAlwaysAndWhenInUseUsageDescription` key from `Info.plist`. Pre-release pick **#9** from [[battery#sorted-shortlist-low-hanging-fruit-first]].
**Why:** The escalation was triggering a second iOS dialog asking for Always-permission, but the app declares no `UIBackgroundModes` so Always provided zero actual background capability. The escalation was net-negative: misleading UX + App Store review risk (Apple flags apps that ask for Always without legitimate background usage). The Info.plist string further promised "background alerts" that the code never delivered. With escalation removed and the key gone, the app asks for `WhenInUse` only — honest, minimum-necessary permission.
**Alternatives considered:**
- Keep the key but rewrite the string to match reality — rejected. If the key exists, Apple may still surface the Always prompt path or scrutinize it at review. Cleaner to remove entirely.
- Also touch the macOS branch (relax `locAuthorized` to accept WhenInUse on macOS, then drop macOS escalation) — partly taken on 2026-06-16 by Jim: macOS `locAuthorized` (`Municipal+Loc.swift:53-56`) now accepts `.authorizedAlways || .authorizedWhenInUse`, matching iOS. The platform split (`#if os(iOS) / #elseif os(macOS)`) is preserved deliberately because `.authorizedWhenInUse` has historical macOS-availability complaints in Xcode — see [[feedback-clauthorization-platform-split]]. **macOS still escalates** (lines 38-39, 83-84) — dropping that is a follow-up candidate since the escalation is no longer load-bearing for `locAuthorized`, but it isn't actively harmful and was kept out of #9's scope.
**Implementation:**
- `hootowl/Municipalities/framework/Municipal+Loc.swift:34-37` — `handleAuthChange` case `.authorizedWhenInUse` wrapped in `#if os(iOS)`: iOS logs only, macOS still calls `requestAlwaysAuthorization()`.
- `hootowl/Municipalities/framework/Municipal+Loc.swift:75-78` — `requestLocationPermission` case `.authorizedWhenInUse` wrapped the same way.
- `hootowl/Municipalities/framework/Municipal+Loc.swift:79-80` — `case .authorizedAlways: fatalError("alreadyAlways")` replaced with a log. Latent crash if the user granted Always via Settings while the guard at line 66 raced; now a no-op log.
- `hootowl/Info.plist:7-8` — `NSLocationAlwaysAndWhenInUseUsageDescription` key + string removed.
**Flagged-then-resolved:**
- `hootowl/Municipalities/Nbs/NbsObsM+LocDel.swift:44` — was flagged on 2026-06-15 (`locMan.requestAlwaysAuthorization()` called directly from any auth state, with `locMan` storage commented out at `NbsObsM.swift:50`, suggesting dead code). Jim staged the file for deletion on 2026-06-16, validating the read. No remaining iOS `requestAlwaysAuthorization` call sites in the active codebase.
**Validation:** Working tree only, not yet committed. Manual test plan when verifying: launch app fresh on iOS → grant WhenInUse → confirm no second "Always" prompt appears.

See [[battery]] for the full investigation.

## 2026-06-13 — Add tolerance to Timer.publish (10% of interval)
**Decision:** Add `tolerance: <interval> * 0.1` to all active `Timer.publish` call sites that didn't already have it. Pre-release pick **#6** from [[battery#sorted-shortlist-low-hanging-fruit-first]].
**Why:** A non-zero tolerance on `Timer.publish` lets iOS coalesce timer fires with other apps' wake-ups, reducing CPU wake-ups and improving battery globally. Apple's documented recommendation is ~10% of the interval — small enough to be invisible UX-wise, large enough for meaningful coalescing. Effectively free win.
**Alternatives considered:**
- Fixed `tolerance: 2` to match the existing precedent in `TpeTrailObs.swift:112` — rejected. Fixed tolerance is fine for short intervals but wastes coalescing opportunity for the daily timer (interval up to 21600s = 6h). `interval * 0.1` scales naturally across the full range.
- Higher tolerance (e.g. 25%) — would coalesce harder but starts to feel unreliable. 10% is the documented sweet spot.
**Impact:**
- `hootowl/Municipalities/framework/Mu1Base+Ext.swift:66` — daily timer (interval 5s–21600s depending on `timerDailySoon`)
- `hootowl/Municipalities/framework/Mu1Base+Ext.swift:285` — minutely timer
- `hootowl/ViewModel/CyclopsObs.swift:42` — cyclops watch timer
- `hootowl/Municipalities/Zone2/SourceBase.swift:294` — zone retriever timer
- `hootowl/iAp/Receipe/ReceiptObs.swift:247` — StoreKit receipt retry timer
- Sites originally "left as-is" or "skipped" were all deleted in Jim's 2026-06-15 cleanup wave (so the leave-alone decision became moot via deletion): `ViewModel/TpeTrailObs.swift` (had `tolerance: 2`), `UI/Cyclops/deprecated/CyclopsScreen.swift` (deprecated, had `tolerance: 2`), `kitchens/ZoneRetrivers/zz_Ntpc_b08_ob.swift` (the `zz_` candidate I'd flagged for Jim's call).
**Status:** Functionally complete as of 2026-06-15. All 5 surviving `Timer.publish` sites have `tolerance: <interval> * 0.1`, no remaining ambiguous cases.
**Validation:** Committed in `837cbef` on 2026-06-15. No diagnostics raised on the edited lines.

See [[battery]] for the full investigation and the ranked option list.

## 2026-06-12 — GPS accuracy Best → HundredMeters
**Decision:** Change `desiredAccuracy` from `kCLLocationAccuracyBest` to `kCLLocationAccuracyHundredMeters` at all 5 active `CLLocationManager` configuration sites. This is pre-release pick **#1** from [[battery#sorted-shortlist-low-hanging-fruit-first]].
**Why:** Best-accuracy GPS is the single most expensive thing the app does — HundredMeters is roughly an order of magnitude cheaper. A parking-search app does not need sub-100m precision; `distanceFilter = 100` was already in place, so the existing UX expectation is already 100m-scale.
**Alternatives considered:**
- Keep Best on one or more screens that genuinely need it (e.g. turn-by-turn-ish navigation) — rejected on inspection; none of the 5 sites had surrounding context suggesting Best was load-bearing.
- `kCLLocationAccuracyNearestTenMeters` instead — overkill for parking search and would lose most of the battery savings.
**Impact (after 2026-06-13 cleanup reconciliation):**
- `hootowl/Municipalities/framework/Municipal.swift:163` — sole surviving site, now `kCLLocationAccuracyHundredMeters` with a brief inline rationale comment.
- 4 other originally-edited files were deleted by Jim's 2026-06-13 Obs-framework dedup cleanup (so the edits became moot via deletion): `Municipalities/Obs/MunicipalObs.swift`, `Municipalities/Nbs/NbsObs0.swift`, `kitchens/nearBySearch/NbsObs.swift`, `UI/Map/MyLocationObs.swift`. The deprecated `zzz/grog01.swift` (skipped during the edit) was removed in the same cleanup.
**Status:** Functionally complete as of 2026-06-13. Single live `desiredAccuracy` site, already correct. No further code change needed for #1.
**Side effect:** Active iOS `CLLocationManager()` instance count dropped 5 → 2 — partially pre-completes #5. The 2 remaining are both `self.locationMan = …` re-assignments in `Municipal.swift` at lines 122 and 160; likely 1-line dedupe.
**Validation:** Committed in `837cbef` on 2026-06-15 alongside the #6 edits and Jim's 2026-06-13/15 cleanup waves. Pre-existing SourceKit index noise unchanged; none of the diagnostics reference these lines or `CLLocationManager`.

See [[battery]] for the full investigation and the ranked option list this came from.

## 2026-06-10 — Disambiguate colliding district names by nearest user location
**Decision:** When `AddressSearchObs.normalized(_:)` is extended past Taipei + New Taipei, resolve 區-name collisions by picking the candidate city whose centroid (or nearest loaded `MncplParkItem`) is closest to the user's current location — not by first-match-wins ordering. This promotes option (c) in [[swift-patterns#taiwan-address-pre-normalization]] from "one of three" to the chosen rule.
**Why:** HootOwl is a "what parking is near me" app — the user's location is almost always available and is the strongest disambiguation signal. The "user searching a far destination" failure mode is uncommon here and is already covered by the 市/縣 escape hatch.
**Alternatives considered:**
- First-match-wins ordering — rejected, silently wrong for shared districts.
- Remove colliding names from all Sets to force loud failure — rejected, punishes the common case to handle the rare one.
- `completer.region.center` biasing only — covers typeahead but not the `CLGeocoder` fallback path; explicit nearest-city choice covers both.
**Required fallbacks:**
- Location unavailable (first launch, permission denied, indoors with no fix): return the query unchanged so the geocoder fails loud and the user is prompted to type 市. Do NOT default to a first-match guess — that recreates the original bug.
- Border-zone correctness (e.g. southern 基隆 vs 台北): rank by nearest-known-parking-lot distance using `MncplParkItem` coordinates when lot data is loaded; centroid distance can flip the wrong way near city lines.
- Query already contains 市/縣: skip normalization entirely (current behavior preserved — `台中市信義區` always routes to Taichung).
**Impact (when implemented — not done yet, code change is deferred):**
- `hootowl/Municipalities/Nbs/AddressSearchObs.swift` — `normalized(_:)` switches from ordered `Set<String>` checks to a `[district: [MunicipalEnum]]` lookup + distance ranking. Needs read access to `MyLocationObs.clLoc.location` (or equivalent) at normalization time.
- The MARK warning block in `AddressSearchObs.swift` should be rewritten to describe the chosen rule, not the three-option menu.

See [[bugs#2026-06-09-district-prefixed-taiwan-addresses-silently-dropped-by-apple-geocoder]] and [[swift-patterns#taiwan-address-pre-normalization]].

## 2026-06-09 — Taiwan address normalization for Apple geocoder
**Decision:** Before passing user-typed Taiwan addresses to `MKLocalSearchCompleter` or `CLGeocoder`, run them through `AddressSearchObs.normalized(_:)`, which prepends `台北市` / `新北市` when the query starts with a known 區 and contains no 市/縣 marker. The search bar still shows the original user input.
**Why:** Apple's geocoder returns nothing for Taiwan addresses that lead with a 區 only (e.g. `北投區中央北路2段350巷66號`). The same address resolves cleanly with the city prepended. This is a quiet failure mode — users get an empty result and no signal that they need to add the city.
**Alternatives considered:**
- Show an error/hint asking users to add 市/縣 — rejected, worse UX than silently normalizing.
- Use `completer.region` bias only — insufficient on its own; geocoder still returns nothing without the prefix.
**Impact:**
- `hootowl/Municipalities/Nbs/AddressSearchObs.swift` — `taipeiDistricts`, `newTaipeiDistricts`, `normalized(_:)`, `query.didSet`.
- `hootowl/Municipalities/Nbs/NbsScreen.swift` — `geocodeAndSearch` passes `normalized(query)` to `CLGeocoder().geocodeAddressString(_:in:)`.

See [[swift-patterns#taiwan-address-pre-normalization]] for the collision trap when adding more cities.
