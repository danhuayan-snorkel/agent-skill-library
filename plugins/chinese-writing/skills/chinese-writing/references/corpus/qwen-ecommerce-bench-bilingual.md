# Qwen blog: E-Commerce Bench (ZH ↔ EN)

- Page: https://qwen.ai/blog?id=e-commerce-bench (switch language with the site's language toggle)
- Raw text: https://qwen.ai/api/v2/article/?language=zh-CN&path=e-commerce-bench&type=qwen_ai (use `language=en-US` for English; the HTML is in `data.content`)
- Titles: 「E-Commerce Bench：长程经营，多维评估」 / "E-Commerce Bench: Long-Horizon Operations, Multi-Dimensional Evaluation"
- Author / organization: Qwen Team, with Taobao & Tmall Group (淘天集团)
- Publication date: 2026-09-03
- Type: bilingual pair / benchmark report. Chinese is probably the original: the Chinese uses natural colloquial idioms, and the English sometimes calques them.
- Audience and format: AI researchers and the business-minded technical reader; narrative benchmark report with figures and per-capability findings
- Status: pending. The pair was compared on 2026-11-04. The user flagged Qwen blogs as high-quality Chinese ↔ English technical writing but has not reviewed specific passages.

## What works in the Chinese

The best native Chinese register among the samples. It explains a technical benchmark in the vocabulary of the domain it simulates (shop-keeping), with short clauses and concrete verbs:

- Domain verbs instead of abstract nouns: 跟供应商砍价, 定价上架, 盯促销节奏, 管库存和现金流, 一月把货压满, 铺货.
- Idioms that carry a finding: 忙了一年等于原地踏步 (a year of work that ends where it began), 资金链断裂, 冰山一角, 清一色是闭源模型, 真正的分水岭不在"挑谁聊", 一年下来倒也没因此翻车.
- Contrast compressed into parallel phrases: 想清楚再动和边动边想，代价不一样.
- Plain explanation of a design decision: LLM只负责把内核定好的决定说成人话; 多轮砍价的真实感还在，采样噪声却没了.
- Headings that state the finding: 一年下来几乎没有模型将进货价压得更低; 年终总资产只是冰山一角：七维能力拆解.
- Numbers in Chinese conventions: 10万本金, 143万, and 14.31倍 alongside exact percentages (0.12%, 20.11%, 26.4%).
- Statistics in plain words: 零假设, 两个标准差, and 1.0表示模型的出价顺序和随机顺序看不出区别.

## What works in the English rendering

| Chinese | English | Why it works |
|---|---|---|
| 想清楚再动和边动边想，代价不一样 | thinking it through first and figuring it out along the way carry different prices | Keeps the parallel structure and the cost framing. |
| 忙了一年等于原地踏步 | a full year of work that ends where it began | Gives the meaning, not the image. |
| 10万本金 / 143万 | ¥100,000 / ¥1.43M | Converts 万 grouping to Western notation and adds the currency sign. |
| 评测就变成了越狱比赛 | turns the benchmark into a jailbreaking contest | Direct and idiomatic. |
| 真正的分水岭不在"挑谁聊" | The real dividing line is not which suppliers a model chooses to talk to | Expands the elliptical quote into a full clause. |

## What to avoid (drift found in the pair)

- **Numbers that differ across versions.** Qwen3.8-Max-Preview's AnchorRatio is 0.834 in the English and 0.88 in the Chinese. When adapting either version, check figures against the other or the paper, and flag mismatches.
- **One unit named two ways.** In Figure 4's caption, 各5个年份 conflicts with 回合 elsewhere; the English says episodes throughout. Keep one term per unit (回合 or 轮).
- **Calques in the English.** 资金链断裂 became "the cash chain snapped". "ran out of cash" or "cash flow broke down" is more natural English.
- **Untranslated captions.** The Chinese figure captions mix in English layer names (agent loop层, tool层, environment层) and keep "Figure 1:" labels. Use 图 1 and translate layer names, or format the identifiers as code.
- **Promotional closings.** The Chinese ends with 潜力巨大 where the English says "plenty of headroom left". Keep the measured version for neutral reports.

## Spacing note

This post omits spaces between Chinese and Latin text or digits (18个模型, Agent需要). The GSPO and Qwen3 posts add them (Qwen3 模型, 18 万亿个 token). Either is acceptable. Pick one style per document and follow any style guide the assignment specifies.

## Scope

Use this pair for benchmark reports, evaluation write-ups, and business-facing technical narratives, especially for making findings concrete and readable without losing exact numbers. Rankings and model results are the publisher's claims, not verified facts.
