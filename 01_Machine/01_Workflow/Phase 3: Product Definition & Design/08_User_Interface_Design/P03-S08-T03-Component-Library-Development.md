---
phase: P03
step: S08
task: T03
task_id: P03-S08-T03
title: Component Library Development
previous_task: P03-S08-T02
next_task: P03-S08-T04
version: 3.1.0
agent: "@ui-designer-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @ui-designer-agent. Your mission is to design and document a comprehensive library of reusable UI components, including both basic and complex elements, with detailed specifications and state variations for DafnckMachine v3.1. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/08_User_Interface_Design/`

2. **Collect Data/Input**
   - Gather all component requirements, design system standards, and state variation needs.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Basic_Component_Library.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Component_Specifications.json (JSON)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Complex_Component_Library.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Advanced_Component_Specs.json (JSON)
   - Output JSON schemas must include: { "components": [ ... ], "states": [ ... ] }

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json upon successful documentation delivery.

5. **Self-Check**
   - [ ] All required documentation files are present and complete
   - [ ] Output files match the specified schemas and contain actionable guidance
   - [ ] Task status updated in Step.json and DNA.json 
