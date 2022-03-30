from django.urls import path

from blog_app.main.views import IndexView, DashboardView, ShowDashboardCategory

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/<str:name>/', ShowDashboardCategory.as_view(), name='dashboard category'),
)
