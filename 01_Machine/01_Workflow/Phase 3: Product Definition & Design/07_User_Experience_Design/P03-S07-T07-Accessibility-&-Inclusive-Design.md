---
phase: P03
step: S07
task: T07
task_id: P03-S07-T07
title: Accessibility & Inclusive Design
previous_task: P03-S07-T06
next_task: P03-S07-T08
version: 3.1.0
agent: "@ux-researcher-agent, @ui-designer-agent, @design-system-agent, @design-qa-analyst, @branding-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @ux-researcher-agent. Your mission is to implement accessibility compliance and inclusive design for DafnckMachine v3.1, ensuring universal access, WCAG compliance, and support for all users. Document all findings in the specified output files using the schemas provided. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/07_User_Experience_Design/`

2. **Collect Data/Input**
   - Gather accessibility standards, inclusive design principles, and user needs from previous steps and research.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Accessibility_Compliance_Framework.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/WCAG_Checklist.json (JSON, schema: { checklist: object[] })
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Inclusive_Design_Guidelines.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Universal_Access_Specifications.json (JSON, schema: { specifications: object[] })

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json when all outputs are saved and validated.

5. **Self-Check**
   - [ ] All outputs saved to correct files and match schema
   - [ ] Accessibility and inclusive design are user-centered and validated
   - [ ] Compliance and universal access are clearly documented
   - [ ] Task status updated in Step.json and DNA.json
