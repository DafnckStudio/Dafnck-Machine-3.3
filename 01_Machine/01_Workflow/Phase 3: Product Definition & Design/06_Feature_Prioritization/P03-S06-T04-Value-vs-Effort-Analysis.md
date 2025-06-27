---
phase: P03
step: S06
task: T04
task_id: P03-S06-T04
title: Value vs Effort Analysis
previous_task: P03-S06-T03
next_task: P03-S07-T01
version: 3.1.0
agent: "@prd-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @prd-architect-agent. Your job is to conduct a value-effort analysis for DafnckMachine v3.1. Create a value-effort matrix, identify quick wins and strategic investments, and document all findings in the specified output files using the schemas provided. Coordinate with @uber-orchestrator-agent as needed.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/06_Feature_Prioritization/`

2. **Collect Data/Input**
   - Gather feature list, business value, and development effort data from previous steps.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Value_vs_Effort_Matrix.json (JSON, schema: { features: string[], business_value: number[], development_effort: number[], positioning: string[] })
   - 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Quick_Wins_Analysis.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Strategic_Investment_Plan.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Quick_Wins_Roadmap.json (JSON, schema: { features: string[], quick_wins: string[], timeline: string[] })

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json when all outputs are saved and validated.

5. **Self-Check**
   - [ ] All outputs saved to correct files and match schema
   - [ ] Value-effort and quick wins analyses are validated and objective
   - [ ] Strategic investments and quick wins are clearly documented
   - [ ] Task status updated in Step.json and DNA.json 
