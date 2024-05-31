from django.urls import path
from .api import *




urlpatterns = [
    path('all/', get_all_departments),
    path('company-<int:id>/', get_companies_department)
]