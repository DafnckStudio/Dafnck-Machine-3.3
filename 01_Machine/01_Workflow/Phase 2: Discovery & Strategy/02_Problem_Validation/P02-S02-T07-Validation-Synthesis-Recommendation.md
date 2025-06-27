---
phase: P02
step: S02
task: T07
task_id: P02-S02-T07
title: Validation Synthesis & Recommendation
previous_task: P02-S02-T06
next_task: P02-S03-T01
version: 3.1.0
agent: "@market-research-agent, @technology-advisor-agent, @system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @market-research-agent, @technology-advisor-agent, and @system-architect-agent. Your jobs are:
- @market-research-agent: Consolidate all research findings, analyze validation metrics, identify key insights, and develop evidence-based recommendations with clear go/no-go decision and next steps. Document findings in Validation_Summary.md, Data_Analysis_Report.json, Strategic_Recommendation.md, and Next_Steps_Plan.json.
- @technology-advisor-agent: Support analysis by providing technical validation and feasibility input.
- @system-architect-agent: Support analysis by providing implementation and operational feasibility input.
- Collaborate to ensure recommendations are comprehensive and actionable. Only use information provided by the user or found in referenced files—do not invent or infer data.
- After saving, update Step.json and DNA.json to mark this task as SUCCEEDED and set the next task to P02-S03-T01.
- Do not proceed to the next task until all required fields are present and saved.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/02_Problem_Validation/`

## 2. Collect Data/Input
- Validation data, research findings, metrics analysis, success assessment, key insights, evidence summary, conclusions
- Go/no-go decision, supporting rationale, evidence base, next steps, optimization opportunities, strategic priorities, action items, timelines, success criteria, responsibilities

## 3. Save Output
- Save output to:
```
01_Machine/04_Documentation/vision/Phase_2/02_Problem_Validation/Validation_Summary.md
01_Machine/04_Documentation/vision/Phase_2/02_Problem_Validation/Data_Analysis_Report.json
01_Machine/04_Documentation/vision/Phase_2/02_Problem_Validation/Strategic_Recommendation.md
01_Machine/04_Documentation/vision/Phase_2/02_Problem_Validation/Next_Steps_Plan.json
```
- Output schemas:
```json
// Data_Analysis_Report.json
{
  "metrics_analysis": ["string"],
  "success_assessment": ["string"],
  "key_insights": ["string"],
  "validation_synthesis": "string",
  "evidence_summary": ["string"],
  "conclusions": ["string"]
}
// Next_Steps_Plan.json
{
  "go_no_go_decision": "string",
  "supporting_rationale": "string",
  "evidence_base": ["string"],
  "next_steps": ["string"],
  "optimization_opportunities": ["string"],
  "strategic_priorities": ["string"],
  "action_items": ["string"],
  "timelines": ["string"],
  "success_criteria": ["string"],
  "responsibilities": ["string"]
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
