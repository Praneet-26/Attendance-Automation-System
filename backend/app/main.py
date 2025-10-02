from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from backend.app.routes import professor_routes, student_routes


app = FastAPI(title="Attendance Automation System")

@app.get('/')
async def hello_world():
    return {"message":"hello World"}

@app.get('/greet/{name}')
async def greet_project(name:str,age:Optional[int] = 12) -> dict:
    return {"Message":f"Hello {name}. Your are {str(age)}"}


@app.post('/create_book')
async def create_book():
    pass

app.include_router(professor_routes.router, prefix="/professors", tags=["Professors"])
app.include_router(student_routes.router, prefix="/students", tags=["Students"])
