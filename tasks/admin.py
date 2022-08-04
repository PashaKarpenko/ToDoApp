from django.contrib import admin
from .models import Tasks
from accounts.models import CustomUser


class UserInline(admin.TabularInline):
    model = CustomUser


class TasksAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'author', 'status']
    list_display = ('title', 'brief_description', 'first_name', 'last_name')
    search_fields = ['title']
    list_filter = ['author_id']
    readonly_fields = ['author', 'brief_description']

    def first_name(self, obj):
        task = Tasks.objects.filter(description=obj)

        user = task
        print(task)
        #user = CustomUser.objects.get(email=obj)
        return task

    first_name.short_description = "Ім'я Автора"

    def last_name(self, obj):
        user = CustomUser.objects.get(email=obj)
        return user.last_name

    last_name.short_description = "Прізвище Автора"

    def brief_description(self, obj):
        task = Tasks.objects.get(description=obj)
        desk = str(task.description)
        brief_description = desk[0:50]
        return f'{brief_description}...'

    brief_description.short_description = "Короткий опис"


admin.site.register(Tasks, TasksAdmin)
