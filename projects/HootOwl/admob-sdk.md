# Google Mobile Ads SDK — how it is integrated, and how to update it

**Written 2026-09-20**, when the SDK was taken from **13.3.0 → 13.10.0**. Until then this was the least-documented load-bearing thing in the project: the *consequences* were written up in [[operations#the-upload-symbols-failed-warning--ignore-it-permanently]], but nothing said how the SDK got there or how to change it.

> [!important] Written to be followed on another machine
> Jim syncs this vault to a MacBook Air where a different Claude Code instance works on the same repo. **Everything below is machine-independent** — exact URLs, checksums and commands, no local paths outside the repo. If you are that instance: read [[#If you are on the other machine]] first, because you probably do **not** need to do any of this.

---

## How it is integrated

**A prebuilt XCFramework, vendored at the repo root and committed to git.** Not Swift Package Manager, not CocoaPods.

```
hootowl/GoogleMobileAds.xcframework/     ← 37 MB, 234 files, tracked in git
├── Info.plist
├── _CodeSignature/                      ← Google's own signature
├── ios-arm64/                           ← device
└── ios-arm64_x86_64-simulator/          ← simulator
```

**There is no macOS slice.** That is why every AdMob file is wrapped in `#if os(iOS)` — `GadCon.swift`, `BannerView.swift`, `gAdBannerView.swift`, `Interstitials.swift`, and the import in `hootowlApp.swift`. Remove a guard and `hootmac` stops building.

### The project wiring — four entries, one file reference

All four point at the same `PBXFileReference`. If the framework is ever re-added by hand, all four are needed:

| Section | Entry |
|---|---|
| `PBXFileReference` | `path = GoogleMobileAds.xcframework; sourceTree = "<group>";` plus `expectedSignature = "AppleDeveloperProgram:EQHXZ8M8AV:Google LLC"` |
| `PBXBuildFile` → Frameworks | links it |
| `PBXBuildFile` → Embed Frameworks | `settings = {ATTRIBUTES = (CodeSignOnCopy, RemoveHeadersOnCopy, );}` |
| `PBXCopyFilesBuildPhase` | the *Embed Frameworks* phase lists the build file |

`expectedSignature` pins Google's Apple Developer team **EQHXZ8M8AV**. A replacement framework that is not signed by that team will be rejected by the build — which is a feature, and worth not defeating.

### Why it is not SPM

It **used to be.** [[operations]] records a `Package.resolved` in `farms/backup/hootowl` (April 2025) pinning GoogleMobileAds and Google UMP — *"from the era when ads were an SPM dependency rather than an xcframework."*

The project now has **zero** `XCRemoteSwiftPackageReference` entries; the last one, a dangling `ConcaveHull`, was deleted in `a4a005b` (2026-09-14). That is not incidental — **SPM in this project has a history of breaking command-line builds**, and `ConcaveHull` made `xcodebuild` unusable from the CLI for months ([[bugs]]). A vendored binary cannot fail to resolve, cannot fail offline, and cannot re-resolve differently on another machine.

**The trade is repo size and manual updates.** 37 MB in git, and no tooling tells you when a new version ships.

### What is deliberately *not* here

**`UserMessagingPlatform` (UMP), Google's consent SDK.** The SPM package depends on it; this project does not include it, because the territory decision excludes the EEA and UK, which are the only places it is required. Adding an EEA territory means shipping UMP first — see [[operations#gate-table--read-this-before-adding-any-territory]].

---

## If you are on the other machine

**You almost certainly need to do nothing.** The xcframework is **committed to git**, so `git pull` brings the exact bytes — same version, same signature. There is no per-machine install step, no package to resolve, nothing to download.

> [!warning] The corollary: a pull is the *only* way you learn about a new SDK
> Nothing in the project declares an SDK version, so there is no mismatch warning and no resolution step to fail. **If the other machine has not pulled, it is silently on the old SDK and will build happily.** Check the version explicitly rather than assuming.

Confirm what you have:

```sh
/usr/libexec/PlistBuddy -c 'Print :CFBundleShortVersionString' \
  GoogleMobileAds.xcframework/ios-arm64/GoogleMobileAds.framework/Info.plist
```

Expected: **13.10.0** as of 2026-09-20.

Follow the runbook below **only** to move to a newer version.

---

## Runbook — updating to a new SDK version

### 1. Find the latest version

Google's SPM mirror is the authoritative, scriptable source of both the version list and the binary:

```sh
curl -sS "https://api.github.com/repos/googleads/swift-package-manager-google-mobile-ads/tags?per_page=10" \
  | python3 -c "import json,sys; [print(' ', t['name']) for t in json.load(sys.stdin)]"
```

### 2. Get the exact URL and checksum for that version

**Do not guess the URL** — it contains a per-release hash. Read it out of the tagged `Package.swift`:

```sh
VER=13.10.0
curl -sS "https://raw.githubusercontent.com/googleads/swift-package-manager-google-mobile-ads/${VER}/Package.swift" \
  | grep -A 4 "binaryTarget"
```

That prints the `url:` and `checksum:` for the release.

### 3. Download and verify

**Verify the checksum before unpacking.** This is the only integrity check in the whole process:

```sh
curl -sS -L "<url from step 2>" -o sdk.zip
shasum -a 256 sdk.zip        # must equal the checksum from step 2
unzip -q sdk.zip -d extracted
```

### 4. Confirm it is what you think it is

```sh
NEW=extracted/GoogleMobileAds.xcframework
ls -1 "$NEW"                                   # expect ios-arm64 and ios-arm64_x86_64-simulator
/usr/libexec/PlistBuddy -c 'Print :CFBundleShortVersionString' \
  "$NEW/ios-arm64/GoogleMobileAds.framework/Info.plist"
codesign -dv --verbose=2 "$NEW" 2>&1 | grep -E "Authority|TeamIdentifier"
```

**`TeamIdentifier` must be `EQHXZ8M8AV`** — that is what `expectedSignature` in the project pins. If it is anything else, stop.

### 5. Swap it in

Keep the old one **outside the repo** until the new one is proven:

```sh
cp -R GoogleMobileAds.xcframework /tmp/backup-<oldver>.xcframework
rm -rf GoogleMobileAds.xcframework
cp -R extracted/GoogleMobileAds.xcframework ./GoogleMobileAds.xcframework
```

**No project-file change is needed.** The path and the signature expectation are unchanged, so the four pbxproj entries keep working. If Xcode is open, close and reopen the project so it re-reads the framework.

### 6. Build all four configurations

```sh
export DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer
xcodebuild -project hootowl.xcodeproj -scheme hootowl -configuration Debug   -destination 'generic/platform=iOS Simulator' build
xcodebuild -project hootowl.xcodeproj -scheme hootowl -configuration Release -destination 'generic/platform=iOS' build
xcodebuild -project hootowl.xcodeproj -scheme hootmac -configuration Release -destination 'platform=macOS' build
xcodebuild -project hootowl.xcodeproj -scheme hootmac -configuration Debug   -destination 'platform=macOS' build
```

**Both macOS builds matter here**, even though macOS has no ads — they are what prove the `#if os(iOS)` guards still hold.

### 7. Compiling is not enough — run it and watch for an ad

The SDK can compile and fail at runtime. Build for a simulator, install, launch, and read the console:

```sh
UDID=$(xcrun simctl list devices available | grep -m1 "iPhone 1[78]" | grep -oE '[0-9A-F-]{36}')
xcodebuild -project hootowl.xcodeproj -scheme hootowl -configuration Debug \
  -destination "id=$UDID" -derivedDataPath DerivedData/sim ENABLE_DEBUG_DYLIB=NO build
xcrun simctl boot "$UDID"; xcrun simctl bootstatus "$UDID" -b
xcrun simctl install "$UDID" DerivedData/sim/Build/Products/Debug-iphonesimulator/hootowl.app
xcrun simctl launch --console-pty "$UDID" com.sharkda.hootowl
```

**The line that means it works:**

```
BannerView  83  bannerViewDidReceiveAd(_:)   🟢 bannerViewDidReceiveAd h=100.0
```

That is the SDK initialising, requesting, and *receiving* an ad. `🏗️ banner makeUIView` alone is not enough — it only proves the view was created.

Also confirm the version that actually ended up in the bundle, not just on disk:

```sh
/usr/libexec/PlistBuddy -c 'Print :CFBundleShortVersionString' \
  DerivedData/sim/Build/Products/Debug-iphonesimulator/hootowl.app/Frameworks/GoogleMobileAds.framework/Info.plist
```

### 8. Commit — and use `git add -A`, or you will commit a broken framework

**This is the step with a trap in it.** A version bump is not just modified files. The 13.3.0 → 13.10.0 swap was:

| | count | what |
|---|---|---|
| `M` | 14 | the binaries, signature and Info.plists |
| `D` | 18 | headers that no longer exist (the `*_Beta.h` preload headers) |
| `??` | **2** | **new, untracked** — `PrivateHeaders/` in each slice |

**`git commit -am` would silently skip the two untracked directories.** It would still build *on this machine*, because the files are on disk — and be **missing from the framework for anyone who clones or pulls.** That is the worst shape of bug: works here, broken everywhere else, and the cause is invisible in the diff.

```sh
git add -A GoogleMobileAds.xcframework
git status --porcelain GoogleMobileAds.xcframework | grep '^??'   # must print nothing
git commit -m "Update Google Mobile Ads SDK to <version>"
git push
```

Commit it **on its own**, never folded into source changes, so it can be reverted in one step.

### 9. Push — this is the only way the other machine gets it

**The xcframework is the delivery mechanism.** Until the commit is pushed, the new SDK exists only in one working tree. A second machine that pulls before then gets the *old* version and has no way to know it is behind, because nothing in the project declares a version.

Confirm after pushing:

```sh
git status -sb | head -1          # expect: ## main...origin/main   (no "ahead")
```

---

## Known consequences of this approach

**`Upload Symbols Failed` on every upload, forever.** Google ships no dSYM and the embedded framework's UUID is regenerated on every build, so the warning can never be satisfied. It runs *after* the binary is accepted and blocks nothing. Full explanation: [[operations#the-upload-symbols-failed-warning--ignore-it-permanently]].

**Nothing tells you a new version exists.** With SPM, Xcode would offer an update. Here, step 1 of the runbook is the only mechanism — worth running before each release.

---

## Version history

| Date | Version | Notes |
|---|---|---|
| ~2026-04-10 | **13.3.0** | The vendored xcframework as first committed. Replaced the earlier SPM dependency. |
| **2026-09-20** | **13.10.0** | Seven minor versions in one step. **No source change required** — all four configurations built unmodified, and a test banner loaded on the iPhone 18 Pro / iOS 27.0 simulator (`🟢 bannerViewDidReceiveAd`, zero errors). Checksum verified against Google's published value `04a18e81…5321c`; signature `EQHXZ8M8AV`. Same two slices, same layout, still carries its own `PrivacyInfo.xcprivacy` per slice. |

## Related
[[Admob]] — the three findings and their status · [[operations#2b-ads-idfa-and-territories]] — ads, IDFA and territories · [[operations#the-upload-symbols-failed-warning--ignore-it-permanently]] — the dSYM warning · [[bugs]] · [[jim-actions]]
