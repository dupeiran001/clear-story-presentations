# 09 — Tool-neutral production pipeline and quality assurance

**Content architecture should survive a tool change.** Choose the tool for deliverables and maintenance, not because it automatically produces attractive templates.

## Choose a tool based on use case

| Need | Candidate | Trade-off / validation |
|---|---|---|
| Editable PowerPoint, automation | PptxGenJS; python-pptx; environment PPTX skill | Verify charts, notes, fonts and shape positioning in target viewer |
| Web-native, interactive or developer talk | Reveal.js, Slidev | Browsers/network assets; export fallback |
| Markdown authored, fast static slides | Marp | Limits for intricate editorial layouts |
| Technical publishing with code/LaTeX | Quarto, Typst/Touying, Beamer | Export and compatibility vary |
| Existing branded template | PowerPoint-native edit / existing tool | Preserve master/layout, don't bypass corporate constraints |
| Visual draft | SVG/HTML and rendered screenshots | Visual fidelity does not imply editable PPTX |

When a dedicated slide, PDF or design skill is installed, read it for technical instructions. This Skill governs **why/what/how to explain**; implementation skill governs **format syntax and rendering**. Read external repositories critically, do not execute unreviewed install scripts.

## Output folder structure (example, adapt to user)

```text
presentation/
  communication-brief.md
  source-notes.md
  story-spine.md
  storyboard.md
  speaker-notes.md
  references.md
  slides.pptx                 # when requested and supported
  slides.pdf                  # when export supported
  source/                     # code/assets necessary for edits
  previews/                   # rendered slides for QA
  appendix/                   # optional supporting details
  qa-report.md
```

Do not force a folder full of artifacts when the task only asks for a revised outline or explanation.

## Draft → render → inspect → fix

1. Review source documents and verify access to source plots, logos, fonts, icons, diagrams and required assets.
2. Produce communication brief and narrative spine.
3. Write storyboard with one communicative job per slide and exact evidence mapping.
4. Design reusable tokens; prototype **1 dense evidence slide, 1 concept slide and 1 transition slide** before filling deck.
5. Build pages with editable native objects where feasible; keep raw inputs and chart values.
6. Export/render every slide. Generate montage or inspect each page at presentation scale.
7. Check **visual errors**: clipping/overflow, baseline alignment, line breaks, font substitution, insufficient contrast, cramped labels, poor image crop, blurry plots, thin arrows, broken math, low-res figures.
8. Check **semantic errors**: claim unsupported by plot, misaligned comparative axes, illegible footnotes hiding crucial caveats, labels missing units, claims contradicting notes.
9. Check **story errors**: title-only flow, skipped prerequisites, repeated claim, dropped question, unjustified reveal, weak ending.
10. Revise and render again; only report QA checks actually performed.

## Visual acceptance tests

- **Contact sheet:** Scan all slides at once. Is composition varied but coherent? Are five consecutive pages copies of the same template?
- **Single slide:** Can unfamiliar audience orient their eyes within five seconds?
- **Projector scale:** Can title, data labels and semantic codes be read from back row or small stream?
- **Grayscale/color-vision check:** Is meaning preserved without color distinction?
- **Bad-connection check:** Do embedded videos/remote fonts/interactive elements fail gracefully?
- **Static export check:** Does build/animation dependency remain understandable in PDF?
- **Read-alone check, if required:** Does the deck include enough provenance, context and caveats?

## Critical red-team questions

- What's the strongest claim we couldn't prove?
- Which interpretation would a skeptical audience challenge?
- Do we label proposed future performance as measured outcome?
- If only headings remain, is the logic visible?
- Are slides teaching the topic or only listing facts about it?
- Has tasteful design become generic or unnecessarily sparse?
- Can the speaker honestly speak this in time?
- Can user revise the final deliverable without a full rebuild?

## Weighted critique (optional, do not reduce to one meaningless number)

Score 1–5 with short evidence-based notes for each:

| Dimension | Suggested weight |
|---|---|
| Truth, evidence and scope | 20% |
| Listener-centered message | 15% |
| Narrative structure/transitions | 15% |
| Explanation and prerequisites | 15% |
| Ruthless focus and clarity | 10% |
| Visual evidence and craft | 10% |
| Human voice and originality | 10% |
| Rehearsal/time/accessibility | 5% |

**Blocking flaws:** fabricated numbers or citations; misleading chart axes; unreadable essential evidence; unclear ask in decision presentation; missing necessary logical step; persistent overflow. Polish cannot offset them.

## Boundaries and transparency

If source assets are inaccessible, mark what was inferred vs verified. If file output/export is unsupported, supply storyboard or source and tell user exactly what remains undone. Do not say you visually validated a PPTX unless it was actually rendered and inspected. No made-up success scores or invented URLs.
