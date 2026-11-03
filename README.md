# Agent Skill Library

Private personal skill library for `danhuayan-snorkel`, with installable plugins for Codex and Claude Code and portable skill folders for other compatible agents.

| Skill | Purpose | Version |
|---|---|---|
| [Chinese Writing](plugins/chinese-writing/skills/chinese-writing/SKILL.md) | Natural Chinese translation, adaptation, and original technical/business writing | 0.1.2 |
| [Paper Reading](plugins/paper-reading/skills/paper-reading/SKILL.md) | Full-paper reading, method explanation, evidence review, and visual walkthroughs | 0.1.0 |

## Install

See [installation instructions](docs/INSTALL.md) for private-repo access, updates, and agent-specific choices.

Codex:

```sh
codex plugin marketplace add danhuayan-snorkel/agent-skill-library
codex plugin add chinese-writing@danhuayan-agent-skills
codex plugin add paper-reading@danhuayan-agent-skills
```

Claude Code, inside a session:

```text
/plugin marketplace add danhuayan-snorkel/agent-skill-library
/plugin install chinese-writing@danhuayan-agent-skills
/plugin install paper-reading@danhuayan-agent-skills
```

Other supported agents, using the optional Skills CLI (Node.js 22.20+):

```sh
npx skills add danhuayan-snorkel/agent-skill-library -g
```

Choose the skills and agents interactively. Use either plugins or direct skill installation for a given skill in an agent, to avoid duplicate discovery.

## Maintain the library

Edit the canonical files in `plugins/<plugin>/skills/<skill>/`. Each skill has one content source shared by all package formats. Update the source checkout, commit, and push; then refresh installed copies using the appropriate installation route.

For Chinese reference material, use [the reference index](plugins/chinese-writing/skills/chinese-writing/references/corpus/index.md) and [reference template](plugins/chinese-writing/skills/chinese-writing/references/corpus/reference-template.md). The package includes six screenshot originals and four contextual notes, alongside six approved bilingual calibration choices. New articles are contextual evidence until the user confirms a preference. No Alibaba source HTML or private sales deck is bundled.

Paper Reading was copied unchanged from the existing personal skill on 2026-11-03. Its default output is English. It requests a visual method walkthrough and already includes a diagram fallback when interactive tools are unavailable. Actual fetching and visual capabilities depend on the agent.

Use `$chinese-writing` or `$paper-reading` in Codex. In Claude Code, plugin skills are namespaced, for example `/chinese-writing:chinese-writing` and `/paper-reading:paper-reading`.

## Validate

```sh
python3 scripts/validate.py
```

If Claude Code is installed:

```sh
claude plugin validate .
claude plugin validate plugins/chinese-writing
claude plugin validate plugins/paper-reading
```

The validation checks packaging and references, not prose quality. Chinese Writing has [behavioral review cases](evals/README.md). An installed agent's abilities still determine which tools it can use.

Packaging references: [OpenAI plugins](https://developers.openai.com/plugins/build/plugins), [Claude marketplaces](https://code.claude.com/docs/en/plugin-marketplaces), and [Skills CLI](https://github.com/vercel-labs/skills).

## Package ZIPs for sharing

```sh
python3 scripts/validate.py
python3 scripts/package.py
```

Versioned ZIPs and SHA-256 checksums are generated in the ignored `dist/` folder. Each ZIP contains one complete plugin with `plugin.json` at the archive root. Only Git-tracked files within that plugin are included; add new reference files to Git before packaging. The archive includes skill references and screenshot assets, without repository history or client task files.

See [ZIP installation](docs/INSTALL.md#install-from-a-shared-zip) for recipient instructions. ZIP distribution is a snapshot; build and share a new version after updates.
