from fastapi import FastAPI
from sqlmodel import SQLModel
from database import Database

app = FastAPI()

@app.get("/")
async def index(self):
    return {"data": "root"}

if __name__ == "__main__":
    # uvicorn.run("main:app", port=8080, reload=True)
    SQLModel.metadata.create_all(Database("sqlite:///backend/data/users.db").engine)
