from django.urls import path
from .views import all_tasks, CreateTaskFormView


urlpatterns = [
    path('', all_tasks, name="all_tasks"),
    path('tasks/create/', CreateTaskFormView.as_view(), name="create_task")
]
