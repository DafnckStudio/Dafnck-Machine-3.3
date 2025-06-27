---
phase: P03
step: S05
task: T03
task_id: P03-S05-T03
title: Universal Technology Stack Support Matrix
previous_task: P03-S05-T02
next_task: P03-S05-T04
version: 3.1.0
agent: "@technology-advisor-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @technology-advisor-agent. Your job is to define the universal technology stack support matrix for DafnckMachine v3.1, ensuring support for all major development platforms, frameworks, and languages. Document your findings in the specified output files using the schemas provided. Collaborate as needed to ensure cross-platform consistency.

### 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/05_PRD_Generator/`

## 2. Collect Data/Input
- Gather requirements for technology stack support and platform integration
- Research best practices for universal technology support

## 3. Save Output
- Save technology stack matrix to: `01_Machine/04_Documentation/vision/Phase_3/05_PRD_Generator/Technology_Stack_Matrix.md`
- Save design system integration to: `01_Machine/04_Documentation/vision/Phase_3/05_PRD_Generator/Design_System_Integration.md`

### Technology_Stack_Matrix.md (Markdown)
```
# Technology Stack Matrix
- Web: [string[]]
- Mobile: [string[]]
- Desktop: [string[]]
- System: [string[]]
- Game: [string[]]
- Data Science: [string[]]
- Blockchain: [string[]]
- Enterprise: [string[]]
```

## 4. Update Progress
- Mark this task as complete in Step.json and DNA.json after outputs are saved and validated.

## 5. Self-Check
- [ ] Are all required output files present and complete?
- [ ] Is the technology stack matrix comprehensive and up to date?
- [ ] Is cross-platform consistency addressed?
- [ ] Is the design system integration clearly documented? 
