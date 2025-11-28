from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import Department, Workflow

Employee = get_user_model()

class EmployeeFlowTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = Employee.objects.create_superuser(
            username='admin', email='admin@example.com', password='admin123'
        )
        self.client.force_authenticate(user=self.admin_user)
        self.department = Department.objects.create(name='Engineering')

    def test_create_department(self):
        response = self.client.post('/api/departments/', {
            'name': 'HR',
            'description': 'Human Resources'
        }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'HR')

    def test_create_workflow(self):
        response = self.client.post('/api/workflows/', {
            'department': self.department.id,
            'title': 'Onboarding',
            'description': 'New employee onboarding'
        }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], 'Onboarding')
