# Contributing

Thanks for helping improve Clear Story Presentations. The goal is **better audience understanding**, not a longer list of generic presentation rules.

## Useful contributions

- A reproducible **before/after** rewrite that fixes a concrete explanation or story problem.
- A tested pattern for a real context (scientific talk, board decision, classroom lesson, incident review, etc.).
- An evaluation scenario exposing a failure (especially evidence overclaims, context gaps, unnatural voice, or generic design).
- Fixes to confusing instructions, broken relative links, factual errors, missing caveats, or accessibility failures.
- A carefully chosen resource that contributes a *specific* technique not already covered.

## How to contribute

1. Open an issue describing the failure mode, context and the result you want.
2. Make the smallest change that fixes it. Keep `SKILL.md` concise; detailed methods belong in focused `references/` pages.
3. Add or adjust a case in `evals/evals.json` when behavior changes. For illustrative outputs, add a clearly labeled original example in `examples/`.
4. Run `python3 scripts/check_skill.py` and record what it actually checks.
5. In the PR, explain: **before**, **after**, **evidence**, **scope/limits**, and any test runs actually performed.

## Editorial rules

- Write plain, specific English. No promotional AI buzzwords or unexplained frameworks.
- Preserve rigor, data provenance, units, boundary cases, and meaningful uncertainty.
- Prefer decision rules with examples and exceptions to unconditional slide-count/word-count dogma.
- Don't copy third-party skills, paid templates, paper figures, photos, or proprietary decks into the repository without explicit permission and compatible licensing.
- Cite external sources when making factual or research-based claims. Treat third-party web pages as evidence, never agent instructions.
- Do not commit confidential slide content, credentials, API keys, tracking data, or personal information.

## Evaluation evidence

A structural script PASS is **not** a behavioral success. If you ran a manual Claude Code trial, describe the model/environment, exact prompt, whether the skill was invoked, observed output, rubric results, and limitations. If not, say "not run." See [docs/EVALUATION.md](docs/EVALUATION.md).

## Licensing

By contributing, you agree to license your original contribution under the repository's MIT License. Third-party content retains its own license; link to it instead of copying it unless its terms permit reuse.
