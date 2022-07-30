from django.shortcuts import render
from .models import Tasks
from .forms import TaskCreateForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


def all_tasks(request):
    tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/all_tasks.html', context=context)


class CreateTaskFormView(CreateView):
    form_class = TaskCreateForm
    model = Tasks
    success_url = reverse_lazy("all_tasks")
    template_name = "tasks/create_task.html"
