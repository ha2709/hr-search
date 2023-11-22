from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine
from schemas import EmployeeCreate


app = FastAPI()
# Create the database tables
models.Base.metadata.create_all(bind=engine)

 

@app.post("/employees/")
def create_employee(employee: EmployeeCreate):
    db = SessionLocal()
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    db.close()
    return db_employee

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
