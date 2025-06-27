---
phase: P02
step: S02
task: T01
task_id: P02-S02-T01
title: Problem Statement Refinement
previous_task: P01-S01-T05
next_task: P02-S02-T02
version: 3.1.0
agent: "@elicitation-agent, @market-research-agent, @idea-generation-agent, @technology-advisor-agent, @system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @elicitation-agent, supported by @market-research-agent, @idea-generation-agent, @technology-advisor-agent, and @system-architect-agent. Your job is to:
- Retrieve and analyze user briefing outputs to extract the initial problem statement and requirements.
- Refine the problem statement by clarifying scope, identifying root causes, and defining measurable success metrics.
- Document the refined problem statement in 01_Machine/04_Documentation/vision/Phase_2/02_Problem_Validation/Problem_Statement.md using the required schema.
- Identify and categorize all stakeholders affected by the problem, quantify impact levels, and prioritize validation targets.
- Document the stakeholder impact matrix in 01_Machine/04_Documentation/vision/Phase_2/02_Problem_Validation/Stakeholder_Impact_Matrix.json using the required schema.
- Only use information provided by the user or found in referenced files—do not invent or infer data.
- After saving, update Step.json and DNA.json to mark this task as SUCCEEDED and set the next task to P02-S02-T02.
- Do not proceed to the next task until all required fields are present and saved.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/02_Problem_Validation/`

## 2. Collect Data/Input
- Initial problem statement, scope, root causes, success metrics
- Stakeholders, impact levels, validation priority

## 3. Save Output
- Save output to:
```
01_Machine/04_Documentation/vision/Phase_2/02_Problem_Validation/Problem_Statement.md
01_Machine/04_Documentation/vision/Phase_2/02_Problem_Validation/Stakeholder_Impact_Matrix.json
```
- Output schemas:
```json
// Problem_Statement.md
{
  "problem_scope": "string",
  "root_causes": ["string"],
  "success_metrics": ["string"]
}
// Stakeholder_Impact_Matrix.json
{
  "primary_stakeholders": ["string"],
  "secondary_stakeholders": ["string"],
  "impact_levels": ["string"],
  "impact_severity": ["string"],
  "validation_priority": ["string"],
  "research_targets": ["string"]
}
```

## 4. Update Progress
- Update:
```
01_Machine/03_Brain/Step.json
01_Machine/03_Brain/DNA.json
```

## 5. Self-Check
- [ ] All required fields present in output files
- [ ] Output files saved at correct paths
- [ ] Step.json and DNA.json updated

