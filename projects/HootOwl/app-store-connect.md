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

### Recommended · 159/170

```text
Live space counts for car parks across Taipei and New Taipei City. Numbers fade as they age, so you can always tell a fresh count from one that stopped moving.
```

Every parking app claims "real-time". Almost none admit that a feed goes quiet, and the result is a number that looks authoritative and is an hour old. This app is the one that shows the difference — pin opacity on the map, colour on the watch list, both on the same 5- and 30-minute thresholds. **That is the real differentiator, it is shipped, and it is the sentence a person nods at.** It also sets the expectation that counts are sometimes stale, which is the likeliest source of a one-star review.

### Alternatives

| | Text | Chars |
|---|---|---|
| **B — plain benefit** | `Know whether there's a space before you drive there. Live counts for public car parks across Taipei and New Taipei City, straight from the city open data feeds.` | 160 |
| **C — launch framing** | `New: live car park availability for Taipei and New Taipei City. Pin the lots you use and watch their space counts update on their own, straight from city data.` | 159 |
| **D — short and blunt** | `Stop circling the block. Live space counts for Taipei and New Taipei City car parks, every number showing how recent it is.` | 123 |
| **E — watch-list angle** | `Pin the car parks you actually use and watch their free spaces update on their own. Live open data for Taipei and New Taipei City, with a freshness clock on every count.` | 169 |

**B** is the safest and the most forgettable — it describes the category, not this app. **C** wastes "New" on a launch where everything is new; save that framing for the day a city is added, which is exactly what this field is for. **D** has the only real voice here, but "stop circling the block" promises an outcome the data cannot always deliver. **E** says the most and reads like a feature list.

### Rules this copy stays inside

- **No pricing claims.** Free with ads, subscription removes them — "free" ages badly in a field you will forget to edit, and Apple shows the price anyway.
- **No superlatives, no competitor references.** "The best", "the only", naming another app — rejection surface for zero gain.
- **Nothing the app does not do.** No routing, no reservations, no payment, no prediction.
- **No emoji.** Inconsistent across locales, and noise on a utility app.

## 2.3 Description — not written yet

Must carry the data-source attribution: **臺北市政府交通局停車管理工程處** and **新北市政府交通局**, published under **政府資料開放授權條款-第1版**. That is a licence obligation, not an App Review one — [[release-strategy#a-licence-obligation-nobody-has-noticed]].

## 2.4 Keywords — not written yet

The field that actually affects search. Do not repeat the name or subtitle in it; Apple already indexes those.

---

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

- [ ] **Description** (4,000, English) — with the attribution line.
- [ ] **Keywords** (100).
- [ ] **中文 for everything above.** A separate localisation in ASC, and a translation of the English will read worse than copy written in Chinese. Its own pass, alongside [[zh-review]].
- [ ] **What to Test for build 2** — rewritten as *what changed*, not the whole app again.
- [x] ~~**App Review Notes** for the real submission~~ — **done 2026-09-18**: §3.4 needs no edit, see §3.5. Still owed: the demo-video link once R-13 exists.

---

# Changelog

- **2026-09-18** — §3.4 rewritten and §3.5 added. The draft's key claim (*the list is not location-filtered*) was **verified in the code and against the live feed** rather than left as an assertion, and the instruction order was inverted: the All tab plus an uppercase `TPE` search now leads, because a reviewer has the binary and not your simulator. Found in passing that `tpe` matches nothing, which promotes **J-01** from a backlog nicety to rejection insurance.
- **2026-09-14** — page created by folding together the two notes written earlier the same day (`testflight` and `store-listing`), so that all ASC copy lives in one place. Contents: the field map, name/subtitle, Promotional Text (5 options), What to Test for build 1, Beta App Description, Feedback Email, Beta App Review notes.
