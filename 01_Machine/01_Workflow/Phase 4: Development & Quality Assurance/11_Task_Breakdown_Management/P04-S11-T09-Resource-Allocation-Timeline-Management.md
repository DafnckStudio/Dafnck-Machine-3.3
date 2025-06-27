---
phase: P04
step: S11
task: T09
task_id: P04-S11-T09
title: Resource Allocation & Timeline Management
agent: ["@task-planning-agent"]
previous_task: P04-S11-T08
next_task: P04-S11-T10
version: 3.1.0
source: Step.json
---

# Super Prompt
@task-planning-agent: Develop and document strategies for resource allocation and timeline management for DafnckMachine v3.1, leveraging TaskMaster data and project documentation. Document all allocation, planning, and optimization steps with clear rationale and evidence. Output all strategy and planning files to the required locations. Communicate blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4_Development_QA/`

2. **Collect Data/Input**
   - Gather all tasks, team capacity, and skill requirements from tasks.json and supporting documentation.
   - Collect team input and constraints regarding resource allocation and timeline planning.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Resource_Allocation_Strategy.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Capacity_Planning_Framework.json (JSON, schema: {"team_members": [string], "skills": [string], "capacity": object})
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Timeline_Optimization_Plan.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Milestone_Planning_Framework.json (JSON, schema: {"milestones": [string], "tasks": [string], "critical_paths": [string]})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Is the resource allocation and timeline management rationale clearly documented?
   - [ ] Are allocation, planning, and optimization steps justified and reproducible?
   - [ ] Have all blockers and requirements been communicated and addressed? 
