from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfileView, EditProfilePageView, CreateProfileView
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name="registration/change_password.html")),
    path('password/', PasswordsChangeView.as_view(template_name="registration/change_password.html")),
    path('password_success', views.password_success, name="password_success"),
    path('<int:pk>/profile', ShowProfileView.as_view(), name="user_profile"),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(), name="edit_profile_page"),
    path('create_profile_page', CreateProfileView.as_view(), name="create_profile_page"),
]