from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str
    
@app.post("/students/")
async def create_item(item: StudentCreateSchema):
    return item
