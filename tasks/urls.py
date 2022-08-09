from django.urls import path
from .views import CreateTaskView, TasksListView, TaskDetailView, StatisticsView

urlpatterns = [
    path('', TasksListView.as_view(), name="all_tasks"),
    path('tasks/create/', CreateTaskView.as_view(), name="create_task"),
    path('tasks/task_detail/<int:pk>/', TaskDetailView.as_view(), name="task_detail"),
    path('tasks/statistics/', StatisticsView.as_view(), name="statistics"),
]
