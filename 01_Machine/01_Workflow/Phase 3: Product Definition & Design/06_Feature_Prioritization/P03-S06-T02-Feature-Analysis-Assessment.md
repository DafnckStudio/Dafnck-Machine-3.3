---
phase: P03
step: S06
task: T02
task_id: P03-S06-T02
title: Feature Analysis Assessment
previous_task: P03-S06-T01
next_task: P03-S06-T03
version: 3.1.0
agent: "@market-research-agent, @ux-researcher-agent, @system-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @market-research-agent, @ux-researcher-agent, and @system-architect-agent. Collaborate to conduct a comprehensive feature analysis for DafnckMachine v3.1. Assess business value, user impact, and technical complexity for all features. Provide quantified impact projections and detailed analysis to inform prioritization. Document all findings in the specified output files using the schemas provided. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/06_Feature_Prioritization/`

2. **Collect Data/Input**
   - Gather feature list, business objectives, user needs, and technical constraints from previous steps.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Business_Value_Assessment.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Revenue_Impact_Analysis.json (JSON, schema: { features: string[], revenue_projection: number[], roi: number[] })
   - 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/User_Impact_Evaluation.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Experience_Enhancement_Matrix.json (JSON, schema: { features: string[], impact_scores: number[], adoption_projection: number[] })
   - 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Technical_Complexity_Analysis.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Development_Effort_Matrix.json (JSON, schema: { features: string[], effort_estimation: number[], resource_requirements: string[] })

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json when all outputs are saved and validated.

5. **Self-Check**
   - [ ] All outputs saved to correct files and match schema
   - [ ] Analyses are validated and comprehensive
   - [ ] Feature analysis is feasible and clearly documented
   - [ ] Task status updated in Step.json and DNA.json 
