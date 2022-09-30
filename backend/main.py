from fastapi import FastAPI
from database import Database
import uvicorn
from routers.user import router as u_router

app = FastAPI()
database = Database()

@app.get("/")
async def index():
    return {"data": "root"}

# Including routers
app.include_router(u_router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
    # SQLModel.metadata.create_all(Database().engine)
