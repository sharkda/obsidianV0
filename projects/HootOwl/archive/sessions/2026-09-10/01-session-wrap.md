# 2026-09-10 — Session wrap

**Everything is committed and pushed.** Long day: the app got its name, its last English strings, and two more instances of the same underlying bug class.

---

## What landed

| | |
|---|---|
| **The app is named** | `Find Parking TW` / `找車位`, localised in a new `InfoPlist.xcstrings`. Killed three stale names, and localised both system permission prompts — the last user-visible English in a Chinese build |
| **Map pins fade with age** | The map had no freshness concept at all. Alpha now carries it: 0.9 / 0.7 / 0.45 across the same 5- and 30-minute thresholds Cyclops uses |
| **Subscription sheet spoke English** | Two causes, one inside the string catalogue and one entirely outside it |
| **Export compliance** | `ITSAppUsesNonExemptEncryption` declared, so App Store Connect stops asking on every upload |
| **中文** | 11 more keys — the tab bar and search field a real user sees on first launch |
| **StoreKit descriptions** | Cut to fit App Store Connect's 45-character limit, which the English one exceeded |

## The theme of the day, worth naming

**Three separate bugs, one shape: something that was true once and quietly stopped being true.**

- The map banner offering *"Enable Always for background nearby search"* — accurate until battery #9 removed the Always escalation in June, then shown to **every iOS user permanently** with a dead button, promising background location the app cannot do.
- The denied-location string naming *"(While Using or Always)"* — same June change, same staleness.
- `availFetched` on the map pins — a boolean meaning "we got data at some point", which never expires, so an hour-old count looked identical to a ten-second-old one.

None of these were caught by reading the code, because the code was fine. They were caught by **looking at the running app** and by Jim noticing things on screen. Written up as patterns in [[swift-patterns]] — the removal-leaves-the-copy rule, and "has been fetched" is not a freshness signal.

## And one lesson about my own audit

On 2026-09-09 I verified six ways that the app **cannot** run location in the background, and called the privacy claim safe. The next day Jim found the map advertising background nearby search. Both were true: the code could not do it, and the app was telling users it could. **Verifying the implementation is half of a privacy audit; the copy is the other half.**

## New capability

`export DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer` makes `xcodebuild` and `simctl` usable from the session even though `xcode-select` points at CommandLineTools. It still cannot build (ConcaveHull resolution fails), but it **can** read simulator language settings, dump an installed bundle's compiled `.lproj` tables, and launch the app and screenshot it. That chain is what diagnosed the English paywall after two wrong guesses. In [[operations#3-building-and-testing]].

## Where the release stands

**Nothing is blocked on code.** [[jim-actions]] is the list; the shape of what remains:

- **The Gist** still needs a real `support.email` and the real tutorial video. Both cities' contacts are now real and sourced ([[data-sources]] — mine to re-check, next due 2026-10-09).
- **App Store Connect** — name and subtitle, availability (Taiwan/US/Japan/HK/Macau, set by hand), the subscription's Traditional Chinese localisation, privacy labels, screenshots, age rating.
- **A device pass and a TestFlight pass** — nothing has been exercised on hardware, and TestFlight is the only way to see sandbox purchases, the real ATT prompt and real ads.
- **Two open product questions:** whether a subscription should do anything beyond removing ads, and what a user sees when the feed is down (currently: nothing).

## Related
[[00-pushed-and-state]] · [[jim-actions]] · [[operations]] · [[bugs]] · [[decisions]]
