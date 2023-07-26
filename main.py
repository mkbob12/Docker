from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import logging

app = FastAPI()
templates = Jinja2Templates(directory="./")

# Logging 설정
logging.basicConfig(level=logging.INFO)

# mount 
#app.mount("/soochan", StaticFiles(directory="soochan"), name="static")


@app.get("/soochan")
async def root(request: Request):
    logging.info("Hello World")
    return templates.TemplateResponse("mypage.html", {"request": request, "name": "Your Name", "introduction": "Write your introduction here!"})
    #return {"hello"}
