# E-28 — Terms of Use, and the dead screen that wasn't

**Commit `327bf08`.** Four files, all four configurations build, strings verified in the bundle.

---

## What Guideline 3.1.2 was actually missing

Both subscription screens set:

```swift
.storeButton(.visible, for: .restorePurchases, .policies, .signIn, .cancellation)
```

`.policies` advertises **two** policy buttons. Only one destination was ever supplied — `grep -rn "termsOfService"` across the project returned **nothing**. So the sheet offered a terms affordance with nothing behind it.

## Why Apple's standard EULA, rather than writing one

The app ships no terms of its own. Absent a custom EULA, **Apple's standard EULA is the agreement that actually governs the subscription** — so linking it is not a shortcut, it is the correct target. One constant to change if a custom page is ever written:

```swift
enum LegalLink {
    static let privacyPolicy = URL(string: "https://jimhsuyc.wixsite.com/tataro/privacy-policy")!
    static let termsOfUse    = URL(string: "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/")!
}
```

Deliberately **not** the privacy-policy page. That page claimed terms were *"accessible at bopomofo"* — a page that does not exist — and the sentence was deleted on 09-18 rather than pointed somewhere, precisely because this constant is the real answer.

## Two things found while wiring it

### 1. `SubscriptionStoreScreen` is not unreferenced — and that mattered

[[unfinished]] has said since **2026-09-08** that `EntitledView.swift` and `SubscriptionStoreScreen` are unreferenced. For `SubscriptionStoreScreen` that is **wrong**, and the path is not obscure:

```
AppScreen.swift:89  MncplCyclopsScreen()
  → MncplCyclopsScreen.swift:58  toolbar0 → ToolbarPrinciple()
    → ToolbarPrinciple.swift:12  SubButtons()
      → SubButtons.swift:23      NavigationLink(destination: SubscriptionStoreScreen())
```

The note was presumably written from `AppScreen.swift:112`, where a direct call **is** commented out — and the toolbar route was missed.

**The consequence was live.** That screen's policy link was still:

```swift
Link("Privacy Policy", destination: URL(string: "…")!)
```

A bare English literal — exactly the bug [[bugs#2026-09-09-the-subscription-sheet-rendered-english-on-a-chinese-device]] fixed in the *other* screen on 09-09. So for eleven days a Chinese user could reach a shipping screen showing English, while the vault said the screen was dead. Now uses `sub_privacy_policy`, the same key as its sibling.

> [!warning] The lesson is the list, not the file
> The same 09-08 note makes the same claim about **`EntitledView`**, and **E-16 proposes deleting three more files on the strength of notes of the same vintage.** Re-verify each by tracing callers before deleting anything. Tracked as **E-29**.

### 2. `.xcstrings` will happily produce a 652-line diff for one key

Adding `sub_terms_of_use` by loading the catalogue, inserting, and re-serialising with `json.dumps(indent=2)` rewrote **the whole file** — Xcode writes `" : "` with spaces around the colon, and its key order is not Python's. 652 changed lines for one string, in a file where a real diff is how you see what a session did to the copy.

**Redone as a textual insert** at the right alphabetical position, preserving Xcode's formatting: **18 lines, all additions.** Worth remembering for any future catalogue edit made outside Xcode.

## Verified, and not

**Verified:**
- All four configurations build — iOS Debug/Release, hootmac Debug/Release.
- The new key ships in **both** locales. Read back out of the built app rather than trusted from the source:
  `en.lproj → "Terms of Use"`, `zh-Hant.lproj → "使用條款"`.
- App launches and runs on the simulator; no regression in the flows already exercised.

**Not verified — and it is the obvious one:**
**The button has never been seen.** This Xcode ships **no Simulator.app**, so there is no way to tap into the subscription sheet from here. The code path mirrors the privacy destination directly above it, which is known to work, but "mirrors something that works" is not the same as seeing it. **Folded into R-14**, the device pass: open the Subscribe tab and confirm *both* policy buttons appear and open.

The 中文 is also `needs_review` — 使用條款 is the standard rendering, but it has not been through Jim's pass like the other 35 keys. → [[zh-review]].

## Related
[[00-state-of-play]] · [[privacy-policy#finding-3-re-scoped--2026-09-18-there-is-no-terms-of-use-anywhere]] · [[unfinished]] · [[bugs]] · [[jim-actions]]
