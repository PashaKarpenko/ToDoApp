from django.conf import settings
from django.db import models


class Tasks(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    deadline_date = models.CharField(max_length=10)
    status = models.CharField(max_length=20, null=True, blank=True)
    priority = models.CharField(max_length=10, default='')
    importance = models.CharField(max_length=10, default='')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title},  {self.description}'

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
