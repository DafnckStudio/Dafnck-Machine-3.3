---
phase: P03
step: S05
task: T09
task_id: P03-S05-T09
title: PRD Compilation and Template Compliance
previous_task: P03-S05-T08
next_task: P03-S06-T01
version: 3.1.0
agent: "@prd-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

## Super Prompt
You are @prd-architect-agent. Your job is to compile the comprehensive PRD for DafnckMachine v3.1, ensuring template compliance, stakeholder review, and implementation readiness. Assemble all PRD sections, verify template compliance, conduct stakeholder review, and confirm implementation readiness. Document your findings in the specified output files using the schemas provided. Collaborate as needed to ensure all requirements are met.

## 1. Documentation Reference
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/05_PRD_Generator/`

## 2. Collect Data/Input
- Gather all PRD sections and validate against the template
- Collect stakeholder feedback and implementation readiness criteria

## 3. Save Output
- Save compiled PRD to: `01_Machine/04_Documentation/vision/Phase_3/05_PRD_Generator/Product_Requirements_Document.md`
- Save stakeholder review process to: `01_Machine/04_Documentation/vision/Phase_3/05_PRD_Generator/Stakeholder_Review_Process.md`

### Product_Requirements_Document.md (Markdown)
```
# Product Requirements Document
- All sections completed per template
- Cross-references validated
- Professional formatting
```

### Stakeholder_Review_Process.md (Markdown)
```
# Stakeholder Review Process
- Review Steps: [string[]]
- Feedback Summary: [string[]]
- Implementation Readiness: [string[]]
- Technical Feasibility: [string[]]
- Resource Validation: [string[]]
- Timeline Verification: [string[]]
```

## 4. Update Progress
- Mark this task as complete in Step.json and DNA.json after outputs are saved and validated.

## 5. Self-Check
- [ ] Are all required output files present and complete?
- [ ] Is the PRD fully template-compliant and professionally formatted?
- [ ] Has stakeholder review and implementation readiness been confirmed?
- [ ] Have all supporting agents contributed as needed?
