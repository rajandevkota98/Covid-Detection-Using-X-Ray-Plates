import os, sys
from xray.exception  import XrayException
from xray.logger import logging
from xray.pipeline.training_pipeline import Trainigpipeline
from uvicorn import run as app_run
from fastapi import FastAPI, File, UploadFile,Request
from xray.constants.application import APP_HOST,APP_PORT
from starlette.responses import RedirectResponse,FileResponse
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
import shutil
from xray.pipeline.prediction_pipeline import single_prediction, bulk_prediction

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline = Trainigpipeline()
        train_pipeline.run_pieline()
        return Response('Model is trained successfully')
    except Exception as e:
        raise XrayException(e,sys)     

UPLOAD_DIRECTORY = "Uploaded"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


@app.post("/single_prediction_route")
async def single_prediction_route(request:Request,image_file: UploadFile = File(...)):
    try:
        image_path = os.path.join(UPLOAD_DIRECTORY, image_file.filename)
        with open(image_path, "wb") as f:
            shutil.copyfileobj(image_file.file, f)
        prediction = single_prediction(image_path=image_path)
        return prediction
    except Exception as e:
            raise XrayException(e,sys)
    
@app.post("/bulk_prediction-route")
async def bulk_prediction_route(zip_file: UploadFile = File(...)):
    zip_path = os.path.join(UPLOAD_DIRECTORY, zip_file.filename)
    with open(zip_path, "wb") as f:
        shutil.copyfileobj(zip_file.file, f)
    predicted_zip_file = bulk_prediction(zip_path)
    return FileResponse(predicted_zip_file, media_type="application/zip", headers={"Content-Disposition": "attachment; filename=predicted_files.zip"})


        
if __name__ == "__main__":
    app_run(app,host=APP_HOST,port=APP_PORT)




