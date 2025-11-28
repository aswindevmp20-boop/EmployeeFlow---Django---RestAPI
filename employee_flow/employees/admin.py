from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, Department, Workflow

@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    list_display = ('username', 'email', 'department', 'role', 'status', 'is_staff')

admin.site.register(Department)
admin.site.register(Workflow)