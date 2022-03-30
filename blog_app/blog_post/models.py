from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from django.db import models

from blog_app.blog_category.models import Category
from blog_app.profile_app.validators import MaxFileSizeInMbValidator

UserModel = get_user_model()


class Post(models.Model):
    IMAGE_MAX_FILE_SIZE_MB = 5
    HEADING_MAX_LENGTH = 50

    IMAGES_UPLOAD_TO = 'post_image'

    heading = models.CharField(
        max_length=HEADING_MAX_LENGTH,
    )

    text = models.TextField()

    image = models.ImageField(
        upload_to=IMAGES_UPLOAD_TO,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_FILE_SIZE_MB),
        ),
    )

    created_on = models.DateField(
        auto_now_add=True,
    )

    updated_on = models.DateField(
        auto_now=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Comment(models.Model):

    message = models.TextField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
