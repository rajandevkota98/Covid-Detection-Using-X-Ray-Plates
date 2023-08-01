FROM python:3.8.5-slim-buster
RUN apt update -y and install awscli -y
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "python", 'main.py' ]