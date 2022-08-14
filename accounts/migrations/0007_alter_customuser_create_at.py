# Generated by Django 4.0.6 on 2022-08-11 07:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
