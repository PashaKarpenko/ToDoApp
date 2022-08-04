from rest_framework import routers
from tasks.api_v1_views import TaskViewSet

router = routers.SimpleRouter()
router.register('', TaskViewSet, basename='tasks')
