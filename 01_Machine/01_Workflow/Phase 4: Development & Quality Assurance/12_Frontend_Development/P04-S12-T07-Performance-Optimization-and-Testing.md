---
phase: P04
step: S12
task: T07
task_id: P04-S12-T07
title: Performance Optimization and Testing
agent:
  - "@coding-agent"
  - "@performance-load-tester-agent"
  - "@test-orchestrator-agent"
previous_task: P04-S12-T06
next_task: P04-S12-T08
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @coding-agent, @performance-load-tester-agent, and @test-orchestrator-agent. Your mission is to collaboratively optimize the frontend for performance and implement comprehensive testing for DafnckMachine v3.1. Ensure the application is fast, efficient, and robust under load. Document all optimization strategies, test plans, and results. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/12_Frontend_Development/`

2. **Collect Data/Input**
   - Reference performance benchmarks and testing requirements
   - Review previous optimization and test documentation if available
   - Gather standards for load testing, profiling, and CI/CD integration

3. **Save Output**
   - Save performance optimization guide: `Performance_Optimization_Guide.md`
   - Save profiling results: `Profiling_Results.json`
   - Save testing strategy: `Testing_Strategy.md`
   - Save test results: `Test_Results.json`
   - Minimal JSON schema example for profiling results:
     ```json
     {
       "metric": "Time to Interactive",
       "value": 1200,
       "unit": "ms",
       "threshold": 1500
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S12-T08

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Performance and testing meet defined benchmarks and standards
   - [ ] Documentation and results are clear and complete
   - [ ] Task status updated in workflow tracking files

## Output Artifacts Checklist
- _No Output Artifacts section found_

# Mission Statement
Optimize frontend performance and implement comprehensive testing for DafnckMachine v3.1, ensuring fast, reliable, and maintainable user experiences.

# Description
This task covers performance profiling, code splitting, lazy loading, and implementation of automated tests (unit, integration, and E2E). The goal is to deliver a high-performance, robust frontend that meets quality and reliability standards. 
