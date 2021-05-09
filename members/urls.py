from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register/', views.UserRegisterView, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('edit_profile/', UserEditView, name='edit_profile'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='registration/logged_out.html'), name='logout'),

    # ACTIVATION PAR EMAIL
    path('activate/<uidb64>/<token>/',
         views.activate, name='activate'),

    # PASSWORD CHANGE
    path('password/', PasswordsChangeView.as_view(
        template_name='registration/change-password.html'), name="password_change"),
    path('password_success', views.password_success, name='password_success'),

    # PASSWORD RESET
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset/password_reset_complete.html'), name='password_reset_complete'),


]
