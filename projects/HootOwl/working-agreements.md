# Working agreements — for whichever Claude picks this up

**Written 2026-09-20, for a second machine.** Everything here came out of Claude Code's *local* memory store (`~/.claude/projects/…/memory/`), which lives on one laptop and **does not sync with this vault**. Jim syncs Obsidian to a MacBook Air and expects the instance there to work the same way — so these are written down here, where they travel.

> [!info] If you are that instance
> Read this, then [[CURRENT|projects/CURRENT]], then the newest `sessions/` note. Nothing below is a rule for its own sake — each one is here because getting it wrong already cost a session.

---

## Paths differ per machine

**Jim works on more than one Mac.** One path is standardised and one is not:

| | Where | |
|---|---|---|
| **This vault** | **`~/obsidianV0` on every machine** | Jim's call, 2026-09-20 — standardised rather than discovered. → [[decisions#2026-09-20-the-vault-lives-at-obsidianv0-on-every-machine]] |
| **The app repo** | **differs per machine** | Nothing depends on it; every command runs from `git rev-parse --show-toplevel` |

**So `CLAUDE.md`'s `Vault path: ~/obsidianV0` is correct on both machines and needs no edit.** If it ever does not resolve, **the vault is in the wrong place — move the vault, do not edit the file.** It is committed to the app repo, so divergent copies would conflict on every pull.

Everything else still holds: **nothing in this vault should assume the app repo's path.** Anything that does is a bug that only shows up on the machine you are not testing on.

### Find things, do not assume them

```sh
# the app repo — from any directory inside it
REPO="$(git rev-parse --show-toplevel)"

# confirm it is the right one, by remote rather than by name
git -C "$REPO" remote get-url origin        # → …:sharkda/hootOwl.git
```

**The vault is at `~/obsidianV0`.** Use it directly. The discovery snippet below is a **fallback** for a machine that somehow differs — it was written before the path was standardised, and is kept because it costs nothing and answers "am I even in the right vault":

```sh
MARKER="$(find "$HOME" -maxdepth 5 -path '*/projects/HootOwl/INDEX.md' 2>/dev/null | head -1)"
VAULT="$(dirname "$(dirname "$(dirname "$MARKER")")")"
git -C "$VAULT" remote get-url origin       # → …:sharkda/obsidianV0.git
```

*(Tested 2026-09-20 on the main Mac: resolves the vault root and the right remote.)*

**If `~/obsidianV0` does not exist on this machine, stop and tell Jim** — that is the vault not having been moved yet, not a path to work around. It is on their to-do list: [[jim-actions#second-machine--the-macbook-air]].

### Two things that are per-machine and will not arrive by syncing

**`.claude/settings.local.json` is gitignored, so a second machine has none.** On Jim's main Mac it allowlists the vault so writes do not stop for approval on every note — 13 references to the vault path, plus `permissions.additionalDirectories`, without which an out-of-tree folder is not in scope at all.

**Symptom if it is missing:** every single vault write prompts for permission, which makes the "write it to Obsidian" convention unusable — and it will look like the convention is broken rather than like a missing settings file.

**Fix:** it lives at `.claude/settings.local.json` in the app repo. **Now that the vault path is the same on every machine, copy it across verbatim** — no path editing. It stays gitignored, so the two machines never conflict. Record: [[decisions]], 2026-08-13.

*(`CLAUDE.md` used to be the other half of this problem — it names an absolute vault path and is committed to git. Standardising the vault path settled it: the line is simply correct everywhere now.)*

### When writing notes from now on

- **Commands assume you are already in the repo root.** `xcodebuild -project hootowl.xcodeproj …`, not `cd /Users/…`.
- **Refer to files repo-relative** — `hootowl/Municipalities/Zone2/NewTaipeiCityObs.swift:20`.
- **Refer to vault notes by wikilink**, never by path. They resolve by name wherever the vault sits.
- An absolute path is acceptable only in a **dated historical record** of something that happened on a specific machine — never in an instruction.

---

## Working with Jim

**Jim spent years as a software product manager.** It shows in how they work, and it should change how you work.

- **Take a position.** When I hedged on whether an onboarding paywall was badly timed — *"most apps do it anyway, worth measuring"* — they came straight back: *"are you for or against this 'bad timing'?"* **Recommendation first, reasoning after.** A balanced survey reads as avoidance.
- **Scope decisions arrive clean and final.** *"task 2 first, skip ob3, add the mention line."* Implement exactly that. Do not relitigate the settled parts.
- **Expect user-perception catches you will miss.** They spotted that a leading glyph reads as a bullet point rather than as an icon — I had verified it matched the real button and never asked how the eye would parse its position.
- **Prioritisation is explicit and risk-weighted.** *"bigger fishes to fry."* When they defer something, **record the reasoning next to the decision** — they think in expected cost, not checkboxes.
- **Pronouns: use "Jim" or they/them.** Their pronouns have not been stated. I assumed he/his across a long session — commits, vault notes, decision records — and got a one-word correction: *"'he'?"* (2026-09-09). In dense technical prose the name usually reads better than they/them anyway, and these records get re-read months later.

### Session wrap — push **both** repos, every time

**Jim's instruction, 2026-09-20:** *"next time, do wrapup, please always push both."*

There are **two** git repositories, and a wrap-up that pushes one of them is half-finished. **Identify them by remote, never by path** — see [[#Paths differ per machine]]:

| Remote | Holds |
|---|---|
| `git@github.com:sharkda/hootOwl.git` | the app, **and the vendored AdMob xcframework** |
| `git@github.com:sharkda/obsidianV0.git` | this vault |

**Why it matters more than it sounds.** Jim works across two machines, and these repos are the only channel between them. Code pushed without notes means the other instance sees a change it cannot explain; notes pushed without code means it reads about work that is not there. **The pair is the handoff** — either half alone is worse than neither, because it looks complete.

```sh
# from anywhere inside either repo
git -C "$(git rev-parse --show-toplevel)" status -sb | head -1   # expect no "ahead"
```

Do this **unprompted** as the last step of any wrap-up, not only when asked to push.

### Where Jim actually reads

- **Long answers go in the vault, not the terminal.** Briefings, investigations, plans, option menus → a note; the terminal gets a few lines and a pointer. Asked for explicitly 2026-08-13. The terminal scrolls away and is not searchable.
- **Every session opens a dated folder** `sessions/YYYY-MM-DD/`, numbered notes inside (`00-…`, `01-…`). Do this without being asked. Since 2026-09-17 the day's first note is `00-state-of-play.md` — one table, every open item, **a stable ID per row** (`R-` release · `E-` engineering · `J-` Jim's backlog · `D-` decision). The next day copies it forward and only the **State** and **Moved** columns change.
- **Session notes are append-only.** Do not retroactively edit yesterday's note to reflect today — carry the table forward into today's instead. I got this wrong twice and had to restore.
- **Sessions older than two days move to `sessions/older/`.** Wikilinks resolve by note name, so moving breaks nothing — except where a name is duplicated (`01-session-wrap` exists three times), where the link must spell out the full path.
- **Topic notes are updated inline, as work happens** — not batched to session END. `battery.md`, `privacy-policy.md`, `admob-sdk.md` and the like are meant to be readable standalone, months cold.
- **`CURRENT.md` stays short and current-state-only.** Narrative accumulating there is what made it drift before.
- **Jim files some requests as table rows in Obsidian**, not in chat — e.g. `## jim's request table` at the top of [[onboarding]], columns `id | request | rational | status | AI response`. **Check topic notes for these**, answer in the `AI response` cell, set `status`, and never edit their `request` or `rational` text.
- **"save this"** is shorthand for the full session END protocol in `CLAUDE.md`.

---

## Project conventions that are not obvious from the code

### iOS is the product; macOS only has to compile

Jim, verbatim (2026-09-06): *"the app is for iOS, we can ignore the macOS ones, just try to minimize any erros complaints for macOS will be fine."*

Keep `hootmac` building — wrap iOS-only affordances in `#if os(iOS)` rather than letting them render wrongly — but **never design, lay out, or polish for macOS**, and do not raise macOS UX as a decision. Several views are reachable from both targets, so it is easy to burn a session on something nobody sees.

**Exception that survives this:** keep the `#if os(iOS) / #elseif os(macOS)` split around `CLAuthorization` / `.authorizedWhenInUse` references even when the branches are identical — Xcode has historically flagged that case as macOS-unavailable.

### Write for the newest OS only — no `#available` branches

No `#available(iOS X, *)` branches, no legacy fallbacks, no compat shims. When a deprecation warning appears, **replace the call site with the new API** rather than branching. A stray `MACOSX_DEPLOYMENT_TARGET = 14.5` in the pbxproj is leftover config, not a support commitment. Only branch if Jim says so.

### A new `.swift` file written to disk is in no target

The app group is **not** file-system-synchronized — the app target carries ~632 explicit Sources entries. A file created outside Xcode compiles for nobody.

**Wire it yourself**; it is mechanical. Copy a sibling's shape — `grep -n "Sibling.swift" hootowl.xcodeproj/project.pbxproj` returns **exactly 6 lines**: 1 `PBXFileReference`, 2 `PBXBuildFile` (one per app target, both pointing at the single fileRef), 1 `PBXGroup` child, 2 `PBXSourcesBuildPhase` entries. Fresh 24-hex-uppercase ids. Verify with `plutil -lint` and by re-grepping for 6 entries.

**The tell that you forgot:** the error is *not* "no such member". Because the missing symbol is usually inside an overloaded API's trailing closure, Swift reports a **shifting argument-count error** ("expects 0 arguments, but 1 was used" ↔ "expects 1 argument, but 2 were used") that changes as you edit. A shifting message means an orphaned file, not a broken closure.

### `Codable` must be declared in the type's own file

`extension Foo: Codable {}` in a *different* file looks tidy and **silently skips synthesis** — the compiler then complains about missing `encode(to:)`. Add `Codable` to the conformance list where the `struct`/`class` is declared.

### Pair every `ffl(..., .error)` with a simulator earcon

```swift
ffl("⚠️ message", .error)
#if targetEnvironment(simulator)
Earcon.alert_high_intensity.caf()   // unmissable — simulator only
Earcon.ps(SystemSoundID(1109))      // shake — bypasses EarconMode
#endif
```

**`SystemSoundID` needs an explicit `import AVFoundation`** under Xcode 27 — `SWIFT_UPCOMING_FEATURE_MEMBER_IMPORT_VISIBILITY` is on, so it no longer arrives transitively.

### `ffl` levels decide whether you can see anything on a device

`.debug` and `.info` go through `print()`, which **exists only while Xcode's debugger is attached**. To observe anything on real hardware, log at **`.notice` or above** and read Console.app (device selected, filter category `ffl`). A silent log looked exactly like an app hang and cost most of a day.

`.debug` is *additionally* gated per-file by `fileDubugLevelDict`. **Do not lower a file's threshold without checking what it logs per item** — lowering `Mu1Base+Ext` to `1` enabled per-item logging over ~1,750 lots and produced a **five-minute launch freeze**.

### Prefer singleton state for state-bearing screens

Lift trail/accumulation/derived state to `Municipal` or a dedicated `@Observable` class, read via computed properties. **View-local `@State` silently resets** when SwiftUI loses view identity — which is exactly what `AppTabView`'s dynamic `ForEach` inside `TabView(selection:)` does. That was the Cyclops emptiness bug.

`@State` is still right for disposable per-view state: focus, sheet flags, search text, scroll position.

---

## Verification standards, learned expensively

- **Compiling is not enough — run it.** On 2026-09-15 an empty `@CommandsBuilder` closure compiled clean and aborted at launch, producing an archive that was uploadable and unrunnable.
- **A toolchain change expires every "it builds" claim in this vault.** That is not hypothetical; it happened between 09-14 and 09-15 and cost most of a session.
- **Check claims against the repo before repeating them.** Notes go stale. A 09-08 note said `SubscriptionStoreScreen` was unreferenced; it was reachable from the Cyclops toolbar, and because the note said otherwise, a localisation fix skipped it and shipped English to Chinese users for eleven days. **Trace callers; do not trust "this is unused".**
- **Measure the claim you are about to write down.** Standard string comparison is documented as width-insensitive; measured, it did not fold full-width `ＴＰＥ`. The comment now records the measurement, not the documentation.

## Related
[[CURRENT|projects/CURRENT]] · [[INDEX]] · [[operations#3-building-and-testing]] — the environment and build commands · [[admob-sdk]] · [[patterns/swift-patterns|swift-patterns]] · [[bugs]] · [[decisions]]
