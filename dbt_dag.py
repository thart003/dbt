import os
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

airflow_home=os.environ['AIRFLOW_HOME']

#Define paths to the DBT project and virtual environment
PATH_TO_DBT_PROJECT = f'{airflow_home}/dbt_project'
PATH_TO_DBT_VENV = f'{airflow_home}/dbt_venv/bin/activate'
PATH_TO_DBT_VARS = f'{airflow_home}/dbt_project/dbt.env'
ENTRYPOINT_CMD = f"source {PATH_TO_DBT_VENV} && source {PATH_TO_DBT_VARS}"

default_args = {
  "owner": "Taylor Hart",
  "retries": 0,
  "execution_timeout": timedelta(hours=1),
}

@dag(
  start_date=datetime(2024, 5, 9),
  schedule='@once',
  catchup=False,
  default_args=default_args,
)
def jaffle_shop_dbt_dag():
  








