---
phase: P03
step: S06
task: T01
task_id: P03-S06-T01
title: Prioritization Framework Development
previous_task: P03-S05-T01
next_task: P03-S06-T02
version: 3.1.0
source: Step.json
agent: "@prd-architect-agent"
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
You are @prd-architect-agent. Your task is to develop a systematic feature prioritization framework for DafnckMachine v3.1. Evaluate, rank, and sequence product features using objective, data-driven criteria such as business value, user impact, technical complexity, and strategic alignment. Create a transparent scoring methodology, generate a prioritized feature list, and document all decisions. Coordinate with @uber-orchestrator-agent as needed. Output all frameworks and matrices to the specified files.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/06_Feature_Prioritization/`

2. **Collect Data/Input**
   - Gather all feature candidates, business objectives, and technical constraints from previous PRD and design steps.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Feature_Prioritization_Framework.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Evaluation_Criteria_Matrix.json (JSON, schema: { criteria: string[], weights: number[], description: string })
   - 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Scoring_Methodology.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Prioritization_Algorithm.json (JSON, schema: { algorithm: string, parameters: object })

4. **Update Progress**
   - Mark this task as complete in Step.json and DNA.json when all outputs are saved and validated.

5. **Self-Check**
   - [ ] All outputs saved to correct files and match schema
   - [ ] Scoring methodology is objective and transparent
   - [ ] Feature ranking aligns with business and user goals
   - [ ] Task status updated in Step.json and DNA.json

## Output Artifacts Checklist
- [ ] 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Feature_Prioritization_Framework.md — Feature_Prioritization_Framework.md: Feature_Prioritization_Framework.md (missing)
- [ ] 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Evaluation_Criteria_Matrix.json — Evaluation_Criteria_Matrix.json: Evaluation_Criteria_Matrix.json (missing)
- [ ] 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Scoring_Methodology.md — Scoring_Methodology.md: Scoring_Methodology.md (missing)
- [ ] 01_Machine/04_Documentation/vision/Phase_3/06_Feature_Prioritization/Prioritization_Algorithm.json — Prioritization_Algorithm.json: Prioritization_Algorithm.json (missing)
