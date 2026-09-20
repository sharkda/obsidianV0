# Service-area awareness — Jim's spec, compiled

**Jim's input after testing `destination-mode`, 2026-09-20.** Organised into requirements, with the geometry checked and two judgement calls flagged.

---

## The bug he found first

> *"though we show that prompt say 'Showing Taipei — you are not there', the map still centering on Cupertino."*

**Confirmed, and the cause is one of my own changes.** `NbsScreen` moves the camera only when `nbs.searchMode != .mapTap` (`:124`) — a rule that exists so an explicit map tap does not yank the camera. Choosing a destination now sets `.mapTap`, so the map correctly searched Taipei and **deliberately refused to look at it.**

So the bar told the truth about a map that was showing somewhere else entirely. Worse than either alone.

---

## The requirements

### R1 — Choosing a destination moves the map there
Non-negotiable; it is the bug above.

### R2 — "Search here" becomes context-sensitive, and never lies
The magnifying-glass button searches at the map centre.

- **Target inside the service area** → green. Normal behaviour.
- **Target outside** → grey, **but still tappable**, and tapping says: *"We haven't collected live parking information for this area yet."*

> [!note] Jim changed his own mind mid-spec, and the second answer is better
> He first said *"should be disabled"*, then: *"maybe we do not disable, we only prompt… so that users will not be confused by the button."* **A disabled button explains nothing** — the user is left guessing whether the app is broken, or they did something wrong. A grey-but-live button that answers when pressed teaches them the rule. Taking the second reading.

**This rule is universal, not an out-of-Taiwan special case.** Someone standing in Taipei who pans to Kaohsiung gets the same grey button and the same message. That is the point — the app has no data there either way, and where the user's body is does not change that.

### R3 — "Centre on me" is disabled when the user is outside the service area
> *"there is no point to center back to his position if he cannot find any near-by parking info."*

Agreed, and this one **is** a genuine disable rather than a prompt: the action has no useful outcome at all, whereas "search here" at least explains the area.

### R4 — A Jump button, in the bar, always to Taipei centre
> *"to make things simple, we always jump to Taipei, Center of Taipei, e.g. Taipei Train Station… this button should be in the extended area of the current 'Showing Taipei' Prompt."*

So the bar becomes: **Showing 台北市 — you're not there · Jump · Clear**

**Taipei Main Station, 25.0478 / 121.5170.** One destination, no picking, and the user pans from there — including into New Taipei, which surrounds it.

### R5 — The active area is the New Taipei fence, plus 1 km
> *"New Taipei City zone surround the Taipei City. so if target is outside the new Taipei city, it is outside the current active area."*
>
> *"unless we are very near the border of the active zone, like no more than 1KM away from it."*

---

## The geometry, checked rather than assumed

**Jim's claim holds exactly.** Testing every Taipei fence vertex against the New Taipei fence:

> **13 of 13 Taipei vertices fall inside the New Taipei fence.**

So New Taipei is the outer boundary and a single test against it answers "is this in the active area". Confirmed against real places:

| Place | in Taipei fence | in New Taipei fence | verdict |
|---|---|---|---|
| Taipei 101 | ✅ | ✅ | covered |
| Taipei Main Station | ✅ | ✅ | covered |
| Banqiao | ❌ | ✅ | covered |
| Tamsui | ❌ | ✅ | covered |
| **Keelung** | ❌ | **✅** | **covered — and it should not be** |
| Taoyuan | ❌ | ❌ | outside |
| Kaohsiung | ❌ | ❌ | outside |
| Cupertino | ❌ | ❌ | outside |

> [!warning] Keelung is a false positive, and it is the fence's fault
> These fences are **convex hulls of each city's car parks**, so the New Taipei hull bulges out over Keelung — a different city with no data in this app. Under R5, Keelung gets a **green** button and a promise of parking we do not have.
>
> **Shipping it anyway**, because it is one adjacent city, the failure is soft (a search returns nothing rather than something wrong), and the alternative is a real-polygon boundary we do not have data for.
>
> **The better long-term rule is data-driven, not geometric:** ask the quadtree whether any lot exists within the search radius. That answers Keelung, Taoyuan and every future gap correctly and automatically, with no fence maintenance. Worth doing when the third city lands — recorded as a follow-up rather than built now, because Jim specified the fence rule and it is right for the two cities we have.

---

## What gets built

| | Change |
|---|---|
| `Municipal` | `isInServiceArea(_:tolerance:)` — inside any fence, or within 1 km of one. Point-to-**segment** distance, not vertex distance, or a long edge would report a false "far". |
| `Municipal` | `taipeiCentre` — Taipei Main Station, the single jump target |
| `NbsScreen` | camera follows a destination choice (**R1**) |
| `DestinationBar` | gains **Jump** (**R4**) |
| Search-here button | green / grey by service area, always tappable, explains itself (**R2**) |
| Centre-on-me button | hidden when the user is outside the service area (**R3**) |
| Strings | jump, and the "no data here yet" message, en + 中文 |

## Related
[[destination-mode]] · [[sessions/2026-09-20/02-destination-mode-design|02 — the original design]] · [[00-state-of-play]]
