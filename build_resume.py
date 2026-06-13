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
TAGLINE = "L&D Platform Producer  ·  Platforms · Community · Analytics"
CONTACT = "San Francisco, CA  ·  matthewsfo@gmail.com  ·  linkedin.com/in/picocat  ·  learnmatthew.com"

SUMMARY = (
    "Learning and enablement leader who builds the platforms, communities, and data behind how "
    "people learn. At Apple, grew an internal learning platform to serve teams across the "
    "organization, fostered the community that made it thrive, and built the analytics that proved "
    "its impact. Part designer, part builder, part leader, with roots in product management and the arts."
)

EXPERIENCE = [
    {
        "title": "L&D Producer, Learning Platform",
        "org": "Apple University — San Francisco, CA",
        "dates": "2021 – Present",
        "bullets": [
            "Product manager for Apple's internal global learning platform across iOS, macOS, and web — owning roadmap, cross-functional delivery, and adoption for a worldwide workforce.",
            "Grew the platform to serve teams across the organization without expanding the support team, through automation, documentation, and a self-service enablement curriculum.",
            "Built the community and enablement systems — workshops, office hours, best-practice guides — that let content teams publish independently.",
            "Led an analytics modernization connecting learning activity to real-time insight and AI tooling.",
            "Architected the function from the ground up in a high-ambiguity environment with no existing playbook.",
        ],
    },
    {
        "title": "Creative Pro / Lead Creative",
        "org": "Apple — Retail",
        "dates": "2012 – 2021",
        "bullets": [
            "Lead customer educator and product expert at flagship locations, delivering technical and creative training to thousands of customers.",
            "Made complex technical concepts accessible and actionable; contributed to regional training initiatives and mentored junior team members.",
        ],
    },
    {
        "title": "Store Leader & Market Training Lead",
        "org": "Starbucks — Seattle, WA",
        "dates": "2004 – 2012",
        "bullets": [
            "Designed and delivered multi-unit training programs across a regional portfolio; built curriculum and measured outcomes against operational KPIs.",
            "As Store Leader, owned full P&L and led a team of 25+.",
        ],
    },
    {
        "title": "Gallery Coordinator",
        "org": "Viking Union Gallery, Western Washington University — Bellingham, WA",
        "dates": "2002 – 2004",
        "bullets": [
            "Curated and produced international exhibitions; managed public programming and stakeholder relationships — an early foundation in audience-centered experience design.",
        ],
    },
]

SKILLS = [
    ("Platform & Product", "0-to-1 platform building, roadmap & adoption strategy, multi-surface (iOS · macOS · web), product discovery"),
    ("Learning & Enablement", "Instructional design, community management, onboarding frameworks, enablement curriculum, SCORM / xAPI, Kirkpatrick model"),
    ("Data & Analytics", "SQL, Tableau, Snowflake, dashboards & curated data sources, AI-accessible data pipelines"),
    ("Design & Tools", "Adobe Creative Suite, Figma, Miro"),
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
    pdf.ln(6)
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 13, t(label.upper()), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    y = pdf.get_y() + 1
    pdf.set_draw_color(*BORDER)
    pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
    pdf.ln(4)

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
pdf.multi_cell(CW, 13.5, t(SUMMARY))

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
        pdf.multi_cell(CW - 12, 12, t(b), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)

# Skills
section("Skills")
for cat, items in SKILLS:
    pdf.set_font("Helvetica", "B", 9.7)
    pdf.set_text_color(*DARK)
    pdf.cell(120, 13, t(cat), new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font("Helvetica", "", 9.7)
    pdf.set_text_color(*MUTED)
    pdf.multi_cell(CW - 120, 13, t(items), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

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
