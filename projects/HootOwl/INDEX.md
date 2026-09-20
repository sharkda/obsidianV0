# HootOwl — where everything is

**A map of this folder.** Fourteen topic notes and eleven dated session folders have accumulated; this is what lives where, and which note answers which question.

> Reading order after a break: [[CURRENT|projects/CURRENT]] → [[jim-actions]] → whatever it points at.

---

## Start here

| Note                      | Answers                                                                                                                                                                                              |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[[jim-actions]]**       | *What do I have to do?* Only things needing **you** — your accounts, your device, your judgement. Grouped by where you'd be sitting: browser, Xcode, App Store Connect                               |
| **[[release-strategy]]**  | *How do I get through review?* TestFlight vs straight to release, order of operations, what a reviewer will poke, and the reviewer-in-California problem                                             |
| **[[operations]]**        | *How do I do the thing?* Runbooks: editing the Gist, the release checklist, territories and their gate table, building and testing                                                                   |
| **[[app-store-connect]]** | *What do I paste into App Store Connect?* The one page for all ASC copy — the field map, promotional text, What to Test, Beta App Review notes. Everything ASC-shaped goes here, not into a new note |

## Reference — the durable record

| Note | Holds |
|---|---|
| **[[decisions]]** | Every architectural and product decision with its rationale **and the alternatives rejected**. Newest first. Read this before re-opening a settled question |
| **[[bugs]]** | Every bug found, with root cause and how it hid. The most re-read note in the vault |
| **[[unfinished]]** | Things knowingly left undone — not bugs, not decisions. "We stopped here on purpose" |
| **[[data-sources]]** | The two open-data portals, their contacts, the licence, and a re-check schedule **I own**, not you |
| **[[battery]]** | The battery investigation: the ranked plan, what shipped, what is still owed |

## Topic notes

| Note | Holds |
|---|---|
| **[[onboarding]]** | The three screens' copy, every superseded version, and **jim's request table** at the top |
| **[[zh-review]]** | The 中文 review table you edit in place; I read your corrections back into the catalogue |
| **[[Admob]]** | Your paste of the ads findings, with status added under each |
| **[[cyclops-first-run]]** | The 🕐 investigation — the ancestor of most of what followed |
| **[[working-agreements]]** | *How do I work on this project?* **Read this first on a new machine.** How Jim works, the project conventions not visible in the code, verification standards, and the two-repo push rule. Written 2026-09-20 because Claude Code's own memory does not sync with this vault |
| **[[admob-sdk]]** | *How is the ad SDK wired, and how do I update it?* A vendored XCFramework committed to git rather than SPM — the four pbxproj entries, why not SPM, and a step-by-step update runbook with checksums. Written 2026-09-20 to be followed on a second machine |
| **[[app-icon]]** | *Why did the icon break again?* The alpha rule, the iOS mask, the Icon Composer workflow, and the **wiring step that makes a `.icon` actually take effect**. Two silent failures in two days live here |
| **[[Jim's backlog]]** | Yours. Bugs you want to work on with me |

## Sessions — the narrative

`sessions/YYYY-MM-DD/`, one folder per day, append-only. Long-form reasoning that would bury the notes above.

> [!tip] 📋 **Every day now opens with `00-state-of-play.md`** (from 2026-09-17)
> One table, every open item, **a stable ID per row** (`R-` release · `E-` engineering · `J-` Jim's backlog · `D-` decision). The next day copies the table forward and only the **State** column moves, so nothing falls off quietly. Latest: [[sessions/2026-09-19/00-state-of-play|2026-09-19]].
>
> **Anything older than two days moves to `sessions/older/`**, so the top level shows only what is current. Wikilinks resolve by note name, not path, so nothing breaks — the one exception is a duplicated name (`01-session-wrap` exists three times), where the link spells out the full path.

Most useful recent ones:

- **[[sessions/older/2026-09-10/01-session-wrap|2026-09-10/01]]** — the name, map freshness, and the three-bugs-one-shape theme
- **[[00-location-privacy-audit|2026-09-09/00]]** — six checks proving location never runs in the background, **plus the addendum where that audit turned out to be half the job**
- **[[00-subscription-screen|2026-09-08/00]]** — the subscription rewrite and the three bugs it exposed
- **[[00-req-taipei2Taiwan|2026-09-07/00]]** — the coverage-wording thread end to end
- **[[01-resume-here|2026-09-05/01]]** — the Cyclops arc's closing handoff

---

## Where today's specific findings went

Since several came up at once and are scattered by design — each lives with its own kind, not in one pile:

| Finding | Lives in |
|---|---|
| Reviewer sees an empty map in California | [[release-strategy#the-one-risk-i-would-bet-money-on]] + 🔴 in [[jim-actions]] |
| Open-data licence needs attribution | [[release-strategy#a-licence-obligation-nobody-has-noticed]] + 🔴 in [[jim-actions]] |
| No crash reporting; no feed-down state | [[jim-actions#gaps-found-2026-09-10--things-that-were-on-no-list]] |
| `ITSAppUsesNonExemptEncryption` | Fixed. Rationale in the `Info.plist` comment itself |
| Map pins had no freshness at all | [[bugs]] 2026-09-10 + pattern in [[swift-patterns]] |
| Subscription sheet spoke English | [[bugs]] 2026-09-09 — two causes, one outside the catalogue |
| "Background nearby search" banner | [[bugs]] 2026-09-09 + [[00-location-privacy-audit]] addendum |
| App name and why not "Taipei" | [[decisions]] 2026-09-10 |
| Territories, and the gate before adding any | [[operations#gate-table--read-this-before-adding-any-territory]] |
| iOS 26.0 minimum limits reach | ❓ in [[jim-actions]] |
| Subscription unlocks nothing but ad removal | 🔴 in [[jim-actions]] — still an open product question |

## Conventions

- **Long-form goes in the vault, the terminal stays a pointer.** Every session gets a dated folder by default.
- **`jim-actions` is filtered to you.** [[operations#2-release-checklist]] is the complete list including what I can do.
- **Dated notes are append-only** — never edited after the fact, so the record stays honest about what was believed when.
