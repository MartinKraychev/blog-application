from django.urls import path

from blog_app.blog_post.views import CreatePostView, DetailsPostView, EditPostView, DeletePostView, EditCommentView, \
    DeleteCommentView

urlpatterns = (
    path('create/', CreatePostView.as_view(), name='create post'),
    path('details/<int:pk>', DetailsPostView.as_view(), name='post details'),
    path('edit/<int:pk>', EditPostView.as_view(), name='edit post'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete post'),
    path('edit-comment/<int:pk>', EditCommentView.as_view(), name='edit comment'),
    path('delete-comment/<int:pk>', DeleteCommentView.as_view(), name='delete comment'),
)
