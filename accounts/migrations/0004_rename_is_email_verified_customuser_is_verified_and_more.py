# Generated by Django 4.0.6 on 2022-08-02 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_is_aproove_customuser_is_email_verified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_email_verified',
            new_name='is_verified',
        ),
        migrations.AddField(
            model_name='customuser',
            name='token',
            field=models.CharField(default='None', max_length=100),
        ),
    ]