"""
This is a server API written with FastAPI, 
it demonstrates deployment with cicd principles on aws
"""
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def func():
    """Serves a static page from our server"""
    return FileResponse("./src/index.html")
