# schemas.py

from pydantic import BaseModel

# Schema for Department
class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    class Config:
        orm_mode = True

# Schema for Position
class PositionBase(BaseModel):
    title: str

class PositionCreate(PositionBase):
    pass

class Position(PositionBase):
    id: int
    class Config:
        orm_mode = True

# Schema for Location
class LocationBase(BaseModel):
    name: str

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int
    class Config:
        orm_mode = True

# Schema for Status
class StatusBase(BaseModel):
    name: str

class StatusCreate(StatusBase):
    pass

class Status(StatusBase):
    id: int
    class Config:
        orm_mode = True

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
