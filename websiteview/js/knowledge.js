/* ================================================================
 * Kenny VMX · Knowledge Hub — knowledge.js
 * ----------------------------------------------------------------
 * Static hub: 不再用 fetch / JSON-driven app。只負責:
 *   1. Sidebar TOC 高亮(scroll spy)
 *   2. 搜尋:filter 各 doc card 顯示與否
 *   3. Category 動態 doc count badge 更新
 * ================================================================ */
(function () {
  'use strict';

  const search = document.getElementById('searchBox');
  const tocLinks = document.querySelectorAll('aside.toc a[data-cat]');
  const cats = document.querySelectorAll('section.cat');
  const noMatch = document.getElementById('nomatch');

  /* ── 1. Scroll spy for sidebar TOC ── */
  function updateActiveCat() {
    const y = window.scrollY + 140;
    let activeId = null;
    cats.forEach((c) => {
      if (c.offsetTop <= y) activeId = c.id;
    });
    tocLinks.forEach((a) => {
      a.classList.toggle('active', a.getAttribute('href') === '#' + activeId);
    });
  }
  window.addEventListener('scroll', updateActiveCat, { passive: true });
  updateActiveCat();

  /* ── 2. Search filter — case-insensitive across title + filename + tags ── */
  function applyFilter() {
    const q = (search.value || '').trim().toLowerCase();
    let totalMatches = 0;
    cats.forEach((c) => {
      const cards = c.querySelectorAll('.doc-card');
      let visible = 0;
      cards.forEach((card) => {
        const hay = (
          (card.dataset.title || '') + ' ' +
          (card.dataset.file || '') + ' ' +
          (card.dataset.tags || '') + ' ' +
          card.textContent
        ).toLowerCase();
        const match = !q || hay.indexOf(q) !== -1;
        card.classList.toggle('hidden', !match);
        if (match) visible++;
      });
      // Hide category if zero visible AND a query is set
      c.classList.toggle('hidden', q && visible === 0);
      // Live count badge
      const counter = c.querySelector('.cat-count .num');
      if (counter) counter.textContent = visible;
      totalMatches += visible;
    });
    if (noMatch) noMatch.classList.toggle('hidden', !q || totalMatches > 0);
  }
  if (search) {
    search.addEventListener('input', applyFilter);
    /* Ctrl+K / Cmd+K → focus search */
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        search.focus(); search.select();
      }
      if (e.key === 'Escape' && document.activeElement === search) {
        search.value = ''; applyFilter(); search.blur();
      }
    });
  }

  /* ── 3. Set initial per-category counts from DOM ── */
  cats.forEach((c) => {
    const cards = c.querySelectorAll('.doc-card');
    const counter = c.querySelector('.cat-count .num');
    if (counter) counter.textContent = cards.length;
  });
})();
