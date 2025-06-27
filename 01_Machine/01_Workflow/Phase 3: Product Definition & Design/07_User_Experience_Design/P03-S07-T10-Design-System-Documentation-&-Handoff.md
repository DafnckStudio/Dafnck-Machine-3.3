---
phase: P03
step: S07
task: T10
task_id: P03-S07-T10
title: Design System Documentation & Handoff
previous_task: P03-S07-T09
next_task: P03-S08-T01
version: 3.1.0
agent: "@design-system-agent, @ui-designer-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @design-system-agent and @ui-designer-agent. Collaborate to compile the complete design system documentation and prepare a comprehensive development handoff package for DafnckMachine v3.1. Ensure all design specifications, guidelines, and assets are clear, actionable, and ready for seamless developer implementation. Document all findings in the specified output files using the schemas provided. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/07_User_Experience_Design/`

2. **Collect Data/Input**
   - Gather all finalized design components, usage guidelines, pattern documentation, and implementation specifications.
   - Collect feedback from development teams regarding handoff requirements.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/UX_Design_System.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Complete_Design_Specifications.json (JSON)
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Development_Handoff_Package.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Implementation_Specifications.json (JSON)
   - Output JSON schemas must include: { "components": [ ... ], "guidelines": [ ... ], "assets": [ ... ], "handoff_notes": "string" }

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json upon successful documentation and handoff package delivery.

5. **Self-Check**
   - [ ] All required documentation files and handoff packages are present and complete
   - [ ] Output files match the specified schemas and contain actionable guidance
   - [ ] Feedback from development teams has been incorporated
   - [ ] Task status updated in Step.json and DNA.json
