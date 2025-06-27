---
phase: P03
step: S09
task: T10
task_id: P03-S09-T10
title: Architecture Documentation and Validation
agent: ["@system-architect-agent", "@devops-agent"]
next_task: P03-S10-T01
version: 3.1.0
source: Step.json
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
@system-architect-agent and @devops-agent: Compile all technical architecture documentation and validate the overall system for DafnckMachine v3.1. Ensure all documents are complete, organized, and the architecture is validated for feasibility, scalability, security, and implementation readiness. Output all findings and guidelines to the required files. Communicate any critical issues or blockers immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/09_Technical_Architecture/`

2. **Collect Data/Input**
   - Gather all technical documentation, specifications, and review feedback from previous steps and team discussions.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/Complete_Technical_Architecture.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/Implementation_Guidelines.json (JSON, schema: {"guidelines": [string], "references": [string]})
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/Architecture_Validation_Report.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/Technical_Review_Results.json (JSON, schema: {"findings": [string], "actions": [string]})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Is the architecture validated for feasibility, scalability, security, and readiness?
   - [ ] Are all technical guidelines and review results documented?
   - [ ] Have all critical issues been communicated and addressed? 
