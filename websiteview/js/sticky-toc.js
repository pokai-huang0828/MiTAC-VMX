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

  /** Return the part-N section that contains the heading, or null. */
  function findParentSection(h) {
    let el = h.parentElement;
    while (el && el !== document.body) {
      if (el.tagName === 'SECTION' && el.id && /^part-\d+$/.test(el.id)) {
        return el;
      }
      el = el.parentElement;
    }
    return null;
  }

  function init() {
    const content = document.querySelector('main.doc-standalone .doc-content');
    if (!content) return;
    const headings = Array.from(content.querySelectorAll('h2[id]'));
    if (headings.length < 8) return;
    if (window.innerWidth < 1100) return;

    // ─── 2026-05-12: detect merged-doc sections + disambiguate duplicate labels ───
    // Step 1: collect raw text per heading
    const items = headings.map((h, i) => {
      const cloned = h.cloneNode(true);
      cloned.querySelectorAll('[aria-hidden]').forEach(el => el.remove());
      const raw = (cloned.textContent || '').trim().replace(/\s+/g, ' ');
      const parentSec = findParentSection(h);
      const partNum = parentSec ? parseInt(parentSec.id.replace(/^part-/, ''), 10) : null;
      return { h, raw, partNum, idx: i };
    });

    // Step 2: count label occurrences. Duplicate label inside merged docs gets §N prefix.
    const labelCount = {};
    items.forEach(it => { labelCount[it.raw] = (labelCount[it.raw] || 0) + 1; });

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

    items.forEach(it => {
      const li = document.createElement('li');
      const a = document.createElement('a');
      a.href = '#' + it.h.id;
      // Add §N prefix when the label appears more than once across the doc
      // AND the heading is inside a part-N section (merged-doc case).
      let label = it.raw;
      if (labelCount[it.raw] > 1 && it.partNum !== null) {
        li.classList.add('sticky-toc-subitem');
        label = `§${it.partNum} · ${label}`;
      } else if (it.partNum !== null && it.partNum > 0) {
        // Indent items that belong to a part-N section so the visual hierarchy
        // shows merged-doc structure
        li.classList.add('sticky-toc-subitem');
      }
      a.textContent = label.slice(0, 60);
      a.dataset.targetId = it.h.id;
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
