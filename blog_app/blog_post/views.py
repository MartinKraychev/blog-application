from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView
from blog_app.blog_post.forms import CreatePostForm, CreateCommentForm, EditPostForm, EditCommentForm, CreateLikeForm
from blog_app.blog_post.models import Post, Comment, PostLike
from blog_app.profile_app.templatetags.profile import get_profile


class CreatePostView(LoginRequiredMixin, CreateView):
    form_class = CreatePostForm
    template_name = 'blog_post/create_post.html'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        profile = get_profile(
            {'request': self.request}
        )

        if not profile:
            return redirect(reverse('create profile'))

        return super(CreatePostView, self).dispatch(request, *args, **kwargs)

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
        if self.object.user == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog_post/delete_post.html'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied


class DetailsPostView(FormMixin, DetailView):
    model = Post
    template_name = 'blog_post/post_detail.html'
    context_object_name = 'post'
    form_class = CreateCommentForm
    second_form_class = CreateLikeForm

    def get_success_url(self):
        return reverse('post details', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(DetailsPostView, self).get_context_data(**kwargs)

        context['comment_form'] = CreateCommentForm(initial={'post': self.object})
        context['like_form'] = CreateLikeForm(initial={'post': self.object})

        if self.request.user.is_authenticated:
            context['liked'] = PostLike.objects.filter(user=self.request.user, post=self.object)

        context['total_likes'] = PostLike.objects.filter(post=self.object).count
        context['comments'] = Comment.objects.filter(post_id=self.object.id)
        context['can_not_comment_or_like'] = (
                self.request.user.id == self.object.user.id or not self.request.user.is_authenticated)
        context['is_post_owner'] = (self.request.user.id == self.object.user.id)

        return context

    def form_invalid(self, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if 'comment' in request.POST:

            # get the primary form
            form_class = self.get_form_class()
            form_name = 'comment'

        else:

            # get the secondary form
            form_class = self.second_form_class
            form_name = 'like'

        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(**{form_name: form})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = self.object
        form.save()

        return super(DetailsPostView, self).form_valid(form)


class EditCommentView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = EditCommentForm
    template_name = 'blog_post/edit_comment.html'

    def get_success_url(self):
        post_pk = self.object.post.id
        return reverse('post details', kwargs={'pk': post_pk})

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = self.object.post
        form.save()
        return super().form_valid(form)


class DeleteCommentView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog_post/delete_comment.html'

    def get_success_url(self):
        post_pk = self.object.post.id
        return reverse('post details', kwargs={'pk': post_pk})

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied
