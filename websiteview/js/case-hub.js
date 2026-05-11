/* ================================================================
 * case-hub.js — Tab switching + smooth scroll for the Case Hub page
 * ----------------------------------------------------------------
 * Extracted 2026-05-11 from inline <script> block inside case-hub.html
 * so case-hub stays "no inline JS, no inline style".
 * ================================================================ */

/* Tab switching — uses class toggling so CSS controls visibility + animations */
function switchCase(id, evt) {
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
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function scrollToSection(id, evt) {
  if (evt) evt.preventDefault();
  const el = document.getElementById(id);
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
}
