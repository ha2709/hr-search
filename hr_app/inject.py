import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()

from employee_app.models import Employee

# data = [
#     {
#         "first_name": "John",
#         "last_name": "Doe",
#         "contact_info": "john@example.com",
#         "department": "HR",
#         "position": "Manager",
#         "location": "New York",
#         "status": "Active",
#     },
#     {
#         "first_name": "Jane",
#         "last_name": "Smith",
#         "contact_info": "jane@example.com",
#         "department": "Sales",
#         "position": "Sales Representative",
#         "location": "Los Angeles",
#         "status": "Active",
#     },
#     {
#         "first_name": "Alice",
#         "last_name": "Johnson",
#         "contact_info": "alice@example.com",
#         "department": "IT",
#         "position": "Software Engineer",
#         "location": "San Francisco",
#         "status": "Inactive",
#     },
#       {"first_name": "OO5Test", "last_name": "005", "contact_info": "email@example.com", "department": "asd", "position": "Assistant Manager", "location": "Singapore", "status": "ACTIVE"},


# ]


# Inject the data into the database
for entry in data:
    employee, created = Employee.objects.get_or_create(
        first_name=entry["first_name"],
        last_name=entry["last_name"],
        defaults=entry,  # This will set all other fields on creation
    )
    if not created:
        # Update the existing employee if necessary
        for key, value in entry.items():
            setattr(employee, key, value)
        employee.save()

print("Data injection complete.")
