# 2026-09-05/06 — Session wrap + RESUME HERE

**Written for a cold start.** If you are picking this project up after a restart, read this note and [[unfinished]] and you are current.

---

## Repo state — everything is committed and pushed

`origin/main` = `43ac0a0`. Working tree clean, local and remote in sync. Nothing is sitting unbuilt or uncommitted.

```
43ac0a0  Size three Cyclops cards for the layout they actually render in
881652b  Seed the Cyclops watch list from one place, with landmark defaults
c6e758f  Remove the Cyclops freshness diagnostics
0f863ed  Give the All-screen search keyboard a way out
14ceac7  Drive Cyclops cells from @State, not @Observable tracking
4f6dfd2  CyclopsView takes its item by value, not as a read-only @Binding
b069eb2  Track availability freshness by "last confirmed", not "last changed"
f069086  Aug31a   ← where the server was on 2026-09-04 morning
```

Leftover branch `cyclops-freshness` is merged and redundant: `git branch -d cyclops-freshness`.

> **The CLI cannot build this project** — `Package.resolved` is gitignored, so SPM tries to re-resolve `ConcaveHull` over the network and fails. All verification is Jim building in Xcode. Plan around that: prefer one well-instrumented run over several speculative fixes, because every iteration costs Jim a manual build.

---

## What this stretch of work actually was

**The Cyclops "grey numbers" arc is closed.** It was never a colour bug. Cyclops parking numbers had not been updating for a long time, and nobody could see it, because *a stale parking number is indistinguishable from a quiet car park*. Attaching a freshness clock made the invisible failure loud — a frozen timestamp ages on its own and eventually trips a threshold.

Four bugs came out of it. One was mine (in the new feature), three were pre-existing:

| # | Bug | Commit |
|---|---|---|
| 1 | Freshness read `converted` ("last **changed**") instead of a "last **confirmed**" clock | `b069eb2` |
| 2 | `CyclopsView` held a read-only `@Binding`, suppressing child re-renders | `4f6dfd2` |
| 3 | `minuteFlow()` published into `@Observable` state from a background thread | `b069eb2` |
| 4 | `@Observable` invalidation never reaches `MncplCyclopsScreen` **on device** | `14ceac7` |

Then, after that: the All-screen **keyboard trap** (open since 2026-06-15), the **fresh-install watch-list disagreement**, and the **three-card layout** off-by-one.

**#4's cause is still unexplained.** `14ceac7` routes around it with an explicit `@State` + `uiKickSbj` path; it does not answer why SwiftUI drops the invalidation. **Three screens now carry the same workaround** (`MncpltOne`, `MncplCyclopsScreen0000`, `MncplCyclopsScreen`), so it is structural, not incidental. `AppTabView`'s dynamic `ForEach` + auto-hide tab bar is the prime suspect. Worth its own session; not blocking anything.

---

## Next, in priority order

### 1. Onboarding — **the only release blocker**
Everything else outstanding is verification or hygiene. This is the last feature work.

**Decided (2026-09-05):** lane 3, blunt/utilitarian, with Cyclops promoted to its own screen. Copy is final and sits at the top of [[onboarding]] under "REVISED".

- [ ] **`Localizable.xcstrings` batch** — English filled, 中文 blank. `hootowl/Localizable.xcstrings` already exists. *This is the natural next action and needs no decision from Jim.*
- [ ] Wire `LandingScreen` (ob0), build out ob1/ob2. `hootowl/UI/onboard/` is still 2024 scaffolding.
- [ ] **Decide feedback transport** for screen 1's "Tell us where to go next →". Undecided. Recommendation: `mailto:` for v1 — ships today, no infra, and migrating later does not change the copy.

### 2. Two device checklists, one sitting
Both keep being carried forward and would clear together:
- **Phase 3 lifecycle test** — committed `aa6b02a` (June 26), never run. Background/foreground refresh, lock/unlock no-thrash, `.inactive` no-op, app-switcher resume.
- **Cyclops 🕐 checklist** — does the clock clear after ~15–20 s on a cache-less launch, or never.

### 3. Before the next city is added
**Mark `Municipal` `@MainActor`.** No live bug — all four `fetch(...)` sinks hop to main correctly today. But that hop is a per-call-site convention with **zero enforcement**, and `minuteFlow()` already lost it once by copy-paste. Every new zone is another chance to repeat it. Reasoning and alternatives: [[00-why-municipal-should-be-mainactor]].

Full standing list: [[unfinished]] (13 open items).

---

## Decisions still waiting on Jim

1. **`.primary` vs literal white** for the 5–30 min freshness state. Spec said white; implemented as `.primary` so it isn't invisible on an unpinned light-mode device. One line in `AvailFreshness.heroColor`.
2. **Feedback transport** (above).
3. **`CLAUDE.md` / `AGENTS.md` park-ID prefix claim** — both state IDs are `tpe_`/`ntpc_` prefixed; no code does this, and it cost a full investigation cycle on 08-07. Jim's files to correct.

---

## Things I got wrong here, so they aren't re-derived

Recorded plainly because each cost real time:

- **Misread a log as confirmation.** I called logs3's `obsNow` resets proof the binding fix worked. They occurred at exactly two points — matching the two times Jim backgrounded the app. Forced re-renders, not observation. The reset *count* matched Jim's backgrounding count and I did not check.
- **Instrumented the wrong target.** Every `🎨`/`🖌`/`🏠` run was on the **simulator**, where the bug does not reproduce, while the bug lived on the **device**. Several "confirmations" were invalid because of it.
- **Shipped a fix with no signal of its own.** The `uiKick = UUID()` attempt had no log line, so "the fix failed" and "the build was stale" were indistinguishable until I added one.
- **`@State` writes only invalidate if `body` reads that state.** I wrote a counter the body never read, and documented the mistaken reasoning in the comment. The two screens that already had this workaround do it correctly via `.id("\\(pid)-\\(uiKick)")` — I had the right example in front of me.
- **Caused a 5-minute launch hang.** Lowering `Mu1Base+Ext`'s threshold to `1` enabled per-item `.debug` logging over ~1,750 lots on the launch path. Reverted; confirmed fixed 2026-09-05.
- **Two overstated claims, both retracted:** main-thread JSON parsing is *not* a hitch risk (measured 8–56 ms for 472 KB), and `SourceBase.swift:180` is *not* an unhopped fetch (it is the `fetch` definition; its call site hops fine).

Method that eventually worked, and the rule behind it: [[01-technique-instrument-dont-guess]].

---

## Working preferences reconfirmed this stretch

- **Long-form goes in the vault**, terminal stays a short pointer. Dated folder per session, created by default.
- **Direct file access for the vault** — never MCP. Reads stall too, not just writes.
- **Commits go straight to `main`** (solo repo; the 09-04 branch was unnecessary ceremony). Push only when asked.
- Jim invites **aggressive tidying** of legacy code when touching it — verbatim: *"I would like you to aggressive make thing tidy and clean from my spaghatis."*

## Related
- [[unfinished]] — the standing list, read this second
- [[02-session-wrap]] (09-04) — the previous day's wrap
- [[00-status-where-we-are]] — the four-bug ledger and the three failed fixes
- [[onboarding]] — final copy, ready to turn into strings
