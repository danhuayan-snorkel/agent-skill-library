---
name: model-capability-assessment
description: Build an agent-capability assessment for a named foundation model, with an internal artifact and a client-facing bilingual HTML report drawn from public benchmarks, Snorkel SDS results, and user feedback.
---

# Model capability assessment

Use this when someone asks where a model (for example Qwen 3.8 Max, Kimi K3 or GLM 5) stands as an agent model, wants its capability gaps, or wants a client-facing report for the model's team. The method was first built for the Qwen 3.8 Max case study in November 2026 and is meant to be repeated for any model.

One evidence base produces two deliverables:

1. **Internal artifact** (published Artifact, shared within Snorkel): the full working version, with tabs, highlights and comments, internal names, SDS provenance, and spec cross-checks.
2. **External HTML file** (sent as a file, not published): client-facing, with an English/中文 toggle, numbered citations, and nothing internal.

## 0. Scope the run

Confirm or infer the following, and state them at the top of the work:

- The target model and its exact versions or snapshot dates. Exclude results for sibling or earlier models; do not cite them, even for comparison.
- The model's own products to survey for feedback (for Qwen: Qoder, Qoder CLI, 千问办公).
- Languages for feedback and output. The default for Chinese labs is English and Chinese.
- The snapshot date. Every figure is as of that date.

Keep a task list: taxonomy, public benchmarks, SDS, user feedback, synthesis, internal artifact, external HTML, verification.

## 1. Capability framework

Use the same five axes for every model, and place every result on each axis that applies.

- **C · Capability** (what the model must do): C1 retrieve and ground · C2 remember and learn, including using supplied skills · C3 act through tools, where MCP sits · C4 operate interfaces · C5 write and run code · C6 plan and sustain over long horizons · C7 synthesize and produce deliverables · C8 interact: clarify, model preferences, act proactively, push back · C9 self-monitor: calibration, verifying before done, knowing when to stop · C10 honor boundaries: authority, consent, leakage, injection.
- **H · Harness** (a condition, not a capability): H1 fixed minimal scaffold · H2 the vendor's native product · H3 ablation of one component.
- **S · Setting**: S1 personal · S2 workplace · S3 software · S4 customer-facing · S5 research.
- **E · Environment** (what the test world provides): E1 static packet · E2 stateful apps · E3 simulated user · E4 clock and events · E5 persistent history.
- **Q · Quality**: Q1 success · Q2 reliability (pass^k) · Q3 efficiency (cost, steps and time per solved task) · Q4 safety and integrity · Q5 two-sided calibration.

Optionally, map an error-mode taxonomy onto the C families. An error mode is what a missing capability looks like in a trajectory.

## 2. Survey public benchmark results

For each C family, list the benchmarks that are still maintained at the snapshot date. Record what each isolates, access (open, private or mixed), grading, first release date, the current leader and its score, and the target model's result. Also cover composite indices such as the Vals Index and the Artificial Analysis Intelligence Index.

Use sources in this order:

1. Independent runs on official sites: Vals AI model and benchmark pages, Artificial Analysis model and evaluation pages, Epoch, Snorkel leaderboards, and the benchmark's own board.
2. Aggregators such as BenchLM, BenchmarkList and BenchLeader, only when no official page has the figure. Label them as aggregators.
3. Vendor launch tables, labelled as vendor-reported.

Rules learned from the first run:

- **Cite the official site, not a blog that quotes it.** When a figure comes from a secondary post, find it on the official page and record rank, number of models, harness, attempts and date.
- **Prefer an independent run to a vendor figure,** and show the vendor figure beside it.
- **Record run conditions:** harness, timeout, attempts and effort. A vendor-versus-independent gap is evidence about the harness only when the harness is the only thing that changed. A longer timeout is efficiency (Q3) evidence. Say so when nothing isolates the cause.
- If a board lists two snapshots, say which one each figure comes from.
- Keep "Not checked" (the board was not looked up) separate from "None found".

Give each row a **standing tag** in column 2, next to the benchmark name:

| Tag | Rule |
|---|---|
| Frontier | Rank 1 to 3, or within 5% of the leader |
| Near frontier | Top 10% by rank, or within 10% |
| Average | Top half by rank, or 10 to 35% below |
| Behind | Bottom half by rank, or more than 35% below |
| Disputed | Sources disagree on the class |
| Unverified | Vendor figure with nothing to compare against |
| No data | No result for the target model found |

Use rank where a board gives one; otherwise use the score relative to the listed leader. Above the tables, write one paragraph per capability summarizing the model's standing.

## 3. Survey Snorkel SDS results as frontier evidence

The target model usually has no SDS traces. SDS rows answer one question: is a gap specific to this model, or still open at the frontier?

Sources:

- The master Data Catalog sheet gives official dataset names, capability tags, target benchmark, reference model, Pass@1, harness and grading sample.
- DaaS manifest statistics give, per dataset and model, the number of tasks, mean accuracy, and the shares fully solved and never solved. Get them through the SDS Bench Launcher artifact or a manifest export; ask the user to run the export if this session cannot.
- Notion GTM and outreach kits are a source for named failure modes only. Never use them for scores when catalog or manifest figures exist.

Rules:

- **Put SDS rows inside the capability tables,** next to the open benchmarks they extend: one row per dataset family, with frontier results summarized in one cell. Do not make a separate SDS section.
- Use catalog display names (for example, Terminal-Bench 4.0+ Batch E), not manifest slugs.
- Mark the target model's cell "No data · frontier evidence only".
- Never compare SDS pass rates with public scores or across batches, because each batch was graded on the models current when it was built. Flag duplicate rows between datasets and count mismatches between statistics and traces; do not fix them silently.

## 4. Survey user feedback in English and Chinese

Search in extended mode in both languages. Combine the model name and its coding and office products with terms such as slow, expensive, loops, gives up, 慢, 贵, 死循环, 摆烂, 越改越错 and 积分. Cover Hacker News, Reddit, GitHub issues for the vendor's agent, product forums (for example forum.qoder.com), Chinese technology media and hands-on reviews (ifanr, Huxiu, Zhihu, CSDN, Juejin, Woshipm, SMZDM), and Trustpilot.

For each usable page, record the date, product, model version, harness, a verbatim quote in the original language, and what happened. Then:

- Group the reports into themes, and map each theme to a C or Q code and to a gap.
- Exclude feedback about other models in the same family. Mark product-level posts that do not name the model, and posts about another vendor's model.
- List pages that could not be opened; Zhihu, LINUX DO and CSDN often block.
- Quotes come through a page reader. Say so, and ask the user to spot-check them.

Give each gap a **feedback strength tag**:

| Tag | Meaning |
|---|---|
| Strong | Several independent reports naming the model |
| Mixed | Reports disagree |
| Some | One or two reports |
| Consistent | Fits the benchmark pattern without testing it |
| Thin | Very little |
| None found | No public report located |

Feedback can surface a gap that no benchmark measures, such as degrading or quitting after repeated corrections. Keep that as a users-only gap.

## 5. Synthesize gaps, business context and recommendations

For each candidate gap, record:

- The benchmark standing and the feedback tag.
- Reasoning that combines both views: what each shows, where they agree, and what is not isolated.
- What would close the gap.
- Why it matters, split into **Cowork**, **General capability** and **Verticals**.
- An SDS line where the frontier also fails.

Then:

- Pick three to five **priority gaps** in the order the user sets. List the rest as further observations, such as robustness to run setup, deliverable quality, coding quality, users-only gaps and unmeasured areas.
- List strengths to keep.
- Describe how the gaps connect, labelled as interpretation.
- Suggest next measurements: a controlled harness comparison, cost per solved task as a reported metric, a multi-turn repair evaluation, and results on the unmeasured capabilities.
- In the internal version only, optionally check the "gaps worth building" against current Snorkel specs and client asks.

## 6. Build the internal artifact

Load the artifact design guidance, and the capabilities guidance for highlights and comments. Use the Snorkel template: a midnight hero band with the logo, stone body, Geist with Noto Sans SC, theme tokens with dark mode, and an English/中文 toggle at the top right.

Tabs:

| Tab | Contents |
|---|---|
| Recommendation | Gap table with a feedback column, a benchmarks-versus-users comparison, the feedback survey, landscape gaps against specs |
| Benchmarks | Capability tables with SDS rows, composite indices, tag legend, reading notes, economic-value benchmarks |
| Taxonomy | Board shaded as a heatmap of the model's standing, error-mode mapping, coverage matrix, blending tiers |
| Reference reading | Holistic frameworks, cross-cutting findings, personal versus workplace agents, sources |
| My highlights | Saved highlights and notes |

Declare the `comments` capability (composer only), `db` (a highlights collection) and `user`. Mark internal names with a check-before-sharing note. Before any republish, re-read the live artifact and its comments, because another session may have changed it. Answer comment threads in the thread.

## 7. Build the external HTML

Build it from the same evidence and deliver it as a file, not a published page. It has two tabs and a shared reference list.

- **Recommendation:** one table only, with columns Gap, Benchmark standing (tag and figures), User feedback (tag and quotes), Reasoning (benchmark and feedback, ending with what would close the gap), and Why it matters (Cowork, General capability, Verticals). Follow it with strengths to keep and how the gaps connect.
- **Technical report:**
  1. Introduction.
  2. Capability taxonomy: the unshaded board and the three design choices.
  3. Approach: public benchmarks, Snorkel private SDS, public user feedback in both languages, the standing classification, and limitations.
  4. Benchmark results: the capability tables.
  5. User feedback in depth.
  6. Conclusions: the priority gaps, a table of further observations, and next measurements.
- **References:** paper-style numbered citations such as [1] in the text, with the full list at the bottom. Cite SDS as "Snorkel AI, internal evaluation, unpublished".

Before sending, remove Notion links, client names, spec status, internal draft names, the highlight and comment interface, "my" and "you" phrasing, and catalog, manifest and TBD wording. Search the output for each. Tell the user that SDS figures are present (they must confirm these are cleared to share), that quotes need spot checks, and that Google Fonts may not load in mainland China.

## 8. Write the Chinese

Use the chinese-writing skill (`/chinese-writing:chinese-writing` from this library, or `fdr-skills:chinese-writing`). These decisions from the Qwen run are worth reusing:

- Write in a neutral technical-report register with no promotional emphasis. Keep claim strength: "suggests" becomes 提示……可能, not 说明.
- Keep model, benchmark and metric names in English. Define harness once, as 套在模型外层的智能体框架.
- Use 前沿模型 for frontier models in general and 领先模型 for the leader on a given board. For the target model's self-reported figures, name the vendor (for example 阿里公布); for other vendors, use 厂商自报.
- Standing tags: 领先 / 接近领先 / 中游 / 落后 / 有争议 / 未验证 / 无数据. Feedback tags: 反馈较多 / 反馈不一 / 未找到反馈.
- Use Chinese number grouping without rounding (1802 万, 953.2 万), add 分别 when pairing figures, and put English quotations inside Chinese text in full-width quotes “”.
- After translating, check every number against the English.

## 9. Verify before handing over

- Render each tab in both languages at desktop width and at 400px with Playwright. Expect no horizontal overflow and no page errors, and look at the screenshots.
- Check for duplicate ids, broken in-page anchors and unbalanced tags.
- Make sure every figure in the recommendation table traces to a citation. Re-fetch any figure the user questions from the official page.
- Report what was built, what is unverified, and the decisions that belong to the user, such as sharing SDS data and the order of the gaps.
