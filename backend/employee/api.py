from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

#This file contains all the end point for the employee app


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_employees(request):
    """
    End point that
    returns: all the employees for the database"""
    employees = Employee.objects.all()
    employees_serialziers = EmployeeSerializer(employees, many=True)
    return Response(employees_serialziers.data,
                    status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_employee_by_id(request, id):
    """End point for 
    return: the matched employee by id with 202 if success
        else not found msg with 404"""
    try:
        employee = Employee.objects.get(id=id)
        employee_serializer = EmployeeSerializer(employee)
        return Response(employee_serializer.data,
               status=status.HTTP_202_ACCEPTED)
    except Employee.DoesNotExist:
        return Response({
            'details': 'Employee not found'
        }, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
# @permission_classes(IsAuthenticated)
def post_new_employee(request):
    """
    Add a new employee,
    return: On succes , success message and status 201
            on faliure, failure message and status 400"""
    #if authorized to :
    data = request.data
    employee_serializer = EmployeeSerializer(data=data)
    if employee_serializer.is_valid():
        employee_serializer.save()
        return Response({
            'details': 'New employee has been added successfully'
        }, status=status.HTTP_201_CREATED)
    #failuer
    return Response(employee_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
# @permission_classes(IsAuthenticated)
def update_employee(request, id):
    """
    Update an employee data
    return On succes, updating success message, status=200"""
    try:
        employee = Employee.objects.get(id=id)
        data = request.data
        employee_serializer = EmployeeSerializer(instance=employee, data=data, partial=True)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return Response({
            'details': 'New employee has been updated successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(employee_serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
        
    except Employee.DoesNotExist:
        return Response({
            'details': 'Employee not found'
            }, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
# @permission_classes(IsAuthenticated)
def delete_employee(request, id):
    """
    Update an employee data
    return On succes, updating success message, status=200"""
    try:
        employee = Employee.objects.get(id=id)
        employee.delete()
        return Response({
            'details': 'Employee deleted successfully'
            }, status=status.HTTP_204_NO_CONTENT)
    except Employee.DoesNotExist:
        return Response({
            'details': 'Employee not found'
            }, status=status.HTTP_404_NOT_FOUND)
        

        
