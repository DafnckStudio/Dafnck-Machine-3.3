---
phase: P04
step: S13
task: T05
task_id: P04-S13-T05
title: Business Logic and Service Layer Implementation
agent:
  - "@coding-agent"
  - "@system-architect-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S13-T04
next_task: P04-S13-T06
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @coding-agent, @system-architect-agent, and @test-orchestrator-agent. Your mission is to collaboratively implement the business logic layer, service architecture, data validation, business rule enforcement, error handling, and logging for DafnckMachine v3.1 backend. Ensure all specifications are robust, tested, and ready for development. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  : `01_Machine/04_Documentation/Doc/Phase_4/13_Backend_Development/`

2. **Collect Data/Input**
   - Reference business logic and service layer requirements
   - Review previous architecture and error handling documentation if available
   - Gather standards for validation, error handling, and logging

3. **Save Output**
   - Save business logic architecture: `Business_Logic_Architecture.md`
   - Save service layer design: `Service_Layer_Design.json`
   - Save error handling guide: `Error_Handling_Guide.md`
   - Save logging configuration: `Logging_Configuration.json`
   - Minimal JSON schema example for service layer design:
     ```json
     {
       "service": "UserService",
       "methods": ["createUser", "getUser", "updateUser", "deleteUser"],
       "validation": true,
       "logging": true
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S13-T06

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Business logic, error handling, and logging are functional and tested
   - [ ] Documentation and configuration are clear and complete
   - [ ] Task status updated in workflow tracking files 
