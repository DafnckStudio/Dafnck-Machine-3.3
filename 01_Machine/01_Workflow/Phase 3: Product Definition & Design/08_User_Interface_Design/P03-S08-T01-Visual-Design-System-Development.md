---
phase: P03
step: S08
task: T01
task_id: P03-S08-T01
title: Visual Design System Development
previous_task: P03-S07-T10
next_task: P03-S08-T02
version: 3.1.0
agent: "@ui-designer-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @ui-designer-agent. Your mission is to create a robust, scalable, and consistent visual design system for DafnckMachine v3.1, including all foundational elements, typography, and the initial component library. Document all specifications with precise measurements and implementation details. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/08_User_Interface_Design/`

2. **Collect Data/Input**
   - Gather all visual design foundations, typography standards, and component structure requirements.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/UI_Design_System.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Visual_Foundation_Specifications.json (JSON)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Typography_System.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Font_Specifications.json (JSON)
   - Output JSON schemas must include: { "foundations": [ ... ], "typography": [ ... ], "components": [ ... ] }

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json upon successful documentation delivery.

5. **Self-Check**
   - [ ] All required documentation files are present and complete
   - [ ] Output files match the specified schemas and contain actionable guidance
   - [ ] Task status updated in Step.json and DNA.json
