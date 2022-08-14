from accounts.models import CustomUser
from accounts.serializers import EditUserSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin


class EditUserViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = EditUserSerializer
    permission_classes = [IsAuthenticated]

