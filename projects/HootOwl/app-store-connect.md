# App Store Connect — all the copy

**The single page for everything App Store Connect asks you to type.** Listing metadata, TestFlight, review notes — all of it, paste-ready, in the order ASC asks for it.

Started 2026-09-14. **This page grows; it does not spawn siblings.** Every further piece of ASC copy — description, keywords, 中文, What to Test for build 2, review notes for a resubmission — gets appended here rather than becoming its own note. That is the point of it.

App: **`Find Parking TW` / `找車位`** · ASC app id `6612022714`

> [!info] Related
> [[release-strategy]] — *how do I get through review*, and the rejection worth betting on · [[operations#2-release-checklist]] — the full pre-submit checklist · [[jim-actions]] — the ASC items only Jim can do · [[zh-review]] — the 中文 pass

> [!warning] I have no App Store Connect access
> Everything here is **copy to paste**, not changes made. If a field name has moved or a limit has changed, the text still fits — but nothing below has been checked against the live form.

---

# Part 1 — The field map

Two separate forms, and it is easy to fill in the wrong one. **Which build a field is attached to decides how expensive a mistake is.**

## App Store listing (the public product page)

| Field | Limit | Changeable without a new build? | Where it shows |
|---|---|---|---|
| **App Name** | 30 | no — tied to a version | everywhere |
| **Subtitle** | 30 | no — tied to a version | under the name |
| **Promotional Text** | 170 | **yes, any time** | **above** the description on the product page |
| **Description** | 4,000 | no — tied to a version | product page, behind "more" |
| **Keywords** | 100 | no — tied to a version | invisible; search only |

## TestFlight

| Field | Where | Scope | Needed for **internal** testing? | Needed for **external**? |
|---|---|---|---|---|
| **What to Test** | the build's own page | **per build** | optional, but it is the whole point | yes |
| **Beta App Description** | TestFlight → Test Information | per app | no | **yes** |
| **Feedback Email** | TestFlight → Test Information | per app | no | **yes** |
| **Marketing URL / Privacy Policy URL** | Test Information | per app | no | privacy policy yes |
| **Sign-in required + demo account** | Test Information | per app | n/a — the app has no login | n/a |
| **Beta App Review Information** (contact + notes) | Test Information | per app | **no** | **yes** |

**Internal testing needs almost none of this.** No Beta App Review, no Beta App Description, no feedback email — you add yourself as an internal tester and install as soon as the build finishes processing. Only *What to Test* matters today.

**Two fields are the cheap ones**, and they are worth knowing by name because they are where you can afford to change your mind later: **Promotional Text** (any time, no build) and **What to Test** (per build, so it is rewritten each time anyway).

---

# Part 2 — App Store listing

## 2.1 Name and Subtitle — decided

Decided 2026-09-10, wired in `InfoPlist.xcstrings`, reasoning in [[decisions#2026-09-10-app-name-find-parking-tw--找車位]].

- **Name:** `Find Parking TW` / `找車位`
- **Subtitle:** `Taipei & New Taipei parking` — 27/30

Coverage lives in the **subtitle** on purpose, so it can change every release without renaming the app. Check the name is still available before you commit to it.

Because the subtitle already says *where*, nothing else on the page has to open with it — the rest is free to say *why this one*.

## 2.2 Promotional Text — English · 170 characters

### ✅ Chosen — C · 159/170 · Jim's call, 2026-10-07

```text
New: live car park availability for Taipei and New Taipei City. Pin the lots you use and watch their space counts update on their own, straight from city data.
```

> Jim: *"I prefer C, straight forward and also finger point to city data!"*

**The two qualities he named are the right read of it.** It says what the app does in one clause with no setup, and it **attributes the numbers to the cities** — which is the credibility claim this app actually has and most parking apps do not. A user who knows the counts come from the city government reads a stale number as the city's feed being quiet, not as the app being wrong.

> [!note] My own recommendation was different, and it is worth keeping on the page
> I argued for the freshness-fading line below, and against C on the grounds that **"New:" is wasted on a launch where everything is new** — save that framing for the day a city is added, which is what this editable field is for.
>
> That objection still stands **about the prefix only**, not about C. Jim named straightforwardness and the data pointer, and neither depends on the word "New". **Both forms are drafted below; the prefix is one phrase to drop.**

### Previously recommended — the freshness angle

```text
Live space counts for car parks across Taipei and New Taipei City. Numbers fade as they age, so you can always tell a fresh count from one that stopped moving.
```

Every parking app claims "real-time". Almost none admit that a feed goes quiet, and the result is a number that looks authoritative and is an hour old. This app is the one that shows the difference — pin opacity on the map, colour on the watch list, both on the same 5- and 30-minute thresholds. **That is the real differentiator, it is shipped, and it is the sentence a person nods at.** It also sets the expectation that counts are sometimes stale, which is the likeliest source of a one-star review.

### Alternatives

|                          | Text                                                                                                                                                                        | Chars |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **B — plain benefit**    | `Know whether there's a space before you drive there. Live counts for public car parks across Taipei and New Taipei City, straight from the city open data feeds.`          | 160   |
| **D — short and blunt**  | `Stop circling the block. Live space counts for Taipei and New Taipei City car parks, every number showing how recent it is.`                                               | 123   |
| **E — watch-list angle** | `Pin the car parks you actually use and watch their free spaces update on their own. Live open data for Taipei and New Taipei City, with a freshness clock on every count.` | 169   |

**B** is the safest and the most forgettable — it describes the category, not this app. **C is now the chosen text, above.** **D** has the only real voice here, but "stop circling the block" promises an outcome the data cannot always deliver. **E** says the most and reads like a feature list.

### Rules this copy stays inside

- **No pricing claims.** Free with ads, subscription removes them — "free" ages badly in a field you will forget to edit, and Apple shows the price anyway.
- **No superlatives, no competitor references.** "The best", "the only", naming another app — rejection surface for zero gain.
- **Nothing the app does not do.** No routing, no reservations, no payment, no prediction.
- **No emoji.** Inconsistent across locales, and noise on a utility app.

## 2.3 Description — English · paste-ready

**Drafted 2026-10-05.** **1707 / 4,000 characters.** Every claim below was checked against the source or the vault, not written from imagination — see *What each claim rests on* after the text.

> [!important] The first paragraph is doing the most work on this page
> App Store collapses the description after a couple of lines, so **the opening sentence is the only part most people read** — and it is **the one place a reviewer learns the coverage before installing.** The app is called `Find Parking TW`; it covers **Greater Taipei**. The subtitle carries that correction and so must this.

```text
Live space counts for public car parks across Taipei City and New Taipei City, straight from the two city governments' own open data.

See where there is room before you set off, instead of after you have circled the block twice.


WHAT IT DOES

• Live space counts on a map of what is near you, closest first
• Pin the car parks you actually use — open the app and every count is already there
• Numbers fade as they age, so you can always tell a fresh count from one that has stopped moving
• Search any address, or browse every car park by name, district or ID
• Planning a trip? Choose the city and the whole app works before you arrive


COVERAGE

Taipei City and New Taipei City today — more than 3,000 public car parks between them. Other cities will follow as their open data becomes available, and you can tell us which one you need from inside the app.


ABOUT THE NUMBERS

Counts come straight from the city feeds and are only ever as fresh as the feeds themselves. Some car parks do not publish live availability yet; the app says so rather than guessing, and a count that has stopped updating is shown as old rather than as current. Nothing is estimated and nothing is invented.


PRIVACY

Your location is used on your device, to find the car parks nearest you and to centre the map. It stays there. The app has no servers of its own and never receives where you are.


FREE, WITH ADS

Find Parking TW is free and shows a banner advert. An optional subscription removes the banner; every other part of the app works exactly the same either way.


DATA SOURCES

Parking data from the Taipei City and New Taipei City open data platforms, used under the Open Government Data License, version 1.0.
```

### What each claim rests on

| Claim | Basis |
|---|---|
| *"straight from the two city governments' own open data"* | `TaipeiObs` / `NewTaipeiCityObs` fetch the city portals directly. [[data-sources]] |
| *"more than 3,000 public car parks"* | **3,124** in the quadtree on 2026-10-05. Deliberately "more than 3,000" rather than a precise figure — the feeds move daily |
| *"closest first"* | the nearby search sorts by distance from the search centre |
| *"Numbers fade as they age"* | `5048976` — solid under 5 min, 0.7 at 5–30 min, 0.45 beyond |
| *"browse every car park by name, district or ID"* | the All tab searches `"\(id) \(name) \(address) \(area)"`, and is **not** location-filtered |
| *"Choose the city and the whole app works before you arrive"* | destination mode, [[destination-mode]] |
| *"Some car parks do not publish live availability yet"* | New Taipei's own portal: lots mid-operator-change report `-9`. Saying so is more honest than hiding them — [[data-sources]] |
| *"no servers of its own and never receives where you are"* | **verified by grep over every `URLRequest`/`dataTask` site**: whole-city datasets are downloaded and filtered on-device; no coordinate is ever put in a request. [[privacy-policy]] |
| *"removes the banner; every other part works exactly the same"* | true today and stated on the purchase screen. **If subscriber-only features are ever added, this line must change** — see D-01 |
| the **Data sources** paragraph | **word-for-word the app's own `opt_attribution_body`**, so the listing and the app cannot drift. 政府資料開放授權條款－第1版 requires the credit |

### Deliberately not said

- **No "real-time".** The feeds publish every 1–3 minutes; "live" is fair, "real-time" oversells it.
- **No count of cities "coming soon"**, and no dates. Keelung is the intended next zone ([[decisions]]) but nothing is promised.
- **No mention of bus tracking.** It is in the project's description but not in this build.
- **Nothing about ads beyond the one factual line.** The in-app note already pre-frames it; the listing does not need to argue.

## 2.3b Description — 中文 · ✅ drafted 2026-10-06, see §2.5 (every field, not just the description)

**The one that matters more**, for a Taipei-primary app. It is a separate localisation in App Store Connect, and a translation of the English above will read worse than copy written in Chinese — so it wants its own pass alongside [[zh-review]], not a machine translation of this. Tracked as **R-17**.


Must carry the data-source attribution: **臺北市政府交通局停車管理工程處** and **新北市政府交通局**, published under **政府資料開放授權條款-第1版**. That is a licence obligation, not an App Review one — [[release-strategy#a-licence-obligation-nobody-has-noticed]].

## 2.4 Keywords — paste-ready

**58 / 100 characters.** Comma-separated, no spaces — App Store counts the spaces.

```text
parking,car park,parking lot,parking space,availability,live,garage,taiwan,find parking,open data
```

> [!warning] Corrected 2026-10-06
> This field held mostly **Chinese** terms when first drafted. Keywords are **per-localisation**, so Chinese belongs in the zh-Hant field (§2.5) and this one should spend its 100 characters on English. Swapped.

**Why these.** Apple already indexes the **app name and subtitle**, so nothing here repeats *Find Parking TW*, *Taipei* or *New Taipei* — that space would be wasted. What is left is what a driver in Taiwan actually types:

- **停車場 · 車位 · 停車位 · 停車** — the plain words, in the forms people search
- **即時車位** — the thing that makes this app different from a static map
- **公有停車場** — matches the feeds' own framing (公有路外停車場)
- **路邊停車** — on-street, which users search for even where coverage is car parks
- **找停車 · 空位 · 停車資訊** — intent phrasings
- **parking · car park** — for visitors searching in English, and the only English worth the characters

**Revisit after the first release**, not before: App Store Connect reports actual search terms, and guessing twice is cheaper than guessing once and leaving it.

The field that actually affects search. Do not repeat the name or subtitle in it; Apple already indexes those.

---

## 2.5 繁體中文 — every field, paste-ready

**Drafted 2026-10-06.** Written *as* Chinese rather than translated from §2.3 — a translation of English marketing copy reads like translated English marketing copy, and this is the primary market.

> [!warning] 🀄 Needs Jim's pass before it goes in
> Same standing as the `needs_review` strings: the wording is mine, and Jim has corrected my Chinese before. **Nothing here should be pasted until he has read it.** → [[zh-review]]

### The voice came from the app, not from me

Every choice below matches what the app already says, so the listing and the product sound like one thing:

| | The app's own usage | Followed |
|---|---|---|
| the city | **台北市** (`city_taipei`) | ✅ |
| the government | **臺北市政府** (`opt_attribution_body`) | ✅ — 台 for the city, 臺 for the institution, which is what the portals themselves do |
| pinning | **釘選** (`onb_s2_body`) | ✅ |
| live counts | **即時車位** (`onb_s1_title`) | ✅ |
| subscribing | **訂閱** — decided over 課金, 2026-09-09 | ✅ |
| the fading | **「隨著時間，未更新的數字顏色越淡」** | ✅ paraphrased, not re-invented |
| address | **你** throughout, and `App` in Latin letters | ✅ |

### Name — 3 characters

```text
找車位
```

Already live in `InfoPlist.xcstrings` as `CFBundleDisplayName`. Decided 2026-09-10.

### Subtitle — 15 / 30 characters

```text
台北・新北 公有停車場即時車位
```

Carries the coverage, as the English one does. **公有** is deliberate — it matches the feeds' own framing (公有路外停車場) and quietly sets the expectation that this is not private or on-street.

### Promotional text — 70 / 170 characters

**Rewritten 2026-10-07 to match the English C**, on Jim's call. The earlier Chinese followed the freshness angle; this one is straightforward and points at the city data, which is what he asked for.

```text
全新上線：台北市與新北市公有停車場的即時剩餘車位。釘選你常用的停車場，車位數會自己更新——資料直接來自臺北市政府與新北市政府的開放資料平臺。
```

**Without the launch prefix** — 65 / 170, and the form I would ship on a *first* release, since 「全新上線」 has nothing to be new against:

```text
台北市與新北市公有停車場的即時剩餘車位。釘選你常用的停車場，車位數會自己更新——資料直接來自臺北市政府與新北市政府的開放資料平臺。
```

**Why the pointer is spelled out rather than implied.** The English says *"straight from city data"*; Chinese has room for **「資料直接來自臺北市政府與新北市政府的開放資料平臺」**, naming both governments outright. At 170 characters that costs nothing and it is the whole credibility claim — a reader who knows the numbers come from the city reads a quiet feed as the city's quiet feed, not as a broken app. Note **臺** for the institutions, matching the app's own attribution string.

**This is the one listing field that changes without a build.** Safe to paste and rethink any time — and the natural place for 「全新上線：基隆市」 on the day Keelung lands.

### Description — 608 / 4,000 characters

Shorter than the English, and that is not laziness: Chinese says the same thing in fewer characters, and padding it would only bury the opening.

```text
台北市與新北市公有停車場的即時剩餘車位，資料直接來自兩市政府的開放資料。

出門前就知道哪裡還有位子，不用繞到現場才發現繞第二圈。


功能

• 地圖顯示你附近的停車場，最近的排在最前面，車位數即時更新
• 把常用的停車場釘選起來，打開 App 就直接看到，不用再找
• 數字會隨時間變淡，一眼就能分辨哪些是剛更新的、哪些已經停止回報
• 可以搜尋任何地址，也可以用名稱、行政區或編號查全部停車場
• 要去台北？先選城市，人還沒到，整個 App 就已經可以用了


涵蓋範圍

目前是台北市與新北市，兩市合計超過三千個公有停車場。其他縣市會隨著開放資料到位陸續加入——你也可以在 App 裡直接告訴我們你需要哪一個。


關於這些數字

車位數直接來自各市的資料來源，資料有多新，App 就有多新。有些停車場目前還沒有提供即時車位，App 會直接說明，不會猜；已經停止更新的數字也會標示成舊資料，而不是假裝還是即時的。不推估，不編造。


隱私

定位只在你的裝置上使用，用來找出最近的停車場、把地圖對到你的位置，而且就留在裝置上。這個 App 沒有自己的伺服器，也從來不會收到你在哪裡。


免費，有廣告

「找車位」免費，畫面上會有一則橫幅廣告。訂閱可以把廣告關掉；除此之外，App 的其他部分完全一樣。


資料來源

停車資料來自臺北市政府與新北市政府開放資料平臺，依「政府資料開放授權條款－第1版」使用。
```

**The final paragraph is `opt_attribution_body` word for word** — the app's own Chinese attribution string, so the listing and the app cannot drift on a licence obligation.

### Keywords, 繁體中文 — 52 / 100 characters

```text
停車場,車位,停車位,即時車位,公有停車場,路邊停車,找停車,停車,空位,停車資訊,車位查詢,停車位查詢
```

> [!important] ⚠️ This corrects yesterday's §2.4
> **Keywords are per-localisation**, and yesterday I put mostly *Chinese* terms in the **English** field. That spends the English listing's 100 characters on words its readers are not typing, and leaves the zh-Hant field — the one Taiwanese users actually hit — to be filled separately anyway. **The Chinese terms belong here; the English field should spend its characters on English.** §2.4 is corrected to match.

Added beyond the English set: **車位查詢 · 停車位查詢** — query phrasings people actually type, and there was room.

### Keywords, English — 97 / 100 characters

```text
parking,car park,parking lot,parking space,availability,live,garage,taiwan,find parking,open data
```

Repeats neither the app name nor the subtitle, since Apple indexes both. **taiwan** is in because an English-language searcher is almost certainly a visitor, and that is the word they would use.

### Still owed for the 中文 listing

- [ ] **Jim's wording pass** on everything above
- [ ] **Screenshots** — separate from this, and they need Chinese captions if captioned at all
- [ ] **App Information localisation** in ASC is a *third* thing again, separate from both the listing and the app's own strings

---

## miscellaneous

to claude-code: these seems to be app agnostic, or I can tune them to be. 

support Url :
https://jimhsuyc.wixsite.com/tataro/support
need to add action so that this page is app agnostic 

marking url 
https://n90287707.app-ads-txt.com


# Part 3 — TestFlight

## 3.1 What to Test — build 1 · paste-ready

Per build, does not carry forward. Build 2 gets a fresh one, and the useful version of it is *what changed since build 1*. Build 1 is the exception, because there is no "since".

Written for the only tester there is: **you, on a real device, in Taipei.** It deliberately doubles as the device pass owed since June — walk it once and [[jim-actions]] loses five items.

Limit is 4,000 characters; this is well under.

```text
First build. Taipei and New Taipei City only — outside those two cities the app has no data yet, and does not currently say so.

Install over a DELETED copy, not an update. Several things below only happen once per install.

1. First launch
   - Three intro screens, then the location permission dialog.
   - Note WHICH screen the location dialog appears on (1st or 3rd). If it is the 1st, screen 3's copy is describing a prompt that already happened.
   - Tap the tutorial video link. It currently points at a placeholder clip.
   - The "tell us where you need it most" prompt has no working mail button yet. Expected.

2. Second launch (quit fully, relaunch)
   - The App Tracking Transparency prompt should appear now, not on the first launch.
   - Once per install: to retest, delete and reinstall.

3. Near Me! tab
   - Nearby car parks with live space counts.
   - Leave the app open past five minutes: map pins fade as their numbers age (solid under 5 min, fainter at 5-30 min, faintest beyond). The question is legibility over busy map detail, not correctness.

4. Auto tracking tab
   - Your pinned lots, with numbers that update on their own.
   - On a cold launch with no cached data, a clock glyph appears instead of numbers. It should clear within about 15-20 seconds. If it never clears, that is the bug being hunted.

5. All tab
   - Every lot, searchable. Type into the search field and then dismiss the keyboard — it should go away.
   - Pin and unpin a lot; pins are shared with the Auto tracking tab.
   - Open a lot's detail and tap the phone number. It dials the city office with an extension appended.

6. Subscribe tab
   - Should read "Subscribe" before purchase and "My Subscription" after.
   - Restore Purchases must work.
   - A subscription removes the ad banner and nothing else. The copy says so.

7. Backgrounding
   - Background the app for a minute and return. Numbers should refresh promptly, not sit stale.
   - Lock and unlock; switch apps and come back. Nothing should stutter or double-refresh.

8. The app icon
   - New this build. Check the home screen: it should be opaque, edge to edge, with nothing clipped by the rounded corners, and no owl.

Known and expected, do not report:
- "Upload Symbols Failed" on upload — the ad SDK ships without symbols. Permanent, not fixable.
- Some New Taipei lots show no count: those car parks are mid-operator-change and genuinely do not report yet.
- No "we do not cover your area" message outside Taipei/New Taipei. That is the next thing being built.
```

ASC lets you localise *What to Test* per language. Skip the 中文 version until there is a tester who needs it.

## 3.2 Beta App Description — paste-ready

Tester-facing, shown in the TestFlight app. Required before external testing.

```text
Find Parking TW shows live space counts for public car parks in Taipei City and New Taipei City, using the two city governments' open data feeds.

Three ways in: car parks near you on a map, a searchable list of every lot, and a watch list of the ones you use that updates on its own. Counts fade as they age, so you can tell a fresh number from a stale one rather than trusting a figure that stopped moving an hour ago.

Coverage is Taipei and New Taipei City only. Data comes from 臺北市政府交通局停車管理工程處 and 新北市政府交通局.
```

## 3.3 Feedback Email

ASC wants an address here, and it is **separate from the `support.email` still missing from the Gist** ([[jim-actions]]) — this one is shown only to TestFlight testers and used only for their feedback. Your own address is the right answer for a build whose only tester is you. **Filling this in does not close the Gist item.**

## 3.4 Beta App Review Information — paste-ready

**Not needed until you invite an external tester.** When you do, the Notes field is what prevents the rejection [[release-strategy#the-one-risk-i-would-bet-money-on]] is about — a reviewer opens the app in California and sees nothing.

> [!success] Rewritten again 2026-09-19 — **the map is testable too, and that is the better instruction**
> The 09-18 version led with the All tab, which works but shows a *list*. The app's actual proposition is a live map, and it turns out a reviewer can drive that from California with **no setup at all**:
> - The map screen carries an **address search bar** (`NbsScreen.swift:172`, `AddressSearchBar` in `.principal`), and resolving an address calls `nbs.search(mapMode: .mapTap, loc0: coord)` — **a search around an arbitrary point, with no reference to the user's location**.
> - It biases to `AddressSearchObs.taiwanRegion`. **Verified against the live geocoder 2026-09-19 with that exact region**: `Taipei 101` → 25.0336, 121.5648 ✅ · `Taipei Main Station` → 25.0486, 121.5149 ✅ · `台北101` ✅ · `信義區` ✅. **English works**, so no IME is needed.
> - The outside-coverage card is an **overlay, not a takeover** (`NbsScreen.swift:60-75` — *"the map stays pannable, so someone curious can still look at Taipei"*), so panning and tapping the map also work.
>
> So the notes now lead with the map, keep the All tab as the second route, and the simulator instructions are gone entirely — a reviewer has neither your simulator nor your Xcode.

> [!info] The 09-18 rewrite, for the record
> The 09-14 draft said *"the full list is not location-filtered"* and buried it as the **second** option, behind simulator and Xcode instructions. **The claim is true — checked in the code, not assumed** — and the ordering was backwards. A reviewer has your binary on a device; they have neither your simulator nor your Xcode project. **The All tab is the whole answer and now leads.**
>
> **What was verified:**
> - `MncplAllScreen.filtered()` (`:68`) filters by mode and search text only — **never by distance**. `items` (`:52`) is `municipal.actParkInfos.values.flatMap(\.items)`: every lot of every loaded city.
> - The coverage notice appears on that screen only when `displayItems.isEmpty && searchText.isEmpty` (`:111`), so a populated list is never covered by it.
> - The app downloads **whole-city datasets wherever you are** — the 09-16 Cupertino run pulled 1,770 Taipei + 1,392 New Taipei lots and built the quadtree from 3,162, with live availability. Only the map and nearby list were blocked.
> - **`TPE` matches all 1,773 Taipei lots. `tpe` matches 0. `Taipei` matches 0.** Checked against the live `TCMSV_alldesc.json`. Search is `contains`, case-sensitive, over `"\(id) \(name) \(address) \(area)"`.
> - The Chinese suggestions do work — 信義 158, 大安 246, 臺北 113, 台北 63 — **but need an IME the reviewer does not have.** Keep them as a fallback, never as the first instruction.

- **Sign-in required:** No.
- **Contact:** your name, email and phone.
- **Notes:**

```text
This app shows live public car-park availability for Taipei City and New Taipei City, Taiwan, from the two city governments' open data feeds. There is no account and no login.

COVERAGE: Greater Taipei only — Taipei City and New Taipei City. The app is not intended for use elsewhere, including the United States. Outside those two cities it says so on screen rather than showing an empty map.

HOW TO SEE THE MAP WORKING FROM CALIFORNIA — no setup, no location changes:
1. Open the first tab ("Nearby").
2. Tap the search field at the top and type: Taipei 101
3. Pick the result. The map recentres on Taipei and fills with car parks; the number on each pin is that car park's live free-space count, refreshed from the city feed.
4. Tap any pin for details. You can also tap anywhere on the map to search around that point, and drag to explore.

Other queries that work: Taipei Main Station, Taipei City Hall.

HOW TO SEE THE FULL LIST — also works anywhere in the world:
1. Open the "All" tab.
2. Type TPE in the search field.
3. About 1,700 Taipei car parks appear, with live counts and total capacity. This list is not filtered by your location.

WHY THE MAP IS EMPTY BEFORE YOU SEARCH: it shows car parks near you, and there are none within range outside Taiwan. Instead of a blank screen the app names the cities it does cover. That is the designed behaviour for this case, not a failure.

SUBSCRIPTION: removes the advertising banner and changes nothing else. This is stated plainly on the purchase screen. Restore Purchases is on both the purchase and subscribed screens, and both the Privacy Policy and Terms of Use are linked there.

APP TRACKING TRANSPARENCY: requested on the second launch, after the app has been seen working — never as a gate to using it.

DATA SOURCES: 臺北市政府交通局停車管理工程處 and 新北市政府交通局, published under 政府資料開放授權條款-第1版. Credited in the app under Options > Data source.
```

```

## 3.5 App Review Notes — the real submission

**Use §3.4 as written.** It needs no edit for the real submission: nothing in it is TestFlight-specific. **Do not skip this field even now that the empty state ships** — the empty state explains the map; only these notes tell a reviewer the All tab exists and works.

**Worth adding when it exists:** a link to the demo video (R-13). Apple accepts one in this field, and for a geo-restricted app it is the single strongest artifact — it shows the app working in Taipei without the reviewer having to reproduce anything.

---

# Part 4 — Still owed on this page

- [x] ~~**Description** (4,000, English)~~ — **drafted 2026-10-05, §2.3**, attribution line included verbatim from the app's own string.
- [x] ~~**Keywords** (100)~~ — **drafted 2026-10-05, §2.4.**
- [x] ~~**中文 for everything above**~~ — **drafted 2026-10-06, §2.5**: name, subtitle, promotional text, description and keywords, written as Chinese rather than translated. **Awaiting Jim's wording pass** before anything is pasted.
- [ ] **What to Test for build 2** — rewritten as *what changed*, not the whole app again.
- [x] ~~**App Review Notes** for the real submission~~ — **done 2026-09-18**: §3.4 needs no edit, see §3.5. Still owed: the demo-video link once R-13 exists.

---

# Changelog

- **2026-09-18** — §3.4 rewritten and §3.5 added. The draft's key claim (*the list is not location-filtered*) was **verified in the code and against the live feed** rather than left as an assertion, and the instruction order was inverted: the All tab plus an uppercase `TPE` search now leads, because a reviewer has the binary and not your simulator. Found in passing that `tpe` matches nothing, which promotes **J-01** from a backlog nicety to rejection insurance.
- **2026-09-14** — page created by folding together the two notes written earlier the same day (`testflight` and `store-listing`), so that all ASC copy lives in one place. Contents: the field map, name/subtitle, Promotional Text (5 options), What to Test for build 1, Beta App Description, Feedback Email, Beta App Review notes.
