---
phase: P04
step: S14
task: T02
task_id: P04-S14-T02
title: API Documentation Creation
agent:
  - "@documentation-agent"
  - "@backend-developer-agent"
  - "@system-architect-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S14-T01
next_task: P04-S14-T03
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @documentation-agent, @backend-developer-agent, @system-architect-agent, and @test-orchestrator-agent. Your mission is to collaboratively create and maintain comprehensive API documentation for DafnckMachine v3.1. Ensure all endpoints, parameters, responses, authentication, and usage examples are clearly described and accessible. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/14_Technical_Documentation/`

2. **Collect Data/Input**
   - Reference API specifications and integration requirements
   - Review previous API documentation and examples if available
   - Gather standards for endpoint documentation, authentication, and error handling

3. **Save Output**
   - Save API documentation: `API_Documentation.md`
   - Save API usage examples: `API_Examples.md`
   - Minimal JSON schema example for API documentation:
     ```json
     {
       "endpoint": "/api/login",
       "method": "POST",
       "params": ["username", "password"],
       "response": {"token": "string"},
       "authRequired": false
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S14-T03

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] API documentation and examples are clear and complete
   - [ ] Authentication and error handling are documented
   - [ ] Task status updated in workflow tracking files 
