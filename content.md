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
title: Matthew Anderson — Learning Platforms & Content Leader
description: Portfolio of Matthew Anderson — a learning leader who builds the platforms, content standards, and AI-native systems that make organizational learning actually work, and measures whether people actually got better.

## nav
logo: Matthew Anderson
about: About
work: Work
contact: Contact

## hero
eyebrow: Learning Platforms · Content & Curriculum · AI-Native Production
heading: Twenty years teaching people to *think for themselves* — first in person, now at *platform scale*.
sub: At Apple, Matthew grew an internal learning platform to serve 145+ teams — none of which report to him — set the quality bar that kept it substantive instead of hollow, and built the measurement to prove whether people got better, not whether they came back. Now he's experimenting at the intersection of AI and learning with Claude, encoding that craft into systems instead of guarding it.
cta: See his work

## about
label: About
heading: The short version
photo_alt: Matthew Anderson
bio: Matthew is a learning leader with a decade turning technical and creative subject matter into platforms and content systems that actually teach. His roots are in product management, arts & culture, and direct instruction — which means he approaches the work the way a craftsperson approaches production: with real editorial taste, a bias for measurement, and a refusal to accept engagement as a proxy for learning.

He learned to lead the direct way first: running a Starbucks store with a team that reported to him, then a market-level role teaching Lean Thinking to store leaders who didn't. Over the past decade he's grown and set the content standards for a 145+ team learning platform — none of which report to him, leadership by influence rather than authority. He coached instructional designers away from click-through courseware and toward learning grounded in adult learning theory, and built the feedback systems that prove whether it worked. Alongside that, he's curated international art exhibitions and run a two-year museum partnership teaching creative technology to the public. Now he's experimenting at the intersection of AI and learning with Claude — an adaptive tutor and an interactive portfolio — putting those same standards into systems that scale past what any team could produce by hand.

Based in San Francisco. B.A. Integrated Social Sciences from the University of Washington, with a minor in Art History and coursework in Mixed Media Studio Arts.

## skills
### Learning Platforms & Product
desc: Multi-surface platform strategy (iOS · macOS · web), roadmapping, product discovery, distributed authoring models, self-serve enablement across 145+ teams, adoption metrics
### Content & Curriculum
desc: Instructional design, curriculum architecture, quality standards, multi-format production (written, video, interactive), editorial judgment, coaching teams toward substance over engagement
### Learning Science
desc: Adult learning theory (Freire, ADDIE), Kirkpatrick evaluation, learning measurement & instrumentation, SCORM · xAPI
### AI-Native Production
desc: Building content with Claude, Anthropic API, prompt engineering, human-vs-AI line-drawing, adaptive/tutoring system design
### Leadership & Measurement
desc: Leading through influence across non-reporting teams, coaching content creators and instructional designers, direct people management, feedback dashboards, adoption analytics, executive communication

## work
label: Work
heading: Selected projects
### Learn Matthew
category: experiments
tags: Experiment
image: learn-matthew.svg
link: https://learn-matthew-ai.vercel.app
cta: Launch the experience →
desc: An AI-powered interactive portfolio that personalizes the experience based on who you are. Visitors pick a persona and an AI guide walks them through his work — revealing content modules through conversation, not a fixed page layout.
more: Built as an argument, not just a demo: that personalization doesn't require harvesting personal data. Visitors choose a persona and a Claude-powered guide adapts tone and depth accordingly, while every interaction is logged as anonymous xAPI statements — the same measurement discipline he brings to L&D, pointed at his own portfolio this time. React front end, a serverless API streaming Claude responses, Claude as production partner throughout.
stat: React · Vite · Claude API
### Adaptive Tutor (research prototype)
category: experiments
tags: Experiment
image: adaptive-tutor.svg
link: https://adaptive-tutor-ruddy.vercel.app
cta: Try the prototype →
desc: A working argument for what an adaptive AI tutor should be. A learner works a lesson with an AI tutor while a live inspector shows the whole pipeline — behavior → xAPI → inferred state → adaptation — with every inference shown honestly, including its confidence (capped below 100% on purpose) and what drove it. The learner can see, contest, and override what the system infers.
more: The core design bet: an adaptive system should never assert more confidence than its evidence supports, and the learner should always be able to see and challenge its reasoning. The live inspector shows the exact behavioral signals — pacing, hesitation, review patterns — that produced each inferred state, before any adaptation happens. Built solo with Claude as production partner across the full stack: React front end, an xAPI event pipeline into a Learning Record Store, and an inference layer translating raw behavior into pedagogical decisions.

Building the prototype opened onto a bigger thesis: most "adaptive" tutors reset with every session. The interesting problem, especially for corporate L&D, is a **persistent adaptive tutor** — a learner-tutor relationship that builds a profile over time instead of starting cold each time someone opens it. That thesis split into three research threads he's kept developing past the prototype itself.

**Thread A — Persistent Adaptive Tutor.** Cognitive load is the easier half to infer: pacing, error rates, time-to-completion, how often someone asks for clarification. The harder half is behavioral and contextual — when a person learns best, whether they need a concrete example before an abstraction or the reverse, whether they thrive on productive struggle or get frustrated by it. That's the same territory Josh Bersin's Dynamic Enablement model points at, and it's where a persistent profile actually earns its keep.

**Thread B — Privacy-Preserving Adaptive Tutoring.** Enterprise data-minimization policy is a real design constraint, not a footnote: a tutor built for a corporate context has to infer learning style and cognitive load from implicit behavioral signals, with minimal explicit data collection. Most of the literature treats privacy and personalization as a trade-off to be balanced — he'd argue that's a genuine research gap, not a settled question. The technical path runs through federated learning (FedProx has shown gains over FedAvg specifically on heterogeneous student data), differential privacy, on-device data locality, and explainability techniques that keep the inference auditable instead of opaque.

**Thread C — Intent-Aware Learning Design.** Not every question deserves the same kind of answer. Sometimes a learner needs a fast, direct answer to finish a task under deadline pressure; sometimes what they actually need is for the knowledge to stick. The system distinguishes a direct-answer mode from a retrieval-practice mode, and flags when a pattern of repeated quick-answer requests might itself be the signal that deeper learning — not just task completion — is what's needed.

Supporting research runs alongside all three threads: NSF-funded work out of AI-ALOE at Georgia Tech, RCT evidence that AI tutoring can outperform traditional instruction in some studies, and federated learning as the concrete technical path for the privacy-preserving angle.
stat: React · Claude · xAPI → LRS · behavior-based inference
### How This Site Ships Itself
category: experiments
tags: Experiment
image: site-pipeline.svg
link: https://github.com/bebaboba/learn-matthew/blob/main/build.js
cta: Read the build script →
desc: This page is itself a content pipeline with a quality gate. Every word lives in one markdown file; a small dependency-free Node script builds it into the page and refuses to ship if anything's broken — it lists the exact unfilled tokens and exits, instead of failing silently.
more: All of the copy here lives in a single file, content.md, in a tiny key:value format anyone could edit. A build script — plain Node, built-in modules only, zero npm packages — parses it and fills a template to produce the page, and the generated HTML is never touched by hand. A GitHub Action rebuilds it on every push that changes the content, template, or script, so the source and the live site can't drift apart. Editing the site is editing markdown.

The design decision that matters most is the failure mode. After the build fills the template, it scans the output for any token it failed to replace — the fingerprint of a typo in the content or the template — and if it finds one, it prints the exact list and refuses to build. That was the deliberate middle path: not a heavyweight CMS, not a "just don't typo it" honor system, but a lightweight pipeline with a loud quality gate. It's the same instinct as the content standards and measurement systems elsewhere on this page, scaled down to a personal site — if content is going to be edited safely, by other people or by future Matthew, the system has to catch mistakes before readers do.
stat: One markdown file · Zero build dependencies · Fails loud by design
### Content Standards for a 145+ Team Platform
category: product
tags: Product, Content
image: learning-platform.svg
desc: Set and defended the quality bar for Apple's internal learning platform — 145+ distinct teams producing their own learning. Defined what "great" meant precisely enough that teams could hit it without him in the room, and coached instructional designers away from click-through, compliance-style courseware toward learning grounded in adult learning theory.
more: The standard wasn't a style guide — it was a small set of testable questions any team could ask before publishing, like whether the content respects the learner's time and whether anyone could actually measure if it worked. Teams that could answer those honestly got out of his way; teams that couldn't got coaching, not a rejection. That's the difference between governing quality and just gatekeeping it.
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
more: The dashboard itself was never the point — the loop was. Feedback rolled up alongside adoption and support signals on a regular cadence, then went back to the teams that made the content and into what got built next. Content that scored well on completion but poorly on "did this actually help" was a signal to redesign, not a metric to celebrate.

That same measurement discipline is what this site demonstrates in miniature. Every visitor interaction here is logged as anonymous xAPI statements to a live Learning Record Store and read back onto the page in the Live insights section below — the same feedback loop, small enough to watch run in real time.
stat: Closed-loop into production · xAPI-based measurement · Live demo on this page
### New Team Onboarding Framework
category: ld
tags: L&D
image: onboarding-framework.svg
desc: Replaced an onboarding process that took hours of live training per team plus a week or more of backend setup with a unified, self-serve experience — driving a 50%+ reduction in time-to-productivity for newly onboarded teams across the platform.
more: The old process was white-glove by brute force: several hours of live, one-on-one training walking each new provider through the system, while the backend onboarding ran at least a week in parallel. The replacement made the entire path self-service, anchored to weekly office hours, with a single 30-minute one-to-one preserved for each new team — the white-glove touch kept where it earns its keep, not spread across the whole process.

The other deliberate move: from day one, new teams are pointed at each other and at the more experienced members of the community, so the platform team stopped being the only place answers lived. Front-loading the standards and platform mechanics meant teams spent their early weeks building content, not discovering the system by trial and error.
stat: 50%+ reduction in time-to-productivity · Hours of live training → 30 minutes
### Bellevue Arts Museum Partnership
category: ld
tags: L&D, Partnership
image: market-training.svg
desc: Built and owned an external cultural partnership from scratch — a two-year monthly Art Walk series (2018–2020) with the Bellevue Arts Museum. Planned each session and led public groups who drew, sketched, and photographed the collection using Apple technology, translating technical skills into creative practice for a general audience. New audiences for the museum, hands-on creative learning for participants, ended only by COVID.
more: What started as a one-off session turned into two years of monthly programming because the format worked — give people real tools and real art, get out of the way, and let looking closely turn into making something. It's the same instinct behind everything else on this page — the best teaching moments are the ones where the "teacher" mostly sets up the conditions and steps back.
stat: 2-year external partnership · Public audience · Cross-format teaching
### A Philosophy Reading Practice
category: personal
tags: L&D, Personal
image: consolidation.svg
desc: A lifelong habit of reading philosophy — the kind of lifelong where he spent a marathon training block with Plato's Republic in his ears. Epistemology, ethics, philosophy of education: not for credential, but because it's the actual root of how he thinks about teaching. Freire's line between education as the practice of freedom and the "banking model" that deposits information into passive recipients isn't classroom theory he picked up for a job; it's what he reaches for on his own time, unassigned.
more: Epistemology in particular — the question of how we actually know something, versus how we merely feel confident about it — turns out to be the same question underneath most of his measurement work. A completion rate tells you someone finished; it doesn't tell you they understood. The marathon detail is the tell here: nobody assigns the Republic to a training plan. Reading philosophy for its own sake, with no professional agenda, is what keeps that distinction sharp instead of theoretical.
stat: Lifelong habit · Epistemology, ethics, philosophy of education
### From Carburetors to Quarks
category: personal
tags: L&D, Personal
image: certification.svg
desc: A standing habit of taking things apart to see how they actually work — car engines, mechanical clocks — that found its steepest test yet in quantum mechanics during the pandemic. Same itch, different scale. Lately it runs the other direction too: 3D-modeling his own prints, and watching home automation start to absorb LLMs.
more: The pull was never really about physics specifically — it's wanting to know how the thing in front of him works, whether that's a combustion engine, a watch movement, or one of his own 3D prints warping off the bed until he figures out why. Quantum mechanics was just the hardest version of that same question, and the best test case yet for explaining something genuinely hard well.

What kept him in it was watching great science communicators solve the exact problem he solves for a living: making complex ideas stick. His favorites — [Space Time](https://www.youtube.com/c/pbsspacetime), [Kurzgesagt](https://www.youtube.com/channel/UCsXVk37bltHxD1rDPwtNM8Q), and [ScienceClic](https://www.youtube.com/@ScienceClicEN) — all lean on the same trick: ground the physics in the history of how the thinking evolved, and keep the confusion and awe in instead of editing it out.

The pattern he keeps noticing across the channels he returns to: they don't sand the confusion out of the story. They show you the specific historical moment where people were genuinely stuck, let you feel the size of the problem, and only then hand you the resolution. Understanding sticks better once you've felt the weight of the question it's answering — the same argument he'd make for teaching almost anything else, not just physics.

The newest version of the itch is home automation, right at the point where it's starting to absorb LLMs. A house that used to run on if-this-then-that rules is starting to run on models that reason about what you probably want, and he's tinkering with that shift at home — the first hobby that's converged with what he does for a living.
stat: Self-directed curiosity · Cars, clocks, 3D modeling, quantum mechanics, home automation × LLMs

## insights
label: Live insights
heading: This page runs on xAPI
intro: Every interaction here is recorded as anonymous xAPI statements to a Learning Record Store, then read back and shown below — a working demonstration of the measurement discipline he brings to content: instrument it, and let the data change what you build next. No personal data is collected; just anonymous, aggregate signals.
caption: Powered by xAPI · anonymous, aggregate data only · refreshes live

## contact
label: Contact
heading: Let's talk
sub: Matthew is open to conversations about learning platform strategy, content & curriculum leadership, and AI-native production — especially roles at the intersection of teaching craft and AI production systems. Whether you have a role in mind or just want to connect — his inbox is open.
button: Say hello
email: matthewsfo@gmail.com
linkedin: https://linkedin.com/in/picocat
resume_label: Download résumé (PDF)
resume_file: Matthew_Anderson_Resume.pdf

## footer
text: Matthew Anderson · San Francisco
