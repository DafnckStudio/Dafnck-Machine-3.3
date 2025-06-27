---
phase: P04
step: S15
task: T07
task_id: P04-S15-T07
title: Quality Assurance & Test Coverage
agent:
  - "@test-orchestrator-agent"
  - "@functional-tester-agent"
previous_task: P04-S15-T06
next_task: P04-S15-T08
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @test-orchestrator-agent and @functional-tester-agent. Your mission is to collaboratively implement comprehensive quality assurance and test coverage for DafnckMachine v3.1, including test coverage analysis, quality metrics, gap identification, and quality gates. Ensure all outputs are saved to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/15_Automated_Testing/`

2. **Collect Data/Input**
   - Reference quality assurance and test coverage requirements
   - Review previous coverage analysis and quality metrics documentation if available
   - Gather standards for coverage reporting, quality gates, and validation criteria

3. **Save Output**
   - Save test coverage analysis: `Test_Coverage_Analysis.md`
   - Save quality metrics framework: `Quality_Metrics_Framework.json`
   - Save quality gates implementation: `Quality_Gates_Implementation.md`
   - Save validation criteria: `Validation_Criteria.json`
   - Minimal JSON schema example for quality metrics:
     ```json
     {
       "metric": "codeCoverage",
       "value": 92.5,
       "threshold": 90,
       "status": "pass"
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P04-S15-T08

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Coverage analysis and quality gates are comprehensive and pass
   - [ ] Documentation and configs are clear and complete
   - [ ] Task status updated in workflow tracking files 
