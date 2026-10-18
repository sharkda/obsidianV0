
# Jim's comment:
first thing first, what kind of "solution are we looking at, the upperbound of our solution." 
if the best we can do is the make sure the app does not crash, but the data is stalled, and this will not be fixed until 
1. developer /us found out about this issue
2. fixed it, release it.
3. users took the time to download the revision
I am afraid that is not good enough, 

I am thinking:
1. developer / us can be the first one to learn if the field name changed and the app will not work properly
2. developer fix it and release it over the air. 
3. users get the fix w/o downloading and upgrade.



# Claude's answer — 2026-10-18

**You're right, and the page was aimed too low.** I wrote it to the standard "the app must not crash," and you're asking for the standard "a break is a non-event." Those are different ceilings and the second one is reachable. What follows replaces the Layer 5 recommendation at the foot of this page.

Your three steps turn out to have three different answers, so let me take them in your order.

---

## Your #1 — "we learn first." The app is the wrong place to look.

This is the part I got wrong, and it's the part that makes everything else optional.

I had put detection inside the app: raise the log levels, record it on the proto, show it on the DQI screen. That only works if **someone is already looking at a console**, which means it tells you after a user has already hit it. Useless for what you want.

**But you don't need the app to tell you. The feed is public.** You can watch it yourself, from outside the app entirely:

> A scheduled job — GitHub Actions, free tier, every 15 minutes — fetches both feeds, decodes them against the schema committed in the repo, and **opens a GitHub issue / emails you** the moment the shape stops matching.

Compare the two honestly:

| | In-app telemetry | **Scheduled job outside the app** |
|---|---|---|
| Detects a break when nobody is using the app | ❌ | ✅ |
| Detects it **before** the first user sees it | ❌ | ✅ |
| Detects it at 3am | only if someone is awake and using it | ✅ |
| Needs a server | ✅ you'd have to run one | ❌ |
| Needs app code | ✅ | ❌ **zero** |
| Needs a privacy-label change | ✅ — see below | ❌ |
| Can ship today, independent of the binary | ❌ | ✅ |

> [!warning] Why in-app telemetry is actively the worse choice here
> Reporting a schema break from the app means **collecting diagnostic data**, which is a declarable category in Apple's privacy nutrition labels. This app's labels commit to *precise location, app functionality, foreground-only* and nothing else. Adding a diagnostics channel means a label change, a new justification, and new App Review surface — on a first submission. For a signal you can get for free from a public URL with no user involved at all.

**This is the first thing to build, and it is not Swift.** It's a ~40-line script and a cron YAML. It does not touch the app, does not need a build, does not need review, and can be running before the next archive.

Once it exists, your #1 is solved completely and permanently — **and a break stops being an emergency**, because you find out while the app is still showing merely-stale numbers rather than when a user writes a review.

---

## Your #2 and #3 — the OTA fix. How far it actually reaches.

Mostly achievable. Here is the honest table, because the ceiling is not the same for every kind of change:

| What Taipei changes | Fixable without a release? | Heal time |
|---|---|---|
| A key renamed — `availablecar` → `carRemain` | ✅ **yes** — alias map | minutes |
| A key recased — `availablecar` → `availableCar` | ✅ **yes** — and no config needed, Layer 3 handles it | instant |
| `UPDATETIME`'s date **format** changes | ✅ **yes** — *if the format string is config too* | minutes |
| A value's type changes — `203` → `"203"` | ✅ **yes** — and no config needed, tolerant decoder | instant |
| The endpoint moves, or a v2 is published | ✅ **yes** — *if the URL is config too* | minutes |
| Structure reshaped — `park` array becomes a nested object, or CSV becomes JSON | ❌ **no** | needs a release |

Two of those rows are new to this page and both are cheap: **put the date format and the feed URL in the same config as the aliases.** `UPDATETIME` is already one of the eight fatal items precisely because its format is hardcoded at `AllAvailable.swift:47`, and a hardcoded URL means a deprecated endpoint costs a release for no reason. Same mechanism, same Gist, a few lines each.

> [!note] Apple's actual limit, so we design inside it rather than discovering it at review
> **Guideline 2.5.2:** an app may download and act on **data and configuration**; it may not download and execute **code** that changes its features.
>
> A key-alias map is data. A date format string is data. A URL is data. All fine — this is exactly what Firebase Remote Config does, and Apple ships that pattern themselves.
>
> What is *not* available is "push a code patch OTA." So the bottom row of that table genuinely needs a release. There is no way to buy it, which is why Layers 0–2 still matter: they decide whether those 1–3 days look like *stale numbers going grey* or *an app that crashes every two minutes*.

---

## Three things in today's code would stop your #3 from working

Your step 3 is *"users get the fix w/o downloading and upgrade."* That is true of the design and **false of the current implementation**, for three specific reasons. These are the real work.

### 1. The config is fetched once per process launch, ever

```swift
// ContactConfig.swift:264-270
func fetchIfNeeded() async {
    guard !hasFetched else { return }     // ← latched for the life of the process
    hasFetched = true
    …
}
```

So a Gist edit reaches a user **only on a cold launch.** iOS keeps apps resident for days — someone who opened HootOwl on Monday and backgrounds it may not cold-launch again until Thursday. Your five-minute fix would take three days to reach them.

**Fix, and this is the clever bit:** refetch on foreground with a floor (15 minutes, so it isn't chatty), **and refetch immediately when a schema break is detected.** The break becomes its own trigger. A broken app checks for its own cure every poll cycle, so the heal latency after you save the Gist is **one poll — about two minutes — not one launch.**

That single detail is most of the difference between your #3 working and merely being true on paper.

### 2. DEBUG builds never read the Gist at all

`loadCached()` returns hardcoded scaffolding in DEBUG (`ContactConfig.swift:187-200`) and never consults the Gist. Sensible for contact emails; fatal for an alias map, because **you could not test the mechanism in the simulator** — the one place you'd want to rehearse it before trusting it in an emergency.

Needs a DEBUG path that can opt into the real config, or the whole escape hatch is untested code you first exercise during an actual outage.

### 3. The raw Gist URL is CDN-cached

`gist.githubusercontent.com/…/raw` is served through GitHub's edge with cache headers. Your edit is not instantly visible, so "five minutes" is "five minutes plus however long the edge holds it." Needs a cache-buster (`?t=<epoch>`) or a `URLRequest` with `.reloadIgnoringLocalAndRemoteCacheData`.

Small, but without it the mechanism's headline promise is wrong by an unpredictable amount, in the one situation where you are watching a clock.

---

## The actual upper bound — since you asked for it

There is one more rung, and you should see it even though I don't think you should build it.

The scheduled job from your #1 is **already fetching and decoding both feeds every 15 minutes.** So it could also *republish* them, normalised into the shape the app expects, at a static URL. Then the config flips the app to that mirror — and **even the bottom row of the table becomes an OTA fix**, because you'd be changing a script in a repo instead of a binary in the App Store.

That is the real ceiling: **no schema change Taipei can make would require a release.**

The cost is that you stop being an app developer and start also operating a data pipeline. Your app's data is then only as available as your job is — and a free cron that silently stops running is a much quieter failure than a crash. For two cities I think that trade is wrong today.

**My recommendation: build the detector, write the mirror down as a documented escalation, don't build it.** If a third and fourth city arrive, or if Taipei turns out to churn more than twice a year, it stops being over-engineering and the detector is already 80% of it.

---

## Revised plan, in the order I'd do it

| # | What | App code? | Size | Why this order |
|---|---|---|---|---|
| **1** | **Scheduled feed-shape detector** | **none** | ~40 lines + cron YAML | Solves your #1 outright. Needs no build, no review, no binary. **Makes everything below it optional rather than urgent** |
| **2** | **Layers 0 + 1 + 2** — never `fatalError` on remote input, drop the two unrendered mandatory fields, lossy decode with a floor | yes | ~65 lines, 6 files | The OTA fix is worthless if the app dies before it can read the config. This is the foundation, not an alternative |
| **3** | **Tolerant decoding** — Layer 3 casing/separators + type tolerance (`203` / `"203"`) | yes | ~70 lines | Two whole rows of the table fixed with **no config and no operator action**. Best value per line after #2 |
| **4** | **Config-driven everything** — alias map, date format, feed URL, plus the three fixes above | yes | ~200 lines | Your #2 and #3, properly. The biggest piece, and the one with a schema to get right |
| — | Mirror / republish | n/a | real infrastructure | Documented, not built |

**What I'd change about my earlier advice:** I said ship Layers 0–2 and defer the alias map, and I'd now split that differently. **#1 and #2 before the archive** — one is free and outside the app, the other is ~65 lines and closes a shipping crash. **#3 is cheap enough to come along.** Whether **#4** makes build 1 is genuinely yours: deferring it is safe *once #1 exists*, because then a rename costs you a release you start the same hour, rather than a disaster you hear about from a user. But it is also cheapest to write now, while all of this is in your head rather than six months from now in an outage.

If you want it all in build 1, say so and I'll start at #1 and work down.

---

# When a field name changes

**Design note, 2026-10-16. Nothing shipped yet.** Written because the quick patch was the wrong instinct — Jim: *"no wait, this need to be a dedicated obsidian pages, 'When field name changes', and we need to design the best solution for it."*

> [!question] The question that started it
> *"if Taipei changes a field name, does that mean the data will not be proceeded any further? if this is the available, there will be no available data until I change the field name accordingly and release it?"*

---

## The short answer

**No — it's worse than that.** The app does not lose the data and carry on. **It crashes.** On a real iPhone, in Release, roughly **every two minutes**, for as long as the rename stands.

There is no "no available data" state to fall back into, because the code never gets that far. `fatalError` is reached before anything can decide what to show.

So the honest version of Jim's question is: *if Taipei renames one field, HootOwl becomes unusable until I ship an update — and the App Store takes 1–3 days.*

That is the problem this page is about.

---

## What actually happens today

### The live availability path — the dangerous one

Taipei's live counts come from `TCMSV_allavailable`, polled every ~2 minutes. The decode lands here:

```swift
// Mu1Base+Ext.swift:221-226  — minuteFlow(), the LIVE path
}catch DecodingError.keyNotFound(let key, let context) {
    fatalError("[\(self.id)] Missing key: \(key.stringValue) — Path: \(context.codingPath)")
}catch{
    fatalError("\(self.urlMinutely.absoluteString) \(error.localizedDescription)")
}
```

**Both arms are unguarded.** No `#if DEBUG`, no `targetEnvironment(simulator)`. This is the shipping binary.

`minuteFlow()` is live — called at `Mu1Base+Ext.swift:78` and `:336`. (`minutelyRetrieveFlow()` is the dead twin; its call at `:337` is commented out.)

### Everything that must be present or the app dies

This is the **mandatory decode surface** for Taipei's live feed. Any one of these missing, renamed, or reshaped reaches the `fatalError` above:

| # | What | Where | If it changes |
|---|---|---|---|
| 1 | `data` object | `AllAvailable.swift:20` | crash |
| 2 | `data.UPDATETIME` **as a String** | `:45` | crash |
| 3 | …parsing as exactly `EEE MMM dd HH:mm:ss 'CST' yyyy` | `:47` | crash — **a date *format* change is as fatal as a rename** |
| 4 | `data.park` array | `:57` | crash |
| 5 | `id` on every item | `:128` | crash |
| 6 | `availablecar` on every item | `:129` | crash |
| 7 | `availablemotor` on every item | `:130` | crash — **and the app never shows it** |
| 8 | `availablebus` on every item | `:131` | crash — **and the app never shows it** |
| — | `ChargeStation` | `:132` | safe (optional) |

> [!danger] Rows 7 and 8 are the finding
> `availablemotor` and `availablebus` are **mandatory to decode and read nowhere in the app.**
>
> Verified by grep. Every mention is the struct itself, a `static let` fixture, or a JSON sample inside a doc comment:
> - `availablemotor` → `AllAvailable.swift:130, 144, 145, 221` · `CyclopsModel.swift:381`
> - `availablebus` → `AllAvailable.swift:131, 145, 222` · `CyclopsModel.swift:382`
>
> No view renders them. No model derives from them. **Two of the eight ways Taipei can kill the app buy us nothing at all.**

### Why a default value doesn't save you

This is the trap, and it's worth stating because it looks wrong:

```swift
var availablemotor:Int = 0     // ← looks optional. IS NOT.
```

In Swift's `Codable`, **a default value does not make a key optional.** The synthesized decoder still calls `decode(Int.self, forKey: .availablemotor)` and still throws `keyNotFound`. Only `Int?` is allowed to be absent.

And `park` is `[ParkAvailableItem]` — **array decoding is all-or-nothing.** One malformed lot out of ~1,700 throws, and all 1,700 are discarded.

### The other paths, for completeness

| Path | Site | On a real iPhone |
|---|---|---|
| Taipei daily description | `TaipeiObs.swift:91` (keyNotFound) | **crash** — unguarded |
| Taipei daily description | `TaipeiObs.swift:94` (everything else) | throws — guarded to macOS/simulator |
| Taipei minutely async | `TaipeiObs.swift:24` | dead today — a stray `fatalError()` *after* a successful decode |
| New Taipei CSV, column count ≠ header count | `NewTaipeiCityObs.swift:131` | `continue` — **correctly guarded** |
| New Taipei CSV, column count ≠ 2 | `NewTaipeiCityObs.swift:137` | **crash** — unguarded |

> [!warning] A second, separate latent crash — New Taipei
> `guard fields.count == 2 else {fatalError("2field,id+count")}` has no build guard.
>
> New Taipei's feed is CSV and the parser compares **column count, not column names** — so a *rename* there is harmless. But **if New Taipei adds a third column**, every row passes the header-count check at `:131` and then dies at `:137`. In Release. On device.
>
> A city adding a column to its own CSV export is an entirely ordinary thing for a city to do.

---

## The principle

> **Remote data is untrusted input.**
>
> Three consequences, in priority order:
> 1. It must **never** crash the app.
> 2. A failure must lose **only what actually broke** — not the other 1,699 lots, not the previous good data.
> 3. A rename should be fixable **without App Review.**

`fatalError` is the right tool for *"I, the programmer, have broken an invariant."* It is the wrong tool for *"a government web server sent me something I didn't expect."* The first can't happen in a shipped build; the second happens whenever Taipei's IT department feels like it.

---

## The design — six layers

Each layer is independent and independently shippable. They're ordered by value per line changed.

### Layer 0 — never `fatalError` on remote input

**The floor. Non-negotiable.**

```swift
}catch DecodingError.keyNotFound(let key, let context) {
    ffl("📛 [\(self.id)] availability schema changed — missing '\(key.stringValue)' at \(context.codingPath.map(\.stringValue).joined(separator: "."))", .error)
    self.schemaBreak = SchemaBreak(key: key.stringValue, at: .now)
    self.setMinutelyTimer(mg0: self.minutelyPubInterval)   // keep polling; it may come back
}catch{
    ffl("📛 [\(self.id)] availability parse failed: \(error)", .error)
    self.setMinutelyTimer(mg0: self.minutelyPubInterval)
}
```

Two details that matter:

- **Keep the timer running.** An early `return` without `setMinutelyTimer` silently stops polling forever — the feed could heal and the app would never find out. This is the easy mistake to make while fixing the hard one.
- **Do not publish.** `availableVbj.send(nil)` would blank the map. Say nothing and the last good values stay up, which is what Layer 4 wants.

**Sites:** `Mu1Base+Ext.swift:222`, `:225`, `TaipeiObs.swift:91`, `NewTaipeiCityObs.swift:137`, and delete the stray `TaipeiObs.swift:24`.

**Effect:** "crash every 2 minutes" becomes "counts freeze." Nothing else in this document matters until this is done.

---

### Layer 1 — decode only what you render

**The highest-leverage change in the whole page, and it's a four-line diff.**

```swift
struct ParkAvailableItem: Codable {
    var id: String
    var availablecar: Int
    var ChargeStation: TChargeStation? = nil
    // availablemotor / availablebus deleted 2026-10-16: mandatory to decode,
    // rendered nowhere. Two ways for Taipei to break us, for no feature.
}
```

Mandatory per-item surface: **4 fields → 2.** Total mandatory surface: **8 → 6.**

The fixtures at `:143-145` need their arguments trimmed; nothing else references the fields.

> [!tip] The general rule this is an instance of
> **Every mandatory field is a liability. A mandatory field nothing renders is a liability with no asset behind it.**
>
> Worth re-running the same grep on `TCMSV_alldesc` and the daily-description structs before release — the same pattern is likely there.

---

### Layer 2 — lossy array decoding, with a floor

Today one bad lot discards all ~1,700. Fix it by decoding the array element-by-element and keeping what works:

```swift
/// Decodes `[T]` element-wise. A bad element is skipped, not fatal.
struct Lossy<T: Decodable>: Decodable {
    let values: [T]
    let skipped: Int
    init(from decoder: Decoder) throws {
        var c = try decoder.unkeyedContainer()
        var good: [T] = []; var bad = 0
        while !c.isAtEnd {
            do { good.append(try c.decode(T.self)) }
            catch { bad += 1; _ = try? c.decode(Blank.self) }   // consume and move on
        }
        self.values = good; self.skipped = bad
    }
    private struct Blank: Decodable {}
}
```

Then the floor, which is the part that keeps this honest:

```swift
let rate = Double(decoded.values.count) / Double(decoded.values.count + decoded.skipped)
guard rate >= 0.70 else {
    ffl("📛 [\(id)] only \(Int(rate*100))% of lots decoded — rejecting payload, keeping previous", .error)
    return    // Layer 4 takes over
}
```

**Why a floor and not just "take whatever decodes":** if Taipei renames `availablecar`, *every* item fails and lossy decoding yields an empty array — which, published, blanks the map and looks like "no parking anywhere." A floor turns a total schema break back into Layer 4's keep-last-good, while still letting a single corrupt row be shrugged off.

**My call: 70%.** Low enough that a genuinely partial outage still shows something, high enough that a schema break can't masquerade as one. It is one constant and trivially tunable.

---

### Layer 3 — normalised key matching

Catches the cheap half of real-world renames for free: casing and separators.

```swift
/// Matches coding keys case- and separator-insensitively:
/// availablecar == availableCar == available_car == AVAILABLECAR
struct LooseKey: CodingKey { … }
```

Implemented as a custom `init(from:)` that normalises both the incoming keys and the expected ones to lowercase-alphanumeric before comparing.

**What it covers:** `availablecar` → `availableCar` → `available_car` → `AvailableCar`. In practice a large share of government-feed churn is exactly this — a backend rewrite changing the serializer's naming convention, not anybody renaming a concept.

**What it does not cover:** `availablecar` → `carRemain`. That's a true rename, and it needs Layer 4.

---

### Layer 4 — keep last good, let the existing colours speak

**The app already has the whole user-facing half of this built, and it's unused in this scenario** because we crash before reaching it.

`AvailFreshness` (5-minute / 30-minute thresholds) already drives:
- the Cyclops hero colour — `CyclopsView.swift:127`, `MncplCyclopsScreen.swift:52`
- the stale notice in `CoverageNoticeView.swift:233`

So Layer 0's "don't publish, don't blank" gets the right behaviour for free: the last known counts stay on screen and **visibly age** — fresh → aging → stale — exactly as they would if the user walked into a tunnel. No new UI. No new strings. No new localisation.

**This is the layer that answers "will there be no available data?"** There will be data. It will be the last data we trusted, honestly labelled as old.

One thing to add: after a sustained break (say 30 minutes of consecutive failures), the stale notice should say *why* — a data-source problem rather than a connectivity one, with the municipal report contact from the Gist. That's one new string and it can come later.

---

### Layer 5 — the escape hatch: a key-alias map in the Gist

**The only layer that fixes a true rename without an App Store release.**

`ContactConfig` already exists and already does exactly this shape of job — a JSON blob on a Gist, fetched on launch, cached in `@AppStorage`, no SDK, no console. Its own doc comment states the reason it exists: *"Adding a key here needs no app release — which is the whole reason this file exists."*

Add one optional section:

```json
{
  "version": 2,
  "contacts": { … },
  "support":  { … },
  "fieldAliases": {
    "taipei.available": {
      "availablecar": ["carRemain", "available_car_count"],
      "id":           ["parkId", "PARKID"]
    }
  }
}
```

The decoder tries the canonical key, then each alias in order. Alias list empty or absent → today's behaviour exactly.

**What this buys:** Taipei renames `availablecar` → `carRemain` at 09:00. Jim edits a Gist at 09:05. Every app that has launched since is working by 09:06. **No build, no archive, no review, no 1–3 day wait.**

**What it costs:** a config schema version bump, a custom `init(from:)` that consults a runtime table, and a cache-timing question (how long until a running app picks up a changed Gist). Perhaps 100–150 lines and a real test pass.

> [!note] Is it worth it for a two-city app?
> Honest accounting. **Without it,** a true rename costs 1–3 days of a broken app. **With it,** five minutes.
>
> How often do Taiwanese open-data feeds rename fields? Unknown — and `AllAvailable.swift:150` already carries a `#warning("the data and metadata is chaning will break this ")`, which says past-Jim had seen enough churn to leave a note about it.
>
> **My call: design it now, ship it after submission.** Layers 0–4 take the failure from *crash* to *visibly stale*, which is survivable for the 1–3 days a release takes. Layer 5 turns survivable into a non-event, but it is the only layer that adds a schema and a custom decoder, and adding that in the week before a first submission is how first submissions slip.

---

### Layer 6 — find out before the users do

Two separate things, both small.

**Observability.** The swallowed catches throughout the retrieval path log at `.debug`, which means a schema break would be invisible in a TestFlight console. Raise the ones that mean *"the feed changed shape"* to `.error`, and record a `schemaBreak` on the proto so `AvailDQIScreen` can show it. The DQI machinery (`AvailDataQuality`, `computeAvailDQI` at `Mu1Base+Ext.swift:719`) already counts static vs feed vs no-signal lots — a schema-break field belongs beside those counts.

**A pre-release contract test.** One test that fetches both live feeds and decodes them, run before every archive:

```
decode(TCMSV_allavailable) from live Taipei URL   → ≥ 1 item, rate ≥ 0.95
decode(NTPC CSV)          from live NTPC URL      → ≥ 1 item, header count == expected
```

It will be flaky — it's a network test against a government server — so it must never gate CI. It's a **release checklist line in [[operations]]**, run deliberately, which is where it's actually useful: it tells you the feed still matches the build you're about to ship.

---

## What I recommend shipping

> [!warning] Superseded 2026-10-18 by **Claude's answer** at the top of this page.
> Jim raised the ceiling: detection must reach *him* first, and the fix must reach users without a download. The table below is kept because the per-layer sizing still holds — but the **order** and the verdict on Layer 5 are replaced by the revised plan above.

| Layer | Ship | Size | Why |
|---|---|---|---|
| **0** — no `fatalError` on remote input | **before submission** | ~20 lines, 5 sites | Turns a crash into a non-event. Nothing else counts without it |
| **1** — drop unrendered mandatory fields | **before submission** | ~4 lines | Removes 2 of 8 break causes for zero cost |
| **2** — lossy array + 70% floor | **before submission** | ~40 lines | One bad lot stops discarding 1,700 |
| **4** — keep last good | **before submission** | falls out of Layer 0 | Already built; just needs to be reachable |
| **5a** — raise log levels to `.error` | **before submission** | ~10 lines | So a break is visible in TestFlight |
| **3** — normalised key matching | after submission | ~60 lines | Covers casing churn; nice, not urgent |
| **5** — Gist alias map | after submission | ~150 lines | The real insurance. Too big for release week |
| **6b** — live-feed decode test | after submission | ~30 lines + runbook | Add to the [[operations]] checklist |

**The pre-submission set is roughly 75 lines across six files**, and it changes the answer to Jim's question from

> *"the app crashes every two minutes until you ship an update"*

to

> *"the counts freeze and visibly go grey, and you have 1–3 days to ship a fix at your own pace."*

That is the gap worth closing this week. Layer 5 closes the remaining gap and can wait.

---

## Open for Jim

> [!done] Answered 2026-10-18
> ~~**Layer 5 — in or out?**~~ **In.** Jim's comment settles it: *"users get the fix w/o downloading and upgrade."* It is now item **#4** of the revised plan, and the only remaining question is whether it lands in build 1 or build 2.

1. **Does the config layer (#4) make build 1?** Yours. Deferring is safe **once the detector (#1) exists** — a rename then costs a release you start the same hour. Shipping it now is cheaper than writing it six months from now during an outage.
2. **The 70% floor.** Alternative: any failure at all rejects the whole payload and keeps last-good. Simpler, more conservative, throws away good data when one lot is malformed. I prefer the floor; it's one constant either way. *(Still open.)*
3. **Where should the detector shout?** A GitHub issue, an email, or both. An issue is free, dated, and already where the repo lives; email reaches you on a phone. Default if you don't say: **both** — issue for the record, email so you actually see it.
4. **New Taipei's `:137`** is a crash the moment that city adds a CSV column. It's inside Layer 0 and costs nothing extra. Flagging it because it's a *second* bug found while designing for the first; it has its own line in [[bugs]] under 2026-10-16.

---

## Related

- [[bugs]] — **2026-10-16** carries the short version of this as a bug entry, with the seven `fatalError` sites in one table
- [[2026-10-15]] — the crash that started this: Taipei's daily payload truncated and spliced upstream, byte-identical across fetches. A corrupt payload, not a rename — but it reached the app through the same unguarded `fatalError`
- [[data-sources]] — the two portals, their contacts, the re-check schedule
- [[operations]] — where the detector's runbook goes, and the Gist runbook that item #4 extends
- [[decisions]] — this page's conclusion belongs there once Jim has chosen
