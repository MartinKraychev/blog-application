from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from blog_app.blog_category.models import Category
from blog_app.blog_post.models import Post


class IndexView(TemplateView):
    template_name = 'main/index.html'


class DashboardView(ListView):
    model = Post
    template_name = 'main/dashboard.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            number_of_likes=Count('postlike')
        ).order_by('-number_of_likes')
        return queryset


class ShowDashboardCategory(ListView):
    model = Post
    template_name = 'main/dashboard.html'
    paginate_by = 5
    context_object_name = 'posts'

    def get_category_name(self):
        return self.kwargs.get('name').capitalize()

    def get_queryset(self):
        category = Category.objects.filter(name=self.get_category_name()).first()
        queryset = Post.objects.filter(category=category) \
            .annotate(
            number_of_likes=Count('postlike')
        ) \
            .order_by('-number_of_likes')

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ShowDashboardCategory, self).get_context_data(**kwargs)
        context['category'] = self.get_category_name()
        context['categories'] = Category.objects.all()

        return context


def show404(request, exception):
    return render(request, 'error_codes/404.html')


def show403(request, exception):
    return render(request, 'error_codes/403.html')


def show500(request, exception):
    return render(request, 'error_codes/500.html')


def show400(request, exception):
    return render(request, 'error_codes/400.html')
