/* Anonymous xAPI tracker for learnmatthew.com.
   Sends lightweight events to the Vercel proxy, which writes xAPI statements
   to the Learning Record Store. No personal data — just a random session id
   kept in localStorage so repeat events in a visit aren't double-counted. */
(function () {
  'use strict';
  var API = 'https://learn-matthew-ai.vercel.app/api/track';
  var SID_KEY = 'lm_sid';

  function sessionId() {
    try {
      var s = localStorage.getItem(SID_KEY);
      if (!s) {
        s = (window.crypto && crypto.randomUUID)
          ? crypto.randomUUID()
          : String(Date.now()) + Math.random().toString(36).slice(2);
        localStorage.setItem(SID_KEY, s);
      }
      return s;
    } catch (e) {
      return 'anon';
    }
  }

  function track(event, label) {
    try {
      var body = JSON.stringify({ event: event, label: label || '', sessionId: sessionId() });
      if (navigator.sendBeacon) {
        navigator.sendBeacon(API, new Blob([body], { type: 'application/json' }));
      } else {
        fetch(API, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: body,
          keepalive: true
        }).catch(function () {});
      }
    } catch (e) { /* analytics must never break the page */ }
  }
  window.lmTrack = track;

  document.addEventListener('DOMContentLoaded', function () {
    track('session_start', 'Portfolio session');

    var seen = {};
    function once(key) { if (seen[key]) return false; seen[key] = 1; return true; }

    if ('IntersectionObserver' in window) {
      // Project card views (fire once each, when half-visible)
      var projectObs = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          var titleEl = e.target.querySelector('.project-title');
          var title = titleEl && titleEl.textContent.trim();
          if (title && once('p:' + title)) track('project_view', title);
          projectObs.unobserve(e.target);
        });
      }, { threshold: 0.5 });
      document.querySelectorAll('.project-card').forEach(function (c) { projectObs.observe(c); });

      // Section engagement
      var sectionObs = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          var id = e.target.id || 'section';
          if (once('s:' + id)) track('section_view', id);
        });
      }, { threshold: 0.4 });
      document.querySelectorAll('main section[id]').forEach(function (s) { sectionObs.observe(s); });
    }

    // AI launches + outbound clicks (capture phase so it fires before navigation)
    document.addEventListener('click', function (ev) {
      var a = ev.target.closest && ev.target.closest('a');
      if (!a) return;
      var href = a.getAttribute('href') || '';
      if (a.classList.contains('project-card-link') || /learn-matthew-ai\.vercel\.app/.test(href)) {
        track('ai_launch', 'Learn Matthew');
      } else if (/^mailto:/.test(href)) {
        track('outbound_click', 'Email');
      } else if (/linkedin\.com/.test(href)) {
        track('outbound_click', 'LinkedIn');
      }
    }, true);
  });
})();
