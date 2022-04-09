"""blog_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_app.main.urls')),
    path('auth/', include('blog_app.user_auth.urls')),
    path('profile/', include('blog_app.profile_app.urls')),
    path('post/', include('blog_app.blog_post.urls')),
    path('categories/', include('blog_app.blog_category.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'blog_app.main.views.show404'
handler403 = 'blog_app.main.views.show403'
handler500 = 'blog_app.main.views.show500'
handler400 = 'blog_app.main.views.show400'
