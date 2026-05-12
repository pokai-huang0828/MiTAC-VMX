/* jira-snapshot.js — Status filter for the ticket table */
(function () {
  const btns = document.querySelectorAll('.ji-filter');
  const rows = document.querySelectorAll('.ji-table tbody tr');
  btns.forEach(b => b.addEventListener('click', () => {
    btns.forEach(x => x.classList.remove('active'));
    b.classList.add('active');
    const f = b.dataset.filter;
    rows.forEach(r => {
      r.style.display = (f === 'all' || r.dataset.status === f) ? '' : 'none';
    });
  }));
})();
