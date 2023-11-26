from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from databases import Base


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    contact_info = Column(String, unique=True, index=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    position_id = Column(Integer, ForeignKey("positions.id"))
    location_id = Column(Integer, ForeignKey("locations.id"))
    status_id = Column(Integer, ForeignKey("statuses.id"))
    department = relationship("Department", back_populates="employees")
    position = relationship("Position", back_populates="employees")
    location = relationship("Location", back_populates="employees")
    status = relationship("Status", back_populates="employees")
