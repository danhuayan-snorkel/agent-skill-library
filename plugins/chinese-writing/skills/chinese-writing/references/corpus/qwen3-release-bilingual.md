# Qwen3 release blog (EN ↔ ZH)

- English: https://qwenlm.github.io/blog/qwen3/ ("Qwen3: Think Deeper, Act Faster")
- Chinese: https://qwenlm.github.io/zh/blog/qwen3/ ("Qwen3：思深，行速")
- Author / organization: Qwen Team. Both versions are official; which was written first is not stated.
- Publication date: 2025-04-29
- Type: bilingual pair / model release announcement
- Audience and format: developers and AI practitioners; announcement plus training overview and usage guide
- Status: pending. The pair was compared on 2026-11-04. The user has not reviewed specific passages.

## What works

| English | Chinese | Why it works |
|---|---|---|
| Today, we are excited to announce … | 今天，我们宣布推出 … | Drops the excitement filler. Chinese announcements rarely need it. |
| outcompetes QwQ-32B with 10 times of activated parameters | 激活参数数量是 QwQ-32B 的 10%，表现更胜一筹 | The English is ambiguous. The Chinese states the ratio explicitly, then the result. |
| Qwen2.5-Math and Qwen2.5-Coder | 这两个数学和代码领域的专家模型 | Adds a short gloss so readers who do not know the model names can follow. |
| open-weighting | 开源了 … 的权重 | Names what is released instead of coining a verb. |
| headings: Pre-training / Post-training / Friends of Qwen | 预训练 / 后训练 / Qwen 的朋友们 | Plain, parallel headings. |

English is kept for model names, frameworks, MoE, Dense, token, Agent, MCP, Base/Instruct, and API endpoint. Established ML concepts get Chinese: 思考模式, 思考预算, 激活参数, 上下文长度, 长思维链, 冷启动, 强化学习.

## What to avoid (drift found in the pair)

- **Hedges added to exact numbers.** "235 billion total parameters" became 2350 多亿, and "30 billion" became 约 300 亿. The source gives exact figures; write 2350 亿 and 300 亿.
- **Scope changes in headings.** "Hybrid Thinking Modes" became 多种思考模式. Hybrid (two modes in one model) is not the same as several modes. 混合思考模式 keeps the meaning.
- **Stage names that change meaning.** "reasoning-based RL" became 长思维链强化学习. "Scaling up computational resources for RL" was compressed to 大规模强化学习, which loses the point about compute.
- **Wrong standard terms.** "exploration and exploitation" became 探索和钻研能力. The standard RL pair is 探索与利用.
- **Narrowed scope.** "PDF-like documents" became PDF 文档.
- **Inconsistent terms for one concept.** "base model" appears as both 基座模型 and 基础模型 within a few paragraphs. Pick one per document.
- **Content that does not match.** The Chinese adds a deployment tip (removing `--reasoning-parser`) that the English page lacks. Cross-language versions can diverge, so do not treat either as an exact translation without checking.
- **Promotional verbs.** 赋能 and 鼎力支持 suit a corporate register. Do not import them into neutral technical writing.

## Scope

Use this pair for release notes, model cards, and announcement-style technical posts: what to keep in English, how to present parameter counts, and how to order headings. Model capabilities and benchmark comparisons are the publisher's claims, not verified facts.
