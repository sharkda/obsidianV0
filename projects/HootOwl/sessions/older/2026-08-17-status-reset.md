# 2026-08-17 — Status reset

**Project:** HootOwl
**Repo state at open:** HEAD `860f82d` (2026-07-03). Working tree clean apart from untracked `AGENTS.md`.
**Code changed this session:** none. Read-only verification + vault corrections.

> [!note] What this note is
> A dated snapshot, written because Jim asked to "reset" on the bug-report progress after a break. Accurate for 2026-08-17, never edited afterward. Canonical current state lives in [[CURRENT]]; per-topic detail in [[battery]], [[cyclops-first-run]], [[bugs]], [[decisions]], [[onboarding]].

---

## Headline

**The vault was already in good shape.** The 2026-08-07 reconciliation and the [[2026-08-13-session-start]] briefing both still hold. The repo has now been idle for **~6 weeks** (last commit 2026-07-03), so there was very little room for drift — and what drift existed was in *old dated entries*, not in the current-state notes.

This session went one step further than 2026-08-13: instead of checking the vault against `git log` alone, every substantive code claim was re-grepped against the working tree. Results in [[battery#re-verification--2026-08-17]].

---

## Verification done

```
git log --oneline -1   →  860f82d Jul03
git status --short     →  ?? AGENTS.md
```

All battery claims re-checked in source (not just in commit messages) — see the table in [[battery#re-verification--2026-08-17]]. All three Cyclops findings re-confirmed present in the current code:

- `activate()` (`Mu1Base+Ext.swift:15`) still fires **no** immediate fetch — Finding 1 intact.
- `Municipal+Ext.swift:135` still `allFencesVbj.send(enclosing)` — Finding 2 intact.
- `ActDeActOnes` (`Municipal+Ext.swift:165`) still has **zero callers** — Finding 3 intact.

---

## The one substantive advance: the `parkId` gate is cleared

[[2026-08-13-session-start#what-i-d-do-next-and-why]] named this the cheapest real progress available — a grep, no device needed, which would either clear the assumption or reorder the whole Cyclops plan. **It was run this session. The plan does not reorder.**

The assumption as recorded was that `CyclopsModel.swift:112` compares `tpe_`/`ntpc_`-prefixed watchList IDs against a possibly-unprefixed `MncplParkItemAvail.parkId`. **The premise was wrong in an unexpected way: neither side is prefixed.**

- `String.municipalityFromPidPrefix` (`MunicipalEnum.swift:44–48`) is the *only* code that knows about `tpe_`/`ntpc_`, and it has **zero callers**. The convention is aspirational, not applied.
- `MncplParkItemAvail.parkId` ← raw feed IDs: `TaipeiObs.swift:59` (`parkId: $0.id`), `NewTaipeiCityObs.swift:62` (`parkId: fields[0]`).
- `MncplParkItem.id` ← `MncplParkItem.swift:173` passes `id: p0.id` straight through.

Raw-to-raw. No mismatch. **Finding 1 remains the main cause of the 🕐 bug**, and the next gate is now simply the device run.

**Residual to eyeball during that run:** the hardcoded watchList seeds `["TPE0080", "TPE0835", "TPE0270"]` (`MncplAllScreen.swift:47`, `AllTpeParkingScreen.swift:28`) use an uppercase `TPE####` shape matching neither the raw feed format nor the `tpe_` convention. Likely legacy defaults from the old all-Taipei screen. If a *default* pin never resolves while a *user-added* pin does, that's the explanation.

Static reading only — not device-verified.

---

## Vault corrections applied

Per the [[decisions#2026-08-07-vault-correction-convention-fix-forward-looking-status-preserve-dated-entries]] convention: forward-looking status corrected in place, dated entries preserved with a correction callout.

| Note | Was | Now |
|---|---|---|
| [[bugs]] 2026-06-09 (Taiwan address) | "fixed (working tree, not yet committed)" | committed `08c5816` (2026-06-13); stale for ~2 months |
| [[bugs]] 2026-07-12 (target membership) | narrative says file was orphaned until 2026-07-12 | git says it entered `project.pbxproj` fully target-linked in `aa6b02a` (2026-06-26); callout added, outcome unchanged |
| [[bugs]] / [[cyclops-first-run]] `parkId` assumption | flagged unverified, "could outrank everything" | checked and cleared, see above |
| [[battery]] #1 site | `Municipal.swift:163` | `Municipal.swift:172` (file shifted) |

**Not changed, because they were correct:** #5's target lines (`Municipal.swift:127` + `:169` — verified still exact), all four completed battery picks, the measurement confound callout, both open bugs.

---

## Backlog as it actually stands

Nothing here is new. Consolidated for the reset.

**Battery — 4 of 5 pre-release picks done and committed.**
- [ ] **#5** — dedupe `CLLocationManager` at `Municipal.swift:169` (delete the assignment, keep the config lines that follow). ~1 line, code-health not battery. The last pre-release item, and independent of everything else.
- [ ] **Phase 3 device test** — owed since `aa6b02a`. Background 30s → foreground refreshes; lock/unlock no thrash; `.inactive` tears nothing down; app-switcher resume.
- [ ] **Post-launch Energy Impact measurement** — deferred, and **confounded** until the all-zone polling question is settled.

**Cyclops 🕐 bug** — investigated, deliberately unpatched.
- [x] ~~Verify the `parkId` prefix assumption~~ — cleared 2026-08-17.
- [ ] One fresh-install device run: does the clock clear at ~15–20s, or never? Capture `🐎 minutelyAvailable`, `📦 minutely Received`, `📛 <512bytes`, `previousHash not changed`. **Combine with the Phase 3 test — same fresh install, both checklists.**
- [ ] Then the two one-liners: immediate `minuteFlow()` at the end of `activate()`; `allFencesVbj.send` → `activeFencesVbj.send`.
- [ ] Fence-driven activation policy — design decision, not a patch. Do not wire opportunistically; unsafe until Finding 2 is fixed.

**Onboarding** — copy exists, code does not.
- [ ] Jim picks the screen-1 headline lane.
- [ ] `Localizable.xcstrings` batch (English filled, 中文 blank).
- [ ] Wire into `LandingScreen` (ob0), build `ob1`/`ob2`.
- [ ] Feedback transport decision (mailto vs. hosted form) + `requestReview` win-moment trigger.

**Other open bug**
- [ ] [[bugs]] 2026-06-15 — IME blocks UI on All-screen search. Logged, never investigated. First step is reproduction: which input method, which dismiss gesture.

---

## Housekeeping note — vault path moved

`wrap.MD` in the repo (and the older MCP config it describes) still points at
`~/Library/Mobile Documents/com~apple~CloudDocs/obsidianV0`. **That path no longer exists.** The live vault is `/Users/jimhsu/obsidianV0`, which is what `~/.claude.json` correctly points to. The iCloud copy survives only as `…/CloudDocs/zzzobsidianV0` (the `zzz` prefix matching the repo's own deprecation convention).

The `obsidian-mcp` server also stalled again this session (`list-available-vaults` hung past 120s and was killed); these edits were made with direct file writes instead. The vault is a git repo, so the changes are diffable and revertable as usual.
