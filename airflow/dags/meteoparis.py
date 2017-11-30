from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import datetime as dt
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': dt.datetime(2017, 11, 29),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('meteoparis', default_args=default_args)

templated_command = "python $DSFLOW_ROOT/dsflow-run.py {{ params.job_name }} {{ ds }}"

def dsflow_job_operator(job_name):
    return BashOperator(
        task_id=job_name,
        bash_command=templated_command,
        params={'job_name': job_name},
        dag=dag)


t1 = dsflow_job_operator("download-meteoparis")
t2 = dsflow_job_operator("create-table-meteoparis")
t3 = dsflow_job_operator("create-table-meteo_agg")

t1 >> t2 >> t3
