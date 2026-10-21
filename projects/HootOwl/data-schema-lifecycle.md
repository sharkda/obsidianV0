# Data schema lifecycle

**How HootOwl survives, detects, announces and repairs an upstream data change.** Clean rebuild 2026-10-21, replacing [[when-field-name-changes]] — that page is kept as the working-out and the jim/claude thread, but three of its plan tables superseded each other and two different things were both called "#4". Nothing here is shipped yet.

> [!abstract] The whole thing in five lines
> 1. Taipei and New Taipei change their feeds **about once every four or five months** — seven times in 31 months, and **never once a rename**.
> 2. Today a change can **crash the app every two minutes** in Release, because `fatalError` is used as the handler for untrusted network input.
> 3. The app should **survive** any change, **detection should happen outside the app** so we learn before any user does, and the user should be **told honestly** why the numbers are old.
> 4. Most changes are then fixable by **editing a Gist** — no release, no App Review.
> 5. A structural reshape still needs a release. Nothing can buy that (guideline 2.5.2), so everything above exists to make those 1–3 days uneventful.

---

## The record — what upstream has actually done

Reconstructed from git. Full table with per-row confidence in **[[data-sources#Incident log — every time a feed changed under us]]**.

| Failure class | Times | Worst example |
|---|---|---|
| **A mandatory field quietly went missing** | **3** | `tel`, 2026-03-05 — two years in, model settled. Fixed reactively, after the break, with a release |
| Transport / access changed | 1, severe | NTPC bulk CSV WAF-blocked 2026-09-16 — an F5 page served as **HTTP 200**. Availability dead city-wide |
| Payload corrupted upstream | 1, severe, **open** | Taipei daily truncated and spliced, 2026-10-15. Byte-identical across fetches |
| Structure reshaped | 1, discounted | Socket list `[String]` → `[{…}]`, 2024-04-25. App was 7 weeks old; likely our own guess being corrected |
| **A field was renamed** | **0** | — |

**Two things this changes about the obvious design.** A rename is the headline fear and the empirical non-event, so a key-alias map goes last. And the recurring failure — *we insisted on a field, it vanished* — has been fixed three times reactively, one field at a time, after a break, with a release. **That is the loop to break.**

---

## The lifecycle

Six stages. Each is independently shippable and the order is the order to build them.

```
   ① upstream changes
          ↓
   ② app SURVIVES it ──────────→ nobody crashes; last good numbers visibly age
          ↓
   ③ we DETECT it (outside the app) → we know before any user does
          ↓
   ④ users are TOLD ──────────→ honest notice, raised by a Gist flag
          ↓
   ⑤ we FIX it ───────────────→ Gist edit if possible, release if reshaped
          ↓
   ⑥ running apps HEAL ───────→ within one poll, not one cold launch
```

---

### ① The damage today

`Mu1Base+Ext.swift:222` and `:225` — the **live** availability decode — both `fatalError`, **unguarded**, in the shipping binary. `minuteFlow()` polls every ~2 minutes.

**Taipei live feed: 8 things that must all be present.** `data` · `data.UPDATETIME` as a String · parsing as exactly `EEE MMM dd HH:mm:ss 'CST' yyyy` · `data.park` · and per lot `id`, `availablecar`, `availablemotor`, `availablebus`.

**Taipei static feed: 15 more** in `ParkDescItem` — `id, area, name, type, summary, address, payex, tw97x, tw97y, totalcar, totalmotor, totalbike, totalbus, FareInfo, EntranceCoord`.

Two traps worth knowing, because both look wrong:

- **A `Codable` default does not make a key optional.** `var availablemotor: Int = 0` still throws `keyNotFound`. Only `Int?` may go missing. Past-you already wrote the scar at the head of `ParkDescItem`: *"some fileds are optional, otherwise the parsing of complete JSON document will faile."*
- **Array decoding is all-or-nothing.** One malformed lot out of ~1,700 discards all 1,700.

Also unguarded and unrelated to renames: **`NewTaipeiCityObs.swift:137`** crashes Release the moment New Taipei adds a **third CSV column**. That parser compares column *count*, never names, so renames there are harmless — a new column is not. Logged in [[bugs]] under 2026-10-16.

---

### ② Survive — the app must not die *(mine)*

Three changes, ~65 lines, six files. **Nothing else on this page matters until these are in**, because an over-the-air fix is worthless if the app dies before it can read the config.

| | What | Why |
|---|---|---|
| **a** | **No `fatalError` on anything parsed from the network.** 5 sites. Log at `.error`, keep the poll timer running, **do not publish `nil`** | Turns "crash every 2 min" into "counts freeze". An early `return` that forgets `setMinutelyTimer` silently stops polling forever — the easy mistake while fixing the hard one |
| **b** | **Optional by default.** Audit both feeds; every field that is not load-bearing becomes optional with a sane default. Delete `availablemotor` / `availablebus` outright — mandatory to decode, **rendered nowhere** (grep: struct, fixtures and doc comments only) | Directly kills the failure class that has recurred **3 times**. Doing the remaining 15 at once is less work than any other item here |
| **c** | **Lossy array decode with a 70% floor.** A bad lot is skipped, not fatal. But if fewer than 70% of lots decode, reject the whole payload and keep the previous one | One bad lot stops discarding 1,700. The floor stops a *total* schema break masquerading as a partial outage — if `availablecar` is renamed, every item fails and lossy decoding would otherwise publish an empty map |

**What the user sees, free of charge.** Because ②a declines to publish rather than publishing `nil`, the last known counts stay on screen and **visibly age** through the existing `AvailFreshness` 5/30-minute colours — already wired into `CyclopsView.swift:127`, `MncplCyclopsScreen.swift:52` and `CoverageNoticeView.swift:233`. No new UI, no new strings, no new localisation. It looks exactly like walking into a tunnel, which is honest.

---

### ③ Detect — outside the app *(mine to build, one setup step yours)*

> [!important] The correction that matters most on this page
> My first draft put detection *inside* the app — raise the log levels, show it on the DQI screen. That only reports **after a user has already hit it**, which is the loop Jim rejected.
>
> **The feeds are public. We can watch them ourselves, with no app involved at all.**

A scheduled job — GitHub Actions — fetches both cities' feeds, decodes them against schema fixtures committed in the repo, and shouts when the shape stops matching.

| | In-app telemetry | **Scheduled job** |
|---|---|---|
| Catches a break when nobody is using the app, at 3am | ❌ | ✅ |
| Catches it **before** the first user | ❌ | ✅ |
| Needs a server | ✅ | ❌ |
| Needs app code, a build, a review | ✅ | ❌ **none** |
| Needs a privacy-label change | ✅ | ❌ |

> [!warning] Why in-app telemetry is the actively worse choice
> Reporting from the app means **collecting diagnostic data** — a declarable category in Apple's privacy nutrition labels. This app's labels commit to *precise location, app functionality, foreground-only* and nothing else. That's a label change, a new justification and new App Review surface, on a first submission, for a signal available free from a public URL.

**It would have caught all seven incidents** — including the WAF block and the truncation, which are not schema changes at all. Five of the seven were failure modes we had not thought of. That is the argument for building it first.

> [!caution] Two practical constraints I'd rather find now than later
> **Cadence vs. billing.** GitHub Free gives private repos ~2,000 Action minutes/month; public repos are unlimited. A 15-minute cron is ~2,880 runs/month and **overruns the private allowance**. Every 30 minutes is ~1,440 and fits. For a feed that reshapes twice a year, 30-minute latency is immaterial — **so: every 30 minutes.** (Worth re-checking the current limits; billing changes.)
>
> **Scheduled workflows are disabled after ~60 days of repo inactivity.** `sharkda/hootOwl` is active today, but a quiet winter would silently switch the detector off. The job should therefore also be the thing that proves it ran — a heartbeat, so silence is itself a signal.

---

### ④ Tell the users — Jim's safety net *(mine to build, copy approval yours)*

> [!quote] Jim, 2026-10-21
> *"if we have a detector offline, I'd also want a 'safety net', I want to have a code inside the App that will check from my git, when we have a detection of app might break, we will raise a flag, and let users know… if the app might break, after a significant reshape, maybe we can have a crucial flag but I am guess this will require a lot of codes to stop the app from loading the data entirely and this is very unlikely to happen"*

**Yes — and it's far cheaper than you're guessing, because the pipe already exists.** `ContactConfig` is already a JSON blob on a Gist, fetched and cached with no SDK. The flag is **one optional struct plus one banner**. The genuinely expensive parts (⑥) are shared with every other config item, so they're paid once.

```json
"feedStatus": {
  "taipei":        { "state": "ok" },
  "newTaipeiCity": { "state": "degraded", "since": "2026-10-21" }
}
```

**Two states, not three.** `ok` shows nothing. `degraded` shows a notice. There is no third level, because:

> [!danger] No kill switch — and the reason is better than the cost
> You guessed a "crucial flag" would need a lot of code to stop the app loading data. It would, but that isn't the objection. **A remote kill switch is a way for *us* to break a working app.** ② already makes bad data non-fatal and keeps the last good numbers visibly ageing, so there is nothing for a kill switch to save — while a flag left stuck on, or set by a false positive, would be worse than any bug it guards against. A severity *word* in the copy is nearly free; a remote off-switch is a liability. **Recommend against.**

> [!tip] The prize: the detector can raise the flag itself
> ③ already has a GitHub token. Patching a Gist is one API call. So: **Taipei breaks at 09:00 → the job notices at 09:30 → the job patches the Gist → every app foregrounding after that carries the notice.** You find out from the same email, at your own pace. **No action from you at the moment it breaks.**
>
> Guarded, though: require **3 consecutive failed checks (~90 minutes)** before auto-flagging, so a ten-minute upstream 500 never alarms anyone. The automatic flag is **advisory only**; stronger wording stays a manual edit by you.

**The copy needs care, and it is yours to approve.** Draft only — 繁體中文 first, per the project convention:

> 「台北市的即時車位數暫時無法更新，畫面上的數字可能已經過時。我們已經在處理。」
> *"Live space counts for 台北市 aren't updating right now, so the numbers you see may be out of date. We're on it."*

**Deliberately not** *"the app might break, please update as soon as practical."* Three reasons: users don't have a schema, they have a parking problem; "might break" invites a one-star review for a working app; and an update is only the answer for a reshape, which is the rarest class. If an update genuinely is the fix, that sentence can be a second, separate line the flag turns on.

> [!warning] Release gate — this must be verified before every archive
> `loadCached()`'s DEBUG scaffolding does not apply to Release, so **a reviewer reads the live Gist.** If a flag is set during review, a reviewer sees an alarming message about the app they are assessing. **`feedStatus` must be `ok` for both cities before submission**, and that belongs on the checklist in [[operations]].

---

### ⑤ Fix — how far an over-the-air repair reaches *(mine to build, timing yours)*

| What upstream changed | Fixable without a release? | Heal time |
|---|---|---|
| A key **recased** — `availablecar` → `availableCar` | ✅ no config even needed — tolerant keys | instant |
| A value's **type** changed — `203` → `"203"` | ✅ no config needed — tolerant decoder | instant |
| A key **renamed** — `availablecar` → `carRemain` | ✅ alias map in the Gist | minutes |
| `UPDATETIME`'s **date format** changed | ✅ *if the format string is config too* | minutes |
| The **endpoint** moved, or a v2 published | ✅ *if the URL is config too* | minutes |
| **Structure reshaped** — array becomes a nested object, CSV becomes JSON | ❌ | needs a release |

The date-format and URL rows are cheap and both have precedent: `UPDATETIME`'s format is hardcoded at `AllAvailable.swift:47` and is one of the eight fatal items for no reason, and the 2026-09-16 WAF incident was an endpoint problem.

> [!note] Apple's actual limit, so we design inside it
> **Guideline 2.5.2:** an app may download and act on **data and configuration**; it may not download and execute **code** that changes its features. An alias map, a format string and a URL are all data — this is exactly what Firebase Remote Config does. "Push a code patch OTA" is not available, which is why ② matters: it decides whether those 1–3 days look like *numbers going grey* or *an app crashing every two minutes*.

---

### ⑥ Heal — so the fix reaches apps already running *(mine)*

**This is where the real work is**, and it's shared by ④ and ⑤ — pay it once.

| | Problem today | Fix |
|---|---|---|
| **a** | **`ContactConfig.swift:264-270` latches `hasFetched`** — the config is fetched **once per process, ever**. A Gist edit reaches a user only on a **cold launch**, and iOS keeps apps resident for days. A five-minute fix would take three days to arrive | Refetch on foreground with a 15-minute floor, **and refetch immediately when a schema break is detected.** The break triggers its own cure, so heal latency is **one poll (~2 min), not one launch.** This single detail is most of the difference between the OTA story working and merely being true on paper |
| **b** | **`loadCached()` returns hardcoded DEBUG scaffolding** (`:187-200`) and never reads the Gist, so the escape hatch would be **untestable in the simulator** — first exercised during the outage it exists for | A DEBUG path that can opt into the real config |
| **c** | **The raw Gist URL is CDN-cached.** "Five minutes" is five minutes plus however long GitHub's edge holds it — unpredictable, in the one situation where you're watching a clock | Cache-buster `?t=<epoch>`, or `.reloadIgnoringLocalAndRemoteCacheData` |

---

## The upper bound, for the record — not recommended

③ is already fetching and decoding both feeds every 30 minutes, so it could also **republish them normalised** to a static URL, and ⑤'s config could flip the app to that mirror. Then **no change Taipei can make would require a release** — even a reshape becomes a script edit.

That is the true ceiling. The cost is that you stop being an app developer and also become the operator of a data pipeline: the app's data is then only as available as the job is, and **a free cron that silently stops is a far quieter failure than a crash.** For two cities that trade is wrong today. If a third and fourth city arrive, or if churn turns out to be more than twice a year, revisit — ③ is already 80% of it.

---

## Actions

### Yours

| | Action | Blocking? | My default if you say nothing |
|---|---|---|---|
| **J1** | **Decide: do ④ ⑤ ⑥ land in build 1, or build 2?** ② and ③ go in regardless | **Yes — the one real decision** | **Build 2.** Once ③ exists, a break costs a release you start the same hour, not a disaster a user reports. But it's cheapest to write now, while it's all in your head |
| **J2** | **The 70% floor**, or reject-everything-on-any-failure? | no | **70% floor** |
| **J3** | **Where should the detector shout** — GitHub issue, email, or both? | no | **Both.** Issue for the dated record, email so you actually see it |
| **J4** | **Approve the user-facing copy** in ④ once I draft it properly, 繁中 + EN | before ④ ships | — |
| **J5** | **Is `sharkda/hootOwl` public or private?** Decides the detector's cadence and whether minutes are billed | before ③ ships | assume **private**, 30-minute cadence |
| **J6** | **Create a GitHub token with `gist` scope and add it as a repo secret** — only needed if you want the detector to raise the flag automatically (③ → ④ with no human step). Your account, so it has to be you | only for the auto-flag | — |
| **J7** | **Paste one `feedStatus` block into the existing Gist** with both cities `ok`. I'll give you the exact JSON | before ④ ships | — |

### Mine

| | Action | Depends on |
|---|---|---|
| **C1** | **② Survive** — 5 `fatalError` sites, optional-by-default audit across both feeds, lossy decode + floor. Build-verify all four configurations | J2 |
| **C2** | **③ Detect** — the script, the workflow, the committed schema fixtures, the heartbeat | J3, J5 |
| **C3** | **⑥ Heal** — foreground refetch + refetch-on-break + cache-buster + the DEBUG config path | J1 |
| **C4** | **④ Tell** — the `feedStatus` struct, the banner, and a proper copy draft for J4 in 繁中 + EN | J1, then J4 |
| **C5** | **⑤ Fix** — alias map, config date format, config feed URL. **Last**, and only if J1 says build 1 | J1 |
| **C6** | Two release-checklist lines in [[operations]]: run the live-feed decode before every archive, and **verify `feedStatus` is `ok` before submission** | C2 |
| **C7** | Write the outcome into [[decisions]] once J1 and J2 are answered — including the alias map being **designed and deliberately deferred**, so it isn't re-litigated in six months | J1, J2 |

**Shortest path to most of the value: C1 + C2.** ~65 lines of Swift and a cron job. That removes a shipping crash and means we learn about every future incident before a user does. Everything after that is about how gracefully we recover, not whether we survive.

---

## Decided, so it doesn't get re-opened

| Decision | Why |
|---|---|
| **Detection lives outside the app** | Catches breaks at 3am with nobody using the app, needs no build, and avoids declaring diagnostics collection on a first submission |
| **No remote kill switch** | A way for us to break a working app, guarding a case ② already makes non-fatal |
| **The key-alias map goes last** | 0 occurrences in 31 months. Designed, deferred, written down |
| **Optional-by-default is promoted above everything else in app code** | 3 of 7 observed incidents, the only class that has repeated |
| **No republishing mirror** | Makes us the operator of a pipeline whose silent death is quieter than a crash |
| **Copy describes what the user can see, not the schema** | "The app might break, please update" earns one-star reviews for a working app |

## Still open

1. **J1** — build 1 or build 2 for ④ ⑤ ⑥. Everything else is sequencing.
2. **J2** — the floor value.
3. Whether the 2026-10-15 corruption is still happening. ②c covers it either way, but [[2026-10-15]] has no closing entry.

---

## Related

- [[when-field-name-changes]] — the working-out: the jim/claude thread, the full crash-surface analysis, the six-layer draft this replaces
- [[data-sources]] — the incident log with per-row confidence, the two portals, their contacts, the re-check schedule
- [[bugs]] — 2026-10-16 carries the crash surface as a bug entry
- [[2026-10-15]] — the corrupt Taipei payload
- [[operations]] — where C6's two checklist lines go, and the Gist runbook ⑤ extends
- [[decisions]] — gets C7 once J1 and J2 are answered
