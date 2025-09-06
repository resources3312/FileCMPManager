from utils import (BytesCMPManager)
from validator import UserRequestAccept
from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import FileResponse, RedirectResponse

app = FastAPI()

def requestAccept(state: int) -> bool:
    return True if state > 0 else False

@app.get("/")
async def redirect_to_home_page():
    return RedirectResponse(url="/home")

@app.get("/home")
async def show_home_page(request: Request):
    return FileResponse("templates/index.html")

@app.get("/services")
async def show_home_page():
    return FileResponse("templates/services.html")

@app.get("/api")
async def show_home_page():
    return FileResponse("templates/api.html")

@app.get("/about")
async def show_home_page():
    return FileResponse("templates/about.html")

@app.get("/services/filepair/")
async def show_filepair_page():
    return FileResponse("/templates/filepair.html")

@app.post("/services/filepair/cmp")
async def ret_filepair_cmp_result(request: Request, file_1: UploadFile, file_2: UploadFile):
    return {"result": -2}  if not UserRequestAccept(request.cookies.get("token")).getRequestAccept() else {"result": 0} if BytesCMPManager.cmpByteArrayPair(await file_1.read(), await file_2.read()) else {"result": -1}
