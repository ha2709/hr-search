from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    contact_info: str
    department: str
    position: str
    location: str
    status: str
