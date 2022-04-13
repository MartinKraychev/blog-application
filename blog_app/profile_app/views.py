from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView

from blog_app.profile_app.forms import ProfileCreateForm
from blog_app.profile_app.models import Profile
from blog_app.profile_app.templatetags.profile import get_profile


class CreateProfileView(LoginRequiredMixin, CreateView):
    form_class = ProfileCreateForm
    template_name = 'profile/create_profile.html'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):

        profile = get_profile(
            {'request': self.request}
        )

        if profile:
            return redirect(reverse('edit profile', kwargs={'pk': request.user.id}))

        return super(CreateProfileView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/edit_profile.html'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        # PermissionDenied returns 403
        raise PermissionDenied

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile/profile_view.html'
    context_object_name = 'person_profile'
