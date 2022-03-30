from django.db import models


class Category(models.Model):
    CATEGORIES_NAME_MAX_LENGTH = 50

    name = models.CharField(
        max_length=CATEGORIES_NAME_MAX_LENGTH,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.name}'
