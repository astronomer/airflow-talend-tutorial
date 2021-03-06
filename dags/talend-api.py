from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from datetime import datetime, timedelta
import json

# This DAG uses the SimpleHttpOperator to execute Talend jobs via the Talend API.
# A Talend Cloud license is required in order to access the API.
# For more information on when to use this method when working with Airflow and Talend, check out the guide here:
# https://www.astronomer.io/guides/airflow-talend-integration

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
        http_conn_id='talend_api', # Connection to the Talend API with an API key for access
        endpoint='/tmc/v2.2/executions', # API endpoint that will run a job
        data=json.dumps({"executable": "5fb2f5126a1cd451b07bee7a"}), # The executable ID for the Talend job you want to run
    ) 