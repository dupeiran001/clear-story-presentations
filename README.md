# Clear Story Presentations

**A presentation-thinking Agent Skill for Claude Code.** Make the point clear *before* making the slides beautiful.

[中文说明](README.zh-CN.md) · [How to publish](docs/PUBLISHING.md) · [Skill instructions](SKILL.md) · [Method library](references/10-research-library.md) · [Evaluation guide](docs/EVALUATION.md)

Clear Story Presentations helps an AI assistant **think through what to say, why it matters, how to explain it, and how to show the evidence**. It is designed for research talks, technical teaching, executive briefings, status updates, product demos, pitches, workshops, and critique of existing decks.

Most presentation generators start with a layout. This skill starts with the **audience's unanswered question**, builds a defensible message, orders the explanations, deletes the noise, then uses visual design to help the audience follow the reasoning.

> **This is a methodology skill, not a slide-rendering engine.** It can guide slide creation and review when your agent has suitable tools installed, but it does not bundle PowerPoint, image-generation services, or any external model API. PPTX/PDF output depends on the tools available in your environment.

## What it helps with

| Before | After |
|---|---|
| An agenda copied from source-document headings | A storyline built around the audience's actual questions |
| “Background → Method → Results → Conclusion” as a default | A context-specific argument with explicit logical transitions |
| Facts and graphics crammed onto slides | The minimum evidence needed for each precise claim |
| A complex diagram shown all at once | A paced explanation with prerequisites and a running example |
| Polished but repetitive AI template slides | Intentional compositions chosen for each communication job |
| Script that repeats the slides | Natural speaking notes, emphasis, transitions, and time budget |
| Attractive but potentially misleading charts | Figures with accurate scales, sources, scope, and caveats |

**Core workflow:** Audience & goal → Main message & evidence → Story spine → Explanation & editing → Slide storyboard → Visual system & implementation → Rehearsal & QA.

## Install

Claude Code can load skills from a personal `~/.claude/skills/` directory or a repository's `.claude/skills/` directory. See the [official Claude Code documentation](https://code.claude.com/docs/en/skills).

**Personal installation** (available across local projects):

```bash
git clone https://github.com/YOUR_USERNAME/clear-story-presentations.git \
  ~/.claude/skills/clear-story-presentations
```

**Project installation** (commit with a project):

```bash
mkdir -p .claude/skills
git clone https://github.com/YOUR_USERNAME/clear-story-presentations.git \
  .claude/skills/clear-story-presentations
```

Replace `YOUR_USERNAME` with the publisher's GitHub username **after the repository is published**. You can also download the repo as a ZIP, extract it, and copy the **whole `clear-story-presentations/` folder** into either skills directory. On Windows, use the same relative directories under your home or project folder and copy the folder with File Explorer or PowerShell.

For non-Claude agents, consult their [Agent Skills](https://agentskills.io/specification) support and skill-discovery paths; compatibility has not been verified on every agent runtime.

## Use

Invoke explicitly with `/clear-story-presentations`, or ask naturally for help with an appropriate presentation task.

**Start with the storyline, not a deck:**

```text
/clear-story-presentations I need to explain an unfamiliar technical idea
in 8 minutes to engineers. Identify their prerequisite knowledge,
construct the argument, use one worked example, and propose a storyboard.
Don't generate a PPTX yet.
```

**Turn a paper into a conference talk:**

```text
/clear-story-presentations Read the paper and supplementary materials.
Extract the central claim, build a 12-minute research talk with a coherent
narrative, keep claims tied to actual figures, and draft speaker notes.
Move nonessential technical details to backup slides.
```

**Rewrite an unfocused status presentation:**

```text
/clear-story-presentations Turn these 30 activity bullets into a
5-minute leadership update. Lead with state vs plan, decision needs,
risks, and evidence. Cut filler; do not invent metrics.
```

**Critique an AI-looking deck:**

```text
/clear-story-presentations Diagnose why this presentation feels generic.
Fix the logic and clarity before suggesting typography and layout changes.
Give me specific before/after alternatives, not just aesthetic adjectives.
```

**Example:** [A fictional launch-decision briefing, rewritten from clutter to a decision-ready story](examples/launch-decision-storyboard.md).

## Why it is structured this way

The main [SKILL.md](SKILL.md) is the executable method. Eleven focused files in [`references/`](references/) are **loaded selectively** for jobs such as narrative design, complex explanations, editing, chart design, visual craft, rehearsal, and production QA. This avoids loading the entire library into every session.

```text
clear-story-presentations/
├── SKILL.md                   # Core workflow and when to load references
├── references/                # 11 focused method and resource guides
├── examples/                  # Worked narrative transformation
├── evals/evals.json           # 9 scenario prompts; not automatically graded
├── scripts/check_skill.py     # Dependency-free structural validator
├── docs/EVALUATION.md         # How to test behavior and log results
├── README.md                  # English project documentation
├── README.zh-CN.md            # Chinese project documentation
├── LICENSE                    # MIT license for original project contents
└── .github/workflows/         # Structural check on pull requests
```

## Design principles

- **Truth before persuasion:** never turn correlation into causation, a proposal into an observation, or an uncertain result into a definitive headline.
- **Understanding before decoration:** a beautiful slide is not successful if it skips the inferential step the audience needs.
- **Edit without losing meaning:** remove clutter, not assumptions, units, caveats, or critical context.
- **Speak like a person:** no invented emotional hooks, hollow AI buzzwords, and obligatory three-column cards.
- **Choose the right format:** a live talk, a read-alone deck, a workshop, and a decision briefing have different information needs.
- **Be tool-agnostic:** the narrative should work even if the PPTX rendering tool changes.

## Status & limitations

- **Package:** original skill instructions, 11 reference notes, 9 manual scenario evals and a local structural validator.
- **Checked locally:** metadata, local documentation paths, evaluation JSON schema, and repository file structure via `python3 scripts/check_skill.py`.
- **Not yet independently confirmed:** performance in a live Claude Code evaluation run, PPTX rendering quality on actual decks, and cross-agent compatibility. These should be tested with representative presentations before making stronger claims.
- **Source library:** a curated collection of third-party readings, not bundled source code and not a certification or endorsement. Some external pages may change. See [resource provenance](docs/SOURCES.md).

To test the package without network access or dependencies:

```bash
python3 scripts/check_skill.py
```

To test **behavior** with and without the Skill, follow [docs/EVALUATION.md](docs/EVALUATION.md). A structural PASS is not evidence that all nine behavior scenarios pass.

## Contributing & licensing

Contributions that improve explanation quality, audience fit, scientific rigor, accessibility, or the anti-template editorial process are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md). If you plan to publish your own fork, see [the release checklist](docs/PUBLISHING.md).

The **original text and scripts in this repository** are offered under [MIT](LICENSE). Third-party repositories, publications, diagrams, code, and visual assets linked from this project retain their own licenses; none are bundled here. No affiliation with Anthropic, Claude, TED, MIT, or the linked authors is implied.
