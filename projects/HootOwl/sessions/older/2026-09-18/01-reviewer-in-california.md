# The reviewer in California — how little work it actually takes

**Question (Jim, 2026-09-18):** if the app is reviewed in California, how do we help the reviewer check it with the least work?

**Answer: no code, one text field.** And the reason is a property of the app nobody had written down as an asset.

---

## The app already works in California

`MncplAllScreen` — the **All** tab — is **not filtered by location**. Verified in the code, not assumed:

| Where | What it does |
|---|---|
| `MncplAllScreen.swift:68` `filtered(avMap:)` | filters by **mode** and **search text** only — no distance term anywhere |
| `MncplAllScreen.swift:52` `items` | `municipal.actParkInfos.values.flatMap(\.items)` — every lot of every loaded city |
| `MncplAllScreen.swift:111` | the coverage notice appears **only** when `displayItems.isEmpty && searchText.isEmpty`, so a populated list is never covered by it |

And the data is on the device regardless of where the device is — the app downloads **whole-city datasets** and filters locally. From the 09-16 Cupertino run:

```
🐢 daily ["newTaipeiCity ⏳d:16,h:14 ⨊1392 ", "taipei ⏳d:16,h:14 ⨊1770 "]
NbsObsM+Ext 25 init0()  parkInfoVbj → building QuadTree from 3162 items
🐎 minutelyAvailable ["taipei ⏳16 14:00 ∑1178", "newTaipeiCity ⏳16 12:04 ∑1411"]
```

**So in California: the map says *"We're not here yet"*, and the All tab shows 3,162 real car parks with live numbers.** Only the map and Nearby are blocked, and both now explain themselves.

> [!note] This is the same property that makes the privacy story strong
> "No coordinate is ever put in a network request" and "a reviewer can use the app from California" are the **same fact** seen from two directions: the app fetches whole cities and filters on-device. Worth knowing that the privacy decision paid for itself twice. See [[privacy-policy#what-the-app-actually-does-with-data--verified-against-the-source]].

## The one line that makes it work on a US keyboard

The 09-14 draft suggested searching `台北`, `信義`, `大安`. **They all match** — checked against the live `TCMSV_alldesc.json`: 信義 158, 大安 246, 臺北 113, 台北 63.

**But a reviewer in California would need a Chinese IME to type any of them.**

Every Taipei lot id is `TPE####`. Search is `contains` over `"\(id) \(name) \(address) \(area)"` (`MncplParkItem.swift:176`):

| Term | Matches |
|---|---|
| `TPE` | **1,773** — every Taipei lot |
| `tpe` | **0** |
| `Taipei` | **0** |

**The instruction is "type `TPE`, in capitals."** One term, no IME, the whole city.

## What was wrong with the drafted notes

The 09-14 draft was **right on the facts and backwards in its ordering**. It led with:

- *"Simulator: Features > Location > Custom Location…"*
- *"Device: Xcode > Debug > Simulate Location…"*

**A reviewer has neither.** They have the binary on a device, no Xcode project and no simulator of yours. The one option that actually works for them — the All tab — was listed last, as a clause. Rewritten: the All tab leads, the simulator lines survive as an optional footnote for a populated map.

## `tpe` → 0 changes the priority of J-01

[[Jim's backlog]] item 1 — *"the search should be case insensitive, or simply move English upper, since I have to type TPE0155 or tpe0155 will not click!"* — has been a usability nicety since June.

It is now **rejection insurance**. A reviewer who follows the notes, types lowercase out of habit, and gets an empty list has just been shown an app that appears broken. One `localizedCaseInsensitiveContains` in `MncplAllScreen.swift:77` removes that failure mode — and fixes the bug Jim actually reported.

**Promoted to R-21.**

## What this does *not* solve

- **The request-a-city button still does not render.** `CoverageNoticeView.swift:132,154` hide both the ask line and the button when no support URL is configured — and the `support` key was deliberately deleted from the Gist. So the outside-coverage screen currently ends at a statement. That is **R-02**, and the reviewer is exactly the person who proves why it matters: the one user who cannot use the app, and can still tell you where to go next.
- **A demo video** would be stronger than any of this, and is already owed as **R-13**. Apple accepts a link in the review-notes field.

## Related
[[app-store-connect#34-beta-app-review-information--paste-ready]] · [[release-strategy#the-one-risk-i-would-bet-money-on]] · [[00-state-of-play]] · [[Jim's backlog]]
