from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog_app.user_auth.models import BlogUser


@admin.register(BlogUser)
class BlogUserAdmin(admin.ModelAdmin):
    # list_display = ['username', 'is_staff', 'is_superuser']
    filter_horizontal = ('groups', 'user_permissions')
    list_filter = ('groups__name',)
    list_display = ('username', 'custom_group',)

    def custom_group(self, obj):
        """
        get group, separate by comma, and display empty string if user has no group
        """
        return ','.join([g.name for g in obj.groups.all()]) if obj.groups.count() else ''


admin.site.unregister(BlogUser)
admin.site.register(BlogUser, BlogUserAdmin)
