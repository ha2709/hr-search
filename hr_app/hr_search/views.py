from django.http import HttpResponse
from django.shortcuts import render


import requests


def employee_list(request):
    BASE_URL = "http://localhost:8001/"
 

 
    # Fetch data from FastAPI endpoints
    statuses = fetch_data_from_api(BASE_URL + "statuses")
    locations = fetch_data_from_api(BASE_URL + "locations")
    companies = fetch_data_from_api(BASE_URL + "companies/")  # Adjust the endpoint based on your API
    positions = fetch_data_from_api(BASE_URL + "positions/")
    departments = fetch_data_from_api(BASE_URL + "departments/")

    # Your existing code to get display_columns
    display_columns = get_organization_display_columns()

    context = {
        "display_columns": display_columns,
        "employees": [],
        "statuses": statuses,
        "locations": locations,
        "companies": companies,
        "positions": positions,
        "departments": departments,
    }

    return render(request, "employees.html", context)

def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle error response
        return []
    
def get_organization_display_columns():
    # fetch the configuration for the current organization
    # This can involve querying  database or any other data source.
    # Return a list of column names based on the organization's preference.
    # For example, ["contact", "department", "position"]
    return ["contact", "department", "position"]
