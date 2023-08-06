import uvicorn
from fastapi import FastAPI

from config import settings


app = FastAPI()


@app.get("/")
def health_check() -> dict[str, str]:
    return {"Health check": "All right"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
