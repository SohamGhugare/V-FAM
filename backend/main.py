from fastapi import FastAPI
from dotenv import find_dotenv, load_dotenv
import uvicorn

from database import Database
from routers import user


app = FastAPI()
database = Database()

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

@app.get("/")
async def index():
    return {"data": "root"}

# Including routers
app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
    # SQLModel.metadata.create_all(Database().engine)
