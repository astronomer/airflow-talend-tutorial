# talend-astronomer-tutorial
This repo is home to a tutorial for how to use Astronomer+Airflow with Talend. It contains reference DAGs and other supporting materials needed for a presentation and demo.

## Tutorial Overview
There are a few ways to execute Talend jobs with Airflow - containerizing the jobs and executing them with the KubernetesPodOperator, or executing the jobs via the Talend API using the SimpleHTTPSOperator, or something similar. This tutorial focuses on the former, since the later is only possible with a Talend Cloud enterprise account.

An Airflow DAG that will execute published Talend jobs can be found in the `dags/` directory. The Talend jobs used in this tutorial are published to this public registry on docker hub: https://hub.docker.com/repository/docker/kentdanas/talend-astro-tutorial

Some brief introductory slides are saved here as well; they introduce the topic and set the stage for a demonstration with the Talend jobs and DAG. A written tutorial that can be sent out as needed can be found here: https://www.notion.so/astronomerio/Containerized-Talend-Jobs-on-Astronomer-f264beb82688434b8f07b0290664c0cb


## Requirements
To follow this tutorial from scratch, including containerizing the Talend jobs, you must have the following installed locally:

- Talend Studio
- Docker
- Astronomer CLI



