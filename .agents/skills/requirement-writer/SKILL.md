---
name: requirement-writer
description: >
  Guides users through structured requirements gathering via interactive
  dialogue to generate Problem Framing, SRD, and PRD documents as Markdown
  files. Use when users mention: PRD, SRD, problem framing, requirement doc,
  product spec, feature spec, kickoff brief, or need to define/collect/organize
  product requirements. Also triggers for "new feature idea", "think through
  this project", "define the problem", or partial tasks like writing a
  background section or success metrics.
---

# Requirement Writer

Generate three types of requirement documents through interactive dialogue.
They form a progressive chain — each builds on the previous:

```
Problem Framing → SRD → PRD
(Why do this?)    (What direction?)  (How exactly?)
```

## File loading rules

Before starting, read `references/questioning-guide.md` for questioning
strategy and completeness scoring.

Load templates on demand based on document type:
- Problem Framing → `references/problem-framing-template.md`
- SRD → `references/srd-template.md`
- PRD → `references/prd-template.md`

## Workflow

Track progress with this checklist (copy into conversation):

```
Requirements Progress:
- [ ] Phase 1: Confirm document type + initial project context
- [ ] Phase 2: Layered questioning to collect information
- [ ] Phase 3: Identify project type + confirm optional sections
- [ ] Phase 4: Completeness scoring + user confirmation
- [ ] Phase 5: Generate document
- [ ] Phase 6: Multi-role review + retrospective

To revise: loop back to Phase 2, then regenerate.
```

### Phase 1: Confirm document type

Ask what the user wants to generate. If unsure, recommend based on project stage:
- Idea stage, not yet decided whether to build → Problem Framing
- Direction decided, need cross-team alignment → SRD
- Ready for dev handoff, need execution spec → PRD

A user can start with Problem Framing and expand to SRD/PRD later.

### Phase 2: Layered questioning

Read `references/questioning-guide.md` for the full strategy.

Core approach — three thinking layers, not a field-by-field checklist:

1. **Problem essence** (open-ended): What problem? Who has it? When?
   → Extract WHO, WHAT Problem, WHEN signals from the answer
2. **Solution direction**: How to solve it? Any references? What's in/out of scope?
   → Extract WHAT Job, Solution, Scope signals
3. **Success definition**: How to measure success? What benefits?
   → Extract Benefits, Metrics, A/B signals

After each answer, extract as much as possible and only ask about gaps.
If the user gives comprehensive answers, skip ahead.

### Phase 3: Project type identification

Determine project type from collected information and activate optional sections:

| Signal in user's description | Project type | Activated sections |
|------------------------------|-------------|-------------------|
| Single page/component/feature | Standard | None extra |
| Multiple pages, funnel, conversion path | Cross-page flow | PRD §4.0 User Flow |
| Different user segments, personalization | Segmented | PRD §4.0 User Segments |
| Redesign, overhaul, multi-phase | Holistic optimization | SRD §5.4 Phasing |

Combinations are possible. Confirm with the user before proceeding:
> "This looks like a cross-page flow project with user segmentation.
> I'll include User Flow and User Segments sections in the PRD. Correct?"

### Phase 4: Completeness scoring

Read `references/questioning-guide.md` §Completeness Scoring for criteria.

Apply traffic-light scoring to each required field:
- 🟢 All green → proceed to generate
- 🟡 Has yellow → inform user which fields are thin, ask if they want to supplement
- 🔴 Has red → must ask follow-up questions for red fields before generating

### Phase 5: Generate document

**Critical: Before generating, re-read the relevant template file** to ensure
structural accuracy (long conversations may push earlier context out of window):
- Problem Framing → re-read `references/problem-framing-template.md`
- SRD → re-read `references/srd-template.md`
- PRD → re-read `references/prd-template.md`

Generate as Markdown file. In Claude.ai, save to `/mnt/user-data/outputs/`.
In IDE environments (Claude Code, Cursor, Kiro), save to `docs/` in the project root.

Document language: match the user's conversation language.
For sections with insufficient information, mark as `> ⚠️ TBD — 待补充`.
Do not fabricate content.

### Phase 6: Multi-role review + retrospective

After generating, perform two checks:

**Multi-role review** — scan the document from three perspectives:
- 🎯 Product: Is the problem clear? Are metrics measurable? Is scope defined?
- 🎨 Design: Are scenarios specific enough for design work? Missing states (empty, error, loading)?
- 🔧 Engineering: Are backend/API needs clear? Data sources defined? Non-functional requirements covered?

Present findings as a brief checklist. Ask if user wants to supplement.

**Retrospective** — briefly note:
- Which sections are thinnest and why
- What questions could have been asked earlier to get better information

In IDE environments (Claude Code, Cursor, Kiro), append retrospective to `docs/review-log.md`.
In Claude.ai, output in conversation for the user to reference.
