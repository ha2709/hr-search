import os
import json
from dotenv import load_dotenv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

load_dotenv()
API_KEY_NAME = os.getenv("API_KEY_NAME")
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
 
@login_required
def search_employee(request):
    # Fetch data from FastAPI endpoints
    statuses = fetch_data_from_api(API_URL + "statuses")
    locations = fetch_data_from_api(API_URL + "locations")
    companies = fetch_data_from_api(API_URL + "companies/")
    positions = fetch_data_from_api(API_URL + "positions/")
    departments = fetch_data_from_api(API_URL + "departments/")

    context = {
        # "employees": [],
        "api_url": API_URL,
        "api_key":API_KEY,
        "api_key_name": API_KEY_NAME,
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
        API_KEY_NAME: API_KEY,
    }
  
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle error response
        return []
