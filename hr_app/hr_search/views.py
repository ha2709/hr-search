from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Employee


# def index(request):



def employee_list(request):
    employees = Employee.objects.all()
    template = loader.get_template('employees.html')
    return HttpResponse(template.render())
    # return render(request, 'employees.html', {'employees': employees})