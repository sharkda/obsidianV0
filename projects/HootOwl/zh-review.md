# 中文 review — edit this note in place

**How this works:** the 中文 column is my draft. **Type your correction in the last column.** Leave it blank if the draft is fine. When you're done, tell me and I'll read this note and write your version straight into `Localizable.xcstrings` — you never have to touch the catalogue.

All 33 drafts are marked `needs_review` in Xcode, so nothing here is pretending to be finished.

> [!warning] One decision to make first, because it changes several rows
> The catalogue currently uses **both 課金 and 訂閱**. The tab says **課金** (your word); the subscription screen says **訂閱** (mine).
> **My recommendation: 訂閱 everywhere.** It is what Apple's own iOS subscription sheet uses — and *Manage subscription* sends the user straight into that sheet, so two different words would read as two different things.
> Whichever wins, `onb_ads_note` quotes the tab and has to match. **Answer here →**訂閱

---


### Onboarding — screen 1 · what it is

| key                      | English                                                       | 中文 (my draft)             | note                                                    | ✏️ your fix |
| ------------------------ | ------------------------------------------------------------- | ------------------------- | ------------------------------------------------------- | ----------- |
| `onb_s1_title`           | Live parking. Right now.                                      | **即時車位。現在就看。**            | two beats, mirroring the English                        | 即時找車位       |
| `onb_s1_body`            | Taipei and New Taipei City today — more cities soon.          | **目前支援台北市與新北市，其他縣市陸續加入。** |                                                         |             |
| `onb_s1_feedback_prompt` | Tell us where you need it most — we'll adjust our priorities. | **告訴我們你最需要哪裡，我們會調整順序。**   |                                                         |             |
| `onb_s1_feedback_link`   | Request your city →                                           | **申請新增城市 →**              | considered 許願城市 — idiomatic but too cute for this voice | 我想要這個地區先 -> |

### Onboarding — screen 2 · pinned lots

| key                   | English                                                                                                              | 中文 (my draft)                                      | note                                                            | ✏️ your fix             |
| --------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------------------- | ----------------------- |
| `onb_s2_title`        | Your car parks. One screen.                                                                                          | **你的停車場，一頁看完。**                                    |                                                                 | 停車場即時車位,一目了然            |
| `onb_s2_body`         | Pin the lots you actually use. Open the app and every count is already there — no search, no map, no tapping around. | **把你常去的停車場釘選起來。打開 App 就看到所有車位數，不用搜尋、不用開地圖、不用一直點。** |                                                                 | 直接釘選常用停車場，不用再滑來滑去，手忙腳亂。 |
| `onb_s2_freshness`    | Numbers fade as the data ages, so you always know how current they are.                                              | **隨著時間，未更新的數字顏色越淡，一眼可判讀資料的即時性** | says the **colour** fades, which is what the app literally does |                         |
| `onb_s2_tutorial_cta` | Watch how it works on YouTube →                                                                                      | **到 YouTube 看怎麼用 →**                               |                                                                 | youtube 上的教學影片 ->       |

### Onboarding — screen 3 · location

| key                 | English                                                                                                      | 中文 (my draft)                                  | note                                                     | ✏️ your fix                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------- | -------------------------------------------------------- | -------------------------------------- |
| `onb_s3_title`      | Find what's near you                                                                                         | **找出你附近的車位**                                   |                                                          |                                        |
| `onb_s3_body`       | Turn on location and the closest lots come first. Used only while the app is open — never in the background. | **開啟定位，最近的停車場就排在最前面。只在使用 App 時取用，絕不在背景執行。**    |                                                          | 開啟定位，最近的停車場就排在最前面。只在使用 App 時取用，切入背景就停止 |
| `onb_s3_cta_enable` | Enable Location                                                                                              | **開啟定位**                                       |                                                          |                                        |
| `onb_s3_cta_skip`   | Not now                                                                                                      | **以後再說**                                       | Apple often uses 稍後; this reads warmer                   |                                        |
| `onb_ads_note`      | Ads keep this free. You can turn them off any time from Subscribe — look for this button on any screen: | **廣告讓這個 App 免費。你隨時可以「訂閱」把廣告關掉——在各頁面找這個圖示：** | the arrow and glyph after it are drawn by the code, not part of the string — keep the trailing colon |                                        |
|                     |                                                                                                              |                                                |                                                          |                                        |

### City request mail

| key | English | 中文 (my draft) | note | ✏️ your fix |
|---|---|---|---|---|
| `onb_feedback_subject` | City request | **城市需求** |  | |
| `onb_feedback_body` | Which city or district do you want parking for?<br><br>Anything else we should add? | **你希望我們支援哪個縣市或行政區？<br><br>還有什麼想加的功能嗎？** |  | |
| `onb_feedback_sent` | Noted. We'll get to it when we can. | **收到了。我們會盡快處理。** |  | |

### Settings rows

| key | English | 中文 (my draft) | note | ✏️ your fix |
|---|---|---|---|---|
| `settings_request_city` | Request a city | **申請新增城市** |  | |
| `settings_send_feedback` | Send feedback | **意見回饋** |  | |
| `settings_rate_app` | Rate the app | **為這個 App 評分** |  | |

### Subscription — paywall, not subscribed

| key                 | English                                                                                                                                                                                             | 中文 (my draft)                                               | note                                        | ✏️ your fix                               |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------- | ----------------------------------------- |
| `sub_paywall_title` | Ads keep this app running                                                                                                                                                                           | **廣告養活這個 App**                                              | colloquial on purpose. alt: 廣告是這個 App 的收入來源 |                                           |
| `sub_paywall_body`  | There will be more of them over time. If you'd rather they stayed out of your way, a subscription turns them off completely — live counts, pinned lots and search work exactly the same either way. | **之後廣告會越來越多。如果你不想被打擾，訂閱可以把廣告完全關掉——即時車位、釘選的停車場和搜尋，訂不訂閱都一樣。** |                                             | 可能廣告會越來越多。如果你不想被打擾，訂閱可以把廣告完全關掉，目前免費版本功能齊全 |

### Subscription — active state

| key | English | 中文 (my draft) | note | ✏️ your fix |
|---|---|---|---|---|
| `sub_active_title` | You're subscribed | **你已訂閱** | ⚠️ 訂閱 | |
| `sub_active_thanks` | Thanks — the ad banner stays off. | **謝謝支持，廣告已經關閉。** |  | |
| `sub_renews_on` | Renews on | **續訂日期** | noun form — sits before a date | |
| `sub_expires_on` | Expires on | **到期日期** | noun form — sits before a date | |
| `sub_manage` | Manage subscription | **管理訂閱** | ⚠️ 訂閱 — opens Apple's own sheet, which also says 訂閱 | |
| `sub_restore` | Restore purchases | **回復購買項目** | Apple's own Taiwan wording, kept verbatim to match StoreKit's buttons | |
| `sub_restoring` | Restoring… | **回復中…** |  | |
| `sub_sheet_done` | Done | **完成** |  | |

### Subscription — payment problems

| key | English | 中文 (my draft) | note | ✏️ your fix |
|---|---|---|---|---|
| `sub_state_grace` | There's a problem with your payment. Your subscription is still active for now. | **付款發生問題，訂閱目前仍然有效。** |  | |
| `sub_state_billing_retry` | There's a problem with your payment. Apple is retrying it. | **付款發生問題，Apple 正在重試。** |  | |
| `sub_state_expired` | Your subscription has ended. | **你的訂閱已經結束。** |  | |
| `sub_state_revoked` | This subscription was refunded. | **這筆訂閱已退款。** |  | |

### Tab label — already had 中文, listed for the 課金/訂閱 call

| key | English | 中文 (my draft) | note | ✏️ your fix |
|---|---|---|---|---|
| `sub_tab_subscribe` | Subscribe | **課金** | your word, unchanged | |
| `sub_tab_mine` | My Subscription | **我的課金** | ⚠️ my draft, composed from your 課金 | |


### Second batch — 2026-09-10 · strings a shipping user sees

Found from the simulator screenshot: the tab bar mixed 自動更新 / 更多 with **"Near Me!"**, **"all"**, **"options"**, and the search field read **"Address or place"**. Those keys had no 中文 at all.

Eleven keys, chosen by tracing what is reachable from the six tabs in `AppScreen.sorted()`. The other 23 untranslated keys live on kitchen and retriever screens no user can open, and are deliberately left English.

| key | English | 中文 (my draft) | ✏️ your fix |
|---|---|---|---|
| `Near Me!` | Near Me! | **附近車位** | |
| `all` | all | **全部** | |
| `options` | options | **選項** | |
| `Address or place` | Address or place | **地址或地點** | |
| `Location access is disabled` | Location access is disabled | **定位權限已關閉** | |
| `This page requires location permission (Whil` | This page needs location permission to find parking near you. Turn it on in Settings. | **這個頁面需要定位權限才能找出你附近的停車場，請到「設定」開啟。** | |
| `Open Settings` | Open Settings | **前往設定** | |
| `reorder` | reorder | **重新排序** | |
| `Reset to defaults` | Reset to defaults | **回復預設值** | |
| `subscribe` | subscribe | **訂閱** | |
| `showToolbar` | showToolbar | **顯示工具列** | |

⚠️ One English string was **corrected**, not just translated: the denied-location banner said the page *"requires location permission (While Using or Always)"*. iOS has not asked for Always since battery #9 in June — the same stale-claim class as the "background nearby search" banner. It now reads *"This page needs location permission to find parking near you. Turn it on in Settings."*

---

## Not translated, on purpose

About 24 keys are still English-only and should stay that way — they are developer output: `twd97_step_1/2/3`, `twd97_workflow_overview`, `consolePipeText`, `detail prompt`, `cyclopsScreen`, and bare format strings like `%@ %@` or `nextPoll: %@\tPubInt:%@`. Nobody reads debug logs in Chinese, and translating them is maintenance with no user.

## Two older entries worth a glance while you're here

Both were already `needs_review` before this pass and I have not touched them:

| key | 中文 | |
|---|---|---|
| `cyclops` | 自動更新 | |
| `parkNav` | 台北停車s | the trailing "s" looks like a slip |

## Note on Hong Kong / Macau

They fall back to `zh-Hant`, so they read exactly these strings. 停車場 and 車位 are fine there, but the register will read as Taiwanese. Acceptable; no separate `zh-HK` planned.

## Related
[[jim-actions]] · [[01-chinese-drafts]] · [[onboarding]]

---

# ✅ Applied — 2026-09-09 (`2a42a2c`)

All seven corrections applied **verbatim**, and every zh-Hant entry moved from `needs_review` to `translated` — a blank row meant approved.

**訂閱 won.** The tab labels dropped 課金 (now 訂閱 / 我的訂閱) and `onb_ads_note`, which quotes the tab, followed. Three 課金 strings remain in the catalogue — `entitle`, `EntitleViewIntro`, `renew on:` — all belonging to the unwired `EntitledView`, so nothing displays them. Left alone rather than churning dead strings.

## Five things I noticed applying them — none blocking

Listed once; say the word on any and it is a one-line change each.

**1. ~~Two trailing arrows disappeared~~ — both restored in the second pass.** `onb_s1_feedback_link` (`我想要這個地區先`) and `onb_s2_tutorial_cta` (`youtube 上的教學影片`) both lost the `→` the English still has. The arrow is the affordance that says *this is tappable* — without it the Chinese UI reads as a label, not a link. **Recommend adding both back.**

**2. ~~`youtube` → `YouTube`~~** — applied 2026-09-09 on Jim's word.

**3. `onb_s2_title` — re-read and kept, now 停車場即時車位，一目了然.** Draft was 你的停車場，一頁看完 ("your car parks, one screen"); it is now **停車場即時車位** ("car park live spaces"). That is what *every* competitor does — and it is the exact thing you pushed back on when the copy was chosen on 2026-09-05:

> *"most of the app out there using Map, we do that too, but Cyclops is our differential feature… 2 is OK too, but not Cyclops highlighting enough."*

Screen 2 exists to sell the pinned watch list. The body still carries it (`直接釘選常用停車場`), so the meaning is not lost — but the headline no longer leads with it. **Worth one re-read**; your call, and the new title is shorter and punchier, which is a real argument for it.

**4. ~~The privacy clause is now English-only~~ — restored as 切入背景就停止, which is *more* accurate than the English.** `onb_s3_body` dropped **絕不在背景執行** ("never runs in the background"), which the English keeps. Nothing untrue results — but it is the strongest privacy reassurance on the screen, it is [[00-location-privacy-audit|backed six ways in the code]], and a Chinese reader now gets less than an English one. Also lost its closing 。

**5. ~~The paywall no longer says what stays the same~~ — restored as 目前免費版本功能齊全.** `sub_paywall_body` dropped 即時車位、釘選的停車場和搜尋，訂不訂閱都一樣. That clause was doing honesty work — it is what stops the paywall implying features are locked. The English keeps it.

*(Your 之後 → 可能 change in the same string is an improvement and stays: "ads **may** increase" is a weaker commitment than "ads **will** increase", and easier to live with later.)*
