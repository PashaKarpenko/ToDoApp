import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send_email_every_day': {
        'task': 'tasks.tasks.send_email_everyday_8am',
        'schedule': crontab(minute=0, hour=8)
    },
}
