import datetime
from rest_framework.response import Response
from tasks.models import Tasks
from tasks.serializers import TaskSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.contrib.auth import get_user_model


User = get_user_model()


class TaskViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status']
    search_fields = ['title']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(Tasks.objects.filter(author_id=request.user.id).all())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(**{'author': self.request.user})

    @action(methods=['post'], detail=True)
    def mark_as_importance(self, request, pk=None):
        task = self.get_object()
        if task.importance == False:
            task.importance = True
            task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def mark_as_in_progress(self, request, pk=None):
        task = self.get_object()
        if task.status == 'todo':
            task.status = 'in_progress'
            task.in_progress_task = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def mark_as_blocked(self, request, pk=None):
        task = self.get_object()
        if task.status == 'in_progress':
            task.status = 'blocked'
            task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def mark_as_in_progress_after_blocked(self, request, pk=None):
        task = self.get_object()
        if task.status == 'blocked':
            task.status = 'in_progress'
            task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def mark_as_finished(self, request, pk=None):
        task = self.get_object()
        if task.status == 'in_progress':
            task.status = 'finished'
            task.finished_task = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

