# 2026-09-11/12 — Resume here

> Session ran across midnight; kept as one note because the work is continuous.

**Status: briefing written; a Release-only compile error and an upload-blocking icon fixed (both below); the recommended empty-state work not started.** If today ends without the work below being done, this note is the whole handoff — start tomorrow by reading it and nothing else.

Session START protocol was run: [[decisions]], [[bugs]], [[battery]], [[CURRENT]], [[swift-patterns]], plus [[jim-actions]] and [[01-session-wrap|sessions/2026-09-10/]].

---

## Where the repo actually is

`origin/main` = `5048976` ("Map pins fade as their data ages"). The app is named `Find Parking TW` / `找車位`, 中文 is complete across all 35 user-facing keys, export compliance is declared, and map pins fade with age.

**Working tree is not clean.** `hootowl.xcodeproj/project.pbxproj` is modified. Diffed and classified:
- The bulk is **Xcode re-sorting the `PBXBuildFile` entries** that were hand-added outside the IDE — moved into alphabetical position. Verified as a pure reorder: the removed and added line sets are identical apart from the item below. Nothing lost.
- One real change: **`MARKETING_VERSION` 0.5.2 → 1.0** on both targets. This matches what [[jim-actions]] already claims is current, so it reads as deliberate.

`hootowl/iAp/StoreObs.swift` is also modified now — the Release-only fix below.

**Action:** commit both before starting anything, so the next diff is clean. The `StoreObs` fix deserves its own commit; it is unrelated to the version bump.

## The correction to carry forward

[[CURRENT]] and the 2026-09-10 wrap both say **"nothing is blocked on code."** That is now stale. The gaps audit on 2026-09-10 added three 🔴 items that *are* code, and all three were re-verified against the source today as still unbuilt:

| Claim | How it was checked | Result |
|---|---|---|
| No "outside coverage" state | `grep -rn "ContentUnavailableView" --include="*.swift"` | **One hit only** — a leftover placeholder at `Backyard Birds/AppDetailColumn.swift:18` ("filled for LandingScreen"). Nothing real. |
| Nothing tells a user the feed is down | grep for user-facing error/empty strings across `hootowl/UI` + `hootowl/Municipalities` | No hits. Counts simply stay stale or empty. |
| Data sources are uncredited | grep for `政府資料開放` / `資料來源` / `attribution` / `data source` across `*.swift` + `*.xcstrings` | **Zero hits anywhere in the project.** |

So the honest statement is: *nothing is blocked on code **except** the empty-state work.*

---

## Fixed today — a Release-only compile error in `StoreObs.swift`

**Found by Jim building, not by reading code.** `hootowl/iAp/StoreObs.swift:270` called the `async` `revokeEntitlment(rcpVld0:)` with no `await` and no `Task`.

**Why it could not be called synchronously:** the enclosing context is a Combine `.sink(receiveValue:)` closure — synchronous, non-async, escaping. There is no way to make a sync call site await. The work has to be handed to a `Task` so the closure can return immediately. The other **nine** cases in the same `switch` already did exactly that; `.malformed21002` was the one that did not.

**The fix** — now identical to its siblings:

```swift
case .malformed21002:
#if DEBUG
    ffl("\(rcpVld0.detailedMessage!), not revoking in debug",.info)
#else
    ffl("\(rcpVld0.detailedMessage ?? "")")
    Task{
        await self.revokeEntitlment(rcpVld0: rcpVld0)
    }
#endif
```

**Why it stayed hidden until now — this is the part worth keeping.** The broken line lived in the `#else` half of a `#if DEBUG`. **A Debug build never compiles it.** It could only surface on a Release or Archive build — which is precisely the build being prepared for submission. The bug was written at some unknown earlier date and sat there through every Debug build since.

**Two adjacent things checked, both clean:**
- The `detailedMessage!` force-unwrap on the DEBUG side looks asymmetric beside the `?? ""` below it, but is safe — `detailedMessage` returns `nil` only from its `default:` case (`VerifyReactEnum.swift:41-60`), and inside `case .malformed21002` the value is always that case. Left alone.
- Every other `#else` branch in the app's own sources was scanned for the same class of breakage. **No other async call is missing a `Task`.** All ten `revokeEntitlment` call sites now match.

**Not compile-verified by me** — the CLI still cannot build this project (gitignored `Package.resolved` → SPM re-resolves `ConcaveHull` over the network). It needs an Xcode build, and specifically a **Release** one.

**The generalisable lesson, for [[swift-patterns]] if it recurs:** `#if DEBUG` / `#else` branches are real compiled code that the everyday build never type-checks. Half of every such pair is untested until the first Archive. This is the second time in two days that a bug was found by *running or building the real thing* rather than by reading source — same family as the three staleness bugs on 2026-09-10.

---

## The app icon — blocked the first upload, and should not ship as-is

**Upload to ASC failed** with `ITMS-90717`:

> *Invalid large app icon. The large app icon in the asset catalog in "hootowl.app" can't be transparent or contain an alpha channel.*

### What was actually wrong

Inspected every PNG in `hootowl/Assets.xcassets/AppIcon.appiconset` — **all 20 carried an alpha channel.** And `Icon1024.png` was not merely a 4-channel file with opaque alpha; it is **genuinely transparent**: 26.01% of pixels fully transparent, 25,127 partial, all four corners `rgba(0,0,0,0)`. The art is an owl shape floating on nothing.

### Fixed

Flattened onto **white**, art unchanged, alpha channel dropped, for the 13 icons referenced by the `iphone` / `ipad` / `ios-marketing` idioms:

`Icon1024 · Icon180 · Icon167 · Icon152 · Icon120 · Icon87 · Icon80 · Icon76 · Icon60 · Icon58 · Icon40 · Icon29 · Icon20`

Verified with `sips -g hasAlpha` — all now `no`. Done with a small CoreGraphics Swift script (`CGImageAlphaInfo.noneSkipLast`, so the written PNG has no alpha channel at all rather than an opaque one). Originals are in git.

**Deliberately left alone:** `Icon16 / 32 / 64 / 128 / 256 / 512` are referenced only by the `mac` idiom, and **macOS icons are supposed to be free-form with transparency**. Per [[feedback-ios-is-the-target]] macOS only has to compile. `Iconwatch.png` is referenced by nothing at all.

**Build number:** a validation failure at upload means the build never reached ASC, so `1` is almost certainly not burned. Retry as build 1; only bump if ASC says *"bundle version must be higher."*

### 🔴 But the icon should not ship — three problems, the alpha was the smallest

1. **iOS will clip the ear tufts.** iOS masks every app icon to its own squircle; the app does not get to supply the shape. This art has **rounded corners drawn into it** and the tufts sit at the very top edge, inside the corner-radius zone. Result on a home screen: double-rounded corners and both tufts sliced off. The art was drawn as though it were the final shape.
2. **It has `yuchinghsu` written across it** — a personal handle, on the App Store, in low-contrast pink-on-pink that is already mud at 1024px and will be a smudge at 60px. Text in app icons is rarely legible at real sizes.
3. **It is an owl, and the owl is retired.** The app is `Find Parking TW` / `找車位`. The mascot was deliberately dropped from the onboarding voice ([[project-app-name-placeholder]]) and three stale names were cleared out of the strings on 2026-09-10. **The icon is the last surviving piece of the placeholder identity — and the most visible surface there is.** Someone browsing the App Store for parking currently sees a pink owl.

**Status: Jim is making a new icon (started 2026-09-11).** Not code; a design decision. Does not block the archive — the flattened icons upload fine — but **does block submission**.

### ⚠️ The second silent failure — the `.icon` was added but was not the icon (2026-09-12)

Jim built `FindParkingTw.icon` in Icon Composer and added it to `hootowl/resources/`. It is in the project, in **both** targets' Resources phase, and visible in the navigator. **It was still not the app's icon.**

```
ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon    ← all four configurations
```

The `.icon` was being copied in as an inert resource while the old appiconset kept building. **Nothing warns you** — the project looks correct. Answering Jim's actual question ("do I remove the old icons?"): **no, and not yet** — deleting them at that moment would have shipped an app with no icon at all.

**Correct order:** set the build setting (Xcode → target → General → App Icons and Launch Screen → App Icon → `FindParkingTw`, **both** targets) → build and look at a real home screen → *then* delete `AppIcon.appiconset` only, never the whole `Assets.xcassets` (`AccentColor` lives there).

**The new icon is good on all three counts from yesterday:** 1024×1024, opaque, full-bleed, no `yuchinghsu`, no tufts for the mask to clip. Two optional notes — the blue `fill` gradient in `icon.json` is dead config (the single opaque layer covers the whole canvas), and one layer forfeits the depth/parallax that is the point of Icon Composer.

> **This is the second time in two days the icon failed silently** — once as a rejected upload, once as a file that was present but inert. That pattern is why the subject got its own note.

👉 **All of it now lives in [[app-icon]]** — rules, wiring, workflow, verification commands, troubleshooting table. `operations` §2e is a two-line pointer at it.

### How to make one icon instead of nineteen

The per-size set in this project is the **old** way and is why one bad file blocked an upload. Two modern paths, both removing the per-resolution chore:

**A. Single Size (simplest, ~30 seconds).** Since Xcode 14 an iOS app icon can be **one 1024×1024 PNG**. Select `AppIcon` in the asset catalog → Attributes Inspector (⌥⌘4) → **App Icon: Single Size**. Xcode generates every derived size at build time. Still must be **opaque**.

**B. Icon Composer — the right one for this app. ✅**

`/Applications/Xcode.app/Contents/Applications/Icon Composer.app` (also *Xcode → Open Developer Tool → Icon Composer*). Verified present in Xcode 26.6 on 2026-09-11.

Why it is the right choice here specifically:
- **The deployment target is iOS 26.0/26.1**, so **every** user gets Liquid Glass. A flat legacy PNG will look dated beside system apps.
- **It applies the mask itself and shows the safe area** — which is exactly problem 1 above. You stop drawing the shape and let the tool own it.
- **It generates dark, tinted and clear variants** that would otherwise each be drawn by hand.
- It covers macOS too, with that platform's own shape.

Workflow: design at **1024×1024** → **do not draw rounded corners or a container shape**; supply a full-bleed background layer plus foreground layers → keep key content inside the safe zone → export layers as **SVG** (best) or transparent PNG → drop into Icon Composer → preview light/dark/tinted/clear → save as `FindParkingTW.icon` → add to the project and set it as the target's icon.

> ⚠️ **Counterintuitive, so worth stating:** per-layer transparency is **expected and required** in the Icon Composer workflow. The no-alpha rule that caused today's rejection applies to the **flattened marketing PNG in the legacy appiconset flow only**. Do not carry today's lesson into the layer workflow.

---

## Recommended pick for today — the "no data here" state

**One sitting, three blockers.** They are the same view in three modes — *you are outside coverage* / *the feed is down* / *waiting for first fetch* — so building them separately would be waste.

Why this over everything else on [[jim-actions]]:

1. **It is the rejection to bet on.** App Review opens the app in **California**, sees an empty map with no explanation, and that reads as Guideline 2.1, *does not function*. Every other open item is a paperwork risk; this one is a **rejected build** risk. Reasoning already recorded in [[release-strategy#the-one-risk-i-would-bet-money-on]].
2. **It is the only remaining work that needs a session.** The Gist, App Store Connect, availability, age rating, screenshots — those are Jim's accounts and Jim's browser. They do not need me.
3. **It gates the device pass.** One device sitting is owed (Phase 3 lifecycle — never run since June, Cyclops 🕐 on a cache-less launch, the three-screen onboarding walk, ATT on 2nd launch, and now the new pin fade). Shipping the empty state *first* means that sitting exercises everything at once instead of requiring two.

**Attribution rides along** — one line on `OptionsScreen`, one string pair, same pass. It is licence compliance (政府資料開放授權條款-第1版 requires it), not App Review, but it is cheap here and expensive to remember later.

### Two calls owed from Jim before any code is written

1. **What does the outside-coverage screen offer?**
   - *Recommended:* honest + useful — name the two cities covered, and put the **"request a city"** path right there. It turns a dead end into the demand signal the ratings/feedback strategy wanted for city prioritisation ([[decisions#2026-07-12-onboarding-copy--feedback--ratings-strategy]]).
   - *Alternative:* a plain "not available in your area."
2. **How should feed-down read?**
   - *Recommended:* keep the last known numbers visible but **visibly stale**, with a banner. Reuses the freshness vocabulary already built (`AvailFreshness`, `Municipal.lastConfirmed`, the 5/30-minute thresholds).
   - *Alternative:* blank the screen — rejected in my view, it discards information the user may still find useful.

**Neither call was answered before this note was written.** Whoever picks this up tomorrow: ask these two first, do not guess.

---

## The first archive — decided today

**Question Jim asked:** does the first archive go to TestFlight internal only, or to App Store Connect?

**The question contains a false split.** There is only **one** upload destination — App Store Connect. TestFlight is not a separate archive target; it is one of two things you can do with a build that is *already* in ASC.

```
Archive → Organizer → Distribute App → App Store Connect → Upload
                              │
                     build processes (minutes–1hr)
                              │
              ┌───────────────┴───────────────┐
     TestFlight internal              attach to a version
     (no review, immediate)           → Submit for Review
```

Same binary, same upload, no re-archive in between.

**The reassurance worth remembering: uploading is not submitting.** Nothing reaches App Review until the build is explicitly attached to a version and Submit is pressed. A build that lands in ASC and sits there costs nothing and commits to nothing.

### ⚠️ The menu trap — pick the right distribution option

Xcode 26.6's *Distribute App* sheet contains **both** of these, and they are not the same:

| Option | What it means |
|---|---|
| **App Store Connect**<br>*"Distribute on TestFlight and the App Store."* | ✅ **Use this.** Uploads to ASC. Usable for internal TestFlight, external TestFlight, **and** App Store submission. |
| **TestFlight Internal Only** | ❌ Uploads a build **permanently locked** to internal testers. Can never go external, can never be submitted to the App Store. |

**"Internal only" is a decision about who receives the build — made in App Store Connect by not adding an external group — not a decision made at upload time.** Choosing *TestFlight Internal Only* means that if the build turns out to be good, it cannot be shipped; it would have to be re-archived as build 2 for no reason but the menu choice. That option is for knowingly-throwaway builds.

*(This corrects a loose phrase in my own first answer today, which said "internal TestFlight first" without distinguishing the channel from the upload option. Recorded because the mistake is easy to repeat.)*

### Recommendation: archive today, before the empty-state work

**Not to submit — to upload and let it sit.** Reasons in order:

1. **A Release-only compile error was found today by building** (`StoreObs.swift:270`, above). That is precisely the category an Archive exists to flush out, and **there may be more** — every `#if DEBUG` / `#else` pair in the project has a half that has never been type-checked.
2. **Xcode validates at upload** — icons, entitlements, the privacy manifest, the export-compliance key. Cheap now, annoying later.
3. **Processing takes up to an hour and metadata is a parallel track.** [[release-strategy#order-of-operations]] is blunt that this is where solo devs lose days.
4. **It does not block the empty state** — that ships in build 2.

### Mechanics to know before pressing it

- **Build numbers burn on upload.** Currently `MARKETING_VERSION 1.0`, build `1`. The moment build 1 is uploaded that number is gone forever, even if the build was garbage. Increment freely; it is a counter, not a statement.
- **Export compliance should now be silent** thanks to `ITSAppUsesNonExemptEncryption` (committed `5411f69`). **If ASC still asks on this upload, the key did not take** — worth knowing immediately.
- **Internal testers** must be ASC team members with Admin / App Manager / Developer / Marketing role, up to 100. Add yourself.
- **Not parallelizable:** the **first subscription group must be reviewed alongside an app version** ([[release-strategy]]). So the subscription's Traditional Chinese localisation in ASC — still open on [[jim-actions]] — is on the critical path for the real submission, though not for this upload.

### The sequence

1. Archive
2. Distribute App → **App Store Connect** → Upload
3. Wait for processing
4. ASC → TestFlight → add **yourself** as an internal tester → install
5. Metadata in parallel while it processes
6. Submission stays a separate, later, explicit decision

---

## The alternative, if Jim would rather not code today

Spend the sitting on the **App Store Connect block** instead — [[operations#2-release-checklist]] walked item by item. That block is: name + subtitle, availability set by hand (Taiwan / US / Japan / HK / Macau), the subscription's Traditional Chinese localisation, privacy nutrition labels, screenshots + description, and the age-rating questionnaire. All browser work, none of it blocked on anything.

## Not today

- **[[data-sources]] re-check** — not due until **2026-10-09**. Leave it.
- **The two open product questions** — whether a subscription should do more than remove ads, and the `−9` New Taipei lots. Both are product calls, neither blocks a submission.

## Related
[[jim-actions]] · [[release-strategy]] · [[operations]] · [[CURRENT]] · [[bugs]] · [[01-session-wrap|sessions/2026-09-10/]]
