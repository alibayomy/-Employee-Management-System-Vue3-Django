from django.db import models

# Create your models here.
from company.models import Company

class Department(models.Model):
    """Department table with att
    name: str
    Company: one to many 
    employee: many realtionship"""
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f'{self.name} in {self.company}'
    class Meta:
        """Assgining a composite PK"""
        constraints = [
            models.UniqueConstraint(fields=['name', 'company'], name='company_department')
        ]