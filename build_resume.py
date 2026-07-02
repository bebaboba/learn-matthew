#!/usr/bin/env python3
"""Generate Matthew_Anderson_Resume.pdf, styled to match learnmatthew.com.

Requires fpdf2:  python3 -m pip install --user fpdf2
Uses the site's actual webfonts (DM Serif Display, DM Sans, JetBrains Mono) —
see FONT_DIR below. Regenerate after editing content: python3 build_resume.py

NOTE: This résumé is PUBLIC. Keep it sanitized — no internal metrics, system
names, project codenames, or anything that wouldn't belong on learnmatthew.com.
"""

import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

FONT_DIR = os.path.expanduser(
    "~/.claude/jobs/570681a0/tmp/fonts"
)

# ── Content (mirrors job-search/files/resume-content-curriculum.md) ───────────
NAME = "Matthew Anderson"
TAGLINE = "Content & Curriculum Leadership · Learning Science · AI-Native Production"
CONTACT = "San Francisco, CA · matthewsfo@gmail.com · linkedin.com/in/picocat · learnmatthew.com"

SUMMARY = (
    "I build content systems, not just content. A decade turning technical and creative subject "
    "matter into experiences that actually teach — and I don't accept engagement metrics as a "
    "stand-in for whether anyone actually got better. At Apple, owned the learning platform behind "
    "145+ internal teams — none of which report to me — set the quality bar that let those teams "
    "author independently without it turning to noise, and coached instructional designers away "
    "from click-through courseware toward learning that respects the learner's time and "
    "intelligence. Now I am experimenting with building AI-native learning products using Claude — "
    "an adaptive tutor and an interactive portfolio are my first forays. Check them out on "
    "learnmatthew.com."
)

BELIEVE = [
    "Good content measures whether people got better, not whether they came back. Streaks, "
    "completion rates, and time-on-platform tell you people showed up — they don't tell you "
    "anyone learned anything, and I've seen those two things treated as the same thing too many "
    "times. I design for people to build their own ability to reason through something new, "
    "including through ambiguity, not just get through it. It's the Freire distinction — education "
    "as the practice of freedom, not rote transmission — and it holds whether I'm designing a "
    "single classroom session or a platform-wide standard. I hold a hard line against hollow "
    "engagement either way.",
    "I also believe taste doesn't scale by being protected — it scales by being encoded. "
    "Accessibility should be a beginning to design, not a last-minute consideration. Twenty-page "
    "courses completed in two minutes should be a signal of poor quality, not lack of engagement. "
    "We must meet learners where they are, respect their time, and strive to create ah-ha "
    "experiences that enable people to do their best work.",
]

EXPERIENCE = [
    {
        "title": "L&D Producer · Learning Platform Product Owner",
        "org": "Apple University — San Francisco, CA",
        "dates": "2021 – Present",
        "intro": (
            "Owned the content standards, production model, and platform behind Apple's internal "
            "learning ecosystem — 145+ distinct teams, each a world unto itself with its own "
            "mission, subject matter, and learners, and none of them reporting to me. Apple has a "
            "phrase for that kind of leadership: accountability without control."
        ),
        "bullets": [
            ("Set and defended the quality bar at scale.", "Built a distributed authoring model that let 145+ teams produce their own learning — but defined content standards and quality governance precise enough that self-serve scale didn't become noise."),
            ("Coached the craft.", "Pushed instructional designers away from click-through, compliance-style courseware toward experiences grounded in adult learning theory that meet learners where they are. The recurring fight: functional enablement that stays substantive instead of going hollow."),
            ("Owned learning measurement.", "Built a feedback system — post-engagement surveys on a structured cadence, aggregated into a dashboard alongside adoption and support signals — and closed the loop by reporting back to teams and leadership and feeding it into the product roadmap."),
            ("Held the line on data privacy.", "As analytics modernization created pressure for broader access to learner data, navigated the tension between what provider teams wanted to see and Apple's minimal-collection values, and implemented privacy-conscious governance instead of just opening up access."),
            ("Built the function from nothing.", "No precedent, no template — architected the content and platform operation as the work demanded it, in a high-ambiguity environment."),
        ],
    },
    {
        "title": "Creative Pro / Lead Creative",
        "org": "Apple — Retail, San Francisco, CA",
        "dates": "2012 – 2021",
        "intro": (
            "Face-of-Apple educator across formats and audiences — the foundation of a conviction "
            "that teaching lands only when it starts with the person, not the product."
        ),
        "bullets": [
            (None, "Taught technical and creative subjects — coding, video, audio, photography — to thousands of learners from first-timers to working professionals, adapting the same material across radically different levels."),
            ("Built and owned an external cultural partnership.", "A two-year monthly Art Walk series (2018–2020) with the Bellevue Arts Museum — built the relationship end-to-end, planned each session, and led public groups who drew, sketched, and photographed the collection using Apple technology. Ran for two years, until COVID ended it, because the format was simple: hand people real tools and real art, and get out of the way."),
            (None, "Ran coding sessions for K–12 school groups across multiple districts; mentored junior team members and contributed to regional training initiatives."),
        ],
    },
    {
        "title": "Store Leader & Market Training Lead",
        "org": "Starbucks — Seattle, WA",
        "dates": "2004 – 2012",
        "intro": None,
        "bullets": [
            (None, "Designed and delivered multi-unit training curriculum across a regional market — building materials adopted market-wide and measuring outcomes against operational KPIs."),
            (None, "As Store Leader: led a team of 25+ and owned full P&L. Early, formal people-leadership foundation."),
            (None, "Drove Lean Thinking adoption across the Portland and Seattle markets, and learned firsthand the tension between pride in your work and standardizing it. It's a balance I still think about anytime I'm trying to scale quality."),
        ],
    },
    {
        "title": "Gallery Coordinator",
        "org": "Viking Union Gallery, Western Washington University — Bellingham, WA",
        "dates": "2002 – 2004",
        "intro": None,
        "bullets": [
            (None, "Curated and produced international exhibitions; managed public programming and stakeholder relationships at a mission-driven arts institution — early training in audience-centered design."),
        ],
    },
]

PROJECTS = [
    {
        "title": "Adaptive Tutor",
        "url": "adaptive-tutor-ruddy.vercel.app",
        "year": "2026",
        "desc": (
            "My take on what an adaptive AI tutor should be. A Claude-powered tutor where every "
            "inference — engagement, frustration, confusion, intent — is shown to the learner in "
            "real time with its confidence level (capped below 100% on purpose) and the signals "
            "behind it; the learner can read, contest, and override any conclusion. Building it "
            "opened up three research threads I've kept developing: persistent adaptive tutoring, "
            "privacy-preserving personalization via federated learning, and intent-aware learning "
            "design. Built with Claude as production partner. Stack: React, Vite, Tailwind, "
            "Anthropic API, xAPI → LRS."
        ),
    },
    {
        "title": "Learn Matthew AI",
        "url": "learnmatthew.com",
        "year": "2026",
        "desc": (
            "Interactive AI-guided portfolio with streaming Claude responses, persona-based "
            "adaptive UX, and anonymous xAPI analytics — proof that personalization doesn't "
            "require harvesting personal data. It's also built on the same AI-native technology a "
            "modern learning program should run on."
        ),
    },
]

CRAFT = [
    ("Leadership", "Leading through influence across 145+ non-reporting teams, accountability without control, cross-functional coaching, org design input"),
    ("Content & Curriculum", "Instructional design, curriculum architecture, quality standards, multi-format production (written, interactive), editorial judgment"),
    ("Learning Science", "Adult learning theory, ADDIE, Kirkpatrick evaluation, learning measurement & instrumentation, SCORM/xAPI"),
    ("AI-Native Production", "Building content with Claude, Anthropic API, prompt engineering, human-vs-AI line-drawing, adaptive/tutoring system design"),
    ("Systems & Scale", "Distributed authoring, 0-to-1 platform building, production workflow design, self-serve enablement at scale"),
    ("Measurement", "Dashboards, adoption analytics, feedback cadence design, SQL, Tableau, Snowflake, privacy-conscious data governance"),
]

EDUCATION = [
    ("B.A., Integrated Social Sciences — University of Washington", "", "Art History minor; coursework in Communications, Computer Science, Mixed Media Studio Arts."),
    ("Fine Art & Design Studies — Western Washington University", "", ""),
]

CERTS = "Kirkpatrick Bronze Level — Kirkpatrick Partners, 2025"

# ── Palette + type, lifted straight from css/style.css ────────────────────────
BG      = (246, 242, 234)  # --color-bg
SURFACE = (255, 253, 249)  # --color-surface
TEXT    = (33, 31, 27)     # --color-text
MUTED   = (111, 106, 96)   # --color-muted
ACCENT  = (191, 106, 72)   # --color-accent
BORDER  = (226, 219, 204)  # --color-border


class ResumePDF(FPDF):
    def header(self):
        self.set_fill_color(*BG)
        self.rect(0, 0, self.w, self.h, style="F")
        if self.page_no() > 1:
            self.set_xy(self.l_margin, 24)
            self.set_font("Mono", "", 8)
            self.set_text_color(*MUTED)
            self.cell(0, 10, "MATTHEW ANDERSON — RESUME", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_y(46)

    def footer(self):
        self.set_y(-32)
        self.set_font("Mono", "", 7.5)
        self.set_text_color(*MUTED)
        self.cell(0, 10, f"{self.page_no()}", align="C")


pdf = ResumePDF(orientation="P", unit="pt", format="Letter")
pdf.set_auto_page_break(auto=True, margin=46)
pdf.set_margins(56, 46, 56)

pdf.add_font("Serif", "", f"{FONT_DIR}/DMSerifDisplay-Regular.ttf")
pdf.add_font("Serif", "I", f"{FONT_DIR}/DMSerifDisplay-Italic.ttf")
pdf.add_font("Sans", "", f"{FONT_DIR}/DMSans-Regular.ttf")
pdf.add_font("Sans", "B", f"{FONT_DIR}/DMSans-SemiBold.ttf")
pdf.add_font("SansMed", "", f"{FONT_DIR}/DMSans-Medium.ttf")
pdf.add_font("Mono", "", f"{FONT_DIR}/JetBrainsMono-Medium.ttf")
pdf.add_font("Mono", "B", f"{FONT_DIR}/JetBrainsMono-SemiBold.ttf")

pdf.add_page()
CW = pdf.w - pdf.l_margin - pdf.r_margin


def rule():
    y = pdf.get_y()
    pdf.set_draw_color(*BORDER)
    pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
    pdf.ln(9)


def section(label):
    rule()
    pdf.set_font("Mono", "B", 9)
    pdf.set_text_color(*ACCENT)
    spaced = " ".join(label.upper())  # crude letter-spacing stand-in
    pdf.cell(0, 11, spaced, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)


# Header
pdf.set_font("Serif", "", 27)
pdf.set_text_color(*ACCENT)
pdf.cell(0, 30, NAME, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("Sans", "", 10.5)
pdf.set_text_color(*TEXT)
pdf.cell(0, 14, TAGLINE, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("Mono", "", 8.5)
pdf.set_text_color(*MUTED)
pdf.cell(0, 14, CONTACT, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(4)

# Summary
section("Summary")
pdf.set_font("Sans", "", 9.7)
pdf.set_text_color(*TEXT)
pdf.multi_cell(CW, 12.5, SUMMARY)
pdf.ln(2)

# What I believe
section("What I Believe About Teaching")
pdf.set_font("Sans", "", 9.7)
for i, para in enumerate(BELIEVE):
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(CW, 12.5, para)
    if i < len(BELIEVE) - 1:
        pdf.ln(3)
pdf.ln(2)

# Experience
section("Experience")
for i, role in enumerate(EXPERIENCE):
    pdf.set_font("Sans", "B", 10.5)
    pdf.set_text_color(*TEXT)
    pdf.cell(CW * 0.72, 13, role["title"], new_x=XPos.LMARGIN, new_y=YPos.TOP)
    pdf.set_font("SansMed", "", 9)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 13, role["dates"], align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("SansMed", "", 9)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 12, role["org"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)
    if role["intro"]:
        pdf.set_font("Sans", "", 9)
        pdf.set_text_color(*MUTED)
        pdf.multi_cell(CW, 11.5, role["intro"])
        pdf.ln(2)
    pdf.set_font("Sans", "", 9.2)
    indent = pdf.l_margin + 12
    for lead, rest in role["bullets"]:
        y0 = pdf.get_y()
        pdf.set_fill_color(*ACCENT)
        pdf.ellipse(pdf.l_margin + 2, y0 + 4.5, 3, 3, style="F")
        pdf.set_left_margin(indent)
        pdf.set_x(indent)
        if lead:
            pdf.set_font("Sans", "B", 9.2)
            pdf.set_text_color(*TEXT)
            pdf.write(11.5, lead + " ")
            pdf.set_font("Sans", "", 9.2)
            pdf.set_text_color(*MUTED)
            pdf.write(11.5, rest)
        else:
            pdf.set_font("Sans", "", 9.2)
            pdf.set_text_color(*MUTED)
            pdf.write(11.5, rest)
        pdf.ln(11.5)
        pdf.set_left_margin(pdf.l_margin - 12)
        pdf.ln(1)
    if i < len(EXPERIENCE) - 1:
        pdf.ln(3)
pdf.ln(1)

# AI-native learning projects
section("AI-Native Learning Projects")
for i, proj in enumerate(PROJECTS):
    pdf.set_font("Serif", "", 12)
    pdf.set_text_color(*TEXT)
    pdf.cell(CW * 0.72, 15, proj["title"], new_x=XPos.LMARGIN, new_y=YPos.TOP)
    pdf.set_font("Mono", "", 8.5)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 15, proj["year"], align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Mono", "", 8.5)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 11, proj["url"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)
    pdf.set_font("Sans", "", 9.2)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(CW, 11.8, proj["desc"])
    if i < len(PROJECTS) - 1:
        pdf.ln(3)
pdf.ln(1)

# Craft & capabilities
section("Craft & Capabilities")
for cat, items in CRAFT:
    y0 = pdf.get_y()
    pdf.set_font("Sans", "B", 9.2)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(130, 11.8, cat, new_x=XPos.LEFT, new_y=YPos.TOP)
    pdf.set_xy(pdf.l_margin + 130, y0)
    pdf.set_font("Sans", "", 9.2)
    pdf.set_text_color(*MUTED)
    pdf.multi_cell(CW - 130, 11.8, items, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2.5)

# Education & certification
section("Education & Certification")
for school, dates, detail in EDUCATION:
    pdf.set_font("Sans", "B", 10)
    pdf.set_text_color(*TEXT)
    pdf.cell(CW * 0.72, 14, school, new_x=XPos.LMARGIN, new_y=YPos.TOP)
    if dates:
        pdf.set_font("SansMed", "", 9.5)
        pdf.set_text_color(*MUTED)
        pdf.cell(0, 14, dates, align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    else:
        pdf.ln(14)
    if detail:
        pdf.set_font("Sans", "", 9.5)
        pdf.set_text_color(*MUTED)
        pdf.multi_cell(CW, 13, detail, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)
pdf.set_font("Sans", "", 10)
pdf.set_text_color(*TEXT)
pdf.multi_cell(CW, 14, CERTS)

pdf.output("Matthew_Anderson_Resume.pdf")
print("Wrote Matthew_Anderson_Resume.pdf —", pdf.page_no(), "page(s)")
