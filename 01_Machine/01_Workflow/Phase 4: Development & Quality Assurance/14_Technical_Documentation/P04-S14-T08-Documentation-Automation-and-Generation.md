---
phase: P04
step: S14
task: T08
task_id: P04-S14-T08
title: Documentation Automation and Generation
agent:
  - "@documentation-agent"
  - "@devops-agent"
  - "@system-architect-agent"
  - "@development-orchestrator-agent"
previous_task: P04-S14-T07
next_task: P04-S14-T09
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @documentation-agent, @devops-agent, @system-architect-agent, and @development-orchestrator-agent. Your mission is to collaboratively automate the generation and maintenance of technical documentation for DafnckMachine v3.1. Implement robust, automated workflows that keep all documentation current and accurate, integrated with CI/CD. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/14_Technical_Documentation/`

2. **Collect Data/Input**
   - Reference documentation automation and CI/CD requirements
   - Review previous automation scripts and workflows if available
   - Gather standards for documentation tooling and integration

3. **Save Output**
   - Save automation scripts: `Automation_Scripts.md`
   - Save CI/CD documentation workflow: `CI_CD_Documentation_Workflow.md`
   - Minimal JSON schema example for automation script:
     ```json
     {
       "tool": "JSDoc",
       "script": "npm run docs",
       "ciIntegration": true
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S14-T09

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Documentation automation and CI/CD integration are functional
   - [ ] Scripts and workflows are clear and complete
   - [ ] Task status updated in workflow tracking files 
