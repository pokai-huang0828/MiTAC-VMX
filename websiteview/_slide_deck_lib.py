"""
Shared boilerplate for image-first slide-deck build scripts
(_build_briefing.py and _build_architecture.py).

Eliminates ~150 lines of duplication per script:
- HTML head + body chrome
- Trailing SlidePresentation JS + lightbox markup
- page_detail_slide() — image-first 2-column slide for Master/Fleet pages
"""
from __future__ import annotations
import html as _html


# ── Labels (i18n hook) ─────────────────────────────────────────────────
LABELS_ZH = {"purpose": "用途", "decision": "能決定", "sees": "看到"}
LABELS_EN = {"purpose": "Purpose", "decision": "Decision", "sees": "Sees"}


# ── Boilerplate strings ────────────────────────────────────────────────
def head_block(*, title: str, lang: str, css_file: str) -> str:
    """DOCTYPE + html + head + body opener + slide-deck chrome."""
    return (
        f'<!DOCTYPE html>\n'
        f'<html lang="{lang}">\n'
        f'<head>\n'
        f'  <meta charset="UTF-8">\n'
        f'  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f'  <title>{title}</title>\n'
        f'  <link rel="stylesheet" href="css/shared.css">\n'
        f'  <link rel="stylesheet" href="css/animations.css">\n'
        f'  <link rel="stylesheet" href="css/{css_file}">\n'
        f'</head>\n'
        f'<body>\n'
        f'  <div class="progress-bar"></div>\n'
        f'  <nav class="nav-dots" aria-label="Slide navigation"></nav>\n'
        f'  <div class="keyboard-hint">↑ ↓ ← → · Space · Click dots</div>\n'
        f'  <a class="web-hub-link" href="index.html" title="Back to Web Hub">← Web Hub</a>\n\n'
    )


_SLIDE_PRESENTATION_JS = '''<script>
class SlidePresentation {
  constructor() {
    this.slides = Array.from(document.querySelectorAll(".slide"));
    this.currentIdx = 0;
    if (this.slides.length > 0) this.slides[0].classList.add("visible");
    this.setupIntersectionObserver();
    this.setupKeyboardNav();
    this.setupTouchNav();
    this.setupProgressBar();
    this.setupNavDots();
  }
  setupIntersectionObserver() {
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add("visible");
          const i = this.slides.indexOf(e.target);
          if (i >= 0) {
            this.currentIdx = i;
            this.updateProgressBar();
            this.updateNavDots();
          }
        }
      });
    }, { threshold: 0.3 });
    this.slides.forEach(s => obs.observe(s));
  }
  goTo(i) {
    if (i < 0 || i >= this.slides.length) return;
    this.slides[i].scrollIntoView({ behavior: "smooth", block: "start" });
  }
  setupKeyboardNav() {
    document.addEventListener("keydown", (e) => {
      if (["ArrowDown","ArrowRight"," ","PageDown"].includes(e.key)) {
        e.preventDefault(); this.goTo(this.currentIdx + 1);
      } else if (["ArrowUp","ArrowLeft","PageUp"].includes(e.key)) {
        e.preventDefault(); this.goTo(this.currentIdx - 1);
      } else if (e.key === "Home") { e.preventDefault(); this.goTo(0); }
      else if (e.key === "End") { e.preventDefault(); this.goTo(this.slides.length - 1); }
    });
  }
  setupTouchNav() {
    let startY = 0;
    document.addEventListener("touchstart", e => { startY = e.touches[0].clientY; }, { passive: true });
    document.addEventListener("touchend", e => {
      const dy = startY - e.changedTouches[0].clientY;
      if (Math.abs(dy) > 50) this.goTo(this.currentIdx + (dy > 0 ? 1 : -1));
    }, { passive: true });
  }
  setupProgressBar() {
    this.progressBar = document.querySelector(".progress-bar");
    this.updateProgressBar();
  }
  updateProgressBar() {
    if (!this.progressBar) return;
    const pct = (this.currentIdx / Math.max(1, this.slides.length - 1)) * 100;
    this.progressBar.style.width = pct + "%";
  }
  setupNavDots() {
    const c = document.querySelector(".nav-dots");
    if (!c) return;
    c.innerHTML = "";
    this.navDotsEls = this.slides.map((_, i) => {
      const b = document.createElement("button");
      b.className = "nav-dot" + (i === 0 ? " active" : "");
      b.setAttribute("aria-label", `Go to slide ${i+1}`);
      b.addEventListener("click", () => this.goTo(i));
      c.appendChild(b);
      return b;
    });
  }
  updateNavDots() {
    if (!this.navDotsEls) return;
    this.navDotsEls.forEach((d, i) => d.classList.toggle("active", i === this.currentIdx));
  }
}
new SlidePresentation();
</script>

<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Image preview">
  <button class="lightbox-close" type="button" aria-label="Close preview" onclick="document.getElementById('lightbox').classList.remove('is-open')">×</button>
  <img alt="">
  <div class="lightbox-caption"></div>
</div>
<script src="js/lightbox.js" defer></script>

</body>
</html>
'''


def trailing_block() -> str:
    """Slide-deck navigation JS + lightbox + closing tags."""
    return _SLIDE_PRESENTATION_JS


# ── Page-detail slide (Master / Fleet per-page UI) ─────────────────────
def _alt(name: str) -> str:
    """Strip HTML entities from a name for use in alt= attribute."""
    return _html.unescape(name.replace("&amp;", "&"))


def page_detail_slide(*, side: str, idx: int, total_in_section: int,
                       total_pages: int, page_num: int,
                       name: str, image: str | None,
                       purpose: str, decide: str, see: str,
                       section_label: str,
                       labels: dict,
                       no_shot_text: str) -> str:
    """Image-first 2-column per-page slide.
    side: 'master' | 'fleet'
    image: filename inside VMX_images/{Master|Fleet}/, or None for placeholder
    labels: dict with 'purpose' / 'decision' / 'sees' keys (i18n)
    no_shot_text: HTML shown in the placeholder when image is None
    """
    badge_label = "MASTER" if side == "master" else "FLEET"
    if image:
        sub = "Master" if side == "master" else "Fleet"
        alt = _alt(name)
        img_block = (
            f'      <div class="page-detail-image">\n'
            f'        <img src="../VMX_images/{sub}/{image}" alt="{badge_label} Portal — {alt}">\n'
            f'      </div>\n'
        )
    else:
        img_block = (
            f'      <div class="page-detail-image no-shot">\n'
            f'        {no_shot_text}\n'
            f'      </div>\n'
        )
    return (
        f'<section class="slide inner">\n'
        f'  <header class="title-bar">\n'
        f'    <div class="title-text">{badge_label} Portal · {name}</div>\n'
        f'    <div class="breadcrumb">{section_label}<span class="breadcrumb-dot">●</span></div>\n'
        f'  </header>\n'
        f'  <div class="body">\n'
        f'    <div class="page-detail {side} reveal">\n'
        f'{img_block}'
        f'      <div class="page-detail-info">\n'
        f'        <div class="page-num-badge">{badge_label} · {idx:02d} / {total_in_section:02d}</div>\n'
        f'        <h2 class="page-title">{name}</h2>\n'
        f'        <div class="page-rule"></div>\n'
        f'        <div class="meta-block">\n'
        f'          <div class="meta-label">{labels["purpose"]}</div>\n'
        f'          <div class="meta-val">{purpose}</div>\n'
        f'        </div>\n'
        f'        <div class="meta-block">\n'
        f'          <div class="meta-label">{labels["decision"]}</div>\n'
        f'          <div class="meta-val">{decide}</div>\n'
        f'        </div>\n'
        f'        <div class="meta-block">\n'
        f'          <div class="meta-label">{labels["sees"]}</div>\n'
        f'          <div class="meta-val">{see}</div>\n'
        f'        </div>\n'
        f'      </div>\n'
        f'    </div>\n'
        f'  </div>\n'
        f'  <div class="footer">\n'
        f'    <span>Copyright © MiTAC Digital Technology Corp.</span>\n'
        f'    <span class="page-num">{page_num} / {total_pages}</span>\n'
        f'  </div>\n'
        f'</section>\n\n'
    )
