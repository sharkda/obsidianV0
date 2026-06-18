# SwiftUI View Lifecycle, State, and Identity

A reference for the subtle but real bugs caused by SwiftUI's view identity tracking — when `@State` persists vs. resets, and the patterns that make state-bearing screens robust vs. fragile.

Captured 2026-06-17 after investigating the "`MncplCyclopsScreen` goes empty on quick switch out / in" bug in HootOwl. The bug turned out to be a SwiftUI identity quirk, not application logic — and the same trap can bite any future state-bearing screen.

---

## TL;DR

- `@State` survives only as long as **SwiftUI considers the view the same identity**.
- View identity can be lost on body re-renders if the view is hosted inside a structure with unstable identity (notably, dynamic `ForEach` inside `TabView(selection:)` is the canonical landmine).
- When `@State` resets, all view-local cache / trail / derived state is wiped — and the typical recovery code (`.onAppear` re-firing wire(), relying on subscription replay) is racy and easy to get wrong.
- **Default pattern in HootOwl: state-bearing display data lives on the `@Observable` singleton (or a dedicated `@Observable` class), and views read it as computed properties.** Use view-local `@State` only for transient UI state that should reset when the view is destroyed (focus, scroll position, sheet flags, etc.).

---

## What is view identity in SwiftUI?

SwiftUI manages a tree of view nodes. Each node has an **identity** computed from its position in the view hierarchy + the type of view + any explicit identifiers (`.id(...)`, `.tag(...)`).

`@State` storage is associated with a node by its identity. Two consequences:

- **Same identity across re-renders → `@State` persists.** This is the common case for statically structured layouts.
- **Identity changes → `@State` is wiped to its initial value**, even though the View struct is "the same type" in the source code. The Swift struct gets re-initialized; SwiftUI gives it fresh storage.

Identity is *not* preserved automatically just because the parent's `body` produces "the same kind of view." It's computed from structural position + explicit identifiers + the framework's identity heuristics — which are not always predictable for dynamic constructs.

---

## When does @State persist?

- Within a single body re-render (always).
- Across body re-renders if the view's identity is stable (most common case for static layouts).
- Across `.background → .active` app lifecycle transitions (the view tree persists in memory through iOS app suspension, as long as iOS doesn't jettison the process).
- Within a `TabView` if the tabs are **statically declared** — each tab being a distinct position in source gives each one a stable identity slot.

## When does @State silently reset?

- Parent uses a conditional that flips: `if foo { A() } else { B() }` — even flipping back to the original branch later may not restore the original `@State`.
- `ForEach` over a recomputed array — even if the array contents are identical, SwiftUI's `ForEach` identity tracking can lose fidelity (see the antipattern section).
- View is presented via `.sheet` / `.fullScreenCover` and re-presented after dismissal — each presentation creates fresh `@State`.
- Custom containers, view modifiers, or animation transitions that re-create child views.
- View is placed inside `LazyVStack` / `LazyHStack` / `LazyVGrid` and scrolls off-screen far enough that SwiftUI recycles the slot.

---

## Antipattern: dynamic ForEach inside TabView(selection:)

```swift
TabView(selection: $selection) {
    ForEach(MyScreen.sorted(filter: filter)) { screen in
        screen.destination
            .tag(screen)
            .tabItem { screen.label }
    }
}
```

This LOOKS reasonable: tabs are derived from a sorted list, can adapt to subscription tier / user preference / runtime data.

**Why it's fragile:** each time the parent body re-renders, `sorted(filter:)` returns a new array. SwiftUI's `ForEach` identity tracking inside `TabView(selection:)` is sensitive — under certain conditions (which include "the array is recomputed even if contents are identical"), SwiftUI re-creates the tab views, and their `@State` resets to defaults.

Triggers that cause the parent body to re-render:
- Selection binding change (a tab switch).
- Any `@State` / `@Environment` change in the parent.
- Any timer / animation completion that toggles `@State`.

In HootOwl's case (`AppTabView`), an auto-hide tab bar uses `.task(id: hideToken)` to flip `interconnect.tabVisible` every 5s of inactivity → parent body re-renders → `ForEach` re-evaluates → child `@State` (in `MncplCyclopsScreen`) resets to empty defaults.

### Two ways out

1. **Fix at the TabView level (if dynamic tabs are required):** pre-build the tab list once and store it in `@State` of the parent so the `ForEach` reads a stable reference; or use static tabs with conditional visibility (`.tabItem` + `.hidden()` modifiers).
2. **Fix at the child level (what HootOwl chose):** make the child view *stateless* by lifting state to an `@Observable` singleton. The child can lose `@State` infinitely without affecting what's rendered — because there's nothing to lose.

The child-level fix is more robust because it doesn't depend on getting the host right, and it generalizes — once a screen is stateless against its host, it survives any future re-hosting.

---

## Antipattern: relying on subscription replay to repopulate reset @State

```swift
struct MyScreen: View {
    @State private var displayModel: DisplayModel = .empty
    @State private var cancellables = Set<AnyCancellable>()

    var body: some View {
        // ... reads displayModel
        .onAppear { wire() }
        .onDisappear { unwire() }
    }

    private func wire() {
        publisher.sink { value in
            self.displayModel = DisplayModel(value)
        }.store(in: &cancellables)
    }
}
```

Common in HootOwl screens that historically accumulated trail or derived data. The intent: when the view appears, subscribe to the data publisher, which (if it's a `CurrentValueSubject`) immediately replays the current value into `displayModel`.

**Why it's fragile:** this only works if all of these hold:

1. `.onAppear` fires at the moment of re-appearance. **Not guaranteed when SwiftUI re-creates the view due to identity loss** — whether SwiftUI treats this as "new appearance" vs. "still appeared" is opaque framework behavior.
2. The publisher is a `CurrentValueSubject` (replays on subscribe). A `PassthroughSubject` does *not* replay — `displayModel` would stay `.empty` until the next emission.
3. The replay completes before SwiftUI re-renders. There can be a frame where the empty state is visible.
4. The view's `@State` is not racing with the publisher's emission ordering.

It also fails to preserve work-in-progress across appearance cycles (e.g., trail history that should accumulate over time, even when the screen isn't visible).

---

## The recommended pattern: singleton state + thin views

```swift
// Singleton — typically Municipal, or a dedicated @Observable class.
@Observable final class Municipal {
    var displayModel: DisplayModel = .zero

    private var cancellables = Set<AnyCancellable>()

    init() {
        wireOnce()  // called once at app startup; subscriptions live for app lifetime.
    }

    private func wireOnce() {
        parkInfoVbj.sink { items in
            self.displayModel = DisplayModel(items: items, oldTrails: self.displayModel)
        }.store(in: &cancellables)
    }
}

// View — reads singleton via @Environment, no @State for display data.
struct MyScreen: View {
    @Environment(Municipal.self) private var municipal

    var body: some View {
        ForEach(municipal.displayModel.items) { item in
            ItemView(item)
        }
    }
}
```

**Why this pattern works:**
- The singleton's `@Observable` properties always reflect the latest state, regardless of what SwiftUI does to view identity.
- SwiftUI's `@Observable` integration triggers view re-render when accessed properties change — no manual `.sink` in the view.
- Trail / accumulation logic runs once at app startup; doesn't depend on view appearance.
- The view can be re-created infinitely without losing or duplicating work.
- The view becomes trivially testable — pass a mock singleton, render the view, assert what it shows.

**The CLAUDE.md guidance summarizes this for HootOwl:**

> "Municipal is `@Observable` — read its properties directly in computed vars; SwiftUI tracks changes automatically. No Combine needed for simple reads. Use Combine (`sink` + `@State`) only when you need to accumulate state across successive data deliveries (e.g. trail/history)."

The accumulation Combine pipeline belongs on the singleton, not the view.

---

## When IS view-local @State the right answer?

`@State` is the correct choice for state that's **intentionally per-view-instance and disposable**:

- Focus state (`@FocusState`).
- Search text being typed (before commit / submit).
- Sheet / alert presentation flags.
- Scroll position (`ScrollViewReader` proxy targets).
- Animation state (e.g. expanded/collapsed flag).
- Form field values before submission.

The rule of thumb: **if the state SHOULD reset when the view is destroyed** (and starts fresh on next appearance), `@State` is fine. **If the state needs to survive view destruction**, lift it to a singleton.

A useful test: imagine the view being re-created mid-session. Would resetting this `@State` to its default value be the correct behavior? If yes, `@State` is fine. If no, you need a singleton.

---

## Diagnostic checklist for "screen goes empty / state lost" bugs

When investigating an "I switched out and back in and the screen was empty / state was lost" report:

1. **Does the screen use `@State` for derived / aggregated / accumulated data?** If yes, suspect identity loss. Lift to singleton.
2. **Is the screen hosted inside dynamic `ForEach` (especially in `TabView(selection:)`)?** If yes, suspect identity loss. Either make the host static or make the screen stateless.
3. **Does parent body re-render often** (timers, environment changes, animations)? Each re-render is a chance to lose child identity.
4. **Does `.onAppear` fire when the empty state appears?** If yes, race in `wire()`. If no, identity loss without re-mount.
5. **Is the underlying publisher `CurrentValueSubject` or `PassthroughSubject`?** `PassthroughSubject` won't replay — relying on subscription is broken.
6. **Is there a sheet / fullScreenCover involved?** Each re-presentation creates fresh `@State`.

---

## HootOwl-specific cross-references

- **The pattern to follow:** `MncplAllScreen` (computed properties off `municipal.actParkInfos` / `municipal.parkAvPack`). The view body always reads live singleton state — survives any SwiftUI re-render.
- **The pattern to avoid:** the pre-fix `MncplCyclopsScreen` (`@State cyclopsMod` cache + Combine sinks in `.onAppear` / `.onDisappear`).
- **The host that triggers the trap:** `AppTabView` — dynamic `ForEach(AppScreen.sorted(subTier:))` + auto-hide tab bar that re-renders every 5s.
- **The fix project:** see `[[battery]]` Phase 1 (Layer A) for the planned `MncplCyclopsScreen` refactor.

---

## External references

(Annotate as Jim finds relevant Apple docs / WWDC talks / community write-ups.)
