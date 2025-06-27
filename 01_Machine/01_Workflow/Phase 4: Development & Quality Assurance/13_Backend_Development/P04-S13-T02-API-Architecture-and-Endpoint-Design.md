---
phase: P04
step: S13
task: T02
task_id: P04-S13-T02
title: API Architecture and Endpoint Design
agent:
  - "@system-architect-agent"
  - "@coding-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S13-T01
next_task: P04-S13-T03
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @system-architect-agent, @coding-agent, and @test-orchestrator-agent. Your mission is to collaboratively design a scalable API architecture for DafnckMachine v3.1, including RESTful endpoints, GraphQL schema, and complete documentation for developer integration. Ensure all specifications are clear, versioned, and ready for implementation. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  : `01_Machine/04_Documentation/Doc/Phase_4/13_Backend_Development/`

2. **Collect Data/Input**
   - Reference API requirements and integration needs
   - Review previous API architecture and documentation if available
   - Gather standards for REST, GraphQL, and OpenAPI

3. **Save Output**
   - Save API architecture design: `API_Architecture_Design.md`
   - Save endpoint structure specs: `Endpoint_Structure_Specs.json`
   - Save API documentation: `API_Documentation_Complete.md`
   - Save OpenAPI specifications: `OpenAPI_Specifications.json`
   - Minimal JSON schema example for endpoint specs:
     ```json
     {
       "endpoint": "/api/user",
       "method": "GET",
       "description": "Fetch user data",
       "authRequired": true
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S13-T03

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] API architecture and documentation meet standards and are complete
   - [ ] OpenAPI specs and endpoint details are validated
   - [ ] Task status updated in workflow tracking files 
