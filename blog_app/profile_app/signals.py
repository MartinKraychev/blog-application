from django.db import models
from django.dispatch import receiver

from blog_app.main.util import delete_file
from blog_app.profile_app.models import Profile


@receiver(models.signals.post_delete, sender=Profile)
def delete_profile_picture(sender, instance, *args, **kwargs):
    """ Deletes image files on `post_delete` """
    if instance.profile_image:
        delete_file(instance.profile_image.path)

