# 2026-09-10 — 18 commits pushed; where things stand

`origin/main` = **`53f21b2`**. Working tree clean, local and remote in sync.

## What landed

Eighteen commits since the last push, in four groups:

| Group | Commits |
|---|---|
| Subscribe reach | toolbar button on four screens, icon iterations, the white-circle fix, onboarding signpost with the glyph |
| 中文 | the 33-key draft, Jim's two review passes, the freshness line, 訂閱 over 課金 |
| Phones | extension now actually dials (`,,` not `;`), international dialling opt-in in Options → Advanced |
| Honesty fixes | the map screen's false "background nearby search" offer removed; subscription sheet localisation |

## Build status — better than the count suggests

Jim built and ran at **09:12 on 2026-09-10**, which covered everything through `016f852`. I confirmed by launching that build on the simulator, so those seventeen commits are **compile-verified and running**, not merely parse-checked.

Only **`53f21b2`** is unverified, and it edits `hootowl.storekit` — JSON test configuration with no compile surface.

## New capability worth remembering

`export DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer` makes `xcodebuild` and `simctl` usable from this session even though `xcode-select` points at CommandLineTools. It cannot build the project (ConcaveHull package resolution still fails), but it *can*:

- read a simulator's `AppleLanguages` / `AppleLocale` and per-app language overrides
- dump an **installed** bundle's compiled `.lproj/Localizable.strings`
- launch the app and take screenshots

That combination is what finally diagnosed the English-subscription-screen bug after two wrong guesses. Recorded in [[operations#3-building-and-testing]].

## Still owed

Nothing is blocked on code. The list is [[jim-actions]]; the largest items are the **app name** (still in the iOS permission dialog), a real **`support.email`**, **App Store Connect** (availability, Traditional Chinese product localisation, privacy labels, screenshots), and the open product question of **whether a subscription does anything except remove ads**.
