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
  const searchStatus = document.getElementById('searchStatus');
  const filterChips = document.querySelectorAll('.filter-chip');
  const allCards = document.querySelectorAll('.doc-card');
  const totalDocs = allCards.length;
  let activeFilter = '';
  let activeFilterLabel = '';

  function normalizeSearchText(value) {
    return String(value || '')
      .normalize('NFKC')
      .toLowerCase()
      .replace(/[\u2010-\u2015\u2212_-]+/g, ' ')
      .replace(/[\/\\]+/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
  }

  function compactSearchText(value) {
    return normalizeSearchText(value).replace(/\s+/g, '');
  }

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

  function getCardText(card) {
    return (
      (card.dataset.title || '') + ' ' +
      (card.dataset.file || '') + ' ' +
      (card.dataset.tags || '') + ' ' +
      card.textContent
    );
  }

  function updateCounters(cat, visible) {
    const counter = cat.querySelector('.cat-count .num');
    if (counter) counter.textContent = visible;

    const tocLink = document.querySelector(`aside.toc a[href="#${cat.id}"] .num`);
    if (tocLink) tocLink.textContent = visible;
  }

  function updateSearchStatus(totalMatches, hasQuery) {
    if (!searchStatus) return;

    const parts = [];
    if (activeFilterLabel) parts.push(activeFilterLabel);
    if (hasQuery) parts.push(`"${search.value.trim()}"`);

    const scope = parts.length ? `符合 ${parts.join(' + ')} 的 ` : '';
    searchStatus.textContent = `顯示 ${scope}${totalMatches} / ${totalDocs} 份文件`;
  }

  /* ── 2. Search/filter — case-insensitive across title + filename + tags ── */
  function applyFilter() {
    const q = normalizeSearchText(search.value);
    const qCompact = compactSearchText(search.value);
    const filter = normalizeSearchText(activeFilter);
    const filterCompact = compactSearchText(activeFilter);
    let totalMatches = 0;
    cats.forEach((c) => {
      const cards = c.querySelectorAll('.doc-card');
      let visible = 0;
      cards.forEach((card) => {
        const rawHay = getCardText(card);
        const hay = normalizeSearchText(rawHay);
        const hayCompact = compactSearchText(rawHay);
        const queryMatch = !q || hay.indexOf(q) !== -1 || (!!qCompact && hayCompact.indexOf(qCompact) !== -1);
        const filterMatch = !filter || hay.indexOf(filter) !== -1 || (!!filterCompact && hayCompact.indexOf(filterCompact) !== -1);
        const match = queryMatch && filterMatch;
        card.classList.toggle('hidden', !match);
        if (match) visible++;
      });
      // Hide category if zero visible AND a query is set
      c.classList.toggle('hidden', (q || filter) && visible === 0);
      updateCounters(c, visible);
      totalMatches += visible;
    });
    if (noMatch) noMatch.classList.toggle('hidden', !(q || filter) || totalMatches > 0);
    updateSearchStatus(totalMatches, !!q);
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

  filterChips.forEach((chip) => {
    chip.addEventListener('click', () => {
      activeFilter = chip.dataset.filter || '';
      activeFilterLabel = activeFilter ? chip.textContent.trim() : '';
      filterChips.forEach((item) => {
        item.classList.toggle('active', item === chip);
      });
      applyFilter();
    });
  });

  /* ── 3. Set initial per-category counts from DOM ── */
  cats.forEach((c) => {
    const cards = c.querySelectorAll('.doc-card');
    updateCounters(c, cards.length);
  });
  updateSearchStatus(totalDocs, false);
})();
