from django.urls import path

from blog_app.blog_category.views import ShowCategories, AddCategoryView, EditCategoryView, \
    DeleteCategoryView

urlpatterns = (
    path('', ShowCategories.as_view(), name='categories'),
    path('create/', AddCategoryView.as_view(), name='add category'),
    path('edit/<int:pk>', EditCategoryView.as_view(), name='edit category'),
    path('delete/<int:pk>', DeleteCategoryView.as_view(), name='delete category'),
)
