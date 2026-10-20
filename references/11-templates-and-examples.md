# 11 — Ready-to-use prompts, templates and before/after transformations

Templates below are **thinking scaffolds**. Do not copy empty headings into every deck. Substitute truthful, task-specific content and sources.

## A. Communication brief template

```markdown
Audience and probable skepticism:
Why this talk exists now:
Audience exit (understand / decide / do):
One-sentence takeaway:
Central question:
Three essential claims and their evidence:
Known assumptions and unknowns:
Time, modality and format:
Constraints and source materials:
Need for appendix / leave-behind:
```

## B. Source-to-story traceability

```markdown
| Claim ID | Proposed claim | Exact supporting source/figure | Scope/caveat | Listener prerequisite | Keep/location |
| C1 | ... | file/page/chart/link | ... | ... | live/notes/backup/cut |
```

Never confuse a future scenario with an observed result. If evidence is missing, leave `UNVERIFIED — obtain source` rather than fabricate.

## C. Story spine template

```markdown
1. The situation that matters is ...
2. But / the obstacle is ...
3. The audience's key question is ...
4. The useful insight is ...
5. The mechanism or recommended change is ...
6. The decisive evidence is ...
7. The limitation or trade-off is ...
8. Therefore [what the audience should know or decide] ...
```

If the talk is only a status update or short decision brief, reorder/shorten this template. Do not manufacture an obstacle for drama.

## D. Slide storyboard template

```markdown
| # | Audience question | Action title / anchor | Visual evidence & source | Speaker explanation | Bridge to next | Seconds |
|---|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... | ... |
```

**Presentation-specific choice:** For live speech, prefer minimalist projected content + notes. For read-alone decks, include concise explanatory context and sourcing in slide body. The action title should not promise more certainty than the graphic proves.

## E. Anti-dump transformation: fictional research example

**Original source-shaped deck:** “Background” (six bullets) → “Prior Work” (paper list) → “Methodology” (18-box system) → “Experiments” (four dense tables) → “Conclusion” (“our method is effective”).

**Clearer audience-shaped route:**

1. Why did predictions degrade after the input distribution changed? *(illustrated failure case)*
2. A fixed training distribution leaves the model blind to later shifts. *(paired distributions; claim requires evidence in real use)*
3. Existing baseline updates are either too slow or too unstable under the target constraint. *(fair comparison / source)*
4. The key idea is to separate fast adaptation from slow parameter updates. *(one running example)*
5. A simple gate routes uncertain cases to an update step. *(progressive mechanism)*
6. The improvement is largest under specific shift conditions. *(annotated, real experimental curve)*
7. The method remains sensitive to mislabeled feedback. *(failure case)*
8. Takeaway: adaptation helps when shift is real and feedback is trustworthy. *(qualified synthesis)*

These are illustrative **fictional** claims and must never be presented as facts about an actual paper.

## F. Anti-dump transformation: fictional executive update

**Dump:** 23 completed tasks, organizational updates, roadmap screenshots, six metrics, two unrelated customer quotes. Ends with “Next Steps.”

**Decision story:**

1. “We can meet the launch date only if the integration risk closes this week.”
2. “Core features are ready; one dependency is 9 days behind plan.”
3. “The delay affects payment confirmation, not the whole checkout flow.”
4. “Two options: scope reduction or late launch; cost and risks differ.”
5. “Recommendation: ship limited scope after safety test; approve owner and checkpoint today.”

Actual numbers/status and recommendation require real evidence; these sentences are demonstration placeholders.

## G. Per-slide content editing example

**Bad:**

```text
INNOVATIVE SOLUTION
Leveraging our state-of-the-art end-to-end ecosystem,
we unlock a new paradigm of seamless efficiency.
[three identical cards: Speed | Scalability | Insights]
```

**Better when verified:**

```text
The new handoff removes two approval steps.
[before/after route with removed steps highlighted]
Speaker: “This used to cross three teams. It now stays with one owner. 
The remaining question is whether the audit trail is equally reliable.”
```

## H. Explanation plan for hard ideas

```markdown
Term/idea:
Why the audience needs it now:
Prerequisite:
One-sentence intuition:
Realistic small example:
Visual model:
Formal definition if needed:
Likely misconception:
Boundary/counterexample:
How it moves the story forward:
```

## I. Speaker notes template

```markdown
Slide 6 — [claim / anchor]
Purpose: answer [audience question]
Opening: [natural 1-sentence line]
Point to: [the relevant axis, part, or object]
Explain: [one short paragraph of reasoning]
Interpretation: [what this proves and what it does not]
Bridge: [why the next slide follows]
Timing: [rough seconds]
Likely Q&A: [question + exact backup slide/source]
```

## J. Critique response template

```markdown
Communication goal and current failure:
Three highest-impact problems (with locations and evidence):
1. ... / consequence / proposed change
2. ...
3. ...
Revised single-sentence message:
Proposed 5–9-beat arc:
Before → after: one representative slide:
Cuts / merges / appendices:
Visual system changes that support the new story:
Truth/uncertainty notes and next validation:
```

## K. Fast self-audit (binary)

- Can a listener articulate the main answer without source knowledge?
- Are any prerequisites introduced **after** their first use?
- Can claim headlines be traced to actual evidence?
- Does every slide advance, substantiate or deliberately orient the argument?
- Would removing a text block preserve understanding? If yes, remove it.
- Do diagrams and charts explain a relation rather than decorate it?
- Is the visual design recognizably specific to this subject?
- Can someone speak the notes naturally within the time?
- Are essential uncertainties, baselines and trade-offs visible?
- Has the deck been rendered and inspected if file production was required?
