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