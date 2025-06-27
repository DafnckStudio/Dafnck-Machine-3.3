---
phase: P03
step: S07
task: T03
task_id: P03-S07-T03
title: Information Architecture & Navigation Design
previous_task: P03-S07-T02
next_task: P03-S07-T04
version: 3.1.0
agent: "@ux-researcher-agent, @ui-designer-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @ux-researcher-agent and @ui-designer-agent. Collaborate to design information architecture and navigation systems for DafnckMachine v3.1, ensuring optimal content organization, findability, and user wayfinding. Document all findings in the specified output files using the schemas provided. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/07_User_Experience_Design/`

2. **Collect Data/Input**
   - Gather user research, content inventory, and existing navigation patterns from previous steps.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Information_Architecture.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Content_Hierarchy_Structure.json (JSON, schema: { hierarchy: object[] })
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Navigation_System_Design.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Menu_Structure_Specifications.json (JSON, schema: { menus: object[] })

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json when all outputs are saved and validated.

5. **Self-Check**
   - [ ] All outputs saved to correct files and match schema
   - [ ] Architecture and navigation are user-centered and validated
   - [ ] Content hierarchy and navigation are clearly documented
   - [ ] Task status updated in Step.json and DNA.json
