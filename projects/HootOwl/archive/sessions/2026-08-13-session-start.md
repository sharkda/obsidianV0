# 2026-08-13 — Session start briefing

**Project:** HootOwl
**Repo state at open:** HEAD `860f82d` (2026-07-03). Working tree clean apart from untracked `AGENTS.md`.
**Code changed this session so far:** none.

> [!note] What this note is
> A dated, long-form briefing written at session start. It is a **snapshot**, not a status page — it is accurate for 2026-08-13 and is never edited afterward. The canonical current state stays in [[CURRENT]]; the per-topic detail stays in [[battery]], [[cyclops-first-run]], [[bugs]], [[decisions]], [[onboarding]]. See the folder convention at the bottom.

---

## Verification done at open

Read `decisions.md`, `bugs.md`, `battery.md`, `CURRENT.md`, `swift-patterns.md` per the session START protocol, then checked them against the repo:

```
git log --oneline -3   →  860f82d Jul03 / aa6b02a June26 / 61eec92 June24
git status --short     →  ?? AGENTS.md
```

**The vault matches reality.** The 2026-08-07 reconciliation held up — HEAD, the commit chain, and the clean-tree claim in [[CURRENT]] are all still correct. No drift to fix this time. The repo has been idle since 2026-07-03 (~6 weeks).

---

## Where the project actually stands

### Battery work — done, minus two loose ends

All four pre-release picks are implemented **and committed**. Worth stating plainly, because the vault previously mis-recorded two of them as uncommitted and that error cost a session:

| Pick | What | Commit |
|---|---|---|
| #1 | GPS `kCLLocationAccuracyBest` → `HundredMeters` | `837cbef` (2026-06-15) |
| #6 | `tolerance: interval * 0.1` on all 5 `Timer.publish` sites | `837cbef` (2026-06-15) |
| #9 | Drop iOS Always-auth escalation + `Info.plist` cleanup | `04e2165` (2026-06-16) |
| #2 + #3 | `scenePhase` pause/resume (Phase 3) | `aa6b02a` (2026-06-26) |

Two things remain, both small:

1. **#5 — dedupe `CLLocationManager`.** `Municipal.swift:127` assigns `self.locationMan = CLLocationManager()` (required before `super.init()` because the property is non-optional), then `wire0()` at `:169` discards it and builds a second. Fix: delete the `:169` assignment, keep the config lines that follow. ~1 line. This is code-health, not battery — the GPS chip is shared, so two managers do not draw double power.
2. **Phase 3 device test — still owed.** Phase 3 was committed *without* the manual test its own plan called for. Not a blocker (it's in and it compiles), but the behaviour is unverified: background 30s → foreground refreshes; lock/unlock does not thrash; `.inactive` tears nothing down; app-switcher resume works.

The post-launch Energy Impact measurement stays deferred — **and it is confounded until the zone-activation question below is settled.** See the warning callout in [[battery]].

### Cyclops 🕐 bug — traced to root cause, deliberately unpatched

Your 2026-06-29 backlog item ("cyclops keeps the clock forever until kill and restart") was investigated on 2026-08-07. Full trace in [[cyclops-first-run]]. Three findings:

**Finding 1 — the main cause, and it isn't a first-run bug.**
`activate()` (`Mu1Base+Ext.swift:15–49`) starts a 15s minutely timer but fires **no immediate fetch**. `resumePolling()` (`:78`), added later in Phase 3, *does*. So the two entry points into the same polling machinery disagree. On any launch without a usable cache, the first availability data arrives one full interval late — with `loadOnStart` activating protos at +1.2s, that is **≥16 seconds of clocks, guaranteed**.

Why it looked like a first-run bug: `seedFromCache()` fills `parkAvPack` synchronously in `Municipal.init` (`:133`) before `wireCyclops()` (`:134`), so a warm cache hides the dead air completely. But the cache expires at 24h (`Municipal+Cache.swift:47`) — and for episodic parking use (you open the app when you drive somewhere), **most sessions land on the cold path**. The bug is routine, not rare.

**Finding 2 — a latent landmine.**
`Municipal+Ext.swift:135`, in the cold-start branch of `assessFences`, sends the enclosing fences to `allFencesVbj` instead of `activeFencesVbj`. Since the value being sent was *derived from* `allFencesVbj.value`, this overwrites its own input and **destructively narrows the full fence list** — a user standing outside all fences collapses it to `[]`, after which every later `assessFences` throws `.noFences` permanently, unrecoverable without relaunch.

Harmless today because nothing reads `activeFencesVbj` for activation. It becomes a hard failure the moment activation goes fence-driven — i.e. it would surface as *"the new city doesn't work"* during multi-city expansion.

**Finding 3 — an unwired design intention, not a bug.**
`ActDeActOnes(ids:)` (`Municipal+Ext.swift:165–175`) has **zero callers**, and `activeIds` at `:158` is computed and thrown away. The fence→activation link its own comment promises was never wired. Every proto activates unconditionally via `loadedProtos.map({ $0.activate() })` at `:43`, so **a user in Taipei is continuously polling New Taipei City too**.

Cost is linear in cities — tolerable at two, meaningful at six, and it multiplies load on public open-data endpoints that may rate-limit. It also directly confounds the deferred battery measurement, since some of the drain being measured is zones the user isn't in.

### Why nothing was patched

You made the sequencing an explicit decision on 2026-08-07 ([[decisions#2026-08-07-cyclops-fix-sequencing-verify-assumption-device-run-before-any-edit]]), and the reasoning still holds: **the ≥16s window is proven by static reading; "forever" is not.** Shipping the one-line fix and closing the bug risks declaring victory over 16 seconds while an indefinite stall — a silent `minuteFlow()` bail-out at `Mu1Base+Ext.swift:144–177` — survives underneath it.

Two gates before any edit:

1. **Verify the unchecked assumption.** `CyclopsModel.swift:112` matches `$0.parkId == pid` against `tpe_`/`ntpc_`-prefixed watchList IDs. It was never confirmed that `MncplParkItemAvail.parkId` actually carries that prefix. If it doesn't, that is a **larger bug than all three findings above** and reorders the whole plan.
2. **One fresh-install device run.** Does the clock clear on its own at ~15–20s, or genuinely never? That single observation splits Finding 1 from the `minuteFlow` bail-outs. Capture the logs: `🐎 minutelyAvailable`, `📦 minutely Received`, `📛 <512bytes`, `previousHash not changed`.

Only then apply the two one-liners: immediate `minuteFlow()` at the end of `activate()`, and `allFencesVbj.send` → `activeFencesVbj.send`.

### Onboarding — copy exists, code does not

Three-screen flow drafted in [[onboarding]]: parking-only scope, owl-mascot voice, no app name baked in, freshness-honest wording, plus a ratings loop that decouples App Store reviews from feature requests. `hootowl/UI/onboard/` is still the 2024 scaffolding. Blocked on your headline pick for screen 1, then the `Localizable.xcstrings` batch.

### Other open bug

[[bugs]] 2026-06-15 — IME blocks the UI on the All-screen search; user gets stuck in the search field. Logged, deferred, **never investigated**. First step is still reproduction: which input method (注音 / 拼音 / handwriting / English) and which dismiss gesture fails.

---

## What I'd do next, and why

**Cheapest real progress: gate #1 above.** Confirming whether `MncplParkItemAvail.parkId` carries the `tpe_`/`ntpc_` prefix is a grep — a few minutes, no code touched, no device needed. It either clears the assumption or it reorders everything else. There is no reason to do the device run first, and no reason to touch code before it.

After that, the device run is the only thing standing between you and closing the 🕐 bug, and it can be combined in one sitting with the owed Phase 3 verification — same fresh install, both checklists.

**#5 is independent** of all of the above and can be done any time you want a two-minute win.

**Don't** wire fence-driven activation opportunistically. It changes which zones fetch for whom — a behavioural change with correctness, coverage, and battery consequences, and it's unsafe until Finding 2 is fixed. Open questions logged in [[decisions#2026-08-07-fence-driven-zone-activation-is-an-open-design-decision-not-a-patch]]: what activates a zone when location is unknown or denied, does a boundary user keep both zones warm, and is there a manual override for checking a destination city remotely.

---

## Folder convention (new, 2026-08-13)

`projects/HootOwl/sessions/` holds dated session notes, named `YYYY-MM-DD-<topic>.md`.

**Why the split:** [[CURRENT]] has to read as *current* — when it drifts it actively misleads the next session, which is precisely what happened before the 2026-08-07 reconciliation. Long-form narrative accumulating inside it is what makes it drift. Dated session notes are append-only history that is never wrong later, so they can be as long as they need to be.

This mirrors the convention already recorded in [[decisions#2026-08-07-vault-correction-convention-fix-forward-looking-status-preserve-dated-entries]]: correct forward-looking status in place, leave dated entries as written.

**Where things go:**
- **This folder** — session briefings, investigations, long-form reasoning. Dated, immutable.
- [[CURRENT]] — short, current-state-only. Overwritten as things change.
- [[battery]], [[onboarding]], [[cyclops-first-run]] — standalone topic notes, updated inline as work happens.
- [[decisions]] / [[bugs]] — atomic entries, newest at top.
