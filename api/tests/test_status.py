import os
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from main import app


load_dotenv()
API_KEY_NAME = os.getenv("API_KEY_NAME")
API_KEY = os.getenv("API_KEY")
headers = {
    "Content-Type": "application/json",
    API_KEY_NAME: API_KEY,
}
client = TestClient(app)

# Test function for /statuses endpoint
def test_get_statuses():
    response = client.get("/v1/statuses", headers=headers)
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
 
