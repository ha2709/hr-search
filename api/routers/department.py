import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List
import models, databases
from schemas.department import Department, DepartmentCreate, DepartmentBase
from utils.security import verify_api_key
from utils.rate_limit import rate_limited


department_router = APIRouter()
load_dotenv()
max_calls = int(os.getenv("MAX_CALLS", default=2))
time_frame = int(os.getenv("TIME_FRAME", default=60))

@department_router.get("/departments", response_model=List[Department])
@rate_limited(max_calls=max_calls, time_frame=time_frame)
def get_departments(
    db: Session = Depends(databases.get_db), api_key: str = Depends(verify_api_key)
):
    return db.query(models.Department).all()
