from rest_framework import serializers
from .models import Employee, Department, Workflow

# JSON Payloads are validated and shaped Here
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id', 'username', 'email',
            'first_name', 'last_name',
            'department', 'role', 'status'
        ]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description']

class WorkflowSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Workflow
        fields = ['id', 'employee', 'department', 'title', 'description', 'status', 'created_at']