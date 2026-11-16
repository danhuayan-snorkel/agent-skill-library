# Subagent briefs

Templates for the parallel research streams in section 2 of the skill. Fill every `{placeholder}` before sending; a subagent starts with no context from the main conversation. Send all briefs in one turn so they run in parallel.

Shared header for every brief:

```text
Target model: {model name}. Snapshots: {snapshot list with dates}. The current snapshot is {current}; figures for any other snapshot must be labelled with that snapshot.
Snapshot date for all figures: {date}.
Capability framework (use these codes): C1 retrieve and ground; C2 remember and learn, including supplied skills; C3 act through tools and MCP; C4 operate interfaces; C5 write and run code; C6 plan and sustain over long horizons; C7 synthesize deliverables; C8 interact (clarify, preferences, proactivity, pushback); C9 self-monitor (calibration, verify before done, know when to stop); C10 honor boundaries. Quality: Q1 success, Q2 reliability, Q3 efficiency, Q4 safety, Q5 calibration. Harness: H1 neutral scaffold, H2 vendor product, H3 ablation.
You research and report only. Do not write deliverables, publish anything, or edit files outside your scratch space. Return the table below and nothing else except a short list of pages you could not open.
```

## Public benchmarks (one brief per capability group)

```text
{shared header}
Your capability group: {for example C4, C5, C6}.
For each benchmark in this group that is still maintained on {date}, find the current leader and {model}'s result.
Source order: (1) the official board or an independent run on its official page (Vals AI, Artificial Analysis, Epoch, the benchmark's own site); (2) aggregators (BenchLM, BenchmarkList, BenchLeader) only if no official page has the figure, labelled "aggregator"; (3) vendor launch tables, labelled "vendor-reported" with the snapshot they were published for. Cite the official page, never a blog that quotes it.
Return one row per benchmark with these columns:
benchmark | capability codes | what it isolates (one line) | access (open, private, mixed) | grading | first released | leader, score, source URL | {model} score, rank of N, harness, attempts, timeout, snapshot, source URL | source type (official, independent, aggregator, vendor) | notes (two snapshots listed, settings missing, sources disagree)
Write "Not checked" if you did not look a board up and "None found" if you looked and found no result. Do not assign standing tags; the main agent does that.
```

Also send one brief for composite indices (Vals Index, Artificial Analysis Intelligence Index and its cost and time per task, GDPval-AA, AA-Briefcase).

## User feedback (English and Chinese, one brief each)

```text
{shared header}
Language: {English | Chinese}. Products to cover: {model API, vendor coding agent, vendor office product, for example Qoder, Qoder CLI, 千问办公}.
Search in extended mode. Combine the model and product names with terms such as {English: slow, expensive, loops, gives up, hallucinate, credits | Chinese: 慢, 贵, 死循环, 摆烂, 越改越错, 积分, 幻觉}.
Cover: {English: Hacker News, Reddit, GitHub issues for the vendor agent, product forums, Trustpilot | Chinese: ifanr, Huxiu, Zhihu, CSDN, Juejin, Woshipm, SMZDM, product forums}.
Return one row per usable page:
date | source and URL | product | model snapshot (from the date and wording; "not stated" if unclear) | harness or product setup | verbatim quote in the original language (with an English gloss for Chinese) | what happened (one line) | capability codes | names the model? (yes, product-level only, other vendor's model)
Exclude feedback about other models in the same family. Keep praise as well as complaints. List pages you could not open (Zhihu, LINUX DO and CSDN often block).
```

## SDS analysis

```text
{shared header}
Inputs from the user: {paths or pasted tables: per-dataset results, manifest exports, trace folders, catalog sheet or Bench Launcher export}.
The target model's traces come from snapshot {snapshot}; confirm this from the files if possible.
For each dataset with a {model} result:
1. Map the series or edition slug to the catalog display name. If the catalog does not give the mapping, match a reference model's score between the edition and a catalog batch, and mark the mapping "inferred".
2. Give the task count, attempts per task, harness and time limit, and whether the set is frontier-difficulty only or mixed.
3. List every model on the same set with pass@1 and pass@k, rank {model} (rank R of N on pass@1) and its distance to the leader in percent.
4. Give the share of {model}'s trials that timed out and that errored, and say whether the pass rate counts those trials as failures or excludes them, or that the files do not say.
5. Flag: duplicate tasks across datasets, task counts that differ between statistics and traces, zeroed or withheld results in a newer manifest, malformed result files, and any private or pre-release third-party models in the run.
Return one table per dataset plus a list of flags. Do not compare across batches or with public benchmark scores.
```
