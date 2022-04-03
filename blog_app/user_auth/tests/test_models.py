from django.contrib.auth import get_user_model
from django.db import DataError
from django.test import TestCase

UserModel = get_user_model()


class BlogUserTests(TestCase):

    def test_creating_user_with_valid_data(self):
        UserModel.objects.create(username='abv', password='123456')
        user = UserModel.objects.all()[0]
        self.assertEqual(user.username, 'abv')

    def test_creating_user_with_bigger_max_length(self):
        with self.assertRaises(DataError):
            UserModel.objects.create(username='abvaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', password='123456')

