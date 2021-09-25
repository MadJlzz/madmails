"""
This module is the entrypoint of the project.
It runs a FastAPI webserver with uvicorn.
"""
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/hello/{name}")
async def hello(name: str):
    return {"message": f"hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True, log_level="info")
