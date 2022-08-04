from django.contrib.auth import get_user_model, get_user
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.views.generic import DetailView

from .models import Tasks
from .forms import TaskCreateForm
from django.urls import reverse

User = get_user_model()


class TasksView(View):
    def get(self, request):
        tasks = Tasks.objects.filter(author_id=request.user.id).all()
        paginator = Paginator(tasks, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'page_obj': page_obj}
        return render(request, 'tasks/all_tasks.html', context=context)


class CreateTaskView(View):
    def post(self, request):
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            create_form = form.save(commit=False)
            create_form.author = request.user
            create_form.save()
        return redirect(reverse('all_tasks'))

    def get(self, request):
        context = {'create_task_form': TaskCreateForm}
        return render(request, 'tasks/create_task.html', context=context)


class TaskDetailView(View):
    def get(self, request, pk):
        task = get_object_or_404(Tasks, id=pk)
        context = {'task': task}
        return render(request, 'tasks/task_detail.html', context=context)


class StatisticsView(View):
    def get(self, request):
        user_id = request.user.id
        tasks_count = Tasks.objects.filter(author_id=user_id).count()
        todo_task_count = Tasks.objects.filter(status='todo').count()
        in_progress_task_count = Tasks.objects.filter(status='in_progress').count()
        blocked_task_count = Tasks.objects.filter(status='blocked').count()
        finished_task_count = Tasks.objects.filter(status='finished').count()

        context = {
            'tasks_count': tasks_count, 'todo_task_count': todo_task_count,
            'in_progress_task_count': in_progress_task_count,
            'blocked_task_count': blocked_task_count,
            'finished_task_count': finished_task_count,
        }
        return render(request, 'tasks/statistics.html', context=context)
