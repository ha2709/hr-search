from django.urls import path

from . import views

urlpatterns = [
    path("", views.search_employee, name="search_employee"),
]
