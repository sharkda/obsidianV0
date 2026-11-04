# 2026-09-04 — Launch hang (~5 min), and the grey fix confirmed

Two separate things came out of Jim's 11:00 device run. One is settled, one is a new hypothesis.

---

## Settled: the grey/stale bug is fixed

`con01.md` is unambiguous over a 10-minute unattended run:

| Marker | Count |
|---|---|
| `🎨 model refreshed` | 9 |
| `🦵 uiKick received` | 9 |
| `🏠 body eval` | 8 |

Every model refresh produced a sink fire and a body evaluation, every `🏠` read `firstObs:0s firstCar:7`, every `🎨` reported `thread:main`, and a single `🆔 12708723194660554214` confirms one `Municipal` instance. Jim: *"it never turned gray on my test."*

The `@State items` + `uiKickSbj` route works. That closes bug #4 in [[00-status-where-we-are]] — the fix, not the cause; **why `@Observable` invalidation fails on this screen is still unexplained.**

### Retraction: main-thread parsing is not a problem

I flagged main-thread JSON parsing as a hitch risk on 09-02. The log measures it — payload received → view re-rendered:

| `📦` received | `🏠` body eval | elapsed |
|---|---|---|
| 11:00:11.101 | 11:00:11.115 | **14 ms** |
| 11:02:12.021 | 11:02:12.077 | **56 ms** |
| 11:04:12.572 | 11:04:12.580 | **8 ms** |

472 KB parsed, model rebuilt, view re-rendered, all inside 60 ms. **My concern was overstated** — that item drops off the urgent list. It may still matter as cities are added, but it is not a present problem and it is not the hang.

---

## New: the ~5 minute launch hang

**Jim's sequence:** launch → grey → UI unresponsive ~5 min → responsive → tab tap → green → stayed green.

Grey at launch is *correct* (cache older than 30 min). The hang is the issue.

### What the log rules out

The capture starts at 11:00:00.320 with the app already mid-fetch, so **the hang window is not in it.** But across the 594 s it does cover, the largest gap is 52 s, and network/audio events flow continuously. So the process was never stopped — **the main thread was blocked while background work continued.**

### Hypothesis: my own diagnostic change caused it

On 2026-09-02 I lowered `"Mu1Base+Ext"` from `4` to `1` in `ffl.swift`'s `fileDubugLevelDict` to surface `📦 minutely Received` / `previousHash …`.

`classDebugFilter` prints a `.debug` line when `level <= debugThreashold` (2). At 4 those lines are suppressed; at **1 they all print**. And `Mu1Base+Ext` is exactly the wrong file to open up — it is full of **per-item `.debug` logging over ~1,400–1,750 lots**, all on the **daily** transform path:

- `WgsId_Pre_Dynamic` — a `rtWoPreMap` line per item with no pre-map, each doing a TWD97→WGS84 conversion and string interpolation
- `assessItemsForPreRtDiscrepanciesByPreMap` — `.map{ffl($0.descDiscrepancy,.debug)}` over `sampled`, `offs` **and** `wayOffs`
- `loadBundleIdWgs84Lookup` / `loadBundleWgs84Id0` — per-line CSV parse loops
- `removeDuplicated` — plus an `#if DEBUG` block that is **O(n²)** (`a0.filter` inside a map over `dupIds`)

`print()` is synchronous; thousands of them at launch, with a debugger or Console attached, blocks for a long time.

### Why it appeared only now

The daily heavy path runs on the **first launch of a new day**. `activate()` sets `timerDailySoon = true` only when `dailyDataState` is `.outdated`/`.noFile`; otherwise the daily timer is 21600 s and nothing heavy happens.

- 09-03 runs: 18:44, 19:36, 21:46 — daily already fetched that day → `.incumbent` → no heavy path → **no hang reported**
- 09-04 run: 11:00, first of the day → full daily transform → **hang**

That fits the observation exactly, and explains why the threshold change (made 09-02) only bit on 09-04.

### Status: CONFIRMED 2026-09-05 — reverted, and the hang is gone

`"Mu1Base+Ext"` is back to `4`. Nothing is lost: `📦` and `previousHash` are now `.notice`, and `.notice` bypasses `classDebugFilter` entirely.

**Confirmed 2026-09-05** (`sessions/2026-09-05/con01.md`). Capture started before launch, on the first run of the day, with the threshold back at 4:

- The heavy path **definitely ran**: `WgsNoPre(dyanmic)mapped is 1417` (NTP) and `1756` (Taipei) — the full per-item transform over ~3,173 lots.
- Both completed ~11 s and ~13 s after launch, log continuous throughout, **no stall**, and Jim observed no hang.

So the ~5 min freeze was thousands of synchronous `print()` calls from per-item `.debug` logging, not the daily transform itself. Cause: my own diagnostic change. Fixed by the revert.

**Correction:** I said earlier that Taipei skips `WgsId_Pre_Dynamic`'s per-item loop (no pre-map file, "taipei, return"). It does not — 1,756 Taipei items went through it. Doesn't change the conclusion, but the characterisation was wrong.

---

## Next capture, if the hang recurs

1. Start Console.app recording **first**, then launch the app.
2. Do it on the **first launch of a day** (or delete the app's cached daily file) so the heavy path runs.
3. Look for: `📦 daily Received`, `WgsNoPre(dyanmic)mapped`, `rtWoPreMap`, `obyId`, `🐢 daily`.

If the hang is gone after this revert, that is the answer. If it recurs **with** the threshold back at 4, the cause is the daily transform itself, not the logging — and the real fix is moving that work off the main thread, which is a genuine structural issue independent of anything I changed.

---

## Standing concern this exposes

Even with logging back at 4, the daily path does heavy per-item work after `.receive(on: DispatchQueue.main)` in `dailyRetrieveFlow` — dedup, WGS84 mapping, sanity filters over ~1,750 items — and includes an `#if DEBUG` O(n²) block. It happens once a day so it is easy to miss, and it grows with every city added. Worth revisiting alongside the `@MainActor` work in [[00-why-municipal-should-be-mainactor]].

## Related
- [[00-status-where-we-are]] — the four-bug ledger
- [[unfinished]] — cleanup and open items
- `con01.md` — this run
