
```markdown
## 📝 製作備註（錄音時可刪）

- **選篇檢查**：這篇適合 9 歲嗎？有沒有太恐怖／太成人的情節要拿掉？
- **朗讀技巧**：「——」停一下製造期待；對話可變聲；想像面對面講給一個小孩聽。
- **錄音狀態**：☐ 已寫稿　☐ 已試讀　☐ 已錄音　☐ 已上架
```

Now saving it as a file you can drop straight into your vault:

Created a file, read a file

範本檔好了，直接放進 vault 的 `templates` 資料夾就能用。

幾個 Obsidian 使用重點：

- **`{{date}}` 和 `{{title}}`** 是 Obsidian 內建變數。用內建的 **Templates** 或 **Templater** 外掛套用時，`{{date}}` 會自動換成當天日期；`{{title}}` 會換成你新筆記的檔名，所以你可以把檔名取成故事名，`title` 欄就自動帶入。
- **`<<...>>`** 是我自己放的填空記號（Obsidian 不會自動處理），提醒你哪裡要換字。套用範本後，用搜尋 `<<` 就能快速跳到每個要填的地方。
- 最上面的 YAML 會變成筆記的 **properties**，`status: draft` 之後可以改成 `published`，配合 Dataview 就能一眼看到哪幾集還沒錄。

如果你有裝 **Templater** 外掛，還能再進一步：把「集數」做成自動遞增、或套用時跳出視窗問你故事名。要的話我可以給你一版 Templater 語法的進階範本。

不然，我也可以直接照這個範本幫你把 **嶗山道士** 寫成第二集。你想先要哪一個？