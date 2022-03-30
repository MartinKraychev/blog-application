from django.contrib import admin

from blog_app.profile_app.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

