---
phase: P04
step: S11
task: T06
task_id: P04-S11-T06
title: Progress Tracking & Monitoring System
agent: ["@task-planning-agent"]
previous_task: P04-S11-T05
next_task: P04-S11-T07
version: 3.1.0
source: Step.json
agent: "@task-planning-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
@task-planning-agent: Establish and verify a robust progress tracking and monitoring system for DafnckMachine v3.1, including analytics and reporting. Document all frameworks, specifications, and analytics guides with clear rationale and evidence. Output all tracking and analytics files to the required locations. Communicate blockers or gaps in requirements immediately.

## MCP Tools Required
- edit_file
- mcp_taskmaster-ai_set_task_status
- mcp_taskmaster-ai_get_task
- mcp_taskmaster-ai_get_tasks

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4_Development_QA/`

2. **Collect Data/Input**
   - Gather all tasks, statuses, and milestones from tasks.json and supporting documentation.
   - Collect team input and constraints regarding progress tracking, analytics, and reporting needs.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Progress_Tracking_Framework.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Monitoring_System_Setup.json (JSON, schema: {"statuses": [string], "milestones": [string], "metrics": [string]})
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Analytics_Implementation_Guide.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Reporting_System_Specs.json (JSON, schema: {"kpis": [string], "report_formats": [string], "data_sources": [string]})
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Analytics_Dashboard_Specifications.md (Markdown)

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Is the progress tracking and analytics rationale clearly documented?
   - [ ] Are tracking, analytics, and reporting guides justified and reproducible?
   - [ ] Have all blockers and requirements been communicated and addressed? 
