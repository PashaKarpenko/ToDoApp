# Generated by Django 4.0.6 on 2022-07-30 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='importance',
            field=models.BooleanField(),
        ),
    ]
