
June 23

 Phase 2 is next — disk cache. Before I touch code, a few design questions worth settling so the

  implementation matches your intent:

  

  **Phase 2 design questions**

  

  1. **Storage backend.** Three reasonable options:

    - @AppStorage / UserDefaults Data — simplest, but Apple discourages storing larger blobs there (the

  parkAvPack snapshot could be 10-50KB per municipality).

    - A small JSON file in Library/Caches/ — proper place for "regenerable but useful to keep" data; iOS may

  purge under storage pressure (which is fine — we just re-fetch).

    - A small JSON file in Library/Application Support/ — survives storage pressure; more "permanent" feel.

  

  **Recommendation:** Library/Caches/. The cache is regenerable; survival across launches is the only

  requirement.

  2. **What exactly to cache.**

    - **Latest user location:** one CLLocationCoordinate2D + timestamp. Tiny.

    - **Latest** **MncplParkAvPack** **per municipality:** the full pack (id + cars + chargers per lot + published: 

  Date?). Already Codable-friendly if the types conform; if not, ~20 mins to add Codable.

    - **actParkInfos** **(static info):** **probably skip.** This is the daily-refresh data — large (every parking lot in

   city), changes rarely, and the daily timer will re-fetch on next foreground tick anyway. Caching it would

  be a separate decision; I'd leave it for Phase 4 territory.

  

  So: location snapshot + parkAvPack snapshot.

  3. **When to write.**                                                  

    - On every actMinutely(p0:) update (the existing entry point for new availability data). Cheap because

  the data is already in hand.

    - On every userLoc2dVbj emission (cheap, single coordinate write).

  

  Alternative: write on .background only. Faster steady-state but loses data if the app crashes. The "write

  on every update" pattern is simpler and the cost is one small write per minute.

  4. **When to read.**

    - At Municipal init (cold launch) — seed parkAvPack + the location subject from cache before any network

  fetch fires.

    - On .active — Phase 3 will trigger this. For Phase 2 alone, cold launch is the main case.

  

  The cyclopsMod auto-rebuilds via the existing parkAvailVbj sink (from Phase 1b) as soon as we seed the data

   — no extra wiring needed.

  5. **Staleness badge.**

    - The existing MncplParkAvPack already has a published: Date? field. The UI could surface staleness as

  "Updated 12 min ago" if published is older than, say, 5 min.

    - Could also dim the count or add an icon.

    - Where does this badge live? MncplCyclopsScreen already shows municipal.availableTime in the infoBar —

  could augment that.

    - **Or defer the badge** to a separate small change after Phase 2 lands, so the cache infrastructure ships

  clean first.

  6. **Cache invalidation.**

    - On app launch, if cache is older than N hours (e.g. 24h), discard and start fresh — avoids showing very

   stale data after a long absence.

    - If watchList municipality changes shouldn't affect this; cache is per-municipality.

  

  **My recommendation**

  **Phase 2 scope (strict):**

  - New Municipal+Cache.swift extension: saveSnapshot() / loadSnapshot() helpers writing to

  Library/Caches/hootowl-snapshot.json.

  - Hook saveSnapshot() into actMinutely(p0:) and the userLoc2dVbj sink.

  - Hook loadSnapshot() into Municipal.init() _before_ wireCyclops() so the existing pipeline picks up the

  seeded data naturally.

  - Discard cache if older than 24h.                        

  - **Defer:** staleness badge UI, actParkInfos caching, .active re-read (those slot into Phase 3 + later).

  Estimated ~80-100 lines, one new file + ~5 lines in Municipal.swift.

  

  **Three open decisions for you**

  

  1. **Storage backend** — Library/Caches/ recommended; confirm or override.

  2. **Stale-cache discard threshold** — 24h recommended; confirm or override (1h? 7d?).

  3. **Staleness badge** — defer to a follow-up, or bundle into Phase 2?

  

  Greenlight + answers → I'll start implementation.




testin:

**Manual** **test** **plan** **(per** **the** **decisions.md** **entry** **—** **please** **run** **before** **committing):**

  1. Open Cyclops with ≥1 pin → wait for parking counts to load.

  2. Switch to another tab → return within 5 min → counts should still be visible (the original bug).

  3. Switch to another tab → wait > 5s (auto-hide tab bar) → return → counts still visible.

  4. Background app → return after a minute → counts still visible.

  5. Reorder sheet: move and delete should persist across sessions.

  6. MncplAllScreen swipe-to-pin/unpin should reflect in Cyclops immediately.

  

  Per your partition plan, this is the day-of-testing stop point. Let me know how it behaves, then we move on to Phase 2 (Layer B1 disk

  cache for cold-launch / jettison cases).
  
```
 ## 2026-06-15 — Drop Always-auth escalation + Info.plist cleanup

      39  **Decision:** Stop auto-escalating from `.authorizedWhenInUse` to `requestAlwaysAu

          thorization()` on iOS, and remove the misleading `NSLocationAlwaysAndWhenInUseUsag

          eDescription` key from `Info.plist`. Pre-release pick **#9** from [[battery#sorted

          -shortlist-low-hanging-fruit-first]].

      40  **Why:** The escalation was triggering a second iOS dialog asking for Always-permi

          ssion, but the app declares no `UIBackgroundModes` so Always provided zero actual

          background capability. The escalation was net-negative: misleading UX + App Store

          review risk (Apple flags apps that ask for Always without legitimate background us

          age). The Info.plist string further promised "background alerts" that the code nev

          er delivered. With escalation removed and the key gone, the app asks for `WhenInUs

          e` only — honest, minimum-necessary permission.
          
          test
```