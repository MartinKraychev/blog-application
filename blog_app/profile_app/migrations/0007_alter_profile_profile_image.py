import blog_app.profile_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0006_alter_profile_facebook_alter_profile_github_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(upload_to='profiles', validators=[blog_app.profile_app.validators.MaxFileSizeInMbValidator(5)], verbose_name=''),
        ),
    ]
