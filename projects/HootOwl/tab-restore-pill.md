# The floating tab-restore pill — a defect and an open decision

> [!success] ✅ **Decided and done — 2026-10-05, `7afc3fa`.** Jim: *"stop mirroring the tab entirely."* The pill now carries **one fixed symbol, `chevron.up`**, and `systemImageName` — the table it mirrored — is deleted. All four configurations build; verified running on a clean install.

Found 2026-10-01 when Jim looked at the map with the tab bar hidden. Kept as a page because the reasoning outlived the fix: it is a worked example of **a derived value that drifted twice and should never have been derived.**

---

## What the pill is

`AppTabView` **auto-hides the tab bar after 5 seconds** (`autoHideDelay`), so most of the time a user is actually looking at the app there is no tab bar. A **floating pill** then appears to bring it back:

| | |
|---|---|
| **Where** | bottom-**right** — `padding(.bottom, 20)`, `padding(.trailing, 16)` |
| **What** | 46 pt dark circle, white glyph, `AppTabView.swift:80` |
| **Glyph** | `selection.systemImageName` — *the current tab's own icon* |
| **Tap** | restores the tab bar |

On the map, the overlay buttons sit opposite it:

| | |
|---|---|
| **Where** | bottom-**left** — `alignment: .bottomLeading`, `padding(.leading, 20)` |
| **What** | 52 pt dark circles, `NbsScreen.swift:558` |
| **Which** | `location.circle.fill` (blue) to re-centre on the user · `magnifyingglass` (**green** where we have data, **grey** where we do not) to search here |

So with the tab bar hidden, the map has **three dark circles along the bottom edge** — two on the left, one on the right — and only the left pair are about the map.

## Jim's report

> *"the tab button on the mapView, when collapsed, is usually 'magnify glass/search', like the 'search' button on the left, so it become button left green search button, button right, white search button, clearly a defect that need to be addressed"*

## What is actually wrong

The pill's own comment states its contract:

```swift
/// SF Symbol name matching each tab's label icon — used by the floating restore pill.
var systemImageName: String
```

**It does not match. Audited across all five shipping tabs:**

| Tab | Tab bar icon | Floating pill icon | |
|---|---|---|---|
| **Map** (`NearBySearch`) | `location.fill` | **`tortoise`** | ❌ |
| Cyclops | `eye` | `eye` | ✅ |
| All (`mncplAll`) | `tree.fill` | `tree.fill` | ✅ |
| **Subscribe** (`entitle`) | `checkmark.seal.fill` | **`cart.fill`** | ❌ |
| Onboard | `play.house` | `play.house` | ✅ |

### The map: a tortoise

`tortoise` is a leftover from **`nbsCook0`**, a screen that no longer exists — the commented-out `Label("nbsCook0", systemImage:"tortoise")` is still visible right above the live label in `AppScreen.swift`. So the pill shows a white animal glyph with nothing to connect it to "bring the tab bar back".

> **Why Jim read it as a second search button** is worth noting: it is the same size, same dark circle, same visual family as the magnifier on the left. **The glyph barely matters — the *form* says "another one of those".** That is the real defect, and it would survive a glyph swap.

### Subscribe: a cart, against a decision already taken

On **2026-09-08** Jim chose **`creditcard.circle`** — *"a card rather than a cart: this is a recurring charge, not a shop with items in it."* That decision reached `SubscribeAffordance.icon` and the tab label. **It never reached this table.** → [[decisions]]

## Why the obvious fix is not obviously right

Setting the map's pill to `location.fill` — matching its tab, honouring the stated contract — puts it **directly opposite the overlay's blue `location.circle.fill`**.

**Two location glyphs, one on each side of the screen, doing different things:** one restores the tab bar, one re-centres the map. That is a worse confusion than the tortoise, because both now *look* like they belong to the map.

## The options

### 1. ⭐ Stop mirroring — one fixed glyph ✅ **CHOSEN**

The pill's job never changes: **bring the tab bar back.** A single glyph that says that — a chevron, or a grid — says it better than any tab icon can.

- Removes **both** mismatches permanently
- **Deletes a lookup table that has already drifted twice** and will drift again every time a tab changes
- No collision with the map's own buttons, now or later
- Costs: the pill stops hinting which tab you are on — which the tab bar itself tells you the moment it returns

### 2. Fix the two stale entries

Map → `location.fill`, Subscribe → `creditcard.circle`. Honours the stated contract and the 09-08 decision.

- Costs: the map collision above, and the table stays a thing to keep in sync

### 3. Fix the mapping *and* move the overlay

Correct both entries, then shift the re-centre/search pair so they are not level with the pill.

- Removes the collision rather than tolerating it
- Costs: most work, and the sync burden remains

## What shipped

```swift
/// One fixed symbol, never the current tab's.
fileprivate static let restoreGlyph = "chevron.up"
```

**`chevron.up` because that is literally what tapping it does** — the tab bar comes back up from the bottom. It shares nothing with the map's own circles, which is the half of Jim's report a glyph swap would not have fixed.

`systemImageName` is gone, with a comment left where it stood. **A lookup table that drifts twice will drift again**, and this one had exactly one reader.

> [!note] The general lesson, worth more than the icon
> The table existed to keep two things in sync that **did not need to be in sync at all**. The pill's job never changes, so neither should its icon — deriving it from the tab created an obligation to maintain, and the obligation was not met twice over.
>
> **Before deriving one value from another, ask whether it actually tracks it.** Here it only looked like it did.

## Also answered in the same pass

**"Enable Location" on onboarding screen 3 is a real `Button`**, not an image that looks like one — `Button(action: enableLocation)` with `.borderedProminent`. It also **retargets itself to "Open Settings"** when permission is already blocked, and "Not now" beside it is a real button too.

## Related
[[decisions]] · [[sessions/2026-10-05/00-state-of-play|today's state of play]] · `AppTabView.swift:80` · `AppScreen.swift` → `systemImageName` · `NbsScreen.swift:558`
