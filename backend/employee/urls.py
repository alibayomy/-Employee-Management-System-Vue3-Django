from django.urls import path
from .api import *




urlpatterns = [
    path('all/', get_all_employees),
    path('add-employee/', post_new_employee),
    path('get-<int:id>/', get_employee_by_id),
    path('update-<int:id>/', update_employee),
    path('delete-<int:id>/', delete_employee)
]