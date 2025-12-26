from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import os

from ripeness_detector import detect_ripeness

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

latest_result = {"status": "Unknown"}

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ripeness = detect_ripeness(file_path)
    latest_result["status"] = ripeness

    return {"ripeness": ripeness}

@app.get("/status")
def get_status():
    return JSONResponse(content=latest_result)
