---
phase: P03
step: S05
task: T04
task_id: P03-S05-T04
title: Automated Development Pipeline Specifications
previous_task: P03-S05-T03
next_task: P03-S05-T05
version: 3.1.0
agent: "@development-orchestrator-agent, @test-orchestrator-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @development-orchestrator-agent, supported by @test-orchestrator-agent. Your job is to define the automated development pipeline for DafnckMachine v3.1, specifying the agent swarm, QA automation, testing frameworks, and deployment mechanisms. Document your findings in the specified output files using the schemas provided. Collaborate as needed to ensure autonomous coding and quality assurance.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/05_PRD_Generator/`

## 2. Collect Data/Input
- Gather requirements for development agent swarm and QA automation
- Research best practices for automated pipelines and testing

## 3. Save Output
- Save development agent specifications to: `01_Machine/04_Documentation/vision/Phase_3/05_PRD_Generator/Development_Agent_Specifications.md`
- Save QA automation framework to: `01_Machine/04_Documentation/vision/Phase_3/05_PRD_Generator/QA_Automation_Framework.md`

### QA_Automation_Framework.md (Markdown)
```
# QA Automation Framework
- Continuous Quality Gates: [string[]]
- Automated Testing: [string[]]
- Security Scanning: [string[]]
- Performance Monitoring: [string[]]
- Accessibility Compliance: [string[]]
- Cross-Platform Testing: [string[]]
```

## 4. Update Progress
- Mark this task as complete in Step.json and DNA.json after outputs are saved and validated.

## 5. Self-Check
- [ ] Are all required output files present and complete?
- [ ] Are development agent and QA automation specifications comprehensive?
- [ ] Are quality gates and testing frameworks clearly documented?
- [ ] Have all supporting agents contributed as needed? 
