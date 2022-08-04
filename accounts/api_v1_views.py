from rest_framework.response import Response

from accounts.models import CustomUser
from accounts.serializers import EditUserSerializer
from tasks.models import Tasks
from tasks.serializers import TaskSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.contrib.auth import get_user_model


class EditUserViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = EditUserSerializer
    permission_classes = [IsAuthenticated]

