---
phase: P02
step: S03
task: T02
task_id: P02-S03-T02
title: Competitive Intelligence Deep Dive
previous_task: P02-S03-T01
next_task: P02-S03-T03
version: 3.1.0
agent: "@market-research-agent, @deep-research-agent, @idea-generation-agent, @technology-advisor-agent, @system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @market-research-agent, supported by @deep-research-agent, @idea-generation-agent, @technology-advisor-agent, and @system-architect-agent. Your job is to conduct a detailed competitive intelligence deep dive for DafnckMachine v3.1. Systematically analyze competitors, create profiles, and map competitive positioning. Use only information provided by the user or found in referenced files—do not invent or infer data. Document all findings in the output files below. After saving, update Step.json and DNA.json to mark this task as SUCCEEDED and set the next task to P02-S03-T03. Do not proceed until all required fields are present and saved.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/03_Market_Research/`

## 2. Collect Data/Input
- Competitor business models, strategies, financials, market share, strengths, weaknesses
- Positioning maps, feature comparisons, pricing analysis, brand positioning

## 3. Save Output
- Save output to:
```
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Competitive_Intelligence_Matrix.json
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Competitor_Profiles.md
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Competitive_Positioning_Map.json
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Feature_Comparison_Matrix.md
```
- Output schema for Competitive_Intelligence_Matrix.json:
```json
{
  "competitors": [
    {
      "name": "string",
      "business_model": "string",
      "strategy": "string",
      "financial_performance": "string",
      "market_share": "string",
      "strengths": ["string"],
      "weaknesses": ["string"]
    }
  ]
}
```
- Output schema for Competitive_Positioning_Map.json:
```json
{
  "dimensions": ["string"],
  "positions": [
    { "competitor": "string", "x": "number", "y": "number" }
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
