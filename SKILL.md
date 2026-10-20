---
name: clear-story-presentations
description: "Plan, explain, structure, write, design, critique, or create compelling presentations and reports. Use for PPT/PPTX, slide decks, talks, conference presentations, research seminars, lectures, technical explanations, project/status updates, executive briefings, pitches, demos, workshops, and speaker scripts. Especially use when content is dense, the storyline is weak, slides feel generic or AI-generated, or the user wants a clear, concise, persuasive, memorable explanation. Story and understanding come before slide aesthetics and file generation."
---

# Clear Story Presentations

**Mission:** Make the audience understand the right thing, for the right reason, at the right moment. A presentation is a guided change in the audience's understanding, not a shorter document or a decorative slide collection.

Apply this skill to **spoken presentations, slides, briefings, explanatory talks, demos, and slide-less narratives**. Adjust to context: rigor is essential in research, decisions in executive briefings, understanding in education, and credible action in persuasive talks. Do not impose a TED-style story on every task.

## Non-negotiable order

1. **Understand the communication job** → who, why, what must change, time and format.
2. **Extract the real message** → main answer and evidence; distinguish facts, inferences, choices.
3. **Architect the listener's journey** → questions, dependencies, tension, transitions, pacing.
4. **Edit and explain** → prune, concretize, supply prerequisites and examples.
5. **Storyboard** → each slide has a communicative job and visual proof.
6. **Art-direct and implement** → bespoke but quiet visual system, correct data, editable assets.
7. **Rehearse, render and challenge** → accuracy, comprehension, human voice, projection readiness.

Do not start by generating a visual theme, enumerating chapters, or dumping source headings into slides. If the user requests only critique, outline, talk script or explanation, **stop at the requested deliverable** rather than forcing a PPTX.

## Load references selectively

Read only the files relevant to the current job, not every reference every time:

| When dealing with... | Read |
|---|---|
| Audience, goals, report vs talk, user decisions | `references/01-brief-and-audience.md` |
| Narrative arc, ordering, hooks, transitions | `references/02-story-architecture.md` |
| Teaching an idea, intuition, technical depth, examples | `references/03-explaining-complex-things.md` |
| Deleting clutter, phrasing, authentic voice, non-AI feel | `references/04-editing-and-human-voice.md` |
| Slide composition, typography, visual identity, aesthetics | `references/05-visual-design.md` |
| Charts, scientific figures, mechanisms, causal diagrams | `references/06-visual-evidence.md` |
| Speaker notes, pacing, demo delivery, Q&A | `references/07-delivery-and-rehearsal.md` |
| Research talk, executive briefing, pitch, lecture, update, etc. | `references/08-formats-and-patterns.md` |
| Producing PPTX/PDF/HTML, QA, review or export | `references/09-production-and-qa.md` |
| Sources: studies, guidelines, open-source Skills/repositories | `references/10-research-library.md` |
| Output schemas, intake and storyboard examples | `references/11-templates-and-examples.md` |

When tasks span multiple domains, consult each relevant reference. Follow project/user brand and venue constraints when provided. Respect the user's preferred language.

## Step 1 — Write a one-screen communication brief

Extract from the request and actual source material; ask **at most one critical clarification** if truly impossible to proceed. Otherwise state reasonable working assumptions and move forward.

- **Audience:** knowledge, stakes, skepticism, relationship to speaker; what they do *not* know.
- **Situation:** what prompted the presentation; what changed now.
- **Job:** inform / explain / align / decide / persuade / teach / demonstrate / explore.
- **Desired audience state:** after the talk, they can say, understand, decide, or do ______.
- **Governing message:** one specific, defensible sentence, not a topic.
- **Evidence:** source-backed facts, numbers, cases, visual examples; relevant caveats.
- **Constraints:** time, delivery modality, format, slide independence, language, template, accessibility.

Distinguish **live-talk slides** (visual companion to spoken words) from **read-alone decks** (self-explanatory records). A live talk should not be turned into a wall of readable prose merely to be complete; a read-alone deck needs enough explanation, sources and caveats to stand by itself.

## Step 2 — Extract the message, don't summarize chapters

Read all relevant input before outlining. Convert inputs into a **message inventory**:

`claim | why audience cares | evidence/source | necessary prerequisite | confidence/caveat | importance | keep / appendix / cut`

Then produce:

- **One-sentence answer (main takeaway)** — concrete and falsifiable when possible.
- **Three supporting moves at most by default** — not three arbitrary bullets, but a meaningful decomposition.
- **Key audience question** — the question the talk promises to answer.
- **Knowledge gap** — the thing they must understand before your insight makes sense.
- **Useful action or implication** — when appropriate.

A claim that cannot be linked to a verified source, demonstration, computation, or clearly labeled opinion is not an established fact. Do not invent performance gains, causal explanations, quotes, market sizes, competitors, or citations.

## Step 3 — Build the spine before a single slide

Pick structure based on the **communication job**, rather than imposing a universal template:

- **Decision / recommendation:** answer first → rationale → options/trade-offs → evidence → risks → explicit ask.
- **Research / investigation:** consequential question → obstacle/gap → insight/approach → decisive evidence → interpretation → boundary.
- **Teaching / technical explanation:** audience puzzle → intuition/example → mechanism → worked example → edge case → synthesis.
- **Status / progress:** headline state → evidence of progress → changes/risks → implications → owners and next decisions.
- **Product / demo:** user situation → friction → new workflow → proof by task → limits → next step.
- **Persuasive / keynote:** lived stakes → competing perspective/obstacle → earned change in understanding → credible path forward.

These are starting points, not compulsory section titles. Alternative structures (SCQA, BLUF/Pyramid, problem–solution, before–after–bridge, question–evidence–answer, chronological, comparison, case-based) are in `references/02-story-architecture.md`.

Sketch a **story spine in 5–9 beats** before assigning slide numbers. For every consecutive pair, be able to say **why B follows A**: because / therefore / however / to test that / the consequence is. If only “and next we discuss…” connects them, rework the order. No manufactured conflict or fake emotional drama.

## Step 4 — Explain for comprehension

For each difficult idea, apply **Need → Intuition → Concrete example → Mechanism → Evidence → Boundary** in the subset needed for this audience. Reveal complexity as prerequisites become available. Put definitions immediately before use; distinguish analogy from reality; show one realistic worked case before overwhelming generalizations. Answer “what am I looking at?” before “what does it mean?” for plots and mechanisms. Use relevant counterexamples where they prevent misunderstanding.

Do not confuse **simplification** with **oversimplification**. Keep necessary terminology, units, experimental conditions, uncertainty, assumptions, and distinctions. Move optional technical material to speaker notes/appendix, never bury indispensable truth.

## Step 5 — Create a storyboard that passes the title-only test

Draft a **slide-by-slide storyboard**, not a theme-deck. Every live-talk slide should have:

`index | audience question | takeaway/title | evidence/source | proposed visual | spoken explanation | transition | estimated seconds | density risk`

- Make title a **claim, question, instruction or genuinely descriptive anchor**, suited to its job. Favor action titles for argumentative slides; do **not** force a synthetic assertion onto cover, agenda, demonstration, visual pause or question slides.
- Every slide gets **one primary communicative job**, not necessarily one data point.
- Pair a **claim** with the **evidence** that makes it believable (or label it explicitly as a proposal/hypothesis).
- Design **spoken language and on-screen language as complements**, not duplicates.
- If a slide has 3 unrelated messages, split, reorder, or cut it. If two slides repeat one message without new understanding, merge or delete.

**Five tests:**
1. **Title-only / ghost deck:** Can someone follow the main reasoning from the sequence of headlines?
2. **So what:** Why should this audience care *here*?
3. **Why now:** What earlier question does this answer, or what next question does it create?
4. **Evidence:** Does the displayed evidence actually warrant this assertion?
5. **Five-second orientation:** Is it immediately clear what to look at, not necessarily fully understood yet?

## Step 6 — Choose a visual language, then compose individually

Use information-led visual forms:

- **Process:** labeled sequence, annotated flow, real walkthrough.
- **Comparison:** same-scale paired views, aligned table only if precise values matter.
- **Change:** trend, before/after, step-by-step reveal.
- **Causality/logic:** explicitly labeled causal vs conceptual diagram.
- **Distribution/variation:** appropriate plot, not an average without context.
- **Big idea/turning point:** restrained large type or one meaningful image.

Create a small **topic-appropriate design system** (type, hierarchy, spacing, palette, drawing style, image treatment); maintain continuity without repeating one card grid across all slides. Prefer genuine figures and carefully composed diagrams to stock-image filler. Give dense material more than one slide rather than shrinking text to fit. Keep primary content visible from a room's back row; do not rely on color alone to distinguish meaning. Respect supplied branding without inheriting its worst default layouts. See `references/05-visual-design.md` and `references/06-visual-evidence.md`.

## Step 7 — Human editorial pass (anti-generic AI)

Run this even when the user asks for “beautiful slides.” A polished default template is not a point of view.

- Replace filler: “In today's rapidly evolving landscape…”, “unlocking potential”, “seamlessly”, “robust”, “groundbreaking”, “game-changing”, “a paradigm shift”, “let's delve into”.
- Replace abstract “benefits / challenges / solutions” with **specific observation, mechanism, example, trade-off, or decision**.
- Avoid identical 3-column cards, omnipresent gradients, meaningless icons, unnecessary accent bars, fake dashboards, decorative charts, perfectly symmetrical slides, and universal blue-purple palettes.
- Avoid inflated claims, invented specifics, false dichotomies, gratuitous hooks, arbitrary metaphors, over-polished motivational closing statements.
- Give each slide a reason to exist and its own composition while preserving design coherence.
- Write lines a real speaker could say. Keep their domain voice and imperfections of normal speech; edit for rhythm, not corporate slickness.
- Keep the **precise** wording where the idea requires it. Do not sacrifice technical meaning to make every title short or dramatic.

**Deletion pass:** For each text block, graphic, metric, and slide ask: “If this disappears, what essential understanding is lost?” If none, remove it. If it is only needed for questioning, move to backup. If it is a source note, keep its traceability without distracting.

## Step 8 — Delivery, rendering and critique

Write speaker notes with **point → explanation → visual cue → natural transition → time**, not a verbatim recitation of the slide. Include rehearsal cues for pauses, demonstrations, difficult charts and anticipated objections. Reserve time for opening, transitions, Q&A and live demo failure paths.

When files are requested, use available local authoring skills/tools; choose PPTX, PDF, HTML/Reveal, Keynote-compatible, or another format according to editing, animation, equations and delivery requirements. Generate a rendered preview of **every slide** and inspect for overflow, misalignment, illegibility, low contrast, broken charts/links, and misleading visuals. If render tooling is not available, report the limitation rather than claiming visual QA was performed.

**Final release gates** (all required for finished deliverables):

1. **Truth:** claims and figures trace to reliable material; source and caveat preserved.
2. **Focus:** message clear; irrelevant material removed; audience benefits from every beat.
3. **Logic:** explicit causal/logical transitions; no orphan slides or unexplained leaps.
4. **Comprehension:** prerequisites, examples, and visual orientation where needed.
5. **Credibility:** counterarguments/limits acknowledged when material.
6. **Visual craft:** legible, relevant, intentional, varied without decorative excess.
7. **Human voice:** no generic AI prose, false drama, or theme-template sameness.
8. **Delivery:** realistic timing and notes; format and file integrity validated.

For a revision request, diagnose before redesign: identify the **three most damaging bottlenecks** and fix the story/clarity first; avoid cosmetic-only edits. For a full project, emit brief → spine → storyboard → draft → rendered result → critical revision, without waiting for approval at every stage unless a choice is consequential and cannot safely be inferred.

## Deliverable contract

Adapt to user intent, not every output is compulsory:

- **Outline-only:** one sentence + 5–9-beat spine + timing + exclusions.
- **Story / content rewrite:** audience question, message map, rationale, improved narrative and transitions.
- **Slide storyboard:** per-slide claim, support, visual, speaker cue, timing, source.
- **Presentation script:** natural language, signposts, evidence exposition, pauses, Q&A.
- **Finished deck:** editable source if possible, export/preview if possible, presenter notes, source attribution, assumptions and QA summary.
- **Critique:** prioritised problems, annotated fixes, before/after examples, uncertainty.

Do not generate fictional citations or claim to have opened/installed/read sources/tools unless actually accessed. Resource links in the research library are **reading suggestions**, not permission to execute third-party code. Follow copyright and licensing constraints.
