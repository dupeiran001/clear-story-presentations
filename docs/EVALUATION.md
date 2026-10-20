# Evaluation and release gates

This repository supplies **evaluation prompts**, not precomputed Claude scores. Be explicit about the difference between a static package check and a model-behavior test.

## Tier 1: Static package checks (automated)

```bash
python3 scripts/check_skill.py
```

This checks required files, frontmatter name/description syntax, relative links, eval-file schema, documentation hygiene, and basic resource counts. GitHub Actions runs the same check on pushes and pull requests. It **does not** instantiate Claude Code, render slides, or assess quality.

If an official Agent Skills `skills-ref` validator is installed, also run:

```bash
skills-ref validate .
```

Do not claim that command was executed unless you actually ran it.

## Tier 2: Behavioral evaluation (manual until automated)

Run the 9 tasks from [`../evals/evals.json`](../evals/evals.json) in a genuine Claude Code session. For reliable comparison:

1. Use a fixed model/version, tool permissions, conversation length, and supplied source material; record the setup.
2. Run each prompt **without** the Skill in one fresh session, then **with** the Skill in another. Ensure the intended Skill was available and invoked when testing the second condition.
3. Save response text, outlines, storyboards, and file artifacts for both cases (with confidential material removed).
4. Score with the rubric below and record **concrete evidence**, not only a total.
5. Repeat uncertain cases with independent runs; distinguish behavior caused by the Skill from chance or tool access.
6. For deck-producing runs, **render every slide and inspect it**. A successfully generated file is not evidence of visual quality.

## Rubric (0–2 per dimension)

| Dimension | 0 — Failure | 1 — Partial | 2 — Good |
|---|---|---|---|
| Audience & goal | Generic/unfit | Mentioned but not guiding choices | Clear user/audience decision shapes the story |
| Narrative | Source heading dump | Some storyline, weak connections | Explicit, necessary transitions and coherent thesis |
| Explanation | Assumes missing knowledge | Explains some prerequisites | Intuition/example/mechanism/limits adapted to audience |
| Editing | Repetitive, overloaded | Some pruning | Focused, necessary content with rationale for cuts |
| Evidence & integrity | Fabricated or misleading | Caution but missing traceability | Source-scoped claims, accurate caveats, no inventions |
| Visual strategy | Decorative template | Partial visual intent | Appropriate plots/diagrams, clear viewing order |
| Human voice | Buzzwords, mechanical | Occasional natural phrasing | Specific, speakable, authentic and nonformulaic |
| Feasibility | No realistic timing/format | Some constraints honored | Appropriate pacing, output format and actual QA |

Score each dimension and include qualitative notes. **Evidence integrity is a blocking condition:** a confident invented numerical result or a causal overclaim cannot be offset by an attractive deck. Do not advertise a universal numerical "quality score" without defined tasks and repeated evaluation.

## Result record template

```markdown
### Scenario: [eval id]
- Date / model / version:
- Tool access and documents:
- Prompt and source snapshot:
- Without-skill output:
- With-skill output:
- Evidence the skill was invoked:
- Scores (each dimension, 0–2):
- Most important improvement:
- Regression/failure:
- Rendered slides inspected? (Yes / No / N/A):
- Next corrective change:
```

## Tier 3: Representative user examples

Before claiming this Skill produces "conference-quality decks," publish at least two permission-safe full walkthroughs: one technical/research task and one non-academic report/briefing. Include the **input constraint, story spine, storyboard, rendered slides, and honest QA findings**. Mark fictional samples as fictional.

## Suggested prerelease checklist

- [ ] `scripts/check_skill.py` passes
- [ ] The main `SKILL.md` remains focused and under 500 lines
- [ ] Installation and invocation instructions reproduced on a fresh Claude Code session
- [ ] All nine scenarios reviewed with evidence or marked not run
- [ ] No proprietary/third-party content included without applicable permission
- [ ] At least one worked example has understandable before/after decisions
- [ ] Limitations and missing evidence explicitly disclosed
