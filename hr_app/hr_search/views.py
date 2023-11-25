import os
import json
from dotenv import load_dotenv
from django.http import HttpResponse
from django.shortcuts import render


load_dotenv()
API_KEY_NAME = os.getenv("API_KEY_NAME")
API_KEY = os.getenv("API_KEY")

import requests


def employee_list(request):
    BASE_URL = "http://localhost:8001/"

    # Fetch data from FastAPI endpoints
    statuses = fetch_data_from_api(BASE_URL + "statuses")
    locations = fetch_data_from_api(BASE_URL + "locations")
    companies = fetch_data_from_api(
        BASE_URL + "companies/"
    )
    positions = fetch_data_from_api(BASE_URL + "positions/")
    departments = fetch_data_from_api(BASE_URL + "departments/")

    # display_columns = get_organization_display_columns()

    context = {
        # "display_columns": display_columns,
        "employees": [],
        "statuses": statuses,
        "locations": locations,
        "companies": companies,
        "positions": positions,
        "departments": departments,
    }

    return render(request, "employees.html", context)


def fetch_data_from_api(api_url):
    headers = {
        "Content-Type": "application/json",
        API_KEY_NAME:API_KEY, 
    }
    response = requests.get(api_url,headers=headers  )
    if response.status_code == 200:
        return response.json()
    else:
        # Handle error response
        return []



