# Claude Memory 系統使用

> Claude Code 跨 session memory 路徑:`C:\Users\pokai.huang\.claude\projects\C--Users-pokai-huang-Desktop-MiTAC-KennyHuang\memory\`

## 為什麼要記到 memory(而不是 knowledge folder)

| 屬性 | knowledge folder(這資料夾) | Claude memory |
|------|--------------------------|---------------|
| 持久度 | 跨 session / 跨工具 | 跨 session(只給 Claude 用) |
| 可分享 | ✅ 可給 Brian / Lucy | ❌ 私人 |
| 內容 | 結構化、operational | Claude 行為規則 + 校正歷史 |
| 更新 | 手動編輯 | 自然語言觸發 Claude 寫入 |

## Memory 13 條索引(2026-05-06 截止)

| 類型 | 名稱 | 用途 |
|------|------|------|
| user | user_kenny.md | Kenny 個人 profile |
| project | project_vmx.md | VMX 產品 + 利害關係人 |
| project | project_training_progress.md | 30-day onboarding 暫停狀態 |
| project | project_portal_walkthrough.md | Brian portal task + 26 頁系統地圖 |
| project | project_meeting_2026-05-06_q2_review.md | 5/6 Q2 Review 戰略洞察 |
| feedback | feedback_training_style.md | 訓練官風格 8 條 |
| feedback | feedback_vmx_facts.md | 已校正事實 + Sheet vs Jira mismatch 紀錄 |
| feedback | feedback_internal_vs_external_truth.md | 三層真相規則 |
| reference | reference_vmx_resources.md | KB / NotebookLM / Jira 等連結 |
| reference | reference_html_pipeline.md | HTML 簡報 SOP(已校正色板) |
| reference | reference_user_skills.md | ~/.claude/skills/ 4 個 |
| reference | reference_mdt_pptx_template.md | MDT 2026 模板規格 |
| reference | reference_miai_roadmap_2026.md | Tier × Chip × Model |
| reference | reference_ai_tasks_sheet_2026-05-05.md | AI sheet 結構洞察 + sync 缺口 |
| reference | reference_kenny_pm_frameworks.md | Hub 第三 tab 4 框架 |

## 何時觸發 Claude 寫 memory

- ✅ Kenny 校正 Claude 過去答錯的事實
- ✅ Kenny 給互動風格 feedback(「不要做 X」/「保持做 Y」)
- ✅ 重大專案 / 戰略決策(Brian 同步戰略 / 客戶名單變動)
- ✅ 跨 session 才會用到的 reference(KB 連結 / 帳號 / 路徑)

## 何時 NOT 寫 memory

- ❌ 一次性對話狀態
- ❌ 已經在 git history 的程式碼
- ❌ Knowledge folder 已經有的(別重複)
- ❌ 機密資料(雖然 memory 在本機,但別當保險箱用)

## 維護建議

每 2 週執行一次:
1. 跟 Claude 說「列出 memory 索引,看哪些該合併 / 刪除」
2. 看哪些 reference 已被 KB / Sheet 取代
3. 看哪些 project 已結案,可降級為 archive

## Memory 跟 Knowledge folder 的同步

當 Claude 校正 memory 時,如果該事實也應該在 knowledge folder:
- 要 Claude 同步更新 knowledge folder 對應檔案
- 例:Yawning 狀態校正 → 同時更新 `01_product-knowledge/kb-cheatsheet.md` 和 `feedback_vmx_facts.md`
