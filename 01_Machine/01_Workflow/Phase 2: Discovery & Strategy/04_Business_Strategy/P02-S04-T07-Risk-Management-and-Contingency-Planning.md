---
phase: P02
step: S04
task: T07
task_id: P02-S04-T07
title: Risk Management and Contingency Planning
previous_task: P02-S04-T06
next_task: P02-S04-T08
version: 3.1.0
agent: "@market-research-agent, @system-architect-agent, @technology-advisor-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @market-research-agent, supported by @system-architect-agent and @technology-advisor-agent. Your job is to develop a risk management framework for DafnckMachine v3.1, including strategic risk assessment, mitigation strategies, and contingency planning. Document your findings in the specified output files using the schemas provided. Collaborate as needed to ensure technical and business feasibility.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/04_Business_Strategy/`

## 2. Collect Data/Input
- Gather data on strategic risks and prioritization
- Research mitigation strategies and contingency options
- Collect scenario planning and crisis management protocols

## 3. Save Output
- Save risk assessment matrix to: `01_Machine/04_Documentation/vision/Phase_2/04_Business_Strategy/Risk_Assessment_Matrix.json`
- Save contingency strategy plan to: `01_Machine/04_Documentation/vision/Phase_2/04_Business_Strategy/Contingency_Strategy_Plan.md`

### Risk_Assessment_Matrix.json (JSON Schema)
```
{
  "type": "object",
  "properties": {
    "risks": {"type": "array", "items": {"type": "string"}},
    "prioritization": {"type": "array", "items": {"type": "string"}},
    "mitigation_strategies": {"type": "array", "items": {"type": "string"}}
  },
  "required": ["risks", "prioritization", "mitigation_strategies"]
}
```

### Contingency_Strategy_Plan.md (Markdown)
```
# Contingency Strategy Plan
- Strategic Scenarios: [string[]]
- Contingency Responses: [string[]]
- Crisis Management Protocols: [string[]]
- Decision Triggers: [string[]]
```

## 4. Update Progress
- Mark this task as complete in Step.json and DNA.json after outputs are saved and validated.

## 5. Self-Check
- [ ] Are all required output files present and complete?
- [ ] Are risk and contingency strategies validated against business and technical objectives?
- [ ] Is the risk management framework feasible and clearly documented?
- [ ] Have all supporting agents contributed as needed? 
