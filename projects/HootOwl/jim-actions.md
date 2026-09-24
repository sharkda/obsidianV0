# Jim's action list — release

**The only list of things *you* have to do.** One place, worked through one at a time. Detail for any item is a click away; this note is deliberately short.

Tick items as you go. Nothing here needs the terminal or a conversation to resume — each item says what to do, where, and how you know it is done.

> [!note] What belongs where
> - **This note** — only things that need *you*: your accounts, your device, your judgement.
> - [[operations#2-release-checklist]] — the full checklist including everything I can do.
> - [[operations]] — how-to steps (editing the Gist, testing).
> - [[unfinished]] — engineering work not tied to release.
> - [[Jim's backlog]] — bugs you want to work on with me.

---

> [!tip] 🗺️ [[INDEX]] maps the whole folder — which note answers which question.

> [!tip] 👉 The plan, as opposed to the list: [[release-strategy]]
> TestFlight-vs-release, the order of operations, what a reviewer will poke, and the one rejection I would bet on. Read that first; this note is what to tick.

> [!warning] 🔴 New 2026-09-15 — **the archive you already uploaded cannot launch**
> Xcode updated itself from 26.6 to 27.0, and under 27 the app aborted at startup on a construct that compiled fine before ([[bugs#2026-09-15-the-app-could-not-launch-under-xcode-27-an-empty-commands-closure-fixed]]). Fixed and verified running. **But the 09-14 archive was built by the old toolchain and contains the broken binary — do not submit it. Archive again.** Build numbers are a counter, not a statement; burn another.

> [!success] ✅ 2026-09-16 — everything is pushed
> `origin/main` = `9a7190c`. The icon replacement and the whole 09-15/16 session are on GitHub. Nothing lives only on the laptop.

> [!danger] 🖥️ You updated macOS — **re-verify before trusting any "it builds" note**
> If Xcode changed, every verification in this vault expired, exactly as it did between 09-14 and 09-15. The worst breakage last time **compiled clean and crashed at launch**, so compiling is not enough — run the app too. Commands: [[02-pick-up-here|sessions/2026-09-15/]].

> [!warning] 🔴 The 09-14 archive cannot launch — **archive again before you submit**
> It was built by Xcode 26.6 and contains the `.commands` crash. Build numbers are a counter, not a statement; burn another.

## Privacy policy — the *page* has no 🔴 left, but the subscription flow does (checked 2026-09-18)

Live at https://jimhsuyc.wixsite.com/tataro/privacy-policy. Full review, and a table of **what the app actually does with data verified against the source**, in [[privacy-policy]].

- [x] ~~Add location, AdMob/IDFA, Apple-purchases and geocoding disclosure~~ — **done in your 09-16 revision.**
- [x] ~~🔴 **Scope the AdMob sentence.**~~ — **done in your 09-18 revision**, pasted verbatim. The policy no longer contradicts its own ATT prompt. **No 🔴 findings remain on the page.**
- [ ] 🟠 **The headline claim is still Bopomofo's** — "collects only 'name'" is the first thing under *Information Collection and Use* and is **false for this app**. Worse than it looks: the opening paragraph lists `FindParkingTW` under *both* Commercial and Ad-supported, so the "paid edition lets you input a name" paragraph reads as applying here. **Put the app name in front of each claim.**
- [ ] 🔴 **There is no Terms of Use — anywhere.** Not a link on the policy page (*"accessible at bopomofo"* is plain text), **no Terms page on the site** (the sitemap is four pages), and **no terms link in the app** — only the privacy policy is wired into both subscription screens. Guideline 3.1.2 wants both beside an auto-renewable subscription. **You do not have to write one:** Apple's standard EULA applies and linking it satisfies the requirement. ✅ **Your half is done 09-18** — the dead sentence is deleted and verified, zero "term" mentions left on the page. **What remains is the code half (E-28), ~4 lines per screen — say go.** It is the last compliance item that has to be *in the binary*, so it comes before the re-archive. Re-scoped from 🟠 on 09-18: [[privacy-policy#finding-3-re-scoped--2026-09-18-there-is-no-terms-of-use-anywhere]].
- [ ] 🟡 Name it **`Find Parking TW`**, as the Store listing will. Add an effective date. Typos: "personal identical", "that that you".
- [ ] 🟡 **Delete the duplicated AdMob sentence** (new 09-18). Your scoped sentence now says it properly; the older *"When using free edition and Advertisement is activated…"* two paragraphs down repeats it and can go.
- [ ] 🟡 A 中文 version — everything else is localised down to the permission strings.
- [ ] ❓ **Want the full corrected draft, English + 中文?** Offered 09-15, 09-16 and 09-18, deliberately not written — it is your document to own.
- [ ] ❓ **Or just the four sentences?** Smaller offer, 09-18: paste-sized replacements for the headline claim, the terms link, the retention paragraph and the duplicate — each swapping for a sentence already on the page. Closes everything but the 中文 version and the effective date.

> [!tip] You do **not** need to buy a domain
> Wix upsells one. `wixsite.com` is fine for Apple's Privacy Policy URL *and* Support URL, and that page is already shipping in the app. The contact form / Messenger link on it **is** the relay you wanted — no personal address published, destination changeable without a release. [[decisions#2026-09-16-no-custom-domain-the-relay-is-a-form-on-the-site-that-already-exists]]

## ✅ `destination-mode` — kept, merged 2026-09-23

Seven rounds of your testing, then merged to `main` and pushed. **It ships in build 1.** Everything about it: [[destination-mode]].

**Three things it leaves open, none of which block the merge:**

- [ ] 🀄 **26 zh-Hant strings marked `needs_review`** — nine of them new this week (the eight `dest_*`/`svc_*` strings plus `sub_terms_of_use`). The one worth your eye is **`dest_bar_showing` → 「顯示 %@ — 你不在這裡」**: that bar is on screen constantly, and my Chinese for *"you're not there"* may land harsher than the English. *(Ignore `parkNav` → `台北停車s` — stray Latin "s", but nothing references it; it is a dead string on the unreachable `allTpe` screen.)*
- [ ] 📱 **Parts nobody has tapped yet:** the grey/green search button and its *"we haven't collected live parking information for this area yet"* alert · the auto-search 1.2 s after the map settles 300 m away · **Clear** disappearing when you are outside the zone.
- [ ] ⚠️ **E-12 is now load-bearing.** `convexEnclosing` is integer-truncated and was inert; `isInServiceArea` now depends on it, so a point near a fence boundary could resolve wrongly — green button where there is no data, or grey where there is. The 1 km tolerance masks it in practice.

## ~~Test `destination-mode`~~ — done, the old checklist

Branch `destination-mode`, four commits, **not merged**. The scheme now launches the simulator in **Cupertino**, so Run gives you the out-of-zone case directly. Switch back in-zone via scheme → Run → Options → Default Location → `Wanli34.gpx`.

- [ ] 🌿 **Round 2 is in and also untapped:** the search button's green/grey, the "no data here yet" alert, **Jump**, and the centre-on-me button disappearing outside the area. **The camera fix was verified from the log** — a restored destination now logs `destination → camera` and the map goes to Taipei.
- [ ] 🌿 **Does the picker read as an offer or as an error?** It still sits inside `ContentUnavailableView` — Apple's "nothing here" furniture — which may be the wrong frame for a screen that says *"here is where to go"*.
- [ ] 🌿 **Is the "Showing 台北市 — you're not there" bar reassuring, or nagging?** It stays for as long as a destination is set.
- [ ] 🌿 **Tap through the whole thing.** **Nothing in the UI has ever been pressed** — this Xcode ships no Simulator.app, so the model was proven by seeding a destination and relaunching, and not one pixel was exercised. That is the part only you can judge.
- [ ] 🌿 **Then switch back to Taipei and confirm nothing changed at all.** With no destination the code path is identical by construction, and it was verified that way — but you are the one who knows what normal feels like.

Everything, including how to revert each commit: **[[destination-mode]]**.

## Second machine — the MacBook Air

- [ ] 💻 **Put the vault at `~/obsidianV0` on the Air**, the same absolute path as here. **Your call, 2026-09-20** — standardise the path rather than make every note path-agnostic. It means `CLAUDE.md`'s `Vault path: ~/obsidianV0` line is simply *correct* on both machines and needs no edit, and the session-start protocol works there with no change. Reasoning: [[decisions#2026-09-20-the-vault-lives-at-obsidianv0-on-every-machine]].
- [ ] 💻 **Create `.claude/settings.local.json` in the app repo on the Air.** It is **gitignored**, so it does not sync and the Air has none. Without it **every vault write stops for approval**, which makes the "write it to Obsidian" convention unusable. Now that the vault path is the same on both machines, **this file can be copied across verbatim** — no path editing. It lives in the app repo at `.claude/settings.local.json`.
- [ ] 💻 **Then point the other Claude at [[working-agreements]]** — it is the note written for exactly that moment, and its first section covers what still differs per machine (the project folder, which you have not standardised).

## Right now — 10 minutes, in a browser

Everything in this block is one edit to the same file: https://gist.github.com/sharkda/1abaa9806dae0f34205725b51f21ad87
Steps if you need them: [[operations#how-to-edit-it--step-by-step]]. **Validate the JSON before saving** — invalid JSON is the one thing that breaks it.

- [x] ~~Real contact email + phone for **Taipei**~~ — **done 2026-09-09, already live in the Gist**: `sb0457@gov.taipei` / `02-27590666#6543` (交通局停管處). Source and re-check command: [[data-sources]].
- [x] ~~New Taipei contact~~ — **email done 2026-09-09 and live**: `ae8131@ntpc.gov.tw` (新北市政府交通局).
- [x] ~~New Taipei phone~~ — **resolved 2026-09-09 and live.** The bureau publishes **02-29702960** specifically for 路邊停車及停車場相關業務, so the Gist uses that rather than guessing which switchboard carries extension 8607. **Both cities' contacts are now real** — that release blocker is closed. Reasoning: [[data-sources#the-phone--resolved-2026-09-09]].
- [ ] 🔴 **A city-request destination.** ⬆️ **Changed 2026-09-15 — it no longer has to be an email.** The config now takes `support.url` (a hosted form or page, preferred) as well as `support.email`, and the URL wins when both are set. So the question is *where should "Request a city" go*, not *which address do I publish*. Recommendation: a **Wix form** — structured rows you can count, no Mail-account dependency, and it does not expose your personal address. A Facebook page works too, but only one that describes **this** app (see the caveat in [[operations#support--which-transport-and-why-url-wins]]). **This gates TWO screens.** The new outside-coverage screen offers a "request a city" button from the same address, and without it that screen degrades to a statement with nothing to act on. It is the one place where a user who cannot use the app can still tell you where to go next. — I removed the `REPLACE-` placeholder, because it shipped a *working* mail button to a domain that does not exist. **But the onboarding prompt still renders**, so users read "tell us where you need it most" with nothing to tap. I deliberately did not substitute your personal address — that is yours to decide, not mine to publish.
- [ ] ❓ Bump `version` so you can tell which edit is live.

**Done when:** the raw URL shows your values — `curl -sS -L "https://gist.githubusercontent.com/sharkda/1abaa9806dae0f34205725b51f21ad87/raw"`

---

## Needs a sitting

- [ ] 🔴 **Record the real tutorial video**, then put its URL in `tutorials.onboarding`. The one there now is your personal test clip. Strip any `?feature=share`. Removing the key is a safe fallback — the button just disappears.
- [x] ~~Review my 中文 drafts~~ — **done 2026-09-09**, 7 corrections applied, all 35 entries now `translated`. **Five small follow-ups noted at the bottom of [[zh-review]]** — two missing `→` arrows, a `youtube` capitalisation, and three clauses the Chinese now omits that the English keeps. None blocking.

- [x] ~~Decide: 課金 or 訂閱?~~ — **訂閱, decided 2026-09-09.** Tab labels and every subscription string now agree; the three remaining 課金 strings belong to the unwired `EntitledView` and display nowhere.
- [x] ~~Build in Xcode~~ — **compiles clean, 2026-09-08**, and pushed (`origin/main` = `37a39f8`).
- [ ] 👀 **Look at the map pins after the next build.** They now fade with age: solid <5 min, 0.7 at 5–30 min, 0.45 beyond. **The judgement call is legibility on a busy map** — if 0.45 is too faint over map detail, raising the floor is one number in `CustomButton.badgeOpacity`. Leave the app open past five minutes to see the first step.
- [ ] 🔴 **Now verify the behaviour on a device** — compiling proved the wiring, not the app. Walk the three onboarding screens; the mail link **must** be tested on hardware (Simulator has no Mail account); tap the video link; open the Subscription tab and check it says **Subscribe**; quit and relaunch to see the **ATT prompt on the 2nd launch**.
- [ ] **While you are on the device, note where the location dialog appears** — screen 1 or screen 3. If it is screen 1, screen 3's copy is setting up a prompt that already happened, and we should talk about it.
- [ ] 🆕 **Coverage states on device (new 2026-09-15).** Simulate a location outside Taiwan (Xcode → Debug → Simulate Location) and confirm the map shows *"We're not here yet"* rather than a blank map; then return and confirm it clears. Watch for `🗺️ coverage … → …` at `.notice` in Console.app. **Also deny location once** — that state was built but never seen running.
- [ ] **Phase 3 lifecycle test** — never run since June. Background/foreground, lock/unlock, app-switcher. Watch for `▶️ app → active: resuming GPS + 0 active proto timer(s)`; **zero** means resume is not restarting polling.
- [ ] **Cyclops 🕐 on a cache-less launch** — does the clock clear after ~15–20 s, or never.
- [ ] 📋 **Release to-do: confirm the New Taipei number is the right destination.** Live now is **02-29702960**, which the bureau publishes for *路邊停車及停車場相關業務*. It was **not** taken from the dataset page — that page gives only extension **8607** with no switchboard, and guessing which of the bureau's two offices (板橋 / 三重) carries it risked shipping a wrong number. **To settle it:** one call to 02-29702960 asking (a) whether that line handles reports of wrong live space counts, and (b) whether 張先生's extension 8607 is on that line or on 02-29603456. If 8607 is on a known line, `<switchboard>#8607` reaches the data owner directly and the app already sends the extension as DTMF. Either answer is a one-line Gist edit I can push. Reasoning: [[data-sources#the-phone--resolved-2026-09-09]].
- [ ] 🐢 **Low priority — the dial pause.** Whether four seconds is enough before the extension fires can only be settled by a real call. **Deferred on Jim's call 2026-09-09:** almost nobody rings a car park, and the dialog shows the number in full (`Button("Call \(phone)")`, `ContactView.swift:158`), so anyone who needs it can read it and dial by hand. **If it is wrong, the symptom is user feedback, not a crash** — a third comma is the fix. Same visit could try Options → Advanced → "Dial numbers internationally (+886)".

> Log at `.notice` or above and read Console.app, or you will see nothing once the debugger detaches.

---

## The app icon — done, pending one build (2026-09-14)

- [x] ~~The alpha channel that blocked the first upload~~ — **fixed.** `ITMS-90717`; all 20 icons carried alpha and `Icon1024` was 26% genuinely transparent.
- [x] ~~Design a new app icon~~ — **done.** `FindParkingTw.icon`, made in Icon Composer: full-bleed, opaque, no owl, no personal handle, nothing for the squircle mask to clip.
- [x] ~~Wire it up~~ — **done.** `ASSETCATALOG_COMPILER_APPICON_NAME = FindParkingTw` across all four configurations. Note for next time: the General tab's App Icon **picker would not list the new file at all** despite everything being correct — the build setting is a free-text field, so type the name. [[app-icon]]
- [x] ~~Delete the old icon sets~~ — **done**, both targets, in its own revertable commit.
- [x] ~~Build in Xcode, Release~~ — **done 2026-09-14.** The 5.38 PM archive built from `icon-replacement` in Release and carries `CFBundleIconName = FindParkingTw`. The three `#if DEBUG` fixes and the icon wiring are proven.
- [x] ~~Confirm `hootmac` compiles~~ — **done 2026-09-14.** Builds clean from the command line on `icon-replacement`, in **both Debug and Release** (`** BUILD SUCCEEDED **`, macOS 26.0, arm64). The shared `.icon` is fine for the mac target. Two pre-existing warnings only (duplicate build files for `NbsScreen.swift` and `IdNameTwdWgs.swift`). **This needed one unrelated fix first** — see [[bugs#2026-09-14-a-dangling-concavehull-package-reference-blocked-every-command-line-build]].
- [x] ~~**Then merge**~~ — **done 2026-09-15.** Fast-forward to `98f1253`; `backup/icon-replacement-pre-fold` deleted. The `icon-replacement` ref still exists and can be removed whenever.
- [ ] 🐢 Optional polish on the new icon: the blue gradient in `icon.json` is **dead config** (the single opaque layer covers it), and **one layer forfeits most of Icon Composer** — depth is computed between layers. [[app-icon#open-notes-on-the-current-findparkingtwicon]]

---

## Decisions only you can make

*Each of these unblocks work I can then do.*

- [x] ~~AdMob: keep or drop?~~ — **keeping (2026-09-07).** *(And I was wrong that no ads were running — banners are built and working. See below.)*
- [x] ~~IDFA prompt (ATT)~~ — **done 2026-09-07: appears on 2nd launch.** Info.plist key, launch counter and wiring are all in. **Verify on device:** launch once (no prompt), quit, launch again → the alert appears. `🎯 ATT:` logs at `.notice` every launch saying waiting / asking / settled. **Delete and reinstall to retest** — it is once per install. Detail: [[operations#how-it-is-wired]]
- [x] ~~Which territories?~~ — **decided 2026-09-07: skip EEA/UK.** Taiwan + US + Japan need no consent SDK. ✅ Both are fine for AdMob and both have a real audience (visitors to Taiwan, and Taiwanese abroad); Japanese users would see the app in **English**.
- [ ] ⚠️ **Mainland China: I'd drop it.** Three independent blockers — Apple requires an **ICP filing (备案)** for the China mainland App Store, which needs a Chinese entity or agent; **Google is blocked there so AdMob serves nothing**; and the app shows Taipei parking, which is no use to someone in China. **Hong Kong and Macau are separate territories** with none of those problems and they already get 中文 — include those instead if Chinese-speaking reach is the goal.
- [ ] 🔴 **Set availability manually in App Store Connect** — it defaults to ***all*** territories, which would put you in the EEA with no consent platform. Set exactly: **Taiwan, United States, Japan, Hong Kong, Macau.** (App Store Connect → your app → *Pricing and Availability* → Availability → *Edit*.)
- [ ] 📌 **Before you ever add a territory later, read [[operations#gate-table--read-this-before-adding-any-territory]] first.** It is written for the version of you who has forgotten why these were excluded. Short version: HK/Macau are free to add; **EEA/UK needs the UMP consent SDK shipped in a build first**; **mainland China needs an ICP filing (备案) and earns nothing anyway because Google is blocked there**.
- [x] ~~The app name~~ — **decided and wired 2026-09-10: `Find Parking TW` / `找車位`.** Both live in `InfoPlist.xcstrings`, localised, so they can differ deliberately. The stale `Park-Chia`, the "Hootowl uses your location…" permission string and `LandingScreen`'s hardcoded 車停對 are all gone, and both usage prompts are now localised — the last user-visible English in a Chinese build.
- [ ] 📋 **Set the App Store name to `Find Parking TW`** and the **Subtitle** to `Taipei & New Taipei parking` (27/30). Check the name is available first. The subtitle is where coverage lives so it can change every release without renaming the app — reasoning in [[decisions#2026-09-10-app-name-find-parking-tw--找車位]]. **Promotional Text is drafted and paste-ready in [[app-store-connect#22-promotional-text--english--170-characters]]** (2026-09-14) — it is the one listing field you can change later without a build, so it is safe to paste the recommended line now and rethink it any time.
- [ ] ❓ **New Taipei's −9 lots — now explained, so the decision is easier.** The portal states it outright: *部分停車場因更換營運廠商，尚無提供即時車位，其顯示數值將為-9* — those lots are **mid-operator-change**, not broken. So they are real, usable car parks that simply do not report yet. **Labelling beats hiding**, and the rate should fall on its own as operators finish switching. See [[data-sources#-this-dataset-answers-the-open-9-question]].
- [ ] 🔴 **Is there any reason to subscribe?** Found 2026-09-08: on iOS `AppScreen.sorted()` returns **the same tabs for every tier**, so nothing is gated — the *only* thing a subscription changes is turning off the ad banner. The old paywall claimed "unlock advanced features", which was false; the new screen says only what is true. **If subscribers were meant to get more, that gating was never built.** Product call, not a bug. See [[00-subscription-screen]].
- [ ] **Look at the new subscription screen when you build** — the `.entitle` tab no longer shows `EntitledView` (the one with the receipt dump). `EntitledView` is still in the tree, just unwired. The tab itself now reads **Subscribe** / **My Subscription** depending on state.
- [x] ~~Three small calls on the subscription-reach work~~ — **all settled 2026-09-08:** `cart.fill`, icon + label, and no onboarding paywall at all (a one-line mention instead). See [[tasks]].
- [x] ~~Check my 中文 draft for the subscribed tab label~~ — **done**; it is 我的訂閱 now, reviewed with the rest.
- [ ] ⚠️ **Watch early reviews for the ad-expectation line** — "There will be more of them over time" is deliberate pre-framing, but it can read as a threat. One string to soften if it lands badly.

---

## Gaps found 2026-09-10 — things that were on no list

*Audited against the repo rather than from a generic checklist. The iPad/visionOS device family looked like a problem and is not — that is the UI-test target; the app is iPhone-only.*

- [x] ~~🔴 **`ITSAppUsesNonExemptEncryption` is absent from `Info.plist`**~~ — **done, and verified again 2026-09-17.** Added in `5411f69` with a comment explaining why `false` is correct (HTTPS through system APIs; the only CryptoKit use is `SHA256.hash()` to detect whether a feed payload changed). Xcode deleted the key on 09-16 while migrating it to a build setting; that was reverted, so the documented version is what ships. ASC stops asking on every upload.
- [ ] 🔴 **Age rating questionnaire** in App Store Connect. Required before submission and easy to forget because nothing in Xcode mentions it.
- [x] ~~**How does a reviewer in California check the app?**~~ — **answered 09-18, and it needs no code.** The **All** tab is not filtered by location, so it shows ~3,162 live Taipei + New Taipei car parks anywhere in the world. The reviewer only has to be told: open **All**, type **`TPE`** in capitals. Paste-ready notes: [[app-store-connect#34-beta-app-review-information--paste-ready]] · working: [[sessions/older/2026-09-18/01-reviewer-in-california|01-reviewer-in-california]].
- [ ] 🔴 **A TestFlight pass before release.** Not on any list so far, and it is the only way to exercise things the simulator cannot: StoreKit **sandbox** purchases (as opposed to the local `.storekit`), the **real ATT prompt**, **real ads** rather than test ads, and the actual `mailto:` and `tel:` handoffs.
- [ ] 🟠 **App Store listing in 繁體中文** — description, keywords, screenshots. Separate from the app's own strings, and separate again from the App Information localisation already in place.
- [ ] 🟠 **There is no crash visibility.** No Crashlytics, Sentry or equivalent. Xcode Organizer shows crashes from users who opted into sharing analytics, so it is not zero, but it is partial and delayed. Worth deciding **before** launch — retrofitting after a bad week is the wrong time.
- [x] ~~🔴 **Ship an "outside coverage" empty state**~~ — **shipped `fb28765` (2026-09-15), and exercised on the simulator 09-17:** from Cupertino the map says *"We're not here yet"*; from Taipei 101 it clears and pins come live. The rejection I would have bet on is closed. **Still owed: seeing it on a device, and the location-denied state** — that one was built but has never been seen running (**R-14**). See [[release-strategy#the-one-risk-i-would-bet-money-on]].
- [x] ~~🔴 **Credit the data sources** *in the app*~~ — **shipped 2026-09-15 in `fb28765`**, confirmed by audit 09-19. `OptionsScreen.swift:166` carries a **Data source** section naming both city governments and 政府資料開放授權條款－第1版, translated in en **and** zh-Hant. **Still owed: the same line in the App Store description** — folded into the description work (R-10), since that is where it has to be typed anyway.
- [ ] 🟠 **Nothing tells a user when the feed is down.** `grep` finds no user-facing error state for a failed municipal fetch — counts simply stay stale or empty. For an app whose entire proposition is *live* numbers, that is the most likely source of "it doesn't work" reviews, and it is cheap to fix relative to what it prevents.
- [ ] ❓ **iOS 26.0 minimum, so anyone on an older OS cannot install at all.** This follows the documented latest-only stance ([[feedback-no-availability-branching]]) and is a legitimate engineering choice — but the reach consequence is worth pricing deliberately for a commuter utility, where a slice of the audience is on older hardware.
- [ ] 🐢 Minor: fixed font sizes (`.system(size: 34/44/50/64)`) in the onboarding and subscription screens do not scale with Dynamic Type. Most are icons, where it barely matters; the app-name text at 34 and 50 is the part a large-text user would notice.

## App Store Connect — your account, nobody else can

- [ ] 🔴 **Add Traditional Chinese to the subscription product in App Store Connect.** The local `.storekit` had it as `zh_CN` (Simplified), which a zh-Hant device never matches — so the sheet fell back to English. Fixed for local testing; **ASC has the same problem and that is the one real users hit.** Suggested text: 訂閱 / 關閉廣告橫幅。其他功能訂不訂閱都一樣。 See [[bugs#2026-09-09-the-subscription-sheet-rendered-english-on-a-chinese-device]].
- [ ] 🔴 **Privacy nutrition labels** — location, and whatever the AdMob decision lands on. **Location evidence is already gathered:** precise, app functionality, **foreground-only**, never used for tracking — six checks in [[00-location-privacy-audit]] back it.
- [ ] 🔴 **Screenshots and description.** Coverage (Taipei + New Taipei City) belongs here: it is what people read *before* installing, which is why onboarding does not have to carry the whole disclosure.
- [ ] ❓ Privacy policy URL and support URL — App Store Connect requires both.
- [ ] ❓ Confirm version/build. Currently `MARKETING_VERSION = 1.0`, build `1`.

---

## Waiting on you, but then they are mine

Say go and I will do these — listed so you know they are not forgotten, **not** so you do them.

- [x] ~~`PrivacyInfo.xcprivacy`~~ — **done 2026-09-07**, wired into both targets. Declares tracking (ATT/IDFA) plus two required-reason APIs — `UserDefaults` and, found by audit, **file timestamps** (`Municipal+Fence.swift:70`). **Your bit:** run Product → Archive → *Generate Privacy Report* before submitting, and remember the App Store Connect nutrition labels are a **separate** declaration that must cover what AdMob collects. → [[operations#c-app-store-submission]]
- [ ] **Fix the location permission string** — stop naming the app, and localise it. Blocked only on the name decision above.
- [x] ~~Draft the 中文 strings~~ — **done 2026-09-09.** All 35 user-facing keys carry reviewed 中文, marked `translated`. Record: [[zh-review]].
- [ ] **Localise the two Info.plist prompts** — the location one and the new tracking one are **English-only**, so a Chinese-locale user reads English in both system alerts. Needs an `InfoPlist.xcstrings`; best done in one pass, and the location string is blocked on the app-name decision anyway.
- [ ] **Delete the three now-unreferenced files** (`UserGuide`, `OnboardTab0`, `OnboardDebug`) and their project entries. Note: `OnboardDebug` was your quick route to the IAP receipt + options screens.
- [ ] **Reject placeholder config values** — treat an `@example.com` address or a `1234-5678` phone as absent, so this class of mistake cannot ship again. ~4 lines.
- [x] ~~**`OnboardScreen.swift:26`** still uses the deprecated `NavigationView`.~~ — **removed 2026-09-24 (`ea9ce8f`)**, and it turned out to be the cause of the stray top-left "back" button Jim spotted in onboarding: it nested a second navigation container inside `LandingScreen`'s own. The eject button is a plain overlay now. [[decisions#2026-09-24-onboarding-stays-a-tab-and-has-two-ways-out]]

---

## Related
[[operations]] · [[unfinished]] · [[bugs]] · [[onboarding]] · [[Admob]] · [[Jim's backlog]]
