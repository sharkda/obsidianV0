# Request `taipei2Taiwan` — answer

From the request table at the top of [[onboarding]]. Asked 2026-09-07.

> **request:** in the current build it is Taipei only, it will cover more cities later, eventually all of Taiwan if users request
> **rational:** to let users feedback if they want other cities, so we can prioritize, currently only Taipei and new Taipei city. one of the reasons is other city they park anywhere they like....

---

## Premise, checked then confirmed

The request reads "in the current build it is Taipei only", which would have made screen 1's copy a false claim, so it was checked first. The code says two cities:

- `MunicipalEnum` has exactly two cases — `.taipei` and `.newTaipeiCity` (`MunicipalEnum.swift:20-23`).
- `Municipal.loadOnStart()` (`Municipal+Ext.swift:35-45`) adds **both** — `addTaipei()` at +0.8 s, `addNewTaipeiCity()` at +0.9 s — then activates every loaded proto at +1.2 s.

**Jim confirmed the same day:** *"yes, only Taipei and New Taipei city now."* So "Taipei only" meant *only these two cities, not all of Taiwan* — not Taipei alone. **`onb_s1_body` ("Real-time space counts across Taipei and New Taipei") is accurate as written and needs no correction.**

## One caveat that is not a copy problem

New Taipei's feed is mostly dead: **`noSignal:1001 / live:433 / coverage:30%`** — roughly **70% of NTP lots return −9** and render as no-signal. A user in 新北 can open the app and see a screen of blanks, which is indistinguishable from "not covered".

That is a **data-quality** problem, and copy cannot fix a 30% feed. It is already on the standing list as a product question (hide the −9 lots? label them?) and is worth separating from this request — but it is the thing most likely to make a New Taipei user believe the coverage claim is untrue.

## On "more cities later, eventually all of Taiwan"

The stated goal — *let users feed back so we can prioritize* — is **already implemented**, and without making a promise:

- Screen 1 carries "Not your city yet? **Tell us where to go next →**", directly under the coverage line.
- As of 2026-09-06 that link opens a real `mailto:` with a prefilled "City request" subject, addressed from the Gist-backed config ([[decisions#2026-09-06-city-request-feedback-rides-the-existing-gist-contact-config]]). It is waiting on one thing: the `support` address in the Gist.
- Prioritizing by **counting demand in that inbox** is the mechanism already agreed in [[app-store-ratings-and-feedback-policy]].

### Your "they park anywhere they like" point argues *against* promising

Added to the rationale mid-conversation, and it is the most useful sentence in the request: outside the two metro areas, drivers park informally, so there may be little demand for a structured-parking app there **and** little structured data to build it from. That is a reason to be *less* committal on screen, not more:

- A promise of "all of Taiwan" would commit to cities where the product may not make sense.
- Letting the inbox report demand is exactly the right instrument — and it costs nothing to be wrong, whereas a promise on screen 1 cannot be taken back.

So the request and the existing constraint agree; the nudge is the whole mechanism.

**What is deliberately *not* there is the promise.** The copy constraint locked 2026-07-12 says coverage stays present-tense and never commits to future cities. That is not timidity — per-city data availability is outside our control, a promise invites "you said you'd cover 台中" complaints, and forward-looking coverage claims are the kind of thing App Store review reads closely. "All of Taiwan" as a stated intention is the version of this request I would push back on.

## If you want the expansion signal to be explicit anyway

The smallest honest change is one line — screen 1's body:

- **(a) keep as-is** — *"Real-time space counts across Taipei and New Taipei."*
- **(b) add the mechanism** — *"Real-time space counts across Taipei and New Taipei — more cities as people ask for them."*

(b) states how expansion happens without naming a city or a date, so it stays inside the constraint. **My recommendation is (a)**: the nudge sitting immediately below it already says exactly this, and lane 3 is deliberately blunt and short — (b) makes the reader parse the same idea twice. But (b) is defensible and costs one `onb_s1_body` edit in `Localizable.xcstrings`; say the word.

## Status

**Premise resolved** (two cities, copy accurate). **One open call: (a) or (b).** No code changed for this request.

---

# Resolution — 2026-09-07, Jim's clarification

Jim clarified in the request cell:

> *i mean we need to revise the wording in the onboarding, don't say we are two cities, we need to send the messages, let us know where you want and we will diiver*

That overrides my recommendation (a). The ask is not "is the copy accurate" — it is **stop leading with coverage and start leading with the offer**. Everything above about the premise still stands; the conclusion changes.

## What screen 1 says now

> **Live parking. Right now.**
> Live space counts, expanding city by city.
> Tell us where you need it — we'll head there next.
> **Request your city →**

Three `onb_s1_*` values changed in `Localizable.xcstrings`. **No code change was needed for the copy** — `LandingScreen` reads the keys, and the keys kept their names.

| Key | Was | Now |
|---|---|---|
| `onb_s1_body` | Real-time space counts across Taipei and New Taipei. | Live space counts, expanding city by city. |
| `onb_s1_feedback_prompt` | Not your city yet? | Tell us where you need it — we'll head there next. |
| `onb_s1_feedback_link` | Tell us where to go next → | Request your city → |

`onb_s1_feedback_link` now matches the mailto subject ("City request") and the `settings_request_city` row, so the same action is named the same way in all three places.

## Why dropping the city names is defensible

I raised the honesty constraint before Jim decided, and they decided; recording *why the decision is safe* rather than re-arguing it:

**Coverage disclosure moves to the App Store listing** — which is where a prospective user reads it *before* installing, and where Apple expects region limits to be stated. Onboarding runs after the install decision is already made, so it was never the surface protecting a 台中 user from a wasted download. Dropping the names there is a change of emphasis, not a concealment.

What we still do **not** do is name a future city or a date. "Expanding city by city" and "we'll head there next" describe a mechanism and a commitment to respond — deliberately weaker than the "we will deliver" in Jim's note. If Jim wants it stronger, that is one more string edit; the risk is that a specific promise cannot be retracted once it is in a shipped binary.

## One code change this did force

`LandingScreen.cityRequest` used to hide **the entire block** when no `support` address was configured. Under the old copy that was right — it was a link plus its caption. Under the new copy the prompt line *is the message Jim wants sent*, so hiding it would have silently dropped the whole point of the revision.

Now the prompt always renders and only the tappable link is conditional.

**Consequence: the Gist `support` address is load-bearing as of today.** Without it, users read "tell us where you need it" and have nothing to tap. That moves it from "nice to have" to a release item.

## Status

**Done**, pending the Gist address and an Xcode build. 中文 for the three revised keys is still open along with the other 14.

---

# Second revision, same day — coverage goes back in

Jim, after reading the first pass:

> *"ok, but still need to be clear where we are 'We cover Taipei and New Taipei City now, we will expand to other cities soon, and you can tell us where you need mostly. we will adjust our priorities.'"*

Not a reversal of *"don't say we are two cities"* — a correction of how I read it. Jim did not want coverage **hidden**; they wanted it to stop being the *whole* message. The screen needs **three beats**, and my first pass had dropped the first one.

| Beat | Line |
|---|---|
| where we are today | Taipei and New Taipei City today |
| where we're going | — more cities soon. |
| how you influence it | Tell us where you need it most — we'll adjust our priorities. |

## Final copy

> **Live parking. Right now.**
> Taipei and New Taipei City today — more cities soon.
> Tell us where you need it most — we'll adjust our priorities.
> **Request your city →**

`onb_s1_body` + `onb_s1_feedback_prompt` changed again; `onb_s1_feedback_link` stayed `Request your city →`. Values only — no code change, and the `cityRequest` fix from the first pass (prompt always renders, only the link is conditional) is still exactly right, since the prompt now carries the priorities message.

## The one flag left, then it is Jim's

**"soon" is a timing commitment; "expanding city by city" was not.** It is the single word on this screen someone could hold us to — a reviewer, or a user in 台中 six months from now. Raised, and kept, because Jim asked for it specifically and twice. Recorded here so the choice is visible rather than re-argued later.

## Two dependencies this copy created

1. **The Gist `support` address is a release item.** The prompt renders with or without it, so a missing address means users read "tell us where you need it most" with nothing to tap.
2. **`onb_s1_body` hardcodes the live city list.** Shipping a third municipality now requires editing that string in en *and* 中文, alongside the `Municipal.loadOnStart()` change. A copy string is now coupled to a code change — worth pairing them in the same commit.

Both are in [[unfinished]].
