---
phase: P03
step: S07
task: T05
task_id: P03-S07-T05
title: Visual Design System Development
previous_task: P03-S07-T04
next_task: P03-S07-T06
version: 3.1.0
agent: "@branding-agent, @design-system-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @branding-agent and @design-system-agent. Collaborate to develop a visual design system for DafnckMachine v3.1, integrating brand identity, design tokens, and consistent styling for a cohesive visual experience. Document all findings in the specified output files using the schemas provided. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/07_User_Experience_Design/`

2. **Collect Data/Input**
   - Gather brand guidelines, visual identity assets, and design system requirements from previous steps.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Brand_Integration_Guidelines.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Visual_Identity_System.json (JSON, schema: { identity: object })
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Design_Token_System.json (JSON, schema: { tokens: object })
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Token_Usage_Guidelines.md (Markdown)

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json when all outputs are saved and validated.

5. **Self-Check**
   - [ ] All outputs saved to correct files and match schema
   - [ ] Brand integration and design tokens are user-centered and validated
   - [ ] Visual identity and token usage are clearly documented
   - [ ] Task status updated in Step.json and DNA.json
