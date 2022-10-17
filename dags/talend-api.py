"""
This DAG uses the SimpleHttpOperator to execute Talend jobs via the Talend API.
A Talend Cloud license is required in order to access the API.
For more information on when to use this method when working with Airflow and Talend, check out the guide here:
https://www.astronomer.io/guides/airflow-talend-integration

"""

from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from datetime import datetime
import json



with DAG('talend_api_jobs',
    start_date=datetime(2019, 1, 1),
    schedule_interval='@once',
    doc_md=__doc__,
    default_args={
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
    },
) as dag:

    talend1 = SimpleHttpOperator(
        task_id='talend_api',
        method='POST',
        http_conn_id='talend_api', # Connection to the Talend API with an API key for access
        endpoint='/tmc/v2.2/executions', # API endpoint that will run a job
        data=json.dumps({"executable": "5fb2f5126a1cd451b07bee7a"}), # The executable ID for the Talend job you want to run
    )
