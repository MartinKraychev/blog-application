from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

from blog_app.main.mixins import BootstrapFormMixin

UserModel = get_user_model()


class MyUserCreationForm(BootstrapFormMixin, UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2')


class MyAuthenticationForm(BootstrapFormMixin, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


class MyPasswordChangeForm(BootstrapFormMixin, PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
