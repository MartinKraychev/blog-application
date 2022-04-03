import tempfile

from django.contrib.auth import get_user_model
from django.test import TestCase

from blog_app.profile_app.models import Profile

UserModel = get_user_model()


class TestProfileModel(TestCase):

    def setUp(self):
        UserModel.objects.create(username='abv', password='123456')

    def test_full_name(self):
        profile = Profile.objects.create(
            first_name='Martin',
            last_name='Kraychev',
            age=32,
            description='Hello',
            profile_image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            user=UserModel.objects.all()[0]
        )

        self.assertEqual('Martin Kraychev', profile.get_full_name())
