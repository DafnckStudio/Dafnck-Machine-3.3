---
phase: P05
step: S17
task: T04
task_id: P05-S17-T04
title: Business Intelligence and KPI Tracking
agent:
  - "@analytics-setup-agent"
  - "@business-intelligence-agent"
  - "@health-monitor-agent"
  - "@data-analyst-agent"
  - "@devops-agent"
previous_task: P05-S17-T03
next_task: P05-S17-T05
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @analytics-setup-agent, collaborating with @business-intelligence-agent, @health-monitor-agent, @data-analyst-agent, and @devops-agent. Your mission is to implement a BI platform and KPI tracking for DafnckMachine v3.1, ensuring comprehensive business metrics, executive reporting, and actionable revenue analytics. Document all BI setup and KPI tracking procedures with clear guidelines and best practices. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - All outputs must be saved in: `01_Machine/04_Documentation/vision/Phase_5/17_Monitoring_Analytics/`

2. **Collect Data/Input**
   - Reference BI and KPI tracking requirements
   - Review previous BI, KPI, and revenue analytics documentation if available
   - Gather standards for dashboard creation, KPI definitions, and business metrics

3. **Save Output**
   - Save business intelligence setup: `Business_Intelligence_Setup.md`
   - Save KPI tracking framework: `KPI_Tracking_Framework.json`
   - Save revenue analytics implementation: `Revenue_Analytics_Implementation.md`
   - Save business metrics framework: `Business_Metrics_Framework.json`
   - Minimal JSON schema example for KPI tracking framework:
     ```json
     {
       "dashboardCreation": true,
       "kpiDefinitions": ["MRR", "ARR", "ChurnRate"],
       "businessMetricsTracking": true,
       "executiveReporting": true
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P05-S17-T05

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] BI platform and KPI tracking are implemented and operational
   - [ ] Documentation and configs are clear and complete
   - [ ] Task status updated in workflow tracking files
