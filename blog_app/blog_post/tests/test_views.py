import cloudinary
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from blog_app.blog_category.models import Category
from blog_app.blog_post.models import Post
from blog_app.profile_app.models import Profile
from blog_app.user_auth.tests.utils import create_image


UserModel = get_user_model()


class TestDetailsPostView(TestCase):

    def setUp(self):
        group_name = "regular_user"
        self.group = Group(name=group_name)
        self.group.save()

        cloudinary.config(
            cloud_name="dtxdbvgoo",
            api_key="795737877112786",
            api_secret="PKCT_vHBMJG71tn6xsaq4ROTPAM")

        UserModel.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')

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

        Category.objects.create(name='Test Category', description='test')

        Post.objects.create(
            heading='test',
            text='test text',
            image=avatar_file,
            category=Category.objects.all()[0],
            user=UserModel.objects.all()[0]
        )

    def test_if_right_template_used(self):
        response = self.client.get(reverse('post details', kwargs={'pk': 1}))
        self.assertTemplateUsed(response, 'blog_post/post_detail.html')

    def test_if_user_is_attached(self):
        response = self.client.get(reverse('post details', kwargs={'pk': 1}))
        self.assertEqual(UserModel.objects.all()[0], response.context['user'])

    def test_if_context_contains_comment_form(self):
        response = self.client.get(reverse('post details', kwargs={'pk': 1}))
        self.assertTrue(response.context['form'])

    def test_if_owner_is_right(self):
        response = self.client.get(reverse('post details', kwargs={'pk': 1}))
        self.assertTrue(response.context['is_owner'])


