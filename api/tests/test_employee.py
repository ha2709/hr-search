import os
import json
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from main import app
 
from routers.employee import search_employees


load_dotenv()
API_KEY_NAME = os.getenv("API_KEY_NAME")
API_KEY = os.getenv("API_KEY")
headers = {
    "Content-Type": "application/json",
    API_KEY_NAME: API_KEY,
}
client = TestClient(app)


# Test function
def test_search_employees():
    # Test case 1: Without query parameters
    response = client.get("/v1/search", headers=headers)
    # print(34, response)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    # Test case 2: With query parameters
    response = client.get(
        "/v1/search?status=Active&location=office1&company=company_1&department=hr&position=manager",
        headers=headers,
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    # Test case 3: With query array of status
    response = client.get(
        "/v1/search?status=Active, Terminated&location=office1&company=company_1&department=hr&position=manager",
        headers=headers,
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    # Add more test cases as needed

    # Clean up any changes made to the database or other resources
