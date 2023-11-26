import os
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from main import app
from routers.company import get_company_list, get_company_info

load_dotenv()
API_KEY_NAME = os.getenv("API_KEY_NAME")
API_KEY = os.getenv("API_KEY")
headers = {
    "Content-Type": "application/json",
    API_KEY_NAME: API_KEY,
}
client = TestClient(app)

# Test function for /companies endpoint
def test_get_company_list():
 

    response = client.get("/v1/companies", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
     
# Test function for /companies/{company_name} endpoint
def test_get_company_info():
  

    response = client.get("/v1/companies/company_1", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
