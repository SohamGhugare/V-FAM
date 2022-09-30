from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def index(self):
    return {"data": "root"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)