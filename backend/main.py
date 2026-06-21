from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

from fastapi.middleware.cors import CORSMiddleware

import shutil

from services.analysis_pipeline import analyze_image

from services.results_formatter import format_results

app = FastAPI()

app.add_middleware(

    CORSMiddleware,

    allow_origins=[

        "http://localhost:5173"

    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


@app.post("/analyze")

async def analyze(

    image: UploadFile = File(...)

):

    path = f"uploads/{image.filename}"

    with open(

        path,

        "wb"

    ) as buffer:

        shutil.copyfileobj(

            image.file,

            buffer

        )

    data = analyze_image(

        path

    )

    result = format_results(

        data

    )

    return result