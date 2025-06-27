---
phase: P03
step: S07
task: T02
task_id: P03-S07-T02
title: User Journey Mapping & Flow Optimization
previous_task: P03-S07-T01
next_task: P03-S07-T03
version: 3.1.0
agent: "@ux-researcher-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @ux-researcher-agent. Your mission is to design end-to-end user journey maps and optimize all interaction flows and touchpoints for DafnckMachine v3.1, ensuring seamless and engaging user experiences. Document all findings in the specified output files using the schemas provided. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/07_User_Experience_Design/`

2. **Collect Data/Input**
   - Gather user research, behavioral data, and existing journey maps from previous steps.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/User_Journey_Maps.json (JSON, schema: { journeys: object[] })
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Flow_Optimization_Analysis.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Touchpoint_Optimization.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/07_User_Experience_Design/Interaction_Enhancement_Plan.json (JSON, schema: { enhancements: object[] })

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json when all outputs are saved and validated.

5. **Self-Check**
   - [ ] All outputs saved to correct files and match schema
   - [ ] Journey maps and flow optimizations are user-centered and validated
   - [ ] Touchpoint and interaction enhancements are clearly documented
   - [ ] Task status updated in Step.json and DNA.json
