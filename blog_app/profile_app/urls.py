from django.urls import path
from blog_app.profile_app.signals import delete_profile_picture
from blog_app.profile_app.views import CreateProfileView, EditProfileView, ProfileView

urlpatterns = (
    path('create/', CreateProfileView.as_view(), name='create profile'),
    path('edit/<int:pk>', EditProfileView.as_view(), name='edit profile'),
    path('view/<int:pk>', ProfileView.as_view(), name='view profile'),
)

