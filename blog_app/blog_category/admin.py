from django.contrib import admin

from blog_app.blog_category.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
