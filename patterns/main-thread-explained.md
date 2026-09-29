# The main thread, actors, and what E-10 actually was

**Written 2026-09-29 for Jim, who asked for it in plain terms.** Uses HootOwl's own crash rather than textbook examples. Anyone picking this project up cold should read it before touching `Municipal`.

---

## 1. There is one thread that draws the screen

A **thread** is a worker. Your app has several, but **only one of them is allowed to draw** — the **main thread**. Every button, every label, every map pin is put on screen by that one worker.

This is not Apple being awkward. Drawing is a sequence of steps, and if two workers redraw at once you get a half-finished frame. So Apple's rule is: **only the main thread touches anything the screen depends on.**

## 2. Which is why downloads happen somewhere else

If the main thread went off to fetch 1,700 car parks from Taipei's server, the screen would freeze for those seconds — no scrolling, no taps. So the app hands that work to **background threads**.

HootOwl does this constantly: two cities, each with a daily download and a live-availability poll, all on background workers.

**So there is a handoff.** Data arrives on a background worker, and at some point it has to become *state the screen reads*. **That handoff is the dangerous moment**, and it is the only thing this whole topic is about.

## 3. What actually broke

`Municipal` is the object holding what the app knows: which car parks exist, how many spaces are free, where the user is. The screen reads it constantly.

Inside it is a **dictionary** — a lookup table, `city → that city's car parks`:

```swift
actParkInfos[p0.mncplt] = p0      // "file this city's data under its name"
```

Two cities' downloads finished at nearly the same moment, each on its own background worker, and **both ran that line at once.**

A dictionary is not one value — it is a structure with internal bookkeeping. Two writers rearranging that bookkeeping simultaneously leaves it **corrupt**: pointers to things that are no longer there.

**The giveaway was in the error message.** Jim's crash said:

```
-[__NSTaggedDate count]: unrecognized selector
```

*"I asked something for its `count` and got a Date, which has no count."* Mine, from the same line, said `__NSCFNumber`.

> **Same line, same code, a different wrong type each run.** A genuine programming mistake is boringly consistent — it fails the same way every time. **A different wrong answer each run means the app is reading memory that no longer holds what it thought.** That is corruption, and it is what a data race looks like from the outside.

## 4. The first fix: remember to hand over

There is a standard way to say *"go back to the main thread before doing this"*:

```swift
.receive(on: DispatchQueue.main)
```

One line in the pipeline. Three of them were added on 09-24 and the crash stopped.

**But look at how that fix works: it relies on someone remembering to write it.** And the project already had proof that people forget — the very same line had been added to a *different* data flow three weeks earlier, for the same kind of crash. The person fixing that one fixed the flow in front of them and did not look for siblings. The daily-download flow kept the bug for three more weeks.

**That is E-10.** Not the crash — the fact that the rule lived in a comment and was enforced by nobody.

## 5. The second fix: make the compiler hold the rule

```swift
@MainActor
@Observable final class Municipal: NSObject {
```

**One line, and it changes who is responsible.**

`@MainActor` means: *everything in this class belongs to the main thread.* The **compiler** now checks every single place that touches `Municipal` and asks "are you on the main thread?" If not, it says so — while you are typing, not at 2am in a crash report from a user.

The vocabulary in the notes, now that it means something:

| Term | Plain meaning |
|---|---|
| **actor** | a boundary around some state, with a rule about who may cross it |
| **isolated** | "this belongs to the main thread" |
| **hop** | switching from one worker to another before touching something |
| **race** | two workers touching the same thing at once — the bug |

## 6. Why it needed two lines, not one

Adding it to `Municipal` alone produced **36 errors** — almost all of them from `NbsObsM`, the object behind the map, which reads `Municipal` constantly.

`NbsObsM` is *also* state the screen reads. It had the same problem and nobody had said so. **Annotating it too took the errors to zero.**

```swift
@MainActor
@Observable final class NbsObsM {
```

Two lines. Both objects that the UI reads now say so out loud.

> [!warning] A measurement lesson worth more than the actors
> The first count was **"3 sites"**, and it was wrong. That number came from a build that **stopped at its first errors** — the compiler gives up early, so it had never reached the other 33.
>
> **An error count from a failed build is a lower bound, not a total.** Fix the first wave, build again, and only then quote a number.

## 7. What it does not buy yet

Swift has two modes. This project is in the **older one (Swift 5)**, where breaking the rule is a **warning** — the compiler tells you and builds anyway. In **Swift 6** it is an **error** and will not build.

So today the annotation is **a documented boundary, not a locked door.**

As it happens there are **no warnings left at all**, so nothing is being ignored. But the door only locks on a move to Swift 6 language mode — a project-wide job with a long tail, and **deliberately not being done before the release**.

## Related
[[swift-patterns]] · [[bugs#2026-09-24--municipal-mutated-off-the-main-thread-the-app-aborted-on-the-second-citys-feed-fixed]] · [[decisions#2026-09-29-municipal-and-nbsobsm-are-main-actor-isolated]]
