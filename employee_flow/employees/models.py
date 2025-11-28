from django.db import models
from django.contrib.auth.models import AbstractUser

# Defines the Database schema (ORM)
class Employee(AbstractUser):
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return f"{self.username} ({self.department})"


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(blank=True)

    def __str__(self):
        return self.name

class Workflow(models.Model):
    STATUS_CHOICE = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
    ]

    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name = 'workflows')
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[self.title] - {self.status}"