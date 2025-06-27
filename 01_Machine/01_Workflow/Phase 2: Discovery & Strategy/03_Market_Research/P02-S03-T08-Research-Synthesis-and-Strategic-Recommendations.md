---
phase: P02
step: S03
task: T08
task_id: P02-S03-T08
title: Research Synthesis and Strategic Recommendations
previous_task: P02-S03-T07
next_task: P02-S04-T01
version: 3.1.0
agent: "@market-research-agent, @deep-research-agent, @idea-generation-agent, @technology-advisor-agent, @system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @market-research-agent, supported by @deep-research-agent, @idea-generation-agent, @technology-advisor-agent, and @system-architect-agent. Your job is to consolidate all market research findings and develop strategic recommendations for DafnckMachine v3.1. Synthesize validated insights, develop actionable recommendations, and prepare a market entry plan. Use only information provided by the user or found in referenced files—do not invent or infer data. Document all findings in the output files below. After saving, update Step.json and DNA.json to mark this task as SUCCEEDED and set the next task to P02-S04-T01. Do not proceed until all required fields are present and saved.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/03_Market_Research/`

## 2. Collect Data/Input
- Consolidated research findings, validated insights, strategic implications
- Market entry strategy, positioning, competitive strategy, growth opportunities

## 3. Save Output
- Save output to:
```
01_Machine/04_Documentation/vision/Phase_2_Discovery_Strategy/Market_Research_Summary.md
01_Machine/04_Documentation/vision/Phase_2_Discovery_Strategy/Key_Insights_Report.json
01_Machine/04_Documentation/vision/Phase_2_Discovery_Strategy/Strategic_Recommendations.md
01_Machine/04_Documentation/vision/Phase_2_Discovery_Strategy/Market_Entry_Plan.json
```
- Output schema for Key_Insights_Report.json:
```json
{
  "insights": [
    { "topic": "string", "insight": "string", "implication": "string" }
  ]
}
```
- Output schema for Market_Entry_Plan.json:
```json
{
  "steps": [
    { "action": "string", "owner": "string", "timeline": "string" }
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
