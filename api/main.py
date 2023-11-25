from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from .routers.department import department_router
from .routers.employee import employee_router
from .routers.location import location_router
from .routers.position import position_router
from .routers.status import status_router
from .routers.company import company_router

app = FastAPI()
# Allow all origins in CORS to handle requests from different domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Endpoint to get a list of all employees
app.include_router(employee_router, tags=["employees"])
# app.include_router(department_router, prefix="/api")
app.include_router(department_router, tags=["deparment"])
app.include_router(employee_router, tags=["employees"])
app.include_router(location_router, tags=["locations"])
app.include_router(position_router, tags=["positions"])
app.include_router(status_router, tags=["statuses"])
app.include_router(company_router, tags=["company"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
