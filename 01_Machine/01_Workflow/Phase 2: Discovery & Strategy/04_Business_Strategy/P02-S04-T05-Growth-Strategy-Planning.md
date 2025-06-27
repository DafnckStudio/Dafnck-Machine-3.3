---
phase: P02
step: S04
task: T05
task_id: P02-S04-T05
title: Growth Strategy Planning
previous_task: P02-S04-T04
next_task: P02-S04-T06
version: 3.1.0
agent: "@system-architect-agent, @market-research-agent, @technology-advisor-agent, @marketing-strategy-orchestrator"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @system-architect-agent and @market-research-agent, supported by @technology-advisor-agent and @marketing-strategy-orchestrator. Your job is to develop a growth strategy for DafnckMachine v3.1, including a scalability framework, market expansion plan, and resource scaling models. Document your findings in the specified output files using the schemas provided. Collaborate as needed to ensure technical and market feasibility.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_2/04_Business_Strategy/`

## 2. Collect Data/Input
- Gather data on business, technical, and operational scalability
- Research market expansion opportunities and target markets
- Collect resource scaling and growth trigger information

## 3. Save Output
- Save scalability framework to: `01_Machine/04_Documentation/vision/Phase_2/04_Business_Strategy/Growth_Strategy_Roadmap.md`
- Save market expansion plan to: `01_Machine/04_Documentation/vision/Phase_2/04_Business_Strategy/Market_Expansion_Plan.md`

### Growth_Strategy_Roadmap.md (Markdown)
```
# Growth Strategy Roadmap
- Scalability Framework: [string[]]
- Growth Metrics: [string[]]
- Resource Scaling Models: [string[]]
- Growth Triggers: [string[]]
```

### Market_Expansion_Plan.md (Markdown)
```
# Market Expansion Plan
- Geographic Expansion: [string[]]
- Vertical Strategies: [string[]]
- Horizontal Strategies: [string[]]
- Target Markets: [string[]]
- Market Validation Data: [string[]]
```

## 4. Update Progress
- Mark this task as complete in Step.json and DNA.json after outputs are saved and validated.

## 5. Self-Check
- [ ] Are all required output files present and complete?
- [ ] Are scalability and expansion strategies validated against market and technical data?
- [ ] Is the growth strategy feasible and clearly documented?
- [ ] Have all supporting agents contributed as needed? 
