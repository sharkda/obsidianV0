# Upstream data sources and their contacts

> [!important] This is **my** standing job, not Jim's
> The contact details the app shows users are scraped from each city's open-data portal and point at **named individuals**. People change roles and extensions get reassigned, so these rot silently — nothing in the app can detect it.
> **I re-check this note at session START whenever the "last checked" date below is more than ~30 days old, and always before a release.** Jim should not have to remember it. The commands are at the bottom; a mismatch is fixed by editing the Gist, which needs no app release.

| City | Last checked | Next check due |
|---|---|---|
| 臺北市 | **2026-09-09** | 2026-10-09 |
| 新北市 | **2026-09-09** | 2026-10-09 |

**Live Gist right now (version 5):** Taipei `sb0457@gov.taipei` / `02-27590666#6543`; New Taipei `ae8131@ntpc.gov.tw` / `02-29702960`. Both cities complete.

---

## 臺北市 (Taipei)

**Source:** https://data.taipei/dataset/detail?id=d5c0656b-5250-4179-a491-c94daa56ef2c
**Dataset:** 臺北市停車場資訊 — the app's own feed, publishing both 臺北市停車場資訊V2 (static) and 剩餘停車位數V2 (live).

| Field | Value as of 2026-09-09 |
|---|---|
| 提供機關 | 交通局停管處 |
| 聯絡人 | 王韋翔 |
| 電話 | **02-27590666#6543** |
| 電子郵件 | **sb0457@gov.taipei** |
| 更新頻率 | 每1月 (metadata); 詮釋資料更新時間 2026-08-06 |

**The extension survives the app's dialling code:** `resolvedTelURL` rewrites `#` to `;` and keeps digits, `+` and `;`, so this becomes `tel:0227590666;6543` — pause-then-extension. Paste it as published.

## 新北市 (New Taipei City)

**Source:** https://data.ntpc.gov.tw/datasets/e09b35a5-a738-48cc-b0f5-570b67ad9c78
**Dataset:** 新北市公有路外停車場即時賸餘車位數 — the live availability feed.

| Field | Value as of 2026-09-09 |
|---|---|
| 提供機關 | 新北市政府交通局 |
| 聯絡人 | 張先生 |
| 電話 | **8607** — an extension only; see the resolution below |
| 電子郵件 | **ae8131@ntpc.gov.tw** |
| 更新頻率 | **每3分鐘** |
| 資料量 | 1249 |
| 授權 | 政府資料開放授權條款-第1版 |

### ⚠️ The bulk download stopped working — 2026-09-16

`…/api/datasets/e09b35a5-a738-48cc-b0f5-570b67ad9c78/csv/file`, the whole-file download the app
fetched every 6 minutes, now returns an F5 **"Request Rejected"** page with **HTTP 200**. It broke
within hours of a successful 1411-row fetch the same day. The block is on that one path — the
*daily* description dataset's `/csv/file` still serves 375KB — and no header, referer or cookie
gets past it.

**What still works**, same dataset: `…/csv?page=N&size=1000` and `…/json?page=N&size=1000`, both
capped at **1000 rows per page** against ~1410 published. The app now pages through the CSV form
(`e45051c`); full diagnosis in [[bugs#2026-09-16 — New Taipei City availability is dead: the bulk CSV is WAF-rejected (open)]].

**Worth a phone call, and there is already a reason to make one.** 張先生 / **ae8131@ntpc.gov.tw**
owns this catalogue entry, and the release to-do below already has an open question for that
bureau. Ask whether the bulk download was withdrawn deliberately or is a WAF misfire — if it is a
misfire, saying so costs nothing and the paging code keeps working either way.

### The phone — resolved 2026-09-09

The portal publishes only `8607`, an extension with no switchboard. Rather than invent one, the Traffic Bureau's own site (https://www.traffic.ntpc.gov.tw/) was checked, and it publishes **two** numbers:

| Number | Published as |
|---|---|
| **02-29702960** | **路邊停車及停車場相關業務** — roadside parking and car-park business |
| 02-29603456 (or 1999 within New Taipei) | the bureau's general switchboard |

**The Gist uses `02-29702960`** — deliberately, and not the dataset contact's extension. Two reasons:

1. **It needs no assumption.** `8607` is published without a switchboard, so `02-29603456#8607` would be a guess about *which* line the extension sits on. The bureau runs two offices at different addresses (板橋 and 三重, the latter explicitly for parking), so that guess could easily be wrong — and a wrong number is precisely what the fake `+886-2-8765-4321` was.
2. **It is the better destination anyway.** Our button means *"this lot's data looks wrong"*. The published parking-business line is the team that owns that, where `8607` reaches the person who maintains the data catalogue.

**Open, and on the release to-do list (2026-09-09):** Jim asked to keep 02-29702960 for now and to confirm it before release. One call settles both halves — does that line handle wrong-space-count reports, and is 張先生's extension 8607 on it or on 02-29603456? If 8607 turns out to sit on a known switchboard, `<switchboard>#8607` reaches the data owner directly, and the app already sends the extension as DTMF after a pause. Either answer is a one-line Gist edit.

### 🎯 This dataset answers the open −9 question

Straight from the dataset description:

> 部分停車場因**更換營運廠商**，尚無提供即時車位，其顯示數值將為 **-9**。

So New Taipei's ~70% `-9` rate is **not a broken feed and not our bug** — those lots are mid-operator-change and genuinely have no live count to report. That reframes the product decision in [[jim-actions]]: the honest UI is to *label* them ("no live data from this lot") rather than hide them, because the lots exist and are usable, they simply do not report. It also means the rate should fall on its own as operators finish switching — worth re-measuring at the next check rather than designing around today's number.

**Also useful:** 更新頻率 每3分鐘 confirms the 5-minute "fresh" threshold in `AvailFreshness` is the right side of the publish interval.

---

## How I re-check — one command per city

```bash
# 臺北市
curl -sS -L "https://data.taipei/dataset/detail?id=d5c0656b-5250-4179-a491-c94daa56ef2c" \
 | python3 -c "import sys,re,html;t=re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>','',sys.stdin.read(),flags=re.S));t=html.unescape(re.sub(r'\s+',' ',t));[print(f,re.search(re.escape(f)+r'\s+(\S+)',t).group(1)) for f in ['機關聯絡人','機關聯絡人電話','機關聯絡人電子郵件']]"

# 新北市
curl -sS -L "https://data.ntpc.gov.tw/datasets/e09b35a5-a738-48cc-b0f5-570b67ad9c78" \
 | python3 -c "import sys,re,html;t=re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>','',sys.stdin.read(),flags=re.S));t=html.unescape(re.sub(r'\s+',' ',t));[print(f,re.search(re.escape(f)+r'\s+(\S+)',t).group(1)) for f in ['資料集提供機關聯絡人姓名','資料集提供機關聯絡人電話','資料集提供機關聯絡人電子郵件']]"
```

If either differs from the tables above: update the Gist ([[operations#how-to-edit-it--step-by-step]] — or I can push it directly over SSH), update the table and the "last checked" date here, and tell Jim what moved.

**Reading the Gist back needs a cache-buster.** GitHub's raw CDN served a stale copy for minutes after a push on 2026-09-09; `…/raw?cb=$RANDOM` returns the real thing.

## Related
[[operations]] · [[jim-actions]] · [[bugs]]
