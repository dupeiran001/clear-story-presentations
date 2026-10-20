# 02 — Story architecture: choose the right logic

Story = **structured movement in audience understanding**, not necessarily a personal anecdote or a cinematic three-act drama. Build curiosity with a real unknown, unresolved trade-off, failed assumption or decision, not fabricated suspense.

## Choose by job (not genre labels alone)

| Job | Useful backbone | Typical audience question | When not to use |
|---|---|---|---|
| Decision memo / board briefing | BLUF / answer → reasons → evidence → alternatives → ask | What should we decide? | If key conclusion isn't supported |
| Persuasion | situation → obstacle → changed approach → proof → action | Why should I change? | If there is no credible next action |
| Research talk | why it matters → gap → insight → method → tests → meaning | What have we learned? | If the result is mainly negative; adapt |
| Status update | state vs plan → changes → cause → risk → next steps | Are we on track? | If it hides surprises under wins |
| Technical explanation | puzzle → prerequisites → example → mechanism → boundary | How does it work? | If the audience already knows the basics |
| Educational lesson | diagnostic prompt → model → worked example → practice → feedback | Can I now apply it? | If there is no practice time |
| Product demo | job to be done → existing friction → walkthrough → evidence → caveat | Can this solve my task? | If the demo is feature-tour theater |
| Comparative analysis | evaluation criteria → options → evidence → trade-offs → conclusion | Which option is best under our constraints? | If criteria appear post hoc |
| Incident/postmortem | impact → timeline → mechanism → controls → lessons/actions | What happened and what changes? | If it turns into blame theater |

## Frameworks, with strengths and traps

- **BLUF (Bottom Line Up Front):** give the answer early when the listener decides or is time-poor. Avoid claiming certainty before qualifying risks.
- **SCQA (Situation–Complication–Question–Answer):** orient, introduce real complication, name central question, deliver answer. Avoid a long generic “situation.”
- **Pyramid / answer-first:** conclusion, grouped supporting arguments, evidence under each. Useful for execs; weak if reader needs essential definitions first.
- **Problem–solution–evidence:** strong for concrete interventions; distinguish symptoms from root cause.
- **What is → what could be:** contrast existing reality with plausible alternative; don't sell a fantasy without evidence.
- **And–But–Therefore:** concise logic connecting established context, obstacle, and consequent action. Do not make every sentence perform this formula.
- **Question → evidence → answer:** useful for analytical discovery; preserve uncertainty and competing hypotheses.
- **Example → abstraction → example:** useful for technical teaching; do not generalize from one anecdote.
- **Chronological:** appropriate for incidents, histories, processes; often poor for a recommendation (give conclusion first).
- **Comparison:** aligned alternatives, criteria and trade-offs; avoid winner chosen before criteria.

These are useful working patterns, not universal scientific laws. Choose a structure that aligns with evidence and desired audience outcome.

## Story spine method (5–9 sentences, no slides yet)

Write one honest sentence per beat. Example for a product reliability report:

1. Our release target depends on 99.95% API availability.
2. The service currently meets average load but fails in one burst pattern.
3. The failure comes from shared queue saturation, not database capacity.
4. Partitioning queue traffic isolates critical requests.
5. A replay test improves critical path behavior, with a cost increase.
6. One production-risk assumption still requires a canary.
7. Approval today lets us run the canary; the final launch decision follows its results.

**Causal chain check:** Between two beats, supply `because`, `but`, `therefore`, `to test this`, or `the decision now is`. Replace “and then I will discuss.” Reverse outline any source document that is structured like a log rather than an argument.

## Hooks that respect the audience

Choose a relevant opening, not obligatory theatrics:

- **Consequence:** “If we keep this architecture, the median stays fast but the worst-case user wait doubles.”
- **Concrete discrepancy:** “Two teams measured the same system and reached opposite conclusions.”
- **A question that is genuinely answered:** “Why did error rates fall while user complaints rose?”
- **A short representative example:** show case → reveal deeper mechanism.
- **Decision at hand:** “Today we need to choose between faster launch and delayed verification.”
- **Answer-first:** for busy executive audiences, state the recommendation with its central caveat.

Avoid “Imagine a world where…”, unsupported provocative statistics, fake audience questions and unrelated jokes.

## Bridges / transitions

Every transition should either **close a question** or **open the next one**. Useful patterns:

- “That explains why the symptom matters. It doesn't yet explain the cause.”
- “We have a plausible mechanism; now we need a test that could disprove it.”
- “This approach solves the throughput problem, but it introduces a reliability trade-off.”
- “The result is promising under these conditions. Here is where it does *not* generalize.”
- “With that uncertainty visible, here is the decision we can responsibly make today.”

Do not copy those verbatim across decks. Use the facts and speech patterns of the actual subject.

## Rhythm and information release

Alternate **orientation → difficulty → explanation → evidence → synthesis**. After a high-load chart or method, give a beat for interpretation. A conceptual figure can remain up longer than a title slide; a 20-second animation may take less speech but more rehearsal. Different slide durations are normal. Do not assign 1 minute mechanically; test actual voice-over duration.

## Closing structures

- **Research:** question → most reliable answer → what changes / remains unknown.
- **Decision:** recommendation → caveat → owner / deadline / approval.
- **Teaching:** transferable rule → final application question.
- **Persuasion:** earned implication → concrete action.
- **Demo:** demonstrated value → constraints → realistic next step.

End on the message, not “Thank you” as the sole visible takeaway. A brief thank-you may be spoken.

## Failure diagnoses

- **Topic stack:** sections are named but causally unconnected. Fix by writing audience questions and bridges.
- **Wrong opening:** first five slides are broad market background. Start with the specific stakes.
- **Conclusions at end only:** listeners have no organizing frame. Move conclusion earlier when appropriate.
- **Suspense theater:** withholding facts purely to be dramatic. Give sufficient orientation.
- **Unmotivated detail:** process descriptions that answer no audience question. Delete or move to notes.
- **Forced three points:** exactly three everywhere regardless of substance. Group by logic, not numerology.
