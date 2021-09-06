from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator


default_args = {"owner": "airflow", "start_date": datetime(2019, 9, 1)}

dag = DAG(dag_id="sample_dag", default_args=default_args, schedule_interval="@daily")

t1 = BashOperator(task_id="print_time", bash_command="date", dag=dag)

t1