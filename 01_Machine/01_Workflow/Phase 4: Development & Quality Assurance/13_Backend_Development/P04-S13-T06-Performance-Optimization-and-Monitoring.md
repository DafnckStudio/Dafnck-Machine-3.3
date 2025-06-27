---
phase: P04
step: S13
task: T06
task_id: P04-S13-T06
title: Performance Optimization and Monitoring
agent:
  - "@performance-load-tester-agent"
  - "@health-monitor-agent"
  - "@system-architect-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S13-T05
next_task: P04-S14-T01
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @performance-load-tester-agent, @health-monitor-agent, @system-architect-agent, and @test-orchestrator-agent. Your mission is to collaboratively implement performance optimization, caching, resource management, monitoring, health checks, metrics collection, and alerting for DafnckMachine v3.1 backend. Ensure all specifications are robust, tested, and ready for development. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  : `01_Machine/04_Documentation/Doc/Phase_4/13_Backend_Development/`

2. **Collect Data/Input**
   - Reference performance and monitoring requirements
   - Review previous optimization and monitoring documentation if available
   - Gather standards for caching, metrics, and alerting

3. **Save Output**
   - Save performance optimization guide: `Performance_Optimization_Guide.md`
   - Save caching configuration: `Caching_Configuration.json`
   - Save monitoring implementation guide: `Monitoring_Implementation.md`
   - Save health check configuration: `Health_Check_Configuration.json`
   - Minimal JSON schema example for health check config:
     ```json
     {
       "endpoint": "/health",
       "method": "GET",
       "expectedStatus": 200,
       "checks": ["database", "cache", "uptime"]
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S14-T01

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Performance optimization and monitoring are functional and tested
   - [ ] Documentation and configuration are clear and complete
   - [ ] Task status updated in workflow tracking files 
