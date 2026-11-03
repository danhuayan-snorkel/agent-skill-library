# Chinese Writing · 中文表达与翻译

A personal Codex plugin for natural Chinese technical and business writing: translation, adaptation, editing, and drafting from notes. Covers research explanations, sales decks, reports, pricing, and UI copy.

Version 0.1.1 includes six user-approved calibration choices, contextual terminology, format-aware editorial guidance, and six supplied screenshots organized into four annotated Chinese writing references. Broader style interpretations and glossary defaults remain provisional.

## Use it

Register this repository as a local marketplace from its root:

```sh
codex plugin marketplace add .
```

Then open the desktop app's plugin directory, find **Chinese Writing** in the **Chinese Writing** marketplace, and install it. Start a new chat to test discovery. This repository is a plugin package; creating it does not automatically install it in the app.

Example requests:

```text
Use $chinese-writing to adapt this report for a Chinese ML research audience.
Preserve metrics and experimental conditions. Explain unfamiliar terms where useful.
```

```text
Use $chinese-writing to rewrite the Chinese in this sales deck.
Make the message natural for a Chinese technical buyer and keep pricing terms precise.
```

```text
Use $chinese-writing to draft a Chinese technical explanation from these notes.
```

The skill can also be selected automatically for matching tasks. File creation and rendering use the host's available document, presentation, or web capabilities. No API key or external service is bundled.

## Add Chinese references later

The editable reference folder is:

[`plugins/chinese-writing/skills/chinese-writing/references/corpus/`](plugins/chinese-writing/skills/chinese-writing/references/corpus/index.md)

1. Save a Chinese article or a reference note there. Markdown or plain text is easiest to read; an exported HTML/PDF can accompany a note.
2. Copy `reference-template.md` and record the source, audience, passages you like, and why.
3. Add a link to `index.md`, or ask Codex to organize the new reference for you.

For example:

```text
Add this article to the Chinese Writing references in this repository.
I like how it introduces English technical terms and explains the mechanism.
Record those preferences; treat other style observations as tentative.
```

You can also drop in a file without annotating it and ask Codex to help. The skill can discover unindexed files; annotations make your preferences clearer. Update this source repository rather than an installed cache. Refresh/reinstall the plugin as needed so later chats receive updated references.

Use Chinese articles for native composition, bilingual edits for adaptation decisions, and terminology sources for contextual usage. A post's inclusion does not approve every expression in it. Keep original attribution; reference notes can use links and short excerpts. The six supplied writing-reference screenshots are bundled with attribution notes; private source decks and HTML files are not bundled. An ignored `private/` folder is available for local originals if needed.

## Files to refine

| File | Purpose |
|---|---|
| [SKILL.md](plugins/chinese-writing/skills/chinese-writing/SKILL.md) | Core workflow and reference routing |
| [editorial.md](plugins/chinese-writing/skills/chinese-writing/references/editorial.md) | Working voice and format preferences |
| [approved-examples.md](plugins/chinese-writing/skills/chinese-writing/references/approved-examples.md) | Six selected examples and their meaning conditions |
| [terminology.md](plugins/chinese-writing/skills/chinese-writing/references/terminology.md) | Context-sensitive candidate glossary |
| [corpus/index.md](plugins/chinese-writing/skills/chinese-writing/references/corpus/index.md) | Future Chinese articles and annotations |
| [evals/README.md](evals/README.md) | Fresh cases for checking behavior |

The plugin has a portable root manifest and a Codex compatibility manifest; both refer to the same skill content. The repository marketplace points to `plugins/chinese-writing`. Packaging follows [OpenAI's plugin documentation](https://developers.openai.com/plugins/build/plugins).

## Validate

Requires Python 3, with no third-party packages:

```sh
python3 scripts/validate.py
```

This checks manifests, package paths, skill metadata, and local Markdown links. It does not measure writing quality or verify installation in a particular app build. Use the fresh cases in `evals/` to assess that separately.
