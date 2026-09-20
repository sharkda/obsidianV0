# App Store release strategy

**Written 2026-09-10 for `Find Parking TW` / `找車位`.** How to get through review without the long painful course — specific to this app, not a generic checklist. The mechanical to-dos live in [[jim-actions]]; this note is the *plan*.

---

## The short answer

**Internal TestFlight for a few days → submit for release. Skip the external beta.**

Not the usual advice, and the reasoning matters more than the conclusion.

| | |
|---|---|
| **Internal TestFlight** | **Do this.** No App Review at all, available within minutes of the build processing, up to 100 testers on your own team. This is just "run the real build on real hardware" with none of the ceremony |
| **External TestFlight** | **Skip it.** It requires a Beta App Review, which costs days — and with no actual testers it buys you nothing but delay. A beta with no beta testers is a slow way to learn nothing |
| **Straight to release** | Don't. Not because of bugs, but because of the four things below that *cannot* be tested any other way |

**What only a TestFlight build can tell you** — the local simulator genuinely cannot:

1. **StoreKit sandbox purchases.** Everything tested so far used the local `.storekit` file, which is a simulation with its own storefront and prices. TestFlight uses the real sandbox: real product IDs, real Apple ID prompts, real subscription lifecycle. If the products are misconfigured in App Store Connect, this is where you find out — not in review.
2. **The real ATT prompt.** It fires on the second launch and is once per install.
3. **Real ads.** Everything so far has been AdMob test ads. Real fill, real latency, real layout.
4. **Real location in real Taipei**, against live feeds, on a real cellular connection.

**Timebox it.** Three or four days of using it yourself as you actually drive and park. For this app a long beta buys little — the data either works or it doesn't, and you will know within a session.

---

## The one risk I would bet money on

> **App Review will open your app in California and see nothing.**

This is the single most likely rejection for this app, and it is the thing that turns a two-day review into a three-week one.

Your app shows parking for Taipei and New Taipei. A reviewer launches it in Cupertino. Location resolves to California. What do they see? Today: **an empty map with no explanation** — because there is still no user-facing state for "no data here" (open item in [[jim-actions]]). To a reviewer that looks like *Guideline 2.1 — app does not function*, or *4.2 — minimum functionality*.

**Three things prevent this, in order of value:**

1. **Write real App Review Notes.** This is the highest-leverage field in the whole submission and most developers leave it blank. Say plainly: the app covers Taipei and New Taipei City in Taiwan; the reviewer will see no lots at their location; here is exactly how to see it working. Give them a concrete address to search — a Taipei landmark — and say which screen to look at.
2. **Ship an honest empty state.** "No parking data for your area yet — we currently cover Taipei and New Taipei City." That converts *broken* into *working as designed*, for a reviewer **and** for a real user who installs from the US storefront. It is the same fix as the feed-down state, and it is the highest-value remaining code task before submission.
3. **Consider seeding the map.** If the app opens on a default Taipei region when the user is far outside coverage, the reviewer sees live data immediately.

**Do not skip the notes even if you do 2 and 3.** They cost five minutes and remove an entire category of misunderstanding.

---

## A licence obligation nobody has noticed

Both feeds are published under **政府資料開放授權條款-第1版** (Open Government Data License v1.0), which **requires attributing the source**. Checked 2026-09-10: the app credits its data nowhere — no string in the catalogue mentions 臺北市政府, 新北市政府, or a data source at all.

This is not an App Review issue; it is a licence-compliance one, and it is cheap to fix: a line on the Options screen and/or in the App Store description crediting 臺北市政府交通局停管處 and 新北市政府交通局 as the data sources. Worth doing before launch rather than after someone points it out.

---

## Order of operations

Metadata and binary are separate tracks. Do the metadata **while** the build processes — that is where solo devs lose days.

**Before you build anything**
- [ ] App Store Connect: app name `Find Parking TW`, subtitle `Taipei & New Taipei parking`
- [ ] Availability: **Taiwan, US, Japan, Hong Kong, Macau** — set by hand; it defaults to *all territories* and would put you in the EEA with no consent platform ([[operations#gate-table--read-this-before-adding-any-territory]])
- [ ] Age rating questionnaire
- [ ] Privacy labels — location, plus whatever AdMob implies. Evidence for the location half is in [[00-location-privacy-audit]]
- [ ] Subscription: Traditional Chinese localisation on the **product**, plus its review screenshot
- [ ] The Gist: real `support.email`, real tutorial video ([[operations#1-the-remote-config-github-gist]])

**Then the build**
- [ ] Archive, upload, wait for processing (minutes to an hour)
- [ ] Internal TestFlight → install on your own phone
- [ ] Use it for real: park somewhere, buy the subscription in sandbox, cancel it, let the ATT prompt fire on the second launch, tap the contact number, open the tutorial video

**Then submit**
- [ ] Screenshots from the TestFlight build — real data, not simulator placeholders
- [ ] Description, keywords, support URL, marketing URL, privacy policy URL
- [ ] **App Review Notes** — the Taipei-coverage explanation above
- [ ] Choose **"Manually release this version"**. Approval and release become two separate decisions, and you want that gap

> ⚠️ **Your first subscription group must be submitted with a new app version.** The subscription and the app go through review together. That makes this first submission a bigger surface than a normal one — one more reason to have run the sandbox purchase on TestFlight first.

---

## What a reviewer will actually poke, for *this* app

- **Subscription terms.** Guideline 3.1.2 wants title, duration, price and what you get, plus working links to a privacy policy and terms, visible **before** purchase. `SubscriptionStoreView` supplies most of this; the privacy policy destination is wired. Check the terms/EULA link is present too.
- **Restore purchases.** Must exist and work. It does — on both the paywall and the subscribed screen.
- **What the subscription actually buys.** Yours removes ads and nothing else, and the copy now says exactly that. **This is a strength in review**: reviewers reject overclaiming, never underclaiming.
- **The permission prompts.** Both are localised now and neither names the app.
- **ATT.** It fires on the second launch, so a reviewer opening the app once will not see it. That is allowed. If they ask, the answer is: it is requested after the user has seen the app work, never as a gate.
- **Ads with a subscription.** Legitimate and common. The paywall says ads may increase, which is honest and unusual — it will not hurt.

---

## How to make it not painful

The pain in App Store submissions is rarely the review. It is churn — small things bouncing back, each costing a day.

- **Submit Monday or Tuesday.** A rejection on Friday costs you the weekend.
- **Do not bundle.** Ship the smallest honest first version. Every extra feature is extra review surface, and the first submission is the one most likely to be rejected.
- **A rejection is a conversation, not a verdict.** The Resolution Center is a message thread with a human. Most first rejections are "we could not find X" or "explain Y". Answer plainly, attach a screenshot, and do not resubmit the binary if only an explanation is needed — replying is faster than a new build.
- **If they cannot reproduce it, that is on the notes, not the app.** Rewrite the notes rather than the code.
- **Expect 24–48 hours.** If it sits over three days, that is normal and not a signal. Do not resubmit into the queue — you lose your place.
- **Keep the binary and the metadata separate in your head.** Roughly half of first-submission problems are metadata: labels, screenshots, missing URLs. None of them require a rebuild.

---

## After it is approved

- **Release manually**, when you are awake and able to watch it. Not Friday evening.
- **You have no crash reporting.** Xcode Organizer shows crashes from users who opted into sharing analytics — partial and delayed, but not nothing. Check it on day one and day three. Decide about a real crash SDK before you need it, not after ([[jim-actions]]).
- **Watch the first reviews for two things specifically:** New Taipei users seeing blank lots (the feed is ~30% live — [[data-sources]]), and anyone reacting badly to *"廣告會越來越多"*. Both are known, both are one string or one config change away.
- **The Gist is your fast lever.** Contacts, the tutorial video and the support address change with no release. Remember it exists when something needs fixing quickly — the first instinct after launch is to ship a build, and often you do not have to.

---

## Related
[[jim-actions]] — the tickable list · [[operations]] — runbooks and the release checklist · [[data-sources]] — feeds, contacts and the licence · [[decisions]]
