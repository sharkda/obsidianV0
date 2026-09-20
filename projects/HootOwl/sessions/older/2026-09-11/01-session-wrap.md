# 2026-09-11→14 — Session wrap

**The session that tried to ship.** Ran across three dates as one continuous piece of work; kept in the 09-11 folder because splitting it would break the narrative. Started as "what should I tackle today", became the first real encounter with App Store Connect — and everything that encounter shook out.

👉 The briefing that opened it: [[00-resume-here]].

---

## What actually happened

The plan was to build the "no data here" empty state — the likeliest App Review rejection. **None of that got written.** Instead the first Archive was attempted, and it failed, and then it failed again, and each failure was a different species of problem that had been sitting in the repo invisibly.

That was a better use of the day than the plan was.

| | |
|---|---|
| **Three Release-only compile errors** | All in the `#else` half of an `#if DEBUG` — code that no Debug build had ever type-checked |
| **The app icon blocked the upload** | `ITMS-90717`; all 20 icons carried an alpha channel, and the 1024 was 26% genuinely transparent |
| **Then the icon was replaced** | And the replacement silently did nothing, because adding a `.icon` file does not make it the icon |
| **33 tracked `.DS_Store` files** | `.gitignore` never had a rule; deleting the icon folders churned three of them and made it visible |
| **The empty-state work** | Not started. Still the top recommendation |

## The theme, worth naming

**Everything found this session was invisible to the everyday build.**

Yesterday's theme was *"something that was true once and quietly stopped being true."* This one is narrower and sharper: **the tooling you use every day does not exercise the thing you are about to ship.**

- `#if DEBUG` / `#else` — Xcode compiles only the active half. The other half is real code, never type-checked, first compiled on the day you archive.
- The asset catalogue validates nothing about alpha until Apple's server rejects it.
- `ASSETCATALOG_COMPILER_APPICON_NAME` can point at a deleted concept while the new icon sits in the project looking correct.

None of these produce a warning. All three are found by **doing the real thing** — archiving, uploading, looking at a home screen. That is the same lesson as 2026-09-10's ("found by looking at the running app, not by reading code"), arrived at from a different direction, and it is now twice in three days.

**Operational consequence, already written into [[operations#2d-archiving-and-distributing--2026-09-11]]:** archive **early**, long before the app feels finished. Uploading is not submitting. A throwaway archive costs nothing and is the only thing that type-checks half your conditional code.

## The near-miss

The first attempt at fixing `debugForceAd` set it to `true` in the Release branch. The use site is `if showAd || debugForceAd`, so that would have **forced the ad banner on for every user, including paying subscribers** — breaking the one thing a subscription buys, and exactly what App Review checks when it subscribes in the sandbox.

It would have compiled. It would have shipped. **The compile errors were the lucky ones** — they announced themselves. This one only failed on inspection.

The second attempt guarded the *use sites* instead of the declaration, and missed the `.environment` line one row below the first. Now guarded at the declaration: one place to get right instead of every current and future reference. Pattern: [[swift-patterns#if-debug-else-means-half-your-code-is-never-type-checked]].

## The icon, start to finish

Three problems, only one of which blocked the upload:
1. **Alpha channel** → `ITMS-90717`, upload rejected.
2. **It drew its own rounded corners**, with the ear tufts inside the corner-radius zone — iOS's squircle mask would have **clipped them** on every home screen.
3. **It had `yuchinghsu` written across it**, and it was an **owl** — the retired placeholder identity on an app now called `Find Parking TW` / `找車位`. The icon was the last surviving piece of that identity and the most visible surface the app has.

Fixing only (1) would have cleared the upload and shipped (2) and (3).

Replaced with `FindParkingTw.icon` via **Icon Composer** — right for an iOS-26-only app (Liquid Glass), and it **owns the mask**, which makes the clipping failure impossible by construction.

Then the second silent failure: the `.icon` was in the project, in both targets' Resources phase, visible in the navigator — **and was not the icon.** `ASSETCATALOG_COMPILER_APPICON_NAME` still said `AppIcon`. Nothing warns you. And the General tab's App Icon picker would not list the new file at all, despite everything being structurally correct; the build setting is a free-text field and typing the name works.

**The subject now has its own note: [[app-icon]]** — rules, wiring, workflow, verification commands, troubleshooting table. `operations` §2e is a two-line pointer at it so the content cannot drift in two places.

## Where the code is

**Branch `icon-replacement`, six commits, `main` untouched at `5048976`. Working tree clean.**

```
98f1253  Stop tracking .DS_Store
5eef4fc  Delete the legacy app icon sets
7ab9cf0  Adopt an Icon Composer icon and point both targets at it
eaf1acb  Strip the alpha channel from the legacy app icons
85e4a45  Fix three Release-only breakages that Debug never compiled
5048976  main
```

Deliberately structured so each commit reverts independently — the deletion in particular touches nothing else. A safety ref sits at `backup/icon-replacement-pre-fold`; delete it once the branch is merged.

> [!success] **Compile-verified 2026-09-14** — this caveat is now closed for iOS
> An Archive requires a successful **Release** build, and `hootowl 2026-9-14, 5.38 PM.xcarchive` was built two days after the last source change on this branch (`ContentView.swift`, 09-12 16:43). It carries `CFBundleIconName = FindParkingTw`, which exists **only** on `icon-replacement` — so it was built from the branch, in Release, successfully. **All three `#if DEBUG` fixes and the icon wiring are proven.**
> **Still unproven: the `hootmac` target.** An iOS archive says nothing about whether macOS compiles, and `hootmac` had its own icon set that now shares the `.icon` file.

## Next

1. **Confirm `hootmac` builds.** The only piece the 09-14 archive does not prove.
2. **Merge:** `git checkout main && git merge icon-replacement`, then `git branch -D backup/icon-replacement-pre-fold`.
3. **Upload.** Expect to burn build numbers; that is normal ([[operations#expect-to-burn-build-numbers]]). The `Upload Symbols Failed` warning is expected every time and can never be fixed — [[operations#the-upload-symbols-failed-warning--ignore-it-permanently]].
4. **Then the empty state** — still the highest-value remaining code task, and still the rejection I would bet on. The two design calls in [[00-resume-here]] are still unanswered.

## Loose ends
- **`.gitignore` line 88** reads `iOSInjectionProject/.derived-data-log-0CA5RPJ1` — two rules welded together, so the intended `iOSInjectionProject/` ignore does not work. Harmless unless InjectionForXcode is used. Not touched; changing ignore semantics unasked felt wrong.
- **The `Upload Symbols Failed` warning** for `GoogleMobileAds` will recur on **every** upload. It is not actionable: Google ships the SDK stripped, so no dSYM exists to include. Only ad-SDK crash frames lose symbolication; the app's own dSYM is fine (11 MB, UUID verified against the binary). **Do not** silence it by unchecking "Upload your app's symbols" — that discards symbolication for your own code too.
- **The two open product questions** are untouched: whether a subscription should do more than remove ads, and what a user sees when the feed is down.

## Related
[[00-resume-here]] · [[app-icon]] · [[bugs]] · [[decisions]] · [[jim-actions]] · [[operations]] · [[release-strategy]] · [[swift-patterns]]
