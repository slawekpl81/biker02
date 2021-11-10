# uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def start():
    return {"message": "start"}
