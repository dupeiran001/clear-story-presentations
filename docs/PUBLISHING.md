# Publishing this repository on GitHub

The project folder is prepared as a GitHub repository. **Publishing is a separate action** that requires your own GitHub account and permission to publish all files.

## Before the first public push

- Review the skill's claims, the [worked example](../examples/launch-decision-storyboard.md), and [sources/licensing policy](SOURCES.md).
- Decide if the MIT License matches your intent. This package uses `Copyright (c) 2026 Clear Story Presentations contributors`; you may replace the copyright holder with your own name or organization if appropriate.
- Check that the project contains no company documents, personal details, credentials, private screenshots or unlicensed figures.
- Run `python3 scripts/check_skill.py`. Treat it as a **structural check only**.
- For a stronger quality claim, test the nine cases described in [EVALUATION.md](EVALUATION.md) and publish reproducible results. Currently these have not been run in a live Claude Code instance in this environment.

## Create the GitHub repository

1. Create a new **public**, **empty** GitHub repository called `clear-story-presentations` (do not check “Initialize with README” or select a license; those files are already included here).
2. Unzip the GitHub-ready package on your computer and open a terminal in the **`clear-story-presentations` folder** that directly contains `SKILL.md` and `README.md`.
3. Replace `YOUR_USERNAME` below and run:

```bash
python3 scripts/check_skill.py
git init
git add .
git commit -m "Initial release: clear story presentation skill"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/clear-story-presentations.git
git push -u origin main
```

Existing Git repositories may already have a remote or commit history; inspect `git status` and `git remote -v` first and adapt commands rather than rerunning `git init` or `remote add` blindly.

## Suggested repo metadata

- **Name:** `clear-story-presentations`
- **Description:** `An audience-first Agent Skill for clear presentations: storytelling, explanations, reports, slide strategy, and visual design.`
- **Topics:** `agent-skills`, `claude-code`, `presentation`, `storytelling`, `slide-design`, `scientific-communication`, `data-visualization`
- **License:** MIT (if that's the license you intend)

## After publishing

- Verify the Actions tab shows a passing structural check; check the README's relative links and render correctly on GitHub.
- Fresh-install the Skill using the actual GitHub URL and confirm `/clear-story-presentations` can be invoked in Claude Code.
- Add a **real permission-safe before/after case** with screenshots or slide exports if available; fictional text-only examples show method, not visual outcomes.
- Consider a `v0.1.0` release and GitHub issue discussions after at least one independent user tries it.
- Avoid adding badges such as “all evals passed” until you can substantiate the claim.
