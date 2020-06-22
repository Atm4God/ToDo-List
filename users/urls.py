from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', views.register, name="signup"),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='users/password-reset.html'),
         name='password_reset'),
    path('password-reset_done', auth_views.PasswordResetDoneView.as_view(template_name='users/password-reset-done.html'),
         name='password_reset_done'),
    path('password-reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password-reset-confirm.html'),
         name='password_reset_confirm'),
    path('password-reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password-reset-complete.html'),
         name='password_reset_complete'),
    path('profile', views.profile, name="profile"),
]
