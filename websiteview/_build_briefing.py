"""
Generate websiteview/portal-briefing.html (43-slide image-first deck).

Source of truth for slide content. Re-run after editing data dicts:
    python websiteview/_build_briefing.py
"""
from pathlib import Path
import io
import sys

# Make sibling _slide_deck_lib importable when invoked as a script
sys.path.insert(0, str(Path(__file__).parent))
from _slide_deck_lib import (
    LABELS_ZH,
    head_block,
    trailing_block,
    page_detail_slide,
)

OUT = Path(__file__).parent / "portal-briefing.html"

# ── Master Portal pages (7) ────────────────────────────────────────────
MASTER = [
    ("Dashboard",          "Master-Dashboard.png",
     "你管轄所有設備的即時總覽",
     "看到哪幾類問題在發生 → 分派人去處理",
     "設備總數 / 已派發 vs 未派發比例 / 健康 vs 異常 / 5 種異常分類"),
    ("Analysis",           "Master-Analysis.png",
     "期間設備分配 + 訂閱方案演變圖",
     "看哪些方案賣得好 / 哪些車隊在升降級",
     "過去一週(可調)的方案數量折線圖"),
    ("Inventory",          "Master-Inventory.png",
     "設備池(待分配 vs 已分配)",
     "把新進貨設備派給客戶,或把退回設備重派",
     "設備清單 + IMEI / 機型 / 召回紀錄 / 連線時間"),
    ("Diagnostics",        "Master-Diagnostics.png",
     "跨車隊設備健康檢查",
     "鎖定異常設備,通知對應客戶或派 FAE",
     "✓ 沒問題 / ⚠ 有問題 兩個數字 + 異常設備清單"),
    ("Fleets",             "Master-Fleets.png",
     "你管轄的所有車隊清單",
     "新建車隊 / 加帳號 / 調整車隊資訊",
     "車隊名 / 帳號數 / 設備數 / 創建日期"),
    ("User Account",       "Master-UserAccount.png",
     "管理可登入 Master Portal 的人(經銷商員工)",
     "加新員工 / 停用離職員工 / 調權限(Admin / Viewer)",
     "用戶名 / Email / 角色 / 啟用狀態"),
    ("User Activity Logs", "Master-UserActivityLogs.png",
     "Master 層級登入登出稽核",
     "查可疑登入 / 跨組織存取",
     "時間 / 用戶 / Email / 動作 / IP"),
]

# ── Fleet Portal pages (19, in operational grouping order) ─────────────
FLEET = [
    ("Map Overview",          "Fleet-MapOverview.png",
     "即時車隊位置地圖",
     "看哪些車正在路上 / 偏離預定路線",
     "世界地圖 + 設備 pin + 左側設備清單(可搜尋)"),
    ("Dashboard",             "Fleet-Dashboard-I.png",
     "車隊一日總覽",
     "當日事件多不多?有沒有要立刻關注的駕駛?",
     "Live Trips / Finished Trips / Unknown Drivers + 事件趨勢 + 駕駛安全評分排名"),
    ("Trip List",             "Fleet-TripList.png",
     "所有行程清單(預設過去 30 天)",
     "篩出特定車或駕駛的行程查證",
     "每筆 trip 的時間 / 里程 / 駕駛 / 設備"),
    ("Trip Detail",           None,
     "單筆行程的完整 timeline",
     "查這趟有沒有違規 / 異常事件",
     "GPS 軌跡地圖 + 事件時間軸 + 調閱影片按鈕"),
    ("Trip Report",           "Fleet-TripReport.png",
     "期間行程量化報表",
     "衡量車隊整體活動量是否正常",
     "Trip 數 / 總里程 / 總時長 + 趨勢圖 + 駕駛排名"),
    ("Events 卡片牆",         "Fleet-Safety-Events.png",
     "當日所有事件卡片牆",
     "快速掃過今天有什麼狀況",
     "事件按類型分組(急煞 / 超速 / 跟車過近 等)+ 影片縮圖 + 影片保留剩餘天數"),
    ("Event Detail",          None,
     "單一事件深入分析",
     "這事件要不要記過?要不要做駕駛訓練?要不要丟棄?",
     "雙鏡頭影片 + 事件位置地圖 + 速度時間圖 + 加速度時間圖"),
    ("File Retrieval",        "Fleet-Safety-FIleRetrieval.png",
     "管理已調閱的影片檔案",
     "下載 / 整理事故證據",
     "已調閱影片清單"),
    ("Safety Reports",        "Fleet-Safety-SafetyReport.png",
     "車隊安全月報 / 期間報表",
     "看趨勢有沒有改善,跟主管 / 保險彙報",
     "駕駛 / 車輛 / 事件分類 排名與趨勢"),
    ("Coaching",              None,
     "駕駛訓練教材庫",
     "挑選有教育意義的事件,跟司機坐下來檢討",
     "被標記為「教材」的事件清單(從 Event Detail 標記過來)"),
    ("Devices",               "Fleet-Management-Devices.png",
     "車隊內所有 K-series 設備清單",
     "看哪台設備需要 FAE 介入(ADAS / DMS Health)",
     "設備 ID / 機型 / 上線狀態 / 韌體版本 / AI 健康度"),
    ("Drivers",               "Fleet-Management-Drivers.png",
     "車隊駕駛員清單(綁 RFID 卡)",
     "加新司機 / 停用離職司機 / 看哪位司機開哪些車",
     "司機名 / 員工編號 / IC 卡序號 / Email"),
    ("Vehicles",              "Fleet-Management-Vehicles.png",
     "車輛資料(綁設備)",
     "確認車牌 / 車型 / 設備配對",
     "VIN / 車型 / 對應的設備 ID"),
    ("Geofences",             "Fleet-Management-Geofences.png",
     "地理圍欄設定",
     "設定哪些區域進入 / 離開要警示",
     "已建圍欄清單 + 地圖"),
    ("Configurations",        "Fleet-Configurations-DeviceSetting.png",
     "車隊全域設備行為調整",
     "依車型(轎車 / 中型 / 重型)調觸發門檻、音量、語音、超速安全分數",
     "5 個 tab — Device Settings / Sensor Event / AI Event / Road Safety / Safety Score"),
    ("Accounts &amp; Permissions", "Fleet-AccountsPermissions.png",
     "Fleet Portal 帳號管理",
     "加管理員 / 設角色權限",
     "帳號清單 + 角色 + 啟用狀態"),
    ("Fleets",                "Fleet-Fleets.png",
     "車隊本身的資料(logo / 時區 / 地址 / 電話)+ Contract Fleets",
     "更改車隊基本資料",
     "Fleet 資訊表單"),
    ("Device Usage",          "Fleet-DeviceUsage.png",
     "設備使用率",
     "看哪些設備閒置該回收 / 重派",
     "每台設備使用紀錄"),
    ("User Activity Logs",    "Fleet-UserActivityLogs.png",
     "Fleet 內帳號操作稽核",
     "查可疑操作 / 違規授權",
     "操作時間 / 用戶 / 動作"),
]

TOTAL = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + len(MASTER) + 1 + 1 + len(FLEET) + 1 + 3 + 1 + 1
# Should equal 43

# ── Slide rendering helpers ────────────────────────────────────────────

NO_SHOT_TEXT = "此頁尚未截圖<br>請參考 live portal"


# ── Build ──────────────────────────────────────────────────────────────

def build():
    total = TOTAL  # 43
    parts = []
    page = 0

    parts.append(head_block(
        title="VMX Portal · 客戶簡介手冊",
        lang="zh-Hant",
        css_file="portal-briefing.css",
    ))

    # 1. Cover
    page += 1
    parts.append(
        '<section class="slide cover">\n'
        '  <div class="slide-content">\n'
        '    <div class="eyebrow reveal">客戶簡介手冊 · CLIENT BRIEFING</div>\n'
        '    <h1 class="cover-title reveal">VMX Portal</h1>\n'
        '    <div class="cover-rule reveal"></div>\n'
        '    <div class="cover-subtitle reveal">Master vs Fleet · 一頁一頁看懂</div>\n'
        '    <p class="cover-tag reveal">給三類客戶看 — 車隊老闆 / IT 經理 / 司機主管。每個 portal 頁面獨立 1 張 slide,看到畫面 + 知道做什麼。</p>\n'
        '  </div>\n'
        '  <div class="copyright">Copyright © MiTAC Digital Technology Corp.</div>\n'
        '  <div class="mitac-logo">\n'
        '    <div class="brand">MiTAC</div>\n'
        '    <div class="tag">DIGITAL TECHNOLOGY CORP.</div>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 2. Outline
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">簡介手冊 · 大綱</div>\n'
        '    <div class="breadcrumb">OUTLINE<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <ul class="outline-list reveal">\n'
        '      <li class="navy"><strong>Part 1 · 一張圖看懂兩個 Portal</strong> — 15 秒對焦差異</li>\n'
        '      <li class="orange"><strong>Part 2 · 客戶最常問的 5 個決策</strong> — 開場必答 5 題</li>\n'
        '      <li class="red"><strong>Part 3 · Master Portal 7 頁逐頁</strong> — 每頁 1 張 slide</li>\n'
        '      <li class="gold"><strong>Part 4 · Fleet Portal 19 頁逐頁</strong> — 每頁 1 張 slide</li>\n'
        '      <li class="light"><strong>Part 5 · 三大 Demo 流程</strong> — 各 5 分鐘 · 給三類客戶</li>\n'
        '      <li class="orange"><strong>速查表</strong> — 客戶想做某事 → 看哪頁</li>\n'
        '    </ul>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span class="page-num">{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 3. Part 1 divider
    page += 1
    parts.append(
        '<section class="slide section-divider">\n'
        '  <div class="slide-content">\n'
        '    <div class="part-tag reveal">PART 1</div>\n'
        '    <h2 class="section-title reveal">一張圖看懂<br>兩個 Portal</h2>\n'
        '    <div class="rule reveal"></div>\n'
        '    <p class="section-desc reveal">Master 像「車隊總代理」的後台。Fleet 像「車隊老闆」的後台。</p>\n'
        '  </div>\n'
        '  <div class="copyright">Copyright © MiTAC Digital Technology Corp.</div>\n'
        '</section>\n\n'
    )

    # 4. Master vs Fleet compare
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">Master vs Fleet</div>\n'
        '    <div class="breadcrumb">PART 1 · 對照<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="compare-2 reveal">\n'
        '      <div class="compare-card">\n'
        '        <div class="role-name">Master Portal</div>\n'
        '        <div class="url">portal.visionmaxfleet.com</div>\n'
        '        <div class="label">給誰用</div>\n'
        '        <div class="info">經銷商 / 神達內部 / 跨車隊 IT</div>\n'
        '        <div class="label">管的範圍</div>\n'
        '        <div class="info">跨多個車隊 · 整個設備池(待分配 + 已分配)</div>\n'
        '        <div class="label">主要動作</div>\n'
        '        <div class="info">把新設備派給客戶 · 跨車隊看設備健康 · 調整客戶帳號權限 · 跨車隊用戶活動稽核</div>\n'
        '      </div>\n'
        '      <div class="compare-card fleet">\n'
        '        <div class="role-name">Fleet Portal</div>\n'
        '        <div class="url">www.visionmaxfleet.com</div>\n'
        '        <div class="label">給誰用</div>\n'
        '        <div class="info">車隊管理者 / 主管 / 司機調度</div>\n'
        '        <div class="label">管的範圍</div>\n'
        '        <div class="info">單一車隊內 · 你的車、駕駛、行程、事件</div>\n'
        '        <div class="label">主要動作</div>\n'
        '        <div class="info">看每天行程 · 查交通違規 / 駕駛行為事件 · 調閱事故影片 · 修改車型 / 觸發門檻參數</div>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="callout red spaced reveal">\n'
        '      <strong>Master 是「向上派發」的後台</strong>;<strong>Fleet 是「向下運營」的後台</strong>。Master 把設備分配下去,Fleet 把設備跑出來的數據撈起來看。\n'
        '    </div>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span class="page-num">{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 5. Part 2 divider
    page += 1
    parts.append(
        '<section class="slide section-divider">\n'
        '  <div class="slide-content">\n'
        '    <div class="part-tag reveal">PART 2</div>\n'
        '    <h2 class="section-title reveal">客戶最常問的<br>5 個決策</h2>\n'
        '    <div class="rule reveal"></div>\n'
        '    <p class="section-desc reveal">Presentation 中,這 5 題會在前 5 分鐘冒出來。先把答案準備好。</p>\n'
        '  </div>\n'
        '  <div class="copyright">Copyright © MiTAC Digital Technology Corp.</div>\n'
        '</section>\n\n'
    )

    # 6. Q1·Q2
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">Q1 · Q2 — 哪個 portal,看到什麼</div>\n'
        '    <div class="breadcrumb">PART 2 · FAQ<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="callout reveal">\n'
        '      <strong>Q1 · 我用哪個 portal?</strong>(依角色)\n'
        '      <table class="callout-table">\n'
        '        <tr><td class="col-mid"><strong>經銷商 / 神達內部</strong></td><td class="cell-navy">Master Portal — 看到所有客戶的設備池</td></tr>\n'
        '        <tr><td><strong>車隊老闆 / 司機主管</strong></td><td class="cell-orange">Fleet Portal — 只看到自己車隊</td></tr>\n'
        '        <tr><td><strong>同時管多個車隊的 IT</strong></td><td class="cell-text">兩個都要 — Master 派發、Fleet 運營</td></tr>\n'
        '      </table>\n'
        '    </div>\n'
        '    <div class="callout orange reveal">\n'
        '      <strong>Q2 · 我能看到什麼?</strong>\n'
        '      <ul class="callout-bullets">\n'
        '        <li><strong>行程(Trip)</strong>:每台車每天的開車紀錄(時間、里程、軌跡、駕駛是誰)</li>\n'
        '        <li><strong>事件(Event)</strong>:5 種類型 — 急煞、跟車過近、超速、ADAS 校正、DMS 校正</li>\n'
        '        <li><strong>影片</strong>:事件當下前向 + 駕駛艙雙鏡頭片段</li>\n'
        '        <li><strong>報表</strong>:駕駛安全評分、車隊每日活動量、設備健康度</li>\n'
        '      </ul>\n'
        '    </div>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span class="page-num">{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 7. Q3·Q5
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">Q3 · Q5 — 匯出保留 / 設備問題</div>\n'
        '    <div class="breadcrumb">PART 2 · FAQ<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="callout gold reveal">\n'
        '      <strong>Q3 · 資料能匯出嗎?保留多久?</strong>\n'
        '      <ul class="callout-bullets">\n'
        '        <li><strong>Trip / Event 清單</strong>:可匯出 CSV,日期範圍可選</li>\n'
        '        <li><strong>影片</strong>:保留 <strong class="red">180 天</strong>,過期自動刪(每筆事件頁顯示倒數)</li>\n'
        '        <li>想延長保留期 → 找你的服務窗口談</li>\n'
        '      </ul>\n'
        '    </div>\n'
        '    <div class="callout red reveal">\n'
        '      <strong>Q5 · 設備出問題我從哪裡看?</strong>\n'
        '      <table class="callout-table">\n'
        '        <tr><td class="col-narrow"><strong>經銷商</strong></td><td><strong class="cell-navy">Master Portal → Diagnostics</strong> — 看跨車隊哪幾台有問題</td></tr>\n'
        '        <tr><td><strong>車隊客戶</strong></td><td><strong class="cell-orange">Fleet Portal → Devices</strong> — 看自己車隊各台 ADAS / DMS 健康</td></tr>\n'
        '      </table>\n'
        '    </div>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span class="page-num">{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 8. Q4 plans
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">Q4 · 訂閱方案我該選哪個?</div>\n'
        '    <div class="breadcrumb">PART 2 · FAQ · 4 PLANS<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="callout spaced-bot reveal">\n'
        '      4 種方案逐層解鎖 AI 能力。<strong>越上層的方案,設備能偵測的事件越多</strong>。\n'
        '    </div>\n'
        '    <div class="plan-grid reveal">\n'
        '      <div class="plan-card standard">\n'
        '        <div class="head"><div class="name">STANDARD</div></div>\n'
        '        <div class="what">急煞 / 急轉 / 撞擊偵測<br>+ GPS<br>+ 行車影片</div>\n'
        '        <div class="who">只要基本行為紀錄 + 事故佐證</div>\n'
        '      </div>\n'
        '      <div class="plan-card advanced">\n'
        '        <div class="head"><div class="name">ADVANCED</div></div>\n'
        '        <div class="what">Standard +<br><strong>車外輔助</strong>:前車碰撞 FCW、車道偏離 LDW、跟車過近</div>\n'
        '        <div class="who">想做駕駛訓練 + 防車外事故</div>\n'
        '      </div>\n'
        '      <div class="plan-card pro">\n'
        '        <div class="head"><div class="name">PRO</div></div>\n'
        '        <div class="what">Advanced +<br><strong>駕駛艙監控</strong>:分心、打電話、滑手機、疲勞、安全帶</div>\n'
        '        <div class="who">要全方位駕駛行為管理</div>\n'
        '      </div>\n'
        '      <div class="plan-card suspend">\n'
        '        <div class="head"><div class="name">SUSPEND</div></div>\n'
        '        <div class="what">暫停服務<br>不收費<br>設備保留</div>\n'
        '        <div class="who">季節性不開的車輛 / 暫停車輛</div>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="pricing-footnote reveal">詳細定價請洽你的業務窗口</div>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span class="page-num">{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 9. Part 3 divider
    page += 1
    parts.append(
        '<section class="slide section-divider">\n'
        '  <div class="slide-content">\n'
        '    <div class="part-tag reveal">PART 3</div>\n'
        '    <h2 class="section-title reveal">Master Portal<br>7 頁逐頁</h2>\n'
        '    <div class="rule reveal"></div>\n'
        '    <p class="section-desc reveal">經銷商 / 神達內部用 — 每頁 1 張 slide,看到畫面 + 知道做什麼。</p>\n'
        '  </div>\n'
        '  <div class="copyright">Copyright © MiTAC Digital Technology Corp.</div>\n'
        '</section>\n\n'
    )

    # 10–16. Master pages
    for i, (name, image, purpose, decide, see) in enumerate(MASTER, start=1):
        page += 1
        parts.append(page_detail_slide(
            side="master",
            idx=i,
            total_in_section=len(MASTER),
            total_pages=total,
            page_num=page,
            name=name, image=image,
            purpose=purpose, decide=decide, see=see,
            section_label=f"PART 3 · {i}/{len(MASTER)} MASTER",
            labels=LABELS_ZH,
            no_shot_text=NO_SHOT_TEXT,
        ))

    # 17. Part 4 divider
    page += 1
    parts.append(
        '<section class="slide section-divider">\n'
        '  <div class="slide-content">\n'
        '    <div class="part-tag reveal">PART 4</div>\n'
        '    <h2 class="section-title reveal">Fleet Portal<br>19 頁逐頁</h2>\n'
        '    <div class="rule reveal"></div>\n'
        '    <p class="section-desc reveal">車隊運營者用 — 每頁 1 張 slide,加上開頭一張 6 大功能群組地圖。</p>\n'
        '  </div>\n'
        '  <div class="copyright">Copyright © MiTAC Digital Technology Corp.</div>\n'
        '</section>\n\n'
    )

    # 18. Fleet 6 groups overview
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">Fleet Portal — 6 大功能群組</div>\n'
        '    <div class="breadcrumb">PART 4 · 概覽<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="group-grid reveal">\n'
        '      <div class="group-card orange">\n'
        '        <div class="head"><div class="count">2</div><div class="name">每天看</div></div>\n'
        '        <div class="pages-list">Map Overview · Dashboard</div>\n'
        '      </div>\n'
        '      <div class="group-card light">\n'
        '        <div class="head"><div class="count">3</div><div class="name">Trip 管理</div></div>\n'
        '        <div class="pages-list">Trip List · Trip Detail · Trip Report</div>\n'
        '      </div>\n'
        '      <div class="group-card red">\n'
        '        <div class="head"><div class="count">5</div><div class="name">事件 / 客訴</div></div>\n'
        '        <div class="pages-list">Events · Event Detail · File Retrieval · Safety Reports · Coaching</div>\n'
        '      </div>\n'
        '      <div class="group-card gold">\n'
        '        <div class="head"><div class="count">4</div><div class="name">設備 / 駕駛</div></div>\n'
        '        <div class="pages-list">Devices · Drivers · Vehicles · Geofences</div>\n'
        '      </div>\n'
        '      <div class="group-card">\n'
        '        <div class="head"><div class="count">1</div><div class="name">設定</div></div>\n'
        '        <div class="pages-list">Configurations(5 設定 tab)</div>\n'
        '      </div>\n'
        '      <div class="group-card gray">\n'
        '        <div class="head"><div class="count">4</div><div class="name">行政</div></div>\n'
        '        <div class="pages-list">A&amp;P · Fleets · Device Usage · User Activity Logs</div>\n'
        '      </div>\n'
        '    </div>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span class="page-num">{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 19–37. Fleet pages
    for i, (name, image, purpose, decide, see) in enumerate(FLEET, start=1):
        page += 1
        parts.append(page_detail_slide(
            side="fleet",
            idx=i,
            total_in_section=len(FLEET),
            total_pages=total,
            page_num=page,
            name=name, image=image,
            purpose=purpose, decide=decide, see=see,
            section_label=f"PART 4 · {i}/{len(FLEET)} FLEET",
            labels=LABELS_ZH,
            no_shot_text=NO_SHOT_TEXT,
        ))

    # 38. Part 5 divider
    page += 1
    parts.append(
        '<section class="slide section-divider">\n'
        '  <div class="slide-content">\n'
        '    <div class="part-tag reveal">PART 5</div>\n'
        '    <h2 class="section-title reveal">三大 Demo 流程<br>各 5 分鐘</h2>\n'
        '    <div class="rule reveal"></div>\n'
        '    <p class="section-desc reveal">客戶坐下來,你 5 分鐘走完一套。三類客戶各有自己的路徑、節奏、收尾問題。</p>\n'
        '  </div>\n'
        '  <div class="copyright">Copyright © MiTAC Digital Technology Corp.</div>\n'
        '</section>\n\n'
    )

    def demo_slide(title: str, breadcrumb: str, klass: str, hook_html: str,
                    steps: list[tuple[str, str, str]], close_text: str,
                    pnum: int) -> str:
        steps_html = "\n".join(
            f'    <div class="demo-step reveal">\n'
            f'      <div class="num">{n}</div>\n'
            f'      <div>\n'
            f'        <div class="step-name">{step}</div>\n'
            f'        <div class="step-desc">{desc}</div>\n'
            f'      </div>\n'
            f'      <div class="step-time">{t}</div>\n'
            f'    </div>'
            for n, (step, desc, t) in enumerate(steps, start=1)
        )
        return (
            f'<section class="slide inner">\n'
            f'  <header class="title-bar">\n'
            f'    <div class="title-text">{title}</div>\n'
            f'    <div class="breadcrumb">{breadcrumb}<span class="breadcrumb-dot">●</span></div>\n'
            f'  </header>\n'
            f'  <div class="body">\n'
            f'    <div class="demo-flow {klass}">\n'
            f'      {hook_html}\n'
            f'      <div class="demo-steps">\n'
            f'{steps_html}\n'
            f'      </div>\n'
            f'      <div class="demo-close reveal">\n'
            f'        <span class="close-label">CLOSE WITH</span>\n'
            f'        {close_text}\n'
            f'      </div>\n'
            f'    </div>\n'
            f'  </div>\n'
            f'  <div class="footer">\n'
            f'    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
            f'    <span class="page-num">{pnum} / {total}</span>\n'
            f'  </div>\n'
            f'</section>\n\n'
        )

    # 39. Demo A
    page += 1
    parts.append(demo_slide(
        title="Demo A · 給「車隊老闆」",
        breadcrumb="PART 5 · ROI · RISK",
        klass="owner",
        hook_html='<div class="demo-hook reveal"><span class="hook-label">30-SEC HOOK</span>你最在意 — <strong>車隊有沒有出事 / 司機表現好不好 / 保險有沒有依據</strong></div>',
        steps=[
            ("Dashboard", "你的車隊一目了然", "15 秒"),
            ("Trip Report", "本月跑了多少 / 總里程 / 趨勢", "60 秒"),
            ("Safety Reports", "哪幾個司機需要訓練 / 風險最高的車", "90 秒"),
            ("Event Detail(隨選一筆)", "點進去看雙鏡頭影片 + 速度圖,證明這真的有發生", "90 秒"),
            ("Coaching", "把這事件加進訓練教材,跟司機溝通", "45 秒"),
        ],
        close_text='&quot;你想先看看哪個司機 / 哪個事件?&quot;',
        pnum=page,
    ))

    # 40. Demo B
    page += 1
    parts.append(demo_slide(
        title="Demo B · 給「IT 經理」",
        breadcrumb="PART 5 · CONTROL · INTEGRATION",
        klass="it",
        hook_html='<div class="demo-hook gold reveal"><span class="hook-label">30-SEC HOOK</span>你關心 — <strong>設備健康 / 帳號權限 / 資料能匯出 / 對接系統</strong></div>',
        steps=[
            ("Devices", "看到所有車的設備健康度 + 韌體版本", "60 秒"),
            ("Configurations", "改車型門檻、音量、語音 → 全 fleet 套用", "90 秒"),
            ("Accounts &amp; Permissions", "加管理員、設權限,SSO 等可談", "60 秒"),
            ("User Activity Logs", "稽核紀錄,合規好交差", "45 秒"),
            ("Geofences", "圍欄,可以對接你們現有 ERP", "45 秒"),
        ],
        close_text='&quot;你的內部系統有什麼想對接的?(API / Webhook / Custom SDK)&quot;',
        pnum=page,
    ))

    # 41. Demo C
    page += 1
    parts.append(demo_slide(
        title="Demo C · 給「司機主管」",
        breadcrumb="PART 5 · BEHAVIOR · COACHING",
        klass="driver",
        hook_html='<div class="demo-hook reveal"><span class="hook-label">30-SEC HOOK</span>你關心 — <strong>司機怎麼開 / 事故有沒有影片佐證 / 能不能拿來教育</strong></div>',
        steps=[
            ("Map Overview", "即時看到每台車在哪", "30 秒"),
            ("Trip List → 點某筆", "看單一行程細節 + 軌跡 + 事件 timeline", "90 秒"),
            ("Events 卡片牆", "今天 / 本週發生的事件分類", "60 秒"),
            ("Event Detail", "點進去看 7 種駕駛艙偵測標籤(打電話 / 滑手機 / 安全帶 / 抽菸 等)", "90 秒"),
            ("Coaching", "把事件變教材,做訓練紀錄", "60 秒"),
        ],
        close_text='&quot;你目前怎麼跟司機檢討事故?可以省下你這部分時間。&quot;',
        pnum=page,
    ))

    # 42. Quick reference table
    page += 1
    qref_rows = [
        ("看今天車隊狀態", "fleet", "Fleet", "Dashboard"),
        ("找特定司機的行程", "fleet", "Fleet", "Trips &gt; Trip List(搜尋)"),
        ("調某個事故影片", "fleet", "Fleet", "Trip Detail / Event Detail"),
        ("看誰開太快", "fleet", "Fleet", "Safety &gt; Events(篩 Speed Sign Violation)"),
        ("訓練問題司機", "fleet", "Fleet", "Safety &gt; Coaching"),
        ("改車隊觸發門檻", "fleet", "Fleet", "Configurations"),
        ("加新司機", "fleet", "Fleet", "Management &gt; Drivers"),
        ("加管理員帳號", "fleet", "Fleet", "Administration &gt; A&amp;P"),
        ("派發新設備給客戶", "master", "Master", "Management &gt; Inventory"),
        ("看跨車隊有幾台壞了", "master", "Master", "Management &gt; Diagnostics"),
        ("加新車隊客戶", "master", "Master", "Management &gt; Fleets"),
        ("看哪些經銷商員工進來看了", "master", "Master", "User Activity Logs"),
    ]
    rows_html = "\n".join(
        f'        <tr><td>{want}</td><td><span class="portal-tag {tag}">{tag_label}</span></td><td>{where}</td></tr>'
        for (want, tag, tag_label, where) in qref_rows
    )
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">速查 — 客戶想做某事 → 看哪頁</div>\n'
        '    <div class="breadcrumb">QUICK REFERENCE<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <table class="qref reveal">\n'
        '      <thead>\n'
        '        <tr><th>客戶想做什麼</th><th class="portal-col">Portal</th><th>看哪一頁</th></tr>\n'
        '      </thead>\n'
        '      <tbody>\n'
        f'{rows_html}\n'
        '      </tbody>\n'
        '    </table>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span class="page-num">{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 43. End slide
    page += 1
    parts.append(
        '<section class="slide end-slide">\n'
        '  <div class="slide-content end-content">\n'
        '    <div class="part-tag fin reveal">FIN</div>\n'
        '    <div class="end-text reveal">謝謝</div>\n'
        '    <div class="end-rule reveal"></div>\n'
        '    <div class="end-tag reveal">想看哪個 demo flow?車隊老闆 / IT 經理 / 司機主管 — 5 分鐘各一場。</div>\n'
        '  </div>\n'
        '  <div class="copyright">Copyright © MiTAC Digital Technology Corp.</div>\n'
        '  <div class="mitac-logo">\n'
        '    <div class="brand">MiTAC</div>\n'
        '    <div class="tag">DIGITAL TECHNOLOGY CORP.</div>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # ── Trailing scripts (slide nav + lightbox) — shared lib
    parts.append(trailing_block())


    out = "".join(parts)
    with io.open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write(out)
    print(f"Wrote {OUT}")
    print(f"Total slides: {page} (expected {total})")


if __name__ == "__main__":
    build()
