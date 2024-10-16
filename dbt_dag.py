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
  pre_dbt_workflow = EmptyOperator(task_id="pre_dbt_workflow")

  # DBT
  dbt_deps = BashOperator(
      task_id = 'dbt_deps',
      bash_operand=f'{ENTRYPOINT_CMD} && dbt deps',
      env={"PATH_TO_DBT_VENV": PATH_TO_DBT_VENV},
      cwd=PATH_TO_DBT_PROJECT,
  )

dbt_run_models = BashOperator(
    task_id='dbt_run_models',
    bash_command=f'{ENTRYPOINT_CMD} && dbt run --models .',
    env={"PATH_TO_DBT_VENV": PATH_TO_DBT_VENV},
    cwd=PATH_TO_DBT_PROJECT,
)

dbt_run_stg_customers = BashOperator(
    task_id='dbt_run_stg_orders',
    bash_command=f'{ENTRYPOINT_CMD} && dbt run -s stg_orders',
    env={"PATH_TO_DBT_VENV": PATH_TO_DBT_VENV},
    cwd=PATH_TO_DBT_PROJECT,
)

dbt_run_stg_orders = BashOperator(
    task_id='dbt_run_stg_orders',
    bash_command=f'{ENTRYPOINT_CMD} && dbt run -s stg_orders',
    env="PATH_TO_DBT_VENV": PATH_TO_DBT_VENV},
    cwd=PATH_TO_DBT_PROJECT,
)

dbt_run_stg_payments = BashOperator(
    task_id='dbt_run_stg_payments',
    bash_command=f'{ENTRYPOINT_CMD} && dbt run -s stg_payments,
    env={"PATH_TO_DBT_VENV": PATH_TO_DBT_VENV},
    cwd=PATH_TO_DBT_PROJECT,
    )














