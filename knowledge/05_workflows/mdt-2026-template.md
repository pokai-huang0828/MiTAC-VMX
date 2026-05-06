# MDT 2026 PowerPoint Template SOP

> 路徑:`../../MDT_2026_powerpoint_template.pptx`(5.96 MB)
> 2026-05-05 起所有報告基底

## 規格

- 尺寸:**16:9**(13.33 × 7.50 inch)
- 字型:**Calibri Light**(major)/ **Calibri**(minor)/ 新細明體(TC)
- 6 layouts(內含 sample slide,可刪)

## 6 個 Layout

| idx | 名稱 | 用途 | 主要 placeholder |
|-----|------|------|------------------|
| 0 | **Title Slide** | 封面 | Title(2 行 OK)/ Subtitle |
| 1 | **Breakpage** | 章節分隔 | Title + 多層 bullet |
| 2 | **Title and Content 01** | 純文字內頁 | Header + bullet 內文 |
| 3 | **Title and Content 02** | 內頁 + 物件 | Page Title + 段落 |
| 4 | **Title and Content 03** | 滿版物件 | 整片內容區 |
| 5 | **Thank You Slide** | 結尾 | (純視覺) |

## 色票(theme accents)

| 名稱 | 色碼 | 用途 |
|------|------|------|
| accent1 | `#5B9BD5` | 主藍 |
| accent5 | `#4472C4` | 深藍 |
| accent2 | `#ED7D31` | 橘(強調 / CTA) |
| accent3 | `#A5A5A5` | 灰 |
| accent4 | `#FFC000` | 金 |
| accent6 | `#70AD47` | 綠 |

## python-pptx 拷模板程式

```python
from pptx import Presentation

# 拿模板當底
p = Presentation('MDT_2026_powerpoint_template.pptx')

# (選擇)模板已有 6 張 sample slide,可全部刪掉
xml_slides = p.slides._sldIdLst
slides = list(xml_slides)
for slide in slides:
    xml_slides.remove(slide)

# 加新 slide(用 layout 0 = Title Slide)
slide = p.slides.add_slide(p.slide_layouts[0])
slide.placeholders[0].text = '我的主題'
slide.placeholders[1].text = '副標題'

# 加內頁(layout 2 = Title and Content 01)
slide = p.slides.add_slide(p.slide_layouts[2])
slide.placeholders[0].text = '章節標題'
slide.placeholders[1].text = '內文 bullet 1\n內文 bullet 2'

p.save('output.pptx')
```

## 直接手動編輯 SOP

1. 拷貝 `MDT_2026_powerpoint_template.pptx` 改名(例:`Q2-Review.pptx`)
2. PowerPoint 開啟
3. 刪掉 6 張 sample slide
4. **新增投影片時選對應 layout**(右鍵 → 新增投影片 → 選 layout)
5. 文字內容直接編輯 placeholder,**不要動字型 / 顏色**(讓 theme 跑)
6. 儲存

## 何時用 .pptx vs HTML

| 用途 | .pptx | HTML |
|------|-------|------|
| 給主管看 / 內部會議 | ✅(熟悉) | △ |
| 客戶現場 demo | △ | ✅(更專業) |
| 海外客戶 | △ | ✅(連結即看) |
| 內部知識整理 | △ | ✅ |
| 含複雜動畫 | ❌ | ✅ |
| 需要列印 | ✅ | △(要 export PDF) |
