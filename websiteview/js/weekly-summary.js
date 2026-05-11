/* ================================================================
 * Weekly Summary — TOC scroll-spy
 * ----------------------------------------------------------------
 * 每份 weekly-summary/*.md.html 共用。
 * 只做一件事:scroll spy → 高亮 TOC 當前章節。
 * ================================================================ */
(function () {
  'use strict';
  const links = document.querySelectorAll('.toc a');
  const targets = Array.from(links).map((a) => ({
    link: a,
    el: document.querySelector(a.getAttribute('href')),
  })).filter((t) => t.el);

  function onScroll() {
    const y = window.scrollY + 120;
    let active = targets[0];
    for (let i = 0; i < targets.length; i++) {
      if (targets[i].el.offsetTop <= y) active = targets[i];
    }
    links.forEach((l) => l.classList.remove('active'));
    if (active) active.link.classList.add('active');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();
