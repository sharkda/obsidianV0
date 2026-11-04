# 2026-09-04 — Status: where the Cyclops grey investigation actually stands

Written while Jim runs the device test. Supersedes the narrative in [[02-postmortem-what-went-wrong-and-why]] (2026-09-01), which was written before three of the four bugs below were understood — **that note's conclusion is now wrong** and it should be read as a snapshot, not as current status.

---

## One-paragraph summary

The grey numbers were never the bug. They were a **symptom-detector that worked**: Cyclops parking numbers had not been updating for a long time, and nobody could see it, because a stale parking number looks exactly like a quiet parking lot. Adding a freshness colour made the invisible failure visible — a frozen *timestamp* advertises itself as it ages, where frozen *data* just sits there looking plausible. Four distinct bugs came out of this. One was mine, in the new feature. Three were pre-existing. Three are fixed and verified; the fourth has a fix that is **built but not yet verified**, and the underlying cause is still unexplained.

---

## The bug ledger

| # | Bug | Origin | Status |
|---|---|---|---|
| 1 | Freshness read `converted` ("last **changed**") instead of a "last **confirmed**" clock | **mine**, 2026-08-31 | ✅ fixed + verified |
| 2 | `CyclopsView` held a read-only `@Binding`, suppressing child re-renders | pre-existing | ✅ fixed |
| 3 | `minuteFlow()` published into `@Observable` state from a background thread | pre-existing | ✅ fixed + verified (`thread:main` in every log since) |
| 4 | `@Observable` invalidation never reaches `MncplCyclopsScreen` **on device** | pre-existing | ⏳ **fix built, unverified** — cause still unknown |

### #1 — two different clocks (mine)

`MncplParkAvPack.converted` is stamped inside the parse, and `minuteFlow()` returns *before* the parse when the payload hashes identical to last time. So `converted` only advances when the **content changes**, not when the data is **confirmed current**. Parking availability legitimately returns identical bytes for 30+ minutes, so confirmed-good data aged into the stale bucket.

Fixed with a separate `minutelyConfirmedVbj` → `Municipal.lastConfirmed[zone]`, freshness taking `max(converted, lastConfirmed)`. Verified in the wild:

```
taipei conv:142s conf:56s  →  TPE0080 obs:0s FRESH
```

Content unchanged 142s, confirmed 56s ago, correctly stays fresh.

> **The lesson worth keeping:** "when did this last change" and "when did we last confirm this" are different clocks, and anything answering *"how old is this?"* wants the second. This codebase has at least three of the first kind and had none of the second. I had already written down this exact reasoning when rejecting `carTrail.last?.time` — then used `converted`, which has the identical defect one layer up.

### #2 — read-only `@Binding`

`CyclopsView` declared `@Binding var item` and never wrote through it. **A `Binding`'s identity is its storage location, not its value**, so it compares equal on every parent update, SwiftUI concludes the child's inputs are unchanged, and skips its `body`. Fixed by passing the item by value at all six call sites across three screens.

### #3 — background-thread publish

`fetch(url:)` delivers on a URLSession background queue. `minuteFlow()` sank it **without** `.receive(on: DispatchQueue.main)` — while its sibling `minutelyRetrieveFlow()`, which it was copy-pasted from, has always had one. So `cyclopsMod = …` ran off-main, and `@Observable` invalidation is unreliable there. Fixed; every log since reports `thread:main`.

### #4 — the one still open

On device, `refreshCyclops()` runs, mutates `cyclopsMod` on the main thread, on the single shared `Municipal` instance — and `MncplCyclopsScreen.body` **does not re-run**. Evidence (`console01.md`, 2026-09-03): 8 model refreshes including a real `car:18 → 21` change, producing 3 body evaluations, **none of them from a fetch**. The cells only refreshed when Jim forced a structural update — the reorder sheet, or a tab tap.

Every property of a working setup is present. The cause is genuinely unexplained.

---

## Three failed fixes for #4, and why each failed

Worth recording, because each looked right and each taught something.

**Attempt 1 — `@Binding` → value.** Real bug (#2), necessary, insufficient. It couldn't show a result because #3 and #4 were also blocking the same path.

**Attempt 2 — main-thread hop.** Real bug (#3), necessary, insufficient. Same reason.

**Attempt 3 — `uiKick = UUID()` counter.** Failed for a reason that was **entirely my error**: `console3.md` shows the Combine sink firing 4× and `body` running 0×. **SwiftUI only invalidates on a `@State` write if `body` actually reads that state.** I wrote a counter the body never read — and wrote "the value itself is unused — the write is the point" in the comment, which is exactly backwards. The two screens that already carry this workaround (`MncpltOne`, `MncplCyclopsScreen0000`) do it correctly, reading it via `.id("\(pid)-\(uiKick)")`. I had the correct example in front of me and missed the difference.

**Attempt 4 — the one now under test.** `MncplCyclopsScreen` holds `@State private var items: [CyclopsItem]`; `body` reads it; the `uiKickSbj` sink writes it. Because the body reads the state, the write is guaranteed to invalidate. This is the "Combine sink + `@State`" path `CLAUDE.md` already sanctions.

---

## What the current test decides

| Observation | Meaning |
|---|---|
| Every `🦵` followed by a `🏠` | the write invalidates — fix works |
| Stays green 10+ min untouched | the user-visible goal |
| `🦵` with no `🏠` | stop. Something is wrong beyond this screen and it needs isolating in a scratch project |

Plus, ideally, the **negative** test — cut the network for ~6 minutes and confirm it *still* goes grey. The cells now get their data from a different place, so it's worth proving the feature still works rather than only that the plumbing does.

---

## Honest assessment

**Do not treat #4 as fixed until the log says so.** Three prior fixes for this symptom were all wrong, and two of them I presented with more confidence than the evidence supported. Specifically:

- I read the logs3 `obsNow` resets as proof the binding fix worked. They were at exactly two points, matching the two times Jim backgrounded the app — forced re-renders, not observation. The reset *count* matched Jim's backgrounding count and I didn't check.
- I ran every diagnostic on the simulator, where the bug does not reproduce, while the bug lived on the device. That mismatch invalidated several conclusions.
- I shipped attempt 3 with **no log line of its own**, so its own failure was indistinguishable from a stale build until I added one.

**What has held up throughout:** the model is correct, on the main thread, single instance, and the view does not re-run until something forces it. Every other inference has been overturned at least once.

---

## After this test

If it passes:
1. Strip all diagnostics (tracked in [[unfinished]] — `🎨`, `🏠`, `🦵`, `🪟`, plus the `ffl.swift` threshold and the `.notice` level changes).
2. Commit as **separate** commits — these are four independent bugs, and #3 in particular deserves its own message as the reference for "model updates but screen doesn't."
3. Rewrite [[02-postmortem-what-went-wrong-and-why]], which is now materially out of date.

Still open regardless:
- **Why `@Observable` invalidation fails on this screen.** Three screens have now needed the same workaround, so it's structural — `AppTabView`'s dynamic `ForEach` plus the auto-hide tab bar is the prime suspect. Deserves its own investigation, not a blocker on this feature. One concrete oddity: `MncplCyclopsScreen`'s VStack has an extra first child **only on the simulator** (`#if targetEnvironment(simulator) Text(getSourceFileName())`), which is the sole code-level device/simulator difference in the misbehaving view. Speculative, but the only structural asymmetry there is.
- `Municipal` should be `@MainActor` before the next city is added — [[00-why-municipal-should-be-mainactor]].
- `CyclopsModel.==` is broken (reports models with different car counts as equal). No consumer today; a landmine.
- Feed parsing runs on the main thread (~1,400 lots, every ~120s per zone).

## Related
- [[unfinished]] — everything tracked, including every diagnostic to strip
- [[01-technique-instrument-dont-guess]] — the method that eventually worked
- [[swiftui-state-and-identity]] — #2 recorded there
- `console01.md` / `console2.md` / `console3.md` — device evidence for #4
