from datetime import date, timedelta
from core.celery import app
from django.core.mail import send_mail
from core.settings import EMAIL_HOST_USER
from tasks.models import Tasks
from accounts.models import CustomUser


@app.task
def send_email_everyday_8am():
    users = CustomUser.objects.all()
    for user in users:
        user_tasks = Tasks.objects.filter(author=user.id, deadline_date=date.today() + timedelta(days=1)).values()
        if len(user_tasks) != 0:
            tasks_to_send = []
            for user_task in user_tasks:
                if user_task['status'] != 'finished':
                    tasks_to_send.append(user_task['title'])
            send_mail(
                subject='Щоденне сповіщення',
                message=f"Завтра дедлайн по задачам: {', '.join(tasks_to_send)}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
                )
