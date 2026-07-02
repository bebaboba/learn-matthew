#!/usr/bin/env python3
"""Generate Matthew_Anderson_Resume.pdf from the sanitized content below.

Requires fpdf2:  python3 -m pip install --user fpdf2
Regenerate after editing content:  python3 build_resume.py

NOTE: This résumé is PUBLIC. Keep it sanitized — no internal metrics, system
names, project codenames, or anything that wouldn't belong on learnmatthew.com.
"""

from fpdf import FPDF
from fpdf.enums import XPos, YPos

# ── Content (edit here) ───────────────────────────────────────────────────────
NAME = "Matthew Anderson"
TAGLINE = "Content & Curriculum Leadership  ·  Learning Science · AI-Native Production"
CONTACT = "San Francisco, CA  ·  matthewsfo@gmail.com  ·  linkedin.com/in/picocat  ·  learnmatthew.com"

SUMMARY = (
    "Learning leader who builds content systems, not just content. A decade turning technical and "
    "creative subject matter into experiences that actually teach -- and a refusal to accept engagement "
    "metrics as a proxy for whether anyone got better. At Apple, owned the learning platform behind "
    "145+ internal teams, set the quality bar that let those teams author independently without it "
    "turning to noise, and coached instructional designers away from click-through courseware toward "
    "learning that respects the learner's time and intelligence. Now building AI-native learning "
    "products with Claude -- an adaptive tutor and an interactive portfolio -- that encode that craft "
    "into systems rather than guarding it."
)

EXPERIENCE = [
    {
        "title": "L&D Producer, Learning Platform Product Owner",
        "org": "Apple University — San Francisco, CA",
        "dates": "2021 – Present",
        "bullets": [
            "Set and defended the quality bar for a distributed authoring model that let 145+ teams produce their own learning -- precise enough that self-serve scale didn't become noise.",
            "Coached instructional designers away from click-through, compliance-style courseware toward experiences grounded in adult learning theory that meet learners where they are.",
            "Built a learning measurement system -- a structured feedback cadence aggregated into a dashboard alongside adoption and support signals -- and closed the loop by feeding results back into the roadmap.",
            "Cut time-to-productivity 50%+ for newly onboarded teams by replacing fragmented manual workflows with a unified self-serve onboarding experience.",
            "Navigated the tension between stakeholder demand for broader access to learner data and privacy-conscious governance, implementing access controls with security and data engineering teams.",
            "Architected the content and platform function from nothing -- no precedent, no template -- in a high-ambiguity environment.",
        ],
    },
    {
        "title": "Creative Pro / Lead Creative",
        "org": "Apple — Retail",
        "dates": "2012 – 2021",
        "bullets": [
            "Taught technical and creative subjects -- coding, video, audio, photography -- to thousands of learners from first-timers to working professionals, adapting the same material across radically different levels.",
            "Built and owned an external cultural partnership: a two-year monthly Art Walk series (2018-2020) with the Bellevue Arts Museum, planning sessions and leading public groups who used Apple technology for creative practice.",
            "Ran coding sessions for K-12 school groups across multiple districts; mentored junior team members and contributed to regional training initiatives.",
        ],
    },
    {
        "title": "Store Leader & Market Training Lead",
        "org": "Starbucks — Seattle, WA",
        "dates": "2004 – 2012",
        "bullets": [
            "Designed and delivered multi-unit training curriculum across a regional market -- building materials adopted market-wide and measuring outcomes against operational KPIs.",
            "As Store Leader, owned full P&L and led a team of 25+.",
            "Drove Lean Thinking adoption across the Portland and Seattle markets, and learned firsthand the tension between scaling a system and preserving what made it worth scaling.",
        ],
    },
    {
        "title": "Gallery Coordinator",
        "org": "Viking Union Gallery, Western Washington University — Bellingham, WA",
        "dates": "2002 – 2004",
        "bullets": [
            "Curated and produced international exhibitions; managed public programming and stakeholder relationships at a mission-driven arts institution -- early training in audience-centered design.",
        ],
    },
]

SKILLS = [
    ("Content & Curriculum", "Instructional design, curriculum architecture, quality standards, multi-format production (written, interactive), editorial judgment"),
    ("Learning Science", "Adult learning theory, ADDIE, Kirkpatrick evaluation, learning measurement & instrumentation, SCORM / xAPI"),
    ("AI-Native Production", "Building content with Claude, Anthropic API, prompt engineering, human-vs-AI line-drawing, adaptive/tutoring system design"),
    ("Systems & Scale", "Distributed authoring, 0-to-1 platform building, production workflow design, self-serve enablement at scale"),
    ("Measurement", "Dashboards, adoption analytics, feedback cadence design, SQL, Tableau, Snowflake, privacy-conscious data governance"),
]

PROJECTS = [
    {
        "title": "Adaptive Tutor",
        "url": "adaptive-tutor-ruddy.vercel.app",
        "year": "2026",
        "desc": "A working argument for what an adaptive AI tutor should be. Every inference the system makes -- engagement, frustration, confusion, intent -- is shown to the learner in real time with its confidence capped below 100% on purpose, and the signals behind it. The learner can read, contest, and override any conclusion. Stack: React, Vite, Tailwind, Anthropic API, xAPI -> LRS.",
    },
    {
        "title": "Learn Matthew AI",
        "url": "learn-matthew-ai.vercel.app",
        "year": "2026",
        "desc": "Interactive AI-guided portfolio with streaming Claude responses, persona-based adaptive UX, and anonymous xAPI analytics -- demonstrating that personalization doesn't require harvesting personal data.",
    },
]

EDUCATION = [
    ("B.A., Integrated Social Sciences — University of Washington", "2017 – 2018",
     "Art History minor; coursework in Communications, Computer Science, and Mixed Media Studio Arts."),
    ("Fine Art & Design studies — Western Washington University", "1999 – 2004", ""),
]

CERTS = "Kirkpatrick Bronze Level Certification — Kirkpatrick Partners (2025)"

# ── Style ─────────────────────────────────────────────────────────────────────
ACCENT = (200, 149, 108)   # #C8956C
DARK = (26, 26, 24)        # #1a1a18
MUTED = (107, 107, 104)    # #6b6b68
BORDER = (210, 205, 196)

# Core PDF fonts are latin-1 only; map the few typographic chars we use.
def t(s):
    return (s.replace("—", "-").replace("–", "-")
             .replace("’", "'").replace("“", '"').replace("”", '"'))

pdf = FPDF(orientation="P", unit="pt", format="Letter")
pdf.set_auto_page_break(auto=True, margin=40)
pdf.set_margins(54, 40, 54)
pdf.add_page()
CW = pdf.w - pdf.l_margin - pdf.r_margin

def section(label):
    pdf.ln(5)
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 13, t(label.upper()), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    y = pdf.get_y() + 1
    pdf.set_draw_color(*BORDER)
    pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
    pdf.ln(3)

# Header
pdf.set_font("Helvetica", "B", 23)
pdf.set_text_color(*ACCENT)
pdf.cell(0, 26, t(NAME), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("Helvetica", "", 10.5)
pdf.set_text_color(*DARK)
pdf.cell(0, 15, t(TAGLINE), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(*MUTED)
pdf.cell(0, 14, t(CONTACT), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Summary
section("Summary")
pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(*DARK)
pdf.multi_cell(CW, 12.5, t(SUMMARY))

# Experience
section("Experience")
for role in EXPERIENCE:
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(*DARK)
    pdf.cell(CW * 0.72, 14, t(role["title"]), new_x=XPos.LMARGIN, new_y=YPos.TOP)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 14, t(role["dates"]), align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "I", 9.5)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 13, t(role["org"]), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)
    pdf.set_font("Helvetica", "", 9.7)
    for b in role["bullets"]:
        y0 = pdf.get_y()
        pdf.set_fill_color(*ACCENT)
        pdf.ellipse(pdf.l_margin + 2, y0 + 4.5, 3, 3, style="F")
        pdf.set_xy(pdf.l_margin + 12, y0)
        pdf.set_text_color(*DARK)
        pdf.multi_cell(CW - 12, 11.5, t(b), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)

# Projects
section("Projects")
for proj in PROJECTS:
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(*DARK)
    pdf.cell(CW * 0.72, 14, t(proj["title"]), new_x=XPos.LMARGIN, new_y=YPos.TOP)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 14, t(proj["year"]), align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "I", 9.5)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 13, t(proj["url"]), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)
    pdf.set_font("Helvetica", "", 9.7)
    pdf.set_text_color(*DARK)
    pdf.multi_cell(CW, 11.5, t(proj["desc"]), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)

# Skills
section("Skills")
for cat, items in SKILLS:
    pdf.set_font("Helvetica", "B", 9.7)
    pdf.set_text_color(*DARK)
    pdf.cell(120, 11.8, t(cat), new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font("Helvetica", "", 9.7)
    pdf.set_text_color(*MUTED)
    pdf.multi_cell(CW - 120, 11.8, t(items), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Education
section("Education")
for school, dates, detail in EDUCATION:
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(*DARK)
    pdf.cell(CW * 0.72, 14, t(school), new_x=XPos.LMARGIN, new_y=YPos.TOP)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 14, t(dates), align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    if detail:
        pdf.set_font("Helvetica", "", 9.5)
        pdf.set_text_color(*MUTED)
        pdf.multi_cell(CW, 13, t(detail), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)

# Certifications
section("Certifications")
pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(*DARK)
pdf.multi_cell(CW, 13.5, t(CERTS))

pdf.output("Matthew_Anderson_Resume.pdf")
print("Wrote Matthew_Anderson_Resume.pdf —", pdf.page_no(), "page(s)")
