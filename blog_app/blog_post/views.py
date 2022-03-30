from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView

from blog_app.blog_post.forms import CreatePostForm, CreateCommentForm, EditPostForm
from blog_app.blog_post.models import Post, Comment


class CreatePostView(LoginRequiredMixin, CreateView):
    form_class = CreatePostForm
    template_name = 'blog_post/create_post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditPostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'blog_post/edit_post.html'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            return HttpResponse('Unauthorized', status=401)

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog_post/delete_post.html'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            return HttpResponse('Unauthorized', status=401)

        return super().dispatch(request, *args, **kwargs)


class DetailsPostView(FormMixin, DetailView):
    model = Post
    template_name = 'blog_post/post_detail.html'
    context_object_name = 'post'
    form_class = CreateCommentForm

    def get_success_url(self):
        return reverse('post details', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(DetailsPostView, self).get_context_data(**kwargs)
        context['form'] = CreateCommentForm(initial={'post': self.object})
        context['comments'] = Comment.objects.filter(post_id=self.object.id)
        context['can_not_comment'] = (
                self.request.user.id == self.object.user.id or not self.request.user.is_authenticated)
        context['is_owner'] = (self.request.user.id == self.object.user.id)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = self.object
        form.save()

        return super(DetailsPostView, self).form_valid(form)
