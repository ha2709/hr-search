from pydantic import BaseModel
from .department import Department
from .position import Position
from .location import Location
from .status import Status


# Schema for Employee
class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    contact_info: str


class EmployeeCreate(EmployeeBase):
    department_id: int
    position_id: int
    location_id: int
    status_id: int


class Employee(EmployeeBase):
    id: int
    department: Department
    position: Position
    location: Location
    status: Status

    class Config:
        orm_mode = True
