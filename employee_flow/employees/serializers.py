from rest_framework import serializers
from .models import Employee

# JSON Payloads are validated and shaped Here
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id', 'username', 'email',
            'first_name', 'last_name',
            'department', 'role', 'status'
        ]