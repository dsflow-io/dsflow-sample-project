# job: create-table-meteoparis

1) Edit job_specs.yaml to customize job specifications

For instance, add dependencies:
```
dependencies:
  - UPSTREAM_JOB_NAME
```

2) Execute your flow with `dsflow run create-table-meteoparis`