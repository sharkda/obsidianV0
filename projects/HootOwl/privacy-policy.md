# Privacy Policy

The live document: **https://jimhsuyc.wixsite.com/tataro/privacy-policy** (free Wix tier, no custom domain — see below). It is linked from **two hardcoded places in the app**, and is the destination App Store Connect's *Privacy Policy URL* should point at.

Related: [[operations]] · [[app-store-connect]] · [[jim-actions]] · [[decisions#2026-09-15-a-city-request-goes-to-a-url-not-a-mailto]]

---

## No custom domain is needed

Wix pushes a domain purchase. **It is not necessary.** `jimhsuyc.wixsite.com` returns 200 logged-out, and Apple accepts a `wixsite.com` URL for both the *Privacy Policy URL* and the *Support URL*. A custom domain buys polish, not compliance. Checked 2026-09-16.

The same free site already carries a **Support** and **Contact** nav, with a pointer to Messenger on `facebook.com/tataroApp` — which is the "relay" Jim wanted: users reach him without his personal address ever being published, and the destination inbox can change without republishing anything.

---

## ⚠️ The URL is hardcoded in the app, in two places

```
hootowl/iAp/subUi/SubscriptionStoreView.swift:43
hootowl/iAp/subUi/SubscriptionScreen.swift:202
    URL(string: "https://jimhsuyc.wixsite.com/tataro/privacy-policy")!
```

This is out of step with everything else: the municipal contacts, the tutorial video and the city-request destination all live in the Gist precisely so they can move with no release. **If this URL ever changes, it is a build.** Low urgency — Wix redirects `wixsite.com` paths if a custom domain is added later — but it is a trap worth closing. Not done; offered 2026-09-16.

---

## What the app actually does with data — verified against the source

This is the ground truth any wording has to match. Checked 2026-09-16 by reading the code, not by reading the old policy.

| Claim | Verified how | True? |
|---|---|---|
| Location is used on-device to find nearby car parks and centre the map | `Municipal`, `CLLocationManager` at `kCLLocationAccuracyHundredMeters` | ✅ |
| **No coordinate is ever put in a network request** | grepped every `URLRequest` / `URLComponents` / `dataTask` site; the app downloads **whole-city datasets** and filters locally | ✅ |
| Location is cached **on the device only** | `Municipal+Cache.swift` → `Library/Caches/hootowl-snapshot.json`, `CachedLocation`, writes throttled to 30 s | ✅ |
| Cached data older than **24 h** is discarded | `staleAfter` 86400 s; observed firing in the simulator: `🗃 cache snapshot stale (117963s > 86400s), ignoring` | ✅ |
| Addresses the user types go to **Apple** | `MKLocalSearchCompleter` / `CLGeocoder` in `AddressSearchObs` | ✅ |
| AdMob may access device info, and the IDFA only with ATT consent | `GadCon.swift`, `ATTWarmup.swift` (prompt on 2nd launch) | ✅ |
| Purchases handled by Apple; no payment details seen | StoreKit only | ✅ |
| Find Parking TW collects a **name** | — | ❌ **no.** That is Bopomofo |

**The honest version is a better story than the old policy told.** "We have no servers and never receive your location" is a strong claim, and it is true.

---

## Review log

### Round 1 — 2026-09-15
Policy named Bopomofo's data model only. Seven findings; the serious ones:
1. 🔴 **Location never mentioned at all** — in a location-based parking app whose permission prompt a reviewer sees before reading the policy.
2. 🔴 **Contradicted the app's own ATT prompt** — "I will not share any information … to this third party service" versus an alert asking to track across other companies' apps.
3. 🟠 Described the wrong app's model ("collects only name", "preview/paid edition").
4. 🟠 Broken terms reference — "accessible at bopomofo" is not a link.
5. 🟡 Subscriptions unmentioned · 🟡 English only · 🟡 no effective date.

### Round 2 — 2026-09-16 (after Jim's revision)
**Fixed:** location paragraphs added (on-device use, local cache, no servers), Apple Maps geocoding disclosed, AdMob device-info + IDFA-on-consent line added, Apple-handles-purchases line added. Findings 1 and 5 closed.

### Round 3 — 2026-09-18 (after Jim's second revision)

**Fixed: the 🔴.** The blanket sentence is gone and the scoped replacement went in verbatim:

> The free preview edition which you cannot input your "name" uses third party service, the Google AdMob. Since app does not collect any personal identifiable information, not even the name. **I do not send any information that I collect to this third-party service. AdMob collects device information directly, and — only if you allow tracking — the advertising identifier.**

That was the only finding with App Review consequences — a policy contradicting the app's own ATT prompt. **It no longer does.** Finding 1 closed; the page is no longer self-contradictory.

**Nothing else moved.** Findings 2–7 are unchanged, word for word.

#### Two new, both minor

| # | Sev | Issue |
|---|---|---|
| 8 | 🟡 | **The AdMob disclosure is now stated twice.** The new scoped sentence, then two paragraphs later: *"When using free edition and Advertisement is activated, Google AdMob may access device information and, if you allow tracking, the advertising identifier"*. Not a contradiction any more — just redundant. **The second one is now deletable.** |
| 9 | 🐢 | **The voice switches between "I" and "we"** — *"I do not send…"* against *"we have no servers"* and *"we never see payment details"*. Cosmetic, but it reads as two documents spliced. |

#### Why finding 2 is worse than its 🟠 suggests

The opening paragraph lists `FindParkingTW` under **both** categories — *"built the FindParkingTW, the bopomofo app paid edition and others as Commercial apps; and the FindParkingTW, the bopomofo preview edition and others as Ad-supported apps"*. Defensible on its face (this app does have a subscription *and* ads), but it means the paid-edition paragraph — *"the paid edition of the app allow you to input a 'name' value"* — reads as applying to Find Parking TW. **So the policy currently tells a reviewer this app collects a name.** It does not. That is the single most wrong sentence on the page, and it is the first one under the heading.

**Still open:**

| #   | Sev | Issue |
| --- | --- | ----- |
| 2   | 🟠  | **The headline claim is still Bopomofo's** — *"My service and this app collects only 'name' and no other personal identifiable information."* First line under *Information Collection and Use*, sitting **above** the location paragraphs. **Fix: put the app name in front of each claim** rather than making blanket statements. |
| 3   | 🔴  | **Terms of Use is missing everywhere, not just broken on this page.** See the section below — re-scoped from 🟠 to 🔴 on 2026-09-18. |
| 4   | 🟡  | *Retention* still says "the paid edition". The concrete fact is better: the location cache is discarded after **24 h** and removed when the app is deleted. |
| 5   | 🟡  | **Name it as the Store will.** The listing is **`Find Parking TW`**; the policy writes `FindParkingTW` and `FindParkingTw`. |
| 6   | 🟡  | Typos: "personal identical information" → identifiable; "that that you voluntarily input". |
| 7   | 🟡  | Still **English only** — primary market is Taiwan and everything else down to the permission strings is localised. Still **no effective date**. |
| 8   | 🟡  | The duplicated AdMob sentence (above). |
| 9   | 🐢  | "I" / "we" voice (above). |

**Round-by-round:** 7 findings after round 1 → round 2 closed 2 (location, subscriptions) → round 3 closed the 🔴. **No 🔴 remains.** What is left is accuracy and polish, not compliance risk — with the caveat that finding 2 is an outright false statement about this app, which is a bad thing for the first line of a policy to be.

### Finding 3, re-scoped — 2026-09-18: there is no Terms of Use anywhere

Jim asked where the terms reference is. Answering it turned up a bigger problem than the sentence.

**Where the sentence is:** fourth paragraph, last line of the preamble, directly above the *Information Collection and Use* heading.

> The terms used in this Privacy Policy have the same meanings as in our Terms and Conditions, which is accessible at **bopomofo** unless otherwise defined in this Privacy Policy.

Template boilerplate from the App Privacy Policy Generator — the original reads *"accessible at [link]"*, and `bopomofo` was typed over the placeholder and never linked. Confirmed against the raw HTML, not the stripped text: there is **no `<a>` tag**, it is plain text in a `<span>`.

**There is no page for it to point at.** `pages-sitemap.xml` lists the whole site — four pages:

```
/tataro                    /tataro/ask-me-questions
/tataro/privacy-policy     /tataro/support
```

**And the app never links Terms of Use at all.** Both subscription screens supply only the privacy destination:

```
hootowl/iAp/subUi/SubscriptionStoreView.swift:42   .subscriptionStorePolicyDestination(for: .privacyPolicy)
hootowl/iAp/subUi/SubscriptionScreen.swift:200     .subscriptionStorePolicyDestination(for: .privacyPolicy)
```

`grep -rn "termsOfService"` across the project returns **nothing**. `SubscriptionScreen.swift:199` sets `.storeButton(.visible, for: … .policies …)`, so the sheet advertises policy buttons with only one of the two destinations supplied.

**Why it is 🔴.** For an auto-renewable subscription, **Guideline 3.1.2** wants a functional Terms of Use (EULA) link next to the privacy policy. Nothing has to be written: absent a custom EULA, Apple's standard one applies and linking it satisfies the requirement —
`https://www.apple.com/legal/internet-services/itunes/dev/stdeula/`

**The fix, in order of weight:**
1. **Add a `termsOfService` destination to both screens** — ~4 lines each, mirroring the privacy block directly above it. This is the part with review consequences. Tracked as **E-28**. **Still open.**
2. ~~**Then the sentence:** point it at the same EULA, or delete it.~~ — ✅ **Jim deleted it, 2026-09-18.** Re-fetched and verified: **zero occurrences of "term" anywhere on the page**, the spacer before *Information Collection and Use* preserved, paragraph 3 now runs into the heading and reads correctly.

> [!warning] Deleting the sentence did **not** close this finding
> It removed a dead, false reference. Guideline 3.1.2 asks for a *working* Terms of Use link **in the subscription sheet** — that is E-28, and it is a code change, so **it has to be in the binary before the next archive.**

**Also spotted 2026-09-18:** the Facebook blurb's visible label changed from *"link to our page tataroApp"* to *"link to our page our Apps"*, but **the href is unchanged** — still `https://www.facebook.com/tataroApp`. So the caveat in [[operations#support--which-transport-and-why-url-wins]] still stands (that page describes itself as the company behind Bopomofo), and the new wording reads as a grammar slip — *"link to our page our Apps"*.

---

### Offered, not done
A full corrected draft — one document covering both apps with the app-scoped structure, in **English and 中文**, for Jim to paste and approve. Deliberately not written unasked: it is his document and his wording to own. Offered 09-15, 09-16 and 09-18.

**A smaller offer, made 2026-09-18:** rather than a whole draft, just the **four replacement sentences** for findings 2, 3, 4 and 8 — paste-sized, each one swapping for a sentence already on the page. That closes everything except the 中文 version and the effective date without rewriting a document Jim wants to own.
