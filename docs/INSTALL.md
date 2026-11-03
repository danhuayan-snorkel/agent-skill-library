# Install across agents

Repository: `danhuayan-snorkel/agent-skill-library` (private). Marketplace name: `danhuayan-agent-skills`.

## Access on a new machine

Sign into GitHub with an account that can read this repository. Native plugin installation uses the host's configured Git access. The Skills CLI also supports authenticated GitHub CLI access.

```sh
gh auth login
gh repo clone danhuayan-snorkel/agent-skill-library
```

Do not place tokens in repository URLs or files. A local clone can be used when a remote host's authentication is not configured.

## Codex plugins

```sh
codex plugin marketplace add danhuayan-snorkel/agent-skill-library
codex plugin add chinese-writing@danhuayan-agent-skills
codex plugin add paper-reading@danhuayan-agent-skills
```

Or, from a local clone:

```sh
codex plugin marketplace add .
```

Then install the desired plugins as above. Start a new chat after installation; restart the desktop app if discovery has not refreshed.

This machine initially installed Chinese Writing from `chinese-writing-local`, and Paper Reading was already a standalone personal skill. Creating the shared library does not migrate or remove those installations. Avoid installing a second copy in the same agent until you choose to migrate. To check Codex state:

```sh
codex plugin list --json
```

For a Git-backed marketplace, fetch updates with:

```sh
codex plugin marketplace upgrade danhuayan-agent-skills
```

Then update/reinstall the changed plugin in the host as needed. A marketplace refresh and an installed-plugin refresh are separate operations. Bump a plugin's version when shipping changed content.

## Claude Code plugins

Inside Claude Code:

```text
/plugin marketplace add danhuayan-snorkel/agent-skill-library
/plugin install chinese-writing@danhuayan-agent-skills
/plugin install paper-reading@danhuayan-agent-skills
```

For local development, add the absolute path of a cloned repository instead of the GitHub slug. Use the plugin manager to refresh the marketplace and installed plugin when updating; restart the session as required by the host.

Plugin skill invocations are `/chinese-writing:chinese-writing` and `/paper-reading:paper-reading`. Directly installed skills use the standalone skill name instead.

## Other agents via the optional Skills CLI

Requires Node.js 22.20+ and repository access. First list what the library exposes:

```sh
npx skills add danhuayan-snorkel/agent-skill-library --list
```

Install globally and choose agents interactively:

```sh
npx skills add danhuayan-snorkel/agent-skill-library -g
```

When running through an agent, pass `-a` explicitly because the installer may otherwise target the current agent automatically. For example, select Cursor:

```sh
npx skills add danhuayan-snorkel/agent-skill-library -g --skill chinese-writing paper-reading -a cursor
```

Omit `-g` for a project installation. From a local clone, `npx skills add . --list` and `npx skills add . -g` use the local source. `skills.sh.json` lists the canonical skill containers; no duplicated skill content is generated.

For skills installed through this CLI:

```sh
npx skills check
npx skills update chinese-writing paper-reading -g
```

This route uses a third-party installer. If your agent supports `SKILL.md` directly, you can instead copy the complete selected folder (including references and screenshots) from `plugins/<plugin>/skills/<skill>/` into its documented skill location. Never copy only `SKILL.md` when supporting resources are needed. Agent support varies; packaging compatibility does not supply missing browser, file, or visualization tools.
