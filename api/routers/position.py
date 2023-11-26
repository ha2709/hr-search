import os
from dotenv import load_dotenv
from utils.rate_limit import rate_limited
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List
import models, databases
from schemas.position import Position
from utils.security import verify_api_key


position_router = APIRouter()
load_dotenv()
max_calls = int(os.getenv("MAX_CALLS", default=2))
time_frame = int(os.getenv("TIME_FRAME", default=60))


@position_router.get("/positions", response_model=List[Position])
@rate_limited(max_calls=max_calls, time_frame=time_frame)
async def get_positions(
    request: Request,
    db: Session = Depends(databases.get_db), api_key: str = Depends(verify_api_key)
):
    return db.query(models.Position).all()
