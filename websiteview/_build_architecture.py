"""
Generate websiteview/portal-architecture.html (47-slide image-first deck, English).

Source of truth for the VT-team architecture training. Re-run after edits:
    python websiteview/_build_architecture.py
"""
from pathlib import Path
import io
import sys

sys.path.insert(0, str(Path(__file__).parent))
from _slide_deck_lib import (
    LABELS_EN,
    head_block,
    trailing_block,
    page_detail_slide,
)

OUT = Path(__file__).parent / "portal-architecture.html"

NO_SHOT_TEXT = "Screenshot pending<br>refer to live portal"

# ── Master Portal pages (7) — English bullets ──────────────────────────
MASTER = [
    ("Dashboard",          "Master-Dashboard.png",
     "At-a-glance overview of every CDR you manage",
     "Spot which categories of issues are arising → dispatch the right team",
     "Total CDRs / assigned vs unassigned / healthy vs unhealthy / 5-category issue split"),
    ("Analysis",           "Master-Analysis.png",
     "Period-over-period CDR allocation + Plan Type evolution",
     "Identify which plans sell well / which fleets are upgrading or downgrading",
     "Past-week (configurable) Plan Type count line chart"),
    ("Inventory",          "Master-Inventory.png",
     "The CDR pool — unassigned vs already-assigned",
     "Push newly-received CDRs to a customer, or re-deploy returned units",
     "CDR list + IMEI / model / recall history / last-seen timestamp"),
    ("Diagnostics",        "Master-Diagnostics.png",
     "Cross-fleet device health check",
     "Lock onto unhealthy CDRs, notify the corresponding customer or dispatch FAE",
     "✓ Healthy / ⚠ Unhealthy counts + flagged CDR list"),
    ("Fleets",             "Master-Fleets.png",
     "Roster of every fleet you manage",
     "Create fleets / add accounts / adjust fleet metadata",
     "Fleet name / account count / device count / created date"),
    ("User Account",       "Master-UserAccount.png",
     "Manage who can sign into Master Portal (your own staff)",
     "Onboard new staff / disable departing staff / role tuning (Admin / Viewer)",
     "Username / Email / Role / Active status"),
    ("User Activity Logs", "Master-UserActivityLogs.png",
     "Master-tier sign-in / sign-out audit trail",
     "Investigate suspicious logins or cross-org access",
     "Timestamp / User / Email / Action / IP"),
]

# ── Fleet Portal pages (19) ────────────────────────────────────────────
FLEET = [
    ("Map Overview",          "Fleet-MapOverview.png",
     "Real-time fleet position map",
     "See which vehicles are on the road / off planned routes",
     "World map + device pins + searchable left-side device list"),
    ("Dashboard",             "Fleet-Dashboard-I.png",
     "Daily fleet overview",
     "How many events today? Any drivers needing immediate attention?",
     "Live Trips / Finished Trips / Unknown Drivers + event trends + driver safety ranking"),
    ("Trip List",             "Fleet-TripList.png",
     "Every trip (default last 30 days)",
     "Filter to a specific vehicle or driver to verify a trip",
     "Per-trip time / mileage / driver / device"),
    ("Trip Detail",           None,
     "Full timeline of a single trip",
     "Inspect for violations or anomalous events along the route",
     "GPS trajectory map + event timeline + clip-retrieval button"),
    ("Trip Report",           "Fleet-TripReport.png",
     "Period-aggregated trip metrics",
     "Gauge whether overall fleet activity is normal",
     "Trip count / total mileage / total duration + trend chart + driver ranking"),
    ("Events",                "Fleet-Safety-Events.png",
     "Today&#39;s event card wall",
     "Quick scan of what&#39;s happening across the fleet today",
     "Events grouped by type (Harsh Brake / Speed / Tailgating, etc.) + thumbnail + retention countdown"),
    ("Event Detail",          None,
     "Deep dive into a single event",
     "Discipline? Coach? Dismiss as false-positive?",
     "Dual-camera video + event location map + speed chart + acceleration chart"),
    ("File Retrieval",        "Fleet-Safety-FIleRetrieval.png",
     "Manage clips already pulled from the device",
     "Download / archive incident evidence",
     "List of retrieved video clips"),
    ("Safety Reports",        "Fleet-Safety-SafetyReport.png",
     "Fleet safety monthly / period reports",
     "Track whether the trend is improving — present to management or insurer",
     "Driver / vehicle / event-type rankings and trends"),
    ("Coaching",              None,
     "Driver training material library",
     "Pick teaching-worthy events to discuss face-to-face with drivers",
     "Events flagged &quot;for coaching&quot; (tagged from Event Detail)"),
    ("Devices",               "Fleet-Management-Devices.png",
     "Every K-series CDR in your fleet",
     "Identify devices needing FAE intervention (ADAS / DMS Health flags)",
     "Device ID / model / online status / firmware version / AI health"),
    ("Drivers",               "Fleet-Management-Drivers.png",
     "Driver roster (RFID-card linked)",
     "Onboard / disable drivers / see who drove which vehicle",
     "Driver name / employee ID / IC card serial / Email"),
    ("Vehicles",              "Fleet-Management-Vehicles.png",
     "Vehicle records (linked to a device)",
     "Confirm plate / vehicle type / device pairing",
     "VIN / vehicle type / paired device ID"),
    ("Geofences",             "Fleet-Management-Geofences.png",
     "Geographic boundary configuration",
     "Define which zones trigger entry / exit alerts",
     "Defined zone list + map"),
    ("Configurations",        "Fleet-Configurations-DeviceSetting.png",
     "Fleet-wide device behavior tuning",
     "Per vehicle type (sedan / mid / heavy) — adjust thresholds, volume, voice, score weights",
     "5 tabs — Device Settings / Sensor Event / AI Event / Road Safety / Safety Score"),
    ("Accounts &amp; Permissions", "Fleet-AccountsPermissions.png",
     "Fleet Portal account management",
     "Add admins / set role permissions",
     "Account list + role + active status"),
    ("Fleets",                "Fleet-Fleets.png",
     "Fleet metadata (logo / timezone / address / phone) + Contract Fleets",
     "Update basic fleet information",
     "Fleet info form"),
    ("Device Usage",          "Fleet-DeviceUsage.png",
     "Device utilization",
     "See which devices are idle and should be reclaimed / re-deployed",
     "Per-device usage record"),
    ("User Activity Logs",    "Fleet-UserActivityLogs.png",
     "Fleet-tier account action audit",
     "Investigate suspicious operations or unauthorized access",
     "Action timestamp / user / action"),
]

# Slide rendering uses _slide_deck_lib.page_detail_slide (shared with briefing)


# ── Build ──────────────────────────────────────────────────────────────

def build():
    # 1 cover + 1 outline + 1 P1 div + 3 hierarchy + 1 P2 div + 7 master
    # + 1 P3 div + 1 module map + 19 fleet + 1 P4 div + 2 sysarch + 1 P5 div
    # + 4 integration + 1 P6 div + 2 pricing + 1 end = 47
    total = 1+1+1+3+1+len(MASTER)+1+1+len(FLEET)+1+2+1+4+1+2+1
    parts: list[str] = []
    page = 0

    parts.append(head_block(
        title="VisionMax — Architecture &amp; Integration",
        lang="en",
        css_file="portal-architecture.css",
    ))

    # 1. Cover
    page += 1
    parts.append(
        '<section class="slide cover">\n'
        '  <div class="slide-content">\n'
        '    <div class="eyebrow reveal">VT TEAM TRAINING · INTERNAL</div>\n'
        '    <h1 class="cover-title reveal">VisionMax</h1>\n'
        '    <div class="cover-rule reveal"></div>\n'
        '    <div class="cover-subtitle reveal">Architecture &amp; Integration</div>\n'
        '    <p class="cover-tag reveal">A page-by-page walk-through of the Master &amp; Fleet portals, the end-to-end system architecture, two integration paths, and the subscription plan structure.</p>\n'
        '  </div>\n'
        '  <div class="copyright">Copyright © MiTAC Digital Technology Corp. All Rights Reserved.</div>\n'
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
        '    <div class="title-text">Outline</div>\n'
        '    <div class="breadcrumb">AGENDA<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <ul class="outline-list reveal">\n'
        '      <li class="navy"><strong>Part 1 · Master &amp; Fleet Architecture</strong> — How the two-tier portal hierarchy works</li>\n'
        '      <li class="orange"><strong>Part 2 · Master Function</strong> — 7 dealer-side pages, one per slide</li>\n'
        '      <li class="red"><strong>Part 3 · Fleet Function</strong> — 19 fleet-manager pages, one per slide</li>\n'
        '      <li class="gold"><strong>Part 4 · System Architecture</strong> — Device → Cloud → UI data flow</li>\n'
        '      <li class="navy"><strong>Part 5 · Integration Method</strong> — Server-to-Server &amp; VisionMax Elastic</li>\n'
        '      <li class="orange"><strong>Part 6 · Subscription Plans</strong> — Per-device tiers + base service tiers</li>\n'
        '    </ul>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span>{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 3. Part 1 divider
    page += 1
    parts.append(
        '<section class="slide section-divider">\n'
        '  <div class="slide-content">\n'
        '    <div class="part-tag reveal">PART 1</div>\n'
        '    <h2 class="section-title reveal">Master &amp; Fleet<br>Architecture</h2>\n'
        '    <div class="rule reveal"></div>\n'
        '    <p class="section-desc reveal">Two distinct portals — one for dealers selling fleet management services, one for fleet managers operating the fleet.</p>\n'
        '  </div>\n'
        '  <div class="copyright">Copyright © MiTAC Digital Technology Corp.</div>\n'
        '</section>\n\n'
    )

    # 4. Architecture overview
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">Architecture · Overview</div>\n'
        '    <div class="breadcrumb">PART 1 · OVERVIEW<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="callout reveal">Two distinct portal types serve two distinct audiences. The Master portal is owned by the dealer; the Fleet portal is owned by the fleet manager who runs daily operations.</div>\n'
        '    <div class="card-grid reveal mt-1">\n'
        '      <div class="fleet-card">Fleet A</div>\n'
        '      <div class="fleet-card">Fleet B</div>\n'
        '      <div class="fleet-card">Fleet C</div>\n'
        '      <div class="fleet-card">Fleet D</div>\n'
        '      <div class="fleet-card">Fleet E</div>\n'
        '    </div>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span>{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 5. MASTER role
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">Architecture · MASTER role</div>\n'
        '    <div class="breadcrumb">PART 1 · MASTER<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="callout red reveal">The <strong>Master</strong> tier is the dealer&#39;s portal — used to sell fleet management services and assign CDRs to each fleet.</div>\n'
        '    <div class="two-col reveal mt-1">\n'
        '      <div class="role-card">\n'
        '        <div class="role-label">MASTER role</div>\n'
        '        <ul class="role-bullets">\n'
        '          <li>Belongs to the dealer</li>\n'
        '          <li>Sells fleet management services</li>\n'
        '          <li>Assigns CDRs to each fleet</li>\n'
        '        </ul>\n'
        '      </div>\n'
        '      <div class="col-center"><span class="master-block">MASTER (Dealer)</span></div>\n'
        '    </div>\n'
        '    <div class="card-grid reveal mt-1">\n'
        '      <div class="fleet-card">Fleet A</div>\n'
        '      <div class="fleet-card">Fleet B</div>\n'
        '      <div class="fleet-card">Fleet C</div>\n'
        '      <div class="fleet-card">Fleet D</div>\n'
        '      <div class="fleet-card">Fleet E</div>\n'
        '    </div>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span>{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 6. FLEET role
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">Architecture · FLEET role</div>\n'
        '    <div class="breadcrumb">PART 1 · FLEET<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="callout orange reveal">The <strong>Fleet</strong> tier belongs to the fleet manager — responsible for managing the task status of each driver in the fleet.</div>\n'
        '    <div class="two-col reveal mt-1">\n'
        '      <div class="role-card fleet">\n'
        '        <div class="role-label">FLEET role</div>\n'
        '        <ul class="role-bullets">\n'
        '          <li>Belongs to the fleet manager</li>\n'
        '          <li>Manages every driver&#39;s daily task status</li>\n'
        '          <li>Reviews trips, events, and safety reports</li>\n'
        '        </ul>\n'
        '      </div>\n'
        '      <div class="col-center"><span class="fleet-block">FLEET (Manager)</span></div>\n'
        '    </div>\n'
        '    <div class="card-grid reveal mt-1">\n'
        '      <div class="fleet-card">Fleet A</div>\n'
        '      <div class="fleet-card">Fleet B</div>\n'
        '      <div class="fleet-card">Fleet C</div>\n'
        '      <div class="fleet-card">Fleet D</div>\n'
        '      <div class="fleet-card">Fleet E</div>\n'
        '    </div>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span>{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 7. Part 2 divider
    page += 1
    parts.append(
        '<section class="slide section-divider">\n'
        '  <div class="slide-content">\n'
        '    <div class="part-tag reveal">PART 2</div>\n'
        '    <h2 class="section-title reveal">Master Function<br>Introduction</h2>\n'
        '    <div class="rule reveal"></div>\n'
        '    <p class="section-desc reveal">Inside the Master portal — 7 dealer-side pages, one per slide.</p>\n'
        '  </div>\n'
        '  <div class="copyright">Copyright © MiTAC Digital Technology Corp.</div>\n'
        '</section>\n\n'
    )

    # 8–14. Master pages
    for i, (name, image, purpose, decide, see) in enumerate(MASTER, start=1):
        page += 1
        parts.append(page_detail_slide(
            side="master", idx=i, total_in_section=len(MASTER),
            total_pages=total, page_num=page,
            name=name, image=image,
            purpose=purpose, decide=decide, see=see,
            section_label=f"PART 2 · {i}/{len(MASTER)} MASTER",
            labels=LABELS_EN,
            no_shot_text=NO_SHOT_TEXT,
        ))

    # 15. Part 3 divider
    page += 1
    parts.append(
        '<section class="slide section-divider">\n'
        '  <div class="slide-content">\n'
        '    <div class="part-tag reveal">PART 3</div>\n'
        '    <h2 class="section-title reveal">Fleet Function<br>Introduction</h2>\n'
        '    <div class="rule reveal"></div>\n'
        '    <p class="section-desc reveal">Inside the Fleet portal — 19 modules, one per slide. Begins with a 12-module overview.</p>\n'
        '  </div>\n'
        '  <div class="copyright">Copyright © MiTAC Digital Technology Corp.</div>\n'
        '</section>\n\n'
    )

    # 16. Module map
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">Fleet — Module Map</div>\n'
        '    <div class="breadcrumb">PART 3 · OVERVIEW<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="callout orange reveal">Twelve interlocking modules cover the complete fleet-management lifecycle, from live monitoring to post-event coaching.</div>\n'
        '    <div class="module-grid reveal">\n'
        '      <div class="module-tile">Trips</div>\n'
        '      <div class="module-tile">Dashboard</div>\n'
        '      <div class="module-tile">Playback</div>\n'
        '      <div class="module-tile">Coaching</div>\n'
        '      <div class="module-tile">Live View</div>\n'
        '      <div class="module-tile">File Retrieval</div>\n'
        '      <div class="module-tile">Event</div>\n'
        '      <div class="module-tile">Configuration</div>\n'
        '      <div class="module-tile">Safety</div>\n'
        '      <div class="module-tile">Geo Fence</div>\n'
        '      <div class="module-tile">Health</div>\n'
        '      <div class="module-tile">Safety Report</div>\n'
        '    </div>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span>{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 17–35. Fleet pages
    for i, (name, image, purpose, decide, see) in enumerate(FLEET, start=1):
        page += 1
        parts.append(page_detail_slide(
            side="fleet", idx=i, total_in_section=len(FLEET),
            total_pages=total, page_num=page,
            name=name, image=image,
            purpose=purpose, decide=decide, see=see,
            section_label=f"PART 3 · {i}/{len(FLEET)} FLEET",
            labels=LABELS_EN,
            no_shot_text=NO_SHOT_TEXT,
        ))

    # 36. Part 4 divider
    page += 1
    parts.append(
        '<section class="slide section-divider">\n'
        '  <div class="slide-content">\n'
        '    <div class="part-tag reveal">PART 4</div>\n'
        '    <h2 class="section-title reveal">VisionMax<br>System Architecture</h2>\n'
        '    <div class="rule reveal"></div>\n'
        '    <p class="section-desc reveal">How the device, cloud, and portal UIs connect — the underlying data flow.</p>\n'
        '  </div>\n'
        '  <div class="copyright">Copyright © MiTAC Digital Technology Corp.</div>\n'
        '</section>\n\n'
    )

    # 37. End-to-end data flow
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">VisionMax System Architecture</div>\n'
        '    <div class="breadcrumb">PART 4 · DATA FLOW<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="callout reveal">End-to-end flow: every CDR streams data via WebSocket / HTTPS / MQTT to the VisionMax Server (AWS S3 backed), and the VisionMax Web UI reads it back through the API.</div>\n'
        '    <div class="diagram-flow reveal mt-1">\n'
        '      <div class="node">CDR<small>Device + Camera + GPS + G-Sensor + AI</small></div>\n'
        '      <div class="arrow"><span class="label">WebSocket · HTTPS · MQTT</span></div>\n'
        '      <div class="node gold">VisionMax Server<small>AWS S3 bucket · Cloud Storage</small></div>\n'
        '      <div class="arrow"><span class="label">API</span></div>\n'
        '      <div class="node light">VisionMax Web UI<small>Master + Fleet portals</small></div>\n'
        '    </div>\n'
        '    <div class="callout orange reveal mt-1"><strong>VisionAgent</strong> connects to the device locally via Hotspot / BLE for installation and on-site diagnostics.</div>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span>{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 38. Device Architecture
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">Device Architecture</div>\n'
        '    <div class="breadcrumb">PART 4 · DEVICE<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="callout reveal">Inside the device: a BSP system runs four cooperating apps via the MiTAC System API.</div>\n'
        '    <div class="card-grid reveal mt-1">\n'
        '      <div class="fleet-card navy">MiTAC<br>Camera App</div>\n'
        '      <div class="fleet-card red">MiTAC<br>AI App<small>DMS · ADAS</small></div>\n'
        '      <div class="fleet-card gold">MiDM</div>\n'
        '      <div class="fleet-card orange">Install /<br>OTA App</div>\n'
        '    </div>\n'
        '    <div class="callout orange reveal mt-1">Underlying layer: <strong>BSP System</strong> · <strong>MiTAC System API</strong> · sensors (Camera · G-Sensor · GPS · Watchdog · Settings · REC). Cloud companions: <strong>MiDM Cloud</strong> + <strong>VisionMax Cloud</strong>.</div>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span>{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 39. Part 5 divider
    page += 1
    parts.append(
        '<section class="slide section-divider">\n'
        '  <div class="slide-content">\n'
        '    <div class="part-tag reveal">PART 5</div>\n'
        '    <h2 class="section-title reveal">Integration<br>Method</h2>\n'
        '    <div class="rule reveal"></div>\n'
        '    <p class="section-desc reveal">Two officially supported paths for customers: Server-to-Server (API) or VisionMax Elastic.</p>\n'
        '  </div>\n'
        '  <div class="copyright">Copyright © MiTAC Digital Technology Corp.</div>\n'
        '</section>\n\n'
    )

    # 40. Path 1: Server-to-Server
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">Server to Server (API Integration)</div>\n'
        '    <div class="breadcrumb">PART 5 · PATH 1<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="callout red reveal"><strong>Path 1</strong> — MiTAC supplies the API documentation and hosts the storage. The customer builds its own API server and the entire web UI on top.</div>\n'
        '    <ul class="bullet-list reveal">\n'
        '      <li class="red">MiTAC provides the Server API integration documentation</li>\n'
        '      <li class="red">Storage is hosted at MiTAC (AWS S3)</li>\n'
        '      <li class="red">Customer implements its own API server and all expected web UI</li>\n'
        '    </ul>\n'
        '    <div class="diagram-flow cols-3 reveal mt-1">\n'
        '      <div class="node">VisionMax Server<small>AWS S3 · Hosted at MiTAC</small></div>\n'
        '      <div class="arrow"><span class="label">API</span></div>\n'
        '      <div class="node light">Customer API Server<small>+ Customer Web UI · Built &amp; hosted by customer</small></div>\n'
        '    </div>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span>{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 41. Path 2: Elastic Overview
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">VisionMax Elastic · Overview</div>\n'
        '    <div class="breadcrumb">PART 5 · PATH 2<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="callout orange reveal"><strong>Path 2</strong> — Storage hosted at the customer; MiTAC provides ready-made Master Portal and Elastic Portal modules so the customer&#39;s front-end work is dramatically smaller.</div>\n'
        '    <ul class="bullet-list reveal">\n'
        '      <li class="orange">MiTAC provides the Server API integration documentation</li>\n'
        '      <li class="orange">Storage is hosted at the customer</li>\n'
        '      <li class="orange">MiTAC provides the Master Portal</li>\n'
        '      <li class="orange">MiTAC provides the Elastic Portal (Device Info · Configuration · Health Report · Live View)</li>\n'
        '      <li class="orange">Customer implements its own API server and any UI outside the Master / Elastic portals</li>\n'
        '    </ul>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span>{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 42. Path 2: Elastic 4 modules
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">VisionMax Elastic · 4 Pre-built Modules</div>\n'
        '    <div class="breadcrumb">PART 5 · PATH 2<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="callout reveal">The four pre-built Elastic Portal modules: Device Info · Health Report · Live View · Configurations.</div>\n'
        '    <div class="card-grid reveal mt-1">\n'
        '      <div class="fleet-card navy">Device Info<small>at-a-glance device inventory</small></div>\n'
        '      <div class="fleet-card red">Health Report<small>per-device + per-fleet rollup</small></div>\n'
        '      <div class="fleet-card gold">Live View<small>real-time camera streaming</small></div>\n'
        '      <div class="fleet-card orange">Configurations<small>per-vehicle-type tuning</small></div>\n'
        '    </div>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span>{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 43. Path 2: Elastic Pros & Cons
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">VisionMax Elastic · Pros &amp; Cons</div>\n'
        '    <div class="breadcrumb">PART 5 · PATH 2<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="callout reveal">Pros &amp; cons of the VisionMax Elastic path — when does it fit, and what does the customer give up?</div>\n'
        '    <div class="two-col reveal mt-1">\n'
        '      <div class="callout pros">\n'
        '        <strong>ADVANTAGES</strong>\n'
        '        <ul class="callout-bullets">\n'
        '          <li>Reduces development time — roughly 2 to 3 months for quick integration and faster time-to-market.</li>\n'
        '          <li>Data storage stays managed and kept by the customer.</li>\n'
        '        </ul>\n'
        '      </div>\n'
        '      <div class="callout cons">\n'
        '        <strong>DISADVANTAGES</strong>\n'
        '        <ul class="callout-bullets">\n'
        '          <li>The Elastic Portal cannot be flexibly customized — only logo, domain, and background color are changeable.</li>\n'
        '        </ul>\n'
        '      </div>\n'
        '    </div>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span>{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 44. Part 6 divider
    page += 1
    parts.append(
        '<section class="slide section-divider">\n'
        '  <div class="slide-content">\n'
        '    <div class="part-tag reveal">PART 6</div>\n'
        '    <h2 class="section-title reveal">Subscription<br>Plans</h2>\n'
        '    <div class="rule reveal"></div>\n'
        '    <p class="section-desc reveal">Per-device tiers for the AI capability you enable, plus a base service plan that scales with fleet size.</p>\n'
        '  </div>\n'
        '  <div class="copyright">Copyright © MiTAC Digital Technology Corp.</div>\n'
        '</section>\n\n'
    )

    # 45. Pricing 3 cards
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">Subscription Plans (For TSP)</div>\n'
        '    <div class="breadcrumb">PART 6 · PER-DEVICE<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="callout reveal">Three per-device tiers: Standard (G-Sensor only) → Advanced (+ ADAS) → Pro (+ DMS). Pricing is USD per device per month, by camera count.</div>\n'
        '    <div class="pricing-meta reveal">Per-device, per-month · SLA: 24 months · Setup Fee US $3,200</div>\n'
        '    <div class="pricing-grid reveal">\n'
        '      <div class="pricing-card standard">\n'
        '        <div class="header"><div class="name">STANDARD</div><div class="tier">Entry</div></div>\n'
        '        <div class="features">\n'
        '          <div class="feat">Sensor Event Detection</div>\n'
        '          <div class="feat">VMX VT Cloud</div>\n'
        '          <div class="feat">GPS + Video</div>\n'
        '        </div>\n'
        '        <div class="price-row">\n'
        '          <div class="cell"><span class="price">$5</span><span class="cam">1–3 cam</span></div>\n'
        '          <div class="cell"><span class="price">$7</span><span class="cam">4–7 cam</span></div>\n'
        '        </div>\n'
        '      </div>\n'
        '      <div class="pricing-card advanced">\n'
        '        <div class="header"><div class="name">ADVANCED</div><div class="tier">Mid</div></div>\n'
        '        <div class="features">\n'
        '          <div class="feat">Sensor Event Detection</div>\n'
        '          <div class="feat">ADAS Event Detection</div>\n'
        '          <div class="feat">VMX VT Cloud</div>\n'
        '          <div class="feat">GPS + Video</div>\n'
        '        </div>\n'
        '        <div class="price-row">\n'
        '          <div class="cell"><span class="price">$7</span><span class="cam">1–3 cam</span></div>\n'
        '          <div class="cell"><span class="price">$9</span><span class="cam">4–7 cam</span></div>\n'
        '        </div>\n'
        '      </div>\n'
        '      <div class="pricing-card pro">\n'
        '        <div class="header"><div class="name">PRO</div><div class="tier">Top</div></div>\n'
        '        <div class="features">\n'
        '          <div class="feat">Sensor Event Detection</div>\n'
        '          <div class="feat">DMS Event Detection</div>\n'
        '          <div class="feat">ADAS Event Detection</div>\n'
        '          <div class="feat">VMX VT Cloud</div>\n'
        '          <div class="feat">GPS + Video</div>\n'
        '        </div>\n'
        '        <div class="price-row">\n'
        '          <div class="cell"><span class="price">$9</span><span class="cam">1–3 cam</span></div>\n'
        '          <div class="cell"><span class="price">$11</span><span class="cam">4–7 cam</span></div>\n'
        '        </div>\n'
        '      </div>\n'
        '    </div>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span>{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 46. Tier table
    page += 1
    parts.append(
        '<section class="slide inner">\n'
        '  <header class="title-bar">\n'
        '    <div class="title-text">Subscribe Base &amp; Cloud Service</div>\n'
        '    <div class="breadcrumb">PART 6 · BASE TIERS<span class="breadcrumb-dot">●</span></div>\n'
        '  </header>\n'
        '  <div class="body">\n'
        '    <div class="callout reveal">Four base tiers scale with device count and unlock progressive features — White Label, Customer Domain, Webhook/API, Custom API, Custom App, and Standalone.</div>\n'
        '    <table class="tier-table reveal">\n'
        '      <thead>\n'
        '        <tr>\n'
        '          <th class="feature-col">Feature</th>\n'
        '          <th class="starter"><div class="label">STARTER</div><div class="range">1 – 10K devices</div></th>\n'
        '          <th class="tier-pro"><div class="label">PRO</div><div class="range">10 – 30K devices</div></th>\n'
        '          <th class="business"><div class="label">BUSINESS</div><div class="range">30 – 50K devices</div></th>\n'
        '          <th class="enterprise"><div class="label">ENTERPRISE</div><div class="range">&gt; 50K devices</div></th>\n'
        '        </tr>\n'
        '      </thead>\n'
        '      <tbody>\n'
        '        <tr><td class="feature-name">File Retention</td><td>90 days</td><td>180 days</td><td>365 days</td><td>Unlimited</td></tr>\n'
        '        <tr><td class="feature-name">White Label</td><td><span class="check s">✓</span></td><td><span class="check p">✓</span></td><td><span class="check b">✓</span></td><td><span class="check e">✓</span></td></tr>\n'
        '        <tr><td class="feature-name">Customer Domain</td><td></td><td><span class="check p">✓</span></td><td><span class="check b">✓</span></td><td><span class="check e">✓</span></td></tr>\n'
        '        <tr><td class="feature-name">Webhook &amp; API Key</td><td></td><td></td><td><span class="check b">✓</span></td><td><span class="check e">✓</span></td></tr>\n'
        '        <tr><td class="feature-name">Custom API</td><td></td><td></td><td></td><td><span class="check e">✓</span></td></tr>\n'
        '        <tr><td class="feature-name">Custom App</td><td></td><td></td><td></td><td><span class="check e">✓</span></td></tr>\n'
        '        <tr><td class="feature-name">Standalone</td><td></td><td></td><td></td><td><span class="check e">✓</span></td></tr>\n'
        '      </tbody>\n'
        '    </table>\n'
        '  </div>\n'
        '  <div class="footer">\n'
        '    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span>{page} / {total}</span>\n'
        '  </div>\n'
        '</section>\n\n'
    )

    # 47. End slide
    page += 1
    parts.append(
        '<section class="slide end-slide">\n'
        '  <div class="slide-content end-content">\n'
        '    <div class="part-tag fin reveal">FIN</div>\n'
        '    <div class="end-text reveal">END.</div>\n'
        '    <div class="end-tag reveal">Questions, requests, or onboarding requests — reach out to the VT Team.</div>\n'
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
