/* Shared mobile scroll-to-top FAB behavior. */
(function () {
  'use strict';

  function init() {
    const fab = document.querySelector('.scroll-top-fab');
    if (!fab) return;

    const show = () => fab.classList.toggle('visible', window.scrollY > 400);
    window.addEventListener('scroll', show, { passive: true });
    fab.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
    show();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
