---
phase: P03
step: S08
task: T02
task_id: P03-S08-T02
title: Color System Visual Identity
previous_task: P03-S08-T01
next_task: P03-S08-T03
version: 3.1.0
agent: "@ui-designer-agent, @branding-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @ui-designer-agent and @branding-agent. Collaborate to create a robust, accessible, and brand-aligned color system and integrate the visual identity into the UI for DafnckMachine v3.1. Document all specifications with precise guidelines and accessibility standards. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/08_User_Interface_Design/`

2. **Collect Data/Input**
   - Gather all brand guidelines, color palette requirements, and accessibility standards.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Color_Palette_Specifications.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Color_System_Guidelines.json (JSON)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Visual_Identity_Integration.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Brand_Guidelines_Application.json (JSON)
   - Output JSON schemas must include: { "palette": [ ... ], "accessibility": "WCAG AA", "brand": { ... } }

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json upon successful documentation delivery.

5. **Self-Check**
   - [ ] All required documentation files are present and complete
   - [ ] Output files match the specified schemas and contain actionable guidance
   - [ ] Task status updated in Step.json and DNA.json

