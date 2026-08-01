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

  function referrerHost() {
    try {
      if (!document.referrer) return 'direct';
      var h = new URL(document.referrer).hostname.replace(/^www\./, '');
      return (h === 'learnmatthew.com') ? 'direct' : h;
    } catch (e) { return 'direct'; }
  }

  function track(event, label, extra) {
    try {
      var payload = { event: event, label: label || '', sessionId: sessionId() };
      if (extra && extra.ref) payload.ref = extra.ref;
      if (extra && extra.duration != null) payload.duration = extra.duration;
      var body = JSON.stringify(payload);
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

  function throttle(fn, wait) {
    var last = 0, timer = null;
    return function () {
      var now = Date.now();
      if (now - last >= wait) {
        last = now;
        fn();
      } else {
        clearTimeout(timer);
        timer = setTimeout(function () { last = Date.now(); fn(); }, wait - (now - last));
      }
    };
  }

  document.addEventListener('DOMContentLoaded', function () {
    // Checked before sessionId() below creates/reuses the stored id, so this
    // reflects whether the id already existed from a prior visit.
    var isReturning = false;
    try { isReturning = !!localStorage.getItem(SID_KEY); } catch (e) {}

    track('session_start', 'Portfolio session', { ref: referrerHost() });
    if (isReturning) track('return_visit', 'Return visit');

    var seen = {};
    function once(key) { if (seen[key]) return false; seen[key] = 1; return true; }

    // Scroll depth milestones — each fires at most once per pageview.
    var scrollMilestones = [25, 50, 75, 100];
    function checkScrollDepth() {
      var doc = document.documentElement;
      var scrollable = doc.scrollHeight - doc.clientHeight;
      var pct = scrollable > 0 ? Math.min(100, Math.round((window.pageYOffset / scrollable) * 100)) : 100;
      scrollMilestones.forEach(function (m) {
        if (pct >= m && once('scroll:' + m)) track('scroll_depth', String(m));
      });
    }
    window.addEventListener('scroll', throttle(checkScrollDepth, 500), { passive: true });
    checkScrollDepth();

    // Time on page — fired once, whenever the visitor first leaves or hides the tab.
    var pageStart = Date.now();
    var timeSent = false;
    function sendTimeOnPage() {
      if (timeSent) return;
      var seconds = Math.round((Date.now() - pageStart) / 1000);
      if (seconds < 1) return;
      timeSent = true;
      track('time_on_page', '', { duration: seconds });
    }
    document.addEventListener('visibilitychange', function () {
      if (document.visibilityState === 'hidden') sendTimeOnPage();
    });
    window.addEventListener('pagehide', sendTimeOnPage);

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
      if (/learn-matthew-ai\.vercel\.app/.test(href)) {
        track('ai_launch', 'Learn Matthew');
      } else if (/adaptive-tutor-ruddy\.vercel\.app/.test(href)) {
        track('ai_launch', 'Adaptive Tutor');
      } else if (/^mailto:/.test(href)) {
        track('outbound_click', 'Email');
      } else if (/linkedin\.com/.test(href)) {
        track('outbound_click', 'LinkedIn');
      }
    }, true);
  });
})();
