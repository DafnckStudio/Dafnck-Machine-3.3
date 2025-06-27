---
phase: P03
step: S07
task: T08
task_id: P03-S07-T08
title: Prototype Development & Validation
previous_task: P03-S07-T07
next_task: P03-S07-T09
version: 3.1.0
agent: "@ui-designer-agent, @design-qa-analyst, @branding-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @ui-designer-agent and @design-qa-analyst. Collaborate to create interactive prototypes and validate design solutions for DafnckMachine v3.1, ensuring user-centered, accessible, and optimal user experiences. Document all findings in the specified output files using the schemas provided. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/07_User_Experience_Design/`

2. **Collect Data/Input**
   - Gather user flows, interface requirements, and validation criteria from previous steps.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Prototype_Documentation.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Interactive_Flow_Specifications.json (JSON, schema: { flows: object[] })
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Design_Validation_Report.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Usability_Testing_Results.json (JSON, schema: { results: object[] })

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json when all outputs are saved and validated.

5. **Self-Check**
   - [ ] All outputs saved to correct files and match schema
   - [ ] Prototypes and validation are user-centered and validated
   - [ ] Documentation and results are clearly structured
   - [ ] Task status updated in Step.json and DNA.json
