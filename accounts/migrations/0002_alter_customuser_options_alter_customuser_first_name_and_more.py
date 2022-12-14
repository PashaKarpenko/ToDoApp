# Generated by Django 4.0.6 on 2022-08-01 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Обліковий запис', 'verbose_name_plural': 'Облікові записи'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Прізвище'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profession',
            field=models.CharField(max_length=100, verbose_name='Професія'),
        ),
    ]
