import cloudinary
from PIL import Image
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from six import BytesIO

from blog_app.profile_app.models import Profile
from blog_app.user_auth.tests.utils import create_image

UserModel = get_user_model()


class TestProfileView(TestCase):
    def setUp(self):
        cloudinary.config(
            cloud_name="dtxdbvgoo",
            api_key="795737877112786",
            api_secret="PKCT_vHBMJG71tn6xsaq4ROTPAM")

        UserModel.objects.create_user(username='abv', password='123456abv')
        self.client.login(username='abv', password='123456abv')

    def test_redirect_to_edit_if_profile_exists(self):
        avatar = create_image(None, 'avatar.png')
        avatar_file = SimpleUploadedFile('front.png', avatar.getvalue())

        Profile.objects.create(
            first_name='Martin',
            last_name='Kraychev',
            age=32,
            description='Hello',
            profile_image=avatar_file,
            user=UserModel.objects.all()[0]
        )

        response = self.client.get(reverse('create profile'), follow=True)
        self.assertRedirects(response, expected_url=reverse('edit profile', kwargs={'pk': response.context['user'].id}),
                             status_code=302, target_status_code=200)

    def test_show_create_page_if_no_profile_exists(self):
        response = self.client.get(reverse('create profile'), follow=True)
        self.assertTemplateUsed(response, 'profile/create_profile.html')


class TestEditProfileView(TestCase):
    def setUp(self):
        cloudinary.config(
            cloud_name="dtxdbvgoo",
            api_key="795737877112786",
            api_secret="PKCT_vHBMJG71tn6xsaq4ROTPAM")

        UserModel.objects.create_user(username='test1', password='123456')
        self.client.login(username='test1', password='123456')

        avatar = create_image(None, 'avatar.png')
        avatar_file = SimpleUploadedFile('front.png', avatar.getvalue())
        Profile.objects.create(
            first_name='Test1',
            last_name='Test1',
            age=32,
            description='Test',
            profile_image=avatar_file,
            user=UserModel.objects.all()[0]
        )
        self.client.logout()

        UserModel.objects.create_user(username='test2', password='123456')
        self.client.login(username='test2', password='123456')

    def test_return_401__when_edit_other_profile(self):
        response = self.client.get(reverse('edit profile', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 401)
