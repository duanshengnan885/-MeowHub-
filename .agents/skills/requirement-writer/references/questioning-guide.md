# Questioning Guide

## Contents

- Questioning philosophy
- Layer 1: Problem essence
- Layer 2: Solution direction
- Layer 3: Success definition
- Adaptive behavior
- Completeness scoring
  - Problem Framing scoring
  - SRD additional scoring
  - PRD additional scoring

---

## Questioning philosophy

Extract information from natural conversation rather than interrogating
field by field. The user describes their project; you identify what's
covered and what's missing, then ask only about the gaps.

One open question often fills multiple fields. For example, "Tell me
about the project background" might reveal WHO, WHAT Problem, and WHEN
in a single answer.

---

## Layer 1: Problem essence

Goal: understand the core problem and who it affects.

Start with an open question like:
> "这个项目/功能大概要解决什么问题？可以先简单说说背景。"

From the answer, extract signals for:
- **WHO**: target users, segments, personas
- **WHAT Problem**: pain points, current issues, status quo
- **WHEN**: scenario, trigger, touchpoint where the problem occurs
- **Current workaround**: how users cope today (enriches Problem description)

Follow-up only on what's unclear. Examples:
- WHO unclear: "你提到的用户，主要是新用户还是老用户？有没有更具体的群体？"
- Problem vague: "你说的'体验不好'，能举个具体的例子吗？用户卡在哪个环节？"
- WHEN missing: "这个问题是在什么时候/什么操作下出现的？"

---

## Layer 2: Solution direction

Goal: understand what the user wants to build and the boundaries.

Transition naturally:
> "了解了问题，那你们目前打算怎么解决？有没有初步的方案想法？"

From the answer, extract signals for:
- **WHAT Job**: the core task users need to accomplish (JTBD)
- **Solution outline**: high-level approach
- **Scope**: what's in, what's out for this version
- **Benchmark**: any competitive or industry references
- **Before/After**: expected change after launch
- **Project type signals**: single page? cross-page flow? multiple user segments? phased rollout?

Follow-up examples:
- Job unclear: "用户最终想达成什么目的？完成什么任务？"
- Scope undefined: "这个版本主要覆盖哪些功能？有没有明确不做的？"
- No benchmark: "有没有参考过其他产品怎么处理类似的问题？"

---

## Layer 3: Success definition

Goal: understand how to measure success and validate the solution.

Transition:
> "最后聊聊怎么衡量成功——你觉得这个做完之后，看什么指标就知道做对了？"

From the answer, extract signals for:
- **Customer benefit**: value to users
- **Business benefit**: value to company, ideally quantifiable
- **Brand impact**: brand perception change (optional)
- **Success metrics**: primary + observation metrics
- **A/B testing**: hypothesis, groups, trigger conditions
- **Stakeholders**: who needs to be aligned

Follow-up examples:
- Benefits vague: "对用户来说，最直接的改善是什么？对公司来说呢？"
- No metrics: "如果要用数据证明这个功能成功了，你会看哪个指标？"
- A/B unclear: "需要做 A/B 测试吗？对照组和实验组怎么分？"

---

## Adaptive behavior

Adjust based on how much information the user provides:

**User gives detailed context in one message:**
Skip most questions. Summarize what you extracted, highlight any gaps,
and ask about gaps only.

**User gives minimal context:**
Go through all three layers. But keep each round to 1-2 questions max.

**User is unsure about something:**
Offer concrete options to help them decide. Example:
> "成功指标通常可以看转化率、客单价、或者用户留存。对你们这个项目来说，哪个最相关？"

**User wants to skip a section:**
Allow it. Mark as TBD in the document. Don't block progress.

---

## Completeness scoring

Before generating a document, score each required field.

### Problem Framing scoring

| Field | 🟢 Sufficient | 🟡 Thin | 🔴 Missing |
|-------|-------------|--------|-----------|
| WHO | Can answer "who" AND "why this group specifically" | Can answer "who" but not "why this group" | Cannot identify target users |
| WHAT Problem | Specific pain points with concrete examples or data | Has a problem direction but too abstract | No problem articulated |
| WHEN | Clear scenario/touchpoint/trigger | Vague context | No scenario described |
| WHAT Job | Clear task the user is trying to accomplish | Task implied but not explicit | No task defined |
| Customer Benefit | Specific, tangible user value | Directional but generic ("better experience") | Not mentioned |
| Company Benefit | Quantifiable or clearly measurable business value | Has direction but no metric ("increase revenue") | Not mentioned |

Rules:
- All 🟢 → generate
- Any 🟡 → inform user, ask if they want to supplement or proceed as-is
- Any 🔴 → ask follow-up for red fields, do not generate until resolved

### SRD additional scoring

All Problem Framing fields plus:

| Field | 🟢 Sufficient | 🟡 Thin | 🔴 Missing |
|-------|-------------|--------|-----------|
| Solution / Scope | Clear approach with defined boundaries | Has approach but no scope boundaries | No solution direction |
| Success Metrics | Primary metric + at least 1 observation metric | Only directional ("improve conversion") | No metrics |
| Risks | At least 1 identified risk with mitigation | Risks acknowledged but no mitigation | Not considered |

Optional fields (Brand Impact, Benchmark, A/B Testing, Stakeholders, Phasing)
do not block generation — mark as TBD if missing.

### PRD additional scoring

All SRD fields plus:

| Field | 🟢 Sufficient | 🟡 Thin | 🔴 Missing |
|-------|-------------|--------|-----------|
| Frontend requirements | Platform-specific behavior described | General description only | No frontend spec |
| Data/business logic | Rules, sources, and edge cases defined | Some rules but gaps in edge cases | No logic described |
| Backend/API needs (PM layer) | Interfaces and data sources identified | Vague description | Not mentioned |

Optional fields (CMS, i18n, content specs, non-functional requirements,
launch strategy) do not block generation — mark as TBD if missing.
