from django.contrib import admin
from .models import Tasks
from accounts.models import CustomUser


class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ['title']
    list_filter = ['author_id']

    class Meta:
        model = Tasks


admin.site.register(Tasks, TasksAdmin)
