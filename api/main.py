import os
import time
from typing import Optional, List
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends, Query, status, Request
import uvicorn
# from pydantic import BaseModel
from sqlalchemy.orm import Session
from functools import wraps

from . import schemas, models, databases
from api.utils.rate_limit import rate_limited

from api.models import Department, Position, Location, Status, Employee
from .routers.employee import router as employee_router


app = FastAPI()

# Endpoint to get a list of all employees
app.include_router(employee_router,  tags=["employees"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

if __name__ == "__main__":
    

    uvicorn.run(app, host="127.0.0.1", port=8001)
