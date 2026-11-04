# 2026-09-07 — Tutorial video link (built) and screenshots (recommended against)

Jim asked whether onboarding can carry **embedded screenshots** or a **link to a YouTube tutorial**. Both are possible; they are very different propositions, so they got different answers.

---

## What the project starts from

Checked before answering:

- **No WebKit anywhere.** `grep` for `WKWebView` / `import WebKit` / `SFSafariViewController` → zero hits.
- **No video.** `AVKit` is imported in exactly one place (`plumbing/AVAudio.swift`) and only for audio. No bundled `.mp4` / `.mov` / `.gif`.
- **No image assets at all.** `Assets.xcassets` contains colour sets and the app icon — **zero `.imageset`**. Onboarding would be introducing the first bitmap in the app.

## Built: a tutorial link, configurable without an app release

Screen 2 (`OnboardPinsScreen`) now shows **"▶ Watch how it works →"** — but only while a URL is set.

The URL is **not a constant**. It is a new optional `tutorial` key in the Gist-backed remote config, the same mechanism the `support` email uses as of yesterday:

```json
{ "contacts": { … }, "support": { "email": "…" }, "tutorial": "https://youtu.be/xxxxxxxxxxx" }
```

Which means:

- The video can be **recorded, re-recorded, replaced or withdrawn** with a Gist edit — no build, no review, no release.
- **There is no button until there is a video.** Nothing to ship half-done, and nothing to remember to remove if the video is retired.
- A **typo in the Gist hides the button** rather than shipping one that opens nothing: `tutorialURL` returns nil when the string is empty or unparseable.

`ContactConfig` is now the app's general remote config rather than strictly contact info. That is a mild stretch of its name, and cheaper than a parallel fetch/cache mechanism for one string — noted here so it is a choice on the record rather than drift.

### Why link out rather than embed the player

An inline YouTube player means a `WKWebView` and an iframe embed. That buys:

- a **new framework** and a first-launch **network dependency** on the one screen that must work before anything else does;
- a **blank rectangle** whenever the network is slow, the video is region-blocked, or YouTube changes the embed;
- privacy surface (would need `youtube-nocookie.com` at minimum).

`openURL` hands off to the YouTube app or Safari, **cannot fail visibly on our screen**, and costs nothing when unused. If an embedded player is ever wanted, the honest version is a short screen recording bundled in the app and played with `AVKit` — offline, no third party — at the cost of app size.

## Not built: screenshots in onboarding — and why I would not

Possible, but I recommend against it for this app, for reasons that have already bitten this project:

1. **They go stale silently.** A screenshot is a claim about the UI. This codebase has spent real time on copy and code disagreeing; a bitmap of the Cyclops grid becomes a lie the first time a card is resized — as happened on 2026-09-05 — and nothing fails to warn you.
2. **They double with localisation.** The UI ships English and 中文, so an honest screenshot set is two of everything, forever.
3. **The App Store listing already does this job**, and does it *before* the install decision — the same argument that settled the coverage-wording question earlier today.
4. **They would be the app's first bitmaps**, so app size, `@2x/@3x`, and dark-mode variants all arrive at once for a decorative gain.

### If a visual on screen 2 is genuinely wanted

The alternative worth building is a **live SwiftUI mock of a Cyclops card** — two or three fake pinned lots rendered with the real views. It cannot go stale (it *is* the UI), it localises for free, it costs no assets and no app size, and it dark-modes correctly. More work than an image, and it needs a design pass, so it is not taken unasked.

## Status

Working tree only, not committed, not compile-verified. **Jim owes the Gist** two keys now — `support` (release item) and, whenever a video exists, `tutorial` (optional).

## Related
- [[decisions#2026-09-06-city-request-feedback-rides-the-existing-gist-contact-config]] — the pattern this reuses
- [[00-req-taipei2Taiwan]] · [[onboarding]] · [[unfinished]]

---

## Video supplied — 2026-09-07

Jim: `https://youtube.com/shorts/PG4CUrdkb6k?feature=share`. Verified it resolves (HTTP 200, title "907").

**Stored without `?feature=share`** — that parameter is share-sheet attribution, not part of the video's identity, and it would travel into every place the link is used.

**On the "can we put a redirection in the middle" question:** not needed for the app. Nothing about the video is in the binary — `OnboardPinsScreen` reads `ContactConfig.tutorial` from the Gist, so re-pointing the video is already a JSON edit. Embedding a redirect URL in the app would be *worse* than what exists: if the redirect service moved or died it would take an App Store release to fix a link, which is the exact failure the Gist removes.

A redirect still earns its place for **links that live outside the app** — App Store description, QR codes, print — since those genuinely cannot be edited later. The right shape then is both layers: the Gist holds the redirect URL, and everything outside the app uses that same redirect. The app never depends on the redirect surviving.

**DEBUG default now points at the real video** rather than a placeholder, so development builds exercise the same URL production will.

## ⚠️ Found while fetching the Gist

The live config is **still the example placeholders** — `taipei@example.com`, `+886-2-1234-5678`. That is a release blocker independent of anything here: [[bugs#2026-09-07-the-contact-gist-is-still-all-examplecom-placeholders-release-blocker]].
