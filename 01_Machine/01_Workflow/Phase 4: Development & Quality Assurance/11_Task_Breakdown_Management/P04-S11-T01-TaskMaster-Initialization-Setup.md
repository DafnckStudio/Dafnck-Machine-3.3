---
phase: P04
step: S11
task: T01
task_id: P04-S11-T01
title: TaskMaster Initialization Setup
agent: ["@project-initiator-agent", "@task-planning-agent"]
previous_task: null
next_task: P04-S11-T02
version: 3.1.0
source: Step.json
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
@project-initiator-agent (lead), with support from @task-planning-agent: Initialize TaskMaster for DafnckMachine v3.1, ensuring all required files, directories, and configuration are in place for robust task management and workflow orchestration. Document all setup steps, configuration, and environment settings with clear rationale and evidence. Output all guides and configuration files to the required locations. Communicate blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4_Development_QA/`

2. **Collect Data/Input**
   - Gather project requirements, workflow needs, and environment constraints from previous phases and team input.
   - Collect preferences and constraints regarding TaskMaster configuration and AI model selection.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/TaskMaster_Implementation_Guide.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Project_Setup_Configuration.json (JSON, schema: {"files": [string], "directories": [string], "settings": object})
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/TaskMaster_Configuration_Guide.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Environment_Settings.json (JSON, schema: {"main_model": string, "research_model": string, "api_keys": object, "parameters": object})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files and directories present and complete?
   - [ ] Is the TaskMaster setup and configuration rationale clearly documented?
   - [ ] Are configuration and environment settings justified and reproducible?
   - [ ] Have all blockers and requirements been communicated and addressed? 
