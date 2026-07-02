// ── Work filter ────────────────────────────────────────────────
const filterBtns = document.querySelectorAll('.filter-btn');
const projectCards = document.querySelectorAll('.project-card');

filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    const filter = btn.dataset.filter;

    filterBtns.forEach(b => {
      b.classList.remove('active');
      b.setAttribute('aria-selected', 'false');
    });
    btn.classList.add('active');
    btn.setAttribute('aria-selected', 'true');

    projectCards.forEach(card => {
      const match = filter === 'all' || card.dataset.category === filter;
      card.classList.toggle('hidden', !match);
    });
  });
});

// ── Work card expand / collapse ──────────────────────────────────
projectCards.forEach(card => {
  const toggle = card.querySelector('.project-toggle');
  if (!toggle) return;

  const setExpanded = (expanded) => {
    toggle.setAttribute('aria-expanded', String(expanded));
    toggle.querySelector('.project-toggle-label').textContent = expanded ? 'Show less' : 'Read more';
  };

  card.addEventListener('click', (e) => {
    if (e.target.closest('a')) return; // let real links navigate normally
    setExpanded(toggle.getAttribute('aria-expanded') !== 'true');
  });
});

// ── Active nav link on scroll ───────────────────────────────────
const sections = document.querySelectorAll('main section[id]');
const navLinks  = document.querySelectorAll('.nav-links a');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    navLinks.forEach(link => {
      link.classList.toggle('active', link.getAttribute('href') === `#${entry.target.id}`);
    });
  });
}, { rootMargin: '-40% 0px -55% 0px' });

sections.forEach(s => observer.observe(s));

// ── Footer year ─────────────────────────────────────────────────
document.getElementById('year').textContent = new Date().getFullYear();
