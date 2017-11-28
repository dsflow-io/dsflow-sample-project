# job: dashboard-previsions_pluie_paris

1) Edit job_specs.yaml to customize dashboard specifications

For instance, add dependencies:
```
dependencies:
  - UPSTREAM_JOB_NAME
```

2) Run your dashboard with `dsflow run dashboard-previsions_pluie_paris`

3) Go to http://localhost:8050/ to see the dashboard

4) Edit dashboard-previsions_pluie_paris.py to customize your dashboard