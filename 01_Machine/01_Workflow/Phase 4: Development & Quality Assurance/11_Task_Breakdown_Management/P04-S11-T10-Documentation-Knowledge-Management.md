---
phase: P04
step: S11
task: T10
task_id: P04-S11-T10
title: Documentation & Knowledge Management
agent: ["@task-planning-agent"]
previous_task: P04-S11-T09
next_task: P04-S12-T01
version: 3.1.0
source: Step.json
---

# Super Prompt
@task-planning-agent: Generate and consolidate comprehensive documentation and training materials for all tasks and workflows in DafnckMachine v3.1, establishing a robust knowledge management system. Document all task files, workflow guides, and training materials with clear rationale and evidence. Output all documentation and knowledge management files to the required locations. Communicate blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4_Development_QA/`

2. **Collect Data/Input**
   - Gather all tasks, subtasks, and workflow documentation from tasks.json and supporting files.
   - Collect team input and constraints regarding documentation and training needs.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Task_Documentation_Package.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Knowledge_Management_System.json (JSON, schema: {"documents": [string], "training_materials": [string], "links": [string]})
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Documentation_Package.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Workflow_Documentation_Package.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Training_Materials_Collection.json (JSON, schema: {"materials": [string], "type": [string], "audience": [string]})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Is the documentation and knowledge management rationale clearly documented?
   - [ ] Are documentation and training materials justified and reproducible?
   - [ ] Have all blockers and requirements been communicated and addressed? 
