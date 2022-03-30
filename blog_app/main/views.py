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


class ShowDashboardCategory(ListView):
    model = Post
    template_name = 'main/dashboard.html'
    paginate_by = 5
    context_object_name = 'posts'

    def get_category_name(self):
        return self.kwargs.get('name').capitalize()

    def get_queryset(self):
        category = Category.objects.filter(name=self.get_category_name()).first()
        query_set = Post.objects.filter(category=category)

        return query_set

    def get_context_data(self, **kwargs):
        context = super(ShowDashboardCategory, self).get_context_data(**kwargs)
        context['category'] = self.get_category_name()

        return context
