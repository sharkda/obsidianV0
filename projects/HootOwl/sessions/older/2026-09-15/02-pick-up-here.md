# Pick up here — written 2026-09-16, before a macOS update

> [!success] Pushed before the update — the work is safe
> **`origin/main` = `9a7190c`.** All 11 commits went up on 2026-09-16, including the whole icon replacement and everything from this session. Nothing lives only on this disk any more.

> [!success] Re-verified after the macOS update — 2026-09-16, ~14:00
> **macOS is now 27.0 (26A428). Xcode did *not* change: still 27.0 / 27A266a / Swift 6.4 — the same toolchain the 09-15 verification was done on.**
> All three builds pass (iOS Debug, iOS Release, hootmac Release), and the app was **built, installed, launched and driven on the iPhone 17 Pro simulator** — no launch crash, geofences load, `recomputeCoverage()` went `locating → outside` at Cupertino and `outside → covered` at Taipei 101. The 09-15 verification stands.
> **But the run turned up a live P0:** New Taipei City availability is dead — NTPC's bulk availability CSV is being WAF-rejected. See [[bugs#2026-09-16 — New Taipei City availability is dead: the bulk CSV is WAF-rejected (open)]]. **This now comes before the re-archive.**

> [!danger] The standing warning, for the next time
> **If an update brings a new Xcode, every "verified" claim in this vault expires again.** That is not a guess — it is exactly what happened between 09-14 and 09-15 and cost most of a session. **Re-run the three builds before trusting anything**, and re-run the app, because the worst failure last time compiled clean and crashed at launch. Command lines are at the bottom of this note.

---

## Where things stand

**`main` = `origin/main` = `9a7190c`. Working tree clean, everything pushed.**
`icon-replacement` merged as a fast-forward; `backup/icon-replacement-pre-fold` deleted. The `icon-replacement` branch ref still exists and can be deleted.

```
9a7190c  Let a city request go to a URL, not just a mailto
fb28765  Explain what the app shows outside its coverage area
88c5b4b  Make the geofence test correct and the fence data decodable
2c3dbb4  Stop applying .commands on iOS, which crashed the app at launch
391d784  Fix a FanceMapView01 init that Swift 6.4 rejects
a4a005b  Delete the dangling ConcaveHull package reference
98f1253  ← icon-replacement merged here
```

Everything builds: **iOS Debug, iOS Release, hootmac Debug, hootmac Release**, on Xcode 27.0 / Swift 6.4. The app was run and driven on the iPhone 17 Pro simulator.

Full narrative of the session: [[01-session-wrap]]. Its addendum answers "is the Xcode 27 migration complete?".

---

## The three things that happened

1. **Merged `icon-replacement`** into `main`, as planned. Clean fast-forward.
2. **Xcode moved 26.6 → 27.0 under us** and broke two things, one of which meant **the app could not launch at all** (`.commands` with an empty `@CommandsBuilder` closure — compiles silently, aborts in `AppGraph.init`). **The 09-14 archive contains that binary: do not submit it, archive again.**
3. **The empty state shipped** — the rejection I would have bet on is closed. Building it exposed that **the geofence system had never run on iOS** (three independent faults). All fixed and verified by running the app from Cupertino and from Taipei 101.

Then a long product thread on where a city request should go, ending in `support.url` being added to the remote config.

---

## Open threads, in the order I would take them

### 0. ~~Fix New Taipei City availability~~ — done 2026-09-16, `e45051c`
NTPC's `…/csv/file` for the availability dataset returns an F5 **"Request Rejected"** page with HTTP 200. Persistent, path-specific, and not fixable with headers. The same dataset's `…/csv?page=N&size=1000` and `…/json` still serve real rows, but **cap at 1000 per page** and NTPC has 1411 — so the fix has to paginate. Full diagnosis, evidence and the recommended code shape: [[bugs#2026-09-16 — New Taipei City availability is dead: the bulk CSV is WAF-rejected (open)]].
**Why it jumped the queue:** it broke half the coverage area for every user, and archiving before it was fixed would have burned a build number on a release shipping dead data.
**Fixed and verified live** — `📄 newTaipeiCity minutely: 2 page(s), 1410 rows`, published at 22:33 instead of a 15:19 cache. The re-archive is unblocked.

### 1. ~~Push~~ — done 2026-09-16, `origin/main` = `9a7190c`

### 2. Re-archive and upload — **unblocked, this is next**
The old archive cannot launch. Build numbers are a counter, not a statement — burn another. Every ASC field is drafted and paste-ready in [[app-store-connect]]. The `Upload Symbols Failed` warning is expected forever: [[operations#the-upload-symbols-failed-warning--ignore-it-permanently]].

### 3. Privacy policy — mid-revision, two rounds done
Everything is in [[privacy-policy]], including a table of **what the app actually does with data, verified against the source**. Round 2 closed the location gap; **three findings are still open**, and the top one got *worse* rather than better — the policy now contradicts its own ATT prompt two paragraphs apart. Paste-ready fix wording is in that note.

**Offered and not done:** a full corrected draft in English + 中文. Say the word and it gets written; it was deliberately left alone because it is Jim's document to own.

### 4. Decide the city-request destination, then one line in the Gist
The code is done and dormant. `support.url` (hosted page or form) wins over `support.email` when both are set, and requests carry `?src=onboarding` / `?src=coverage` so demand can be attributed to the screen that produced it.

**Where this landed after a long back-and-forth:**
- **No custom domain is needed.** Wix upsells one; `jimhsuyc.wixsite.com` already returns 200 and already hosts the privacy policy that ships in the app.
- **The "relay" Jim wanted already exists** — a contact form / Messenger link on that free site means no personal address is ever published, and the destination can change without a release.
- **Facebook can be the user-facing channel**, and Taiwan's FB usage is a real argument for it — but it cannot replace email entirely, because **App Store Connect's App Review Information requires a contact email**. Use a dedicated mailbox for that, never the personal one; only Apple sees it.
- **`facebook.com/tataroApp` is not usable as-is.** It renders fine logged-out (checked), but its description is *"Tataro is the software company that created the Bobomofo Application"*. Fix the page identity, or give the app its own page.

### 5. The device pass
Everything on [[jim-actions]], plus the new coverage states — simulate a location outside Taiwan, confirm *"We're not here yet"*; deny location once, since that state was built but never seen running.

---

## Loose ends deliberately left

- **`hoot_test_ui` does not build.** Proven pre-existing (identical failure at `a4a005b`), no scheme, in no verification anywhere. Wire it or delete it; it blocks nothing.
- **The privacy policy URL is hardcoded in two Swift files** — the only remote-configurable thing that isn't in the Gist. [[privacy-policy]] has the detail.
- **`convexEnclosing`** is still integer-truncated and still wrong. Inert, and left alone on purpose pending the fence-activation design decision.
- **`ActDeActOnes` still has zero callers**, so every proto polls for every user — still confounds any battery measurement.
- **`TpeParkDescInfo.json` is missing from the iOS bundle**, logged at every launch. Never investigated; possibly the same missing-target-membership shape as `fences` was.
- Two Swift-6-language-mode warnings are latent, not urgent: `AVAudio.swift` attribute whitespace, and `any Mu1Proto` existentials. Inventory in [[01-session-wrap]].

---

## Re-verify after the OS update

```sh
export DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer
xcodebuild -version                      # did Xcode change?

xcodebuild -project hootowl.xcodeproj -scheme hootowl -configuration Debug \
  -destination 'generic/platform=iOS Simulator' build
xcodebuild -project hootowl.xcodeproj -scheme hootowl -configuration Release \
  -destination 'generic/platform=iOS' build
xcodebuild -project hootowl.xcodeproj -scheme hootmac -configuration Release \
  -destination 'platform=macOS' build
```

**Compiling is not enough — run it.** The launch crash compiled clean:

```sh
UDID=$(xcrun simctl list devices available | grep -m1 "iPhone 17 Pro" | grep -oE '[0-9A-F-]{36}')
xcodebuild ... -destination "id=$UDID" -derivedDataPath DerivedData/sim ENABLE_DEBUG_DYLIB=NO build
xcrun simctl boot $UDID
xcrun simctl install $UDID DerivedData/sim/Build/Products/Debug-iphonesimulator/hootowl.app
xcrun simctl privacy $UDID grant location com.sharkda.hootowl
xcrun simctl location $UDID set 37.3230,-122.0322     # Cupertino → "We're not here yet"
xcrun simctl launch --console-pty $UDID com.sharkda.hootowl
xcrun simctl location $UDID set 25.0340,121.5645      # Taipei 101 → card clears, live pins
```

Simulator gotchas learned the hard way, so they are not re-learned:
- `ENABLE_DEBUG_DYLIB=NO` — the preview dylib adds its own launch failures outside Xcode.
- **The ATT prompt becomes a zombie** once presented and unanswered: it survives terminate, reinstall and TCC edits, and this Xcode ships **no Simulator.app** to click it with. `simctl erase` is the way out — a *first* launch never prompts, the gate being launch count ≥ 2.
- `simctl spawn … defaults write` does not reliably reach the app's real preferences; those live in the container plist and `cfprefsd` caches them.

## Related
[[01-session-wrap]] · [[CURRENT]] · [[jim-actions]] · [[privacy-policy]] · [[operations]] · [[app-store-connect]] · [[bugs]] · [[decisions]] · [[swift-patterns]]
