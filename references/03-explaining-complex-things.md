# 03 — Explaining complex things clearly without dumbing down

The failure mode of dense presentations is often **missing inferential steps**, not just too many words. The presenter makes a leap that is easy only because they already know the answer.

## Explanation design

Choose relevant moves from this sequence, not every move for every concept:

1. **Why need it?** What question or task cannot be completed without this concept?
2. **Plain-language intuition:** One sentence with accurate boundaries.
3. **Known anchor:** Connect to something the audience already understands.
4. **Concrete instance:** Small, realistic example with names, units, inputs and outputs.
5. **Mechanism:** What changes, what causes it, which components matter, where are decisions made?
6. **Formalism:** Equation/algorithm/architecture only after definitions; reveal important terms.
7. **Worked result:** Predict first, then show observed outcome.
8. **Boundary:** Where intuition breaks; failure mode, assumption, counterexample.
9. **Transfer:** Ask listener to apply the idea to a second case.

## Prerequisite ladder

List concepts in their **dependency order**, not paper/source order:

`goal → essential vocabulary → example → mechanism → formal representation → consequence`.

For every symbol, acronym or label, ask “has the listener already been taught what this means?” Supply a small vocabulary key if several terms are genuinely needed. Avoid overexplaining primitives the audience knows.

## Visual reasoning strategies

- **One running example:** carry the same object through several slides (e.g. one query, one patient, one transaction, one graph), with stable colors/labels.
- **State-transition views:** before / action / after, not a single unlabeled system diagram.
- **Progressive disclosure:** one meaningful change per build; audience should know what new information appeared. Don't use animation only for decoration.
- **Compare alternatives on the same example:** establish evaluative criteria beforehand.
- **Analogy + disclaimer:** state both where the analogy helps and where it stops.
- **Counterexample:** show a plausible-but-wrong approach and why it fails, especially if misunderstanding is common.
- **Text + graphics integration:** label diagram components next to them; avoid remote legends when direct labels work.

## Explaining a formula

Poor: paste the entire optimization objective and say “we optimize this.”

Better:

1. State the intended behavior: “Choose a path that is fast *and* respects the safety bound.”
2. Show variables with their meanings and units.
3. Start with simplest valid case; add constraints/terms one by one.
4. Highlight the one term carrying the novel idea.
5. Walk through numerical toy example if useful.
6. State what the equation does not guarantee.

If equation doesn't change audience understanding, move full derivation to appendix. In specialist talks where exact formalism *is* the result, show it prominently and give enough time to parse it.

## Explaining algorithms and architectures

Poor: 17 boxes, 11 arrows, 7 colors and dense text all at once.

Better: define input/output and use an example: “A request enters → policy chooses route → model computes score → guard checks threshold → result exits.” Show what changes from the baseline. Mark control vs data paths. Distinguish physical, logical, causal and temporal relationships; arrows cannot mean everything at once.

## Showing results

Tell the viewer: **what is compared → what axis/units mean → what to inspect → finding → interpretation → caution**.

Avoid conclusions stronger than evidence. “Association increased after rollout” is not automatically “rollout caused growth.” “This result is statistically significant” is not the same as “large and operationally relevant.”

## One-slide explanation diagnostic

- Can the listener name the entities and their relationship?
- Is the real question visible before the answer?
- Is each newly introduced term defined?
- Are the axes/units/baselines understandable?
- Is the change compared with a real alternative or counterfactual?
- Can the speaker explain the slide without reading it?
- Could a 30-second concrete example do more than another abstract bullet?

## When to allow density

A graduate seminar, teaching workshop, read-alone analysis, legal review or live code walkthrough may need dense material. Retain density when it is the *object* of study; create layers, visual signposting and enough time, rather than deleting important details for style.
