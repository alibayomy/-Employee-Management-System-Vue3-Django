from typing import Iterable
from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.forms import ValidationError
from django.utils import timezone
# Create your models here.

from company.models import Company
from department.models import Department
from account.models import CustomUser

class Employee(models.Model):
    """Employee table with attr:
    name: str
    email: email str with validation
    mobile_number: validate against egyptian phone numbers only
    address: str"""

    EMPLOYEE_STATUS=(
        ('application_received', 'Application Received'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('hired', 'Hired'),
        ('not_accepted', 'Not Accepted')
    )
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True, 
                              validators=[
                                  EmailValidator
                              ])
    mobile_number = models.CharField( max_length=12,unique=True,
                                    validators = [
                                        RegexValidator(
                                            regex = r"^(?:\+?2)?01[0125][0-9]{8}$",
                                            message='Invalid egyptian mobile number format',
                                            code = 'invalid'
                                        )
                                    ])
    address = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=EMPLOYEE_STATUS, default='application_received')
    title = models.CharField(max_length=50)
    hired_on = models.DateTimeField(null=True, blank=True)
    created_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        """String represntation of the 
        Employee class with his name"""
        return f'{self.name}'
    
    def save(self, *args, **kwargs) -> None:
        """Automatically set the hired date
        only if self.STATUS = hired"""
        if self.status == 'hired' and self.hired_on is None:
            self.hired_on = timezone.now()
        super().save(*args, **kwargs)

    def clean(self) -> None:
        if self.department.company != self.company:
            raise ValidationError('The selected department doesnt exist')
        