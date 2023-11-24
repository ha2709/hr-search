import os
from fastapi import APIRouter, HTTPException, Depends,Request, Query, status
from sqlalchemy.orm import Session
from .. import schemas, models, databases
from ..utils.rate_limit import rate_limited
from dotenv import load_dotenv

router = APIRouter()
load_dotenv()
max_calls = int(os.getenv("MAX_CALLS", default=2))
time_frame = int(os.getenv("TIME_FRAME", default=60))
@router.get("/employees/", response_model=list[schemas.Employee])
@rate_limited(max_calls=max_calls, time_frame=time_frame)
async def read_employees(
    request: Request,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(databases.get_db),
):
    employees = db.query(models.Employee).offset(skip).limit(limit).all()
    return employees

@router.post(
    "/employees/", response_model=schemas.Employee, status_code=status.HTTP_201_CREATED
)
def create_employee(
    employee: schemas.EmployeeCreate, db: Session = Depends(databases.get_db)
):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(databases.get_db)):
    db_employee = (
        db.query(models.Employee)
        .filter(models.Employee.id == employee_id)
        .first()
    )
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@router.get("/search/")
def search_employees(
    status: str = Query(
        None, title="Status", enum=["Active", "Not started", "Terminated"]
    ),
    location: str = None,
    company: str = None,
    department: str = None,
    position: str = None,
    db: Session = Depends(databases.get_db),
):
    query = db.query(models.Employee)

    # Apply filters based on query parameters
    if status:
        query = query.filter(models.Employee.status == status)
    if location:
        query = query.filter(models.Employee.location == location)
    if company:
        query = query.filter(models.Employee.company == company)
    if department:
        query = query.filter(models.Employee.department == department)
    if position:
        query = query.filter(models.Employee.position == position)

    results = query.all()
    return results

