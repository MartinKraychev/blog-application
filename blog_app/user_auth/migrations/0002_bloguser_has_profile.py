# Generated by Django 4.0.3 on 2022-03-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='has_profile',
            field=models.BooleanField(default=False),
        ),
    ]
