# Destination mode — built, and how to undo it

**Branch `destination-mode`, 2026-09-20.** **Six** commits on top of `main` at `5d4d794` — four from the first build, two more after Jim's first test. **Not merged.** Jim: *"I am not so sure about this UI change and experiences, but I can't make decision before I see how it goes, so make sure all these changes are well documented and better reversable."*

---

## What it does

Outside Taipei and New Taipei, the app used to refuse — the map, the watch list and the list all showed a dead end. Now it asks **"Where are you heading?"** and offers a button per covered city. Tap one and **the app works**: live counts, pins, distances, everything, measured from there.

A slim capsule stays on the map the whole time: **"Showing 台北市 — you're not there · Clear"**.

## Why it was smaller than it looked

**The app was never location-bound. The refusal was.** Whole cities download regardless of position, the All tab never filtered by location, the watch list contains **no location code at all**, and `search(mapMode: .mapTap, loc0:)` has always searched around an arbitrary point.

Exactly **three** sites tied everything to the GPS fix, and all three now read `effectiveCentre`:

| Site | Was | Now |
|---|---|---|
| `Municipal+Coverage.swift:88` | coverage from `userLoc2dVbj` | `effectiveCentre` |
| `Municipal.swift:239` | active fences from `userLoc2dVbj` | `effectiveCentre` |
| `NbsObsM+Ext.swift:27` | search trigger from `userLoc2dVbj` | `effectiveCentre` |

```swift
var effectiveCentre: CLLocationCoordinate2D? {
    destination?.coord ?? userLoc2dVbj.value
}
```

> [!important] `userLoc2dVbj` is never overwritten, and must not be
> It is persisted to disk by `Municipal+Cache` as the user's last known position, it is what "distance from me" means, and it is the input to anything that genuinely needs the device. Writing a destination into it would corrupt the cache and quietly lie to every consumer. **That separation is the entire reason `effectiveCentre` exists rather than an override.**

## Reversibility

**The safest property is structural, not procedural: with no destination set, `effectiveCentre` *is* `userLoc2dVbj.value`.** The old path is the default path, by construction — not by a flag someone has to remember to check.

**Four commits, each independently revertable, newest first:**

| Commit | Revert gives you |
|---|---|
| `248137a` — *Searching an address is choosing a destination* | Address search stops setting a destination; search-mode labelling reverts. The feature still works via the city buttons. |
| `6ca0433` — *Offer somewhere to go* | The picker and the bar disappear; the old dead-end card returns. The model stays, inert — nothing can set a destination from the UI. |
| `3080ba1` — *Let the app be about a place the user is not standing in* | The whole concept goes. Requires reverting `6ca0433` first. |
| `52ec2f3` — *Default the simulator to Cupertino* | Scheme goes back to `Wanli34.gpx`. Independent of the rest. |
| `6655f7c` — *Know where we actually have parking data* | `isInServiceArea` / `distanceToEdge` / `taipeiCentre` go. Revert `6faa289` first — the UI reads them. |
| `6faa289` — *Make the map say what it can and cannot do* | The camera stops following a destination (**the bug returns**), Jump goes, and both overlay buttons revert to always-on and always-coloured. |

**To drop all of it:** `git checkout main` — the branch was never merged.

**To keep the concept and drop the UI:** revert `6ca0433` and `248137a`. `effectiveCentre` remains and does nothing, because nothing sets a destination.

## Round 2 — after Jim's first test (2026-09-20)

He found one bug and specified four changes. Compiled spec and the geometry check: [[sessions/2026-09-20/03-service-area-context|03]].

**The bug:** the bar said *"Showing 台北市 — you're not there"* over a map **still centred on Cupertino**. Choosing a destination searched Taipei correctly and then deliberately refused to look at it — `NbsScreen` only moves the camera when the search mode is not `.mapTap`, a rule that exists so an explicit map tap does not yank the view, and that destination mode had quietly inherited. **Fixed:** a destination is an explicit request to *go* somewhere.

**The four changes:**

| | |
|---|---|
| **Service area** | Inside any fence, or within **1 km** of one. One test against the New Taipei fence answers it — **13 of 13 Taipei vertices fall inside it**, checked, because New Taipei geographically surrounds Taipei |
| **"Search here"** | **Green** where we have data, **grey** where we do not — **still tappable**, answering *"we haven't collected live parking information for this area yet"* |
| **"Centre on me"** | **Hidden** when the device is outside the service area — a genuine removal, because the action has no useful outcome to explain |
| **Jump** | In the bar, re-centres on the destination. Always **Taipei Main Station** as the single target |

> [!note] Jim corrected himself mid-spec, and the correction was right
> He first said "search here" should be **disabled** outside the area, then: *"maybe we do not disable, we only prompt… so that users will not be confused by the button."* **A disabled button explains nothing.** Grey-but-live teaches the rule. The distinction against "centre on me" is real: that one has no outcome at all, so there is nothing to say.

**The rule is universal, not an out-of-Taiwan case.** Someone standing in Taipei who pans to Kaohsiung gets the same grey button and the same message — the app has no data there either way, and where the user's body is does not change that.

## Verified

Three cases, on the iPhone 17 Pro / iOS 26.5 simulator:

| Case | Coverage states | Search mode | Result |
|---|---|---|---|
| **In zone, no destination** — the regression case | `locating → waiting → covered` | `.userLocation` | unchanged from before |
| **Out of zone, no destination** — what a reviewer meets | `covered → outside` | `.userLocation`, centred on Cupertino | the picker renders |
| **Out of zone + Taipei destination** | `locating → covered` | `.mapTap`, centred on 25.034/121.564 | **9 lots, 93 m–1874 m, availability merged** |
| **Round 2 — destination restored** | `locating → covered` | `.mapTap` at 25.048/121.517 | **`📍 destination → camera` fires**, then 9 lots — the camera bug is fixed |

**The service-area maths was checked against real places**, not just compiled: Taipei Main Station and Banqiao inside; **Taoyuan 2,952 m** from the nearest edge, so correctly outside the 1 km tolerance; Kaohsiung and Cupertino far outside. **Keelung tests inside** — the known false positive.

All four configurations build: iOS Debug/Release, hootmac Debug/Release.

> [!warning] What is NOT verified — and it is the part Jim wanted to judge
> **Nobody has tapped any of it.** This Xcode ships no `Simulator.app`, so the picker buttons, the bar, and the Clear button have never been pressed. The model path was proven by seeding a destination into the app's preferences and relaunching — which exercises restore → `effectiveCentre` → coverage → search, but **not one pixel of the UI**.
>
> **That is exactly what Jim asked to judge**, so it is his run, not a gap to paper over.

## What to look at when testing

The scheme now launches in **Cupertino**, so the picker is what you get on Run. To go back in-zone: **scheme → Run → Options → Default Location → `Wanli34.gpx`**.

0. **The four round-2 changes have never been tapped either** — button colours, the alert, Jump, and the hidden centre-on-me button. The camera fix *was* verified from the log.
1. **Does the picker read as an offer or as an error?** It still sits inside `ContentUnavailableView`, which is Apple's "nothing here" furniture. That may be exactly the wrong frame for a screen whose message is *"here is where to go"*.
2. **Is the bar reassuring or nagging?** It never goes away while a destination is set.
3. **The watch list and the All tab** now work out of zone — check they do not feel orphaned without the map's context.
4. **Clear** — does returning to "nothing here" feel like losing something?
5. **In Taipei, with the scheme switched back** — confirm nothing changed at all.

## Known rough edges

- **The Chinese is `needs_review`.** Six new strings, written by me rather than through Jim's pass. → [[zh-review]]
- **`convexEnclosing` is still integer-truncated** (**E-12**). `Municipal.swift:239` uses it, so a destination near a fence edge could resolve wrongly. Inert for city-centre destinations; a real risk for an address search near a boundary. **`isInServiceArea` uses it too**, so the same truncation affects the button colours near a boundary — the 1 km tolerance masks it in practice.
- **Keelung reads as covered and is not.** The New Taipei hull bulges over it. Soft failure — a search finds nothing rather than something wrong. **Jim's read: that makes Keelung the obvious next zone.** The durable fix is to ask the quadtree whether any lot exists within the radius, which answers every gap automatically.
- **The picker appears on three screens** — map, watch list, list — because they all share `CoverageNoticeView`. On the map it is compact; on the other two it is the full `ContentUnavailableView`. Consistent, but possibly repetitive.
- **No 'recent destinations'.** `nbs_recent_addresses` already persists searched addresses; the picker does not offer them.

## Related
[[sessions/2026-09-20/01-outside-taiwan-experience|01 — the experience that prompted this]] · [[sessions/2026-09-20/02-destination-mode-design|02 — the design, before building]] · [[bugs]] · [[decisions]]
