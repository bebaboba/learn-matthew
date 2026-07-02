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

// ── Work card detail overlay ──────────────────────────────────────
const overlay = document.getElementById('project-overlay');
const overlayTags = document.getElementById('overlay-tags');
const overlayTitle = document.getElementById('overlay-title');
const overlayBody = document.getElementById('overlay-body');
let lastFocused = null;

function openOverlay(card) {
  const title = card.querySelector('.project-title').textContent.trim();
  overlayTags.innerHTML = card.querySelector('.project-tags').innerHTML;
  overlayTitle.textContent = title;
  overlayBody.innerHTML =
    `<p>${card.querySelector('.project-desc').innerHTML}</p>` +
    card.querySelector('.project-more').innerHTML;

  lastFocused = document.activeElement;
  overlay.hidden = false;
  document.body.classList.add('overlay-open');
  requestAnimationFrame(() => overlay.querySelector('.project-overlay-close').focus());

  if (window.lmTrack) window.lmTrack('project_expand', title);
}

function closeOverlay() {
  overlay.hidden = true;
  document.body.classList.remove('overlay-open');
  if (lastFocused) lastFocused.focus();
}

projectCards.forEach(card => {
  const toggle = card.querySelector('.project-toggle');
  if (!toggle) return;

  card.addEventListener('click', (e) => {
    if (e.target.closest('a')) return; // let real links navigate normally
    openOverlay(card);
  });
});

if (overlay) {
  overlay.addEventListener('click', (e) => {
    if (e.target.closest('[data-overlay-close]')) closeOverlay();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !overlay.hidden) closeOverlay();
  });
}

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
