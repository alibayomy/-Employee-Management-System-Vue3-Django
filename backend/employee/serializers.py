from rest_framework import serializers
from .models import Employee
from django.utils.timezone import now
# Create your views here.

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Employee table TO convert data types
        to RESTFUL API
    """
    days_employed = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__'

    def get_days_employed(self, obj):
        """
        Return: the number of days an employee
            has been employed IF he is hired"""
        if obj.hired_on:
            days_employed = (now() - obj.hired_on).days
            return days_employed
