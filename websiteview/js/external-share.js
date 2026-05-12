/* ================================================================
 * external-share.js — Lightweight share-mode for docs/standalone pages
 * ----------------------------------------------------------------
 * If URL has ?ext=1 (or ?external=1), this script:
 *   1. Hides the topbar "← Knowledge Hub / Case Hub" back link
 *      (because external readers don't have access to internal hub)
 *   2. Adds a short disclaimer at the top of the doc body
 *   3. Removes internal cross-doc links (links to other docs/) — keeps
 *      external links (jira / kb / docs.google etc.) intact
 *   4. Adds 'data-ext-mode' attribute to <body> so CSS can adapt
 *
 * Usage example:
 *   share https://example.com/docs/case-learning--vinicius-platform-science.html?ext=1
 *
 * 2026-05-12 — Persona 4 (external customer share) friction fix.
 * ================================================================ */
(function () {
  'use strict';
  const params = new URLSearchParams(window.location.search);
  if (params.get('ext') !== '1' && params.get('external') !== '1') return;

  document.body.setAttribute('data-ext-mode', '1');

  // 1. Hide back link
  document.querySelectorAll('.doc-standalone-topbar a.back').forEach(el => {
    el.style.display = 'none';
  });

  // 2. Add disclaimer banner above doc-content
  const main = document.querySelector('main.doc-standalone .doc-content')
            || document.querySelector('main.doc-standalone');
  if (main) {
    const banner = document.createElement('div');
    banner.className = 'ext-banner';
    banner.setAttribute('role', 'note');
    banner.innerHTML = '<strong>Shared view</strong> · This document was shared with you. Internal cross-references have been disabled.';
    main.parentNode.insertBefore(banner, main);
  }

  // 3. Disable internal cross-doc links (any href to a docs/ sibling)
  // Keep: external (http/https different domain), in-page anchors (#), email/tel
  const here = window.location.pathname.replace(/[^/]*$/, ''); // dir of current page
  document.querySelectorAll('a[href]').forEach(a => {
    const h = a.getAttribute('href');
    if (!h) return;
    // Always keep:
    if (h.startsWith('#')) return;
    if (h.startsWith('mailto:') || h.startsWith('tel:')) return;
    if (/^https?:\/\//i.test(h)) {
      // External absolute URL — keep
      return;
    }
    // Internal relative link — strip and convert to plain text span
    const span = document.createElement('span');
    span.className = 'ext-disabled-link';
    span.title = 'Internal link disabled in shared view';
    span.textContent = a.textContent;
    a.parentNode.replaceChild(span, a);
  });
})();
