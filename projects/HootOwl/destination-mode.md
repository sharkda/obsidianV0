# Destination mode — built, and how to undo it

**Branch `destination-mode`, 2026-09-20.** Four commits on top of `main` at `5d4d794`. **Not merged.** Jim: *"I am not so sure about this UI change and experiences, but I can't make decision before I see how it goes, so make sure all these changes are well documented and better reversable."*

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

**To drop all of it:** `git checkout main` — the branch was never merged.

**To keep the concept and drop the UI:** revert `6ca0433` and `248137a`. `effectiveCentre` remains and does nothing, because nothing sets a destination.

## Verified

Three cases, on the iPhone 17 Pro / iOS 26.5 simulator:

| Case | Coverage states | Search mode | Result |
|---|---|---|---|
| **In zone, no destination** — the regression case | `locating → waiting → covered` | `.userLocation` | unchanged from before |
| **Out of zone, no destination** — what a reviewer meets | `covered → outside` | `.userLocation`, centred on Cupertino | the picker renders |
| **Out of zone + Taipei destination** | `locating → covered` | `.mapTap`, centred on 25.034/121.564 | **9 lots, 93 m–1874 m, availability merged** |

All four configurations build: iOS Debug/Release, hootmac Debug/Release.

> [!warning] What is NOT verified — and it is the part Jim wanted to judge
> **Nobody has tapped any of it.** This Xcode ships no `Simulator.app`, so the picker buttons, the bar, and the Clear button have never been pressed. The model path was proven by seeding a destination into the app's preferences and relaunching — which exercises restore → `effectiveCentre` → coverage → search, but **not one pixel of the UI**.
>
> **That is exactly what Jim asked to judge**, so it is his run, not a gap to paper over.

## What to look at when testing

The scheme now launches in **Cupertino**, so the picker is what you get on Run. To go back in-zone: **scheme → Run → Options → Default Location → `Wanli34.gpx`**.

1. **Does the picker read as an offer or as an error?** It still sits inside `ContentUnavailableView`, which is Apple's "nothing here" furniture. That may be exactly the wrong frame for a screen whose message is *"here is where to go"*.
2. **Is the bar reassuring or nagging?** It never goes away while a destination is set.
3. **The watch list and the All tab** now work out of zone — check they do not feel orphaned without the map's context.
4. **Clear** — does returning to "nothing here" feel like losing something?
5. **In Taipei, with the scheme switched back** — confirm nothing changed at all.

## Known rough edges

- **The Chinese is `needs_review`.** Six new strings, written by me rather than through Jim's pass. → [[zh-review]]
- **`convexEnclosing` is still integer-truncated** (**E-12**). `Municipal.swift:239` uses it, so a destination near a fence edge could resolve wrongly. Inert for city-centre destinations; a real risk for an address search near a boundary.
- **The picker appears on three screens** — map, watch list, list — because they all share `CoverageNoticeView`. On the map it is compact; on the other two it is the full `ContentUnavailableView`. Consistent, but possibly repetitive.
- **No 'recent destinations'.** `nbs_recent_addresses` already persists searched addresses; the picker does not offer them.

## Related
[[sessions/2026-09-20/01-outside-taiwan-experience|01 — the experience that prompted this]] · [[sessions/2026-09-20/02-destination-mode-design|02 — the design, before building]] · [[bugs]] · [[decisions]]
