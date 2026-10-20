# Worked example — from busy launch checklist to a decision-ready briefing

> **Fictional scenario.** All names, dates and facts below are invented solely to demonstrate the narrative method. They are not claims about a real product, and no performance numbers are implied.

## What the presenter receives

A team plans to release **Atlas Mobile** on Friday. Their notes say:

- The interface redesign is complete.
- The documentation has been updated.
- Mobile login intermittently fails in one test environment.
- The cause of the login failure is not confirmed.
- Translation review for one locale is unfinished.
- The team ran a product demo on Tuesday.
- The approval decision is due Thursday.
- There is not yet enough evidence to estimate how many production users would be affected.

The team originally planned a seven-slide deck: `Overview → Highlights → Activities → Technical Updates → Localization → Achievements → Next Steps`.

**Problem:** this is an activity tour, not a decision brief. It fails to make the uncertainty legible to the person deciding whether to ship.

## New communication brief

- **Audience:** engineering/product release committee; limited time; understands release process.
- **Goal:** choose a responsible Thursday decision and clarify what evidence is required.
- **Decision question:** can Atlas Mobile safely ship on Friday?
- **Governing message:** shipping on Friday cannot yet be justified, because the login failure's scope and cause remain unknown; define a release gate rather than imply a confident go/no-go from incomplete evidence.
- **Uncertainties:** production impact, reproducibility, root cause, and consequence of incomplete translation review.

## Story spine (logical sequence, not source headings)

1. The Friday release is planned, but Thursday is the decision point.
2. The interface, documentation and demo work are ready; these are not the release blockers.
3. Intermittent login failure remains unexplained, and its production scope is unknown.
4. Because login is critical, readiness cannot be inferred from completed design work.
5. There are two relevant choices: proceed only if specified gates clear, or move the release.
6. The committee needs evidence on login behavior, mitigations, and localization sign-off before approving a final choice.

## Five-slide storyboard

| Slide | What the audience needs to understand | Title (with warranted certainty) | Visual | Speaker message | Transition |
|---|---|---|---|---|---|
| 1 | What decision is required? | **Friday's release needs a Thursday readiness decision** | Single-line decision timeline, with two gates | "We need to decide what evidence allows a Friday launch; this isn't just a status review." | "Most work is ready. One issue dominates the risk." |
| 2 | What's complete and what isn't? | **The remaining blockers are login reliability and locale approval** | Status strip separating completed work, unresolved issue, unfinished review | "The UI, docs and demo are done. None of those establishes login reliability." | "The most serious unknown is the login failure." |
| 3 | Why is the unknown decision-critical? | **We cannot bound the login risk from current tests** | Three-step failure investigation: observation → unknown cause/scope → required verification | "We observed a failure, but we cannot extrapolate an incident rate or confidently localize its cause." | "That changes how the go/no-go should be framed." |
| 4 | What can we choose responsibly? | **Set explicit release gates instead of guessing risk** | Two-column conditional choice: ship if gates pass / delay if they fail | "Option A isn't unconditional launch. Option B isn't failure; it preserves the gate." | "So here is the precise ask." |
| 5 | What decision/action is needed? | **Approve the evidence gate and an owner for each test** | Decision checklist: login verification, mitigation evidence, localization sign-off, decision owner | "Today we're asking for agreement on the tests and who decides—not inventing an impact estimate." | Close with agreed next action and time. |

## What was cut or moved

- **Tuesday's demo:** supporting status detail; not needed as a separate slide.
- **Documentation finished:** one factual status marker, not a celebration slide.
- **Detailed engineering activity log:** appendix or notes if someone asks.
- **Invented risk percentage:** explicitly not allowed; scope is unknown.

## One before/after slide

**Before**

> **Project Highlights**
> - Seamlessly accelerated readiness across workstreams
> - Achieved a number of crucial milestones
> - Unlocked cross-functional operational alignment
> - Faced some ongoing technical challenges

**After**

> **We cannot bound the login risk from current tests**
>
> _Visual:_ on the left, one observed intermittent login failure in the test environment; on the right, two labeled unknowns: **root cause** and **production scope**; below, the verification required for a release decision.
>
> _What to say:_ "The important point is not how many tasks we've completed. We still don't know whether the login failure can appear for real users. Without that evidence, I can't call the release safe. Here's the test and sign-off we need before the decision."

No gradients, fictional KPIs or generic team-success cards are needed. The information design *is* the visual concept.

## Why this is better

The new deck answers what the audience came to decide, exposes uncertainty rather than burying it, uses a concrete causal connection between slides, and ends with a precise ask. It deliberately avoids a fake definitive recommendation: the available facts warrant a decision **process and gate**, not a made-up quantified release risk.
