from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, databases
from ..schemas.position import Position
from ..utils.security import verify_api_key


position_router = APIRouter()


@position_router.get("/positions", response_model=List[Position])
def get_positions(db: Session = Depends(databases.get_db), api_key: str = Depends(verify_api_key)):
    return db.query(models.Position).all()
