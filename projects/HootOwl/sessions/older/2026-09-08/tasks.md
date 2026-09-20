# 2026-09-08 — Tasks: making the subscription reachable

Jim's two lines, kept as written, each expanded underneath with what it actually involves.

> [!success] Decided and built 2026-09-08 — `9b87c1c`
> **Task 2 done. ob3 dropped. Mention line added instead.**
> Jim pushed back on my hedging about onboarding timing and asked for a straight answer; the recommendation was *task 2 first, skip ob3, add a mention line*, and they took it. Detail at the bottom of this note.

* add subscription at the end of onboarding
* subcribe in the tab  or subscribe as a toolbar action on major screens.

---

## 1. Subscription as the last onboarding screen

**Jim:** *"add subscription as an option at the end of the onboarding, users are 'encouraged' to subscribe but they can opt out."*

A fourth screen, `ob3`, after location. Encourage, never trap: a visible, unambiguous way past it, and the app fully usable if they skip.

**What it involves**
- Add `case ob3` to `OnboardTab` and a screen that hosts the paywall — reuse `SubscriptionScreen`'s paywall rather than growing a third copy of `SubscriptionStoreView`.
- **Structural consequence worth catching before starting:** ob2's two buttons (*Enable Location* / *Not now*) currently **exit onboarding**. If ob3 comes after them, they must **advance to ob3** instead, and only ob3 exits. Otherwise the new screen is unreachable by anyone who taps either button — which is everyone.
- Skip must be plain text, not a trick. "Not now" / "Maybe later", same weight as the existing ob2 skip.
- Suppress it for someone who already subscribed — reinstalling and being asked to buy what you own reads as broken.

**Rules this has to respect**
- Apple allows an onboarding paywall **only if it is dismissible** and the app works without it. Jim's "they can opt out" already matches.
- Do not stack it against the ATT prompt. ATT fires on the **second** launch, onboarding on the first, so they do not currently collide — worth re-checking after this lands.

**One product observation, not an objection:** the only thing a subscription does today is remove ads, and at the end of onboarding **the user has not seen an ad yet**. The pitch is at its weakest exactly where this screen sits. The counter-argument is that onboarding is the one moment of guaranteed attention, which is why most apps do it anyway. Worth measuring rather than assuming — and it argues for task 2 being the more valuable of the two.

## 2. Subscribe reachable from the main screens

**Jim:** *"before users subscribe, keep the subscribe screen easy to access, can we put the subscribe access as a button on the top-left toolbar in each major function screens?"*

**Yes — with one collision.** Checked all four:

| Screen | Top-left (`.topBarLeading`) | Note |
|---|---|---|
| `MncplAllScreen` | **free** | uses `.principal` (search) + `.keyboard` |
| `NbsScreen` | **free** | uses `.principal` + `.topBarTrailing` (pin) |
| `OptionScreen` | **free** | no toolbar at all today |
| `MncplCyclopsScreen` | ❌ **taken** — `infoBar` | and this is the screen users spend the most time on |

**So the honest answer is "three out of four".** For Cyclops the options are: put it `.topBarTrailing` beside `toolbar0`, move `infoBar` elsewhere, or accept an inconsistent position on that one screen. **Recommendation: same placement on the three that are free, `.topBarTrailing` on Cyclops** — a consistent *icon* matters more than a consistent corner, and `infoBar` earns its spot.

**Present it as a sheet, not a tab switch.** `interconnect.appScreenRelay.send(.entitle)` would work, but it dumps the user on another tab and they have to navigate back. A sheet keeps their place. It also means the button works identically on every screen.

**It must disappear once subscribed** — Jim's "before users subscribe". Same `StoreObs` tier plumbing the tab label now uses, so mirror the tier into `@State` via Combine rather than reading the observable directly (`AppTabView`'s dynamic `ForEach` is where `@Observable` invalidation has been unreliable on device).

**Why this is probably the more valuable of the two:** the tab bar **auto-hides after 5 seconds** (`AppTabView`, `autoHideDelay`). So the Subscribe tab — the only current route — is invisible most of the time a user is actually looking at the app. A persistent toolbar button is not duplicating the tab; it is fixing a discoverability hole the auto-hide created.

---

## Open questions for Jim

1. **Icon.** The tab uses `cart.fill` unsubscribed. Same on the toolbar, or something softer — `sparkles`, `crown`, `nosign` over an ad? A cart implies a shop rather than "remove ads".
2. **Wording on the button.** Icon only, or icon + short label? Icon-only is what the other toolbar items do.
3. **Does ob3 appear on every fresh install**, or only after the user has seen the app work once? Related to the "hasn't seen an ad yet" point above.

## Related
[[00-subscription-screen]] · [[jim-actions]] · [[onboarding]]


---

# What was actually done — 2026-09-08

## ob3 was dropped, deliberately

I originally wrote "worth measuring rather than assuming", which Jim correctly called out as dodging the question. The straight answer:

**Against it.** Onboarding paywalls work when the subscription unlocks something the onboarding just demonstrated — the paywall is the payoff of the demo. This one unlocks nothing; it removes ads. So at the end of onboarding it asks someone to pay to remove a problem **they have not experienced, in an app they have not used, from a developer they have no reason to trust yet.** All three are at their worst at that exact moment, and a fourth screen asking for money measurably increases onboarding abandonment.

"Most apps do it anyway" was true and beside the point: the apps that convert well there are gated-feature apps with a free trial. Different product.

**It also saved the structural change** ob3 would have forced — ob2's two buttons currently exit onboarding and would have needed rerouting.

## The mention line instead — extended 2026-09-09 into a signpost

Jim came back to it: keep it a mention, **but tell users where the control is.** Verbatim: *"not put the button here, but tell them, 'If ADs bother you, look for the creditCard button on each pages to get rid of them'."*

So the note now renders the **creditcard glyph inline** and reads:

> Ads keep this free. You can turn them off any time from Subscribe — look for this button on any screen:  **→ ⊙💳**
> 廣告讓這個 App 免費。你隨時可以「訂閱」把廣告關掉——在各頁面找這個圖示：  **→ ⊙💳**

Revised twice more on 2026-09-09, both Jim's calls and both right:
- **The glyph moved to the end, after an arrow.** Leading it read as a bullet point — the eye takes it as list decoration rather than as the icon to go and find. Both strings now end in a colon so the arrow completes them.
- **從 dropped from the 中文.** 從「訂閱」 read as "from the Subscribe tab", a place; without it 「訂閱」 is the action, which is less stilted. The wayfinding is carried by 在各頁面找這個圖示 anyway.

Two details worth keeping:
- **The glyph is drawn, not described.** It comes from `SubscribeAffordance.icon`, the same constant the tab and the toolbar button use, so what the user is told to look for is literally what they will see — and it cannot drift if the icon changes again.
- **The copy says "this button", not "the credit-card button".** Same reason: naming the icon would make the sentence wrong the moment the icon changes, in two languages.

Still no purchase affordance on the screen — the 09-08 reasoning stands.

## The original mention line

`onb_ads_note`, a footnote at the bottom of the last onboarding screen:

> Ads keep this free. You can turn them off any time from Subscribe.

One string, no new screen. It does the job Jim actually wanted — the expectation is set early so nobody is surprised when ads appear, and the escape hatch is named — **without asking for money at the worst possible moment.**

## Task 2 as built

| Screen | Placement |
|---|---|
| `MncplAllScreen`, `NbsScreen`, `OptionScreen` | top-left |
| `MncplCyclopsScreen` | **top-right** — top-left belongs to `infoBar` |

- **Presents a sheet**, not a tab switch, so the user keeps their place. `SubscriptionSheet` wraps `SubscriptionScreen` and supplies the Done button — `SubscriptionScreen` carries none of its own, because it is also a tab where a Done button would be wrong.
- **Hides once subscribed**, via the same Combine-into-`@State` mirror the tab label uses.
- **One icon constant, `SubscribeAffordance.icon`,** now shared by the tab and the button. Two different icons leading to the same screen read as two features — and it makes Jim's still-open icon choice a genuine one-line change. Currently `sparkles`; it was `cart.fill`, which implies a shop rather than "fewer interruptions".

## Settled the same day

- **Icon: `creditcard.circle`.** Went `sparkles` → `cart.fill` → here. A card reads as a recurring charge rather than a shop with items in it, which is what a subscription actually is.
- **Icon + label**, not icon-only. A bare icon leaves the user guessing what the button costs them.

**Worth one look on device:** icon + label is wider than icon-only, and on `MncplAllScreen` and `NbsScreen` the search field sits in `.principal` immediately beside it. If it squeezes the search field, `.labelStyle(.iconOnly)` on that one screen is the fix.
