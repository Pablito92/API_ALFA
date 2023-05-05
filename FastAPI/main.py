from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from fastapi.staticfiles import StaticFiles
#from typing import List, Union
#import simplejson as json
#from models.models import MateriaPrima
from routers import routes

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "file:///C:/Users/celesio.SILOFERTIL01/fastapi/MeuProjeto/index.html",
    "file:///C:/Users/celesio.SILOFERTIL01/fastapi/MeuProjeto/scripts.js",
    "C:/Users/celesio.SILOFERTIL01/fastapi/MeuProjeto/index.html",
    "C:/Users/celesio.SILOFERTIL01/fastapi/MeuProjeto/scripts.js"
]

app = FastAPI()
#app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    #allow_origins=origins,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)