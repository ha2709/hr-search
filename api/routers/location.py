import os
from dotenv import load_dotenv

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, databases
from ..schemas.location import Location
from ..utils.security import verify_api_key
from ..utils.rate_limit import rate_limited

location_router = APIRouter()
load_dotenv()
max_calls = int(os.getenv("MAX_CALLS", default=2))
time_frame = int(os.getenv("TIME_FRAME", default=60))

@location_router.get("/locations", response_model=List[Location])
@rate_limited(max_calls=max_calls, time_frame=time_frame)
def get_locations(
    db: Session = Depends(databases.get_db), api_key: str = Depends(verify_api_key)
):
    return db.query(models.Location).all()
