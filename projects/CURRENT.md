# Current Project Context

**HootOwl / Find Parking TW**: an iOS SwiftUI app showing live parking for Taipei and New Taipei City. Heading for **GM 1.0**.

> [!info] This note is current state only. **Replace it, don't append to it.**
> What happened before lives in the dated session notes and in [[CURRENT-log-to-2026-11-04]]. Upkeep rules: [[working-agreements#Vault upkeep]].

*Last updated 2026-11-19, before Jim's macOS upgrade.*

## Where things stand

- **App repo:** `main` = `origin/main` = `024c197`. Nothing uncommitted. Build 5.
- **Jim is making the App Store media** (R-10, R-21): Release on the iPhone 18 Pro Max simulator, 繁體中文, scripts in `~/Movies/HootOwl-preview/`. → [[2026-11-19]]
- **Fixed this session:** the `span` label shipping to users · the legacy receipt check revoking paid subscriptions · the map pulsing zoom while moving. → [[bugs]]
- **Open, triage for 1.0:** DestinationBar does not refresh when a location fix arrives. → [[bugs]]
- **Toolchain:** Xcode 27.2 (27B51). **Jim is upgrading macOS now**, so every "it builds" claim expires: rebuild and run. `xcode-select` points at CommandLineTools; use `DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer`.
- **Purchases on device:** Xcode's StoreKit test certificate fails as expired; use Apple sandbox. Re-check after the upgrade.

## Next, for Claude

1. **After the OS upgrade:** build Debug and Release, run on the simulator, re-check the StoreKit test certificate.
2. **DestinationBar refresh bug:** fix or defer, Jim decides.
3. **E-03:** why `TpeParkDescInfo.json` is missing from the iOS bundle (the log still says so every launch).
4. **C2:** the feed-shape detector. **Overdue:** re-check [[data-sources]].
5. **Weekly vault routine:** create it once Jim installs the Claude GitHub app on both repos.

## Where to look

| Question | Note |
|---|---|
| What do I (Jim) have to do? | [[jim-actions]] |
| What ships in 1.0 / 1.1 / 1.2+? Every open ID | [[release-plan]] |
| What happened last session? | [[2026-11-19]] |
| Which note answers which question? | [[INDEX]] |
| New machine, or how we work? | [[working-agreements]] |
| Why did we decide X? Known bugs? | [[decisions]] · [[bugs]] |
