---
phase: P04
step: S15
task: T03
task_id: P04-S15-T03
title: Integration Testing Implementation
agent:
  - "@functional-tester-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S15-T02
next_task: P04-S15-T04
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @functional-tester-agent and @test-orchestrator-agent. Your mission is to collaboratively implement comprehensive integration testing for DafnckMachine v3.1, including API endpoint validation, database integration, and system component testing. Ensure reliable system integration and data integrity. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/15_Automated_Testing/`

2. **Collect Data/Input**
   - Reference integration testing and validation requirements
   - Review previous API and database integration testing documentation if available
   - Gather standards for endpoint validation, data integrity, and error handling

3. **Save Output**
   - Save API integration testing: `API_Integration_Testing.md`
   - Save endpoint validation specs: `Endpoint_Validation_Specs.json`
   - Save database integration testing: `Database_Integration_Testing.md`
   - Save data validation framework: `Data_Validation_Framework.json`
   - Minimal JSON schema example for endpoint validation:
     ```json
     {
       "endpoint": "/api/user",
       "method": "GET",
       "expectedStatus": 200,
       "validations": ["authRequired", "responseSchema"]
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S15-T04

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Integration tests and validation are comprehensive and pass
   - [ ] Documentation and configs are clear and complete
   - [ ] Task status updated in workflow tracking files 
