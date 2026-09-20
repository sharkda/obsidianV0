# HootOwl — App icon

**Everything about the app icon in one place.** Written 2026-09-11/12, after the icon blocked the first App Store Connect upload and then silently failed to take effect once replaced.

> [!important] Written for the version of you who has forgotten all of this
> The icon has bitten twice in two days, both times **silently** — once as a rejected upload, once as a file that was in the project but was not the icon. Neither failure said what was actually wrong. Read the **Rules** and the **Wiring** sections before touching anything.

Related: [[bugs#2026-09-11--app-icon-carried-an-alpha-channel-itms-90717-blocked-the-first-asc-upload]] · [[jim-actions]] · [[operations#2e-app-icons--2026-09-11]] · [[release-strategy]]

---

## Current state — 2026-09-12

| | |
|---|---|
| **New icon** | `hootowl/resources/FindParkingTw.icon` — made in Icon Composer, in the project, in both targets' Resources phase |
| **Is it the app's icon?** | ❌ **Not yet.** `ASSETCATALOG_COMPILER_APPICON_NAME` is still `AppIcon` in **all four** build configurations |
| **Old icon** | `hootowl/Assets.xcassets/AppIcon.appiconset` — 20 PNGs, **still the live icon**, alpha now stripped from the 13 iOS-referenced ones |
| **Safe to delete the old set?** | ❌ **Not until the wiring below is done and verified** |

---

## The rules — learn these once

### 1. The 1024 marketing icon must have **no alpha channel**

Not "opaque alpha" — **no alpha channel at all.** This is what produced `ITMS-90717` and killed the first upload:

> *Invalid large app icon. The large app icon in the asset catalog in "hootowl.app" can't be transparent or contain an alpha channel.*

**Check before every upload:**
```bash
sips -g hasAlpha hootowl/Assets.xcassets/AppIcon.appiconset/Icon1024.png
```
`hasAlpha: no` is the only acceptable answer.

**macOS is the opposite.** macOS icons are free-form and transparency is expected. The `mac`-idiom files in the old set (`Icon16/32/64/128/256/512`) **keep their alpha deliberately** — do not "fix" them.

**Icon Composer layers are also the opposite.** Per-layer transparency is *required* there — that is how layering works. The no-alpha rule applies **only** to the flattened PNG in the legacy appiconset flow. Do not carry this rule into Icon Composer or you will fight the tool.

### 2. iOS applies its **own** mask — never draw your own

iOS masks every app icon to its squircle. You do not get to supply the shape.

The old icon drew its own rounded corners **and** put the owl's ear tufts at the very top edge, inside the corner-radius zone. On a real home screen that gives **double-rounded corners and both tufts sliced off**. It was drawn as though it were the final shape.

**Rule: full-bleed art, no container shape, no rounded corners, keep anything that matters out of the corners.**

### 3. Adding a `.icon` file does **not** make it the icon

This is the one that cost an afternoon. Xcode happily accepts the `.icon` file, adds it to Resources, shows it in the navigator — and keeps building with the old appiconset. **Nothing warns you.** See **Wiring** below.

### 4. A validation failure at upload does not burn the build number

If the upload is rejected during validation, the build never reaches App Store Connect, so the number is still free. Retry the same one; bump only if ASC actually objects. See [[operations#2c-version-and-build-numbers]].

---

## Wiring — making a `.icon` actually take effect

Adding the file is step one of three. **All three, in this order.**

### Step 1 — point the build setting at it

**Xcode → select the target → General → *App Icons and Launch Screen* → App Icon → `FindParkingTw`.**

Do it for **both** the iOS and macOS targets. If macOS stays on `AppIcon`, the old set still has a live consumer and cannot be deleted.

> [!warning] **The dropdown may not list your `.icon` at all — this happened 2026-09-12**
> Jim's App Icon picker offered only `AppIcon`, with the new file nowhere in it. **Everything was structurally correct** — verified: proper `PBXGroup` (not a folder reference), file type `folder.iconcomposer.icon`, and present in **both** `hootowl` and `hootmac` Resources phases. The picker simply did not enumerate it.
>
> **Two cheap things to try first:** quit Xcode and reopen the project (the picker populates from Xcode's index, and a newly added file often will not appear until a reopen — the most likely cause), or click the `.icon` in the navigator and confirm both targets are ticked in the File Inspector.
>
> **If it still does not appear, ignore the picker.** `ASSETCATALOG_COMPILER_APPICON_NAME` is a **free-text build setting**, not a dropdown, and typing a value the picker never offered works fine:
>
> **Target → Build Settings → filter `All` + `Combined` → search `app icon` → "Primary App Icon Set Name" → type `FindParkingTw`** (no `.icon` extension). Repeat on the other target.
>
> The dropdown is a convenience. **The build setting is the truth.**

What this changes under the hood — the check that proves it worked:
```bash
grep -n "ASSETCATALOG_COMPILER_APPICON_NAME" hootowl.xcodeproj/project.pbxproj
```
- **Before:** `= AppIcon;` × 4 (iOS Debug/Release, macOS Debug/Release)
- **After:** `= FindParkingTw;` for the app-target configurations

> Prefer the Xcode dropdown to hand-editing `project.pbxproj`, especially with Xcode open — edits underneath a running Xcode fight each other. The vault's standing preference: [[swift-patterns#new-swift-file-must-be-added-to-target-membership]].

### Step 2 — build and **look at it**

Install and look at the actual home screen. Do not trust the navigator preview. The whole reason this note exists is that the project *looked* correct while building the wrong icon.

### Step 3 — only now, delete the old set

Delete **`hootowl/Assets.xcassets/AppIcon.appiconset`** and nothing else.

> ⚠️ **Do not delete `Assets.xcassets` itself.** `AccentColor` lives in it (`ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor`) and taking the whole catalogue would break the app's tint.

---

## Icon Composer — the workflow

`Xcode → Open Developer Tool → Icon Composer` (or `/Applications/Xcode.app/Contents/Applications/Icon Composer.app`). Confirmed present in **Xcode 26.6**.

**Why it is right for this app:** the deployment target is **iOS 26.0/26.1**, so *every* user gets Liquid Glass — a flat legacy PNG looks a generation old beside system icons. It also **owns the mask** (killing the clipping problem by construction) and generates **dark / tinted / clear** variants that would otherwise each be drawn by hand.

**Workflow:**
1. Design at **1024×1024**
2. **No rounded corners, no container shape**
3. Separate the art into **layers** — this is the point of the tool
4. Export layers as **SVG** (best) or transparent PNG
5. Drop into Icon Composer, preview light / dark / tinted / clear
6. Save as `FindParkingTw.icon`, add to the project, then **do the Wiring steps above**

### The simpler fallback, if Icon Composer is ever more trouble than it is worth

**Single Size**, available since Xcode 14: asset catalog → `AppIcon` → Attributes Inspector (⌥⌘4) → **App Icon: Single Size**. One **opaque** 1024×1024 PNG; Xcode derives every size at build. Removes the per-resolution chore but gives no Liquid Glass treatment.

---

## Open notes on the current `FindParkingTw.icon`

Neither blocks anything. Both are cheap to act on while the icon is still being worked.

**1. The blue gradient is dead config.** `icon.json` sets a background fill of `extended-srgb:0.00000,0.53333,1.00000` — blue — but the single layer `pinkEyes.001.png` is a **fully opaque pink square covering the whole canvas**. The gradient can never show. Either give the layer transparency where the background should come through, or the fill is just noise in the file.

**2. One layer is most of Icon Composer left on the table.** Depth, parallax and specular highlights are computed **between** layers. A single flat image gets the glass material but no separation — closer to a regular icon than an iOS 26 one. The art already separates naturally: **pink background / eye whites / pupils** as three layers would give real depth for a few minutes' work.

---

## Why the old icon was replaced — three problems, the alpha was the smallest

1. **The ear tufts would be clipped** by the iOS squircle mask (rule 2 above).
2. **It had `yuchinghsu` written across it** — a personal handle, on the App Store, in low-contrast pink-on-pink already illegible at 1024px and a smudge at 60px. Text in app icons rarely survives real sizes.
3. **It was an owl, and the owl is retired.** The app is `Find Parking TW` / `找車位`. The mascot was deliberately dropped from the onboarding voice ([[project-app-name-placeholder]]) and three stale names were cleared from the strings on 2026-09-10. **The icon was the last surviving piece of the placeholder identity — and the most visible surface there is.** Someone browsing the App Store for parking saw a pink owl.

The replacement fixes all three: full-bleed, opaque, no text, no owl silhouette to clip.

---

## What was done to the old icons on 2026-09-11

All 20 PNGs carried an alpha channel, and `Icon1024.png` was **genuinely transparent** — 26.01% of pixels fully transparent, 25,127 partial, all four corners `rgba(0,0,0,0)`.

Flattened onto **white** (art unchanged, alpha channel dropped) for the 13 icons referenced by the `iphone` / `ipad` / `ios-marketing` idioms:

`Icon1024 · Icon180 · Icon167 · Icon152 · Icon120 · Icon87 · Icon80 · Icon76 · Icon60 · Icon58 · Icon40 · Icon29 · Icon20`

Done with a CoreGraphics Swift script using `CGImageAlphaInfo.noneSkipLast`, so the written PNG has **no alpha channel** rather than an opaque one — `sips` reports `hasAlpha: no`, which is what the validator checks. The script is reproducible; the approach matters more than the file.

**If the new icon lands and the old set is deleted, all of this becomes history** — kept because the *rules* it taught still apply to whatever replaces it.

---

## Verification — copy-paste before any upload

```bash
cd /Users/jimhsu/developer/farms/hootowl

# 1. Which icon is the build actually using?
grep -n "ASSETCATALOG_COMPILER_APPICON_NAME" hootowl.xcodeproj/project.pbxproj

# 2. If still on the legacy set: is the marketing icon opaque?
sips -g hasAlpha hootowl/Assets.xcassets/AppIcon.appiconset/Icon1024.png

# 3. Every icon at once
cd hootowl/Assets.xcassets/AppIcon.appiconset && \
  for f in *.png; do printf "%-16s " "$f"; \
  sips -g pixelWidth -g hasAlpha "$f" 2>/dev/null | \
  awk -F': ' '/pixelWidth|hasAlpha/{printf "%s ", $2}'; echo; done
```

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `ITMS-90717` on upload | 1024 icon has an alpha channel | Flatten it; see Rules 1 |
| New `.icon` added but the old icon still appears | `ASSETCATALOG_COMPILER_APPICON_NAME` still points at `AppIcon` | Wiring step 1 |
| Icon corners look doubly rounded; edges clipped | Art draws its own shape inside iOS's mask | Rule 2 — redraw full-bleed |
| App tint colour breaks after deleting icons | Deleted `Assets.xcassets` instead of just `AppIcon.appiconset` | Restore the catalogue; `AccentColor` lives there |
| macOS icon looks wrong after an alpha fix | macOS icons are *meant* to be transparent | Leave `mac`-idiom files alone |
| Icon Composer output looks flat | Single layer — no depth to compute | Split into layers |

---

## Related
[[bugs]] · [[jim-actions]] · [[operations]] · [[release-strategy]] · [[decisions]] · [[INDEX]]
