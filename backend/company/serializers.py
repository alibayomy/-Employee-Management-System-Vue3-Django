from rest_framework import serializers
from department.models import Department
from employee.models import Employee
from .models import Company

# Create your views here.

class CompanySerializer(serializers.ModelSerializer):
    """Company model attributes
        Serializer"""
    departments_count = serializers.SerializerMethodField()
    employees_count = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = "__all__"

    def get_departments_count(self, obj):
        """Aggregation calculation
            to the number of departments 
            in a company"""
        departments = Department.objects.filter(company=obj).count()
        return departments

    def get_employees_count(self, obj):
       
       """Aggregation calculation
            to the number of employees 
            in a company"""
       employees = Employee.objects.filter(company=obj).count()
       return employees
       
    