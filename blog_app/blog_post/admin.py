from django.contrib import admin

from blog_app.blog_post.models import Post, Comment, PostLike


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'post', 'user')


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'post', 'user')
