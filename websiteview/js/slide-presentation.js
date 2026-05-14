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
    this.augmentSlides();        // 2026-05-14: data-part / meta-label icons / scroll-hint
    this.setupIntersectionObserver();
    this.setupKeyboardNav();
    this.setupTouchNav();
    this.setupProgressBar();
    this.setupNavDots();
  }
  /* Pre-render augmentations:
     1. section-divider gets data-part="01"/"02"/... based on order
     2. meta-block .meta-label gets icon class based on text content
     3. cover slide gets <div class="scroll-hint">Scroll</div> if not present */
  augmentSlides() {
    // 1. data-part on section dividers
    const dividers = this.slides.filter(s => s.classList.contains('section-divider'));
    dividers.forEach((d, i) => {
      const n = String(i + 1).padStart(2, '0');
      if (!d.dataset.part) d.dataset.part = n;
    });
    // 2. meta-label icon classes (detect by text content, EN + ZH)
    const labelIconMap = {
      'purpose': 'icon-purpose',  '用途':    'icon-purpose',
      'decision': 'icon-decision', '能決定':  'icon-decision', '能決定:': 'icon-decision',
      'sees': 'icon-sees',         '看到':    'icon-sees',
    };
    document.querySelectorAll('.meta-block .meta-label').forEach(el => {
      const text = (el.textContent || '').trim().toLowerCase().replace(/[:].*$/, '').trim();
      const cls = labelIconMap[text];
      if (cls) el.classList.add(cls);
    });
    // 3. scroll-hint + lens-motif on cover (skip if already present)
    const cover = document.querySelector('.slide.cover');
    if (cover) {
      if (!cover.querySelector('.scroll-hint')) {
        const hint = document.createElement('div');
        hint.className = 'scroll-hint';
        hint.textContent = 'Scroll';
        cover.appendChild(hint);
      }
      if (!cover.querySelector('.lens-motif')) {
        const lens = document.createElement('div');
        lens.className = 'lens-motif';
        lens.setAttribute('aria-hidden', 'true');
        cover.appendChild(lens);
      }
    }
    // 4. end-slide signature wrap-up enhancement
    const endSlide = document.querySelector('.slide.end-slide');
    if (endSlide && !endSlide.querySelector('.end-signature')) {
      const sig = document.createElement('div');
      sig.className = 'end-signature';
      sig.setAttribute('aria-hidden', 'true');
      sig.innerHTML = '<span class="end-dot"></span><span class="end-dot"></span><span class="end-dot"></span>';
      endSlide.appendChild(sig);
    }
    // 5. Inject SVG hub-spoke connector lines on architecture diagram slides
    //    (selects two-col + card-grid pattern: hub block above 5 fleet cards)
    this.injectArchitectureConnectors();
  }

  injectArchitectureConnectors() {
    document.querySelectorAll('.slide.inner .body').forEach(body => {
      const twoCol = body.querySelector(':scope > .two-col');
      const grid = twoCol?.nextElementSibling;
      if (!twoCol || !grid || !grid.classList.contains('card-grid')) return;
      const hub = twoCol.querySelector('.master-block, .fleet-block');
      const fleetCards = [...grid.querySelectorAll('.fleet-card')];
      if (!hub || fleetCards.length === 0) return;
      if (body.querySelector('svg.hub-connector')) return;  // already drawn

      // Container 需要 position:relative
      body.style.position = body.style.position || 'relative';

      // 建 SVG overlay 覆蓋 body
      const ns = 'http://www.w3.org/2000/svg';
      const svg = document.createElementNS(ns, 'svg');
      svg.classList.add('hub-connector');
      svg.setAttribute('aria-hidden', 'true');
      svg.style.cssText = 'position:absolute; inset:0; width:100%; height:100%; pointer-events:none; z-index:1;';

      // Draw deferred — wait for layout
      const draw = () => {
        svg.innerHTML = '';
        const bRect = body.getBoundingClientRect();
        const hRect = hub.getBoundingClientRect();
        const hubX = hRect.left + hRect.width / 2 - bRect.left;
        const hubY = hRect.bottom - bRect.top;
        fleetCards.forEach((card, i) => {
          const cRect = card.getBoundingClientRect();
          const cX = cRect.left + cRect.width / 2 - bRect.left;
          const cY = cRect.top - bRect.top;
          const midY = (hubY + cY) / 2;
          const path = document.createElementNS(ns, 'path');
          path.setAttribute('d', `M ${hubX} ${hubY} C ${hubX} ${midY}, ${cX} ${midY}, ${cX} ${cY}`);
          path.setAttribute('stroke', 'rgba(15, 23, 42, 0.30)');
          path.setAttribute('stroke-width', '1.5');
          path.setAttribute('stroke-dasharray', '6 4');
          path.setAttribute('fill', 'none');
          path.setAttribute('stroke-linecap', 'round');
          path.style.animation = `flow-dash 2s linear ${i * 0.15}s infinite`;
          svg.appendChild(path);
        });
      };
      body.insertBefore(svg, body.firstChild);
      // 2026-05-14b: 多階段 draw — rAF 在某些 sandbox 環境不會 fire,
      // 改用 immediate draw + multiple setTimeout fallbacks
      draw();                           // immediate
      setTimeout(draw, 50);             // after micro tasks
      setTimeout(draw, 250);            // after layout settles
      window.addEventListener('load', draw, { once: true });  // after all resources
      let resizeRaf;
      const onResize = () => {
        clearTimeout(resizeRaf);
        resizeRaf = setTimeout(draw, 100);
      };
      window.addEventListener('resize', onResize, { passive: true });

      // Also remove pseudo-connector lines that were drawn by CSS,since SVG now handles it
      grid.classList.add('has-svg-connector');
    });
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
        } else {
          // 2026-05-14: 滑出 viewport 移除 .visible,讓 stagger reveal 動畫可以再次播放
          e.target.classList.remove("visible");
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
    // 2026-05-14: 改成 topic sidebar(以 Part 為單位的跳轉),取代每 slide 一顆 dot
    const c = document.querySelector(".nav-dots, .topic-sidebar");
    if (!c) return;
    c.classList.add('topic-sidebar');
    c.classList.remove('nav-dots');
    c.innerHTML = "";

    // 自動偵測 parts:cover (0..first-divider) / each section-divider / end
    const parts = [];
    let currentPart = null;
    this.slides.forEach((slide, i) => {
      if (i === 0 && slide.classList.contains('cover')) {
        currentPart = { tag: 'Cover', title: '', startIdx: 0, endIdx: 0, kind: 'cover' };
        parts.push(currentPart);
      } else if (slide.classList.contains('section-divider')) {
        const partTag = (slide.querySelector('.part-tag')?.textContent || '').trim();
        // section-title 內含 <br>,textContent 不會加空白 — 自己處理
        const titleEl = slide.querySelector('.section-title');
        const partTitle = titleEl ? titleEl.innerHTML.replace(/<br\s*\/?>/gi, ' ').replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim() : '';
        currentPart = { tag: partTag, title: partTitle, startIdx: i, endIdx: i, kind: 'part' };
        parts.push(currentPart);
      } else if (slide.classList.contains('end-slide')) {
        currentPart = { tag: 'End', title: '', startIdx: i, endIdx: i, kind: 'end' };
        parts.push(currentPart);
      } else if (currentPart) {
        currentPart.endIdx = i;
      } else {
        // outline-type slide before first divider — fold into Cover
        const cov = parts.find(p => p.kind === 'cover');
        if (cov) cov.endIdx = i;
      }
    });

    // Header — deck title + progress
    const headerEl = document.createElement('div');
    headerEl.className = 'topic-sidebar-header';
    const deckTitle = document.title.split('·')[0].trim();
    headerEl.innerHTML = `
      <div class="ts-deck-title">${deckTitle}</div>
      <div class="ts-progress"><div class="ts-progress-bar"></div></div>
      <div class="ts-progress-text"><span class="ts-current">1</span> / ${this.slides.length}</div>
    `;
    c.appendChild(headerEl);
    this.tsProgressBar = headerEl.querySelector('.ts-progress-bar');
    this.tsCurrent = headerEl.querySelector('.ts-current');

    // Topic list
    const listEl = document.createElement('div');
    listEl.className = 'topic-list';
    this.topicItemEls = parts.map((p) => {
      const btn = document.createElement('button');
      btn.className = `topic-item topic-${p.kind}`;
      btn.dataset.startIdx = p.startIdx;
      btn.dataset.endIdx = p.endIdx;
      const labelHTML = p.kind === 'cover' ? `<span class="ti-tag">Intro</span><span class="ti-title">Cover &amp; Outline</span>`
        : p.kind === 'end' ? `<span class="ti-tag">End</span><span class="ti-title">Wrap up</span>`
        : `<span class="ti-tag">${p.tag}</span><span class="ti-title">${p.title}</span>`;
      const range = p.endIdx - p.startIdx + 1;
      btn.innerHTML = `${labelHTML}<span class="ti-count">${range}</span>`;
      btn.setAttribute('aria-label', `Jump to ${p.tag} ${p.title}`);
      btn.addEventListener('click', () => this.goTo(p.startIdx));
      listEl.appendChild(btn);
      return { el: btn, ...p };
    });
    c.appendChild(listEl);

    // Toggle button(mobile / collapsed state)
    const toggle = document.createElement('button');
    toggle.className = 'topic-sidebar-toggle';
    toggle.setAttribute('aria-label', 'Toggle topic sidebar');
    toggle.innerHTML = '☰';
    toggle.addEventListener('click', () => c.classList.toggle('is-open'));
    c.appendChild(toggle);
  }
  updateNavDots() {
    if (!this.topicItemEls) return;
    const i = this.currentIdx;
    this.topicItemEls.forEach(p => {
      p.el.classList.toggle('active', i >= p.startIdx && i <= p.endIdx);
    });
    if (this.tsProgressBar) {
      const pct = ((i + 1) / this.slides.length) * 100;
      this.tsProgressBar.style.width = pct + '%';
    }
    if (this.tsCurrent) this.tsCurrent.textContent = (i + 1).toString();
  }
}

new SlidePresentation();
