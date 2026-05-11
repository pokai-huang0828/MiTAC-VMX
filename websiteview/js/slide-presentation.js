/* ================================================================
 * slide-presentation.js — Scroll-driven slide deck behaviour
 * ----------------------------------------------------------------
 * Shared by:
 *   - websiteview/portal-architecture.html (55 EN slides)
 *   - websiteview/portal-briefing.html     (25 ZH slides)
 *
 * Extracted 2026-05-11 from duplicated inline <script> blocks
 * so both portal decks share one source of truth.
 * ================================================================ */

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
