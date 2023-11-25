from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List
from .. import models, databases
from ..schemas.department import Department, DepartmentCreate, DepartmentBase
from ..utils.security import verify_api_key

department_router = APIRouter()


@department_router.get("/departments", response_model=List[Department])
def get_departments(
    db: Session = Depends(databases.get_db), api_key: str = Depends(verify_api_key)
):
    return db.query(models.Department).all()
