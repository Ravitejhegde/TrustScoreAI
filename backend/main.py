from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil

app = FastAPI()

app.add_middleware(

    CORSMiddleware,

    allow_origins=["http://localhost:5173"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)

@app.post("/upload")

async def upload_image(

    image: UploadFile = File(...)

):

    file_path = f"uploads/{image.filename}"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(

            image.file,

            buffer

        )

    return {

        "filename": image.filename,

        "message": "Image uploaded successfully"

    }