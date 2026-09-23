# Destination mode — built, and how to undo it

**Merged to `main` 2026-09-23 — it ships in build 1.** Twelve commits, fast-forward, `main` = `42ed13b`.

> [!success] Jim's call, 2026-09-23
> *"i want destination mode in build 1, we need to let our potentional users test the app before they are in the zone."*
>
> The reasoning is the product one, not the review one: **someone planning a trip to Taipei should be able to decide the app will work for them before they arrive.** A reviewer in California benefiting too is a side effect.
>
> **Verified on merged `main`:** all four configurations build, and a clean first install out of zone reaches `coverage locating → outside` with the picker, `👁 cyclops rebuilt: 3 of 3 watched` (the three landmark defaults seeding properly, which Jim's old test pin had been hiding) and 3,161 lots loaded. Jim: *"I am not so sure about this UI change and experiences, but I can't make decision before I see how it goes, so make sure all these changes are well documented and better reversable."*

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

> [!note] Now merged — reverting means reverting on `main`
> The table below still holds commit by commit, but `git checkout main` is no longer the escape hatch. The branch ref `destination-mode` still points at the same tip, so `git revert 5d4d794..42ed13b` or a reset to `5d4d794` is the way back if it ever comes to that.

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

He found one bug and specified four changes. Compiled spec and the geometry check: [[sessions/older/2026-09-20/03-service-area-context|03]].

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

## Round 3 — the map's zoom, and what Clear is for

### The sweet spot

**Jump used `savedSpanDelta`** — the `@AppStorage` value updated on *every* camera change. So it inherited whatever zoom the user last left the map at: pan around Cupertino zoomed out, and you arrive in Taipei equally zoomed out. **That is why arriving did not feel like arriving.**

The numbers, at Taipei's latitude:

| Span | On the ground | |
|---|---|---|
| 0.0005 | ≈ 55 m | pinch-in clamp (`nbs_min_span`) |
| 0.008 | ≈ 0.9 km | |
| **0.012** | **≈ 1.3 km × 1.2 km** | **the sweet spot — chosen** |
| 0.015 | ≈ 1.7 km × 1.5 km | the old `savedSpanDelta` default |
| 0.050 | ≈ 5.6 km × 5.0 km | the initial camera, before any saved value |
| 0.300 | ≈ 33 km | pinch-out clamp (`nbs_max_span`) |

**Every programmatic camera move now lands at 0.012** — six call sites. Close enough to read individual car parks and the streets between them, wide enough to hold the near cluster; the nine nearest lots to Taipei Main Station spanned 93 m–1,874 m.

### Unless the user has chosen their own

> Jim: *"there should be a sweet spot for the span factor, and we should always stick to it unless users have changed their span factor."*

That needs a way to tell **a deliberate pinch** from **a span we just set ourselves** — and `savedSpanDelta` cannot, because it records both. `suppressPannedAway` already marks our own moves, so a change outside that window is the user's. A new `nbs_user_set_span` flag latches on the first real pinch, and from then on their zoom is theirs and arrivals stop overriding it.

> [!note] MapKit will not give you exactly what you ask for
> Requesting 0.012 rendered as `spanDelta:0.013 lat:0.015 lon:0.012`. MapKit holds one axis and fits the other to the view's aspect ratio. **Expect the logged number to differ from the requested one** — it is not a bug, and chasing it would be.

### What Clear is for, and where it is not

Clear sets the destination to `nil` — "go back to following my device".

- **In Taipei**, after searching an address across town: returns you to *near me*. Useful.
- **In California**: returns you to **the dead-end picker**. It undoes the only thing that made the app work.

**Hidden when the user's own location is outside the service area**, which is the same rule as the centre-on-me button — and Jim's call: *"clear doesn't make sense when users is outside the active zone."* No location fix at all also counts as hidden: there is nowhere to go back to.

**Jump is now prominent** rather than plain footnote text identical to Clear, which gave the primary action no more weight than the one that undoes it.

## Round 4 — visibility rules, auto-search, and a bug of my own

### Two questions that were being answered by one flag

| | Governed by | Rule |
|---|---|---|
| **The bar** | **where the user is** | visible whenever their own location is outside the active zone |
| **Jump** | **what the user is looking at** | visible only when the map centre has no data — so it vanishes once you have arrived, and returns if you pan off into nowhere |

Jump is hidden entirely for someone inside the active zone: they have *centre on me* for the same job and do not need a second way home.

### The map now searches itself

There was **no such rule before** — panning set `pannedAway` and left the user to find the magnifying glass. **A button you have to discover is one most people never press.**

**1.2 s after settling, at least 300 m from the last search.** Jim proposed 5 s; I argued against it and he took 1.2 — by five seconds the user has concluded nothing will happen and either pressed the button or moved on, which is the problem this solves.

> [!note] The cost objection does not apply here
> `search()` is **entirely local** — phase 1 renders from cached `parkInfoVbj`, phase 2 is `quadTree.findNearest`. **No network call.** Doing it for the user costs a tree walk, not a request. That is what made auto-search an easy yes.

Silent outside the service area, where it would find nothing and quietly contradict the grey button. A programmatic arrival records its own centre, so the timer does not fire on the point we just searched.

### The zoom, and the bug underneath it

**0.012 → 0.004** (≈445 m across, a four-minute walk) after Jim saw it and said *"still too busy"*.

But the reason it looked too busy was **not** the default.

> [!danger] "Has the user chosen their own zoom?" was wrong twice, and the second failure is the instructive one
> **Attempt 1 — timing.** Any camera change outside an 0.8 s suppression window counted as a pinch. **MapKit keeps emitting camera changes after an animation settles**, so our own moves latched the flag.
>
> **Jim caught it by asking the right question** — *"can you read what is the current saved span factor on the simulator? I am not sure that our saved preference will be mistaken by our default value?"* Stored on his device: flag `true`, span **0.028 (≈3.2 km)**. **The sweet spot had never once been applied.** "Too busy" was a stale preference, not the default.
>
> **Attempt 2 — compare rendered against requested.** Also wrong. **MapKit snaps to its own zoom levels, by an amount that grows as you zoom in:** 8% off at 0.012, **50% off at 0.004**. No threshold is safe.
>
> **The fix: stop inferring.** A `MagnifyGesture` on the map answers the only question that matters — did the user's fingers do this — and infers nothing. The `@AppStorage` key is renamed `_v2` to discard what the broken versions latched.

**Verified with every preference cleared:** the map lands at `spanDelta:0.004` and the flag stays unset.

> [!tip] How to check this yourself, on any simulator
> ```sh
> C=$(xcrun simctl get_app_container <UDID> com.sharkda.hootowl data)
> plutil -p "$C/Library/Preferences/com.sharkda.hootowl.plist" | grep -E "nbs_"
> ```
> If `nbs_user_set_span_v2` is true, **you are looking at a saved preference and not the default** — which is the trap that cost this round.

## Round 5 — losing your place, and a preference read as a bug

### The real one: the map forgot where you were

Jump to Taipei → watch list → back to the map → **Cupertino**, with the bar still saying *"Showing 台北市"*.

`cameraPosition` is `@State`, and switching tabs destroys the view. **Exactly the pattern this vault already warns about** — `AppTabView`'s dynamic `ForEach` inside `TabView` loses child identity routinely, which is what [[working-agreements#prefer-singleton-state-for-state-bearing-screens]] is about.

**The destination itself survived** — it lives on `Municipal` and is persisted. Only the camera forgot. Restored on appear, so the context now holds for the whole session.

### The other was not a bug — and it is the second time today

> *"when I jump to Taipei and go to the cyclops, there are no 'pre-defined' watch list"*

Instrumented rather than guessed:

```
👁 cyclops rebuilt: 1 of 1 watched · 3160 lots · 2584 avails
```

**The model was correct.** The simulator held `mncpl_watchList_data = ['TPE0155']` — Jim's own test pin from earlier. The three landmark defaults **seed only when nothing is stored**, deliberately, so a user who unpins everything does not get them resurrected under them.

> [!warning] Twice in one session, a stored preference was read as a broken default
> First the span (`nbs_user_set_span` true, `0.028` saved, so the sweet spot never applied). Then the watch list. **Both times the app was behaving correctly and the device was carrying test residue.**
>
> **When something looks wrong on a simulator that has been tested on for days, read the preferences before reading the code:**
> ```sh
> C=$(xcrun simctl get_app_container <UDID> com.sharkda.hootowl data)
> plutil -p "$C/Library/Preferences/com.sharkda.hootowl.plist" | grep -E "nbs_|mncpl_"
> ```
> `refreshCyclops` now logs what it built at `.notice`, because "the watch screen is empty" has three causes indistinguishable from the UI — an empty list, watched ids missing from the loaded lots, and the `@Observable` invalidation failure that file already documents.

### A real pinch verified the pinch detection

Jim noodled the UI mid-session and asked whether it had interfered. It had not — it **proved the fix**. Afterwards the simulator held `nbs_user_set_span_v2: true` with span `0.0025`, i.e. **the flag latched from a human pinch**, which is precisely what two rounds of inference failed to do and what I could not test without hands on the device.

## Round 6 — the tab-return fix that did not fix it

Jim, after a clean first run: *"select to jump to Taipei City, then Tab away to other and tab back to MapView, back in Cupertino again."*

**The round-5 restore was running and losing.** It fired, then something dragged the camera back a beat later.

**Four separate places snapped straight to `userLoc2dVbj`** — the iOS auth sink, the macOS auth sink, the location sink, and an explicit "snap if already known". **Every one of them ran on every tab return**, because:

> `wire0` re-subscribes each time the view appears, and **`locAuthStateVbj` and `userLoc2dVbj` are `CurrentValueSubject`s** — subscribing *replays the current value*. So the sinks fire instantly with "authorized" and "here is your fix", which is Cupertino.

That is the part worth remembering: **a `CurrentValueSubject` sink is not only a change notification — it is also an immediate callback with whatever is already there.** Re-subscribing on appear turns it into "do this again, now".

**Fixed with one guard, not four patches.** All four route through `snapCameraToDevice(_:animated:)`, which stands down when a destination is set. Patching them individually would have left the next "snap to me" line free to reintroduce the bug; the helper is the thing that holds.

**Verified** with a destination set and the device in Cupertino:

```
📍 returning to 台北市 — camera was reset by the tab switch
📍 ignoring device-location snap — showing 台北市      ×4
```

Also removed a log that lied: the location sink announced *"centering on \<device\>"* before the guard refused the move, so the console claimed the camera had gone somewhere it had not.

## Round 7 — one button

The picker offered **台北市** and **新北市**, one per loaded fence. Jim: *"the two city are too close and one is surrounded by the other, there is no point to provide two buttons now."*

Right, and worse than redundant: it asked the user to make a decision **on the screen where they know least about the app**, between two options that differ by a second of panning.

**Now one button — "Go to Taipei" / 「前往台北市」** — dropping at Taipei Main Station.

**`destinationChoices` no longer derives from the fences.** Fences are a **data** boundary; this is a **destination offer**. The two stop agreeing the moment one metro is served by several fences, which is already true here. New metros get added by hand — **Keelung** is the named next zone and is far enough out to earn its own button; another Taipei-adjacent district would not be.

The label reads as an action rather than a place name: with two options there was a list to scan, with one there is only a thing to press.

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

0. **The round-3 zoom** — does 0.012 (≈1.3 km) feel right on arrival? It is one constant, `NbsScreen.sweetSpotSpan`. Pinch once and the app should stop overriding you from then on.
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
[[sessions/older/2026-09-20/01-outside-taiwan-experience|01 — the experience that prompted this]] · [[sessions/older/2026-09-20/02-destination-mode-design|02 — the design, before building]] · [[bugs]] · [[decisions]]
