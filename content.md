# learnmatthew.com — site copy
# Edit the values below, commit, and push. A GitHub Action rebuilds index.html automatically.
#
# Format:
#   "## section"      groups a section of the page
#   "### Card Title"  starts a card (skills / work)
#   "key: value"      a field; values may span multiple lines (continue until the
#                     next key or heading). A blank line inside a value = new paragraph.
# Lines starting with "#" are comments and are ignored.

## meta
title: Matthew Anderson — Content & Curriculum Leader
description: Portfolio of Matthew Anderson — content & curriculum leader who sets the quality bar for learning at scale, builds AI-native production systems with Claude, and measures whether people actually got better.

## nav
logo: Matthew Anderson
about: About
work: Work
contact: Contact

## hero
eyebrow: Content & Curriculum · Learning Science · AI-Native Production
heading: I build the *content standards*, *quality systems*, and *AI-native workflows* behind learning that actually teaches.
sub: At Apple, I set the quality bar for a learning platform used by 145+ teams, coached the craft that kept it substantive instead of hollow, and built the measurement to prove whether people got better — not whether they came back. Now I'm building AI-native learning products with Claude that encode that craft into systems instead of guarding it.
cta: See my work

## about
label: About
heading: The short version
photo_alt: Matthew Anderson
bio: I'm a content & curriculum leader with a decade turning technical and creative subject matter into experiences that actually teach. My roots are in product management, arts & culture, and direct instruction — which means I approach content the way a craftsperson approaches production: with real editorial taste, a bias for measurement, and a refusal to accept engagement as a proxy for learning.

Over the past decade I've set the content standards and quality bar for a 145+ team learning platform, coached instructional designers away from click-through courseware and toward learning grounded in adult learning theory, and built the feedback systems that prove whether it worked. Alongside that, I've curated international art exhibitions and run a two-year museum partnership teaching creative technology to the public. Now I'm building AI-native learning products with Claude — an adaptive tutor and an interactive portfolio — that put those same standards into systems that scale past what any team could produce by hand.

Based in San Francisco. B.A. Integrated Social Sciences from the University of Washington, with a minor in Art History and coursework in Mixed Media Studio Arts.

## skills
### Content & Curriculum
desc: Instructional design, curriculum architecture, quality standards, multi-format production (written, video, interactive), editorial judgment, coaching teams toward substance over engagement
### Learning Science
desc: Adult learning theory (Freire, ADDIE), Kirkpatrick evaluation, learning measurement & instrumentation, SCORM · xAPI
### AI-Native Production
desc: Building content with Claude, Anthropic API, prompt engineering, human-vs-AI line-drawing, adaptive/tutoring system design
### Systems & Scale
desc: Distributed authoring, 0-to-1 platform building, production workflow design, self-serve enablement across 145+ teams
### Leadership & Measurement
desc: Coaching content teams and instructional designers, direct people management, feedback dashboards, adoption analytics, executive communication

## work
label: Work
heading: Selected projects
### Learn Matthew
category: experiments
tags: Experiment
image: learn-matthew.svg
link: https://learn-matthew-ai.vercel.app
cta: Launch the experience →
desc: An AI-powered interactive portfolio that personalizes the experience based on who you are. Visitors pick a persona and an AI guide walks them through my work — revealing content modules through conversation, not a fixed page layout.
more: Built as an argument, not just a demo: that personalization doesn't require harvesting personal data. Visitors choose a persona and a Claude-powered guide adapts tone and depth accordingly, while every interaction is logged as anonymous xAPI statements — the same measurement discipline I bring to L&D, pointed at my own portfolio this time. React front end, a serverless API streaming Claude responses, Claude as production partner throughout.
stat: React · Vite · Claude API
### Adaptive Tutor (research prototype)
category: experiments
tags: Experiment
image: adaptive-tutor.svg
link: https://adaptive-tutor-ruddy.vercel.app
cta: Try the prototype →
desc: A working argument for what an adaptive AI tutor should be. A learner works a lesson with an AI tutor while a live inspector shows the whole pipeline — behavior → xAPI → inferred state → adaptation — with every inference shown honestly, including its confidence (capped below 100% on purpose) and what drove it. The learner can see, contest, and override what the system infers.
more: The core design bet: an adaptive system should never assert more confidence than its evidence supports, and the learner should always be able to see and challenge its reasoning. The live inspector shows the exact behavioral signals — pacing, hesitation, review patterns — that produced each inferred state, before any adaptation happens. Built solo with Claude as production partner across the full stack: React front end, an xAPI event pipeline into a Learning Record Store, and an inference layer translating raw behavior into pedagogical decisions.
stat: React · Claude · xAPI → LRS · behavior-based inference
### Content Standards for a 145+ Team Platform
category: product
tags: Product, Content
image: learning-platform.svg
desc: Set and defended the quality bar for Apple's internal learning platform — 145+ distinct teams producing their own learning. Defined what "great" meant precisely enough that teams could hit it without me in the room, and coached instructional designers away from click-through, compliance-style courseware toward learning grounded in adult learning theory.
more: The standard wasn't a style guide — it was a small set of testable questions any team could ask before publishing, like whether the content respects the learner's time and whether anyone could actually measure if it worked. Teams that could answer those honestly got out of my way; teams that couldn't got coaching, not a rejection. That's the difference between governing quality and just gatekeeping it.
stat: 145+ teams · Quality bar defined, not just enforced
### Distributed Authoring & Quality Governance
category: product
tags: Product
image: authoring-model.svg
desc: Designed a distributed authoring system that let teams across the organization own their learning programs — establishing content standards, editorial review, and instructional guardrails so self-service scale didn't come at the cost of learning integrity. Speed without quality isn't adoption; it's clutter.
more: Self-serve only works if "good enough to publish" means the same thing to everyone doing the publishing. The system paired lightweight editorial review with clear authoring guardrails so teams could move at their own pace without the platform turning into a pile of unreviewed content. The goal was never to slow teams down — it was to make the fast path and the good path the same path.
stat: Org-wide · Quality-governed self-serve authoring
### Learning Measurement System
category: product
tags: Product, Measurement
image: learning-data.svg
desc: Built the instrumentation to know whether content was actually teaching — post-engagement feedback on a structured cadence, aggregated into a dashboard alongside adoption and support signals — and closed the loop by feeding results back into what got made next. Measurement that changed the content, not decoration on top of it.
more: The dashboard itself was never the point — the loop was. Feedback rolled up alongside adoption and support signals on a regular cadence, then went back to the teams that made the content and into what the platform built next. Content that scored well on completion but poorly on "did this actually help" was a signal to redesign, not a metric to celebrate.
stat: Feedback cadence · Dashboards · Closed-loop into production
### New Team Onboarding Framework
category: ld
tags: L&D
image: onboarding-framework.svg
desc: Replaced fragmented manual training workflows with a unified, self-serve onboarding experience — driving a 50%+ reduction in time-to-productivity for newly onboarded teams across the platform.
more: The old process was tribal knowledge, one-off threads, and whatever the last team happened to write down. Replacing it meant one self-serve path that worked whether a new team's first project shipped in two weeks or two quarters — front-loading the standards and platform mechanics so teams spent their early weeks building content, not discovering the system by trial and error.
stat: 50%+ reduction in time-to-productivity
### Bellevue Arts Museum Partnership
category: ld
tags: L&D, Partnership
image: market-training.svg
desc: Built and owned an external cultural partnership from scratch — a two-year monthly Art Walk series (2018–2020) with the Bellevue Arts Museum. Planned each session and led public groups who drew, sketched, and photographed the collection using Apple technology, translating technical skills into creative practice for a general audience. New audiences for the museum, hands-on creative learning for participants, ended only by COVID.
more: What started as a one-off session turned into two years of monthly programming because the format worked — give people real tools and real art, get out of the way, and let looking closely turn into making something. It's the same instinct behind everything else on this page — the best teaching moments are the ones where the "teacher" mostly sets up the conditions and steps back.
stat: 2-year external partnership · Public audience · Cross-format teaching
### A Philosophy Reading Practice
category: ld
tags: L&D, Personal
image: consolidation.svg
desc: A decade-plus habit of reading philosophy — epistemology, ethics, philosophy of education — not for credential but because it's the actual root of how I think about teaching. Freire's line between education as the practice of freedom and the "banking model" that deposits information into passive recipients isn't classroom theory I picked up for a job; it's the same thinking I bring to an evening with a book. The distance between "what does it mean to understand something" and "what makes a lesson worth a learner's time" is shorter than people think.
more: Epistemology in particular — the question of how we actually know something, versus how we merely feel confident about it — turns out to be the same question underneath most of my measurement work. A completion rate tells you someone finished; it doesn't tell you they understood. Reading philosophy for its own sake, with no professional agenda, is what keeps that distinction sharp instead of theoretical.
stat: Ongoing practice · Epistemology, ethics, philosophy of education
### Teaching Myself Quantum Mechanics
category: ld
tags: L&D, Personal
image: certification.svg
desc: Picked up quantum mechanics during the pandemic — partly to point my attention at something larger than the news, partly because there's no steeper test case for explaining a hard idea well. What kept me in it was watching great science communicators solve the exact problem I solve for a living: making genuinely complex ideas stick. My favorites — [Space Time](https://www.youtube.com/c/pbsspacetime), [Kurzgesagt](https://www.youtube.com/channel/UCsXVk37bltHxD1rDPwtNM8Q), and [ScienceClic](https://www.youtube.com/@ScienceClicEN) — all lean on the same trick: ground the physics in the history of how the thinking evolved, and keep the confusion and awe in instead of editing it out.
more: The pattern I keep noticing across the channels I return to: they don't sand the confusion out of the story. They show you the specific historical moment where physicists were genuinely stuck, let you feel the size of the problem, and only then hand you the resolution. Understanding sticks better when you've felt the weight of the question it's answering — which is the same argument I'd make for teaching almost anything else, not just physics.
stat: Self-directed since 2020 · Science communication as a design problem

## insights
label: Live insights
heading: This page runs on xAPI
intro: Every interaction here is recorded as anonymous xAPI statements to a Learning Record Store, then read back and shown below — a working demonstration of the measurement discipline I bring to content: instrument it, and let the data change what you build next. No personal data is collected; just anonymous, aggregate signals.
caption: Powered by xAPI · anonymous, aggregate data only · refreshes live

## contact
label: Contact
heading: Let's talk
sub: Open to conversations about content & curriculum leadership, learning science, and AI-native education — especially roles at the intersection of teaching craft and AI production systems. Whether you have a role in mind or just want to connect — my inbox is open.
button: Say hello
email: matthewsfo@gmail.com
linkedin: https://linkedin.com/in/picocat
resume_label: Download résumé (PDF)
resume_file: Matthew_Anderson_Resume.pdf

## footer
text: Matthew Anderson · San Francisco
