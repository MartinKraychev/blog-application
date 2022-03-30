from django import forms

from blog_app.main.mixins import BootstrapFormMixin
from blog_app.profile_app.models import Profile


class ProfileCreateForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

        self.fields['facebook'].widget.attrs['placeholder'] = 'optional'
        self.fields['github'].widget.attrs['placeholder'] = 'optional'
        self.fields['linkedin'].widget.attrs['placeholder'] = 'optional'
        self.fields['twitter'].widget.attrs['placeholder'] = 'optional'

    class Meta:
        model = Profile
        exclude = ('user',)


class ProfileEditForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

        self.fields['facebook'].widget.attrs['placeholder'] = 'optional'
        self.fields['github'].widget.attrs['placeholder'] = 'optional'
        self.fields['linkedin'].widget.attrs['placeholder'] = 'optional'
        self.fields['twitter'].widget.attrs['placeholder'] = 'optional'

    class Meta:
        model = Profile
        exclude = ('user',)




