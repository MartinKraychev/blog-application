from django.contrib import admin

from blog_app.user_auth.models import BlogUser


@admin.register(BlogUser)
class BlogUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_staff', 'is_superuser']
    filter_horizontal = ('groups', 'user_permissions')
