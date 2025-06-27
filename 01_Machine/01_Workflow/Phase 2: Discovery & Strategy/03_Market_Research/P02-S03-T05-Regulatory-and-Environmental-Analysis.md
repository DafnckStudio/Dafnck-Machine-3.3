---
phase: P02
step: S03
task: T05
task_id: P02-S03-T05
title: Regulatory and Environmental Analysis
previous_task: P02-S03-T04
next_task: P02-S03-T06
version: 3.1.0
agent: "@market-research-agent, @deep-research-agent, @idea-generation-agent, @technology-advisor-agent, @system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @market-research-agent, supported by @deep-research-agent, @idea-generation-agent, @technology-advisor-agent, and @system-architect-agent. Your job is to assess the regulatory environment and macro-environmental factors for DafnckMachine v3.1. Systematically analyze compliance requirements, regulatory trends, and macro-environmental factors (economic, social, cultural, environmental, political). Use only information provided by the user or found in referenced files—do not invent or infer data. Document all findings in the output files below. After saving, update Step.json and DNA.json to mark this task as SUCCEEDED and set the next task to P02-S03-T06. Do not proceed until all required fields are present and saved.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/03_Market_Research/`

## 2. Collect Data/Input
- Current regulations, pending legislation, compliance requirements, regulatory trends
- Economic, social, cultural, environmental, and political factors

## 3. Save Output
- Save output to:
```
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Regulatory_Environment_Analysis.md
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Compliance_Requirements_Matrix.json
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Macro_Environment_Analysis.md
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/PESTLE_Analysis.json
```
- Output schema for Compliance_Requirements_Matrix.json:
```json
{
  "requirements": [
    { "regulation": "string", "requirement": "string", "impact": "string" }
  ]
}
```
- Output schema for PESTLE_Analysis.json:
```json
{
  "factors": [
    { "type": "string", "description": "string", "impact": "string" }
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
