# fast api
from fastapi import FastAPI

app = FastAPI()

from dotenv import load_dotenv
load_dotenv()

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.post("/build_graph")
async def build_graph():
  return {"message": "Graph built!"}