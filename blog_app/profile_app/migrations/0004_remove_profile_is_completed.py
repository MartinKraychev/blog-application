# Generated by Django 4.0.3 on 2022-03-06 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0003_alter_profile_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_completed',
        ),
    ]
