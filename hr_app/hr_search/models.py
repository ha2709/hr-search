 

from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_info = models.EmailField()
    department = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50)  # e.g., 'Active', 'Terminated'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
