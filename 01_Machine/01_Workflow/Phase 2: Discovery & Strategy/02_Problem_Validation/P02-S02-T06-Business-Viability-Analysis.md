---
phase: P02
step: S02
task: T06
task_id: P02-S02-T06
title: Business Viability Analysis
previous_task: P02-S02-T05
next_task: P02-S02-T07
version: 3.1.0
agent: "@market-research-agent, @technology-advisor-agent, @system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @market-research-agent, @technology-advisor-agent, and @system-architect-agent. Your jobs are:
- @market-research-agent: Analyze revenue potential, cost structure, pricing strategies, monetization opportunities, and document business viability in Business_Viability_Analysis.json and Revenue_Model.md.
- @technology-advisor-agent: Support risk assessment by identifying technical risks and mitigation strategies.
- @system-architect-agent: Support risk assessment by identifying operational and implementation risks and mitigation strategies.
- Collaborate to conduct a comprehensive risk assessment, develop mitigation strategies, and document findings in Risk_Assessment_Matrix.json and Mitigation_Strategies.md.
- Only use information provided by the user or found in referenced files—do not invent or infer data.
- After saving, update Step.json and DNA.json to mark this task as SUCCEEDED and set the next task to P02-S02-T07.
- Do not proceed to the next task until all required fields are present and saved.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/02_Problem_Validation/`

## 2. Collect Data/Input
- Revenue streams, pricing models, monetization strategies, cost structure, operational expenses, maintenance costs, financial projections, break-even analysis, ROI calculations
- Market, technical, business, and competitive risks, risk probability, impact assessment, risk priority, mitigation strategies, contingency plans, risk monitoring

## 3. Save Output
- Save output to:
```
01_Machine/04_Documentation/vision/Phase_2/02_Problem_Validation/Business_Viability_Analysis.json
01_Machine/04_Documentation/vision/Phase_2/02_Problem_Validation/Revenue_Model.md
01_Machine/04_Documentation/vision/Phase_2/02_Problem_Validation/Risk_Assessment_Matrix.json
01_Machine/04_Documentation/vision/Phase_2/02_Problem_Validation/Mitigation_Strategies.md
```
- Output schemas:
```json
// Business_Viability_Analysis.json
{
  "revenue_streams": ["string"],
  "pricing_models": ["string"],
  "monetization_strategies": ["string"],
  "cost_structure": ["string"],
  "operational_expenses": ["string"],
  "maintenance_costs": ["string"],
  "financial_projections": ["string"],
  "break_even_analysis": "string",
  "roi_calculations": "string"
}
// Risk_Assessment_Matrix.json
{
  "market_risks": ["string"],
  "technical_risks": ["string"],
  "business_risks": ["string"],
  "competitive_risks": ["string"],
  "risk_probability": ["string"],
  "impact_assessment": ["string"],
  "risk_priority": ["string"]
}
// Mitigation_Strategies.md
{
  "mitigation_strategies": ["string"],
  "contingency_plans": ["string"],
  "risk_monitoring": ["string"]
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
