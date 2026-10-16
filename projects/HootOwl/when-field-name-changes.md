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

1. **Layer 5 — in or out?** Not *whether* it's correct, but whether a two-city app earns the 150 lines. My answer above is "design now, ship after submission." Say if you'd rather it went in sooner, or never.
2. **The 70% floor.** Alternative: any failure at all rejects the whole payload and keeps last-good. Simpler, more conservative, throws away good data when one lot is malformed. I prefer the floor; it's one constant either way.
3. **New Taipei's `:137`** is a crash the moment that city adds a CSV column. It's inside Layer 0 and costs nothing extra. Flagging it because it's a *second* bug found while designing for the first, and it deserves its own line in [[bugs]].

---

## Related

- [[bugs]] — **2026-10-16** carries the short version of this as a bug entry, with the seven `fatalError` sites in one table
- [[2026-10-15]] — the crash that started this: Taipei's daily payload truncated and spliced upstream, byte-identical across fetches. A corrupt payload, not a rename — but it reached the app through the same unguarded `fatalError`
- [[data-sources]] — the two portals, their contacts, the re-check schedule
- [[operations]] — where the Layer 6 release-checklist line goes, and the Gist runbook Layer 5 extends
- [[decisions]] — this page's conclusion belongs there once Jim has chosen
