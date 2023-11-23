from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Employee
import requests

 



def employee_list(request):
    api_url = 'http://localhost:8001/employees'   

    try:
        # Make an HTTP GET request to the API endpoint
        response = requests.get(api_url)
        print(17, response)
        # Check if the API call was successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse the JSON response to get the employee data
            employees = response.json()
        else:
            # Handle the API call error  
            error_message = f"API call failed with status code: {response.status_code}"
            return render(request, 'error_template.html', {'error_message': error_message})

    except requests.exceptions.RequestException as e:
        # Handle any network or request-related errors here
        error_message = f"API request failed with error: {str(e)}"
        return render(request, 'error_template.html', {'error_message': error_message})

     
    display_columns = get_organization_display_columns() 
 
    context = {
        'display_columns': display_columns,
        'employees': employees,
    }
 
    return render(request, 'employees.html',context)

def get_organization_display_columns():
    # fetch the configuration for the current organization
    # This can involve querying  database or any other data source.
    # Return a list of column names based on the organization's preference.
    # For example, ["contact", "department", "position"]
    return ["contact", "department", "position"]