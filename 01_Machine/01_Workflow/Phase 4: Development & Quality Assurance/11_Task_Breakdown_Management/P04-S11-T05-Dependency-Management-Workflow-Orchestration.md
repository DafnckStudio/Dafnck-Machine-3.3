---
phase: P04
step: S11
task: T05
task_id: P04-S11-T05
title: Dependency Management & Workflow Orchestration
agent: ["@task-planning-agent"]
previous_task: P04-S11-T04
next_task: P04-S11-T06
version: 3.1.0
source: Step.json
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
@task-planning-agent: Validate, map, and optimize all task dependencies for DafnckMachine v3.1, ensuring a logical and efficient workflow. Document all analysis, mapping, and optimization steps with clear rationale and evidence. Output all reports, diagrams, and plans to the required locations. Communicate blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4_Development_QA/`

2. **Collect Data/Input**
   - Gather all tasks and dependencies from tasks.json and supporting documentation.
   - Collect team input and constraints regarding dependency management and workflow optimization.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Dependency_Analysis_Report.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Workflow_Mapping_Diagram.json (JSON, schema: {"tasks": [string], "dependencies": [string], "critical_paths": [string]})
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Dependency_Optimization_Plan.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Workflow_Implementation_Guide.json (JSON, schema: {"steps": [string], "guidelines": [string], "optimization": string})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Is the dependency management and workflow rationale clearly documented?
   - [ ] Are analysis, mapping, and optimization steps justified and reproducible?
   - [ ] Have all blockers and requirements been communicated and addressed? 
