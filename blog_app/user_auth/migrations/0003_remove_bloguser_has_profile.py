# Generated by Django 4.0.3 on 2022-03-26 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_bloguser_has_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloguser',
            name='has_profile',
        ),
    ]
