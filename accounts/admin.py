from itertools import count

from django.contrib import admin

from tasks.models import Tasks
from .models import CustomUser


user = CustomUser


class TaskInline(admin.TabularInline):
    model = Tasks
    fields = ('title', 'brief_description')
    readonly_fields = ('brief_description', 'title')
    extra = 0

    def brief_description(self, obj):
        task = Tasks.objects.get(description=obj)
        desk = str(task.description)
        brief_description = desk[0:50]
        return f'{brief_description}...'

    brief_description.short_description = "Короткий опис"


class UsersAdmin(admin.ModelAdmin):
    inlines = (TaskInline,)
    list_display = ('first_name', 'last_name', 'profession', 'email', 'tasks_cont',)
    readonly_fields = ('first_name', 'last_name', 'email', 'tasks_cont',)
    fields = ('first_name', 'last_name', 'email', 'tasks_cont',)
    search_fields = ['first_name', 'last_name']

    def tasks_cont(self, obj):
        user = CustomUser.objects.get(email=obj)
        user_id = user.id
        tasks = Tasks.objects.filter(author_id=user_id)
        count_tasks = len(tasks)
        return count_tasks

    tasks_cont.short_description = "Кількість створених задач"

admin.site.register(CustomUser, UsersAdmin)
