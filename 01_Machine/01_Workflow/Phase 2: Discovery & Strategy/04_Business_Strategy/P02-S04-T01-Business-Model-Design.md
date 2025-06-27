---
phase: P02
step: S04
task: T01
task_id: P02-S04-T01
title: Business Model Design
previous_task: P02-S03-T08
next_task: P02-S04-T02
version: 3.1.0
agent: "@market-research-agent, @idea-generation-agent, @technology-advisor-agent, @system-architect-agent, @marketing-strategy-orchestrator"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @market-research-agent, supported by @idea-generation-agent, @technology-advisor-agent, @system-architect-agent, and @marketing-strategy-orchestrator. Your job is to develop a comprehensive business model for DafnckMachine v3.1. Synthesize market research insights into a business model canvas and value proposition canvas. Validate all components against market research. Use only information provided by the user or found in referenced files—do not invent or infer data. Document all findings in the output files below. After saving, update Step.json and DNA.json to mark this task as SUCCEEDED and set the next task to P02-S04-T02. Do not proceed until all required fields are present and saved.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/04_Business_Strategy/`

## 2. Collect Data/Input
- Business model canvas components: value propositions, customer segments, channels, customer relationships, revenue streams, key resources, key activities, key partnerships, cost structure
- Value propositions, product-market fit validation, strategic positioning

## 3. Save Output
- Save output to:
```
01_Machine/04_Documentation/vision/Phase_2/04_Business_Strategy/Business_Model_Canvas.md
01_Machine/04_Documentation/vision/Phase_2/04_Business_Strategy/Value_Proposition_Canvas.json
```
- Output schema for Value_Proposition_Canvas.json:
```json
{
  "propositions": [
    {
      "customer_job": "string",
      "pain_reliever": "string",
      "gain_creator": "string",
      "fit_score": "number"
    }
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
