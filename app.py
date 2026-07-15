from pathlib import Path
import shutil

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

# Import your processor
from processor import process_pdf

UPLOAD_FOLDER = Path("uploads")
PARSED_FOLDER = Path("parsed")

UPLOAD_FOLDER.mkdir(exist_ok=True)
PARSED_FOLDER.mkdir(exist_ok=True)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={}
)


@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    pdf_path = UPLOAD_FOLDER / file.filename

    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ########################################################
    # Call YOUR parser here.
    #
    # Example:
    #
    # md_path = process_pdf(pdf_path)
    #
    # It should return the markdown file path.
    ########################################################

    md_path = process_pdf(str(pdf_path))

    return JSONResponse(
        {
            "success": True,
            "filename": Path(md_path).name,
        }
    )


@app.get("/download/{filename}")
async def download(filename: str):

    file_path = PARSED_FOLDER / filename

    return FileResponse(
        path=file_path,
        media_type="text/markdown",
        filename=filename,
    )