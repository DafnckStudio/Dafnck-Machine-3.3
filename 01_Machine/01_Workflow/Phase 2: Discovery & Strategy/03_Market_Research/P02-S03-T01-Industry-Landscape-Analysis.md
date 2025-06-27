---
phase: P02
step: S03
task: T01
task_id: P02-S03-T01
title: Industry Landscape Analysis
previous_task: P02-S01-T07
next_task: P02-S03-T02
version: 3.1.0
agent: "@market-research-agent, @deep-research-agent, @idea-generation-agent, @technology-advisor-agent, @system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @market-research-agent, supported by @deep-research-agent, @idea-generation-agent, @technology-advisor-agent, and @system-architect-agent. Your job is to conduct a comprehensive industry landscape analysis for DafnckMachine v3.1. Systematically analyze industry structure, market dynamics, and competitive landscape. Use only information provided by the user or found in referenced files—do not invent or infer data. Document all findings in the output files below. After saving, update Step.json and DNA.json to mark this task as SUCCEEDED and set the next task to P02-S03-T02. Do not proceed until all required fields are present and saved.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/03_Market_Research/`

## 2. Collect Data/Input
- Industry structure, market segments, value chain, consolidation trends, maturity assessment
- Market dynamics, growth drivers, market forces, disruption factors, regulatory influences

## 3. Save Output
- Save output to:
```
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Industry_Analysis_Report.md
01_Machine/04_Documentation/vision/Phase_2/03_Market_Research/Market_Structure_Map.json
```
- Output schema for Market_Structure_Map.json:
```json
{
  "market_segments": ["string"],
  "value_chain": ["string"],
  "consolidation_trends": ["string"],
  "maturity_assessment": "string"
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
