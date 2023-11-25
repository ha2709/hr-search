import os
from dotenv import load_dotenv
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from .. import models, databases
from ..schemas.employee import Employee, EmployeeCreate, EmployeeBase
from ..utils.rate_limit import rate_limited
from ..utils.security import verify_api_key
from .company import get_company_display_columns

employee_router = APIRouter()
load_dotenv()
max_calls = int(os.getenv("MAX_CALLS", default=2))
time_frame = int(os.getenv("TIME_FRAME", default=60))


@employee_router.get("/employees", response_model=List[Employee])
# @rate_limited(max_calls=max_calls, time_frame=time_frame)
async def read_employees(
    request: Request,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(databases.get_db),
    api_key: str = Depends(verify_api_key),
):
    employees = db.query(models.Employee).offset(skip).limit(limit).all()

    return employees


@employee_router.post(
    "/employees/", response_model=Employee, status_code=status.HTTP_201_CREATED
)
@rate_limited(max_calls=max_calls, time_frame=time_frame)
async def create_employee(
    request: Request,
    employee: EmployeeCreate,
    db: Session = Depends(databases.get_db),
    api_key: str = Depends(verify_api_key)
):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


@employee_router.get("/employees/{employee_id}", response_model=Employee)
@rate_limited(max_calls=max_calls, time_frame=time_frame)
async def read_employee(
    request: Request, employee_id: int, 
    db: Session = Depends(databases.get_db), 
    api_key: str = Depends(verify_api_key),
):
    db_employee = (
        db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    )
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


@employee_router.get("/search/", response_model=None)
@rate_limited(max_calls=max_calls, time_frame=time_frame)
async def search_employees(
    request: Request,
    status: str = None,
    location: str = None,
    company: str = None,
    department: str = None,
    position: str = None,
    db: Session = Depends(databases.get_db),
    api_key: str = Depends(verify_api_key),
):
    query = db.query(models.Employee)

    # Apply filters based on query parameters
    if status:
        query = query.filter(models.Employee.status.has(name=status))
    if location:
        query = query.filter(models.Employee.location.has(name=location))
    if department:
        query = query.filter(models.Employee.department.has(name=department))
    if position:
        query = query.filter(models.Employee.position.has(title=position))
    header_column = []
    if company:
        column_data = get_company_display_columns(company)
        header_column = ["first_name", "last_name"] + column_data + ["status"]
     
    results = query.all()
 
    # Filter the data based on the header_column
    filtered_results = []
    for employee in results:
        filtered_employee = {}

        # Include only the attributes present in header_column
        for key in header_column:
            if hasattr(employee, key):
                filtered_employee[key] = getattr(employee, key)

        filtered_results.append(filtered_employee)

 
    return filtered_results