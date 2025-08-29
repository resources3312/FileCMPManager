from utils import FileCMPManager
from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import FileResponse, RedirectResponse

app = FastAPI()

@app.get("/")
def redirect_to_home_page():
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
    return {"result": 0} if FileCMPManager.cmpByteArrayPair(await file1.read(), await file2.read()) else {"result":-1}
