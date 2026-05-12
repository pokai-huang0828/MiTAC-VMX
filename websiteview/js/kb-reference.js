/* ================================================================
 * kb-reference.js — Tab switching for KB Reference page
 * Quick / Full panel switcher. 2026-05-12 從 inline <script> 抽出。
 * ================================================================ */

(function () {
  var btns = document.querySelectorAll('.kbr-tabs button');
  btns.forEach(function (b) {
    b.addEventListener('click', function () {
      btns.forEach(function (x) { x.classList.remove('active'); });
      b.classList.add('active');
      document.querySelectorAll('.kbr-panel').forEach(function (p) { p.classList.remove('active'); });
      var target = document.getElementById('kbr-' + b.dataset.tab);
      if (target) target.classList.add('active');
    });
  });
})();
