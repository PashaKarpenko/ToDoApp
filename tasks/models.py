from django.conf import settings
from django.db import models


STATUS = [('todo', 'todo'), ('in_progress', 'in_progress'), ('blocked', 'blocked'), ('finished', 'finished')]
PRIORITY = [('low', 'low'), ('medium', 'medium'), ('high', 'high')]


class Tasks(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100, verbose_name='Назва задачі')
    description = models.CharField(max_length=350, verbose_name='Опис задачі')
    deadline_date = models.CharField(max_length=10, verbose_name='Дата дедлайну')
    status = models.CharField(choices=STATUS, max_length=20, default='todo', verbose_name='Статус')
    priority = models.CharField(choices=PRIORITY, max_length=10, default='medium', verbose_name='Пріоритет')
    importance = models.BooleanField(verbose_name='Важливість', default=False)
    in_progress_task = models.CharField(max_length=30, null=True)
    finished_task = models.CharField(max_length=30, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачі'
        ordering = ['-importance', 'deadline_date']


