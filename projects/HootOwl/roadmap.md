# HootOwl — Roadmap

**Features we want but have not built.** The third list, and deliberately separate from the other two:

| This note | Not this note |
|---|---|
| **Features** — capability we would like the app to have | [[unfinished]] — engineering debt and things knowingly left half-done |
| Wanted, not owed | [[bugs]] — things that are wrong |
| Post-launch unless marked otherwise | [[Jim's backlog]] — bugs **Jim** wants to work on |
| | [[jim-actions]] — things only Jim can do, for *this* release |

**IDs are `F-`, permanent, never reused** — same convention as the state-of-play tables, so a feature can be referred to across sessions without re-describing it.

---

## F-01 — Let the user pick which map app gets the directions

**Jim, 2026-10-09:** *"I do plan to add support to google map or even other map vendor later."*

### Where it stands today

One hardcoded handoff, and it **is** reachable — worth stating, because the code around it looks dead and is not:

- `NbsObsM+Ext.swift:112` — `appleMap()` builds `http://maps.apple.com/?daddr=<lat>,<lon>&dirflg=d` and calls `UIApplication.shared.open`.
- Reached from `NbsScreen.swift:206`: `NbsMncplSheetView(nbs:initialLot:onAddress: nbs.appleMap)` — the lot sheet on the map screen.
- ⚠️ `NbsCookScreen0 copy.swift` also calls it and is **not compiled at all** (zero `pbxproj` references). Dead file on disk, not part of this feature — a candidate for the **E-16** deletion sweep.

**So the shape is unusually good.** One function, and the call site already takes the action **as a closure** (`onAddress:`), so a vendor chooser can replace `appleMap` without the sheet knowing anything changed.

### The part worth getting right

> [!tip] 🥇 Start with Google's **universal link**, not its URL scheme
> ```text
> https://www.google.com/maps/dir/?api=1&destination=<lat>,<lon>
> ```
> This opens the **Google Maps app if installed and Safari if not**, so it degrades gracefully with **no scheme, no `canOpenURL`, and no plist change**. For a first version that is the whole feature.
>
> The `comgooglemaps://?daddr=<lat>,<lon>&directionsmode=driving` scheme is only worth adding if we want to *know* whether the app is installed — and **that is where the hidden cost is**: `canOpenURL` returns `false` for an undeclared scheme no matter what the user has installed, and `LSApplicationQueriesSchemes` is **not declared anywhere in this project today** (verified 2026-10-09). So detection means a new Info.plist key, which means a new build.

**The design question to settle before writing any of it:** *ask every time, or remember?*

- **Remember — recommended.** People have one map app they like, and a chooser on every tap is a tax on the common case. One preference, changeable wherever it lives.
- **Ask every time** is only better if we expect people to genuinely alternate, which seems unlikely for commuting to a car park.
- Either way the first tap has to pick something. **Apple Maps stays the default**: it is always installed, so the fallback can never be empty.

**Other vendors (Waze, Taiwan-specific navigation apps):** each needs its scheme and parameters **checked against that vendor's current documentation before shipping** — these change, and a wrong scheme is a button that silently does nothing. Not guessed here on purpose.

> [!warning] Do not confuse this with **D-09**
> Handing a destination to another app is **not** routing. Adding map vendors never requires `MKDirectionsApplicationSupportedModes` or a routing-coverage GeoJSON. → [[app-store-connect#routing-app-coverage-file--no-and-the-field-should-stay-empty]]

**Size:** small — one function, one preference, one optional plist key. **Not release-blocking**; Apple Maps works today.

---

## F-02 — The next municipality, starting with 基隆

**Jim, 2026-09:** *"it's worth noting that Keelung should be the next zone we should cover if not yet."*

The growth path for the whole app, and the one feature that changes what the product *is* rather than how it behaves. Coverage is currently Taipei City and New Taipei City.

**What a new city touches, from what the last two taught us:**

- A feed and its quirks — New Taipei needed **pagination** to get past a WAF (`e45051c`) and has **duplicate parkIds** (E-13) and **−9 lots** mid-operator-change (D-02).
- A fence/coverage polygon, which is where **E-12** (`convexEnclosing` integer truncation) becomes load-bearing — it already decides `isInServiceArea`.
- **E-24** — `onb_s1_body` **hardcodes the city list** in both en and 中文. A third city makes onboarding understate coverage until that string changes.
- `destinationChoices` in `Municipal+Coverage.swift`, which Jim deliberately cut to **one** entry (Taipei) because two adjacent cities was a meaningless choice. A genuinely separate city is the case that earns a second entry back.
- The App Store listing, where coverage is in the **first sentence** of both descriptions, and the promotional text — the one field that changes **without a build**, which is exactly what it is for: 「全新上線：基隆市」.

**Size:** the per-city work is now mostly normalised through `Municipal`, which was the point of that framework. The unknown is always the feed.

---

## Related open questions that may become features

Not duplicated here — these live where they are and are linked so this note stays the list of *wanted things* rather than a second copy of the backlog.

| | Where |
|---|---|
| **D-01** — subscription unlocks nothing but ad removal. If subscribers were meant to get more, that gating was never built. A product question that would *generate* features. | [[jim-actions]] |
| **E-01** — nothing tells a user when a feed is down. Arguably owed rather than wanted, which is why it is 🟠 and not here. | [[jim-actions]] |
| **D-02** — label New Taipei's −9 lots rather than hide them. | [[data-sources]] |
| A second tutorial video — the config is already keyed by **where the button appears**, so `tutorials.cyclops` needs no code. | [[operations#why-tutorials-is-keyed-by-name-not-numbered]] |

## Related
[[unfinished]] · [[Jim's backlog]] · [[jim-actions]] · [[decisions]] · [[INDEX]]
