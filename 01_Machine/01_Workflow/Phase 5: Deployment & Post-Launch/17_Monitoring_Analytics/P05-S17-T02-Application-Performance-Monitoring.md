---
phase: P05
step: S17
task: T02
task_id: P05-S17-T02
title: Application Performance Monitoring
agent:
  - "@performance-load-tester-agent"
  - "@health-monitor-agent"
  - "@data-analyst-agent"
  - "@devops-agent"
previous_task: P05-S17-T01
next_task: P05-S17-T03
version: 3.1.0
source: Step.json
---

# Super Prompt
You are @performance-load-tester-agent, collaborating with @health-monitor-agent, @data-analyst-agent, and @devops-agent. Your mission is to implement and configure robust Application Performance Monitoring (APM) for DafnckMachine v3.1, ensuring real-time performance tracking, transaction tracing, error monitoring, and actionable dashboard visualizations. Document all APM setup and dashboard procedures with clear guidelines and best practices. Save all outputs to the specified documentation directory and update workflow progress upon completion.

1. **Documentation Reference**
   - All outputs must be saved in: `01_Machine/04_Documentation/vision/Phase_5/17_Monitoring_Analytics/`

2. **Collect Data/Input**
   - Reference APM and performance monitoring requirements
   - Review previous APM, metrics, and dashboard documentation if available
   - Gather standards for agent setup, metrics, tracing, and visualization

3. **Save Output**
   - Save APM implementation guide: `APM_Implementation_Guide.md`
   - Save performance metrics configuration: `Performance_Metrics_Configuration.json`
   - Save performance dashboard implementation: `Performance_Dashboard_Implementation.md`
   - Save metrics visualization config: `Metrics_Visualization.json`
   - Minimal JSON schema example for performance metrics configuration:
     ```json
     {
       "apmAgentSetup": true,
       "performanceMetrics": ["latency", "throughput", "errorRate"],
       "transactionTracing": true,
       "errorTracking": true
     }
     ```

4. **Update Progress**
   - Upon completion, update `Step.json` and `DNA.json` to mark this task as SUCCEEDED
   - Proceed to the next task: P05-S17-T03

5. **Self-Check**
   - [ ] All required files are present in the documentation directory
   - [ ] APM and dashboards are implemented and operational
   - [ ] Documentation and configs are clear and complete
   - [ ] Task status updated in workflow tracking files 
