from asyncio import tasks
import json
from textwrap import dedent
import pendulum
import os
from airflow import DAG
from airflow.operators.python import PythonOperator


with DAG(
    'xray_training',
    default_args = {'retries':2},
    description = 'Covid Detection usung X-ray plates',
    schedule_interval = "@weekly",
    start_date = pendulum.datetime(2023,7,2, tz="UTC"),
    catchup = False,
    tags = ['xray_training']
) as dag:
    def training(**kwargs):
        from xray.pipeline.training_pipeline import Trainigpipeline
        training_pipeline = Trainigpipeline()
        training_pipeline.run_pieline()

    
    def sync_artifacts_to_s3_bucket(**kwargs):
        os.system(f'aws s3 sync app/artifacts s3://xray11/artifacts/')
        os.system(f'aws s3 sync app/saved_models s3://xray11/saved_models/')

    

    training_pipeline = PythonOperator(
        task_id = 'training_pipeline',
        python_callable = training,

    )

    sync_data_to_s3 = PythonOperator(
        task_id = 'sync_data_to_s3',
        python_callable = sync_artifacts_to_s3_bucket,

    )

    training_pipeline >> sync_data_to_s3


        
        


