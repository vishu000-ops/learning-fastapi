from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil


app = fastAPI()

@app.get("/hello")
def get_marks()
