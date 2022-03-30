from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from blog_app.blog_category.forms import AddCategoryForm, EditCategoryForm
from blog_app.blog_category.models import Category


class ShowCategories(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'blog_category.view_category'
    model = Category
    template_name = 'category/show_category.html'
    context_object_name = 'categories'


class AddCategoryView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'blog_category.add_category'
    form_class = AddCategoryForm
    template_name = 'category/add_category.html'
    success_url = reverse_lazy('categories')


class EditCategoryView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'blog_category.change_category'
    model = Category
    form_class = EditCategoryForm
    template_name = 'category/edit_category.html'
    success_url = reverse_lazy('categories')


class DeleteCategoryView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'blog_category.delete_category'
    model = Category
    template_name = 'category/delete_category.html'
    success_url = reverse_lazy('categories')
