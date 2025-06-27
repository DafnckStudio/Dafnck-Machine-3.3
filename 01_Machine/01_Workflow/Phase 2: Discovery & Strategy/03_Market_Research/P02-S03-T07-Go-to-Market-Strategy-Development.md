---
phase: P02
step: S03
task: T07
task_id: P02-S03-T07
title: Go-to-Market Strategy Development
previous_task: P02-S03-T06
next_task: P02-S03-T08
version: 3.1.0
agent: "@market-research-agent, @deep-research-agent, @idea-generation-agent, @technology-advisor-agent, @system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @market-research-agent, supported by @deep-research-agent, @idea-generation-agent, @technology-advisor-agent, and @system-architect-agent. Your job is to develop a comprehensive go-to-market strategy for DafnckMachine v3.1. Systematically analyze distribution channels, sales models, partnership opportunities, pricing strategies, and monetization frameworks. Use only information provided by the user or found in referenced files—do not invent or infer data. Document all findings in the output files below. After saving, update Step.json and DNA.json to mark this task as SUCCEEDED and set the next task to P02-S03-T08. Do not proceed until all required fields are present and saved.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/03_Market_Research/`

## 2. Collect Data/Input
- Distribution channels, sales models, partnership opportunities, channel effectiveness
- Pricing strategies, monetization options, revenue projections

## 3. Save Output
- Save output to:
```
01_Machine/04_Documentation/vision/Phase_2_Discovery_Strategy/Channel_Strategy_Analysis.md
01_Machine/04_Documentation/vision/Phase_2_Discovery_Strategy/Distribution_Channel_Matrix.json
01_Machine/04_Documentation/vision/Phase_2_Discovery_Strategy/Pricing_Strategy_Analysis.json
01_Machine/04_Documentation/vision/Phase_2_Discovery_Strategy/Monetization_Framework.md
```
- Output schema for Distribution_Channel_Matrix.json:
```json
{
  "channels": [
    { "name": "string", "type": "string", "effectiveness": "string", "partners": ["string"] }
  ]
}
```
- Output schema for Pricing_Strategy_Analysis.json:
```json
{
  "strategies": [
    { "model": "string", "description": "string", "revenue_projection": "string" }
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
