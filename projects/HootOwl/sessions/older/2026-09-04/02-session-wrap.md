# 2026-09-04 — Session wrap

The day the Cyclops investigation closed and the work finally left this machine.

---

## Headline

**Four commits pushed to `origin/main`** — the first code to reach the server since 2026-08-31, and the end of a multi-day debugging arc. One of them closes a bug that had been open since **2026-06-15**.

```
0f863ed  Give the All-screen search keyboard a way out
14ceac7  Drive Cyclops cells from @State, not @Observable tracking
4f6dfd2  CyclopsView takes its item by value, not as a read-only @Binding
b069eb2  Track availability freshness by "last confirmed", not "last changed"
f069086  Aug31a   ← where the server was this morning
```

---

## What was actually fixed

### The Cyclops grey saga — four bugs, one feature

The grey numbers were never the bug. They were a **detector that worked**: Cyclops parking numbers had not been updating for a long time and nobody could see it, because a stale parking number looks exactly like a quiet parking lot. Adding a freshness colour made the invisible visible — a frozen *timestamp* advertises itself as it ages; frozen *data* just sits there looking plausible.

| # | Bug | Origin | Commit |
|---|---|---|---|
| 1 | Freshness read `converted` ("last **changed**") instead of a "last **confirmed**" clock | mine, 08-31 | `b069eb2` |
| 2 | `CyclopsView` held a read-only `@Binding`, suppressing child re-renders | pre-existing | `4f6dfd2` |
| 3 | `minuteFlow()` published into `@Observable` state from a background thread | pre-existing | `b069eb2` |
| 4 | `@Observable` invalidation never reaches `MncplCyclopsScreen` **on device** | pre-existing | `14ceac7` |

**Verified on device** (`con01.md`): 10 minutes unattended — 9 model refreshes, 9 sink fires, 8 body evaluations, every cell reading `firstObs:0s`, and it never went grey.

**#4's cause is still unexplained.** `14ceac7` routes around it with an explicit `@State` + Combine path; it does not answer why SwiftUI drops the invalidation. Three screens now carry the same workaround, which makes it structural.

### The keyboard trap — open since June

Typing in the All-screen search left the keyboard up with **no way to dismiss it**, and since `AppTabView` auto-hides the tab bar and the floating pill restores it *underneath* the keyboard, every other tab became unreachable. Three faults compounded: `onSubmit` never released focus; the only Done button was a conditional `ToolbarItem(placement: .automatic)` with nowhere to go in an `.inline` nav bar; and the escape hatch was itself covered.

Fixed with **three independent routes out** — `.keyboard` toolbar placement (can't be occluded by the keyboard), focus release on submit, and `.scrollDismissesKeyboard`. `AllTpeParkingScreen` hardened to match.

---

## Two things I got wrong today, corrected

**Main-thread parsing is not a problem.** I flagged it on 09-02 as a hitch risk. The device log measures it: 472 KB received → model rebuilt → view re-rendered in **8–56 ms**. Overstated; dropped from the urgent list.

**The ~5 min launch hang is probably my fault.** On 09-02 I lowered `"Mu1Base+Ext"` from `4` to `1` in `ffl.swift` to surface some debug lines. That file carries **per-item `.debug` logging over ~1,400–1,750 lots** in the *daily* transform path — at threshold 1 all of it prints synchronously at launch. Reverted. The timing fits: the daily path only runs on the first launch of a day, so a change made 09-02 first bit on 09-04. **Unconfirmed** — the hang predates the log capture. Detail: [[01-launch-hang]].

---

## Next, in order

### 1. Tomorrow's first launch — free test, ~2 min
The daily transform only runs on the **first launch of a day**, so this is the one chance per day to test the hang without forcing it.

- Start Console.app recording **before** launching
- Confirm `🐢 daily` appears — that proves the heavy path actually ran (two attempts this afternoon missed it, which is why the question is still open)
- Watch whether the UI responds in the first ~30 s

Clean → the `ffl` threshold was the cause, already reverted, done. Hang → the daily transform is genuinely too heavy for the main thread and needs moving off it.

### 2. Strip the diagnostics — one small commit
Four locations, all listed in [[unfinished]]. Grep `TEMP 2026-09-0`. Also restore the `.notice` levels that were raised so device logs would survive a debugger detach.

### 3. Onboarding — **the actual release blocker**
Everything else outstanding is verification or hygiene. This is the only remaining *feature* work, and it is blocked on a decision only Jim can make:

- [ ] pick the screen-1 headline lane (currently the playful owl) — [[onboarding]]
- [ ] then: `Localizable.xcstrings` batch (English filled, 中文 blank)
- [ ] then: wire into `LandingScreen` (ob0), build out ob1/ob2
- [ ] decide feedback transport (mailto first vs hosted form)

`hootowl/UI/onboard/` is still 2024 scaffolding.

### Also owed, worth one sitting together
Two device checklists that keep being carried forward — the **Phase 3 lifecycle test** (committed June 26, never run) and the **Cyclops 🕐 checklist**. Doing them in one pass would clear both.

### One with a deadline attached
**Mark `Municipal` `@MainActor` before the next city is added.** No live bug — all four `fetch(...)` sinks hop to main correctly today. But that hop is a per-call-site convention with zero enforcement, and `minuteFlow()` already lost it once by copy-paste. Every new zone is another chance to repeat it. Reasoning: [[00-why-municipal-should-be-mainactor]].

---

## Decisions still waiting on Jim

1. **`.primary` vs literal white** for the 5–30 min freshness state. Spec said white; implemented as `.primary` so it isn't invisible on an unpinned light-mode device. One line in `AvailFreshness.heroColor`.
2. **Onboarding screen-1 headline.**
3. **`CLAUDE.md` / `AGENTS.md` park-ID prefix claim** — states IDs are `tpe_`/`ntpc_` prefixed; no code does this, and it cost a full investigation cycle on 08-07. Your files to correct.

---

## Housekeeping

- `cyclops-freshness` branch is merged and redundant: `git branch -d cyclops-freshness`
- [[02-postmortem-what-went-wrong-and-why]] (09-01) is **out of date** — written before bugs #3 and #4 were understood. [[00-status-where-we-are]] supersedes it.

## Related
- [[00-status-where-we-are]] — the four-bug ledger and the three failed fixes
- [[01-launch-hang]] — hang hypothesis + the retraction on parsing cost
- [[unfinished]] — the full standing list
- [[01-technique-instrument-dont-guess]] — the method that eventually cracked it
