# job name: download-car_speed_limits

IMPORTANT: You just generated the job, but it hasn't run yet.

1) Edit download-car_speed_limits/job_specs.yaml to customize job specifications.
In particular, make sure source_path (where the data comes from)
and sink_path (where the data will be written) are properly set.

You can include a parameter in the paths.
For instance, `source_path: http://domain.com/data.csv?date=2018-02-09`

2) Execute your flow with `dsflow run download-car_speed_limits 2018-02-09`

3) Once this job has run, you can start working on the newly imported data, with
`create_table_from_csv` or `create_table_from_json`.

Note: "2018-02-09" (`ds` parameter) is a standard way to partition your data by date.
It makes sense if the data source takes a date parameter, or if data changes over time.
See explanations about `dim` and `fact` tables in dsflow README.