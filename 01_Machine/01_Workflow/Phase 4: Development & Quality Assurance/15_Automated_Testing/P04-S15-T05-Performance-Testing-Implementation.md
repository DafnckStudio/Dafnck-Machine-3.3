---
phase: P04
step: S15
task: T05
task_id: P04-S15-T05
title: Performance Testing Implementation
agent:
  - "@performance-load-tester-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S15-T04
next_task: P04-S15-T06
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @performance-load-tester-agent and @test-orchestrator-agent. Your mission is to collaboratively implement comprehensive performance testing for DafnckMachine v3.1, including load testing, stress testing, scalability validation, bottleneck identification, and performance monitoring. Ensure the application meets all performance and scalability requirements. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/15_Automated_Testing/`

2. **Collect Data/Input**
   - Reference performance testing and monitoring requirements
   - Review previous performance and benchmarking documentation if available
   - Gather standards for load testing, stress testing, and alerting

3. **Save Output**
   - Save performance testing implementation: `Performance_Testing_Implementation.md`
   - Save load testing configuration: `Load_Testing_Configuration.json`
   - Save performance monitoring setup: `Performance_Monitoring_Setup.md`
   - Save benchmarking framework: `Benchmarking_Framework.json`
   - Minimal JSON schema example for load testing config:
     ```json
     {
       "testType": "load",
       "endpoint": "/api/data",
       "concurrentUsers": 100,
       "duration": "5m"
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S15-T06

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Performance tests and monitoring are comprehensive and pass
   - [ ] Documentation and configs are clear and complete
   - [ ] Task status updated in workflow tracking files 
