# Generated by Django 4.0.6 on 2022-08-03 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_tasks_options_alter_tasks_deadline_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(default='todo', max_length=20, null=True, verbose_name='Статус'),
        ),
    ]