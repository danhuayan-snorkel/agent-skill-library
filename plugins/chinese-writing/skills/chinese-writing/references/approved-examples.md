# Approved calibration examples

Approved by the user on 2026-11-03: 1A, 2B, 3B, 4A, 5A, 6A or 6B. Project/vendor names and experiment figures below use placeholders so the examples can be reused without bundling client material. Wording patterns are preserved. These are style examples, not verified experimental claims.

## 1. Preserve distinct training steps — selected A

Awkward: 先用 2.1 风格任务扩大规模，再重新校准并混入 4.0 风格任务。

Approved: 建议的训练方案：先增加 2.1 类任务的训练量，再重新评估模型表现，逐步加入 4.0 类任务。

Working interpretation: name what increases and preserve reassessment as a separate action. Do not mechanically replace every occurrence of recalibration with 重新评估; other contexts may refer to actual score or instrument calibration.

## 2. Name capabilities and describe behavior — selected B

Awkward: 模型在未检查输出的情况下就判定任务成功，且出错后不会重新规划。

Approved: 模型的主要问题在于结果验证和错误恢复：尚未确认任务是否完成就停止执行，遇到错误后也未及时调整策略。

Working interpretation: frame observed behavior in useful capability terms and avoid an unsupported absolute 不会. Check that actual traces support the behavior described.

## 3. Explain why a recommendation works — selected B

Awkward: 训练应从模型能学到东西的地方开始，待信号改善后再逐步提高难度。

Approved: 初期训练应选用模型能够完成一部分的任务，以获得有效的学习信号；随着能力提升，再增加任务难度。

Meaning condition: use this explanation only if the source supports successful attempts supplying the relevant learning signal. It is not a universal statement about reinforcement learning. Do not confuse solving some tasks with receiving partial credit on every task.

## 4. Report experiments neutrally — selected A

Awkward: 在供应商的训练运行中，[N] 个任务将公开 [benchmark] 的 pass@1 从 [X]% 提升至 [Y]%。

Approved: 在供应商的训练实验中，使用 [N] 个任务进行训练后，模型在公开 [benchmark] 测试集上的 pass@1 从 [X]% 提升至 [Y]%。

Alternative not selected: 仅用 [N] 个任务训练，模型在公开 [benchmark] 测试集上的 pass@1 就从 [X]% 提升至 [Y]%。

Working interpretation: avoid adding promotional emphasis. Preserve model identity and evaluation conditions from the actual source even when absent from this short excerpt.

## 5. State the pricing mechanism — selected A

Awkward: 价格按所有团队的验收总量计算，每一笔订单都计入总量，共同争取最优价格。

Approved: 各团队的验收量合并计算，按总量享受相应折扣。

Working interpretation: direct commercial wording can carry the message without restating every implication. Preserve the aggregation period and other qualifications if the offer specifies them.

## 6. Fit labels to context — both approved

Awkward: 因预算上限结束的运行

Approved explicit label: 达到预算上限而终止的运行占比

Approved compact label: 预算耗尽终止率

Meaning condition: these labels describe a rate, not a count. Establish what budget means before expanding it to token, time, or tool-call budget. Use the longer label when space permits or the compact form is unclear.
