import redis.asyncio as aioredis
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Depends, Query, status
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
# from pydantic import BaseModel
from sqlalchemy.orm import Session
 

from . import models
from . import schemas
from . import databases 

app = FastAPI()

# Create a Redis connection
# redis = aioredis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(redis)


# Endpoint to get a list of all employees
@app.get("/employees/", response_model=List[schemas.Employee], dependencies=[Depends(RateLimiter(times=2, seconds=5))])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(databases.get_db)):
    employees = db.query(models.Employee).offset(skip).limit(limit).all()
    return employees


# Endpoint to create a new employee
@app.post("/employees/", response_model=schemas.Employee, status_code=status.HTTP_201_CREATED, dependencies=[Depends(RateLimiter(times=2, seconds=5))])
def create_employee(employee: schemas.EmployeeCreate , db: Session = Depends(databases.get_db)):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# Endpoint to get a single employee by ID
@app.get("/employees/{employee_id}", response_model=schemas.Employee, dependencies=[Depends(RateLimiter(times=2, seconds=5))])
def read_employee(employee_id: int, db: Session = Depends(databases.get_db)):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


@app.get("/search/")
def search_employees(
    status: str = Query(None, title="Status", enum=["Active", "Not started", "Terminated"]),
    location: str = None,
    company: str = None,   
    department: str = None,
    position: str = None,
    db: Session = Depends(databases.get_db)
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
