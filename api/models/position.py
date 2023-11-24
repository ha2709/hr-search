from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..databases import Base


class Position(Base):
    __tablename__ = "positions"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    employees = relationship("Employee", back_populates="position")