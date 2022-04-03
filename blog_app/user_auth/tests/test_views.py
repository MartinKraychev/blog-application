import cloudinary
from PIL import Image
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from six import BytesIO

from blog_app.profile_app.models import Profile
from blog_app.user_auth.models import BlogUser
from blog_app.user_auth.tests.utils import create_image

UserModel = get_user_model()


class TestUserRegistrationView(TestCase):

    def setUp(self):
        group_name = "regular_user"
        self.group = Group(name=group_name)
        self.group.save()

    def test_if_template_is_correct(self):
        response = self.client.get(reverse('sign up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/register.html')

    def test_with_valid_form_data(self):
        response = self.client.post(reverse('sign up'), data={
            'username': 'Martin',
            'password1': '123456abv',
            'password2': '123456abv'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogUser.objects.count(), 1)

    def test_invalid_data_different_passwords(self):
        response = self.client.post(reverse('sign up'), data={
            'username': 'Martin',
            'password1': '123456abv',
            'password2': '123456abvc'
        })

        self.failIf(response.context['form'].is_valid())
        self.failUnless(response.context['form'].errors)


class TestUserLoginView(TestCase):
    def setUp(self):
        UserModel.objects.create_user(username='foo', password='123456abv')

        cloudinary.config(
            cloud_name="dtxdbvgoo",
            api_key="795737877112786",
            api_secret="PKCT_vHBMJG71tn6xsaq4ROTPAM")

    def test_redirect_if_no_profile(self):
        response = self.client.post(reverse('sign in'), data={
            'username': 'foo',
            'password': '123456abv'
        }, follow=True)

        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, expected_url=reverse('create profile'),
                             status_code=302, target_status_code=200)

    def test_redirect_if_profile_(self):
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

        response = self.client.post(reverse('sign in'), data={
            'username': 'foo',
            'password': '123456abv'
        }, follow=True)

        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, expected_url=reverse('dashboard'),
                             status_code=302, target_status_code=200)
