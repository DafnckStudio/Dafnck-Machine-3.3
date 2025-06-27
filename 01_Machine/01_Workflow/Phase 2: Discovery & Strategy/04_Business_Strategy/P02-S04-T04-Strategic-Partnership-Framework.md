---
phase: P02
step: S04
task: T04
task_id: P02-S04-T04
title: Strategic Partnership Framework
previous_task: P02-S04-T03
next_task: P02-S04-T05
version: 3.1.0
agent: "@market-research-agent, @technology-advisor-agent, @system-architect-agent, @marketing-strategy-orchestrator"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @market-research-agent, supported by @technology-advisor-agent, @system-architect-agent, and @marketing-strategy-orchestrator. Your job is to develop a strategic partnership framework for DafnckMachine v3.1, including opportunity identification, collaboration models, value exchange, and governance structures. Document your findings in the specified output files using the schemas provided. Collaborate as needed to ensure technical and market feasibility.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/04_Business_Strategy/`

## 2. Collect Data/Input
- Research potential partners and partnership categories
- Gather data on collaboration models and governance structures
- Collect value exchange and partnership lifecycle information

## 3. Save Output
- Save opportunity map to: `01_Machine/04_Documentation/vision/Phase_2/04_Business_Strategy/Partnership_Opportunity_Map.md`
- Save partnership framework to: `01_Machine/04_Documentation/vision/Phase_2/04_Business_Strategy/Partnership_Framework.md`

### Partnership_Opportunity_Map.md (Markdown)
```
# Partnership Opportunity Map
- Partnership Categories: [string[]]
- Potential Partners: [string[]]
- Strategic Value Scores: [number[]]
- Prioritization Rationale: [string[]]
```

### Partnership_Framework.md (Markdown)
```
# Partnership Framework
- Collaboration Models: [string[]]
- Governance Structures: [string[]]
- Value Exchange Models: [string[]]
- Lifecycle Stages: [string[]]
- Success Metrics: [string[]]
```

## 4. Update Progress
- Mark this task as complete in Step.json and DNA.json after outputs are saved and validated.

## 5. Self-Check
- [ ] Are all required output files present and complete?
- [ ] Are partnership opportunities and frameworks validated against market data?
- [ ] Is the partnership strategy feasible and clearly documented?
- [ ] Have all supporting agents contributed as needed? 
