FROM python:3.8.5-slim-buster
RUN apt update -y and install awscli -y
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENV AIRFLOW_HOME = "/app/airflow"
ENV AIRFLOW__CORE__DAGBG_IMPORT_TIMEOUT = 1000
ENV AIRFLOW__CORE__ENABLE_XCOM_PICKLING=True
RUN airflow db init 
RUN airflow users create  -e r.devkota.98@gmail.com -f Rajan -l Devkota -p admin -r Admin  -u admin
RUN chmod 777 start.sh
ENTRYPOINT [ "/bin/sh" ]
CMD ["start.sh"]