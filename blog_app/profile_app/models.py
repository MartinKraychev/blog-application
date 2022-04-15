from django.contrib.auth import get_user_model
from django.db import models

from cloudinary.models import CloudinaryField

from blog_app.profile_app.validators import validate_letters_only

UserModel = get_user_model()


class Profile(models.Model):

    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MAX_LENGTH = 20

    FACEBOOK_VERBOSE_NAME = 'Facebook Link'
    LINKEDIN_VERBOSE_NAME = 'LinkedIn Link'
    GITHUB_VERBOSE_NAME = 'Github Link'
    TWITTER_VERBOSE_NAME = 'Twitter Link'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            validate_letters_only,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            validate_letters_only,
                    ),
    )

    age = models.PositiveIntegerField()

    description = models.TextField()

    profile_image = CloudinaryField('image')

    facebook = models.URLField(
        verbose_name=FACEBOOK_VERBOSE_NAME,
        null=True,
        blank=True,
    )

    linkedin = models.URLField(
        verbose_name=LINKEDIN_VERBOSE_NAME,
        null=True,
        blank=True,
    )

    github = models.URLField(
        verbose_name=GITHUB_VERBOSE_NAME,
        null=True,
        blank=True,
    )

    twitter = models.URLField(
        verbose_name=TWITTER_VERBOSE_NAME,
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.get_full_name()}'
