# Generated by Django 3.2.8 on 2022-08-16 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_customuser_fcm_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='fcm_token',
        ),
    ]
