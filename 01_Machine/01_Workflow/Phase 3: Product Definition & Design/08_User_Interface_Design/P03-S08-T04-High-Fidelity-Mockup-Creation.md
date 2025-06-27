---
phase: P03
step: S08
task: T04
task_id: P03-S08-T04
title: High-Fidelity Mockup Creation
previous_task: P03-S08-T03
next_task: P03-S08-T05
version: 3.1.0
agent: "@ui-designer-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @ui-designer-agent. Your mission is to create pixel-perfect, high-fidelity mockups for all key screens and user flows for DafnckMachine v3.1, ensuring responsive design and clear depiction of all interface states. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/08_User_Interface_Design/`

2. **Collect Data/Input**
   - Gather all wireframes, user flows, and state requirements for key screens.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Visual_Design_Mockups.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Screen_Layout_Specifications.json (JSON)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/User_Flow_Mockups.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/08_User_Interface_Design/Interaction_State_Specifications.json (JSON)
   - Output JSON schemas must include: { "screens": [ ... ], "flows": [ ... ], "states": [ ... ] }

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json upon successful documentation delivery.

5. **Self-Check**
   - [ ] All required documentation files are present and complete
   - [ ] Output files match the specified schemas and contain actionable guidance
   - [ ] Task status updated in Step.json and DNA.json 
