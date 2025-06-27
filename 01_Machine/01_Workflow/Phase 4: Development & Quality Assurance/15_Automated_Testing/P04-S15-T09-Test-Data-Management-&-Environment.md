---
phase: P04
step: S15
task: T09
task_id: P04-S15-T09
title: Test Data Management & Environment
agent:
  - "@test-orchestrator-agent"
  - "@functional-tester-agent"
previous_task: P04-S15-T08
next_task: P04-S15-T10
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @test-orchestrator-agent and @functional-tester-agent. Your mission is to collaboratively implement comprehensive test data management and environment isolation for DafnckMachine v3.1, including automated data generation, seeding, cleanup, privacy compliance, and environment provisioning. Ensure all outputs are saved to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/15_Automated_Testing/`

2. **Collect Data/Input**
   - Reference test data management and environment requirements
   - Review previous data management and environment documentation if available
   - Gather standards for data generation, privacy, and environment isolation

3. **Save Output**
   - Save test data management: `Test_Data_Management.md`
   - Save data generation framework: `Data_Generation_Framework.json`
   - Save test environment management: `Test_Environment_Management.md`
   - Save environment isolation setup: `Environment_Isolation_Setup.json`
   - Minimal JSON schema example for data generation:
     ```json
     {
       "entity": "User",
       "fields": ["id", "email", "createdAt"],
       "count": 100,
       "privacy": "anonymized"
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S15-T10

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Test data and environment management integrations are comprehensive and pass
   - [ ] Documentation and configs are clear and complete
   - [ ] Task status updated in workflow tracking files 
