---
phase: P02
step: S03
task: T06
task_id: P02-S03-T06
title: Strategic Opportunity Identification
previous_task: P02-S03-T05
next_task: P02-S03-T07
version: 3.1.0
agent: "@market-research-agent, @deep-research-agent, @idea-generation-agent, @technology-advisor-agent, @system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @market-research-agent, supported by @deep-research-agent, @idea-generation-agent, @technology-advisor-agent, and @system-architect-agent. Your job is to identify market gaps and develop a strategic positioning framework for DafnckMachine v3.1. Systematically analyze market intelligence, synthesize opportunities, and define value propositions and differentiation strategies. Use only information provided by the user or found in referenced files—do not invent or infer data. Document all findings in the output files below. After saving, update Step.json and DNA.json to mark this task as SUCCEEDED and set the next task to P02-S03-T07. Do not proceed until all required fields are present and saved.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/03_Market_Research/`

## 2. Collect Data/Input
- Market gaps, unmet needs, underserved segments, white spaces, innovation opportunities
- Value proposition, differentiation strategy, positioning statement, competitive advantages

## 3. Save Output
- Save output to:
```
01_Machine/04_Documentation/vision/Phase_2/Market_Gap_Analysis.md
01_Machine/04_Documentation/vision/Phase_2_Discovery_Strategy/Opportunity_Matrix.json
01_Machine/04_Documentation/vision/Phase_2_Discovery_Strategy/Strategic_Positioning_Framework.md
01_Machine/04_Documentation/vision/Phase_2_Discovery_Strategy/Value_Proposition_Canvas.json
```
- Output schema for Opportunity_Matrix.json:
```json
{
  "opportunities": [
    { "gap": "string", "segment": "string", "value": "string", "priority": "string" }
  ]
}
```
- Output schema for Value_Proposition_Canvas.json:
```json
{
  "propositions": [
    { "segment": "string", "need": "string", "solution": "string", "differentiator": "string" }
  ]
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
