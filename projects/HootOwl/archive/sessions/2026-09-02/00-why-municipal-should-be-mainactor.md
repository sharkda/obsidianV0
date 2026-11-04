# 2026-09-02 — Why `Municipal` being non-`@MainActor` is a standing risk

Expansion of a remark from 2026-09-01, at Jim's request. Background: [[bugs#2026-09-01-minuteflow-published-into-observable-state-from-a-background-thread-fixed]].

**First, a correction to what I said.** I claimed *"`SourceBase.swift:180` has the same unhopped fetch."* **That was wrong.** Line 180 is the *definition* of `fetch(url:)`, not a use of it; `SourceBase`'s only sink site (`:103`) does hop to main correctly. I conflated a definition with a call site. Surveying all four sink sites properly:

| Site | Flow | Hops to main? |
|---|---|---|
| `Mu1Base.swift:211` | daily | ✅ |
| `Mu1Base+Ext.swift:231` | `minutelyRetrieveFlow` | ✅ |
| `Mu1Base+Ext.swift:125` | `minuteFlow` | ✅ *(added 2026-09-01 — was the bug)* |
| `SourceBase.swift:103` | source base | ✅ |

So **the codebase is currently correct at every site.** The argument below is not "there are more bugs like this" — it's "nothing stops the next one."

---

## The mechanism, stated plainly

`fetch(url:)` returns `URLSession.dataTaskPublisher`, which delivers its values on **a URLSession background queue**. Every consumer therefore starts on a background thread and must hop to main before touching UI-observed state:

```swift
fetch(url: urlMinutely)
    .compactMap({ $0 })
    .receive(on: DispatchQueue.main)   // ← the only thing standing between you and the bug
    .sink { data in
        …
        self.availableVbj.send(parsed)   // → Municipal.actMinutely → cyclopsMod = …
    }
```

`cyclopsMod` lives on `Municipal`, which is `@Observable`. **Mutating `@Observable` state off the main thread makes SwiftUI's invalidation unreliable** — the value changes, but the view is never told to re-render. That is precisely what cost 6 log files and ~7 rebuilds: the model was demonstrably correct the whole time (`obs:0s FRESH`) while the cell sat frozen for 98 minutes.

### Why this class of bug is disproportionately expensive

- **It is silent.** No crash, no exception, no warning. Just a value that doesn't arrive.
- **It is nondeterministic.** It presented differently on an iPhone 15 device than on an iPhone 17 Pro simulator, because thread scheduling differs. A bug that changes with hardware is a bug you cannot trust your own testing on.
- **It hides behind plausible alternatives.** Along the way it looked exactly like a stale-cache bug, then exactly like a binding bug. Both of *those* were real and worth fixing — which made it even easier to stop early and believe the job was done.
- **The failure is in the *absence* of a line.** Code review catches wrong lines far more reliably than missing ones. There is nothing at the `minuteFlow` call site to look wrong.

---

## The actual problem: the guarantee is per-call-site

Today, thread-safety here rests on **every future author remembering to write one line** in every new flow that publishes into `Municipal`. That's a convention, not a guarantee, and this codebase already has evidence of the convention failing in the most likely way:

> `minuteFlow()` was copied from `minutelyRetrieveFlow()` — which **has** the hop — and the hop was dropped in the copy.

Copy-paste is the normal way new flows get written here. The one mechanism that would have caught it (`CLAUDE.md`: *"Use `@MainActor` explicitly where UI updates occur"*) is a documentation rule with **no enforcement whatsoever** — nothing in the compiler, the types, or the tests checks it. And `Municipal` will keep growing: every new municipality adds another proto, and every new proto is another flow that must remember.

**The asymmetry is what matters.** Forgetting the hop costs hours of misdirected debugging and is nearly invisible in review. Remembering it costs one line. Any mechanism that converts "must remember" into "compiler tells you" is worth a lot here.

---

## Options

### A. Mark `Municipal` `@MainActor` — the structural fix

```swift
@MainActor
@Observable final class Municipal: NSObject { … }
```

**What it buys:** the compiler now knows every `Municipal` member must be touched from the main actor. Calling `self.actMinutely(…)` from inside a plain (non-isolated) Combine sink becomes a **compile error**, not a silent runtime misbehaviour. The rule stops depending on memory. This also matches what `CLAUDE.md` already asks for, and makes the intent explicit to anyone reading the class.

**What it costs:** every call site must be in a main-actor context. Where one isn't, the compiler makes you write `await MainActor.run { … }` or `Task { @MainActor in … }` — and you'll likely have to work through a batch of these on first adoption. Under Swift 5 language mode with minimal concurrency checking, some of it surfaces as warnings rather than errors, so the enforcement is only as strong as the checking level. `Municipal` also inherits `NSObject` and is a `CLLocationManagerDelegate`; those delegate callbacks already arrive on the main queue in practice, but the compiler may still want annotations.

**Verdict: the right end state.** It converts an invisible runtime failure into a visible compile-time one, which is exactly the trade you want for a bug of this cost. Do it as its own change, not bundled with anything else — the diff will be wide and mechanical, and you want to be able to revert it cleanly.

### B. Move the hop inside `fetch(url:)`

```swift
func fetch(url: URL) -> AnyPublisher<Data, Error> {
    URLSession.shared.dataTaskPublisher(for: url)
        .tryMap { … }
        .receive(on: DispatchQueue.main)   // every consumer gets it, can't be forgotten
        .eraseToAnyPublisher()
}
```

**Pro:** one line, one place, immediately removes the copy-paste hazard. Cheapest possible risk reduction.

**Con:** it hides the threading decision rather than expressing it, and it locks in something that's arguably already wrong — see below. It also can't help any *future* pipeline that doesn't go through `fetch`.

**Verdict:** a decent stopgap if you don't want to do A now. Not a substitute for A.

### C. Leave it, rely on review

Not recommended. The one prior instance of this was introduced exactly the way the next one will be, and it was not caught in review.

---

## A related issue this exposes

Look at what currently runs on the main thread because the hop is placed *before* the sink:

```
receive(on: main) → sink → oParseMinute → JSONDecoder decodes ~1,400 lots → send
```

**JSON decoding of the full city feed happens on the main thread**, roughly every 120 seconds, for every active zone. That's not a correctness bug — but it is main-thread work that could cause a visible hitch, and it grows linearly with each municipality added.

The better shape is to **parse on the background and hop only to publish**:

```swift
fetch(url: urlMinutely)
    .compactMap { $0 }
    .tryMap { try self.oParseMinute(data: $0) }   // stays on background
    .receive(on: DispatchQueue.main)              // hop only for the publish
    .sink { … availableVbj.send(parsed) … }
```

This is a bigger refactor — the current sink interleaves parsing with hash checks, timer scheduling, earcons and DQI, so it can't just be reordered. Worth doing when the polling code is next touched, not before. **Note it interacts with the battery work**: less main-thread work per poll is directly relevant to the deferred Energy Impact measurement.

---

## Recommendation

1. **Now:** nothing — the codebase is correct at all four sites today.
2. **Before adding the next municipality** (i.e. before the next new flow gets copy-pasted): do **A**, `@MainActor` on `Municipal`, as a standalone change. That's the moment the risk becomes live again.
3. **When polling is next refactored:** move parsing off the main thread (the section above), and fold it into the battery measurement work.

If A looks too disruptive when you try it, **B** buys most of the protection for one line and can be done in a minute.

## Related
- [[bugs#2026-09-01-minuteflow-published-into-observable-state-from-a-background-thread-fixed]]
- [[02-postmortem-what-went-wrong-and-why]] — the full debugging narrative
- [[unfinished]] — tracked there under the audit item
- [[battery]] — main-thread parsing cost is relevant to the deferred measurement
