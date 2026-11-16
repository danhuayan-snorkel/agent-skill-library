---
name: model-capability-assessment
description: Build an agent-capability assessment for a named foundation model, with an internal artifact and a client-facing bilingual HTML report drawn from public benchmarks, Snorkel SDS results, and user feedback.
---

# Model capability assessment

Use this when someone asks where a model (for example Qwen 3.8 Max, Kimi K3 or GLM 5) stands as an agent model, wants its capability gaps, or wants a client-facing report for the model's team. The method was first built for the Qwen 3.8 Max case study in November 2026 and is meant to be repeated for any model.

One evidence base produces two deliverables:

1. **Internal artifact** (published Artifact, shared within Snorkel): the full working version, with tabs, highlights and comments, internal names, SDS provenance, and spec cross-checks.
2. **External HTML report**: client-facing, with an English/中文 toggle, numbered citations, and nothing internal. Publish it as a private artifact with comments enabled so the account team can review it, then deliver the final standalone `.html` file for sending.

The work runs in four phases: collect prerequisites, research in parallel with subagents, synthesize, then build and review.

## 0. Collect prerequisites first

Ask for everything below in one message before starting research, using a multiple-choice question tool where one is available. The SDS inputs cannot be found by searching, and they change the conclusions. In the Qwen run, adding the target model's own SDS traces late moved efficiency to the top of the evidence, overturned a listed strength, and downgraded coding from Average to Behind.

| Input | Required? | What to ask for | If missing |
|---|---|---|---|
| Target model and versions | Required | Exact name and every snapshot (preview, launch, updates, with dates). Which snapshot is "current" and so goes unlabelled. | Infer from launch posts and state the assumption at the top of the work. |
| SDS results for the target model | Required for full scope | A per-dataset table for the target model and comparison models on the same task sets: tasks, attempts per task, pass@1 and pass@k, harness, time limit, share of trials that timed out or errored, difficulty mix (frontier-only or mixed), the target model version the traces came from, and the manifest date. Trace folders or manifest exports are fine; summaries are needed for any run whose raw traces you cannot read. | Run with frontier-only SDS rows marked "No data · frontier evidence only", and say in the report and to the user that the target model was not run. |
| SDS naming source | Required if SDS is used | The master Data Catalog sheet or the SDS Bench Launcher artifact, so edition and series slugs map to catalog display names. | Match on reference-model scores (see section 4) and flag every inferred mapping. |
| Sharing constraints | Required for the external report | Which SDS figures are cleared for this client. Which models or customers must not appear (for example other customers' private models in an onsite run). Whether competitor model names may be shown. | Exclude unreleased or private third-party models; tell the user SDS figures still need clearance. |
| Products and channels for feedback | Optional | The model's own agent products (for Qwen: Qoder, Qoder CLI, 千问办公) and languages to cover. | Find them from the vendor's site. |
| Gap ordering and emphasis | Optional | Whether the account team already has a preferred order or framing for the priority gaps. | Order by evidence strength, then ask before the external version. |
| Template and prior work | Optional | A theme or template artifact, and any earlier internal assessment to reuse. | Use the Snorkel template in section 8. |
| Next step for the cover note | Optional | What the client is being asked to do next (for example evaluating the next model, scoping data needs). | Leave the cover note's next step generic. |

State the scope at the top of the work: target model and snapshots, snapshot date for all figures, products surveyed, languages, and which prerequisites were missing. Keep a task list: prerequisites, research fan-out, SDS analysis, synthesis, internal artifact, external report, Chinese, verification.

## 1. Capability framework

Use the same five axes for every model, and place every result on each axis that applies.

- **C · Capability** (what the model must do): C1 retrieve and ground · C2 remember and learn, including using supplied skills · C3 act through tools, where MCP sits · C4 operate interfaces · C5 write and run code · C6 plan and sustain over long horizons · C7 synthesize and produce deliverables · C8 interact: clarify, model preferences, act proactively, push back · C9 self-monitor: calibration, verifying before done, knowing when to stop · C10 honor boundaries: authority, consent, leakage, injection.
- **H · Harness** (a condition, not a capability): H1 fixed minimal scaffold · H2 the vendor's native product · H3 ablation of one component.
- **S · Setting**: S1 personal · S2 workplace · S3 software · S4 customer-facing · S5 research.
- **E · Environment** (what the test world provides): E1 static packet · E2 stateful apps · E3 simulated user · E4 clock and events · E5 persistent history.
- **Q · Quality**: Q1 success · Q2 reliability (pass^k) · Q3 efficiency (cost, steps and time per solved task) · Q4 safety and integrity · Q5 two-sided calibration.

Optionally, map an error-mode taxonomy onto the C families. An error mode is what a missing capability looks like in a trajectory.

## 2. Research in parallel with subagents

Once the prerequisites are in hand, send the independent research streams to subagents in a single turn so they run in parallel. Each subagent starts cold, so its brief must carry the target model, snapshots, snapshot date, capability framework, source rules and the exact return format. Copy the briefs from [subagent briefs](references/subagent-briefs.md) and fill in the placeholders.

| Stream | Subagents | Returns |
|---|---|---|
| Public benchmarks | Two or three, split by capability family (for example C1–C3, C4–C6, C7–C10 plus composite indices) | One row per benchmark in the benchmark schema, with official-page sources |
| User feedback, English | One | One row per usable page in the feedback schema, verbatim quotes |
| User feedback, Chinese | One | Same schema, quotes in the original Chinese with an English gloss |
| SDS analysis | One, given the user's SDS files | Per-dataset standings, timeout and error shares, catalog names, mismatches |

Subagents research and report; they do not write the deliverables, edit files outside their scratch space, or publish anything. When they return:

1. Merge and deduplicate their tables. Where two subagents disagree on a figure, keep both and resolve it from the official page.
2. Spot-check the figures that will carry a priority gap or a strength against the official source yourself. Re-fetch any figure the user questions.
3. Record what each subagent could not reach (blocked pages, permission timeouts) and keep those labelled "Not checked", not "None found".

If the session has no subagent tool, run the same streams yourself in the same order.

## 3. Public benchmark rules

For each C family, list the benchmarks that are still maintained at the snapshot date. Record what each isolates, access (open, private or mixed), grading, first release date, the current leader and its score, and the target model's result. Also cover composite indices such as the Vals Index and the Artificial Analysis Intelligence Index.

Use sources in this order:

1. Independent runs on official sites: Vals AI model and benchmark pages, Artificial Analysis model and evaluation pages, Epoch, Snorkel leaderboards, and the benchmark's own board.
2. Aggregators such as BenchLM, BenchmarkList and BenchLeader, only when no official page has the figure. Label them as aggregators.
3. Vendor launch tables, labelled as vendor-reported, with the snapshot they were published for.

Rules:

- **Cite the official site, not a blog that quotes it.** Record rank, number of models, harness, attempts and date.
- **Prefer an independent run to a vendor figure,** and show the vendor figure beside it.
- **Record run conditions:** harness, timeout, attempts, effort and model version. A vendor-versus-independent gap is evidence about the harness only when the harness is the only thing that changed. Say so when the version also differs.
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

## 4. Snorkel SDS results

SDS rows sit inside the capability tables, next to the open benchmarks they extend: one row per dataset family, never a separate section. Use catalog display names (for example Terminal-Bench 2.0+ Batch D, SWE-Bench CLI+ Batch B), not series slugs or manifest names.

**When the target model has SDS traces** (the preferred case):

- Rank it against the other models on the same task set, with pass@1 and pass@k, and tag it with the same standing rules as public rows.
- Label the version the traces came from. If it is not the current snapshot, say so in the standing note and the result cell.
- Report the share of trials that timed out or errored next to the score. In the Qwen run, 76–86% of trials on the hardest sets hit the agent timeout, which became the strongest efficiency evidence and qualified the long-horizon and coding gaps. Confirm with the user whether timed-out trials count as failures or are excluded from the pass rate, and do not state either until confirmed.
- Keep frontier-difficulty sets and mixed-difficulty sets apart, and say which is which. The gap to the leader is usually much larger on frontier-only sets. Leaderboard sets (for example 200 tasks, 5 attempts) and onsite runs (for example 3 attempts, pass@any) are not directly comparable.
- Drop SDS rows that have no target-model result from the external report. Keep them in the internal artifact as frontier-only evidence.
- Highlight SDS rows in both deliverables with a distinct tint and left bar, plus a legend key.

**When the target model has no SDS traces:** SDS rows answer one question only: is a gap specific to this model, or still open at the frontier? Mark the target model's cell "No data · frontier evidence only".

**Always:**

- Never compare SDS pass rates with public scores or across batches, because each batch was graded on the models current when it was built.
- When only edition or series slugs are available, map them to catalog batches by matching a reference model's score (for example Opus 5.5 at 40.4% on both the edition and the catalog batch). List each inferred mapping for the user.
- Flag duplicate rows between datasets, count mismatches between statistics and traces, and manifests with zeroed or withheld results. Do not fix them silently; use the last complete manifest and say which.
- Exclude other customers' private or pre-release models from anything client-facing, even when they appear in the same run.
- Notion GTM and outreach kits are a source for named failure modes only. Never use them for scores when catalog or manifest figures exist.

## 5. User feedback in English and Chinese

The two feedback subagents follow the brief in [subagent briefs](references/subagent-briefs.md). Their sources include Hacker News, Reddit, GitHub issues for the vendor's agent, product forums (for example forum.qoder.com), Chinese technology media and hands-on reviews (ifanr, Huxiu, Zhihu, CSDN, Juejin, Woshipm, SMZDM), and Trustpilot.

For each usable page, record the date, product, model version, harness, a verbatim quote in the original language, and what happened. Then:

- Group the reports into themes, and map each theme to a C or Q code and to a gap.
- Label the model version of every report from its date and wording (preview, launch, later update, or not stated). Exclude feedback about other models in the same family. Mark product-level posts that do not name the model, and posts about another vendor's model.
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

Feedback can surface a gap that no benchmark measures, such as degrading or quitting after repeated corrections. Keep that as a users-only gap. When most of a Strong tag rests on preview-era reports, tell the user before the external version.

## 6. Label model versions

Models often ship as a preview, a launch version and later updates, and evidence comes from all of them. State one convention in the introduction and under the recommendation table: the target model's name without a qualifier means the current snapshot (for Qwen, "Qwen 3.8 Max" meant the 0902 version). Every figure, trace and user report from another snapshot is labelled where it is used (for example "July preview", "3 August version", "earlier version than 0902"), and evidence whose source does not say which version it tested is labelled "version not stated".

Carry the consequences into the reasoning. A comparison between two figures from different snapshots is indicative, not clean; say so, and point to a same-snapshot figure if one exists.

## 7. Synthesize gaps, business context and recommendations

For each candidate gap, record:

- The benchmark standing (public and SDS) and the feedback tag.
- Reasoning that combines all views: what each shows, where they agree, where they overlap (for example timeouts feeding both efficiency and long-horizon results), and what is not isolated.
- What would close the gap.
- Why it matters, split into **Cowork**, **General capability** and **Verticals**.

Then:

- Pick three to five **priority gaps** in the order the user sets. Write positional references ("gap 2", "ranked third") so they survive reordering, and update every one after any reorder: the connection paragraph, the conclusions list and the next-measurements list.
- List the rest as further observations, such as robustness to run setup, deliverable quality, coding quality, users-only gaps and unmeasured areas. Use the Disputed tag where public and SDS evidence disagree.
- List strengths to keep, and check each against the SDS results and the version labels. Drop a strength that SDS contradicts or that rests only on preview-era reports, or move it to the observations as Disputed.
- Describe how the gaps connect, labelled as interpretation.
- Suggest next measurements: a rerun of the current snapshot on SDS sets with timeouts reported separately, a controlled harness comparison, cost per solved task as a reported metric, a multi-turn repair evaluation, and results on the unmeasured capabilities.
- In the internal version only, optionally check the gaps against current Snorkel specs and client asks.

## 8. Build the internal artifact

Load the artifact design guidance, and the capabilities guidance for highlights and comments. Use the Snorkel template: a midnight hero band with the logo, stone body, Geist with Noto Sans SC, theme tokens with dark mode, and an English/中文 toggle at the top right.

| Tab | Contents |
|---|---|
| Recommendation | Gap table with a feedback column, a benchmarks-versus-users comparison, the feedback survey, landscape gaps against specs |
| Benchmarks | Capability tables with SDS rows, composite indices, tag legend, reading notes, economic-value benchmarks |
| Taxonomy | Board shaded as a heatmap of the model's standing, error-mode mapping, coverage matrix, blending tiers |
| Reference reading | Holistic frameworks, cross-cutting findings, personal versus workplace agents, sources |
| My highlights | Saved highlights and notes |

Declare the `comments` capability (composer only), `db` (a highlights collection) and `user`. Mark internal names with a check-before-sharing note. Before any republish, re-read the live artifact and its comments, because another session may have changed it. Answer comment threads in the thread.

## 9. Build and review the external report

Build it from a script that generates both languages from one source, so reorders and relabels apply everywhere at once. It has two tabs and a shared reference list.

- **Recommendation:** one table only, with columns Gap, Benchmark standing (tag and figures), User feedback (tag and quotes), Reasoning (benchmark and feedback, ending with what would close the gap), and Why it matters (Cowork, General capability, Verticals). Follow it with strengths to keep and how the gaps connect. Under the table, state the version convention and the tag meanings.
- **Technical report:**
  1. Introduction, including the version convention.
  2. Capability taxonomy: the unshaded board and the three design choices.
  3. Approach: public benchmarks, Snorkel private SDS (and whether the target model was run), public user feedback in both languages, the standing classification, and limitations.
  4. Benchmark results: the capability tables, with SDS rows highlighted.
  5. User feedback in depth.
  6. Conclusions: the priority gaps, a table of further observations, and next measurements.
- **References:** paper-style numbered citations such as [1] in the text, numbered in reading order, with the full list at the bottom. Cite SDS as "Snorkel AI, internal evaluation, unpublished".
- **Capability codes:** show each code in the gap column as a chip with its name (for example "C2 · Remember and learn"), and give every code in the page a hover, tap and keyboard-focus definition taken from the taxonomy board. Position the tooltip with `position: fixed` so scrolling tables do not clip it.

Before sending, remove Notion links, client names, spec status, internal draft names, the highlight interface, "my" and "you" phrasing, other customers' models, and catalog, manifest, slug and TBD wording. Search the output for each.

**Review loop:** publish the external report as a private artifact with the `comments` capability (composer only) so the account team can comment on it. For each comment sent to you, make the change in the build script, rebuild both languages, republish to the same URL, and reply in the thread with what changed, including knock-on edits elsewhere in the page. Leave threads for people to resolve. When review is done, send the final standalone `.html` file and, if asked, polish the cover note (section 10).

Tell the user before sending that SDS figures are present (they must confirm these are cleared), that quotes need spot checks, and that Google Fonts may not load in mainland China (the page still renders with system fonts).

## 10. Write the Chinese

Use the chinese-writing skill (`/chinese-writing:chinese-writing` from this library, or `fdr-skills:chinese-writing`). These decisions from the Qwen run are worth reusing:

- Write in a neutral technical-report register with no promotional emphasis. Keep claim strength: "suggests" becomes 提示……可能, not 说明.
- Keep model, benchmark and metric names in English. Define harness once, as 套在模型外层的智能体框架.
- Use 前沿模型 for frontier models in general and 领先模型 for the leader on a given board. For the target model's self-reported figures, name the vendor (for example 阿里公布); for other vendors, use 厂商自报.
- Standing tags: 领先 / 接近领先 / 中游 / 落后 / 有争议 / 未验证 / 无数据. Feedback tags: 反馈较多 / 反馈不一 / 未找到反馈.
- Version labels: 7 月预览版, 8 月 3 日版本, 早于 0902 的版本, 未注明版本.
- The account team may choose a more direct heading than the English (the Qwen run used 亟待提升的四大方面). Point out the tone difference and offer to align the English.
- Use Chinese number grouping without rounding (1802 万, 953.2 万), add 分别 when pairing figures, and put English quotations inside Chinese text in full-width quotes “”.
- After translating, check every number against the English.
- For the cover note to the client, give the evidence as one parallel list (公开评测及各方公布的数据、Snorkel 非公开评测集上的横向对比、中英文公开论坛上的用户反馈), say where the language toggle is, and name the tabs exactly as they appear.

## 11. Verify before handing over

- Render each tab in both languages, light and dark, at desktop width and at 400px with Playwright. Expect no horizontal overflow and no page errors, and look at the screenshots.
- Check for duplicate ids, broken in-page anchors, unbalanced tags, and citation numbers out of reading order.
- Make sure every figure in the recommendation table traces to a citation and carries a version label where needed.
- Report what was built, what is unverified, the inferred SDS name mappings, and the decisions that belong to the user, such as sharing SDS data, timeout accounting and the order of the gaps.
