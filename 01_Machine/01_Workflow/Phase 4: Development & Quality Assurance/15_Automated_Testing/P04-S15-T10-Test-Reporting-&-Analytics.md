---
phase: P04
step: S15
task: T10
task_id: P04-S15-T10
title: Test Reporting & Analytics
agent:
  - "@test-orchestrator-agent"
  - "@development-orchestrator-agent"
previous_task: P04-S15-T09
next_task: P05-S16-T01
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @test-orchestrator-agent and @development-orchestrator-agent. Your mission is to collaboratively implement comprehensive test reporting and analytics for DafnckMachine v3.1, including dashboards, analytics frameworks, quality metrics monitoring, and trend analysis. Ensure all outputs are saved to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - Documentation in  `01_Machine/04_Documentation/Doc/Phase_4/15_Automated_Testing/`

2. **Collect Data/Input**
   - Reference test reporting and analytics requirements
   - Review previous reporting, analytics, and monitoring documentation if available
   - Gather standards for dashboards, metrics, and trend analysis

3. **Save Output**
   - Save test reporting dashboard: `Test_Reporting_Dashboard.md`
   - Save analytics framework: `Analytics_Framework.json`
   - Save quality metrics monitoring: `Quality_Metrics_Monitoring.md`
   - Save monitoring systems setup: `Monitoring_Systems_Setup.json`
   - Minimal JSON schema example for analytics framework:
     ```json
     {
       "dashboard": "Test Results",
       "metrics": ["passRate", "failRate", "avgDuration"],
       "trendAnalysis": true
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next phase: Deployment & Post-Launch

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] Reporting, analytics, and monitoring integrations are comprehensive and pass
   - [ ] Documentation and configs are clear and complete
   - [ ] Task status updated in workflow tracking files 
