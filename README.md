##  Covid  Detection Using X-Ray Plates

## Problem Satement:
It aims to classify X-ray images of patients into two classes: normal and COVID-19 positive cases. X-ray images are an essential diagnostic tool for identifying potential cases of COVID-19, and this automated system will aid healthcare professionals in making quicker and more accurate decisions.


## Proposed Solution:
To address the challenge of COVID-19 detection through X-ray images, we propose transfer learning based efficient and accurate COVID Detection System (CDS). The primary goal of this system is to minimize false predictions while identifying COVID-19 positive cases correctly.


## Tech Stack Used
-Python
-FastAPI
-Docker
-Github Action
-Airflow

## Infrastructure REquired
-AWS S3
-AWS ECR
-AWS EC2
-Git

## Architecture


## How to run the project?
step-1: Create a conda environment and activate it
```Conda create -n <virtual_environmanet_name> python=3.8 -y```
```conda activate <virtual_environmanet_name>```

step2: Install all the requirements
```pip install -r requirements.txt```


step3: Set up your aws account:
```export ACCESS_KEY_ID=<access-key>```
```export AWS_SECRET_KEY=<secret-key>```
```export AWS_REGION=<aws-region>```
```export API_KEY=<api-key>```
```export BUCKET_NAME=<bucket-name>```

Dataset link: 
Download this dataset and keep it in creating data folder.

step4: run s3_setup.py
```python run s3_setup.py```

step5: run main.py

#  FastAPI
