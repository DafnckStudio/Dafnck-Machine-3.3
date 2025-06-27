---
phase: P03
step: S09
task: T09
task_id: P03-S09-T09
title: DevOps and Deployment Architecture
agent: ["@devops-agent", "@system-architect-agent"]
next_task: P03-S09-T10
version: 3.1.0
source: Step.json
orchestrator: "@uber-orchestrator-agent"
---

# Super Prompt
@devops-agent and @system-architect-agent: Collaborate to design and document the CI/CD pipeline, deployment automation, and environment management strategy for DafnckMachine v3.1. Ensure all DevOps practices are secure, efficient, and reproducible. Output all plans and specifications to the required documentation files. Communicate any blockers or architectural concerns immediately.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_3/09_Technical_Architecture/`

2. **Collect Data/Input**
   - Gather requirements for CI/CD, deployment, and environment management from previous technical architecture steps and team discussions.

3. **Save Output**
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/DevOps_Pipeline_Specifications.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/CICD_Automation_Plan.json (JSON, schema: {"pipeline": string, "tools": [string], "stages": [string], "automation": object})
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/Environment_Management_Strategy.md (Markdown)
   - 01_Machine/04_Documentation/vision/Phase_3/09_Technical_Architecture/Configuration_Management_Plan.json (JSON, schema: {"environments": [string], "config": object, "secrets": object})

4. **Update Progress**
   - Mark this task as done in Step.json and DNA.json when all outputs are complete and reviewed.

5. Self-Check
   - [ ] Are all required output files present and complete?
   - [ ] Does the CI/CD and deployment plan follow best practices for security and automation?
   - [ ] Is the environment management strategy reproducible and documented?
   - [ ] Have all architectural concerns been communicated and resolved?
