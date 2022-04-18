import uvicorn
from fastapi import FastAPI

from app.api.v1.api import api_router

app = FastAPI()


@app.get("/")
def index():
    return "Booking System API"


app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="127.0.0.1", port=5000, log_level="info", reload="true"
    )
