/* ================================================================
 * case-hub.js — Tab switching + URL hash routing + smooth scroll
 * ----------------------------------------------------------------
 * 2026-05-12: 加 hashchange + onload handler,讓從 index.html 點
 * `case-hub.html#honeywell` / `#ps` / `#cs` / `#pm` / `#weekly`
 * 進來時自動切到對應 tab(不再卡在 default Platform Science)。
 * ================================================================ */

/* Tab switching — uses class toggling so CSS controls visibility + animations */
function switchCase(id, evt) {
  if (!id) return;
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.sidebar').forEach(s => s.classList.add('hidden'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  const page = document.getElementById('page-' + id);
  const sidebar = document.getElementById('sidebar-' + id);
  if (page) page.classList.add('active');
  if (sidebar) sidebar.classList.remove('hidden');
  const trigger = (evt && evt.currentTarget)
    || document.querySelector('.tab-btn[data-case="' + id + '"]');
  if (trigger) trigger.classList.add('active');
  // Avoid forcing scroll-to-top when invoked from URL hash on first load,
  // which would override the user's expectation of arriving at the case.
  if (evt && evt.currentTarget) {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

function scrollToSection(id, evt) {
  if (evt) evt.preventDefault();
  const el = document.getElementById(id);
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

/* ─── URL hash routing ─────────────────────────────────────────
 * Accepts:  #honeywell · #ps · #cs · #pm · #weekly · #page-<id> · #sidebar-<id>
 * Falls back to first .tab-btn.active if hash absent / invalid.
 * ─────────────────────────────────────────────────────────── */
const VALID_CASES = new Set(['honeywell', 'ps', 'cs', 'pm', 'weekly']);

function caseFromHash() {
  const raw = (window.location.hash || '').replace(/^#/, '');
  if (!raw) return null;
  // Strip page-/sidebar- prefix if present
  const id = raw.replace(/^page-/, '').replace(/^sidebar-/, '');
  return VALID_CASES.has(id) ? id : null;
}

function syncTabFromHash() {
  const id = caseFromHash();
  if (id) switchCase(id);
}

window.addEventListener('hashchange', syncTabFromHash);
document.addEventListener('DOMContentLoaded', syncTabFromHash);
/* In case DOMContentLoaded already fired by the time this script loads: */
if (document.readyState !== 'loading') syncTabFromHash();
