/* Fetches content-construction feedback from the two AI project's own /api/insights
   endpoints (Adaptive Tutor, Plato's Cave) and renders it alongside the site's own
   Live insights widget. Stays hidden until at least one project has real signal,
   so the section never shows empty scaffolding. */
(function () {
  'use strict';
  var SOURCES = [
    { key: 'adaptive-tutor', label: 'Adaptive Tutor', url: 'https://adaptive-tutor-ruddy.vercel.app/api/insights' },
    { key: 'plato-cave', label: "Plato's Cave", url: 'https://plato-cave-tutor.vercel.app/api/insights' },
  ];

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function adaptiveCard(d) {
    var c = d.counters || {};
    var html = '<div class="course-card">' +
      '<span class="course-card-title">Adaptive Tutor</span>' +
      '<div class="course-card-stats">' +
      '<span><strong>' + (c.sessions || 0) + '</strong> sessions</span>' +
      (c.objectivesMetRatePct != null
        ? '<span><strong>' + c.objectivesMetRatePct + '%</strong> objectives met</span>'
        : '') +
      '</div>';
    if (d.struggleSignal) {
      var s = d.struggleSignal;
      html += '<p class="course-signal">Content signal: <em>' + esc(s.problem) + '</em> — ' +
        s.hintRatePct + '% of attempts used a hint, only ' + s.correctRatePct + '% correct on first try ' +
        '(' + s.attempts + ' attempts). Candidate for more scaffolding.</p>';
    }
    html += '</div>';
    return html;
  }

  function platoCard(d) {
    var c = d.counters || {};
    var html = '<div class="course-card">' +
      '<span class="course-card-title">Plato’s Cave</span>' +
      '<div class="course-card-stats">' +
      '<span><strong>' + (c.sessions || 0) + '</strong> sessions</span>' +
      '<span><strong>' + (c.totalTurns || 0) + '</strong> tutor turns</span>' +
      '</div>';
    if (d.mostDiscussed) {
      html += '<p class="course-signal">Most-discussed page: <em>' + esc(d.mostDiscussed.title) +
        '</em> (page ' + d.mostDiscussed.page + ') — ' + d.mostDiscussed.turns + ' turns.</p>';
    }
    if (d.struggleSignal) {
      html += '<p class="course-signal">Content signal: <em>' + esc(d.struggleSignal.title) +
        '</em> (page ' + d.struggleSignal.page + ') skews toward struggle-mode replies ' +
        '(' + d.struggleSignal.struggleRatePct + '% of ' + d.struggleSignal.turns + ' turns).</p>';
    }
    html += '</div>';
    return html;
  }

  var RENDERERS = { 'adaptive-tutor': adaptiveCard, 'plato-cave': platoCard };

  function hasSignal(key, d) {
    var c = d.counters || {};
    if (key === 'adaptive-tutor') return (c.sessions || 0) > 0 || !!d.struggleSignal;
    return (c.sessions || 0) > 0 || !!d.mostDiscussed || !!d.struggleSignal;
  }

  var POLL_MS = 30000;

  document.addEventListener('DOMContentLoaded', function () {
    var el = document.getElementById('course-feedback');
    if (!el) return;

    function load() {
      Promise.all(
        SOURCES.map(function (src) {
          return fetch(src.url)
            .then(function (r) { return r.json(); })
            .then(function (d) { return { src: src, data: d }; })
            .catch(function () { return null; });
        })
      ).then(function (results) {
        var cards = results
          .filter(function (r) { return r && r.data && r.data.ok && hasSignal(r.src.key, r.data); })
          .map(function (r) { return RENDERERS[r.src.key](r.data); });

        if (!cards.length) return;

        el.innerHTML = '<div class="course-feedback-grid">' + cards.join('') + '</div>';
        el.classList.add('course-feedback--ready');
        var label = document.querySelector('.course-feedback-label');
        if (label) label.classList.add('is-ready');
        var intro = el.previousElementSibling;
        if (intro && intro.classList.contains('insights-intro')) intro.classList.add('is-ready');
      });
    }

    load();
    setInterval(load, POLL_MS);
  });
})();
