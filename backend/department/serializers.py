from rest_framework import serializers
from employee.models import Employee
from .models import Department
# Create your views here.

class DepartmentSerializer(serializers.ModelSerializer):
    """
    Depratment table TO convert data types
        to RESTFUL API
    """
    employees_count = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = '__all__'

    def get_employees_count(self, obj):
        """Aggregeation caluc for
        The numb of employees working in
        the department"""

        employees = Employee.objects.filter(department=obj).count()
        return employees