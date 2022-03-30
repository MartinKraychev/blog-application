from django import forms

from blog_app.blog_category.models import Category
from blog_app.main.mixins import BootstrapFormMixin


class AddCategoryForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Category
        fields = '__all__'


class EditCategoryForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Category
        fields = '__all__'




