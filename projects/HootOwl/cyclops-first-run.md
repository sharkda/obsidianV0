# Cyclops — first-run 🕐 clock investigation

> Standalone topic note (same role as [[battery]]). Investigation dated **2026-08-07**.
> Origin: Jim's backlog entry 2026-06-29 — *"cyclops will keep the clock forever, until kill and restart"*.
> Status: **root cause partially confirmed by static reading. Not yet device-verified.** No code changed.

---

## Symptom (as reported)

Launch the app, open the Cyclops screen → every watched lot shows 🕐 and never resolves.
Force-quit and relaunch → the Available numbers appear **immediately**, "right off the bat".

---

## Why the "first run" framing undersells it

The 🕐 window opens on **any launch without a usable cache**, not just a fresh install. Three ways to get there:

| Path | Frequency |
|---|---|
| Fresh install | once per user — but it is the first impression |
| **Cache older than 24h** (`cacheMaxAge`, `Municipal+Cache.swift:47`) | **routine** |
| iOS purges `Library/Caches` under disk pressure | unpredictable, OS-controlled |

The middle row is the important one. Parking use is **episodic** — you open the app when you're driving somewhere. A user who parks twice a week crosses the 24h threshold *every single time*. For them this is not a first-run bug, it is the normal experience.

It lands at the moment of peak intent: user is in the car, looking for a space **now**. A grid of clocks reads as *broken*, not as *loading*.

The behavioural tail is worse than the delay. The workaround users discover is force-quit-and-relaunch — which **works**, because of the cache. That is exactly the path Jim took. A user who learns "you have to kill it and reopen it" has concluded the app is flaky, and that belief survives the fix.

It also undercuts the ratings plan (see [[decisions]] — ratings & feedback strategy): `requestReview` at a win moment can't fire if the opening 20 seconds of every other session is a stall.

---

## Mechanism — where the 🕐 actually comes from

The clock is `CyclopsItem.AvailFeedState.waiting`. It renders whenever a lot has **no availability row yet**.

| File | Lines | What |
|---|---|---|
| `hootowl/model/CyclopsModel.swift` | 47–73 | `AvailFeedState` enum; `.waiting → "🕐"` at `:52` |
| `hootowl/model/CyclopsModel.swift` | 235 | `carAvailable` = `carTrail.last?.count` |
| `hootowl/UI/Cyclops/CyclopsView.swift` | 32 | `isInfoMode = (carAvailable == nil)` — the only switch |
| `hootowl/UI/Cyclops/CyclopsView.swift` | 34–40, 134–145 | info-mode render; `:135` text label, `:142` emoji |

And `carTrail` only ever gets populated from a real availability row:

| File | Lines | What |
|---|---|---|
| `hootowl/model/CyclopsModel.swift` | 109–123 | mncpl init; `avail` lookup at `:112`, feedState 115–120 |
| `hootowl/model/CyclopsModel.swift` | 139–144 | appends **only** if `avail?.cars >= 0` |

> [!note] Cosmetic oddity worth a second look
> `CyclopsModel.swift:117` assigns `.waiting` even when a lot **has** a good number. Harmless today because `carAvailable != nil` wins at `CyclopsView.swift:32` — but it means the enum has no "live / healthy" case.

> [!warning] Unverified assumption
> `CyclopsModel.swift:112` matches `$0.parkId == pid` against the `tpe_` / `ntpc_`-prefixed watchList IDs. **I did not verify that `MncplParkItemAvail.parkId` carries the same prefix.** If it doesn't, that is a different and larger bug than anything below. Worth checking first.

> [!check] Gate checked 2026-08-17 — assumption was wrong in its premise, but the match still lines up
> The grep was run. **Neither side carries a `tpe_` / `ntpc_` prefix**, so there is no mismatch — but not for the reason the warning assumed.
>
> **The prefix convention is dead code.** `String.municipalityFromPidPrefix` (`MunicipalEnum.swift:44–48`) is the only thing in the codebase that knows about `tpe_` / `ntpc_`, and it has **zero callers** — the only grep hit is its own definition. Nothing applies the prefix and nothing consumes it.
>
> **Both sides of the `==` trace back to raw feed IDs:**
> - `MncplParkItemAvail.parkId` ← `TaipeiObs.swift:59` (`parkId: $0.id`) and `NewTaipeiCityObs.swift:62` (`parkId: fields[0]`) — raw, unprefixed (e.g. `060105`, checked literally at `NewTaipeiCityObs.swift:70`).
> - `MncplParkItem.id` ← `MncplParkItem.swift:173` passes `id: p0.id` straight through from the source record — also raw.
>
> So `avail.parkId == pid` compares raw-to-raw. **This does not outrank the other findings, and the plan does not reorder.** Finding 1 (no immediate fetch in `activate()`) stands as the main cause.
>
> **One residual worth a glance during the device run:** the hardcoded watchList seeds are `["TPE0080", "TPE0835", "TPE0270"]` (`MncplAllScreen.swift:47`, `AllTpeParkingScreen.swift:28`) — an uppercase `TPE####` shape that matches neither the raw feed format nor the `tpe_` convention. Probably legacy defaults from the old all-Taipei screen, but if a *default* pin never resolves while a *user-added* pin does, that's the explanation. Static reading only — not device-verified.

### Why relaunch works

`seedFromCache()` fills `parkAvPack` **synchronously inside `Municipal.init`**, before `wireCyclops()` runs — so on run 2 the numbers already exist when the screen first builds.

| File | Lines | What |
|---|---|---|
| `hootowl/Municipalities/framework/Municipal.swift` | 124–135 | init order — seed at `:133` runs **before** `wireCyclops()` at `:134` |
| `hootowl/Municipalities/framework/Municipal+Cache.swift` | 92–123 | `seedFromCache`; parkAvPack fill 109–111, `parkAvailVbj.send` `:114` |
| `hootowl/Municipalities/framework/Municipal+Cyclops.swift` | 23–46, 50–59 | `wireCyclops` sinks; `refreshCyclops()` at `:45` |

---

## Finding 1 — `activate()` fires no immediate fetch ⭐ main finding

`activate()` starts the daily timer and calls `setMinutelyTimer(mg0: 15)`, but **never fetches**. The first availability can only arrive when that 15-second timer ticks.

Combined with `loadOnStart`'s `asyncAfter` chain (protos activated at **+1.2s**), a cache-less launch shows 🕐 for **at least 16 seconds — guaranteed**.

**The tell:** `resumePolling()` *does* fire an immediate fetch (`:78`, `Task.detached { await self?.minuteFlow() }`) — that was added deliberately in Phase 3 for foreground resume. **Cold start never got the same treatment.** Compare the two functions side by side.

| File | Lines | What |
|---|---|---|
| `hootowl/Municipalities/framework/Mu1Base+Ext.swift` | **15–49** | `activate()` — no `minuteFlow()` call anywhere |
| `hootowl/Municipalities/framework/Mu1Base+Ext.swift` | 46–47 | `startTimerRetrievDaily()` + `setMinutelyTimer(mg0: 15)` |
| `hootowl/Municipalities/framework/Mu1Base+Ext.swift` | **73–79** | `resumePolling()` — `:78` is the immediate fetch `activate()` lacks |
| `hootowl/Municipalities/framework/Mu1Base+Ext.swift` | 277–305 | `setMinutelyTimer`; `mg0` path 281–282, timer built 301–305 |
| `hootowl/Municipalities/framework/Municipal+Ext.swift` | 35–46 | `loadOnStart` — +0.8s / +0.9s / +1.2s `asyncAfter` |

**Proposed fix:** fire one immediate `minuteFlow()` at the end of `activate()`, mirroring `resumePolling()`. One line.

**Impact if left:** every stale-cache session opens on ≥16s of clocks. User-visible, high-intent moment. Treat as launch-blocking.

---

## Finding 2 — `assessFences` writes to the wrong subject

`Municipal+Ext.swift:133–136`, the **cold-start branch** (taken whenever `activeFencesVbj` is empty, i.e. every first run):

```swift
if activeFencesVbj.value.count == 0 {
    let enclosing = allFencesVbj.value.filter({ $0.convexEnclosing(point: l2d) })
    allFencesVbj.send(enclosing)      // ← should be activeFencesVbj
    enteringNewZone = true
}
```

This doesn't merely fail to set the right subject — it **corrupts the source of truth**. `allFencesVbj` is the full fence list; the line overwrites it with only the fences enclosing the user. Both consequences are **unrecoverable without a relaunch**:

- User inside Taipei → `allFencesVbj` becomes `[taipei]`. New Taipei City is gone from the list for the rest of the process. Cross the boundary → `inactiveFences` can't find it → `FenceError.noEnclosingFenses` + error earcon.
- User **outside every fence** (anywhere not yet covered) → `allFencesVbj` becomes `[]`. From then on *every* `assessFences` call throws `.noFences` at `:129–131`. Permanently.

**Impact if left:** latent today — nothing currently reads `activeFencesVbj` to drive activation (see Finding 3). The reason to fix now is that it is **a landmine directly under the next feature**: the roadmap is expansion beyond Taipei/New Taipei, and the TODO at `Municipal+Ext.swift:121` says activation should become fence-driven. The day that gets wired, this typo becomes a hard failure for exactly the users the expansion targets — presenting as *"the new city doesn't work"*, which is far more confusing to debug than it is to fix today.

**Proposed fix:** one word — `allFencesVbj.send` → `activeFencesVbj.send`.

| File | Lines | What |
|---|---|---|
| `hootowl/Municipalities/framework/Municipal+Ext.swift` | **135** | the wrong-subject send |
| `hootowl/Municipalities/framework/Municipal+Fence.swift` | 18–29 | `onFencesLoaded` — sends `[]` when location unknown |
| `hootowl/Municipalities/framework/Municipal.swift` | 196–202, 207–221 | the two re-evaluation paths into `assessFences` |

---

## Finding 3 — the fence → activation link was never wired

`activeIds` is computed at `Municipal+Ext.swift:158` and **never used**. `ActDeActOnes(ids:)` at `:165–175` has **zero callers** anywhere in the codebase. Its own comment promises *"link the fenceEntry to the activate and deactivate of the zone Obs"* — that link does not exist.

Zones are only ever activated by the blanket `loadedProtos.map({ $0.activate() })` at `:43`. So **every proto polls for every user regardless of location** — someone in Taipei is also polling New Taipei City on the same cadence.

**Impact if left:**

- **Contradicts the battery work.** #1 / #6 / #9 / Phase 3 all went into cutting idle drain, while every user unconditionally polls every zone. This eats into those wins and may **muddy the deferred post-launch Energy Impact measurement** — see [[battery]].
- **Doesn't scale with the roadmap.** Cost is linear in cities. Two is tolerable; six means every user polls six endpoints continuously, plus multiplied load against public open-data endpoints that may rate-limit.

**This is a design decision, not a typo** — turning it on changes which zones fetch for whom. Log it in [[decisions]] and decide the activation policy; don't patch it blind.

---

## Ruled out — don't re-tread

- **`hootowlApp.swift:51–58` + `Municipal+Lifecycle.swift:24–36`** — Phase 3 landed 2026-06-26 and the bug was filed 2026-06-29, so a launch-time regression was the leading suspect. **It's clean:** at launch `activeProtos` is still empty (protos activate at +1.2s), so `resumeForForeground()` is a no-op.
- `Mu1Base+Ext.swift:65–70` (`pausePolling`) correctly leaves `onOffCancelBag` intact.
- `Mu1Base.swift:132` is inside `init`; `:448–453` (`stopPolling`) is only reachable from `deactivate()`.
- `minuteFlow`'s Combine cancellable **is** stored — `Mu1Base+Ext.swift:202`, `.store(in: &onOffCancelBag)`. (Initially suspected as a discarded `AnyCancellable`; it isn't.)
- `actMinutely` ordering is correct — `parkAvPack` set at `Municipal.swift:106` *before* the send at `:108`.

---

## Open question — what still needs a device run

Finding 1 proves a **≥16s** window. It does **not** prove "forever". The gap between those two is the silent bail-outs in `minuteFlow`:

| File | Lines | Bail-out |
|---|---|---|
| `hootowl/Municipalities/framework/Mu1Base+Ext.swift` | 144–162 | `<512 bytes` → return, retimer only |
| `hootowl/Municipalities/framework/Mu1Base+Ext.swift` | 163–177 | unchanged hash → return; `:174` `assert` fires in DEBUG when `availableVbj.value == nil` |
| `hootowl/Municipalities/framework/Mu1Base+Ext.swift` | 185 | `availableVbj.send(parsed)` — the success path |
| `hootowl/Municipalities/framework/Municipal+Ext.swift` | 73–90 | `actWire` — minutely sink 83–88 |

**Also check:** whether `previousMinutelyHash` persists across launches (`key_hash`, `Mu1Base.swift:464`). If it does, `:163–177` is reachable on a cold launch with `availableVbj.value == nil` — which would explain a genuinely indefinite stall.

### The single decisive observation

> **On a fresh install, does the clock clear on its own after ~15–20 seconds, or genuinely never?**
> That one answer splits Finding 1 from the `minuteFlow` bail-outs.

Log lines to capture on that run:

```
🐎 minutelyAvailable        ← success reached actMinutely
📦 minutely Received        ← bytes arrived
📛 ... < 512bytes           ← bail-out A
previousHash not changed    ← bail-out B
🗃 no cache snapshot to seed from
```

---

## Ranked plan

| # | Action | Cost | When |
|---|---|---|---|
| 1 | Immediate `minuteFlow()` in `activate()` | one line | **before launch** |
| 2 | `allFencesVbj.send` → `activeFencesVbj.send` (`Municipal+Ext.swift:135`) | one word | **before launch** (cheap insurance on a one-way failure) |
| 3 | Fence-driven activation policy (`ActDeActOnes`) | design decision | write up in [[decisions]], don't patch |

> [!important] Don't close the bug on Finding 1 alone
> Fixing #1 is worth doing regardless, but do not assume it resolves the report until a **fresh-install run has been observed clearing on its own**.

---

## Links

- Jim's original report: [[Jim's backlog]] — 2026-06-29
- Bug log entry: [[bugs]] — 2026-08-07
- Battery context (Finding 3 interacts with the deferred measurement): [[battery]]
- Cyclops state-lifting rationale: [[swiftui-state-and-identity]]
