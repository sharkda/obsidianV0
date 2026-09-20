# 2026-09-01 — "Grey forever": root cause and fix

**Reported by Jim (2026-08-31, ~10:43):** Cyclops numbers stay grey indefinitely. The upper-left toolbar time keeps updating. "If this is updated 1 min ago, the colour should definitely get back to normal."

**Verdict: Jim is right, and yesterday's implementation was wrong.** Not a colour-mapping bug and not a ticker bug — the timestamp it read means something different from what the feature assumed.

**Status:** fixed in the working tree. **Not committed, not compile-verified.**

---

## The tell

The split Jim noticed is the whole diagnosis. Toolbar and cells read *different* clocks:

| Surface | Reads | Behaviour |
|---|---|---|
| Toolbar time | `municipal.availableTime` = **max** `converted` across all zones | kept updating |
| Cell colour | `item.observed` = **that lot's zone's** `converted` | frozen |

A max across zones advances as long as **any** zone republishes. A per-zone stamp freezes when **that** zone stops. So one zone was frozen while another kept moving — and the toolbar hid it.

---

## Root cause

`Mu1Base+Ext.minuteFlow()` short-circuits when the fetched payload is byte-identical to the previous one:

```swift
ffl("previousHash not changed")
if self.availableVbj.value != nil {
    ffl("availble w/o update, this round over")
    self.setMinutelyTimer(mg0: self.minutelyPubInterval)
    return          // ← never reaches oParseMinute → no new pack → converted frozen
}
```

`MncplParkAvPack.converted` is set to `Date.now` **inside the parse** (`TaipeiObs.swift:58`). The bail-out returns before that, so:

> **`converted` is the time the data last CHANGED — not the time we last confirmed it is current.**

Parking availability legitimately sits unchanged for long stretches (quiet lots, early morning, a full lot staying full). At 10:43 AM a zone can easily go 30+ minutes returning identical bytes. Every one of those rounds is a **successful fetch that proves the number is current** — and the old code treated the resulting silence as staleness.

So the cells were grey because the *content* hadn't changed in 30 minutes, while the data itself was fresh and confirmed every poll.

### The same mistake, one layer up

Yesterday's note argued against using `carTrail.last?.time` precisely because *"the trail only appends when the count changes, so an unchanged-but-fresh lot would read as old."* That reasoning was correct — and then the implementation used `converted`, which has **the identical defect at pack level**. The trap was avoided at the leaf and walked into at the root. Worth remembering: on this codebase, "when did this last change" and "when did we last confirm this" are different clocks almost everywhere, and freshness always wants the second one.

---

## The fix

Add a confirmation signal that fires on **every successful retrieval**, changed or not, and colour from that.

| File | Change |
|---|---|
| `Mu1Proto.swift` | `minutelyConfirmedVbj: CurrentValueSubject<Date?,Never>` added to the protocol |
| `Mu1Base.swift` | stored property |
| `mocks.swift` | mock conformance |
| `Mu1Base+Ext.swift` | `.send(Date.now)` on **both** the unchanged-bail branch and the parsed-successfully branch |
| `Municipal.swift` | `lastConfirmed: [MunicipalEnum: Date]`; `WirePack` gains a `confirmed` cancellable |
| `Municipal+Ext.swift` | `actWire` subscribes, records `lastConfirmed`, calls `refreshCyclops()` |
| `Municipal+Cyclops.swift` | per-lot stamp = `max(pack.converted, lastConfirmed[zone])` |

### Why a new subject rather than reusing `minutelyUpdateVbj`

The first attempt sent the tick on the existing `minutelyUpdateVbj`. **That would have been a battery regression** and was backed out before it went anywhere.

`minutelyUpdateVbj` feeds `secSincePrevRetrival` (`Mu1Base.swift:57`), which `resumePolling()` reads through the no-argument `setMinutelyTimer()` (`Mu1Base+Ext.swift:77`):

```swift
switch self.secSincePrevRetrival! {
case 0..<self.minutelyPubInterval: newWait = 60
default:                           newWait = self.minutelyPubInterval   // 210
}
```

On a quiet feed the old value stayed large, so a resume picked **210s**. Bumping it on every confirmation would have made it small, picking **60s** — a **3.5× increase in poll frequency after every foreground resume**, landing squarely on top of the battery work (#2/#3 exist to reduce exactly this). `minutelyConfirmedVbj` keeps the two meanings separate.

### What still legitimately goes grey

The fix deliberately preserves the feature's actual purpose. The `< 512 bytes` guard returns **before** the hash check and sends no confirmation, so:

| Situation | Confirmation? | Colour |
|---|---|---|
| Fetch fails / garbage response | no | ages → **grey** ✓ |
| Fetch succeeds, payload unchanged | **yes** | stays live ✓ *(was the bug)* |
| Fetch succeeds, payload changed | yes | stays live ✓ |
| Cold launch from disk cache, no fetch yet | no | **grey until first fetch** ✓ |

The last row is the original motivation and still works.

---

## Not proven from here

The code path is confirmed by reading; **that this was the only cause of what Jim saw is not.** A second candidate is still open and would look identical on screen: the watched pids not matching the live feed's ids — the unresolved `TPE####` seed question in [[bugs#2026-08-20-claudemd-claims-park-ids-are-tpe-ntpc-prefixed-no-code-does-that]]. If the ids don't match, `observedAt[pid]` is nil, the number comes from a stale trail, and the cell greys for a different reason.

**The existing logs already separate the two.** On the next run, watch for a zone repeating:

```
previousHash not changed
availble w/o update, this round over
```

- Repeats every poll for the zone holding the grey lots → this diagnosis, now fixed.
- Zone republishes normally (`🐎 minutelyAvailable`) but cells stay grey → **id mismatch**, a different bug, and the `TPE####` residual is the prime suspect.

Also unverified: nothing here has been compiled. SourceKit in this environment has no module context (it cannot resolve `Municipal`, `Mu1Base`, or `.fern` either), so its diagnostics were noise throughout. Both `Mu1Proto` conformers — `Mu1Base` and `MncpltPrtMock` — were checked by grep to declare the new member.

---

## Working tree now

Three uncommitted, unbuilt changes stacked up:

1. Battery #5 — `CLLocationManager` dedupe (2026-08-20)
2. Cyclops freshness colouring (2026-08-31)
3. This fix (2026-09-01)

All need the same single Xcode build. `.primary`-vs-literal-white from yesterday is still an open call for Jim.
