from django.db import models
from django.contrib.auth.models import AbstractUser

# Defines the Database schema (ORM)
class Employee(AbstractUser):
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return f"{self.username} ({self.department})"