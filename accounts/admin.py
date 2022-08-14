from django.contrib import admin
from tasks.models import Tasks
from .models import CustomUser
from .forms import UserCreateForm


class TaskInline(admin.TabularInline):
    model = Tasks
    fields = ('title', 'brief_description')
    readonly_fields = ('brief_description', 'title')
    extra = 0

    def brief_description(self, obj):
        if obj.id != None:
            task_description = Tasks.objects.filter(id=obj.id).values('description')[0]['description']
            brief_description = task_description[0:50]
            print(task_description)
            return f'{brief_description}...'

    brief_description.short_description = "Короткий опис"


class UsersAdmin(admin.ModelAdmin):
    inlines = (TaskInline,)
    list_display = ('first_name', 'last_name', 'profession', 'email', 'tasks_cont')
    readonly_fields = ('tasks_cont',)
    fields = ('first_name', 'last_name', 'email', 'profession', 'tasks_cont')
    search_fields = ['first_name', 'last_name']
    add_form_template = 'admin/add_user_form.html'

    def add_view(self, request, form_url="", extra_context=None):
        form = UserCreateForm
        extra_context = {'form': form}
        return super(UsersAdmin, self).add_view(request, form_url=form_url, extra_context=extra_context)

    def tasks_cont(self, obj):
        user = CustomUser.objects.get(email=obj)
        user_id = user.id
        tasks = Tasks.objects.filter(author_id=user_id)
        count_tasks = len(tasks)
        return count_tasks

    tasks_cont.short_description = "Кількість створених задач"


admin.site.register(CustomUser, UsersAdmin)



