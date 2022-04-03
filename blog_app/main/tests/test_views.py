from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class TestShowDashboardCategory(TestCase):

    def setUp(self):
        UserModel.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')

    def test_right_category(self):
        response = self.client.get(reverse('dashboard category', kwargs={'name': 'Politics'}))
        self.assertContains(response, 'Politics')

