# NotebookLM CLI 速查表

> 工具：`notebooklm`（Python CLI）
> 版本參考：2026-04
> 執行檔：`C:/Users/pokai.huang/AppData/Local/Programs/Python/Python312/Scripts/notebooklm.exe`

## 目錄
1. [Windows 必看：UTF-8 設定](#windows-必看utf-8-設定)
2. [認證與工作階段](#認證與工作階段)
3. [筆記本管理](#筆記本管理)
4. [Sources（來源）](#sources來源)
5. [Notes（筆記）](#notes筆記)
6. [Chat（問答）](#chat問答)
7. [Artifacts（AI 產出物）](#artifactsai-產出物)
8. [Research（深度研究）](#research深度研究)
9. [Share（分享）](#share分享)
10. [Language（語言設定）](#language語言設定)
11. [常用組合流程](#常用組合流程)
12. [小技巧 & 踩雷筆記](#小技巧--踩雷筆記)

---

## Windows 必看：UTF-8 設定

Windows 的 cp950 console 無法處理部分 Unicode 字元（`™`、`—`、emoji 等），執行任何輸出包含這些字元的指令前請加上環境變數：

```bash
export PYTHONIOENCODING=utf-8
export PYTHONUTF8=1
notebooklm summary
```

或每次一起下：

```bash
PYTHONIOENCODING=utf-8 PYTHONUTF8=1 notebooklm summary
```

> 💡 Git Bash 可以在 `~/.bashrc` 加一次就好。

---

## 認證與工作階段

| 指令 | 說明 |
|---|---|
| `notebooklm login` | 開瀏覽器登入 Google 帳號 |
| `notebooklm auth check` | 檢查登入狀態與診斷問題 |
| `notebooklm status` | 顯示目前選中的 notebook 與 conversation |
| `notebooklm status --paths` | 顯示設定檔路徑（debug 用） |
| `notebooklm use <partial-id>` | 設定目前作業的 notebook（後續指令都用這個） |
| `notebooklm clear` | 清除 current notebook |

**Partial ID 一個重要特色**：幾乎所有需要 ID 的地方都可以只打前幾碼。
```bash
notebooklm use a3aad3ec         # 自動匹配 a3aad3ec-ecf3-4468-a0d9-...
```

---

## 筆記本管理

| 指令 | 說明 |
|---|---|
| `notebooklm list` | 列出所有筆記本 |
| `notebooklm list --json` | JSON 格式輸出 |
| `notebooklm create "標題"` | 建立新筆記本 |
| `notebooklm rename "新標題" -n <id>` | 改名 |
| `notebooklm delete -n <id>` | 刪除（會問 y/n） |
| `notebooklm delete -n <id> -y` | 跳過確認直接刪 |
| `notebooklm summary` | 取得 AI 摘要 |
| `notebooklm summary --topics` | 摘要 + 建議主題 |
| `notebooklm metadata` | 匯出筆記本 meta + sources 清單 |
| `notebooklm metadata --json` | JSON 版 metadata |

**範例：**
```bash
notebooklm create "2026 Q2 產品研究"
notebooklm list --json > notebooks.json
notebooklm summary --topics > summary.md
```

---

## Sources（來源）

### 新增

| 指令 | 說明 |
|---|---|
| `notebooklm source add <url-or-file-or-text>` | 自動判斷類型新增 |
| `notebooklm source add "./doc.md"` | 本機 .txt/.md → 當 text 上傳 |
| `notebooklm source add "https://example.com"` | URL → web page |
| `notebooklm source add "https://youtube.com/watch?v=..."` | YouTube 影片 |
| `notebooklm source add "貼一段筆記" --title "標題"` | Inline text |
| `notebooklm source add "./report.pdf" --type file --mime-type application/pdf` | PDF / 其他檔案 |
| `notebooklm source add-drive <file-id> "標題" --mime-type google-doc` | Google Drive 文件 |
| `notebooklm source add-research "查詢關鍵字" --from web` | 讓 NotebookLM 上網找 |
| `notebooklm source add-research "..." --mode deep --import-all` | 深度研究 + 自動匯入全部結果 |

**常用 `--type` 值：** `url` / `text` / `file` / `youtube`

### 查詢

| 指令 | 說明 |
|---|---|
| `notebooklm source list` | 列出所有 sources |
| `notebooklm source list --json` | JSON 輸出（含 ID、類型、狀態） |
| `notebooklm source get <partial-id>` | 取得來源內容（文字版） |
| `notebooklm source fulltext <partial-id>` | 取得完整索引文字 |
| `notebooklm source guide <partial-id>` | AI 摘要 + 關鍵字 |
| `notebooklm source stale <partial-id>` | 檢查 URL/Drive 來源是否需要更新 |

### 管理

| 指令 | 說明 |
|---|---|
| `notebooklm source rename <id> "新標題"` | 改名 |
| `notebooklm source refresh <id>` | 重新抓取 URL/Drive 內容 |
| `notebooklm source delete <id>` | 刪除 |
| `notebooklm source delete-by-title "確切標題"` | 用標題刪（完全比對） |
| `notebooklm source wait <id>` | 等待處理完成 |

**範例：**
```bash
# 列出所有 source ID 與標題
notebooklm source list --json | jq '.sources[] | {id, title}'

# 批次抓取所有 source 內容
for id in $(notebooklm source list --json | jq -r '.sources[].id'); do
  notebooklm source get "$id" > "sources/$id.txt"
done
```

---

## Notes（筆記）

| 指令 | 說明 |
|---|---|
| `notebooklm note list` | 列出所有筆記 |
| `notebooklm note create "內容" --title "標題"` | 建立筆記 |
| `notebooklm note get <partial-id>` | 讀筆記內容 |
| `notebooklm note save <id> "新內容"` | 更新筆記內容 |
| `notebooklm note rename <id> "新標題"` | 改名 |
| `notebooklm note delete <id>` | 刪除 |

---

## Chat（問答）

### 基本問答

| 指令 | 說明 |
|---|---|
| `notebooklm ask "問題"` | 問目前 notebook（延續上次對話） |
| `notebooklm ask "問題" --new` | 開新對話（不延續） |
| `notebooklm ask "問題" -c <conv-id>` | 延續指定對話 |
| `notebooklm ask "問題" -s <src-id> -s <src-id>` | 只針對特定 source 提問 |
| `notebooklm ask "問題" --json` | JSON 輸出（含引用來源） |
| `notebooklm ask "問題" --save-as-note` | 答案直接存成筆記 |
| `notebooklm ask "問題" --save-as-note --note-title "分析結果"` | 存筆記並指定標題 |

### 對話設定

```bash
# 四種預設模式
notebooklm configure --mode default
notebooklm configure --mode learning-guide   # 教育導向
notebooklm configure --mode concise          # 精簡
notebooklm configure --mode detailed         # 詳細

# 自訂人格
notebooklm configure --persona "你是一位資深 PM，回答要務實具體"

# 回應長度
notebooklm configure --response-length longer   # 或 default / shorter
```

### 對話歷史

| 指令 | 說明 |
|---|---|
| `notebooklm history` | 顯示最近對話 Q&A 預覽 |
| `notebooklm history --show-all` | 顯示完整內容 |
| `notebooklm history --json` | JSON 輸出 |
| `notebooklm history -l 5` | 只顯示最近 5 輪 |
| `notebooklm history --save --note-title "對話紀錄"` | 對話存成筆記 |
| `notebooklm history --clear` | 清除本地對話快取 |

**範例：**
```bash
# 針對特定來源連續問答
notebooklm ask "這份文件的核心觀點是什麼？" -s a1b2c3d4 --json > q1.json
notebooklm ask "它有哪些反對意見？"  # 自動延續上面的對話

# 把答案直接變成筆記
notebooklm ask "整理出 5 個行動項目" --save-as-note --note-title "Action Items"
```

---

## Artifacts（AI 產出物）

NotebookLM 可以自動生成多種產出物：音檔、影片、簡報、報告、心智圖、快閃卡、測驗、資料表、資訊圖表。

### 產生（generate）

所有 `generate` 指令都支援：
- `-s <src-id>` 限定特定 source
- `--wait` 同步等完成（預設 `--no-wait`）
- `--retry N` 被限流時重試 N 次
- `--json` JSON 輸出
- `--language <code>` 指定語言

| 指令 | 選項 |
|---|---|
| `notebooklm generate audio "主題描述"` | `--format deep-dive\|brief\|critique\|debate` <br> `--length short\|default\|long` |
| `notebooklm generate video "描述"` | `--format explainer\|brief\|cinematic` <br> `--style auto\|classic\|whiteboard\|kawaii\|anime\|watercolor\|retro-print\|heritage\|paper-craft` |
| `notebooklm generate slide-deck "描述"` | `--format detailed\|presenter` <br> `--length default\|short` |
| `notebooklm generate report "描述"` | `--format briefing-doc\|study-guide\|blog-post\|custom` <br> `--append "額外指示"` |
| `notebooklm generate mind-map` | — |
| `notebooklm generate flashcards "描述"` | `--quantity fewer\|standard\|more` <br> `--difficulty easy\|medium\|hard` |
| `notebooklm generate quiz "描述"` | 同 flashcards |
| `notebooklm generate data-table "描述"` | — |
| `notebooklm generate infographic "描述"` | `--orientation landscape\|portrait\|square` <br> `--detail concise\|standard\|detailed` <br> `--style auto\|sketch-note\|professional\|bento-grid\|editorial\|instructional\|bricks\|clay\|anime\|kawaii\|scientific` |

**範例：**
```bash
notebooklm generate audio "深入淺出討論 VMX 產品定位" --format deep-dive --length long --wait
notebooklm generate video "給非技術主管看的 3 分鐘總覽" --format explainer --style whiteboard
notebooklm generate slide-deck "高階主管簡報，含講者備註" --format presenter
notebooklm generate report --format briefing-doc --append "聚焦風險與下一步"
notebooklm generate mind-map
notebooklm generate flashcards --quantity more --difficulty hard
notebooklm generate infographic "呈現 key metrics" --orientation portrait --style editorial
```

### 查詢 / 下載

| 指令 | 說明 |
|---|---|
| `notebooklm artifact list` | 列出所有產出物 |
| `notebooklm artifact list --type audio` | 依類型過濾 |
| `notebooklm artifact get <id>` | 取得產出物詳情 |
| `notebooklm artifact rename <id> "新名"` | 改名 |
| `notebooklm artifact delete <id>` | 刪除 |
| `notebooklm artifact poll <id>` | 查生成狀態（單次） |
| `notebooklm artifact wait <id>` | 等待生成完成（blocking） |
| `notebooklm artifact export <id>` | 匯出到 Google Docs/Sheets |
| `notebooklm artifact suggestions` | AI 建議可產生的 report 主題 |

**下載**（每種類型獨立指令）：
```bash
notebooklm download audio                 # 最新的音檔
notebooklm download audio my.mp3          # 指定檔名
notebooklm download audio --all ./audio/  # 全部下載到資料夾
notebooklm download audio --name "chapter 3"  # 用標題模糊比對
notebooklm download audio --all --dry-run # 預覽（不下載）

notebooklm download report               # 預設 .md
notebooklm download slide-deck           # 預設 PDF
notebooklm download slide-deck --format pptx
notebooklm download mind-map             # JSON
notebooklm download video
notebooklm download flashcards
notebooklm download quiz
notebooklm download data-table
notebooklm download infographic
```

共用選項：`--latest` / `--earliest` / `--all` / `--name <text>` / `-a <artifact-id>` / `--dry-run`

---

## Research（深度研究）

搭配 `source add-research --no-wait` 使用：

```bash
# 1. 啟動非同步研究
notebooklm source add-research "車聯網市場趨勢" --mode deep --no-wait

# 2. 查狀態
notebooklm research status

# 3. 等它跑完並自動匯入
notebooklm research wait --import-all
```

---

## Share（分享）

| 指令 | 說明 |
|---|---|
| `notebooklm share status` | 顯示目前分享狀態 |
| `notebooklm share public --enable` | 開啟公開連結 |
| `notebooklm share public --disable` | 關閉公開連結 |
| `notebooklm share view-level <level>` | 設定檢視權限（full / chat-only） |
| `notebooklm share add user@example.com --permission viewer` | 加入使用者（viewer/editor） |
| `notebooklm share update user@example.com --permission editor` | 更新權限 |
| `notebooklm share remove user@example.com` | 移除 |

---

## Language（語言設定）

> ⚠️ 這是**全域設定**，會影響你帳號下所有筆記本的產出物語言。

```bash
notebooklm language list             # 列出支援語言
notebooklm language get              # 查目前設定
notebooklm language set zh_Hant      # 設為繁體中文
notebooklm language set zh_Hans      # 簡體
notebooklm language set en           # 英文
notebooklm language set ja           # 日文
```

---

## 常用組合流程

### 1. 把整本筆記本備份到本機（跟我們今天做的一樣）

```bash
export PYTHONIOENCODING=utf-8 PYTHONUTF8=1
notebooklm use <partial-id>

mkdir -p backup/sources backup/notes
notebooklm metadata --json > backup/metadata.json
notebooklm summary --topics > backup/summary.md
notebooklm source list --json > backup/sources/_index.json
notebooklm history --json > backup/history.json

# 批次抓所有 source
for id in $(jq -r '.sources[].id' backup/sources/_index.json); do
  notebooklm source get "$id" > "backup/sources/$id.txt"
done

# 批次抓所有 note
for id in $(notebooklm note list --json 2>/dev/null | jq -r '.notes[].id'); do
  notebooklm note get "$id" > "backup/notes/$id.md"
done
```

### 2. 新建筆記本並灌入多個來源

```bash
notebooklm create "我的研究" --json | jq -r '.id' | xargs notebooklm use

notebooklm source add "https://example.com/paper1"
notebooklm source add "./local-notes.md"
notebooklm source add-drive 1ABC...XYZ "公司報告" --mime-type google-doc
notebooklm source add-research "delivery robot industry" --from web --import-all
```

### 3. 問答 → 存成筆記 → 匯出報告

```bash
notebooklm configure --mode detailed --response-length longer

notebooklm ask "整理出前 5 大趨勢" --save-as-note --note-title "Top Trends"
notebooklm ask "每個趨勢對應的機會與風險？"  # 延續對話
notebooklm history --save --note-title "趨勢分析對話記錄"

notebooklm generate report --format briefing-doc --append "包含風險評估" --wait
notebooklm download report ./trends-briefing.md
```

### 4. 播客 + 簡報一起生

```bash
notebooklm generate audio "30 分鐘深度討論" --format deep-dive --length long --no-wait
notebooklm generate slide-deck "執行摘要" --format presenter --length short --no-wait

# 等到好了再下載
notebooklm artifact list --type audio
notebooklm download audio --latest ./podcast.mp3
notebooklm download slide-deck --latest ./deck.pdf
```

### 5. 針對單一來源做深入分析

```bash
# 先找到 source ID
SRC=$(notebooklm source list --json | jq -r '.sources[] | select(.title | contains("VMX")) | .id' | head -1)

notebooklm source guide "$SRC"
notebooklm ask "這份資料的核心論點是什麼？" -s "$SRC"
notebooklm generate flashcards -s "$SRC" --difficulty medium --wait
notebooklm download flashcards ./vmx-cards.json
```

---

## 小技巧 & 踩雷筆記

### ✅ 好用小技巧
- **Partial ID 到處都能用**：`notebooklm use a3` 就夠了
- **`--json` 搭配 `jq` 很強**：所有查詢類指令都支援，適合做 pipeline
- **`--wait` vs `--no-wait`**：批次產圖時用 `--no-wait` 不卡住，最後用 `artifact list` / `artifact wait` 統一收斂
- **`--save-as-note`**：問答完直接存成筆記，省去 copy-paste
- **`--retry N`**：遇到限流時自動重試，適合長任務

### ⚠️ 踩雷筆記
- **Windows 必設 UTF-8**：沒設會在含 `™` 等字元時噴 `UnicodeEncodeError`
- **原始檔無法下載**：`source get` 只能拿到 CLI 處理後的文字；m4a/mp4/pdf 原檔請從原始來源取得
- **`language set` 是全域**：改了會影響所有筆記本的產出物，不是個別設定
- **`note list` 沒有 `--json`**：目前只能拿文字格式（ID 會被截斷顯示為 `49fe9299-58b...`），但 `note get <partial-id>` 還是能用
- **套件會過期**：看到 `UnknownTypeWarning: Unknown source type code 18` 的話跑 `pip install -U notebooklm-py` 升級

### 🔍 除錯
```bash
notebooklm -v <command>         # INFO 級別訊息
notebooklm -vv <command>        # DEBUG 級別
notebooklm status --paths       # 看設定檔位置
notebooklm auth check           # 認證問題診斷
```

### 📁 預設路徑
- Auth：`C:\Users\<you>\.notebooklm\storage_state.json`
- 可用 `--storage <path>` 或環境變數 `NOTEBOOKLM_HOME` 覆蓋

---

## 快速備忘卡

```
認證        login / auth check / status / use <id> / clear
筆記本      list / create / rename / delete / summary / metadata
來源        source {list,add,add-drive,add-research,get,fulltext,guide,rename,refresh,delete,wait,stale}
筆記        note {list,create,get,save,rename,delete}
對話        ask / configure / history
產出        generate {audio,video,slide-deck,report,mind-map,flashcards,quiz,data-table,infographic}
下載        download {audio,video,slide-deck,report,mind-map,flashcards,quiz,data-table,infographic}
產物管理    artifact {list,get,rename,delete,poll,wait,export,suggestions}
研究        research {status,wait}
分享        share {status,public,view-level,add,update,remove}
語言        language {list,get,set}
```
