# 2026-09-09 — Does the code back the onboarding privacy claim?

Jim asked whether the location line on onboarding screen 3 is actually true of the implementation:

> Turn on location and the closest lots come first. **Used only while the app is open — never in the background.**

**Answer: yes, and by more than one mechanism.** Six checks, all clean.

| # | Check | Result |
|---|---|---|
| 1 | Which authorization is requested | **iOS only ever calls `requestWhenInUseAuthorization()`.** Both `requestAlwaysAuthorization()` sites (`Municipal+Loc.swift:39`, `:84`) sit inside `#else` branches — macOS only |
| 2 | `Info.plist` (iOS) | **only** `NSLocationWhenInUseUsageDescription`. No Always key |
| 3 | `UIBackgroundModes` | **absent** — so iOS suspends the app on background regardless of intent |
| 4 | `allowsBackgroundLocationUpdates` / `pausesLocationUpdatesAutomatically` / `showsBackgroundLocationIndicator` | **never set anywhere** |
| 5 | Background-waking location APIs | **none.** No `startMonitoringSignificantLocationChanges`, no region monitoring, no visit monitoring |
| 6 | On backgrounding | `pauseForBackground()` calls **`stopUpdateLocation()`** outright (`Municipal+Lifecycle.swift:26`) |

## The one thing that looked like a problem and isn't

`NbsScreen.swift:501` constructs a **`CLCircularRegion`**, which is the type used for geofencing and would wake an app in the background:

```swift
let region = CLCircularRegion(center: biasCenter, radius: 100_000, identifier: "addr_bias")
… CLGeocoder().geocodeAddressString(normalized, in: region)
```

It is a **bias region for the geocoder**, not a monitored region — it narrows address lookup to a 100 km circle and is never handed to a `CLLocationManager`. No monitoring, no background wake. Worth writing down because the type name alone reads like a violation, and the next person to audit this will stop on the same line.

Likewise the app's own **"fences"** (`Municipal+Fence`) are plain coordinate maths, not CoreLocation region monitoring.

## So the claim is conservative

Three independent things would each have to change before location could run in the background: the authorization would have to escalate, `UIBackgroundModes` would have to be declared, and `pauseForBackground` would have to stop stopping GPS. The copy could honestly say more; it does not need to.

## Two caveats, neither affecting the claim

- **macOS does escalate to Always** (the `#else` branches, and the macOS target still declares Always usage strings in its build settings). It does not make the copy untrue, because **onboarding screen 3 never renders on macOS** — `AppScreen.destination` sends macOS to `LandingScreen` alone. The claim is not shown where it would be wrong.
- **The permission is requested automatically at launch**, from `handleAuthChange` on `.notDetermined`, which is a *timing* issue already logged — the dialog probably appears on screen 1 rather than screen 3. That affects whether the copy gets read before the prompt, not whether it is accurate.

## Useful beyond the copy

This is the evidence for the **privacy nutrition labels** in App Store Connect: location is precise, used for app functionality, foreground-only, and never used for tracking. See [[operations#c-app-store-submission]].


---

## Addendum — 2026-09-09: the audit checked the code, not the screens

Jim then spotted a banner on the map screen offering **"Enable Always for background nearby search"**. Every conclusion above still holds — the *code* never could run location in the background — but the app was **telling users otherwise**, and the audit did not catch it because it only looked at APIs and entitlements.

The banner was a leftover from before battery pick #9 removed the Always escalation, its Upgrade button was inert on iOS, and it had been shown to every iOS user permanently since June. Removed on iOS, kept on macOS where Always is genuinely required. Full record: [[bugs#2026-09-09-the-map-screen-offered-background-nearby-search-which-the-app-cannot-do]].

**Lesson for the next audit of this kind:** verifying that the code cannot do X is only half the job. Also grep the strings for anything that *claims* X — a privacy promise is broken by the copy just as effectively as by the implementation.
