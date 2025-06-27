---
phase: P03
step: S07
task: T01
task_id: P03-S07-T01
title: User Research Integration & Persona Refinement
previous_task: null
next_task: P03-S07-T02
version: 3.1.0
agent: "@ux-researcher-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @ux-researcher-agent. Your job is to validate and enhance user personas for DafnckMachine v3.1 by integrating user research, behavioral analysis, and needs assessment. Ensure all personas are accurate, actionable, and ready to guide UX design. Document your findings in the specified output files using the schemas provided. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/07_User_Experience_Design/`

2. **Collect Data/Input**
   - Gather current user research data and existing personas from previous steps.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Enhanced_User_Personas.json (JSON, schema: { personas: object[], validation: string })
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Persona_Validation_Report.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/User_Needs_Analysis.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Goal_Mapping_Framework.json (JSON, schema: { goals: string[], success_metrics: string[] })

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json when all outputs are saved and validated.

5. **Self-Check**
   - [ ] All outputs saved to correct files and match schema
   - [ ] Personas and needs validated against current user research
   - [ ] Persona documentation is actionable and clearly structured
   - [ ] Task status updated in Step.json and DNA.json 
