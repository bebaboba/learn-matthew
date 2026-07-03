/* Fetches aggregated insights from the LRS (via the Vercel proxy) and renders
   them into the "Live insights" widget. Stays hidden until real data exists,
   so the section never shows empty scaffolding. */
(function () {
  'use strict';
  var API = 'https://learn-matthew-ai.vercel.app/api/insights';

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function countUp(el) {
    var target = parseInt(el.getAttribute('data-target'), 10) || 0;
    var from = parseInt((el.textContent || '').replace(/,/g, ''), 10) || 0;
    if (target === from) return;
    var t0 = null, dur = 900;
    function step(ts) {
      if (t0 === null) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      el.textContent = Math.round(from + (target - from) * p).toLocaleString();
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  function stat(n, label) {
    return '<div class="insight-stat">' +
      '<span class="insight-num" data-target="' + (n || 0) + '">0</span>' +
      '<span class="insight-cap">' + esc(label) + '</span></div>';
  }

  function render(el, d) {
    var c = d.counters || {};
    var html = '<div class="insights-counters">' +
      stat(c.sessions, 'visitors') +
      stat(c.projectsExplored, 'projects explored') +
      stat(c.deepDives, 'deep dives opened') +
      stat(c.conversations, 'AI conversations') +
      '</div>';

    if (d.topTopics && d.topTopics.length) {
      html += '<div class="insights-topics">' +
        '<span class="insights-sublabel">Visitors are asking the AI guide about</span>' +
        '<ul>' + d.topTopics.map(function (t) {
          return '<li><span>' + esc(t.label) + '</span><em>' + (t.count || 0) + '</em></li>';
        }).join('') + '</ul></div>';
    }

    if (d.topDeepDives && d.topDeepDives.length) {
      html += '<div class="insights-topics">' +
        '<span class="insights-sublabel">Cards visitors open for the deeper dive</span>' +
        '<ul>' + d.topDeepDives.map(function (t) {
          return '<li><span>' + esc(t.label) + '</span><em>' + (t.count || 0) + '</em></li>';
        }).join('') + '</ul></div>';
    }

    el.innerHTML = html;
    el.classList.add('insights--ready');
    var section = document.getElementById('insights-section');
    if (section) section.classList.add('is-ready');
    el.querySelectorAll('.insight-num').forEach(countUp);
  }

  var POLL_MS = 15000;

  document.addEventListener('DOMContentLoaded', function () {
    var el = document.getElementById('insights');
    if (!el) return;

    function load() {
      fetch(API)
        .then(function (r) { return r.json(); })
        .then(function (d) {
          // Only show once the LRS is connected and at least one event exists.
          if (!d || !d.ok) return;
          var c = d.counters || {};
          if (!(c.sessions || c.projectsExplored || c.conversations || c.deepDives)) return;
          render(el, d);
        })
        .catch(function () {});
    }

    load();
    setInterval(load, POLL_MS);
    // Lets other scripts (e.g. the card-click tracker) ask for a near-immediate
    // refresh instead of waiting out the full poll interval.
    window.lmRefreshInsights = load;
  });
})();
