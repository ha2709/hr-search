from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
import pytest
from main import app


client = TestClient(app)


# Mocked database session for testing
@pytest.fixture
def test_db_session():
    from app import databases

    db = databases.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Test case for the search endpoint
def test_search_employees(test_db_session):
    # Insert test data into the database using the test_db_session

    # Example: Insert a test employee
    # employee = Employee(first_name="John", last_name="Doe", contact_info="john@example.com")
    # test_db_session.add(employee)
    # test_db_session.commit()

    # Perform a test request to the API endpoint
    response = client.get(
        "/search/?status=Active", headers={"Authorization": "Bearer your_test_token"}
    )

    # Assert the response status code and content as needed
    assert response.status_code == 200
