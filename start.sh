#!bin/sh
python main.py &
nohup airflow scheduler &
airflow webserver