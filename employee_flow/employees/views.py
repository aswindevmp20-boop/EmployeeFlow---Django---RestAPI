from rest_framework import viewsets, permissions
from .models import Employee, Department, Workflow
from .serializers import EmployeeSerializer, DepartmentSerializer, WorkflowSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAdminUser]


class WorkflowViewSet(viewsets.ModelViewSet):
    queryset = Workflow.objects.all().order_by('-created_at')
    serializer_class = WorkflowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user)
