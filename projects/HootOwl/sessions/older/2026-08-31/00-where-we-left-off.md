# 2026-08-31 — Where we left off

**Session type:** context load + status verification. No code changed today.
**Repo:** `~/developer/farms/hootowl` · HEAD `860f82d` (2026-07-03) · branch `main`
**Last working session:** 2026-08-20 (11 days ago)

---

## TL;DR

Nothing is left to **build** before release. Everything outstanding is **verification** — and almost all of it collapses into **one device sitting plus one Xcode build**.

The battery shortlist is closed (all five picks implemented). The Cyclops 🕐 bug is traced to root cause with two one-line fixes drafted and gated behind a single device run. The `parkId` prefix assumption that was blocking the Cyclops plan was cleared by grep on 2026-08-17 and re-confirmed today.

---

## Working tree — verified today

```
 M hootowl/Municipalities/framework/Municipal.swift
?? AGENTS.md
```

The one modified file is **battery #5**, applied 2026-08-20 and still uncommitted:

```diff
     fileprivate func wire0(){
-        self.locationMan = CLLocationManager()
+        // battery #5: configure the instance built in init() rather than replacing it —
+        // a second CLLocationManager here silently discarded the first.
         self.locationMan.delegate = self
```

**Status: not committed, not compile-verified.** The CLI cannot build this project — `Package.resolved` is gitignored, so SPM tries to re-resolve `ConcaveHull` over the network and fails. Pre-existing since `dfa738f`, unrelated to this edit. It needs one build in Xcode.

---

## Re-verification run today

Every claim the vault makes about open work was re-grepped against the current source. **All held.**

| Claim | Check | Result |
|---|---|---|
| #5 applied — exactly one `CLLocationManager` in `Municipal` | `grep -rn "CLLocationManager()"` | ✓ one site, `Municipal.swift:127`. (`hootmac/MacOsClans.swift:34` is a separate macOS-only class, not part of the dedupe.) |
| Cyclops fix target 1 — `activate()` fires no immediate fetch | `Mu1Base+Ext.swift:15` vs `:73` | ✓ `activate()` and `resumePolling()` still diverge as documented |
| Cyclops fix target 2 — wrong subject in cold-start branch | `grep "allFencesVbj.send"` | ✓ still `Municipal+Ext.swift:135` — `allFencesVbj.send(enclosing)` |
| Measurement confound — fence→activation never wired | `grep "ActDeActOnes"` | ✓ **still zero callers** — only the definition at `Municipal+Ext.swift:165` |
| Residual watchList seeds | `grep "TPE0080"` | ✓ still hardcoded at `MncplAllScreen.swift:47` and `AllTpeParkingScreen.swift:28` |

Nothing drifted. The repo has been idle since 2026-07-03 apart from the uncommitted #5 edit.

---

## The four open threads

### 1. Battery — shortlist closed, verification owed

All five pre-release picks are in:

| # | What | Status |
|---|---|---|
| #1 | GPS Best → HundredMeters | ✓ committed `837cbef` |
| #6 | `Timer.publish` tolerance (5 sites) | ✓ committed `837cbef` |
| #9 | Drop Always-auth escalation + Info.plist cleanup | ✓ committed `04e2165` |
| #2+#3 | scenePhase pause/resume (Phase 3) | ✓ committed `aa6b02a` — **device test still owed** |
| #5 | `CLLocationManager` dedupe | ✓ working tree — **uncommitted, unbuilt** |

Two things owed, neither of them code:

- **Build #5 once in Xcode**, then commit.
- **Device-test Phase 3** — background/foreground refresh, lock/unlock no-thrash, `.inactive` no-op, app-switcher resume. It was committed without ever being run on device.

The post-launch **Energy Impact measurement stays deferred and stays confounded**: `ActDeActOnes` has zero callers, so every proto polls for every user regardless of location. Measuring before that is controlled gives a number that means nothing. See [[battery]].

> [!note] #5 is code-health, not a battery win
> The GPS chip is shared — two managers never drew double power. It's recorded under #5 because that's where the shortlist tracked it. The real value is removing the ambiguity about which manager the Phase 3 lifecycle calls act on.

### 2. Cyclops 🕐 — one device run from being fixable

Jim's backlog item from 2026-06-29 ("cyclops keeps the clock forever until kill and restart"). Full trace in [[cyclops-first-run]].

- **Not a first-run bug.** The 🕐 opens on *any* launch without usable cache — including cache older than 24h (`Municipal+Cache.swift:47`), which is routine for episodic parking use. A user who parks twice a week hits it every time.
- **Main cause:** `activate()` starts a 15s timer but fires no immediate fetch, while `resumePolling()` does (`Mu1Base+Ext.swift:73`). Cache-less launch = **≥16s of clocks, guaranteed.** Relaunch looks instant only because `seedFromCache()` fills `parkAvPack` synchronously in `Municipal.init`.
- **Two more bugs found in the trace:** `Municipal+Ext.swift:135` sends enclosing fences to `allFencesVbj` instead of `activeFencesVbj` (destructively narrows the fence list — unrecoverable without relaunch); and the fence→activation link was never wired.
- **Still unproven:** ≥16s is certain. *"Forever"* is not. That's exactly what the device run decides — it splits Finding 1 from the silent `minuteFlow` bail-outs at `Mu1Base+Ext.swift:144–177`.

**The gate:** the `parkId` prefix assumption is cleared (done 2026-08-17, re-confirmed today — raw-to-raw comparison, the `tpe_`/`ntpc_` helper has zero callers). The **only** gate left is the device run. Then two edits: one line in `activate()`, one word at `:135`.

Fence-driven activation policy remains a deliberate **open design decision** — not to be patched blind. See [[decisions#2026-08-07-fence-driven-zone-activation-is-an-open-design-decision-not-a-patch]].

### 3. Onboarding — copy written, no code

[[onboarding]] holds 3 screens of drafted copy (parking-only, owl-mascot voice, no app name, freshness-honest) plus a compliant ratings loop. `hootowl/UI/onboard/` is still the 2024 scaffolding. Waiting on:

- Jim to pick the final screen-1 headline lane (currently the playful owl).
- Go-ahead to produce the `Localizable.xcstrings` batch (English filled, 中文 blank).
- A decision on feedback transport — `mailto` first vs. hosted form.

### 4. Documentation trap — `CLAUDE.md` / `AGENTS.md`

Both files state `MncplParkItem` IDs are prefixed `tpe_` / `ntpc_`. **No code does this.** The helper (`MunicipalEnum.swift:44–48`) has zero callers. That doc line is what seeded the 2026-08-07 "unverified assumption" scare and cost a full investigation cycle.

These are Jim's instruction files, so the correction is his call. Suggested rewrite: *"IDs are raw source IDs; a `municipalityFromPidPrefix` helper exists but is unused."*

**Residual worth one glance during the device run:** the hardcoded seeds `["TPE0080","TPE0835","TPE0270"]` use an uppercase `TPE####` shape matching neither the raw feed format nor the `tpe_` convention. If a *default* pin never resolves while a *user-added* pin does, that's the explanation.

---

## Recommended next move

**One device sitting clears nearly everything.** Fresh install, then in a single pass:

1. Run the Cyclops 🕐 checklist — capture `🐎 minutelyAvailable`, `📦 minutely Received`, `📛 <512bytes`, `previousHash not changed`. Does the clock clear after ~15–20s, or never?
2. Run the owed Phase 3 checklist in the same session.
3. Eyeball whether the `TPE####` default pins resolve.
4. While you're in Xcode anyway — build, confirm #5 compiles, commit it.

After that the only genuinely open item is the fence-driven activation **policy decision**, which is a design call, not a task.

---

## Blockers

None. Everything is waiting on a device run and Jim's own review, not on missing information.
