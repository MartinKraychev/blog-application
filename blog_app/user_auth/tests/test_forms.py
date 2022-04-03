from django.test import TestCase

from blog_app.user_auth.forms import MyUserCreationForm


class TestMyUserCreationForm(TestCase):

    def test_form_check_fields(self):
        form = MyUserCreationForm()
        self.assertIn("username", form.fields)
        self.assertIn("password1", form.fields)
        self.assertIn("password2", form.fields)

    def test_boostrap_mixin(self):
        form = MyUserCreationForm()
        self.assertInHTML('<input type="text" name="username" maxlength="30" autofocus class="form-control" required id="id_username">', str(form['username']))

    


