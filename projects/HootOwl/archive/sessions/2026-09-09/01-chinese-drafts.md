# 2026-09-09 — 中文 drafts for the new strings

👉 **To review them, use [[zh-review]]** — a table you edit in place, one empty column for your corrections. This note is the background: what was and was not translated, and why particular words were chosen.

**33 user-facing keys drafted, committed `7ba53de`, all marked `needs_review`.** Not `translated` — they are drafts by someone who is not a native speaker, and `needs_review` is the state Xcode's catalogue editor surfaces so Jim can walk through them and confirm or correct each one.

## What was and was not translated

**Translated (33):** every `onb_*`, `settings_*` and `sub_*` key — the three onboarding screens, the city-request mail, the Settings rows and the whole subscription screen.

**Deliberately left English (about 24):** the remaining untranslated keys are **developer output** — `twd97_step_1/2/3`, `twd97_workflow_overview`, `consolePipeText`, `detail prompt`, `cyclopsScreen`, and bare format strings like `%@ %@` or `nextPoll: %@\tPubInt:%@`. Translating debug logs is churn with a maintenance cost and no user.

Two entries were **already** `needs_review` before this and are untouched: `cyclops` → 自動更新, `parkNav` → 台北停車s (that trailing "s" looks like a slip).

---

## ⚠️ The one decision this surfaced: 課金 or 訂閱?

The catalogue now uses **both**, and it should use one.

| Where | Term | Origin |
|---|---|---|
| Tab label (`sub_tab_subscribe`) | **課金** | Jim's own word, already in the catalogue |
| Subscription screen (`sub_manage`, `sub_active_title`, states…) | **訂閱** | my drafts |
| `onb_ads_note` | **「課金」** | quotes the tab, so it must match whatever the tab says |

**Recommendation: 訂閱 throughout.** It is what Apple's own iOS UI uses for 續訂 / 到期 / 管理訂閱, so it will sit beside the system's own subscription sheet without reading as two different things — and that sheet is exactly where a user lands from **Manage subscription**. 課金 is idiomatic and has personality, but it is gaming-flavoured and does not extend naturally to "renews on" or "expires on".

**If Jim prefers 課金**, it should replace 訂閱 everywhere, and `onb_ads_note` already matches. Either way, the string that quotes the tab must be kept in step.

## Choices worth a second look

| Key | Draft | Note |
|---|---|---|
| `onb_s1_title` | 即時車位。現在就看。 | Mirrors the two-beat English rhythm. Blunt, per lane 3 |
| `onb_s1_feedback_link` | 申請新增城市 → | Considered 許願城市, which is very idiomatic in Taiwanese app copy but too cute for this voice |
| `onb_s2_freshness` | 資料越舊，數字顏色越淡，一眼就知道新不新。 | Says *colour* fades, which is what the app actually does — the English "fade" is vaguer |
| `onb_s3_cta_skip` | 以後再說 | Apple often uses 稍後; 以後再說 is warmer and reads less like a system dialog |
| `sub_paywall_title` | 廣告養活這個 App | Deliberately colloquial. 養活 is punchy; swap for 廣告是這個 App 的收入來源 if it reads too casual |
| `sub_restore` | 回復購買項目 | Apple's own Taiwan wording — worth keeping verbatim so it matches StoreKit's own buttons |
| `sub_renews_on` / `sub_expires_on` | 續訂日期 / 到期日期 | Labels sit before a date, so noun form rather than a verb |

## Note on Hong Kong and Macau

Both fall back to `zh-Hant`, so they read these strings. The vocabulary is Taiwanese — 停車場 and 車位 are fine in HK, but the register will read as Taiwanese. Acceptable, and worth remembering if HK feedback ever mentions it. No separate `zh-HK` is planned.

## Related
[[jim-actions]] · [[onboarding]] · [[00-subscription-screen]]
