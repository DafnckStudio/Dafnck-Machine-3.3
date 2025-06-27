---
phase: P02
step: S04
task: T02
task_id: P02-S04-T02
title: Revenue Strategy Development
previous_task: P02-S04-T01
next_task: P02-S04-T03
version: 3.1.0
agent: "@market-research-agent, @technology-advisor-agent, @system-architect-agent, @marketing-strategy-orchestrator"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @market-research-agent, supported by @technology-advisor-agent, @system-architect-agent, and @marketing-strategy-orchestrator. Your job is to design a comprehensive revenue strategy for DafnckMachine v3.1, including monetization frameworks, pricing models, and financial projections. Validate all strategies against market benchmarks. Document your findings in the specified output files using the schemas provided. Collaborate as needed to ensure technical and market feasibility.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/04_Business_Strategy/`

## 2. Collect Data/Input
- Gather market benchmark data for monetization and pricing
- Research competitive pricing models and revenue streams
- Collect cost structure and financial planning assumptions

## 3. Save Output
- Save revenue model to: `01_Machine/04_Documentation/vision/Phase_2/04_Business_Strategy/Revenue_Model.md`
- Save financial projections to: `01_Machine/04_Documentation/vision/Phase_2/04_Business_Strategy/Financial_Projections_Model.json`

### Revenue_Model.md (Markdown)
```
# Revenue Model
- Monetization Streams: [string[]]
- Pricing Models: [string[]]
- Market Benchmarks: [string[]]
- Key Assumptions: [string[]]
```

### Financial_Projections_Model.json (JSON Schema)
```
{
  "type": "object",
  "properties": {
    "monthly_revenue_projection": {"type": "array", "items": {"type": "number"}},
    "break_even_month": {"type": "integer"},
    "scenarios": {"type": "array", "items": {"type": "string"}},
    "sensitivity_analysis": {"type": "string"}
  },
  "required": ["monthly_revenue_projection", "break_even_month", "scenarios", "sensitivity_analysis"]
}
```

## 4. Update Progress
- Mark this task as complete in Step.json and DNA.json after outputs are saved and validated.

## 5. Self-Check
- [ ] Are all required output files present and complete?
- [ ] Are pricing models and projections validated against market data?
- [ ] Is the revenue strategy feasible and clearly documented?
- [ ] Have all supporting agents contributed as needed? 
