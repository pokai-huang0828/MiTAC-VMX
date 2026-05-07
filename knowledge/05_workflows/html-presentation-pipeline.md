# HTML 簡報製作 SOP

> 2026-05-05 起,新標準對齊 MDT 2026 PowerPoint 模板色 + Calibri

## 色票(寫死在 build script)

```python
# 對齊 MDT 2026 模板
ACCENT1     = '#5B9BD5'  # 主藍
ACCENT5     = '#4472C4'  # 深藍
ACCENT2     = '#ED7D31'  # 橘(強調 / CTA)
ACCENT3     = '#A5A5A5'  # 灰
ACCENT4     = '#FFC000'  # 金
ACCENT6     = '#70AD47'  # 綠
TEXT        = '#1B2541'  # 內文深色
TEXT_LIGHT  = '#5A6779'  # 副文字
BG          = '#FFFFFF'  # 白底
BG_SOFT     = '#F4F6FA'  # 卡片背景
BG_STRIPE   = '#EAEDF2'  # 表格條紋
```

⚠️ **舊 navy `#003B71` + Cabinet Grotesk + Satoshi 已作廢**(2026-05-05)

## 字型(系統字型,不依賴 CDN)

- **英文**:Calibri / Segoe UI fallback
- **中文**:微軟正黑體 / 思源宋體 fallback

## HTML 簡報必備結構

1. ⭐ 套 viewport-base.css(來自 frontend-slides skill,每張 slide 嚴格 `100vh`)
2. CSS 用 `clamp()` 做尺寸,**絕對不寫 fixed px**(否則小螢幕破版)
3. 動畫用 `@keyframes revealIn` + `animation: ... both`
   - **不要**用 `.reveal { opacity: 0 }` + transition + IntersectionObserver(會卡在 0 不顯示)
   - 直接用 keyframe 載入即播
4. **Slide types**:`cover` / `section-divider` / `inner` / `end-slide`
5. **JS controller**:`SlidePresentation` 類處理鍵盤 / 觸控 / progress bar / nav dots

## 已踩過的坑

- ⚠️ **navigate tool 對 `file://` URL 會失敗**(自動加 https://)
  → 用本機 HTTP server:`python -m http.server 8766`(在 portal_reference/)
- ⚠️ PowerPoint COM 自動化用 win32com:`pip install pywin32`,需要 Windows + 已裝 PowerPoint
- ⚠️ LibreOffice / pdftoppm 沒裝 → 用 PowerPoint COM 替代(已寫好 export_pngs.py / export_pdf.py)
- ⚠️ pdftoppm 沒裝:Read tool 讀 PDF 會失敗。改用 PyMuPDF(`pip install pymupdf`)抽文字
- ⚠️ JS console.log 在 Chrome MCP 會被擋(`[BLOCKED]`)— 改用回傳值的方式 debug

## 已存在 build script(可拷貝改)

| 檔案 | 角色 |
|---|---|
| `../../portal_reference/build_html_replica.py` ⭐ | 55 頁 PDF 複刻 HTML 生成器 |
| `../../portal_reference/build_briefing_html.py` ⭐ | 25 頁客戶簡報 HTML 生成器 |
| `../../portal_reference/build_replica_pptx.py` | 55 頁 .pptx 生成器 |
| `../../portal_reference/export_pngs.py` | PowerPoint COM .pptx → PNG |
| `../../portal_reference/export_pdf.py` | PowerPoint COM .pptx → PDF |

⚠️ 既有 build script **沒套 MDT 2026 模板**(用空白 Presentation 從零畫的)。下次重做要遷移到模板基底:

```python
from pptx import Presentation
p = Presentation('MDT_2026_powerpoint_template.pptx')  # 拿模板當底
slide = p.slides.add_slide(p.slide_layouts[2])  # Title and Content 01
slide.placeholders[0].text = '標題'
slide.placeholders[1].text = '內文'
p.save('output.pptx')
```

## SOP 步驟

1. 拷貝 `build_briefing_html.py` 為 `build_<新主題>_html.py`
2. 改 `OUT` 路徑、`<title>`、所有 slide content
3. 改色票:從舊 navy → MDT 2026 accents
4. 跑 `python build_<新主題>_html.py`
5. 開 `http://localhost:8766/<新主題>.html` 驗證
6. 要 PDF / PNG → 用 frontend-slides skill 的 `scripts/export-pdf.sh`(在 `~/.claude/skills/frontend-slides/scripts/`)
7. 要部署到雲端 → `scripts/deploy.sh`(Vercel)

## 既有 HTML 簡報(已統一到 MDT 2026)

集中於 [`../../websiteview/`](../../websiteview/),共用 `css/shared.css`:

- `../../websiteview/portal-briefing.html`(中文 25 張)
- `../../websiteview/portal-architecture.html`(英文 55 張)
- `../../websiteview/case-hub.html`(3-tab dashboard)
- `../../websiteview/knowledge.html`(由 `knowledge/_build_index.py` 產生)
- `../../websiteview/index.html` landing 頁

→ 改配色 / 字型只動 `websiteview/css/shared.css`,4 個 HTML 同步生效。
