---
phase: P03
step: S05
task: T05
task_id: P03-S05-T05
title: Project Initialization and Analysis Protocol
previous_task: P03-S05-T04
next_task: P03-S05-T06
version: 3.1.0
agent: "@prd-architect-agent, @system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @prd-architect-agent, supported by @system-architect-agent. Your job is to define the project initialization and analysis protocol for DafnckMachine v3.1, specifying a universal project specification framework and automated analysis capabilities. Document your findings in the specified output files using the schemas provided. Collaborate as needed to ensure comprehensive requirement capture and informed autonomous decisions.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/05_PRD_Generator/`

## 2. Collect Data/Input
- Gather requirements for project specification and analysis
- Research best practices for automated analysis and architecture generation

## 3. Save Output
- Save project initialization protocol to: `01_Machine/04_Documentation/vision/Phase_3/05_PRD_Generator/Project_Initialization_Protocol.md`
- Save automated analysis framework to: `01_Machine/04_Documentation/vision/Phase_3/05_PRD_Generator/Automated_Analysis_Framework.md`

### Automated_Analysis_Framework.md (Markdown)
```
# Automated Analysis Framework
- Market Research: [string[]]
- Technical Feasibility: [string[]]
- Architecture Generation: [string[]]
- Technology Optimization: [string[]]
- Risk Assessment: [string[]]
- Resource Estimation: [string[]]
```

## 4. Update Progress
- Mark this task as complete in Step.json and DNA.json after outputs are saved and validated.

## 5. Self-Check
- [ ] Are all required output files present and complete?
- [ ] Is the project specification framework comprehensive and actionable?
- [ ] Are automated analysis and architecture generation clearly documented?
- [ ] Have all supporting agents contributed as needed? 
