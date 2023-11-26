import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, databases
from schemas.status import Status
from  utils.security import verify_api_key
from utils.rate_limit import rate_limited


status_router = APIRouter()
load_dotenv()
max_calls = int(os.getenv("MAX_CALLS", default=2))
time_frame = int(os.getenv("TIME_FRAME", default=60))

@status_router.get("/statuses", response_model=List[Status])
@rate_limited(max_calls=max_calls, time_frame=time_frame)
def get_statuses(
    db: Session = Depends(databases.get_db), api_key: str = Depends(verify_api_key)
):
    return db.query(models.Status).all()
