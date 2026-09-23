# What a user outside Taiwan actually experiences — and what to do about it

**A product discussion, 2026-09-20.** Jim: *"in terms of users not in Taiwan, e.g. review in CA, US, what will they experience from the App… I don't see a picture."*

Fair. Everything written so far has been **mechanisms** — which tab is location-filtered, which search mode ignores GPS. None of it says what the thing *feels* like. This note is the picture, then a proposal.

---

## Part 1 — The walkthrough, as it is today

A phone in California. Fresh install. Every step below is what the code does, not what it should do.

| Step | What they see |
|---|---|
| **Onboarding 1** | *"Live parking. Right now."* — *"Taipei and New Taipei City today — more cities soon."* Then: **"Tell us where you need it most — we'll adjust our priorities."** …with **nothing to tap**. The link is hidden because no support URL is configured (`LandingScreen.swift:121`). An invitation that cannot be accepted. |
| **Onboarding 2** | Pin the lots you use. Reasonable. |
| **Onboarding 3** | *"Turn on location and the closest lots come first."* They tap **Enable Location** and grant it. |
| **Lands on the map** (first tab) | A card: 🗺️ **"We're not here yet — Right now we cover Taipei and New Taipei."** **No button.** Behind it, an empty map of their own neighbourhood. |
| **Tab 2 — Cyclops** | The same dead-end card. |
| **Tab 3 — All** | **This one works.** ~3,162 Taiwanese car parks with live space counts. Nothing on screen explains why they would want it. |
| **Options / Subscribe** | Work. Subscribe offers to remove the ads. |
| **Bottom of the screen** | An **ad banner**, throughout. |
| **Second launch** | **"Allow Find Parking TW to track your activity across other companies' apps and websites?"** |

### What that adds up to

> I gave you my location. You told me you don't work here. You showed me an ad. Then you asked to track me.

Two of the five tabs are dead ends. The one screen that *does* work is the one nobody would think to open. And the app asks the user for something — *tell us where you need it* — **twice**, while providing no way to answer either time.

**It is not broken and it will not be rejected.** The empty state is honest and explains itself; that was the 09-15 work and it did its job. But honest is a low bar. **Right now the app's answer to "I'm not in Taipei" is a polite dead end with an ad on it.**

---

## Part 2 — Who is actually in this situation

This is the part that changes the design. **"Outside coverage" is not one user.**

| | Who | What they actually want | What they get today |
|---|---|---|---|
| **A** | **App Review, California** | To verify the app does what the listing says | A dead end, unless they read the notes and type an address |
| **B** | **A Taiwanese person abroad** — visiting family, working overseas, planning a trip home | To use it **in Taipei**, soon. Maybe to look now. | Told "not here yet", as if they were the wrong person |
| **C** | **Someone in Kaohsiung / Taichung / Tainan** — installed it because the name says **TW** | Their own city | "Not here yet", and **no way to say "please come here"** |
| **D** | A random American | Nothing; they churn | Fine, irrelevant |

**B and C are not edge cases.** B is a real slice of a Taiwanese commuter app's audience. C is created by our own app name — **`Find Parking TW` promises Taiwan and delivers Greater Taipei.** The subtitle carries the correction, but the person who installed anyway is standing in Kaohsiung with a dead end.

**And A is not a user at all** — which is why solving A with *review notes* has always felt like a workaround. It is.

---

## Part 3 — The thing worth agreeing on

> **The app treats "outside coverage" as an error state to explain.
> It should treat it as a different mode: not *"we don't work"* but *"you're not there yet."*"**

Here is why that is not just wording. **The data for all of Taipei and New Taipei is already on the device** — every one of these users has ~3,162 car parks with live counts sitting in memory, because the app downloads whole cities and filters locally. That is also why the privacy story is strong.

**Every one of these people could browse Taipei right now. The app simply never offers.**

---

## Part 4 — What to do

### 1. ⭐ "Look around Taipei" — one button on the outside-coverage card

Tap it, the map jumps to Taipei with live pins, and the app works. **The mechanism already exists and is already shipping** — `nbs.search(mapMode: .mapTap, loc0:)` searches around any point with no reference to the user's location; the address search uses it, and tapping the map uses it. This makes it *discoverable* rather than building anything new.

What it does for each person:

- **A — the reviewer:** one tap and they see the real product. **This solves the review-testing problem inside the app rather than in a text field.** The notes stop being the mechanism and become a backup. A reviewer who never reads them still sees it work.
- **B — Taiwanese abroad:** genuine utility. *"Where can I park near my parents' place next week?"* The app becomes usable before the trip, not just during it.
- **C — Kaohsiung:** still not served — but now they have **seen what they would get**, which turns "request your city" from an abstract ask into a concrete one. People ask for things they have experienced.

**Cost:** a button, and a flag so the map knows it is showing a place the user is not standing in. Small.

### 2. Make the city request answerable — **R-02**, already built

Both asks — onboarding screen 1 and the coverage card — are **live today with no destination**. The code is written and dormant; it needs one line in the Gist.

This is the difference between an out-of-coverage user being a **dead end** and being **a demand signal with a name and a city attached**. For a product whose next decision is *which city do we add third*, that signal is the input.

### 3. Deliberately not proposing

- **Hiding the ad on the dead-end screen.** It feels extractive, but #1 removes the dead end — the ad then sits next to working content, which is the normal deal.
- **Suppressing ATT outside coverage.** Special-casing, tiny gain.
- **Renaming the app.** `Find Parking TW` with the coverage in the subtitle is a reasonable bet on where this goes. **But it only stays reasonable if C has a way to ask** — which is #2.

---

## Part 5 — Does this solve the reviewer problem?

**Better than the notes do, and differently.**

| | Review notes (today) | "Look around Taipei" |
|---|---|---|
| Works if the reviewer does not read instructions | ❌ | ✅ |
| Needs them to type an address | ✅ needed | ❌ |
| Demonstrates the map, not a list | ✅ | ✅ |
| Helps a single real user | ❌ | ✅ |

**Keep the notes either way** — they are written, verified and free. But right now the notes are load-bearing, and they should not be. A reviewer following written steps is a process that can fail; a button they cannot miss is a product that works.

---

## The proposal, in one line

**Stop treating "not in Taipei" as a failure to explain, and start treating it as a state the app can do something useful in** — by surfacing the Taipei data already on the device (#1), and by making the city request answerable (#2).

## Related
[[sessions/older/2026-09-19/02-reviewer-scope-and-testing|02 — how a reviewer tests it]] · [[release-strategy#the-one-risk-i-would-bet-money-on]] · [[decisions#2026-09-15-a-city-request-goes-to-a-url-not-a-mailto]] · [[00-state-of-play]]
