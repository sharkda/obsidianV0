# Screenshots — R-10

**The last item on the critical path with a lead time, and the only one with no plan until now.** [[app-store-connect]] drafted every *text* field in both languages and explicitly left this out — *"Screenshots — separate from this"* — so R-10 has been a named blocker with nothing behind the name.

> [!abstract] The short version
> **Two sizes, five or six shots, one real decision.** The spec is settled and measured below. The decision is **plain screenshots or captioned ones** — plain I can produce end to end; captioned needs you to design an overlay, and that is where the lead time actually lives.

---

## 1. The spec — measured on this machine, not quoted from a blog

Three of the five guides that come up for this question say the required iPhone class changed in October 2026 and three say it did not. Rather than pick one, **I booted the simulators and measured what they produce**, 2026-11-04:

| Simulator | Runtime | Screenshot | App Store class |
|---|---|---|---|
| **iPhone 17 Pro** | iOS 26.5 | **1206 × 2622** | 6.3-inch — *"iPhone with Dynamic Island (medium display)"*, the **required** one |
| **iPhone 18 Pro Max** | iOS 27.2 | **1320 × 2868** | 6.9-inch — *"(large display)"*, the largest accepted |

**Shoot both.** Apple's own help page says the required set is the medium display and that App Store Connect *"automatically scales them down for smaller device sizes"* — but the scaling note sits under the large-display entry, and the wording does not clearly say a large-only upload satisfies the medium requirement. Supplying both costs one extra simulator boot and removes the ambiguity entirely. **Confirm against what ASC itself demands at upload time** — the Media Manager names the required sizes, and that is the only authority that matters.

**Other limits from the same page:**

- **1 minimum, 10 maximum per size.** `.png`, `.jpg`, `.jpeg`.
- **No alpha channel, no transparency.** ⚠️ **This app has been bitten by exactly this before** — `ITMS-90717`, all 20 app icons carried alpha and `Icon1024` was 26% transparent ([[app-icon]]). `simctl` screenshots are opaque, but anything passed through a design tool must be re-checked.
- **No iPad set needed.** The iOS target is `TARGETED_DEVICE_FAMILY = 1` — iPhone only. (`1,2,7` in the pbxproj belongs to `hootmac` and `hoot_test_ui`, not the shipping app.)
- Apple states no rule about device frames or marketing imagery; the only content rule is that screenshots must satisfy the App Review Guidelines.

---

## 2. The shot list

**Five shots that each make one claim, in the order a stranger would ask the questions.** Every one is a real screen of the shipping build — nothing staged, nothing that does not exist.

| # | Screen | The claim it makes | Why it earns a slot |
|---|---|---|---|
| **1** | **Near Me!** — the map, pins carrying live counts | *There are spaces near you, and here is how many* | The whole product in one image. If someone looks at one screenshot, it is this |
| **2** | **A lot's detail sheet**, opened from a pin | *Available, total, address, and a way to get there* | Answers "and then what?" — the pin is a promise, this is the payoff |
| **3** | **All** — the list with the filter chips visible | *Every car park in two cities, searchable* | Scale. 2,592 lots across 臺北市 and 新北市 is the one number a competitor cannot fake |
| **4** | **Cyclops** — two or three watched lots with their trails | *The ones you use every day, kept under watch* | The only feature here with no obvious equivalent elsewhere, and the reason someone keeps the app |
| **5** | **Destination mode** — showing a city you are not in | *Check parking before you leave the house* | Turns the app from "I am lost now" into "I am planning" |

**Optional sixth, and an unusual one:** the **no-live-data notice** that D-02 shipped — 「本停車場未提供即時車位」 with the explanation under it. It advertises a *limitation*, which no one does. It is worth considering anyway, because **40.6% of lots in this app have no live number** ([[decisions#2026-10-27--label-the-car-parks-with-no-live-count-d-02]]) and a user who meets that on day one without warning feels misled. Saying it in the listing converts a complaint into a demonstration of honesty. **Jim's call; I would include it as the last shot, not the first.**

### Order matters more than count
Apple shows the **first two** in search results. 1 and 2 must stand alone without captions.

---

## 3. The one real decision: plain or captioned

**App Store screenshots have no caption field.** Any text is burned into the image by you before upload. So:

| | Plain screenshots | Captioned screenshots |
|---|---|---|
| What it is | the app's own screens, unaltered | each screen under a headline, usually on a coloured band |
| Who does it | **me, end to end** — boot, seed, capture, verify sizes, hand you a folder | **you**, in Figma/Sketch/Keynote, from my captures |
| Lead time | **minutes** | the actual lead time in R-10 |
| Localisation | **none needed** — the screens are already localised, so a zh-Hant capture *is* the Chinese set | **two full sets**, and 繁體中文 leads |
| Risk | reads as a utility app. For a parking app, that is the genre norm | a badly set Chinese headline looks worse than no headline |

**Recommendation: plain, for GM 1.0.** Utility apps ship plain screenshots routinely, it costs nothing, and it removes the only lead time standing between here and submission. **Captions are a 1.1 improvement** that can be made without a binary — screenshots can be replaced in ASC at any time, with no review.

If captioned is wanted anyway, the captions are drafted — 繁體中文 leading, per [[working-agreements]]:

| # | 繁體中文 | English |
|---|---|---|
| 1 | **即時車位，就在地圖上** | Live spaces, right on the map |
| 2 | **可用、總數、地址，一次看清** | Spaces, total, address — at a glance |
| 3 | **兩市 2,592 個停車場，一次搜尋** | 2,592 car parks, one search |
| 4 | **常用的停車場，幫你一直盯著** | Keep watch on the ones you use |
| 5 | **出發前，先看目的地有沒有位** | Check the spaces before you leave |
| 6 | **沒有即時資料時，我們直接說** | When there's no live data, we say so |

---

## 4. What I can and cannot do, precisely

**I can:** boot both simulators · install the current build · seed the location to 臺北市 · let the feeds populate · capture at the exact pixel sizes above · verify dimensions and the absence of an alpha channel · deliver a named folder ready to drag into ASC · do the whole thing twice, once per language, by switching the simulator's locale.

**I cannot navigate the app.** `xcrun simctl` can screenshot, install, launch and terminate, but **it cannot inject a tap** — established the hard way on 2026-11-01. And **this machine has no iOS `Simulator.app`**: `Xcode.app/Contents/Developer/Applications/` is empty under Xcode 27.2, so there is no simulator window for desktop automation to click either. Shots 2–5 all require navigation.

**Three ways past that, in the order I would choose them:**

1. **Jim taps, I shoot.** He drives to each screen in Xcode and says the word; I capture headlessly at both sizes. Zero code, ~15 minutes, and he sees every frame before it ships. **This is the one I recommend.**
2. **Jim taps and captures himself.** Xcode's simulator saves a screenshot at native resolution, which is already the correct pixel size. Then I verify and rename. Fewer round trips, but he has to get both device sizes.
3. **A DEBUG-only launch argument** — `-uiScreen cyclops|detail|dest` — so I can drive the set headlessly and regenerate it any time copy or data changes. ~30 lines, `#if DEBUG` only, never in Release. **Worth it only if screenshots get redone more than once**, which captions or a new city would both cause.

---

## 5. Open

- [ ] **Jim: plain or captioned?** Recommendation above is plain for GM 1.0, captions in 1.1.
- [ ] **Jim: include the no-live-data shot?**
- [ ] **Jim: which capture route** — option 1 above unless he says otherwise.
- [ ] Mine: confirm the required sizes against **ASC's own Media Manager** before anything is uploaded, rather than against any documentation.
- [ ] Mine: a zh-Hant set as well as English, since the screens are already localised and it is one locale flag.

---

## 6. App previews — the video in the first slot (new 2026-11-04)

Jim spotted that **SpotHero's first "screenshot" is an animation** and asked whether we can do the same: https://apps.apple.com/us/app/spothero-1-rated-parking-app/id499097243

**It is an App Preview video, confirmed from their page's raw JSON rather than its rendered text:**

```json
{"$kind":"ProductMediaItem","video":{"$kind":"Video",
 "videoUrl":"https://apptrailers.itunes.apple.com/itunes-assets/PurpleVideo112/v4/3c/4d/38/
             3c4d3883-8280-f59a-b2bf-7432f5300fdc/P829802554_default.m3u8"
```

One video, then **five** static screenshots. (Their listing is **English only** — no zh-Hant media at all, which is worth remembering before assuming the competition is doing more than it is.)

### The placement is not a choice — that is why it reads as "the first screenshot"

Apple's spec page, verbatim:

> **App previews always appear before screenshots** on iPhone, iPad, Mac, and Apple TV — even if you reorder them in your app record.

### The spec — from developer.apple.com, not from a guide

| | |
|---|---|
| **Accepted resolution** | **886 × 1920 portrait** (1920 × 886 landscape) |
| **…for which devices** | **every iPhone class** — Duo, Dynamic Island large *and* medium, Face ID large *and* medium. **One file covers all of them**, unlike screenshots |
| Length | **15 s minimum, 30 s maximum** |
| File | ≤ 500 MB · H.264 in `.mov` / `.m4v` / `.mp4`, or ProRes 422 (HQ only) in `.mov` |
| Frame rate | **max 30 fps** · target bit rate 10–12 Mbps |
| Audio | optional in practice; if present, stereo, 256 kbps AAC, 44.1/48 kHz |
| How many | **optional**, up to **3 per device size and language** |
| Poster frame | defaults to the **5 s** mark; selectable |
| Processing | **up to 24 hours after upload** |

**Why 886 × 1920 is not any device's real resolution**, in Apple's own words — this is the sentence that makes the whole workflow make sense:

> **Accepted resolution** is the resolution App Store Connect actually accepts for your app preview file — because most app previews are **recorded via screen recording** rather than rendered at native resolution, App Store Connect accepts a defined set of standard portrait or landscape resolutions per display size instead of requiring an exact per-device match. **Use the accepted resolution — not the device resolution** — when preparing your video file.

> [!warning] ⚠️ The trap: mismatch the aspect ratio and you lose the slot you did it for
> *"If you upload an app preview in an aspect ratio that differs from your screenshots, it appears in the **'A Closer Look'** section on your product page."* All the work, none of the placement. **886 × 1920 is 19.5:9, which matches our 1320 × 2868 and 1206 × 2622 stills**, so this is safe as planned — but it is the reason not to improvise the dimensions.

### Can we produce one here

**Yes, with two gaps.** `xcrun simctl io <device> recordVideo --codec h264` exists and records the booted simulator to a QuickTime movie — verified on this machine, 2026-11-04.

| Gap | Detail |
|---|---|
| **Navigation, worse than for stills** | A screenshot needs one static screen. **30 seconds of preview needs continuous, deliberate movement** — and `simctl` cannot inject a tap, with no `Simulator.app` for desktop automation either (§4). Jim drives, I record. |
| **No encoder** | Recording comes out at device resolution (1320 × 2868); it has to be resampled to **886 × 1920**. **`ffmpeg` is not installed** and `/usr/bin/avconvert` cannot target an arbitrary size. Needs `brew install ffmpeg` — **Jim's machine, Jim's call** — or an export from iMovie/QuickTime. |

### Recommendation: 1.1, not GM 1.0

1. **It is explicitly optional**, and the only item of its kind on the list that is.
2. **It can be added later with no binary and no app review** — media is replaceable at any time, same as screenshots.
3. **Up to 24 hours of processing** is a real scheduling hazard next to a submission date.
4. **Its value is conversion optimisation**, which pays against real traffic. In launch week there is almost none, and that is also when [[release-strategy]] says exposure is at its lifetime minimum.
5. It is **the longest-lead item on the whole GM 1.0 list** — and the only one that nothing requires.

**If we do it in 1.1, the shot list in §2 is already the storyboard**: map → pin → sheet → All with filters → Cyclops → destination. Five beats in 30 seconds is about 5 s each, which is also roughly the minimum a viewer needs to read a screen.
