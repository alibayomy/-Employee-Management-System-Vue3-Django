from django.urls import path
from .api import *




urlpatterns = [
    path('all/', get_all_companies),
    path('get-<int:id>/', get_company_by_id)
]