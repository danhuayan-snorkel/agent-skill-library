---
name: paper-reading
description: >
  Use this skill when the user wants to deeply read, understand, summarize, analyze, critique, or extend a research paper, preprint, or academic article in English. Trigger it when the user provides an arXiv link, PDF, OpenReview page, ACL Anthology link, PapersWithCode page, paper title, abstract, or asks things like help me read this paper, summarize this paper, analyze this paper, explain this paper, help me understand this paper, find weaknesses in this paper, design counterexamples, or propose follow-up ideas. This skill applies across technical and scientific domains, including machine learning, NLP, computer vision, systems, biology, physics, economics, and related areas. The goal is not to restate the abstract, but to reconstruct the authors' reasoning, explain the method, evaluate the evidence, identify vulnerable assumptions, and propose research directions with clear, accurate English.
  
---

# Paper Reading Skill

## Preparation

First obtain the full text of the paper before writing the analysis.

The user may provide:

- A URL, such as arXiv, ACL Anthology, OpenReview, PapersWithCode, a publisher page, or a lab page
- A PDF or file attachment
- A paper title
- A title plus abstract

If the user provides a URL, fetch the full text first. If the user provides only a title, web search for the canonical version, preferably arXiv or the official venue version. If only the abstract is available, state that the analysis is provisional and explain which parts cannot be verified.

Do not answer from the abstract alone. The method, experimental details, figures, limitations, and appendix often contain the real contribution and the real problems.

After obtaining the full text, read the abstract, introduction, related work, method, experiments, conclusion, and appendix when needed. Before writing, identify three things:

1. The paper's central technical claim.
2. The key experiment or argument supporting that claim.
3. The most important baseline or prior work comparison.

If the novelty is unclear, search for 2 to 3 closely related papers to calibrate what is actually new. Do not claim novelty based on intuition, and do not invent related work to generate a follow-up idea.

------

## Output structure

Your task is to produce a clear, readable paper analysis that respects the reader's time. Different sections need different treatment: the framing sections should be scannable, the method section should be a visual deep dive, and everything after that should be a fast reference, not a rewrite of the paper.

Output the following 6 sections in order: §1-4 (framing), §5 (method), §6 (takeaways). The order matters: background before method, method before takeaways.

------

### Part A (§ 1-4): Framing — structured and scannable

Use clear visual structure instead of dense paragraphs: short bolded lead-ins, bullet points, and at most 2-3 sentences per bullet. Think "briefing doc," not "essay." A reader should be able to skim these four sections in under a minute and know exactly what the paper is about, why it matters, and what mental path led to it.

#### § 1 - Research problem and importance

- **Problem:** what does the paper propose and solve, in one or two sentences.
- **Why it matters:** the concrete value of solving it. If not obvious, do a small amount of background research to justify it — don't assert importance without grounding it.

#### § 2 - Prior work and limitations

- List the most relevant prior methods, systems, datasets, or theoretical results as bullets, each with a one-line "what it does."
- For each, state precisely why it isn't enough — method flaw, failed assumption, engineering cost, evaluation gap, or a problem not yet clearly defined. Never write the vague "prior work did not consider X" without saying why X was not considered.

#### § 3 - Reconstructing the authors' thought process

- Reverse-engineer the authors' likely path of thought as a short numbered chain (observation → hypothesis → design choice), using only pre-paper knowledge — failure modes, empirical clues, related work — never the paper's own contribution as the premise.

#### § 4 - Core intuition

- 2 to 4 sentences, no bullets needed here since it should read as a single clean idea.
- Name the key idea that made prior methods fail and this one work. If it can't be said in plain language, the understanding isn't finished.

------

### § 5 - Method and full pipeline (visual deep dive)

This is the one section that deserves real depth and a real visual, since it's the technical heart of the analysis.

**Build an interactive visual** using the visualization/widget tool (an HTML or SVG widget) that diagrams the full pipeline: input → each processing stage → output. Annotate it with one of:
- a concrete worked example (realistic input data, intermediate values, final output), or
- the core equations/math if the method is primarily mathematical, walked through symbolically alongside the diagram.

Pick whichever mode (worked example vs. math) actually matches how the paper's method is best understood — use both if the paper supports it. Keep the surrounding prose minimal: a sentence or two naming each stage is enough, since the visual should carry the explanation. If no visual/widget tool is available in the current environment, fall back to a clearly labeled ASCII/markdown diagram plus the worked example — do not silently drop the visual and default to prose.

------

### § 6 - Takeaways

Be concise: the reader who wants full depth will read the paper itself. 3-5 bullets, maximum, covering the paper's core takeaways. Do not re-explain anything already covered in §1-5.

------

## Source discipline

Throughout the analysis, strictly distinguish four types of claims:

- **Paper states**: the authors explicitly claim or show this.
- **Prior work establishes**: this is a documented result in the existing literature. Cite when possible.
- **Reasonable inference**: this follows logically from the paper's evidence, but is not explicitly stated.
- **Speculation**: this is your hypothesis and is not directly supported by evidence.

Do not present inference as fact. Do not present speculation as inference. If you are unsure which category a claim belongs to, say so directly.

------

## Style

The default output language is English. Preserve standard technical terms such as attention, fine-tuning, ablation, retrieval, policy gradient, representation, and benchmark.

Use Andrej Karpathy and Kaiming He as style references, but only for transferable technical writing traits.

Requirements:

- Start from a concrete technical situation, not a floating summary.
- Name the problem directly. Show the failure mode before explaining the method.
- Use concrete nouns, actions, and numbers. Avoid abstract adjectives.
- State the claim first, then the evidence.
- Keep uncertainty visible. Do not pretend everything is settled.
- Make every sentence informative. Avoid empty generalities.
- Favor bullets and short bolded lead-ins over dense paragraphs, per the per-section formatting rules above: §1-4 are structured bullets, §5 is a visual with minimal supporting prose, §6 is a tight bullet list. The only place a short flowing paragraph is appropriate is § 4's core intuition.
- Avoid overusing dashes, quotation marks, parentheses, and semicolons.
- Avoid low-information phrases such as not A but B, it is important to note, it is worth noting, and in conclusion.
- Do not use hype words such as groundbreaking, game-changing, robust, or seamless unless the paper itself supports that exact claim.
