---
phase: P02
step: S03
task: T04
task_id: P02-S03-T04
title: Market Trends and Future Analysis
previous_task: P02-S03-T03
next_task: P02-S03-T05
version: 3.1.0
agent: "@market-research-agent, @deep-research-agent, @idea-generation-agent, @technology-advisor-agent, @system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @market-research-agent, supported by @deep-research-agent, @idea-generation-agent, @technology-advisor-agent, and @system-architect-agent. Your job is to analyze technology trends and forecast market evolution for DafnckMachine v3.1. Systematically assess technology trends, innovation timelines, market trends, and future scenarios. Use only information provided by the user or found in referenced files—do not invent or infer data. Document all findings in the output files below. After saving, update Step.json and DNA.json to mark this task as SUCCEEDED and set the next task to P02-S03-T05. Do not proceed until all required fields are present and saved.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/03_Market_Research/`

## 2. Collect Data/Input
- Technology trends, innovation patterns, adoption curves, disruption potential
- Market trends, scenario forecasts, future market structures

## 3. Save Output
- Save output to:
```
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Technology_Trends_Report.md
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Innovation_Timeline.json
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Market_Trends_Report.md
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Future_Scenarios_Analysis.json
```
- Output schema for Innovation_Timeline.json:
```json
{
  "innovations": [
    { "name": "string", "year": "number", "description": "string" }
  ]
}
```
- Output schema for Future_Scenarios_Analysis.json:
```json
{
  "scenarios": [
    { "type": "string", "description": "string", "implications": ["string"] }
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
