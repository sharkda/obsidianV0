# Current Project Context

Active focus across projects. Update at session END.

---

## Active project
**HootOwl** — SwiftUI iOS/macOS app for Taiwan urban mobility (real-time bus + parking).

> [!tip] Long-form reading lives in `projects/HootOwl/sessions/`
> This note stays short and current-state-only. Dated session briefings, investigations, and extended reasoning go in [[2026-08-17-status-reset|projects/HootOwl/sessions/]] — append-only, never edited after the fact. Most recent: [[2026-08-17-status-reset]].

## State (session 2026-08-20 — #5 applied; battery shortlist closed)

**First code change since 2026-07-03.** #5 (`CLLocationManager` dedupe) applied to the working tree — one line deleted from `wire0()` in `Municipal.swift`, plus a WHY comment. The app now creates exactly one `CLLocationManager`. **Not committed and not compile-verified** — build it in Xcode before trusting it; the CLI can't build this project (gitignored `Package.resolved` → SPM tries to re-resolve `ConcaveHull` over the network). Detail + caveat in [[battery]], atomic entry in [[decisions#2026-08-20-cllocationmanager-dedupe-battery-5]].

**That closes the pre-release battery shortlist.** All five picks (#1, #6, #9, #2+#3, #5) are implemented. Nothing left to *build*; what remains is verification — the owed Phase 3 device test and the deferred, still-confounded Energy Impact measurement.

**Also logged:** `CLAUDE.md` / `AGENTS.md` claim `MncplParkItem` IDs carry `tpe_`/`ntpc_` prefixes. **No code does this** — the helper has zero callers. That doc line is what seeded the 2026-08-07 "unverified assumption" scare. New entry in [[bugs]]; the instruction files are Jim's to correct.

**Previous state (2026-08-17 status reset)** — HEAD `860f82d` (2026-07-03), tree otherwise clean; every code claim in the vault re-grepped against source and all held.

This session verified the vault a level deeper than 2026-08-13: each battery and Cyclops claim was checked against the working tree source, not only against commit history. **Everything held** — see the table in [[battery#re-verification--2026-08-17]]. Full briefing: [[2026-08-17-status-reset]].

**One real advance: the `parkId` gate is cleared.** The check that was blocking the whole Cyclops plan was run. Neither side of `CyclopsModel.swift:112` carries a `tpe_`/`ntpc_` prefix — the prefix helper (`MunicipalEnum.swift:44–48`) has **zero callers**, and both `MncplParkItemAvail.parkId` and `MncplParkItem.id` pass raw feed IDs straight through. Raw-to-raw, no mismatch. **The plan does not reorder; Finding 1 is still the main cause.** The only gate left before the two one-line fixes is the device run. Residual to eyeball there: the `TPE####` hardcoded watchList seeds (`MncplAllScreen.swift:47`).

Small corrections applied to [[bugs]] (2 stale entries), [[battery]] (#1's line ref `:163` → `:172`), [[cyclops-first-run]] (assumption cleared). **#5's target lines `Municipal.swift:127` + `:169` re-verified exact — unchanged.**

**Everything below is carried forward from the 2026-08-07 → 08-13 sessions and is still accurate.**

> [!abstract] Previous session (2026-08-07 → 08-08)
> No code changes either. Investigation + documentation: traced the Cyclops 🕐 bug to root cause, found two further bugs on the way, corrected stale status across the vault. Produced [[cyclops-first-run]] (new), plus updates to [[bugs]], [[battery]], [[decisions]] (3 entries), [[swift-patterns]] (2 patterns).

> [!info] Corrected 2026-08-07
> The previous version of this note (2026-07-12) said Phase 3 was *"implemented, still uncommitted, awaiting device test"* and gave #5's target as `Municipal.swift:122` + `:160`. Both were wrong. Verified against `git log`:
> - **Phase 3 is committed** — `aa6b02a` (2026-06-26), including `Municipal+Lifecycle.swift` and the `project.pbxproj` target-membership fix.
> - **Last commit is `860f82d`** (2026-07-03), not `61eec92`.
> - **#5's target is now `Municipal.swift:127` + `:169`** — the file shifted.
>
> **Working tree is clean** apart from an untracked `AGENTS.md`. Repo has been idle since 2026-07-03.

**All four pre-release battery picks (#1, #6, #9, #2+#3) are implemented and committed.** Only #5 (trivial `CLLocationManager` dedupe) remains from the shortlist, plus the deferred post-launch measurement.

**Phase 3 was committed without the device test.** Not a blocker anymore (it's in), but the behaviour is still unverified: background/foreground refresh, lock/unlock no-thrash, `.inactive` no-op, app-switcher resume.

**Onboarding copy** — drafted in [[onboarding]] (3 screens, parking-only, owl-mascot voice, no app name, freshness-honest) plus a compliant ratings loop. **Copy only — no code yet.** `hootowl/UI/onboard/` is still the 2024 scaffolding (`LandingScreen.swift`, `OnboardScreen.swift`, `OnboardTab0.swift`, `UserGuide.swift`). Decision: [[decisions#2026-07-12-onboarding-copy--feedback--ratings-strategy]].

Commit chain:
- `860f82d` 2026-07-03 — 4-line touch to `OnboardScreen.swift`. **← HEAD**
- `aa6b02a` 2026-06-26 — Phase 3 (#2+#3) scenePhase pause/resume + target-membership fix.
- `61eec92` 2026-06-24 — Phase 2 (Layer B1) disk cache.
- `2d5eb13` 2026-06-23 — sync (post Phase 1b).
- `392fa82` 2026-06-18 — sync (post Phase 1b initial work).
- `04e2165` 2026-06-16 — #9 / macOS auth split / dead-code cleanup.
- `837cbef` 2026-06-15 — #1 + #6 + cleanup waves.
- `08c5816` 2026-06-13 — first cleanup wave (Obs-framework dedup).

## Where we are in the battery partition plan

Full plan + status lives in [[battery]]. Quick map:

| Phase | What | Status |
|---|---|---|
| #1 — GPS Best → HundredMeters | mechanical at 5 sites (reduced to 1 by cleanup) | ✓ committed `837cbef` |
| #6 — Timer.publish tolerance | 5 active sites + cleanup waves | ✓ committed `837cbef` |
| #9 — Drop Always-auth + Info.plist cleanup | iOS escalation removed, macOS preserved | ✓ committed `04e2165` |
| 1 (Layer A) — Cyclops state → Municipal singleton | `Municipal+Cyclops.swift`; thin view | ✓ committed |
| 2 (Layer B1) — Disk cache for cold-launch / jettison | `Municipal+Cache.swift`, 24h stale threshold | ✓ committed `61eec92` |
| 3 (#2 + #3) — scenePhase handler | pause GPS + proto timers on `.background`, resume + immediate `minuteFlow()` on `.active` | ✓ **committed `aa6b02a`** (device test still owed) |
| 4 (Layer B2) — Cyclops trail history persistence | optional / deferrable | not started |
| 5 — Dedupe `CLLocationManager` at `Municipal.swift:127` + `:169` | delete the `:169` assignment, keep the config lines | not started |

## Cyclops 🕐 bug — investigated 2026-08-07, no code changed

Jim's backlog item 2026-06-29 ("cyclops keeps the clock forever until kill and restart") was traced. Full write-up: [[cyclops-first-run]]. Summary:

- **Not a first-run bug.** The 🕐 opens on any launch without a usable cache — including **cache older than 24h**, which is routine for episodic parking use.
- **Main cause:** `activate()` starts a 15s timer but fires no immediate fetch, while `resumePolling()` does (`Mu1Base+Ext.swift:78`). Cache-less launch = **≥16s of clocks, guaranteed**. Relaunch looks instant because `seedFromCache()` fills `parkAvPack` synchronously in `Municipal.init`.
- **Two more bugs found:** `Municipal+Ext.swift:135` sends enclosing fences to `allFencesVbj` instead of `activeFencesVbj` (destructively narrows the fence list, unrecoverable without relaunch); and the fence→activation link (`ActDeActOnes`) was never wired, so every proto polls for every user regardless of location.
- **Still unproven:** the ≥16s window is certain; *"forever"* is not. Needs one fresh-install device run.

Fix sequencing was made an explicit decision (verify assumption → device run → then edit): [[decisions#2026-08-07-cyclops-fix-sequencing-verify-assumption-device-run-before-any-edit]]. Fence-driven activation logged as an open design decision, deliberately not patched: [[decisions#2026-08-07-fence-driven-zone-activation-is-an-open-design-decision-not-a-patch]]. Two reusable patterns extracted: [[swift-patterns#starting-a-poller-must-also-fire-one-immediate-fetch]] and [[swift-patterns#combine-send-to-the-subject-you-meant-especially-in-cold-start-branches]].

## Open bugs

- [[bugs]] 2026-08-07 — Cyclops 🕐 on cache-less launch. Open, investigated, not fixed.
- [[bugs]] 2026-06-15 — IME blocks UI on All-screen search. Open, deferred.

## Next steps (when Jim resumes)

**Recommended first move (updated 2026-08-20):** #5 is applied and the `parkId` grep is done, so **one device sitting now clears everything that's outstanding** — fresh install, run the Cyclops 🕐 checklist and the owed Phase 3 checklist together, and build #5 in Xcode while you're there. After that the only open item is the activation-policy design decision.

**Cyclops bug (Jim is reviewing the code himself before any edit):**
- [x] ~~Verify the unchecked assumption first~~ — **done 2026-08-17, cleared.** Neither side is prefixed; the `tpe_`/`ntpc_` helper has zero callers. No mismatch, plan unchanged. See [[2026-08-17-status-reset]].
- [ ] One fresh-install device run — does the clock clear after ~15–20s or never? Capture `🐎 minutelyAvailable`, `📦 minutely Received`, `📛 <512bytes`, `previousHash not changed`.
- [ ] Then apply: immediate `minuteFlow()` in `activate()` (one line) + `allFencesVbj.send` → `activeFencesVbj.send` (one word).
- [ ] Decide fence-driven activation policy — design decision, log in [[decisions]], don't patch blind.

**Battery — shortlist now fully implemented; only verification left:**
- [x] ~~#5 dedupe at `Municipal.swift:127` + `:169`~~ — **done 2026-08-20.** Working tree, **not committed, not compile-verified** (see below). Decision: [[decisions#2026-08-20-cllocationmanager-dedupe-battery-5]].
- [ ] **Build once in Xcode** to confirm #5 compiles. CLI `xcodebuild` can't run here — `Package.resolved` is gitignored so SPM re-resolves `ConcaveHull` from the network and fails. Pre-existing, unrelated to the edit.
- [ ] Device-test Phase 3 behaviour (already committed, still unverified).
- [ ] Post-launch Energy Impact measurement — **control for the unconditional all-zone polling first**, or the reading is confounded. See the warning in [[battery]].

**Onboarding (see [[onboarding]] for full TODO):**
- [ ] Jim to pick the final screen-1 headline lane (currently playful owl).
- [ ] Produce `Localizable.xcstrings` batch (English filled, 中文 blank). Note: `hootowl/Localizable.xcstrings` already exists.
- [ ] Wire strings into `LandingScreen` (ob0) + build out `ob1`/`ob2`.
- [ ] Decide feedback transport (mailto first vs. hosted form); implement `requestReview` win-moment trigger + Settings "Request a city" / "Rate the app".

## Open questions / blockers
- None blocking. Cyclops fix is paused on Jim's own code review + one device run. Onboarding needs Jim's headline pick and a go-ahead to produce the xcstrings batch.
