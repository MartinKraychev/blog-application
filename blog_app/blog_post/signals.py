from django.db import models
from django.dispatch import receiver

from blog_app.blog_post.models import Post
from blog_app.main.util import delete_file


@receiver(models.signals.post_delete, sender=Post)
def delete_post_image(sender, instance, *args, **kwargs):
    """ Deletes image files on `post_delete` """
    if instance.image:
        delete_file(instance.image.path)
