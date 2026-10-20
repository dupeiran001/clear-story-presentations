# 06 — Visual evidence, diagrams, and charts

The visual should match the **question and evidence**, never the other way round. Design objective: reduce inference effort without distorting facts.

## Evidence roles

- **Evidence:** observations/data/tests/sources that warrant a claim.
- **Mechanism:** explanation of relationships; may be modeled, not directly observed.
- **Illustration:** helps comprehension; *does not prove* the claim.
- **Analogy:** conveys intuition; must not be presented as a scientific mechanism.
- **Proposal:** future possibility, explicitly conditional; not measured performance.

Caption or orally name the role when ambiguity could mislead. Never use a decorative sketch as implicit proof.

## Chart-selection map

| Question to answer | Usually consider | Key caveat |
|---|---|---|
| How much by category? | ordered bar, dot plot, aligned table | zero baseline for bar lengths; labels and units |
| How changed over time? | line or step plot | time intervals and context |
| Relationship between variables? | scatter plot with sensible axes | association != causation |
| Range/dispersion? | distribution, histogram, box/violin + n | do not hide outliers / sample size |
| Parts of a whole? | sorted bars, stacked bars, treemap selectively | percentages sum and denominators |
| Before vs after? | paired dot/slope, small multiples | matched samples and confounds |
| Spatial variation? | honest map with scale/legend | area and color interpretation |
| Exact lookup? | table with highlighted cells | table is appropriate for precision |
| Trade-offs? | scatter/frontier, comparison table | announce criteria before choice |
| Contribution of components? | waterfall, decomposition | components and residual defined |
| Uncertainty? | interval, distribution, error bar | meaning of interval; units |

Reference: Claus Wilke's *Fundamentals of Data Visualization* and *From Data to Viz*; see `10-research-library.md`.

## Explain one plot in five breaths

1. **What:** “Each point is one experiment / customer / model.”
2. **How to read:** “X shows time; Y shows failure rate; lower is better.”
3. **Compare:** “Blue is baseline; orange uses the new policy.”
4. **Find:** “Most separation happens above [verified threshold].”
5. **Meaning/limit:** “That supports a benefit under burst load; we haven't tested steady-state production traffic.”

Build actual wording from actual data; placeholders are not conclusions.

## Figure redesign protocol

1. Extract the original chart data/meaning (not estimated pixels if numerical source exists).
2. Identify one claim the slide needs to support.
3. Keep the right baseline/control and the uncertainty that changes interpretation.
4. Remove panels and annotations not needed *for this point*; retain them in appendix with citations.
5. Prefer direct labels, selective highlighting, meaningful ordering and consistent units.
6. Write accurate claim and plot caption/source.
7. Compare revised chart against original to verify no semantic drift.

For scientific figures, preserve measurement definitions, test conditions, error bars, uncertainty, exclusions, baselines and sample sizes when material. For business charts, preserve period, population, accounting definitions, missingness and currency.

## Diagrams are models — label the type

- **Flowchart:** path or decision logic. Label decision conditions.
- **Architecture diagram:** component interfaces and data/control pathways.
- **Sequence diagram:** who does what when.
- **Dependency graph:** prerequisites or constraint propagation.
- **Causal diagram:** proposed influence, assumption vs established effect; avoid casual cause-arrows.
- **Concept map:** association or grouping, no implied direction unless stated.
- **Before/after:** invariant frame; show meaningful changed state.
- **Risk/decision tree:** uncertain branching with explicit conditions.

Do not mix every arrow meaning into one diagram. Put unfamiliar node names directly on nodes, avoid tiny external legends, and remove nonessential infrastructure boxes.

## Honest quantitative emphasis

- Use 2D encoding accurately; avoid 3D bars and decorative area where height conveys values.
- Avoid truncated baselines that exaggerate *bar* differences; if zooming a line, disclose the scale.
- Treat relative vs absolute changes carefully: “risk decreased 20% relatively” may mean only 2 percentage points.
- Label exploratory analyses vs pre-specified tests, statistical vs practical significance, confidence interval vs standard deviation.
- Avoid smoothing/interpolation that implies unmeasured behavior. Show real points where possible.
- Cite origin/derivation of numbers and annotate transformations.
- Never fabricate exact sample count or metric merely to populate a polished chart.

## Progressive chart walkthrough

Show context axes → introduce one series → point to relevant anomaly → reveal comparator → interpret → state caveat. Keep scales/positions stable across reveals. Static fallback: use small multiples or visible numbered callouts.

## Evidence audit questions

- What proposition does the display support *exactly*?
- Would a skeptical expert accept the chosen baseline?
- Are sources/date/units/definition traceable?
- Do axis choices exaggerate or minimize variation?
- Are error, uncertainty and sample size relevant?
- Does the graphic imply causality or certainty unsupported by the source?
