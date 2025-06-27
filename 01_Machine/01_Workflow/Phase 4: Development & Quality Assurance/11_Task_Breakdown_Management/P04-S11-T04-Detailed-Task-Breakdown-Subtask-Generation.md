---
phase: P04
step: S11
task: T04
task_id: P04-S11-T04
title: Detailed Task Breakdown & Subtask Generation
agent: ["@task-planning-agent"]
previous_task: P04-S11-T03
next_task: P04-S11-T05
version: 3.1.0
source: Step.json
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
@task-planning-agent: Expand high-priority and all remaining tasks into detailed subtasks for DafnckMachine v3.1, referencing relevant technical and design documentation. Document all breakdowns, specifications, and subtask structures with clear rationale and evidence. Output all breakdowns and subtask files to the required locations. Communicate blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4_Development_QA/`

2. **Collect Data/Input**
   - Gather high-priority and remaining tasks from tasks.json and supporting documentation.
   - Collect team input and constraints regarding subtask generation and breakdown priorities.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/High_Priority_Task_Breakdown.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Subtask_Specifications.json (JSON, schema: {"subtasks": [string], "parent_task": string, "details": object})
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Task_Expansion_Strategy.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Complete_Task_Breakdown.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Full_Subtask_Structure.json (JSON, schema: {"tasks": [string], "subtasks": object, "dependencies": [string]})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Is the subtask breakdown and generation rationale clearly documented?
   - [ ] Are breakdowns and subtask structures justified and reproducible?
   - [ ] Have all blockers and requirements been communicated and addressed? 
