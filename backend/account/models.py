from typing import Any, Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator

# Create your models here.


class CustomUser(AbstractUser):
    """main user class in with attributes
    Name:
    email:
    username:
    password:
    Role"""
    email = models.EmailField(unique=True,
                              validators=[
                                  EmailValidator
                              ])
    username = models.CharField(max_length=50, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    

    def __str__(self) -> str:
        return f'{self.email}'