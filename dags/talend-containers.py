"""
### Execute Talend Jobs via the KubernetesPodOperator

This DAG uses the KubernetesPodOperator to execute Talend jobs. The Talend jobs are containerized,
saved to a registry, and then orchestrated from Airflow. For more information on how to containerize
Talend jobs, and when to use this method when working with Airflow, check out the guide here:
https://www.astronomer.io/guides/airflow-talend-integration
"""


from airflow import DAG
from datetime import datetime
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.operators.email import EmailOperator
from airflow import configuration as conf



namespace = conf.get('kubernetes', 'NAMESPACE')

# This will detect the default namespace locally and read the
# environment namespace when deployed to Astronomer.
if namespace =='default':
    config_file = '/usr/local/airflow/include/.kube/config'
    in_cluster=False
else:
    in_cluster=True
    config_file=None


# Define recipient emails for successful completion notification
email_to = ["noreply@astronomer.io"]

with DAG(
    'talend_containerized_jobs',
    doc_md=__doc__,
    start_date=datetime(2019, 1, 1),
    schedule_interval='@once',
    default_args={
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
    }
) as dag:

    talend1 = KubernetesPodOperator(
                namespace=namespace,
                image="yourregistry/talendjob:hello", # image with your containerized Talend job
                name="talend-test-hello",
                task_id="hello-world",
                in_cluster=in_cluster, # if set to true, will look in the cluster, if false, looks for file
                cluster_context='docker-desktop', # is ignored when in_cluster is set to True
                config_file=config_file,
                is_delete_operator_pod=True,
                get_logs=True
                )

    talend2 = KubernetesPodOperator(
                namespace=namespace,
                image="yourregistry/talendjob:dropbox", # image with your containerized Talend job
                name="talend-test-random",
                task_id="dropbox",
                in_cluster=in_cluster,
                cluster_context='docker-desktop',
                config_file=config_file,
                is_delete_operator_pod=True,
                get_logs=True
                )

    send_email = EmailOperator(
                    task_id='send_email',
                    to=email_to,
                    subject='Talend Jobs Completed Successfully',
                    html_content='<p>Your containerized Talend jobs have completed successfully. <p>'
                )


    talend1 >> talend2 >> send_email
