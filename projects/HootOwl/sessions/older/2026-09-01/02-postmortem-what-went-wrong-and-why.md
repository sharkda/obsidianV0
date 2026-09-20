# 2026-09-01 — Postmortem: the "grey forever" Cyclops bug

Written for learning, at Jim's request. Covers what was actually broken, how the investigation went — **including the two wrong answers** — and what generalises.

**Outcome:** fixed and verified. Working tree, uncommitted, unbuilt beyond Jim's local builds.

---

## Part 1 — What was actually wrong

Three separate problems, stacked. The visible symptom was three layers away from the real cause, which is why it took three attempts.

| # | Problem | Pre-existing? | Severity |
|---|---|---|---|
| 1 | `MncplParkAvPack.converted` means "last **changed**", not "last **confirmed**" | yes, latent | made freshness misreport |
| 2 | Cyclops cells never re-rendered — a read-only `@Binding` suppressed child updates | **yes, and it was the real bug** | numbers were silently stale |
| 3 | The freshness feature was built on clock #1 | no, mine | surfaced #1 and #2 |

### Problem 2 was the actual bug, and it predates everything

**Cyclops numbers were never updating.** Not the colour — the *numbers*. `TPE0080` sat on `19` while the feed said `20`. That had presumably been true for a long time; someone had already felt it and papered over it with a forced-identity hack in `MncplCyclopsScreen0000`:

```swift
.id("\(item.wrappedValue.pid)-\(uiKick)")   // ← a "kick" to force redraw
```

Nobody had diagnosed it, because a stale parking number is **indistinguishable from a quiet parking lot**. There is no way to look at `19` and know it should say `20`.

**The freshness colouring is what made it visible.** A frozen *number* hides; a frozen *timestamp* does not — it ages on its own, crosses a threshold, and changes colour. The feature didn't cause the bug; it turned a silent bug into a loud one.

> **Takeaway:** when a new feature "breaks" something, check whether it actually *exposed* something. Adding an observable that ages by itself is a genuinely good way to find frozen state, because unlike data, elapsed time always changes.

### Why the cells froze — the SwiftUI mechanism

`CyclopsView` declared:

```swift
@Binding var item: CyclopsModel.CyclopsItem
```

but it **never wrote through that binding** — `$item` appears nowhere in the file. It was a read-only `@Binding`.

SwiftUI decides whether to re-run a child's `body` by comparing the child's stored properties. `CyclopsView`'s were `@Binding var item`, `@State`, and `@AppStorage`. **A `Binding`'s identity is its storage location, not its value** — so it compares equal on every parent update, no matter how much the underlying data changed. SwiftUI concluded "this child's inputs are unchanged" and skipped its `body`.

The parent *was* updating correctly the whole time. That's why the toolbar timestamp worked — it reads `municipal.availableTime` directly in the parent's body.

**The fix:** pass by value.

```swift
let item: CyclopsModel.CyclopsItem                       // was @Binding
ForEach(municipal.cyclopsMod.items, id: \.pid) { … }     // was ForEach($bindable.cyclopsMod.items…)
```

Now the child's input is a value that genuinely differs between updates, so SwiftUI re-renders. Reading `municipal.cyclopsMod.items` directly in the body is also what registers the `@Observable` dependency.

> **Rule:** use `@Binding` only when the child **writes back**. A read-only `@Binding` is not merely unnecessary — it actively suppresses updates. Applied to all six `CyclopsView` call sites.

### Problem 1 — two different clocks

`minuteFlow()` short-circuits when the fetched payload hashes identical to the previous one:

```swift
ffl("previousHash not changed")
if self.availableVbj.value != nil {
    self.setMinutelyTimer(mg0: self.minutelyPubInterval)
    return          // ← returns BEFORE oParseMinute, which is where `converted` is stamped
}
```

So `converted` advances only when the **content changes**. Parking availability legitimately returns identical bytes for 30+ minutes. Every one of those rounds is a successful fetch *proving the data is current* — and the code read that silence as staleness.

**The fix:** a separate `minutelyConfirmedVbj`, sent on **every** successful retrieval (changed or not), recorded as `Municipal.lastConfirmed[zone]`, with freshness taking `max(converted, lastConfirmed)`.

Verified in the final log:

```
taipei conv:142s conf:56s  →  TPE0080 hit obs:0s FRESH
```

Content unchanged for 142s, confirmed 56s ago, correctly stays fresh. Under the old code that lot was on its way to grey with perfectly good data.

**What still legitimately goes grey** — the `< 512 bytes` guard returns *before* the hash check and sends no confirmation, so a genuinely failing feed still ages out, as does a cache-seeded cold launch before the first fetch. That was the feature's original purpose and it survives intact.

---

## Part 2 — How the investigation went, honestly

### The two wrong answers

**Wrong answer #1 — build freshness on `converted`.** I had *already written down* the correct reasoning, in the 2026-08-31 note, when rejecting `carTrail.last?.time`:

> *"the trail only appends when the count changes, so an unchanged-but-fresh lot would read as old"*

Then I used `converted`, which has the **identical defect one layer up**. I avoided the trap at the leaf and walked into it at the root.

*Why it happened:* I checked whether `converted` was *set* freshly (it is — `Date.now` inside the parse) and stopped there. I never asked **under what conditions the parse runs at all**. Verifying a value's assignment is not the same as verifying its update *frequency*.

**Wrong answer #2 — assume the confirmation fix was sufficient.** It was necessary, but I asserted it would fix the symptom without evidence. It didn't, because the real bug was elsewhere.

*Why it happened:* I had a mechanism that explained the symptom, and stopped looking. A plausible mechanism that explains the symptom is not proof it is *the* mechanism.

### What actually broke it open

**Jim's incidental observation.** Not a code read:

> *"it still stays greyed out even the toolbar time is very up-to-date."*

That one sentence is a free bisection. Toolbar and cells read the same pipeline through different paths:

```
toolbar → municipal.availableTime      → parent body     → WORKING
cells   → cyclopsMod.items via Binding → child body      → BROKEN
```

Everything upstream of the split had to be healthy, because the toolbar proved it. That eliminated the entire "data isn't arriving" family in one step — more than either of my careful code reads achieved.

> **Takeaway:** when reporting a bug, say what still *works* alongside what's broken. A working sibling narrows the search more than a detailed description of the failure.

### Then: stop guessing, instrument

Two wrong reasoned answers is the signal to switch from analysis to evidence. Method written up separately in [[01-technique-instrument-dont-guess]]. Two log lines were added:

- `🎨` in `refreshCyclops()` — what the **model** holds
- `🖌` in `CyclopsView` — what the **view** holds

Same fields on both sides, deliberately, so they could be diffed. That comparison is what made the answer unmissable:

| | model (`🎨`) | view (`🖌`) |
|---|---|---|
| car | `20` | `19` |
| obs age | `0s` | `627s` |

The model was healthy. The view was 10 minutes behind. Nothing upstream could produce that; it had to be the view layer.

**The clincher was the shape of the number, not its size.** Before the fix `obsNow` climbed monotonically — 181 → 207 → 267 → 327 → 627 — in exact 60s steps, which is the `TimelineView` tick. A frozen timestamp plus a moving clock. After the fix it climbs *and resets* — 93 → 126 → 58 → 77 → 44 → 51. **Only new data can make an age go down.** That single property is what proved the fix, and it's more reliable than watching a car count that might legitimately not change.

> **Takeaway:** prefer a signal whose *shape* is diagnostic (monotonic vs. sawtooth) over one whose *value* you have to judge. Jim couldn't verify the numbers were correct — they weren't at the parking site — but the sawtooth proved liveness regardless.

---

## Part 3 — What was changed

| File | Change |
|---|---|
| `Mu1Proto.swift` / `Mu1Base.swift` / `mocks.swift` | new `minutelyConfirmedVbj` |
| `Mu1Base+Ext.swift` | send it on **both** the unchanged-bail and parsed branches |
| `Municipal.swift` | `lastConfirmed` + `noteConfirmed(_:at:)`; `WirePack.confirmed` |
| `Municipal+Ext.swift` | subscribe, record, rebuild |
| `Municipal+Cyclops.swift` | stamp = `max(converted, lastConfirmed[zone])` |
| `CyclopsModel.swift` | `AvailFreshness`; `observed` on `CyclopsItem` |
| `CyclopsView.swift` | **`@Binding` → `let`**; freshness overrides scarcity colour |
| `MncplCyclopsScreen.swift` + `CyclopsScreen2` + `…0000` | `ForEach($…)` → `ForEach(…)` at all six sites |

### Two near-misses caught before shipping

1. **A battery regression.** My first confirmation tick reused the existing `minutelyUpdateVbj` — which feeds `secSincePrevRetrival`, which `resumePolling()` reads to choose a 60s vs 210s poll interval. That would have **tripled poll frequency after every foreground resume**, straight into the battery work. Hence the separate subject.
   > **Rule:** before reusing an existing signal, check every consumer. A subject's meaning is defined by who reads it, not by its name.

2. **A silent semantic change.** Replacing `avails.first { $0.parkId == pid }` with a dictionary changed first-wins to last-wins. Jim's own log revealed the NTP feed ships **duplicate parkIds** (`060085`, `170120`), so that mattered. Restored explicitly.
   > **Rule:** an "obvious" O(n²)→O(n) optimisation can carry a tie-breaking rule with it. `first` is a specification, not just a search.

---

## Part 4 — The transferable lessons

1. **"Last changed" and "last confirmed" are different clocks.** Anything answering *"how old is this?"* wants the second. This codebase has at least three of the first kind (`carTrail.last?.time`, `converted`, `minutelyUpdateVbj`) and had none of the second until now. Whenever you find a value only updated on change, ask what happens to a consumer who needs to know it's still *valid*.

2. **A read-only `@Binding` suppresses child re-renders.** Use `@Binding` only when the child writes back. Otherwise pass by value.

3. **A new feature that breaks something may have exposed it.** Ask "did I cause this, or reveal it?" — the answer changes what you fix.

4. **Elapsed time is a great canary.** Frozen data hides; a frozen timestamp advertises itself. Consider surfacing an age wherever silently-stale state would be costly.

5. **Two wrong reasoned answers = switch to evidence.** The count is the trigger, not the difficulty.

6. **Instrument both sides of a suspected boundary with identical fields.** The diff is the finding. One-sided logging would not have found this.

7. **Verifying a value's assignment ≠ verifying its update frequency.** "Is this set correctly?" and "under what conditions does this code run?" are different questions. #1 came entirely from answering only the first.

---

## Still unverified

- **The stale path never actually ran.** Peak observed age was 126s; nothing crossed 5 or 30 minutes. Whether genuinely old data goes grey correctly is **untested** — covered by the launch-after-30-minutes step in the device run.
- **`.primary` vs literal white** (2026-08-31 decision) is still Jim's call — spec said "white", implemented as `.primary` so it isn't invisible in light mode.
- **Diagnostics still in the code.** `logFreshnessDiag` (`Municipal+Cyclops.swift`) and `heroColorLogged` (`CyclopsView.swift`), both marked `TEMPORARY`. Recommend keeping until after the device run — that run exercises the stale path and these make it readable — then removing both in one pass.

## Related

- [[00-freshness-grey-forever-root-cause]] — the first (incomplete) diagnosis
- [[01-technique-instrument-dont-guess]] — the instrumentation method
- [[01-cyclops-cache-freshness]] (2026-08-31) — the original feature
- `logs.md` / `logs2.md` / `logs3.md` — raw evidence for each stage
- [[swiftui-state-and-identity]] — the `@Binding` finding belongs there
