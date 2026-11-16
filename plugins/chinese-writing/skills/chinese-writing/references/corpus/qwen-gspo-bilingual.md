# Qwen blog: GSPO (EN ↔ ZH)

- Page: https://qwen.ai/blog?id=gspo (switch language with the site's language toggle)
- Raw text: English https://docs.qwenlm.ai/research/gspo/index.json; Chinese https://docs.qwenlm.ai/research/gspo/index.zh.json (Markdown tokens; read each token's `raw` field)
- Title: "GSPO: Towards Scalable Reinforcement Learning for Language Models"
- Author / organization: Qwen Team. Paper: https://huggingface.co/papers/2507.18071
- Publication date: 2025-07-27
- Type: bilingual pair / research blog. English is probably the original, since it accompanies an English paper.
- Audience and format: RL and LLM researchers; short post with formulas, figures, and a findings summary
- Status: pending. The pair was compared on 2026-11-04. The user flagged Qwen blogs as high-quality Chinese ↔ English technical writing but has not reviewed specific passages.

## What works

| English | Chinese | Why it works |
|---|---|---|
| Reinforcement Learning (RL) | 强化学习（Reinforcement Learning，RL） | Defines the term once in both languages, then uses RL throughout. |
| sequence-level clipping, rewarding, and optimization | 在序列层面执行裁剪、奖励和优化 | Turns stacked modifiers into a verb phrase. |
| group relative advantage | 组内相对优势 | Compact, standard RL term. |
| length normalization to reduce variance | 长度归一化以降低方差 | Keeps the purpose clause short. |
| Routing Replay | 路由回放（Routing Replay）, then Routing Replay | Gives a Chinese gloss on first use and keeps the named technique in English afterward. |
| training-inference disaggregated frameworks | 训推分离框架 | Uses the compact term practitioners say. |
| noisy and inefficient | 有噪和低效 | Short paired adjectives. |
| GSPO has obviated the need for this strategy | GSPO 则无需该策略 | Plain contrast with 则 instead of a literal "obviated". |
| feel free to give us a citation | 欢迎引用！ | Natural closing formula. |

English stays for algorithm names (GSPO, GRPO), token, partial rollout, RL scaling, MoE, benchmark names, and math. Chinese is used for 重要性比率, 似然, 基线, 冷启动模型, 收敛, 数量级, 裁剪.

Structure is identical across languages: headings, formulas, and figures align one-to-one. That makes this pair a good model for research posts where the reader may check both versions.

## What to avoid (drift found in the pair)

- **Dropped items from a list.** In the English, continued improvement comes from three levers: training compute, query-set updates, and generation length. The Chinese keeps only 通过增加算力, which loses the other two findings.
- **A broader claim than the source.** The English says GRPO needs Routing Replay for MoE RL to converge. The Chinese drops "MoE RL" (GRPO 必需采用 Routing Replay 训练策略才能正常收敛), which reads as a claim about GRPO in general.
- **Awkward adverbs.** "inherently resolves" became 根本地解决了. 从根本上解决了 is the natural form.
- **Time words.** "during long training" became 长期训练, which suggests calendar time. 长时间训练 or 长步数训练 is closer.

## Scope

Use this pair for research posts and paper summaries: defining terms once, glossing a named technique, compact Chinese for RL concepts, and keeping formulas aligned. Performance claims are the authors' and are not independently verified.
