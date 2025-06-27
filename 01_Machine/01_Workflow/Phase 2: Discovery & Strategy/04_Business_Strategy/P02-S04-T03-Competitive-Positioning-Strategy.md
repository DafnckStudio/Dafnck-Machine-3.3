---
phase: P02
step: S04
task: T03
task_id: P02-S04-T03
title: Competitive Positioning Strategy
previous_task: P02-S04-T02
next_task: P02-S04-T04
version: 3.1.0
agent: "@market-research-agent, @technology-advisor-agent, @system-architect-agent, @marketing-strategy-orchestrator"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @market-research-agent, supported by @technology-advisor-agent, @system-architect-agent, and @marketing-strategy-orchestrator. Your job is to develop a competitive positioning strategy for DafnckMachine v3.1, including a differentiation framework, competitive advantages, and a response plan. Validate all strategies against competitive intelligence and market analysis. Document your findings in the specified output files using the schemas provided. Collaborate as needed to ensure technical and market feasibility.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/04_Business_Strategy/`

## 2. Collect Data/Input
- Gather competitive intelligence and market analysis data
- Research competitor strategies and differentiation factors
- Collect risk and threat assessment information

## 3. Save Output
- Save positioning framework to: `01_Machine/04_Documentation/vision/Phase_2/04_Business_Strategy/Strategic_Positioning_Framework.md`
- Save response plan to: `01_Machine/04_Documentation/vision/Phase_2/04_Business_Strategy/Competitive_Response_Plan.md`

### Strategic_Positioning_Framework.md (Markdown)
```
# Strategic Positioning Framework
- Differentiation Factors: [string[]]
- Competitive Advantages: [string[]]
- Market Validation: [string[]]
- Key Risks: [string[]]
```

### Competitive_Response_Plan.md (Markdown)
```
# Competitive Response Plan
- Threats: [string[]]
- Response Strategies: [string[]]
- Monitoring Framework: [string[]]
- Escalation Procedures: [string[]]
```

## 4. Update Progress
- Mark this task as complete in Step.json and DNA.json after outputs are saved and validated.

## 5. Self-Check
- [ ] Are all required output files present and complete?
- [ ] Are differentiation and response strategies validated against market data?
- [ ] Is the positioning strategy feasible and clearly documented?
- [ ] Have all supporting agents contributed as needed? 
