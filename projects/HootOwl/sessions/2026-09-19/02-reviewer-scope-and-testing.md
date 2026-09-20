# The California reviewer, part 2 — understanding the scope, and testing it

**Question (Jim, 2026-09-19):** review happens in California. How do we make them understand this app is for Greater Taipei only, and how do we intend to help them test it?

**Two separate problems.** Scope is a *communication* problem and is nearly solved. Testing looked like a *code* problem and turns out not to be one at all.

---

# Part 1 — Understanding that it is Greater Taipei only

Six places a reviewer could learn it. **Five exist. One is missing, and it is the one they read first.**

| # | Surface | Says | State |
|---|---|---|---|
| 1 | **Subtitle** | `Taipei & New Taipei parking` (27/30) | ✅ decided — sits directly under the app name |
| 2 | **Description** | — | ❌ **not written** (R-10) |
| 3 | **Screenshots** | — | ❌ not made (R-10) |
| 4 | **App Review Notes** | coverage stated in the second line | ✅ written, paste-ready |
| 5 | **Onboarding screen 1** | *"Taipei and New Taipei City today — more cities soon."* / 目前支援台北市與新北市，其他縣市陸續加入。 | ✅ shipping |
| 6 | **Outside-coverage screen** | *"We're not here yet — Right now we cover Taipei and New Taipei."* | ✅ shipping, exercised on the simulator |

**The gap is the store listing.** A reviewer meets the product page before the binary, and right now that page would carry the scope only in the subtitle.

> [!warning] The name says more than the coverage does
> **`Find Parking TW`** reads as *Taiwan*. The app covers **Greater Taipei** — someone in Kaohsiung or Tainan installs it and it does not work for them. That is a real metadata-accuracy risk, and the reason the subtitle carries the city names ([[decisions#2026-09-10-app-name-find-parking-tw--找車位]]).
>
> **So the description's first line has to do the same job.** Not a sentence about parking with the cities mentioned later — the cities in the opening clause, the way the subtitle does it. That is the single highest-value line in the whole listing, and it is unwritten.

---

# Part 2 — Helping them test it

**Three routes, all working today, none needing a code change, a simulator, or a faked location.**

## Route 1 — the map, via the address search ⭐ *the one to lead with*

The map screen carries an **address search bar** in its toolbar (`NbsScreen.swift:172`, `AddressSearchBar` in `.principal`). Resolving an address calls:

```swift
nbs.search(mapMode: .mapTap, loc0: coord)   // NbsScreen.swift:669
```

`.mapTap` searches **around an arbitrary point, with no reference to the user's location**. It is not a debug path — it is how map taps and address searches already work for every user.

The completer biases to `AddressSearchObs.taiwanRegion` (centre 23.6978, 120.9605; span 4.5 × 3.5). **Verified against the live geocoder with that exact region, 2026-09-19:**

| Query | Resolves to | |
|---|---|---|
| `Taipei 101` | 25.0336, 121.5648 | ✅ Greater Taipei |
| `Taipei Main Station` | 25.0486, 121.5149 | ✅ Greater Taipei |
| `台北101` | 25.0336, 121.5648 | ✅ |
| `信義區` | 25.0375, 121.5655 | ✅ |

**English works** — no IME needed, which matters for a reviewer on a US keyboard.

**This is the important one**, because it exercises what the app actually is: a live map of nearby parking, with a real free-space count on each pin. Every other route shows a list.

## Route 2 — the map, by panning and tapping

The outside-coverage card is an **overlay, not a takeover**. From `NbsScreen.swift:60-75`, written when the empty state shipped:

> *"A card rather than a full takeover — the map stays pannable, so someone curious can still look at Taipei."*

So a reviewer can drag to Taiwan and tap the map; the tap runs the same `.mapTap` search. Slower than typing an address, but it means a reviewer who never reads the notes can still stumble into the app working.

## Route 3 — the All tab, with `TPE`

Not location-filtered at all ([[sessions/2026-09-18/01-reviewer-in-california|yesterday's write-up]]). Type `TPE` and ~1,700 Taipei car parks appear with live counts and capacity. Works anywhere on earth, and needs no map interaction.

Since `9285a47` the search is case-insensitive, so `tpe` works too — which matters, because a reviewer following written instructions types what is written, in whatever case they are used to.

## Route 4 — the demo video, still owed

**R-13.** Apple accepts a link in App Review Notes, and for a geo-restricted app it is the strongest single artifact: it shows the app working in Taipei without the reviewer reproducing anything. The Gist still points at a personal test clip (`youtube.com/shorts/PG4CUrdkb6k`, checked today).

**It is now belt-and-braces rather than load-bearing** — routes 1–3 stand on their own — but it is owed anyway and it removes the last "I could not get it to work" risk.

---

# What changed as a result

**The App Review Notes were rewritten** (§3.4 of [[app-store-connect]]) to lead with the map and the address search. The 09-18 version led with the All tab — correct, but it demonstrated a list when the product is a map. The simulator and Xcode instructions are gone entirely: a reviewer has neither.

The notes now open with an explicit coverage statement, then give the map route, then the list route.

# What I considered and did not propose

**A "Preview Taipei" button on the outside-coverage screen** — tap it and the map jumps to Taipei with live pins. It was the obvious build before checking the code, and it is **unnecessary**: the address search already does exactly this, for reviewers and for real users alike, and has since long before the coverage screen existed.

Worth revisiting only as a *discoverability* change — a visitor planning a trip might not think to search an address — but that is a product decision about real users, not a review problem. **Not proposed now**; nothing about review requires it.

## Related
[[app-store-connect#34-beta-app-review-information--paste-ready]] · [[sessions/2026-09-18/01-reviewer-in-california|01 — the All tab finding]] · [[release-strategy#the-one-risk-i-would-bet-money-on]] · [[00-state-of-play]]
