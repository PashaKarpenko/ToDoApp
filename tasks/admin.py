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
        author_id = Tasks.objects.filter(id=obj.id).values('author')[0]['author']
        first_name = CustomUser.objects.filter(id=author_id).values('first_name')[0]['first_name']
        return first_name

    first_name.short_description = "Ім'я Автора"

    def last_name(self, obj):
        author_id = Tasks.objects.filter(id=obj.id).values('author')[0]['author']
        last_name = CustomUser.objects.filter(id=author_id).values('last_name')[0]['last_name']
        return last_name

    last_name.short_description = "Прізвище Автора"

    def brief_description(self, obj):
        task_description = Tasks.objects.filter(id=obj.id).values('description')[0]['description']
        brief_description = task_description[0:50]
        return f'{brief_description}...'

    brief_description.short_description = "Короткий опис"


admin.site.register(Tasks, TasksAdmin)
