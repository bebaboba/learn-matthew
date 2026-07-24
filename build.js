#!/usr/bin/env node
/* Renders index.html from content.md + index.template.html.
   No dependencies — Node built-ins only. Run: `node build.js`.
   Edit copy in content.md; never edit index.html directly (it's generated). */

const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const md = fs.readFileSync(path.join(ROOT, 'content.md'), 'utf8');
const template = fs.readFileSync(path.join(ROOT, 'index.template.html'), 'utf8');

// ── Parse content.md into { section: { fields:{}, items:[] } } ──────────────
function parseContent(src) {
  const data = {};
  let section = null;
  let target = null; // object currently receiving key/values
  let key = null;
  for (const line of src.split(/\r?\n/)) {
    if (/^###\s+/.test(line)) {
      const item = { title: line.replace(/^###\s+/, '').trim() };
      data[section].items.push(item);
      target = item;
      key = null;
    } else if (/^##\s+/.test(line)) {
      section = line.replace(/^##\s+/, '').trim().toLowerCase();
      data[section] = { fields: {}, items: [] };
      target = data[section].fields;
      key = null;
    } else if (/^#/.test(line)) {
      continue; // comment
    } else {
      const m = line.match(/^([a-z][a-z0-9_]*):\s?(.*)$/);
      if (m && target) {
        key = m[1];
        target[key] = m[2];
      } else if (key && target) {
        target[key] += '\n' + line; // continuation
      }
    }
  }
  return data;
}

const data = parseContent(md);

// ── Helpers ─────────────────────────────────────────────────────────────────
const esc = (s) =>
  String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const collapse = (s) => String(s).trim().replace(/\s*\n\s*/g, ' ').replace(/[ \t]{2,}/g, ' ');
const field = (sec, k) => (data[sec] && data[sec].fields[k] != null ? data[sec].fields[k] : '');

function heroHeading(text) {
  return text
    .split('\n')
    .map((l) => l.trim())
    .filter(Boolean)
    .map((l) => esc(l).replace(/\*([^*]+)\*/g, '<em>$1</em>'))
    .join('<br />\n          ');
}

function bioParagraphs(text) {
  return text
    .split(/\n\s*\n/)
    .map((p) => collapse(p))
    .filter(Boolean)
    .map((p) => `<p>${esc(p)}</p>`)
    .join('\n            ');
}

const TAG_CLASS = { Product: 'product', 'L&D': 'ld', Experiment: 'experiments', 'Weekend Vibes': 'experiments', Personal: 'personal' };

// Converts markdown-style [label](url) into real links, applied after escaping
// so plain "&" etc. in prose stays safe while intentional links still render.
function linkify(text) {
  return text.replace(
    /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g,
    '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>'
  );
}

function boldify(text) {
  return text.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
}

// Splits a work card's "more" field on blank lines into <p> tags (like
// bioParagraphs), so longer deeper-dive copy can carry real paragraph breaks
// and **bold** labels instead of collapsing into one run-on paragraph.
function moreParagraphs(text) {
  return text
    .split(/\n\s*\n/)
    .map((p) => collapse(p))
    .filter(Boolean)
    .map((p) => `<p>${boldify(linkify(esc(p)))}</p>`)
    .join('\n                ');
}

function skillCards() {
  return data.skills.items
    .map(
      (it) =>
        `            <div class="skill-card">\n` +
        `              <h3>${esc(it.title)}</h3>\n` +
        `              <p>${esc(collapse(it.desc || ''))}</p>\n` +
        `            </div>`
    )
    .join('\n');
}

function tagSpans(tagsField, indent) {
  return (tagsField || '')
    .split(',')
    .map((t) => t.trim())
    .filter(Boolean)
    .map((t) => `${indent}<span class="tag tag--${TAG_CLASS[t] || 'product'}">${esc(t)}</span>`)
    .join('\n');
}

function workCards() {
  return data.work.items
    .map((it) => {
      const cat = (it.category || '').trim();
      const img = (it.image || '').trim();
      const desc = linkify(esc(collapse(it.desc || '')));
      const stat = esc(collapse(it.stat || ''));
      const link = (it.link || '').trim();
      const more = moreParagraphs(it.more || '');
      const thumb = `<div class="project-thumb" aria-hidden="true"><img src="images/${img}" alt="" /></div>`;

      const ctaLink = link
        ? `\n                <a class="project-link" href="${link}" target="_blank" rel="noopener noreferrer">${esc(
            collapse(it.cta || 'Launch the experience →')
          )}</a>`
        : '';

      return (
        `          <article class="project-card" data-category="${cat}">\n` +
        `            ${thumb}\n` +
        `            <div class="project-info">\n` +
        `              <div class="project-tags">\n` +
        `${tagSpans(it.tags, '                ')}\n` +
        `              </div>\n` +
        `              <h3 class="project-title">${esc(it.title)}</h3>\n` +
        `              <p class="project-desc">${desc}</p>\n` +
        `              <span class="project-stat">${stat}</span>${ctaLink}\n` +
        `              <button class="project-toggle" type="button" aria-haspopup="dialog">\n` +
        `                <span class="project-toggle-label">Read more</span>\n` +
        `                <span class="project-toggle-icon" aria-hidden="true"></span>\n` +
        `              </button>\n` +
        `              <div class="project-more" hidden>\n` +
        `                ${more}${ctaLink}\n` +
        `              </div>\n` +
        `            </div>\n` +
        `          </article>`
      );
    })
    .join('\n\n');
}

// ── Token replacements ────────────────────────────────────────────────────────
const replacements = {
  'meta.title': esc(collapse(field('meta', 'title'))),
  'meta.description': esc(collapse(field('meta', 'description'))),
  'nav.logo': esc(collapse(field('nav', 'logo'))),
  'nav.about': esc(collapse(field('nav', 'about'))),
  'nav.work': esc(collapse(field('nav', 'work'))),
  'nav.contact': esc(collapse(field('nav', 'contact'))),
  'hero.eyebrow': esc(collapse(field('hero', 'eyebrow'))),
  'hero.heading': heroHeading(field('hero', 'heading')),
  'hero.sub': esc(collapse(field('hero', 'sub'))),
  'hero.cta': esc(collapse(field('hero', 'cta'))),
  'about.label': esc(collapse(field('about', 'label'))),
  'about.heading': esc(collapse(field('about', 'heading'))),
  'about.photo_alt': esc(collapse(field('about', 'photo_alt'))),
  'about.bio': bioParagraphs(field('about', 'bio')),
  SKILL_CARDS: skillCards(),
  'work.label': esc(collapse(field('work', 'label'))),
  'work.heading': esc(collapse(field('work', 'heading'))),
  WORK_CARDS: workCards(),
  'filters.all': esc(collapse(field('filters', 'all'))),
  'filters.ld': esc(collapse(field('filters', 'ld'))),
  'filters.product': esc(collapse(field('filters', 'product'))),
  'filters.experiments': esc(collapse(field('filters', 'experiments'))),
  'filters.personal': esc(collapse(field('filters', 'personal'))),
  'insights.label': esc(collapse(field('insights', 'label'))),
  'insights.heading': esc(collapse(field('insights', 'heading'))),
  'insights.intro': esc(collapse(field('insights', 'intro'))),
  'insights.caption': esc(collapse(field('insights', 'caption'))),
  'insights.course_label': esc(collapse(field('insights', 'course_label'))),
  'insights.course_intro': esc(collapse(field('insights', 'course_intro'))),
  'contact.label': esc(collapse(field('contact', 'label'))),
  'contact.heading': esc(collapse(field('contact', 'heading'))),
  'contact.sub': esc(collapse(field('contact', 'sub'))),
  'contact.button': esc(collapse(field('contact', 'button'))),
  'contact.email': esc(collapse(field('contact', 'email'))),
  'contact.linkedin': esc(collapse(field('contact', 'linkedin'))),
  'contact.resume_label': esc(collapse(field('contact', 'resume_label'))),
  'contact.resume_file': esc(collapse(field('contact', 'resume_file'))),
  'footer.text': esc(collapse(field('footer', 'text'))),
};

let out = template;
for (const [token, value] of Object.entries(replacements)) {
  out = out.split(`{{${token}}}`).join(value);
}

// Fail loudly if any token went unfilled (typo in template or content).
const leftover = out.match(/\{\{[^}]+\}\}/g);
if (leftover) {
  console.error('ERROR: unfilled tokens remain:', [...new Set(leftover)].join(', '));
  process.exit(1);
}

fs.writeFileSync(path.join(ROOT, 'index.html'), out);
console.log(`Built index.html — ${data.work.items.length} work cards, ${data.skills.items.length} skill cards.`);
