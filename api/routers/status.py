from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, databases
from ..schemas.status import Status
from ..utils.security import verify_api_key
status_router = APIRouter()


@status_router.get("/statuses", response_model=List[Status])
def get_statuses(db: Session = Depends(databases.get_db), api_key: str = Depends(verify_api_key)):
    return db.query(models.Status).all()
