from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from .models import Tasks
from .forms import TaskCreateForm
from django.urls import reverse

User = get_user_model()


class TasksListView(View):
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
        user_tasks = Tasks.objects.filter(author_id=user_id).all()
        tasks_count = user_tasks.count()
        todo_task_count = user_tasks.filter(status='todo').count()
        in_progress_task_count = user_tasks.filter(status='in_progress').count()
        blocked_task_count = user_tasks.filter(status='blocked').count()
        finished_task_count = user_tasks.filter(status='finished').count()
        average_time_spent = self.average_time_spent()

        context = {
            'tasks_count': tasks_count, 'todo_task_count': todo_task_count,
            'in_progress_task_count': in_progress_task_count,
            'blocked_task_count': blocked_task_count,
            'finished_task_count': finished_task_count,
            'average_time_spent': average_time_spent,
        }
        return render(request, 'tasks/statistics.html', context=context)

    def average_time_spent(self):
        user_id = self.request.user.id
        tasks = Tasks.objects.filter(author_id=user_id)
        count = 0
        time_spent = datetime.strptime('0001-01-01 00:00:00', "%Y-%m-%d %H:%M:%S")
        for task in tasks:
            if task.in_progress_task != None and task.finished_task != None:
                time_spent += (datetime.strptime(str(task.finished_task), "%Y-%m-%d %H:%M:%S") - datetime.strptime(
                    str(task.in_progress_task), "%Y-%m-%d %H:%M:%S"))
                count += 1
        average_time_spent_in_seconds = int((time_spent - datetime.strptime('0001-01-01 00:00:00', "%Y-%m-%d %H:%M:%S")).total_seconds() / count)
        average_time_spent = str(timedelta(seconds=average_time_spent_in_seconds))
        return average_time_spent
