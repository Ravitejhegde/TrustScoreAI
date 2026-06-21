from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import FileResponse

import shutil
import uuid

from services.analysis_pipeline import analyze_image

from services.results_formatter import format_results

from services.pdf_generator import generate_pdf


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

    unique_name = (

        f"{uuid.uuid4()}_{image.filename}"

    )

    path = f"uploads/{unique_name}"

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


@app.post("/download-report")

async def download_report(

    image: UploadFile = File(...)

):

    unique_name = (

        f"{uuid.uuid4()}_{image.filename}"

    )

    path = f"uploads/{unique_name}"

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

    pdf = generate_pdf(

        result

    )

    return FileResponse(

        pdf,

        media_type="application/pdf",

        filename="trustscore_report.pdf"

    )