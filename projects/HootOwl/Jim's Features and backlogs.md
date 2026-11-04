undone:

add a feature set in 1.0, the goal is to make those parks that do not provide livefeed of available count
  as clear as possible, so you can chime in here, in the near me (mapview), can user clearly tell  level 0:
  only park lot, no capacity, no live Available count Level 1:


## Features

### User Interface:

#### highlight the rate and level of visibility 
* target: 1.0
Define the com
add a feature set in 1.0, the goal is to highlight those parks that do not provide livefeed of available count 
as clear as possible, so you can chime in here, in the near me (mapview), can user clearly tell  level 0:
  only park lot, no capacity, no live Available count Level 1:

## Backlogs

> [!tip] Release to-dos are in [[jim-actions]] — this note stays for bugs you want to work on with me.

bugs i need to work with claud on :

1. ~~the search should be case insensitive, or simply move English upper, since I have to type TPE0155 or tpe0155 will not click!~~ — **fixed 2026-09-19, `9285a47`.** `tpe0155` now finds the lot; measured 0 → 1 match over the live feed. [[bugs#2026-09-19-search-only-matched-capitals-so-tpe0155-found-nothing-fixed]]
2. ok, why 0080 is gray but others are green now? and the clown of 0155 never turns normal...
3. ~~IME block switch TAB in the all~~ — **fixed 2026-11-01, `5cdc3de` + `2464fe5`.** The IME was a red herring: the keyboard window sat over the tab bar and the field could never lose focus. [[bugs]] · [[2026-11-01]]
4. subscription is shit
5. opening tab... and launch



> 	the backlog that maintained by Jim, the Flesh intelligent,     

One of the main reason is I am in the flow to work Claude-Code on things, I have not figured out
how to work with AI on multi-frontend. so add backlog here. and work on them in sequence for now

<!-- Template:
## YYYY-MM-DD — Short title
**Symptom:** What goes wrong.
**Root cause:** Why it happens (if known).
**Fix / workaround:** What to do.
**Status:** open | fixed | wontfix
**Files:** path:line references.
-->
## Issues:
### 2026-06-29 --- cyclops will keep the clock forever, until kill and restart 
**Sympton:** when first time running the cyclops will keep the clock forever, until kill and restart 
** Root cause: **
** Fix / workaroun: ** kill and restart then the number of Available will show right off the bat.
** Status :** not input yet.
** Files: ** path:line references

# the Claude code comment that I do not get:

>>>Outstanding: #5 (dedupe CLLocationManager at Municipal.swift:169 — ~1 line, code-health not battery), the Phase 3 device test that was never done, and the post-launch Energy Impact measurement — which stays confounded because ActDeActOnes still has zero callers, so every proto polls for every user regardless of location.

11