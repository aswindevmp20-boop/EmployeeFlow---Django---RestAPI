from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet, WorkflowViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'workflows', WorkflowViewSet)

urlpatterns = router.urls
