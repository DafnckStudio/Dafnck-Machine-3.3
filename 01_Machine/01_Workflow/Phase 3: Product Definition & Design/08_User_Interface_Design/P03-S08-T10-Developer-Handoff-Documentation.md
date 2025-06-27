---
phase: P03
step: S08
task: T10
task_id: P03-S08-T10
title: Developer Handoff Documentation
previous_task: P03-S08-T09
next_task: P03-S09-T01
version: 3.1.0
agent: "@documentation-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @documentation-agent. Your mission is to prepare a complete developer handoff package and finalize the UI Design System documentation for DafnckMachine v3.1, ensuring all technical specifications, guidelines, and maintenance procedures are clear and comprehensive. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/08_User_Interface_Design/`

2. **Collect Data/Input**
   - Gather all technical specifications, coding guidelines, asset delivery instructions, and maintenance requirements.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Developer_Handoff_Guidelines.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Implementation_Standards_UI.json (JSON)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Complete_UI_Design_System.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Design_System_Maintenance.json (JSON)
   - Output JSON schemas must include: { "handoff": [ ... ], "standards": [ ... ], "system": [ ... ], "maintenance": [ ... ] }

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json upon successful documentation delivery.

5. **Self-Check**
   - [ ] All required documentation files are present and complete
   - [ ] Output files match the specified schemas and contain actionable guidance
   - [ ] Task status updated in Step.json and DNA.json
