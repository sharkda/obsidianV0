# Current Project Context

Active focus across projects. Update at session END.

---

## Active project
**HootOwl** — SwiftUI iOS/macOS app for Taiwan urban mobility (real-time bus + parking).

## State (2026-06-11)
Pre-release wrap-up. Shipping the current build to gather user feedback first, then circling back to optimization. Battery is the largest known concern; investigation is **deferred to post-launch** but optional pre-ship low-hanging fruit is available.

## Working tree (uncommitted as of 2026-06-10)
- Taiwan address-normalization fix (`hootowl/Municipalities/Nbs/AddressSearchObs.swift`, `NbsScreen.swift`) — manual test of `北投區中央北路2段350巷66號` still owed before commit.
- Other modified: `hootowl.xcodeproj/project.pbxproj`, `hootowl/Localizable.xcstrings`, `wrap.MD`. Decide whether to bundle with the address fix or land as a separate pre-release commit.

## Battery — pre-release decision pending
Full investigation lives in [[battery]]. Ranked shortlist of pre-release picks (each effort ≤ 3, no architectural change, ~60 lines combined):
- **#1** GPS `kCLLocationAccuracyBest` → `HundredMeters` (effort 1, impact 9). Single biggest battery win in the codebase.
- **#6** Add `tolerance` to every `Timer.publish` (effort 1, impact 3). Free.
- **#9** Drop auto-escalation to `requestAlwaysAuthorization` + fix the misleading Info.plist usage string (effort 1, impact 1 battery / 7 App Store review hygiene). Pre-release-friendly.
- **#2 + #3** A single `scenePhase` handler that stops GPS and cancels repeating timers on background (effort 2-3, impact 5-6).

Jim's call before shipping: take some/all, or defer all to post-launch. See [[battery#sorted-shortlist-low-hanging-fruit-first]] for the full ranked table.

## Next steps
- [ ] Verify the address-search fix in simulator (`北投區中央北路2段350巷66號`).
- [ ] Decide which pre-ship battery picks to take (or defer all).
- [ ] Commit the address-search fix (+ any chosen battery picks).
- [ ] Pre-release wrap-up (see `wrap.MD` in the working tree).
- [ ] Ship.
- [ ] Post-launch: revisit [[battery]] starting from the **Verification step** (Xcode Energy Impact, 5 min idle) before any further code change.

## Open questions / blockers
- None blocking the release.
