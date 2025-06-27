---
phase: P02
step: S03
task: T03
task_id: P02-S03-T03
title: Customer Segmentation and Persona Development
previous_task: P02-S03-T02
next_task: P02-S03-T04
version: 3.1.0
agent: "@market-research-agent, @deep-research-agent, @idea-generation-agent, @technology-advisor-agent, @system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @market-research-agent, supported by @deep-research-agent, @idea-generation-agent, @technology-advisor-agent, and @system-architect-agent. Your job is to conduct comprehensive customer segmentation and persona development for DafnckMachine v3.1. Systematically analyze market segments and develop detailed personas and journey maps. Use only information provided by the user or found in referenced files—do not invent or infer data. Document all findings in the output files below. After saving, update Step.json and DNA.json to mark this task as SUCCEEDED and set the next task to P02-S03-T04. Do not proceed until all required fields are present and saved.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/03_Market_Research/`

## 2. Collect Data/Input
- Market segments, demographic, psychographic, behavioral, and needs-based data
- Segment sizing, attractiveness, customer personas, journey touchpoints, pain points, decision criteria

## 3. Save Output
- Save output to:
```
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Customer_Segmentation_Analysis.md
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Segment_Attractiveness_Matrix.json
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Customer_Personas.md
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Customer_Journey_Maps.json
```
- Output schema for Segment_Attractiveness_Matrix.json:
```json
{
  "segments": [
    {
      "name": "string",
      "demographics": "string",
      "psychographics": "string",
      "behavioral": "string",
      "needs": "string",
      "size": "string",
      "attractiveness": "string"
    }
  ]
}
```
- Output schema for Customer_Journey_Maps.json:
```json
{
  "personas": [
    {
      "name": "string",
      "touchpoints": ["string"],
      "pain_points": ["string"],
      "decision_criteria": ["string"]
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
