/* ================================================================
 * lightbox.js — single shared image preview overlay
 * ----------------------------------------------------------------
 * Mounted by every hub HTML via <script src=".../js/lightbox.js" defer>.
 *
 * Requires:
 *   - .lightbox / .lightbox-close / .lightbox-caption styles (in shared.css)
 *   - <div class="lightbox" id="lightbox">…</div> markup somewhere on the page
 *
 * Click handling: any <img> matching SELECTOR opens in a full-screen modal.
 * Keys: Escape closes. Click on backdrop or × also closes.
 * ================================================================ */
(function () {
  // Broad selector — covers all hubs. Pages without these elements are no-ops.
  const SELECTOR = [
    ".slide-image",
    ".slide-thumb",
    ".portal-img-grid img",
    ".portal-img",
    ".page-detail-image img",
    ".doc-content img",
  ].join(", ");

  function init() {
    const overlay = document.getElementById("lightbox");
    if (!overlay) return;
    const lbImg = overlay.querySelector("img");
    const lbCap = overlay.querySelector(".lightbox-caption");
    if (!lbImg || !lbCap) return;

    const close = () => {
      overlay.classList.remove("is-open");
      lbImg.src = "";
      lbCap.textContent = "";
    };

    overlay.addEventListener("click", (e) => {
      if (e.target === overlay || e.target.classList.contains("lightbox-close")) close();
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") close();
    });
    document.addEventListener(
      "click",
      (e) => {
        const t = e.target;
        if (!(t instanceof HTMLImageElement)) return;
        if (!t.matches(SELECTOR)) return;
        e.preventDefault();
        e.stopPropagation();
        lbImg.src = t.currentSrc || t.src;
        lbCap.textContent = t.alt || "";
        overlay.classList.add("is-open");
      },
      true
    );
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
