from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from .routers.employee import router as employee_router


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


@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
