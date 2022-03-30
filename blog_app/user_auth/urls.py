from django.urls import path, include

from blog_app.user_auth.views import UserRegistrationView, UserLoginView, UserLogoutView, ChangePasswordView, \
    DeleteAccountView

urlpatterns = (
    path('sign-in/', UserLoginView.as_view(), name='sign in'),
    path('sign-up/', UserRegistrationView.as_view(), name='sign up'),
    path('sign-out/', UserLogoutView.as_view(), name='sign out'),
    path('change-password/', ChangePasswordView.as_view(), name='change password'),
    path('delete-account/<int:pk>', DeleteAccountView.as_view(), name='delete account'),
)
