# Current Project Context

Active focus across projects. Update at session END.

---

## Active project
**HootOwl** — SwiftUI iOS/macOS app for Taiwan urban mobility (real-time bus + parking).

## State (2026-06-15)
Pre-release wrap-up. Shipping the current build to gather user feedback first, then circling back to optimization. **All pre-release working-tree work is now committed in `837cbef`** — bundle includes the Taiwan address-normalization fix, two battery picks (#1 GPS accuracy, #6 `Timer.publish` tolerance), and two cleanup waves (2026-06-13 + 2026-06-15) that deleted the Obs-framework duplicates and several `zz`/`zzz`/deprecated artifacts. Working tree clean.

## Battery — 2 of 5 pre-release picks taken, 3 still deferrable
Full investigation lives in [[battery]]. Status as of 2026-06-15:
- ~~**#1** GPS `kCLLocationAccuracyBest` → `HundredMeters`~~ ✓ done.
- ~~**#6** Add `tolerance` to every `Timer.publish`~~ ✓ done.
- **#9** Drop auto-escalation to `requestAlwaysAuthorization` + fix the misleading `NSLocationAlwaysAndWhenInUseUsageDescription` usage string (effort 1, impact 1 battery / 7 App Store review hygiene). Pre-release-friendly. Still open.
- **#2 + #3** A single `scenePhase` handler that stops GPS and cancels repeating timers on background (effort 2-3, impact 5-6). Still open.
- **#5** (newly eligible post-2026-06-13 cleanup) Dedupe redundant `self.locationMan = CLLocationManager()` in `Municipal.swift:122` + `:160`. ~1 line, code-health only. Still open.

Jim's call before shipping: take more, or defer the remaining to post-launch. See [[battery#sorted-shortlist-low-hanging-fruit-first]] for the full ranked table.

## Next steps
- [ ] Decide whether to take any of #9 / #2+#3 / #5 before shipping, or defer all.
- [ ] Final pre-release wrap-up (see `wrap.MD`).
- [ ] Ship.
- [ ] Post-launch: revisit [[battery]] starting from the **Verification step** (Xcode Energy Impact, 5 min idle) before any further code change.

## Open questions / blockers
- None blocking the release.
