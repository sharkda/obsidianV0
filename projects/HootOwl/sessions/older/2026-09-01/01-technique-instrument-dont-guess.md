# 2026-09-01 — Technique: stop guessing, write a discriminating log line

Captured at Jim's request while debugging "Cyclops stays grey" ([[00-freshness-grey-forever-root-cause]]). This is the method, not the bug. Candidate for promotion to `patterns/` once it's been used a second time.

---

## The trigger

Two fixes, both reasoned from reading the code, both wrong:

1. Colour from `MncplParkAvPack.converted` → wrong, `converted` freezes on the hash bail-out.
2. Add `lastConfirmed` from a confirmation subject → still grey.

**Two wrong guesses in a row is the signal.** Not "read harder" — the reading was careful both times and produced a confident, plausible, incorrect answer. A third careful read has no reason to do better. At that point the bottleneck is not analysis, it's *evidence*, and the cheapest evidence is a log line designed to discriminate.

This matters more than usual here because the CLI can't build this project (`Package.resolved` gitignored → SPM re-resolves `ConcaveHull`). Every guess costs Jim a manual Xcode build and an app run. Guessing is expensive; instrumenting once is cheap.

---

## The method

### 1. Narrow by deduction first, to know what to instrument

Instrumenting everything is just as lazy as guessing. Use the symptoms to eliminate branches before writing any log.

The decisive symptom here was Jim's own observation: **"the toolbar time is very up-to-date."** Chain it:

```
toolbar shows availableTime
  → availableTime is set in the parkAvailVbj sink
    → parkAvailVbj IS emitting
      → actMinutely IS running
        → parkAvPack HAS fresh `converted`
          → refreshCyclops() IS running with fresh data
```

That single observation killed the entire "data isn't arriving" family of hypotheses and moved the fault downstream of `refreshCyclops`. **The user's incidental detail was worth more than either of my code reads.** Ask for the thing that *works* alongside the thing that's broken — a working sibling is a free bisection.

### 2. Design each field to split hypotheses, not to "show state"

The failure mode of debug logging is dumping everything and reading tea leaves. Every field should have a *prior question it answers*:

| Field | Question it answers |
|---|---|
| `hit` / `MISS` | is this pid present in the live pack at all? (id mismatch vs. not) |
| `obs:<n>s` | is the stamp fresh? (my computation wrong vs. right) |
| `FRESH`/`AGING`/`STALE` | does the model agree with what's on screen? (model vs. view) |
| `conv:` vs `conf:` per zone | is the confirmation fix actually firing? |
| `car:` + feedState | is this cell even in the code path I think it is? |

If you can't say which hypothesis a field eliminates, cut it.

### 3. Write the decision table BEFORE reading the output

This is the part that's easy to skip and does the most work:

| What the line shows | Cause | Where the bug is |
|---|---|---|
| `MISS` on grey lots | pids absent from live pack — id mismatch | not my code |
| `hit` but `obs:` large | stamp computation wrong | `refreshCyclops` |
| `hit`, `obs:` small, `FRESH` — yet grey | model right, view stale | `CyclopsView` / binding |

Committing to the interpretation in advance is what stops the next failure mode: seeing the output and inventing a story that fits it. A table written beforehand can be *wrong* — and finding out it's wrong is itself information ("none of my three branches matched" means the model of the system is off, which is a bigger and more useful finding than any of the three).

### 4. Mark it temporary, in the code

```swift
/// TEMPORARY diagnostic for the "grey forever" report (2026-09-01). … Delete once the cause is found.
fileprivate func logFreshnessDiag(packs:observedAt:) { … }
```

Dated, reason stated, disposal condition stated. Diagnostics that don't say when they die become permanent noise. `fileprivate` keeps it from growing callers.

### 5. One line per event, greppable prefix

`🎨` matches the existing convention (`🐎` minutelyAvailable, `📦` minutely Received, `📛` short response). One line per refresh, all fields on it — so a single grep gives a time series, and you can *see* the moment a value stops advancing. Multi-line dumps lose that.

---

## Why not a debugger / breakpoint

Worth stating, since it's the obvious alternative. This bug is **temporal** — the question is "does this value stop advancing over minutes, and when." Breakpoints freeze time and answer "what is this value once." A log line gives the series. For "why did this stop updating" bugs, logging beats stepping almost every time; for "why is this value wrong right now", the reverse.

---

## The generalisable rules

1. **Two wrong reasoned guesses = switch to evidence.** The count is the trigger, not the difficulty.
2. **Mine what still works.** A working sibling surface (toolbar vs. cells) is a free bisection of the pipeline.
3. **Every logged field must eliminate a hypothesis.** No field, no question, no field.
4. **Write the interpretation table first.** It prevents fitting a story to the output, and "no branch matched" is a real result.
5. **Date the diagnostic and state its disposal condition** in the code.
6. **Logging for temporal bugs, breakpoints for state bugs.**
7. **When each iteration costs the user a manual build, the economics change** — one good instrument beats three cheap guesses. Weigh the user's cost per round-trip, not yours.

---

## Related

- The bug this came from: [[00-freshness-grey-forever-root-cause]]
- The prior trap in the same feature — using a "last changed" clock where "last confirmed" was wanted: [[01-cyclops-cache-freshness]]
