from sqlalchemy import Column, Integer, String
from .database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    contact_info = Column(String, unique=True, index=True)
    department = Column(String, index=True)
    position = Column(String, index=True)
    location = Column(String, index=True)
    status = Column(String, index=True)
