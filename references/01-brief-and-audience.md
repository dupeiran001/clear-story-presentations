# 01 — Communication brief and audience modeling

## One-page intake

Construct from documents and request, leaving unknowns labeled. Do not block on missing preferences if sensible defaults exist.

| Field | Question | Implication |
|---|---|---|
| Speaker | Who is communicating, and with what credibility? | Tone; who owns uncertainty |
| Audience | Which roles, incentives, vocabulary, common misconceptions? | Familiarity and jargon |
| Context | Why are we speaking now? What prompted it? | Open with situation, not bio |
| Intent | Inform, teach, align, persuade, decide, inspire, demonstrate, get feedback? | Story structure |
| Audience exit | What should they explain, believe, decide, remember, or do afterward? | Main takeaway |
| Time | Actual speaking time excluding introductions/Q&A, handovers, demo? | Pacing |
| Format | Spoken live, webinar, slide-less, read-alone deck, leave-behind? | Text density |
| Evidence | What is firsthand, published, computed, speculative? | Labels and sourcing |
| Constraints | Branding, localization, confidentiality, accessibility, recording? | Production |

## Distinguish the question from the answer

Weak: “Talk about our Q3 progress.” Strong: “Can we safely launch region B next month?” and “Probably yes after two outstanding blockers close by Friday.” The presentation should support the **specific decision**.

Weak: “Explain vector databases.” Strong: “Help software engineers choose when approximate vector search is helpful and when conventional retrieval is safer.”

Weak: “Present my paper.” Strong: “Help mixed-discipline attendees understand why existing baselines fail on distribution shift, how our core design handles it, and what the evidence actually supports.”

## Audience empathy without mind-reading

Ask: What do they already know? What will surprise them? Where will they disagree? Which constraints are theirs, not ours? What could cause an incorrect inference? What terms are truly shared?

Capture 3–5 probable **audience questions in their own words**: “Why are we changing?”, “What breaks?”, “How certain is this?”, “What am I being asked to approve?”

Distinguish novice, generalist, near-domain, specialist. A specialist does not need less rigor; they need a shorter runway and clearer comparative evidence. A non-specialist does not need empty metaphors; they need carefully chosen definitions and real examples.

## Message ladder

1. **Topic** (weak): “Renewable energy.”
2. **Finding** (better): “Peak demand has shifted later.”
3. **Meaning** (stronger): “Our current storage dispatch misses the evening peak.”
4. **Decision/implication** (when applicable): “Move two reserve hours to 6–8 p.m., subject to the reliability test.”

Build the main sentence as: **[What is true / proposed] + [how it is supported] + [why it matters / what follows]**. One sentence need not cram all three if readability suffers.

## Presentation ≠ document ≠ sales pitch

- **Live presentation:** spoken guidance carries argument; visuals guide attention; timing is a hard constraint.
- **Read-alone deck:** more textual context and detailed sourcing; no speaker needed to decode it; use summaries and appendix.
- **Decision memo:** readers can pause and skim, so explicit alternatives and limitations matter more than theatrical pacing.
- **Workshop/lesson:** sequences of practice, feedback, comprehension checks, not just broadcasting claims.

For a hybrid use case, produce **two layers** where feasible: sparse projection slides + speaker notes/appendix/handout. Do not produce illegibly dense slides in an attempt to serve both.

## Assumptions protocol

If details are missing, write one line: `Working assumptions: ~12 min, technically literate mixed audience, live talk, English slides, editable PPTX.` Replace only assumptions unsupported by supplied info. Never ask again for known facts; never invent source data. Flag material gaps such as “results absent; cannot substantiate performance claim.”

## Stakeholder-facing clarity

- Prefer action/decision and implications near the beginning in time-limited executive settings.
- For exploratory research, separate **what we know** from **what we need feedback on**.
- For sensitive or high-stakes topics, make uncertainty, conditions and alternatives prominent; avoid emotional framing that disguises evidence quality.
