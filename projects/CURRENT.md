# Current Project Context

**HootOwl / Find Parking TW**: an iOS SwiftUI app showing live parking for Taipei and New Taipei City. Heading for **GM 1.0**.

> [!info] This note is current state only. **Replace it, don't append to it.**
> What happened before lives in the dated session notes and in [[CURRENT-log-to-2026-11-04]] (the full log up to 2026-11-04, kept verbatim). Upkeep rules: [[working-agreements#Vault upkeep]].

*Last updated 2026-11-04.*

## Where things stand

- **Nothing in code blocks GM 1.0.** The remaining release work is Jim's: App Store Connect fields, screenshots, one device pass and TestFlight. → [[jim-actions]]
- **App repo:** `main` = `origin/main` = `1b83b72` (2026-11-01). **Uncommitted:** Jim's `CURRENT_PROJECT_VERSION 3 → 5` in `project.pbxproj`.
- **Settled 2026-11-03:** J5 (repo is private, so C2's cron runs every 30 min) · E-02 (ship on Xcode Organizer alone) · E-30 (actually done 2026-10-09) · R-02 is a paste, not a decision.
- **New 2026-11-04:** [[screenshots]] plans R-10. The App Store preview video is R-21, a 1.1 item.
- **Toolchain:** Xcode 27.0 / Swift 6.4, last re-verified 2026-10-08. If Xcode changes, every "it builds" claim expires. Build **and run** again.

## Next, for Claude

1. **Run C1 and D-02 on the simulator.** Both compile clean but have never been run.
2. **E-03:** find out why `TpeParkDescInfo.json` is missing from the iOS bundle.
3. **C2:** the feed-shape detector (a script plus a 30-minute cron). Unblocked.
4. **Overdue: re-check [[data-sources]]**. It was last checked 2026-09-09, due 2026-10-09. This is Claude's job.
5. **Translate the subscribed-state strings.** *You're subscribed*, *Manage subscription* and *Restore purchases* are still English.

## Where to look

| Question | Note |
|---|---|
| What do I (Jim) have to do? | [[jim-actions]] |
| What ships in 1.0 / 1.1 / 1.2+? Every open ID | [[release-plan]] |
| What happened last session? | [[2026-11-01]], the newest note in `HootOwl/sessions/` |
| Which note answers which question? | [[INDEX]] |
| New machine, or how we work? | [[working-agreements]] |
| How do I do X (Gist, release checklist, builds)? | [[operations]] |
| Why did we decide X? Known bugs? | [[decisions]] · [[bugs]] |
