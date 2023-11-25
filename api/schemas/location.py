from pydantic import BaseModel


# Schema for Location
class LocationBase(BaseModel):
    name: str


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True
