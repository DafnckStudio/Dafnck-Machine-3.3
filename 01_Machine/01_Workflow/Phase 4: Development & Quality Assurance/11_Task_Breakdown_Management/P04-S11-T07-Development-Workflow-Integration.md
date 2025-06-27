---
phase: P04
step: S11
task: T07
task_id: P04-S11-T07
title: Development Workflow Integration
agent: ["@development-orchestrator-agent"]
previous_task: P04-S11-T06
next_task: P04-S11-T08
version: 3.1.0
source: Step.json
agent: "@development-orchestrator-agent"
---

# Super Prompt
@development-orchestrator-agent: Integrate TaskMaster with development tools and establish robust team collaboration protocols for DafnckMachine v3.1. Document all integration steps, collaboration frameworks, and guidelines with clear rationale and evidence. Output all integration and collaboration files to the required locations. Communicate blockers or gaps in requirements immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4_Development_QA/`

2. **Collect Data/Input**
   - Gather requirements for tool integration and team collaboration from previous steps and team input.
   - Collect preferences and constraints regarding workflow, communication, and review processes.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Development_Tool_Integration.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Workflow_Optimization_Guide.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Team_Collaboration_Framework.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Coordination_Protocols.json (JSON, schema: {"protocols": [string], "channels": [string], "review_cycles": [string]})
   - 01_Machine/04_Documentation/vision/Phase_4_Development_QA/Team_Collaboration_Guidelines.md (Markdown)

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. **Self-Check**
   - [ ] Are all required output files present and complete?
   - [ ] Is the integration and collaboration rationale clearly documented?
   - [ ] Are integration steps and collaboration protocols justified and reproducible?
   - [ ] Have all blockers and requirements been communicated and addressed? 
