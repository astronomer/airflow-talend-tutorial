# airflow-talend-tutorial
This repo contains an Astronomer project with two example DAGs showing how to use Airflow to execute Talend jobs. A guide discussing the DAGs and concepts in depth can be found [here](https://www.astronomer.io/guides/airflow-talend-integration).

## Tutorial Overview
There are a few main ways to execute Talend jobs with Airflow:

 - Containerize Talend Studio jobs and execute them using the KubernetesPodOperator
 - Execute Talend Cloud jobs using the Talend API and the SimpleHttpsOperator

This tutorial has one DAG to illustrate each method.

## Requirements
In addition to the Astronomer CLI, to follow this tutorial you will need the following:

- A Talend Cloud account
- Talend Studio installed locally
- Docker installed locally
- A Dockerhub account, or other Docker registry

## Getting Started
The easiest way to run these example DAGs is to use the Astronomer CLI to get an Airflow instance up and running locally:

 1. [Install the Astronomer CLI](https://www.astronomer.io/docs/cloud/stable/develop/cli-quickstart)
 2. Clone this repo somewhere locally and navigate to it in your terminal
 3. Initialize an Astronomer project by running `astro dev init`
 4. Start Airflow locally by running `astro dev start`
 5. Navigate to localhost:8080 in your browser and you should see the tutorial DAGs there
 
Refer to the detailed guide linked above for instructions on how to get Airflow set up specifically for these DAGs. 
