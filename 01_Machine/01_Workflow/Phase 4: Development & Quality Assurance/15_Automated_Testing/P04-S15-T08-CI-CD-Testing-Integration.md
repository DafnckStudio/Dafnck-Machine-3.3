---
phase: P04
step: S15
task: T08
task_id: P04-S15-T08
title: CI-CD Testing Integration
agent:
  - "@development-orchestrator-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S15-T07
next_task: P04-S15-T09
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @development-orchestrator-agent and @test-orchestrator-agent. Your mission is to collaboratively integrate comprehensive testing into CI/CD pipelines for DafnckMachine v3.1, including automated execution, parallel testing, result integration, and continuous feedback. Ensure all outputs are saved to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/15_Automated_Testing/`

2. **Collect Data/Input**
   - Reference CI/CD testing and automation requirements
   - Review previous pipeline and continuous testing documentation if available
   - Gather standards for pipeline configuration, result reporting, and feedback systems

3. **Save Output**
   - Save CI/CD testing integration: `CI_CD_Testing_Integration.md`
   - Save pipeline testing configuration: `Pipeline_Testing_Configuration.json`
   - Save continuous testing framework: `Continuous_Testing_Framework.md`
   - Save feedback systems setup: `Feedback_Systems_Setup.json`
   - Minimal JSON schema example for pipeline testing configuration:
     ```json
     {
       "stage": "test",
       "commands": ["npm run test", "npm run lint"],
       "parallel": true,
       "report": "junit.xml"
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S15-T09

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] CI/CD and continuous testing integrations are comprehensive and pass
   - [ ] Documentation and configs are clear and complete
   - [ ] Task status updated in workflow tracking files 
