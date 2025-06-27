---
phase: P04
step: S11
task: T08
task_id: P04-S11-T08
title: Quality Assurance Integration
agent: ["@test-orchestrator-agent"]
previous_task: P04-S11-T07
next_task: P04-S11-T09
version: 3.1.0
source: Step.json
---

# Super Prompt
@test-orchestrator-agent: Integrate QA processes and testing workflows with TaskMaster for DafnckMachine v3.1, and establish quality gates and validation frameworks. Document all integration steps, quality gates, and validation procedures with clear rationale and evidence. Output all QA and quality gate files to the required locations. Communicate blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4_Development_QA/`

2. **Collect Data/Input**
   - Gather requirements for QA integration and quality gates from previous steps and team input.
   - Collect preferences and constraints regarding testing workflows and validation processes.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Testing_Workflow_Integration.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/QA_Coordination_Framework.json (JSON, schema: {"qa_processes": [string], "integration_points": [string], "milestones": [string]})
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Quality_Assurance_Integration.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Quality_Gates_Framework.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Validation_Process_Specs.json (JSON, schema: {"gates": [string], "criteria": [string], "taskmaster_mapping": object})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Is the QA integration and quality gates rationale clearly documented?
   - [ ] Are integration steps and validation procedures justified and reproducible?
   - [ ] Have all blockers and requirements been communicated and addressed? 
