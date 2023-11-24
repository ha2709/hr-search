 
from fastapi import FastAPI  
import uvicorn
from .routers.employee import router as employee_router


app = FastAPI()
# Endpoint to get a list of all employees
app.include_router(employee_router,  tags=["employees"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

if __name__ == "__main__":
    

    uvicorn.run(app, host="127.0.0.1", port=8001)
