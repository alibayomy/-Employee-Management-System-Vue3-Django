from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Department
from company.models import Company
from .serializers import DepartmentSerializer


#This file contains the end points for Departments application

@api_view(['GET'])
# @permission_classes([IsAuthenticated],)
def get_all_departments(request):
    """
    Return: all the departments
        from the data base as RESTFUL response"""
    departments = Department.objects.all()
    departments_serilaizer = DepartmentSerializer(departments, many=True)
    return Response(departments_serilaizer.data, 
                    status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
# @permission_classes(IsAuthenticated)
def get_companies_department(request, id):
    """Given the company id
    return: all the deparetment in the Company"""
    try:
        company = Company.objects.get(id=id)
        departments = Department.objects.filter(company=company)
        departments_serilaizer = DepartmentSerializer(departments, many=True)
        return Response(departments_serilaizer.data,
                    status=status.HTTP_202_ACCEPTED)
    except Company.DoesNotExist:
        return Response(
            {'details':'Company not found'}
        , status=status.HTTP_404_NOT_FOUND)