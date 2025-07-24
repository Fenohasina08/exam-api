from fastapi import FastAPI
from starlette.responses import JSONResponse
from typing import Optional

app = FastAPI()



@app.get("/hello")
async def say_hello_world():
    return JSONResponse(content={"message": "Hello World"}, status_code=200)

@app.get("/welcome")
async def say_welcome(name: str):
    return JSONResponse(content={"message": f"Welcome {name}"}, status_code=200)

