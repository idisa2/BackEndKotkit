# Generated by Django 3.2.8 on 2022-08-16 10:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_country_flag_emoji'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
