from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        file_size = value.file.size
        if file_size > self.max_size * 1024 * 1024:
            raise ValidationError(f'Max file size is {self.max_size} MB')
