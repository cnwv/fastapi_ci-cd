from fastapi import FastAPI 
from settings import settings
app = FastAPI()


@app.get("/")
def index():
    return "Hello world!"

@app.get("/secret")
def secret():
    return settings.general.my_secret
