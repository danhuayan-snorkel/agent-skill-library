# Editorial preferences

## Evidence and scope

Initial calibration: 2026-11-03. The user chose 1A, 2B, 3B, 4A, 5A, and either 6A or 6B. Those sentences are approved examples. Broader preferences below are working interpretations, open to refinement.

The desired voice is clear, measured Chinese suited to the actual technical or business audience. Preserve useful explanations without repeating predictable context. Neutral experimental reporting is the default; concise mechanisms work well for commercial copy. These are personal preferences, not claims about all Chinese writing.

## Information and implication

- Treat the entire slide or paragraph as the unit of meaning. A title can omit a modifier if the body conveys it clearly.
- Omit repeated subjects, possessives, and collaboration framing when the referent remains clear. Keep responsibility explicit when it affects a commitment or interpretation.
- Preserve an explanation when it connects a recommendation to a technical reason. Brevity alone is not the goal.
- Prefer specific actions to vague phrases such as 扩大规模 when the object is unclear. State whether the increase concerns data volume, training steps, task difficulty, or deployment.
- Replace rhetorical labels such as So what? with a useful takeaway or an audience-relevant label when that fits the piece.
- Avoid converting observed behavior into an absolute capability claim: observed failures to replan do not establish that a model cannot replan.

## Register and format

Technical reports: define uncommon concepts when needed; retain metrics and meaningful English terms; make experimental conditions and baselines clear. Distinguish observations, interpretations, and recommendations.

Sales presentations: foreground relevance and value supported by the source. Move detail between title and body to improve reading. Do not introduce urgency, guarantees, or emphatic 仅……就…… unless the requested voice warrants them.

Pricing and procurement: explain mechanisms directly. Preserve quantities, acceptance triggers, dates, conditions, and commitment language. Do not substitute procurement volume for accepted volume when discounts depend on acceptance.

UI and charts: name the action or measure, use a unit where ambiguity matters, and choose a compact or explicit label based on space and neighboring context. An event count and an event rate require different labels.

Long-form technical articles: connect paragraphs through reasoning; use examples where they clarify a mechanism. Do not inherit a reference author's jargon, slogans, or formality indiscriminately.

## Final meaning review

Check that the reader can still identify what happened, under what conditions, compared with what, and how strongly the evidence supports the claim. Reordering and omission must preserve recoverable meaning. Retain caveats and details that change a decision. If a source claims an exact doubling from 3.0% to 7.6%, flag the mismatch; an accurate description would be 超过原来的两倍, subject to the editing scope.

## Patterns from the Qwen bilingual samples

The user named Qwen Team blogs as models of high-quality Chinese ↔ English technical writing. Notes are in [the index](corpus/index.md). Patterns worth reusing:

- Define a term once in both languages, such as 强化学习（Reinforcement Learning，RL）, then use the short form. Gloss a named technique on first use, such as 路由回放（Routing Replay）, then keep the name.
- Explain technical mechanisms in the vocabulary of the domain they model. E-Commerce Bench uses 砍价, 铺货, 资金链断裂, and 原地踏步 instead of abstract nouns.
- Put the finding in the heading: 一年下来几乎没有模型将进货价压得更低.
- Keep parallel structures parallel across languages (看什么、看多细、怎么呈现，由你定义). Adapt slogan headlines instead of translating them literally (耳聪目明，办事得力 / Omni Senses. Agentic Delivery.).
- Pair every relative change with its absolute values: 从 25.79% 降至 15.30%，相对下降约 40.7%.
- Convert number grouping between languages (10万 ↔ ¥100,000; 143万 ↔ ¥1.43M) without rounding.

## Common translation drift

Even these high-quality pairs drift. Check explicitly for:

- Numbers that differ between versions (AnchorRatio 0.834 in English vs. 0.88 in Chinese), or hedges such as 多 or 约 added to exact figures (235 billion → 2350 多亿).
- Items dropped from a list. One of three scaling levers survived in the GSPO Chinese version.
- Claims broadened by dropping a qualifier. "GRPO needs Routing Replay for MoE RL" lost "MoE RL".
- Standard terms replaced with near-synonyms (exploration/exploitation → 探索和钻研).
- Headings that change scope (hybrid → 多种; PDF-like → PDF).
- One concept or unit named two ways in a document (1M 长上下文 / 1M 长序列; 回合 / 年份; 基座模型 / 基础模型).
- Calques in the other direction (资金链断裂 → "the cash chain snapped").

## Register examples

- Research posts and paper summaries: the [GSPO pair](corpus/qwen-gspo-bilingual.md).
- Benchmark reports and evaluation narratives: the [E-Commerce Bench pair](corpus/qwen-ecommerce-bench-bilingual.md).
- Product launches and feature pages: the [Omni-Flash pair](corpus/qwen-omni-flash-bilingual.md) and the [Qwen3 pair](corpus/qwen3-release-bilingual.md).

Follow their structure and terminology decisions. Treat 赋能, 沉淀, 潜力巨大, "first" claims, and slogan-style titles as launch-register choices, not defaults for neutral reports. Do not import source product, pricing, or benchmark claims into new work.
