from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.models import Group
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login, logout, get_user_model
from django.views.generic import CreateView, DeleteView

from blog_app.profile_app.templatetags.profile import get_profile
from blog_app.user_auth.forms import MyUserCreationForm, MyAuthenticationForm, MyPasswordChangeForm

UserModel = get_user_model()


class UserRegistrationView(CreateView):
    # pass either form or model, fields on the CreateView
    form_class = MyUserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('create profile')

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        auth_login(self.request, self.object)

        return result


class UserLoginView(LoginView):
    template_name = 'auth/login.html'
    form_class = MyAuthenticationForm

    def get_success_url(self):

        profile = get_profile(
            {'request': self.request}
        )

        if not profile:
            return reverse_lazy('create profile')

        return reverse_lazy('dashboard')


class UserLogoutView(LogoutView):
    pass


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'auth/change_password.html'
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('sign in')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            self.request.session.flush()
            logout(self.request)
            return super().form_valid(form)


class DeleteAccountView(LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = 'auth/delete_account.html'
    success_url = reverse_lazy('sign in')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object != self.request.user:
            return HttpResponse('Unauthorized', status=401)

        return super().dispatch(request, *args, **kwargs)
