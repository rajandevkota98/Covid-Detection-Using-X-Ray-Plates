# Covid Detection Using X-Ray Plates

## Table of Contents

- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Proposed Solution](#proposed-solution)
- [Tech Stack](#tech-stack)
- [Infrastructure Required](#infrastructure-required)
- [Architecture](#architecture)
- [DEPLOYMENT](#deployment)
- [How to Run the Project](#how-to-run-the-project)
- [FastAPI](#FastAPI)
- [Airflow-Setup](#Airflow-Setup)


## Introduction

This project aims to build an efficient and accurate COVID Detection System (CDS) using transfer learning to classify X-ray images of patients into two classes: normal and COVID-19 positive cases. The system will aid healthcare professionals in making quicker and more accurate decisions for potential cases of COVID-19 using X-ray images.

## Problem Statement

The primary goal of this project is to minimize false predictions while accurately identifying COVID-19 positive cases through X-ray images.

## Proposed Solution

Our solution involves using transfer learning, where we leverage pre-trained deep learning models to achieve accurate COVID-19 detection from X-ray images.

## Tech Stack

- Python
- FastAPI
- Docker
- GitHub Action
- Airflow

## Infrastructure Required

- AWS S3: Used for storing datasets and model artifacts.
- AWS ECR: Container registry to store Docker images.
- AWS EC2: Virtual server for deploying the FastAPI application.
- Git: Version control system for collaborative development.

## Architecture

![Architecture Diagram](https://github.com/rajandevkota98/Covid-Detection-Using-X-Ray-Plates/blob/main/flowchart/architecture.png)

## Deployment

![Deployment Diagram](https://github.com/rajandevkota98/Covid-Detection-Using-X-Ray-Plates/blob/main/flowchart/deployment.png)


## How to Run the Project

Follow these steps to run the project:

```bash

#Step1 : Clone the project
git clone https://github.com/rajandevkota98/Covid-Detection-Using-X-Ray-Plates.git

# Step 2: Create a Conda Environment and Activate it
conda create -n <virtual_environment_name> python=3.8 -y
conda activate <virtual_environment_name>

# Step 3: Install All the Requirements
pip install -r requirements.txt

# Step 4: Set up Your AWS Account
export ACCESS_KEY_ID=<access-key>
export AWS_SECRET_KEY=<secret-key>
export AWS_REGION=<aws-region>
export API_KEY=<api-key>
export BUCKET_NAME=<bucket-name>
export AWS_ECR_LOGIN_URI=<ecr-login-uri>
export ECR_REPOSITORY_NAME=<ecr-repository-name>
# Step 5: Download and Prepare the Dataset
# Download the dataset and keep it in the "creating data" folder.

# Step 6: Set Up AWS S3 Bucket
python run s3_setup.py

# Step 7: Run the FastAPI Application
python main.py


``` 

## FastAPI:
![FASTAPI SSS Diagram](https://github.com/rajandevkota98/Covid-Detection-Using-X-Ray-Plates/blob/main/flowchart/Screenshot%20from%202023-08-04%2013-53-48.png)


## Airflow-Setup
If you properly setup and run the github action, you will get the docker image in your EC2 instance, you can access airflow from there.


