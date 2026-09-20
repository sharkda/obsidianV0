# 2026-09-08 — Subscription screen; onboarding + ads work committed

## ✅ Built, and pushed — 2026-09-08

**Jim built it in Xcode: "run ok".** The whole stack compiled on the first attempt, which is worth noting because it was six commits of never-compiled work — two new onboarding screens, a new subscription screen, a privacy manifest, ATT wiring, the tier removal, and hand-edited `project.pbxproj` entries for three new files across both targets.

`origin/main` is now `37a39f8`. Working tree clean, local and remote in sync.

```
37a39f8  Name the actual objection in the paywall copy
3b8cb55  One subscription tier, a tab that renames itself, honest paywall copy
7d810af  Give subscriptions a release-facing screen
aae8aa3  Ask for IDFA on the second launch, and declare the privacy manifest
d16e703  Build the three real onboarding screens
53b7bdc  Serve contacts, support inbox and tutorial video from the Gist config
43ac0a0  ← previous HEAD
```

**What "it compiled" does and does not prove.** It proves the pbxproj wiring was right — all three new files are in both targets, or the build would have failed with the misleading overload error documented in [[bugs]]. It does **not** prove any of the behaviour: the onboarding flow, the ATT prompt on second launch, the tutorial link, the subscription screen's two states, and the tab renaming itself are all still unverified on a device. Those checks are in [[jim-actions]].

## Originally committed — four commits, tree clean

```
7d810af  Give subscriptions a release-facing screen
aae8aa3  Ask for IDFA on the second launch, and declare the privacy manifest
d16e703  Build the three real onboarding screens
53b7bdc  Serve contacts, support inbox and tutorial video from the Gist config
43ac0a0  ← previous HEAD
```

Split by layer, as usual. **None of it has been compiled** — the CLI still cannot build this project, so the whole stack is waiting on one Xcode build. Every touched file was parse-checked (`swiftc -parse`), which catches syntax and nothing else. Not pushed.

---

## The `.entitle` tab was shipping a developer surface

Jim: *"if you look at the entitle screen, it's full of developer/debug garbages."* Correct — `EntitledView` embeds `IapReceiptView()` and a raw tier dump. Both sit behind `#if DEBUG`, but Jim builds in Xcode, so that is what they see every time, and it is not a page anyone would want a reviewer to open.

**`EntitledView` is now unwired and left in the tree**, as asked. It is a perfectly good debug view; it was just pointed at by the shipping tab.

### The new screen

`hootowl/iAp/subUi/SubscriptionScreen.swift`, two states:

| State | Shows |
|---|---|
| Not subscribed | The paywall — `SubscriptionStoreView`, restore/policies/sign-in/cancellation buttons, privacy-policy destination |
| Subscribed | Tier icon, plan name and price **from StoreKit**, whether it renews or expires and when, Manage subscription (iOS), Restore purchases |

Name and price come from `Product.displayName` / `displayPrice`, never from our own strings — StoreKit already has them localised and currency-correct for the user's storefront.

The renewal line distinguishes **renews** from **expires** by unwrapping `willAutoRenew` out of the signed renewal info. If verification fails we say *expires* — the claim that cannot mislead. Grace period, billing retry, expired and revoked each get their own honest line, because "there's a problem with your payment" is exactly what someone opens this screen to find out.

## Three bugs found while writing it

1. **A tier-two subscriber was shown the paywall.** `EntitledView` tested `subTier == .one` exactly. Anyone on the higher tier fell through to the purchase screen they had already paid past. Now `tier > .none` — `SubscriptionTier` is `Comparable`, so this reads correctly for any future tier too.
2. **The tab label was the literal string "entitle" in English.** The key had a `zh-Hant` value (課金) but **no `en` value at all**, so English users read the raw key. Now "Subscription".
3. **The old paywall copy was false.** It promised *"unlock advanced features"*. On iOS, `AppScreen.sorted(subTier:)` returns **the same tab list for every tier** — nothing is gated. The only thing a subscription changes is `SubscriptionTier.showingAdBanner`. Overstating that invites refund requests and awkward App Review questions, so the new copy says only what is true: it turns off the ad banner, and the app is otherwise identical.

That third one is worth remembering as a product question rather than a copy fix: **there is currently no functional reason to subscribe.** If the intent was that subscribers get more, the gating was never built.

## One macOS trap avoided

The new screen reads `StoreObs.shared` rather than `@Environment(StoreObs.self)`. The environment value is injected **only under `#if os(iOS)`** in `hootowlApp`, while `.entitle` is in the macOS tab list too — so the environment read would trap on macOS. The singleton exists on both platforms.

State is mirrored into `@State` through Combine rather than read from the observable directly, matching the Cyclops workaround: this screen lives in `AppTabView`'s dynamic `ForEach`, where `@Observable` invalidation has been unreliable on device.

## Now unreferenced

`SubscriptionStoreScreen` (`iAp/subUi/SubscriptionStoreView.swift`) — the old paywall, reachable only through `EntitledView`. Left in the tree with it. Its `paywall text` string is likewise unused now; that is where the "advanced features" claim lives, so it should not be revived without rewriting.

## Related
[[jim-actions]] · [[operations#2-release-checklist]] · [[bugs]] · [[decisions]]

---

# Jim's three follow-ups — 2026-09-08

## 1. One tier only

**Tier two is removed.** `SubscriptionTier` is now `.none` and `.one`.

It was never sold — nothing in App Store Connect corresponds to `com.sharkda.hootowl.ruby` — yet **four switches carried a case for it**, each inventing behaviour for a product a user could not buy. The clearest symptom: `SubButtons` offered a tier-one subscriber an **"upgrade"** button with nowhere to upgrade to.

Removed from `SubscriptionTier` (enum case, `pid`, `sysImg`, `tier(for:)`), `AppPid.pid`, and `SubButtons.setButtonByTier`. `StoreObs.tier2Ad` was **left alone** — despite the name it is "tier → Ad", not tier two.

## 2. The tab renames itself

`AppScreen.label` now takes the tier: **"Subscribe"** with a cart before, **"My Subscription"** with a seal after. Every other case ignores the argument.

Call sites: `AppTabView` passes its own `subTier` (which already drives `AppScreen.sorted`), and `AppSidebarList` passes `.one` to match the tier it already hardcodes.

**中文:** the unsubscribed label reuses **Jim's own 課金**, so Chinese users see exactly what they saw before. The subscribed one is a **draft — 我的課金 — composed from Jim's term and awaiting review.** Flagged in the string's comment. Without this, switching to new keys would have silently regressed Chinese users to English.

## 3. Paywall sets an expectation instead of making a promise

Jim's call, and the reasoning is sound: pre-empt the user who will not pay and then complains about ads.

> **Ads keep this app running**
> There will be more of them over time. If you'd rather they stayed out of your way, a subscription turns them off completely — live counts, pinned lots and search work exactly the same either way.

*(Second sentence reworded on Jim's note the same day: "if that isn't for you" was vague about what "that" is. The objection users actually have is ads getting in the way of using the app, so the line now says that.)*

Still refuses to claim an unlock, because nothing is gated.

> [!note] One risk, stated once and not re-argued
> Telling users the ads will grow can itself draw a bad review — "they threaten you with more ads". It is mitigated by where it appears: the paywall is a screen people open deliberately, not onboarding, so the audience is already considering paying. Worth watching in early reviews; the wording is one string to soften if it lands badly.

## Still true

**Nothing is compiled.** Five commits deep now. Every touched file parse-checks, which catches syntax only.

**The underlying product question is unchanged:** the only thing a subscription does is turn off ads. That is now stated honestly everywhere, but if subscribers were meant to get more, the gating was never built. Open in [[jim-actions]].
