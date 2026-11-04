# Jim's action list

**Only what needs *you*:** your accounts, your device, your judgement. Everything here is open. Each line has an ID; the detail is one click away in [[release-plan]].

*Rebuilt 2026-11-04 from the old list, checked against [[release-plan]] and the app repo. The old list is kept verbatim in [[jim-actions-to-2026-11-04]], including everything that was done and why.*

> [!tip] If something here reads like trivia rather than judgement, push back
> A fact Claude can look up doesn't belong on this list. See [[working-agreements#Vault upkeep]].

---

## 1 · Blocks GM 1.0, in this order

- [ ] **R-10 · Screenshots** plus your wording pass. Plan, sizes and shot list: [[screenshots]]. Recommendation: plain screenshots for 1.0, no captions.
- [ ] **中文 pass · 33 strings marked `needs_review`** (31 in the app, 2 in the system prompts). Edit them in [[zh-review]].
- [ ] **R-02 · Paste the `support` block into the Gist.** It's a paste, not a decision. Exact JSON: [[operations#settled-2026-10-08--jim-chose-option-1-and-it-is-built]]
- [ ] **R-04 · Privacy policy opening line.** *"collects only 'name'"* is false for this app, and it's the first line a reviewer reads. → [[privacy-policy]]
- [ ] **R-14 + E-25 · One device pass.** Covers:
  - the three onboarding screens and the mail link (hardware only)
  - ATT on the 2nd launch
  - the Subscribe sheet (both policy buttons)
  - coverage states (outside Taiwan, and location denied)
  - type `tpe` in All
  - the destination-mode picker and bar: do they read as an offer or as nagging?
  - a clean-install permission run
- [ ] **R-11 · A TestFlight pass:** sandbox purchase, the real ATT prompt, real ads, `tel:` / `mailto:`.

## 2 · App Store Connect: paste and tick in one sitting

- [ ] **R-06 · Territories:** exactly Taiwan, US, Japan, Hong Kong, Macau. It defaults to *all*. Before adding any more later, read [[operations#gate-table--read-this-before-adding-any-territory]].
- [ ] **R-07 · Age-rating questionnaire.**
- [ ] **R-08 · 繁體中文 on the subscription product.** Suggested: 訂閱 / 關閉廣告橫幅。其他功能訂不訂閱都一樣。
- [ ] **R-09 · Privacy nutrition labels:** precise location, app functionality, foreground only, never tracking. With no crash SDK (E-02), there is nothing else to declare.
- [ ] **R-17 · Listing in 繁體中文:** description, keywords and screenshots, plus the data-source credit line (R-12). Drafts: [[app-store-connect]]
- [ ] **Listing fields:** name `Find Parking TW` and subtitle `Taipei & New Taipei parking` · the three URL fields (en **and** zh-Hant) · Marketing URL `https://sharkda.github.io` · categories Navigation then Travel · copyright `2026 Yu-Ching Hsu`. All paste-ready in [[app-store-connect]].
- [ ] **R-20 · Paste the App Review notes.** → [[app-store-connect]]
- [ ] **R-01 · Re-archive and upload. Do this last.** The 09-14 archive can't launch. Commit the build bump (3 → 5) first.

## 3 · Privacy policy polish (🟡, not blocking)

- [ ] **R-18 · Retention:** it still describes "the paid edition". Say instead that the location cache is discarded after 24 h and goes when the app is deleted.
- [ ] **R-19 · Polish:**
  - name it `Find Parking TW` and add an effective date
  - delete the duplicated AdMob sentence
  - fix the typos "personal identical" and "that that you"
  - add a 中文 version
- Offer still open: paste-sized replacement sentences, or a full EN + 中文 draft (**D-05**). Say the word.

## 4 · After launch, or in 1.1

- [ ] **Send Claude the App Store URL** once you're live. It adds the download button to the home page.
- [ ] **Check AdMob's app-ads.txt status** once you're live.
- [ ] **D-06 · Watch early reviews** for the *"there will be more of them over time"* ad line.
- [ ] **R-13 · Record the real tutorial video.** The Gist still points at your test clip.
- [ ] **R-21 · App preview video:** you drive the app, Claude records. → [[screenshots#6-app-previews--the-video-in-the-first-slot-new-2026-11-04]]
- [ ] **J4 · Approve the stale-data copy** · **J7 · Paste the `feedStatus` block** · **J6 · Gist token** (optional). → [[data-schema-lifecycle]]
- [ ] **R-15 · R-16 · Two New Taipei calls:** the blocked bulk download, and whether 02-29702960 / ext. 8607 is right.
- [ ] **E-18 · E-19 · Look on a device:** the toolbar squeeze, and whether pins at 0.45 alpha are legible.
- [ ] **E-02 · Pick a crash SDK for 1.1:** Crashlytics or Sentry. Claude evaluates.
- [ ] **J-02 · J-04 · J-05 · Triage your backlog with Claude.** → [[Jim's Features and backlogs]]

## 5 · Someday (1.2+)

- **D-03** Mainland China (recommendation: drop it) · **D-04** iOS 26.0 minimum · **E-08** lifecycle device test · **E-09** Cyclops 🕐 on a cache-less launch
- **E-22 · E-23** Correct `CLAUDE.md` / `AGENTS.md`: park IDs are not `tpe_`/`ntpc_`-prefixed, and the `fileprivate(set)` note.
- 🐢 Icon polish: the blue gradient in `icon.json` is dead config. → [[app-icon]]
- 🐢 The four-second dial pause, deferred 2026-09-09.

## Second machine (blocks no release)

- [ ] **M-01 · Move the vault on the MacBook Air to `~/obsidianV0`.** Then **M-02:** copy `.claude/settings.local.json` into the app repo there, and point that Claude at [[working-agreements]].
