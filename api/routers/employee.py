import os
from typing import List
from dotenv import load_dotenv
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_ 
from .. import models, databases
from ..schemas.employee import Employee, EmployeeCreate, EmployeeBase
from ..utils.rate_limit import rate_limited
from ..utils.security import verify_api_key
from ..utils.column import get_company_display_columns
 

employee_router = APIRouter()
load_dotenv()
max_calls = int(os.getenv("MAX_CALLS", default=2))
time_frame = int(os.getenv("TIME_FRAME", default=60))



@employee_router.get("/search/", response_model=None)
@rate_limited(max_calls=max_calls, time_frame=time_frame)
async def search_employees(
    request: Request,
    status: List[str] = Query(None),
    location: str = None,
    company: str = None,
    department: str = None,
    position: str = None,
    db: Session = Depends(databases.get_db),
    api_key: str = Depends(verify_api_key),
):
    query = db.query(models.Employee)
    print(35, status, type(status), location,location,department, position)
    status_string = status[0]
    # Split the string into a list
    status_list = status_string.split(',')
    print(50, len(status_list))
    results = []
    if (len(status_list) <2):
        results = apply_filters(query, status, location, department, position)
    else:
        status_array = []
        for status_item in status_list:
            status_array.append(status_item)
            print(45, status_array)
            temp = apply_filters(query, status_array, location, department, position)
            status_array = []
            print(47, temp)
            results += temp
    result_status = []
    
   # Apply filters based on query parameters
    
    header_column = []
 
    if company:
            column_data = get_company_display_columns(company)
    else:
        column_data = get_company_display_columns('company_3')
        # get all column header 
    header_column = ["first_name", "last_name"] + column_data + ["status"]
    print(77, results)
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

def apply_filters(query, status=None, location=None, department=None, position=None):
    print(79, status)
    if status:
        query = query.filter(models.Employee.status.has(name=status[0]))
    if location:
        query = query.filter(models.Employee.location.has(name=location))
    if department:
        query = query.filter(models.Employee.department.has(name=department))
    if position:
        query = query.filter(models.Employee.position.has(title=position))
    results = query.all()
    return results