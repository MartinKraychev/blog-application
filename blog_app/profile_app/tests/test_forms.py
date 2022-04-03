import tempfile

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from blog_app.profile_app.forms import ProfileCreateForm

UserModel = get_user_model()


class TestMyUserCreationForm(TestCase):

    def setUp(self):
        UserModel.objects.create(username='abv', password='123456')

    def test_form_check_fields(self):
        form = ProfileCreateForm()
        self.assertIn("first_name", form.fields)
        self.assertIn("last_name", form.fields)
        self.assertIn("age", form.fields)
        self.assertIn("description", form.fields)
        self.assertIn("profile_image", form.fields)
        self.assertIn("facebook", form.fields)
        self.assertIn("linkedin", form.fields)
        self.assertIn("github", form.fields)
        self.assertIn("twitter", form.fields)


