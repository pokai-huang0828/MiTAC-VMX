/* ================================================================
 * sticky-toc.js — Auto-build a sticky in-page TOC for long docs
 * ----------------------------------------------------------------
 * Activates when the doc has 8+ <h2> inside .doc-content.
 * Builds a fixed-position TOC on the right edge with:
 *   - All h2 (with id) listed
 *   - Active h2 highlighted via IntersectionObserver
 *   - Click → smooth scroll
 * Hidden on viewport < 1100px (small screens have limited horizontal room).
 *
 * 2026-05-12 — for ai-weekly-roundup, cary-elvis-timeline,
 * connectsource-passenger-blurring, q2-request-review, etc.
 * ================================================================ */
(function () {
  'use strict';

  function init() {
    const content = document.querySelector('main.doc-standalone .doc-content');
    if (!content) return;
    const headings = Array.from(content.querySelectorAll('h2[id]'));
    if (headings.length < 8) return;
    if (window.innerWidth < 1100) return;

    // Build TOC
    const toc = document.createElement('nav');
    toc.className = 'sticky-toc';
    toc.setAttribute('aria-label', 'Page sections');
    const inner = document.createElement('div');
    inner.className = 'sticky-toc-inner';
    const head = document.createElement('div');
    head.className = 'sticky-toc-head';
    head.textContent = `📑 ${headings.length} sections`;
    inner.appendChild(head);
    const ul = document.createElement('ul');

    headings.forEach((h, i) => {
      const li = document.createElement('li');
      const a = document.createElement('a');
      a.href = '#' + h.id;
      // Strip aria-hidden emoji wrappers from heading text for cleaner TOC label
      const cloned = h.cloneNode(true);
      cloned.querySelectorAll('[aria-hidden]').forEach(el => el.remove());
      a.textContent = (cloned.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 60);
      a.dataset.targetId = h.id;
      li.appendChild(a);
      ul.appendChild(li);
    });
    inner.appendChild(ul);
    toc.appendChild(inner);
    document.body.appendChild(toc);

    // IntersectionObserver to highlight current section
    const linkById = new Map();
    toc.querySelectorAll('a').forEach(a => linkById.set(a.dataset.targetId, a));

    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        const link = linkById.get(e.target.id);
        if (!link) return;
        if (e.isIntersecting) {
          toc.querySelectorAll('a.is-active').forEach(x => x.classList.remove('is-active'));
          link.classList.add('is-active');
        }
      });
    }, { rootMargin: '-20% 0px -70% 0px', threshold: 0 });
    headings.forEach(h => obs.observe(h));

    // Smooth scroll on click
    toc.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', (e) => {
        e.preventDefault();
        const id = a.dataset.targetId;
        const target = document.getElementById(id);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          // Update URL hash without jump
          history.replaceState(null, '', '#' + id);
        }
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
