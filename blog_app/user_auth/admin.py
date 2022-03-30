from django.contrib import admin

from blog_app.user_auth.models import BlogUser


@admin.register(BlogUser)
class BlogUserAdmin(admin.ModelAdmin):
    list_display = ['username']
    filter_horizontal = ('groups', 'user_permissions')
