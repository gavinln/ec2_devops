from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta

one_day_ago = datetime.combine(datetime.today() - timedelta(1),
                                  datetime.min.time())

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': one_day_ago,
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('first', default_args=default_args,
          schedule_interval=timedelta(hours=1))

# t1, t2 and t3 are examples of tasks created by instatiating operators
t1 = BashOperator(
    task_id='print_date_first',
    bash_command='date',
    dag=dag)
