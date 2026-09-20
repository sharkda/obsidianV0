# Destination mode — what it would take

**Jim's call, 2026-09-20**, rejecting the "Look around Taipei" button as too small:

> *"we want someone who plan to come to Taipei can decide that this will work for them… we do have a search or pin destination, which does not depend upon users current location. 1. tell the users you are not inside the current active zone now. but all the function will work, based on the target destination function, which then we will jump to that function."*

**The answer, after reading the code: this is much closer to already working than it looks.** The app is almost entirely location-independent already. Three lines bind it to "you must be standing in Taipei."

---

## What actually ties the app to the user's GPS fix

Every consumer of `userLoc2dVbj`, audited:

| Where | What it does | Needs changing? |
|---|---|---|
| `Municipal+Coverage.swift:88` | `coverage` is computed **only** from the GPS fix | ✅ **yes** — this drives all three notices |
| `Municipal.swift:239` | `activeFencesVbj` — which fences enclose the user | ✅ **yes** |
| `NbsObsM+Ext.swift:27, 33` | the map auto-searches around the fix | ✅ **yes** |
| `Municipal+Loc.swift:64` | writes the fix when CoreLocation delivers | ❌ no — this is the source |
| `Municipal+Cache.swift:68,78,107` | persists / restores last known position | ❌ **must not change** — see the warning below |
| `Municipal+Fence.swift:19` | logs the fix when fences load | ❌ no |

**Three sites.** That is the whole coupling.

### Everything else already works anywhere on earth

- **The All tab** does no location filtering whatsoever. 3,162 lots, live counts, from anywhere.
- **The watch list (Cyclops) contains *zero* location references.** The only one is the coverage gate we added on 09-15 — and it fires **only when the pin list is empty** (`MncplCyclopsScreen.swift:116`). **A user with pins already has a fully working watch screen in California today.**
- **The data is always there.** Whole cities are downloaded regardless of position, and `ActDeActOnes` has no callers, so every proto polls for every user. Nothing needs "activating" for a destination.
- **Searching around an arbitrary point already ships.** `search(mapMode: .mapTap, loc0:)` has no reference to the user's location; the address bar and map taps both use it.
- **Destinations already persist** — `@AppStorage("nbs_recent_addresses")`.

> [!important] The app was never really location-bound. We made it look that way.
> The 09-15 empty state was built to stop a reviewer seeing a blank map. It did that — and in doing so it taught the app to *refuse* rather than to *redirect*. Jim's instinct is right: the fix is not a button on the refusal, it is removing the refusal.

---

## The design

### One new concept: the **effective centre**

```swift
// Municipal
var destinationVbj = CurrentValueSubject<Destination?, Never>(nil)   // user-chosen, persisted

/// Where the app is *about* right now. The destination when one is set, otherwise the GPS fix.
var effectiveCentre: CLLocationCoordinate2D? {
    destinationVbj.value?.coord ?? userLoc2dVbj.value
}
```

Then route exactly those three sites through `effectiveCentre` instead of `userLoc2dVbj`.

**What falls out for free:**

- Set a Taipei destination → `coverage` computes `.covered` **legitimately**, and all three notices disappear on their own. No screen needs to know about destinations.
- `activeFences` resolves to Taipei → anything fence-driven behaves as if you were there.
- The map searches around the destination; distances are measured from it, which is what someone planning a trip wants.

> [!danger] Do **not** implement this by writing the destination into `userLoc2dVbj`
> It is the obvious shortcut and it is wrong. That subject is persisted to disk by `Municipal+Cache` as the user's last known position, it is what "distance from me" means, and it is the input to any future feature that needs the real device location. Faking it would corrupt the cache and silently lie to everything downstream. **The two must stay separate** — that is the entire reason for a second concept rather than an override.

### The honesty requirement — Jim's point 1

> *"tell the users you are not inside the current active zone now"*

A **slim persistent bar**, shown whenever `destination != nil && destination is not where the user is`:

> 📍 Showing **台北市** — you're not there · **Change** · **Clear**

Non-blocking, always visible, never a card in the way. The user is never confused about whose location the numbers describe, and one tap gets out.

### The entry point — Jim's "jump to that function"

When outside coverage **and no destination set**, the current dead-end card becomes a **destination picker**:

> **You're not in a covered area yet**
> Where are you heading?
> [ 台北市 Taipei ] [ 新北市 New Taipei ]
> 🔍 *or search an address…*
> — *Not your city? **Request it** →*

Two taps from install to a fully working app. The address search already exists; the two city buttons are shortcuts to their fence centroids.

---

## What it would take

| # | Work | Size |
|---|---|---|
| 1 | `Destination` model + `@AppStorage` persistence | S |
| 2 | `effectiveCentre` on `Municipal`; route the three call sites | S — but touches load-bearing coverage logic |
| 3 | `NbsObsM` sinks on destination-or-location instead of location | S, needs care with `searchIfMovedEnough` |
| 4 | Coverage card → destination picker | **M** — the real UI work |
| 5 | The "you're not there" bar | S |
| 6 | Strings, en + 中文 | S |

**Call it a focused day, most of it in #4.**

### Risks, honestly

- **`coverage` is read by three screens.** Changing its input changes behaviour for in-zone users too. The in-zone path must be verified as carefully as the new one — with no destination set, `effectiveCentre` is the GPS fix and nothing should change at all.
- **`convexEnclosing` is integer-truncated and wrong** (**E-12**, known, inert today). `Municipal.swift:239` uses it, so routing a destination through it *exercises a latent bug*. Worth fixing first or at least measuring — a destination landing just outside a fence because of integer truncation would be a confusing failure.
- **Distance semantics change** when a destination is set: "nearest" means nearest to the destination. That is correct and desired, but the sorted list and any "X m away" label now mean something different. The bar above is what keeps that honest.

---

## Does it solve the reviewer problem?

**Yes, and structurally rather than by instruction.**

A reviewer in California opens the app and is asked *"where are you heading?"* with **台北市** as a one-tap answer. Two taps in, they are looking at a working live parking map. No notes to read, no address to type, nothing to know in advance.

**The App Review notes stop being load-bearing** — they become a second path for a reviewer who does something unexpected, which is what notes should be.

---

## The scheme now defaults to California

Jim: *"we can review our schema so the emulator is set in CA."* Done — `Cupertino.gpx` added (Apple Park, deliberately outside every fence) and `hootowl.xcscheme` points at it, replacing `Wanli34.gpx`.

**So every Xcode run now starts out of zone**, which is the scenario that was least exercised and most wrong. To go back in-zone for a run: **scheme → Run → Options → Default Location → `Wanli34.gpx`** (or `sanfu77.gpx`). Both are still in the repo.

## Related
[[sessions/2026-09-20/01-outside-taiwan-experience|01 — the experience today]] · [[sessions/2026-09-19/02-reviewer-scope-and-testing|the reviewer routes]] · [[00-state-of-play]]
