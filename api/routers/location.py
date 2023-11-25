from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, databases
from ..schemas.location import Location
from ..utils.security import verify_api_key


location_router = APIRouter()


@location_router.get("/locations", response_model=List[Location])
def get_locations(
    db: Session = Depends(databases.get_db), api_key: str = Depends(verify_api_key)
):
    return db.query(models.Location).all()
