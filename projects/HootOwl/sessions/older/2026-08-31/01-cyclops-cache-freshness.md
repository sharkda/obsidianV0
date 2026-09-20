# 2026-08-31 — Cyclops cache freshness colouring

**Status:** implemented in the working tree. **Not committed, not compile-verified** (same `Package.resolved` / `ConcaveHull` blocker as #5 — build in Xcode).
**Ask (Jim):** the Cyclops number is cache-seeded so it appears instantly on relaunch — but a long-stale cached number looks exactly like a live one. Save the cache time and colour the number by age: <5 min unchanged, 5–30 min white, >30 min grey.

---

## Two findings that shaped the implementation

### 1. The saved time was already saved

The premise "can we *also* save the saved time" turned out to be already satisfied. `MncplParkAvPack` carries `converted: Date` (`ParkAvailv02.swift:15`), the struct is `Codable`, and `Municipal+Cache` persists **whole packs** — so the timestamp already round-trips through disk. `seedFromCache()` even restores `availableTime` from it (`Municipal+Cache.swift:112`).

**Nothing new needed persisting.** The data was there; it just never reached the view. That kept the change to plumbing + presentation, with no cache-format change and therefore no migration concern for existing installs.

### 2. The obvious timestamp is a trap

`carTrail.last?.time` is the natural-looking source — `CarTrailEntry` already stamps a `Date`. It is wrong in **both** directions:

- **Fresh data reads as old.** The trail only appends when the count *changes* (`CyclopsModel.swift` — `count != cars.last?.count`). A busy lot sitting at 0 for an hour has an hour-old trail entry despite a feed updating every 15s. It would grey out perfectly good data.
- **Stale data reads as brand new.** `CyclopsModel` is not `Codable` and is not cached. On cold launch `oldTrails` is nil, so the first rebuild appends `CarTrailEntry(count:, time: Date())` — stamping **now** onto a number that came off a 3-hour-old disk cache.

That second one is precisely the failure this feature exists to prevent, so building on the trail would have shipped the bug wearing a fix's clothing. The implementation uses `MncplParkAvPack.converted` instead, and the rationale is written into the doc comment on `AvailFreshness` so the next person doesn't re-derive it.

---

## What was built

New `AvailFreshness` enum in `CyclopsModel.swift` — `unknown` / `fresh` / `aging` / `stale`, thresholds as two named `static let`s, and a `heroColor` that returns `nil` for fresh (meaning: don't touch the cell's own colour).

| Age | State | Colour |
|---|---|---|
| < 5 min | `.fresh` | unchanged — keeps the existing scarcity colour (`.fern`, or `.primaryM` at 10–19) |
| 5–30 min | `.aging` | `.primary` |
| ≥ 30 min | `.stale` | `.secondary` |
| no timestamp | `.unknown` | unchanged |

### Files touched

| File | Change |
|---|---|
| `hootowl/model/CyclopsModel.swift` | `AvailFreshness` enum; `observed: Date?` on `CyclopsItem`; all 4 `CyclopsItem` inits assign it; `observedAt:` param (defaulted) on the mncpl `CyclopsModel` init |
| `Municipalities/framework/Municipal+Cyclops.swift` | `refreshCyclops()` builds the `parkId → converted` map from packs |
| `UI/Cyclops/CyclopsView.swift` | hero number wrapped in `TimelineView(.everyMinute)`, freshness overrides the scarcity colour |
| `Municipalities/UI/MncplCyclopsScreen.swift` | toolbar feed timestamp coloured on the same ramp |

---

## Four decisions worth knowing about

### Freshness is per-lot, not per-screen

A watchList spanning Taipei + New Taipei has two feeds landing minutes apart, so one global "last updated" would mislabel one municipality. `refreshCyclops()` builds a `parkId → converted` dictionary across all packs and each `CyclopsItem` carries its own `observed`.

Keyed by **which pack actually contained the lot**, not by `mncplInfo?.mncpl` — the latter is nil whenever static info is missing, which is exactly the degraded case where the label matters most.

### It needs a ticker, and that's not incidental

Staleness only matters **when polling has stopped** — which is exactly when nothing emits to redraw the cell. Without an independent clock the colour would freeze at render time and a number could sit there going stale, still green. `TimelineView(.everyMinute)` is system-aligned and coalesces across cells, so all 9 cells tick together and the thresholds land within a minute of true. It also stops on background for free, so it doesn't reopen the battery question.

### "White" was implemented as `.primary`, "grey" as `.secondary`

**This is the one place the implementation deviates from the literal spec — flagged for Jim's call.**

`MncplCyclopsScreen` only forces dark mode while the screen is *pinned* (`.environment(\.colorScheme, (colorScheme == .dark || pinningScreen) ? .dark : .light)`). On an unpinned light-mode device a literal `.white` number is invisible against the background.

`.primary` / `.secondary` preserve the intent — a **desaturation ramp**: coloured → neutral → dimmed — and read correctly in both schemes (white/grey in dark, black/grey in light). If Jim wants literal white regardless, it's a one-line change in `AvailFreshness.heroColor`.

### Staleness overrides the scarcity colour

The hero number already colours by count (`.fern`, `.primaryM` at 10–19). When both apply, staleness wins: how much you can *trust* the number dominates what it says. Fresh returns `nil` so the scarcity colour is untouched — the common path is byte-for-byte unchanged.

---

## Compatibility

`MncplCyclopsScreen0000.swift:166,182` also calls the mncpl `CyclopsModel` init. `observedAt:` is **defaulted to `[:]`**, so those sites compile untouched and their cells report `.unknown` → no colour change. Same for the direct `CyclopsItem` constructions in `NbsScreen.swift:731` and `NbsObsM+Ext.swift:244,342` (`observed:` defaulted to nil).

The two legacy Tpe inits set `observed = nil` explicitly — that feed carries no pack-conversion timestamp, so those cells keep their current behaviour rather than guessing.

**No new files** — `AvailFreshness` went into the existing `CyclopsModel.swift` deliberately, to avoid the target-membership trap recorded in [[bugs#2026-07-12-misleading-onchange-expects-01-arguments-error-was-a-missing-target-membership]]. Nothing to add to the Xcode project.

**Incidental fix:** the per-lot `avails.first { $0.parkId == pid }` scan is now a dictionary lookup — was O(watchList × avails) against a full-city availability list on every rebuild.

---

## Not verified

- **Not compiled.** SourceKit in this environment has no module context (it can't resolve `Municipal`, `.fern`, or `Cfg` either), so its diagnostics were noise throughout. Correctness was checked by reading: all four `CyclopsItem` inits assign `observed`, confirmed by enumerating them.
- **Not seen running.** Colour ramp, threshold timing, and the toolbar tint are unobserved.

### Worth checking on the device run

This folds neatly into the Cyclops 🕐 device sitting already owed ([[00-where-we-left-off]]):

- Force-quit, wait >30 min, relaunch → numbers should appear **grey**, then flip to `.fern` within ~15s once live data lands. That single check exercises cache-seeding, the ramp, and the ticker at once.
- Sit on the screen and watch a number cross the 5-minute boundary without touching anything — proves the TimelineView tick, which is the part most likely to be silently broken.
- Check both light and dark mode, pinned and unpinned, before signing off on the `.primary` substitution.
