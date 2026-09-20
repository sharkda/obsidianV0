# AdMob — findings and status

> [!tip] 🔧 **How the SDK is integrated, and how to update it: [[admob-sdk]]** (new 2026-09-20)
> A vendored XCFramework committed to git, not SPM — with the full update runbook, written to be followed on another machine. This note is about *what the ads do*; that one is about *how the SDK gets there*.

*Jim's paste of the three findings, kept verbatim. Status added underneath each as they are dealt with — the text above a status line is the original finding, not a description of today.*

**Ads themselves are fine and were never the problem:** the SDK starts at `hootowlApp.swift:79`, the banner is placed in `ContentView.swift:58`, test ad unit in DEBUG and the real one in release, hidden for subscribers via `StoreObs.showAdRelay`, and every main screen honours `\.adBannerHeight`. Only the three items below were outstanding.

---

1. ATT is never requested, so you're earning less than you could. NSUserTrackingUsageDescription is missing from Info.plist, and barebackAtt()/AttModel in ATTWarmup.swift have zero callers. The IDFA prompt never appears, so every impression is non-personalised — materially lower eCPM. That's revenue lost by omission rather than by choice. Also a trap: calling ATT before that Info.plist key exists is an immediate crash, so the file is safe today only because nothing calls it.

> [!success] ✅ DONE 2026-09-07 — the prompt now appears on the **2nd launch**
> `NSUserTrackingUsageDescription` added to `Info.plist`; `attRequestIfDue()` in `ATTWarmup.swift` owns the launch counter and the guards; called from `hootowlApp` on `scenePhase == .active` (ATT is ignored unless the app is active).
> **Second launch, not first** — first launch already spends its system dialog on location, and stacking two damages both answers.
> **Verify on device:** launch, quit, launch again → alert appears. `🎯 ATT:` logs at `.notice` every launch. **Delete and reinstall to retest** — once per install.
> ⚠️ The alert text is **English-only**; Chinese users read English. Needs an `InfoPlist.xcstrings`, same change as the location string. → [[operations#how-it-is-wired]]

2. No privacy manifest — and with ads it's now mandatory, not just advisable. The app target has no PrivacyInfo.xcprivacy. Beyond the UserDefaults declaration, you need NSPrivacyTracking and NSPrivacyTrackingDomains — iOS 17+ blocks connections to tracking domains you haven't declared, so this can quietly suppress ad revenue as well as trip submission checks.

> [!success] ✅ DONE 2026-09-07 — `hootowl/PrivacyInfo.xcprivacy`, in both targets
> `NSPrivacyTracking = true`, plus two required-reason APIs: `UserDefaults` (CA92.1) and **file timestamps** (C617.1) — the second found by auditing the source, at `Municipal+Fence.swift:70`. Disk space, boot time and active keyboards were checked and are genuinely unused, so they are not declared.
> **Correcting my own earlier advice:** I said you would need `NSPrivacyTrackingDomains` filled in with Google's ad domains. **Do not do that.** iOS *blocks* requests to listed domains when ATT is denied — which is most users — so it would stop even the non-personalised ads that are meant to keep serving. It is deliberately empty; Google's SDK covers its own domains. Reasoning is written into the file.
> **Still yours:** App Store Connect nutrition labels are a separate declaration and must cover what AdMob collects. Verify the merged result with Product → Archive → *Generate Privacy Report*.

3. Interstitials don't exist in the build. Interstitials.swift and GadHostV.swift are in the project navigator but in no target's Sources phase, so they never compile — Interstitials.swift still uses the pre-v12 GADInterstitialAd symbol, which is probably why. And gAdBannerView.swift isn't in the project file at all. If you thought interstitials were shipping, they aren't.

> [!question] ❓ OPEN — your call
> Nothing is broken; interstitials simply are not in the build. Either **delete the three dead files** (`Interstitials.swift`, `GadHostV.swift`, `gAdBannerView.swift`) or **port `Interstitials.swift` to the post-v12 API** deliberately if you want interstitials as a second revenue surface. Banners are unaffected either way.

---

## Related
[[admob-sdk]] — **the SDK itself: integration and update runbook** · [[jim-actions]] — your action list · [[operations#2b-ads-idfa-and-territories]] — the how-to and the territory decision · [[bugs#2026-09-07-no-privacy-manifest-att-never-requested-admob-is-staying]] — the full record, including the correction to my original wrong claim that no ads were running

