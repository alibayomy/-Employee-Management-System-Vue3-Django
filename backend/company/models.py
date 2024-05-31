from django.db import models

# Create your models here.


class Company(models.Model):
    """Company table with attri
        name: str
        """
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'