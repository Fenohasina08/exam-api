from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from starlette.responses import JSONResponse

app = FastAPI()


students_db = []


class Student(BaseModel):
    Reference: str
    FirstName: str
    LastName: str
    Age: int


@app.get("/hello")
async def say_hello_world():
    return JSONResponse(content={"message": "Hello world"}, status_code=200)

@app.get("/welcome")
async def say_welcome(name: str):
    return JSONResponse(content={"message": f"Welcome {name}"}, status_code=200)


 

@app.get("/students")
async def get_students():
    return JSONResponse(content=[student.dict() for student in students_db], status_code=200)

