from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from datetime import datetime, timedelta
import json


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


with DAG('talend_api_jobs',
          schedule_interval='@once',
          default_args=default_args
          ) as dag:

    talend1 = SimpleHttpOperator(
        task_id='talend_api',
        method='POST',
        http_conn_id='talend_api',
        endpoint='/tmc/v2.2/executions',
        data=json.dumps({"executable": "5fb2f5126a1cd451b07bee7a"}),
    ) 