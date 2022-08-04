from rest_framework import routers
from accounts.api_v1_views import EditUserViewSet

router = routers.SimpleRouter()
router.register('', EditUserViewSet, basename='edit_user')
