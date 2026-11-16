# Contextual terminology

These are initial candidate defaults, not a fully user-approved glossary. Use source definitions, audience, and explicit user corrections. Preserve formal dataset names, product names, code identifiers, paths, model names, and metric notation. Retain English when more natural for specialists; define it when helpful.

| English / context | Candidate Chinese | Decision rule |
|---|---|---|
| curriculum: task mix and order | 训练方案；训练数据组合与顺序 | 训练课程 is usually misleading here. Use 课程学习 for the actual method curriculum learning. |
| training run | 一次训练实验；一次训练 | Distinguish an experiment from its individual executions. |
| rollout | rollout；一次任务执行；采样轨迹 | Determine whether the unit is a sampled trajectory, task attempt, or another defined object. Do not collapse these units. |
| trace | 执行轨迹；执行记录 | Choose trajectory versus reader-facing log by context. |
| judge | 评判模型；评估器；评审人员 | Establish whether model-based, automated, or human. |
| verifier | 验证器；验证程序 | Explain what is checked if necessary. Keep distinct from judge when roles differ. |
| held-out set | 留出集；未参与训练的评测集 | State only the exclusion boundary supported by the source. Do not infer complete contamination freedom. |
| benchmark | 基准测试；评测基准；benchmark | Preserve official names; use 评测 when generic meaning suffices. |
| pass@k | pass@k | Preserve notation and the source's definition/estimator. Do not equate pass@1, pass@k, mean attempt success, and unique tasks solved. |
| base: model before further training | 基础模型；训练前模型 | 基础 alone may be confused with a task tier. |
| base/core/advanced/frontier: task tiers | 基础 / 核心 / 进阶 / 前沿 | Preserve formal tier mapping until approved alternatives exist; define once if unclear. |
| headroom | 提升空间；与对比模型的差距 | An observed gap is not a guarantee training will recover it. |
| uplift / lift | 提升；训练后提升 | Name the metric; distinguish relative change from percentage points. |
| cost per success: currency | 每完成一个任务的平均成本 | Retain currency and aggregation definition. |
| cost per success: tool-call count | 每完成一个任务所需的工具调用次数 | Do not label a count as monetary cost. Preserve whether calls from unsuccessful attempts enter the aggregate. |
| budget | 预算；执行预算 | Identify tokens, calls, time, money, or another resource before becoming more specific. |
| policy | 规则；策略；政策 | Environment rules, learned policy, and public policy differ. |
| alignment | 对齐；一致性 | Model alignment, rubric agreement, and project coordination differ. |
| datapoint | 数据条目；条数据；样本；任务 | Choose the actual unit, especially for pricing. Do not equate tasks and trajectories without evidence. |
| acceptance: delivery terms | 验收 | Keep separate from purchase, delivery, payment, and use. |
| spec: dataset delivery | 数据规格；交付规范 | Use the official name if defined. Code/API specs may differ. |
| minimum commitment | 最低承诺采购额；最低采购承诺 | Preserve whether amount, quantity, or another obligation. |
| token: LLM text unit | token；Token；词元 | Avoid 令牌 in ML contexts because it suggests an authentication token. Evidence: the Qwen posts keep token (GSPO, Qwen3) or Token (Omni-Flash). |
| dense model | Dense 模型；稠密模型 | Pick one per document. Qwen3 keeps Dense. |
| importance ratio / group relative advantage | 重要性比率 / 组内相对优势 | Evidence: GSPO Chinese version. |
| training-inference disaggregation | 训推分离 | Compact practitioner term. Evidence: GSPO. |
| null hypothesis / standard deviation | 零假设 / 标准差 | Evidence: E-Commerce Bench. |
| reservation price | 保留价 | Evidence: E-Commerce Bench. |
| long-horizon (task, operations) | 长程（任务、经营） | Evidence: E-Commerce Bench, Omni-Flash. 长周期 also appears (Qwen3). Pick one per document. |
| context window | 上下文窗口；长上下文 | Do not alternate with 长序列 for the same feature (Omni-Flash drift). |
| relative vs. absolute reduction | 从 A 降至 B，相对下降约 C% | State both and label the relative change. Evidence: Omni-Flash. |
| base / pre-trained model | 基座模型；基础模型 | Pick one per document. Do not confuse with a base task tier. |
| exploration and exploitation | 探索与利用 | Standard RL pair. Do not paraphrase it (the Qwen3 Chinese has 探索和钻研). |
| supervised (training) | 监督；监督式 | 监管 means regulation or oversight. |
| activated parameters | 激活参数 | Keep total and activated counts distinct and exact. |
| API parameters / config field names | keep English (`reasoning_effort`, `enable_thinking`) | Use Chinese for the concept in prose (推理深度, 思考模式). |

When adding entries, record context, preferred form, alternatives, and approval status. Blog usage is evidence for that context, not automatic global approval.
