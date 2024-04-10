from django.urls import path
from django.contrib.auth.views import (
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # path(r'.*\js$', views.java_script),
    path('home/', views.home, name='home'),
    path('', lambda req: redirect('home')),
    path('checklist/', views.checklist, name='checklist'),
    path(
        'submit_checklist_result/',
        views.submit_checklist_result,
        name='submit_checklist_result'
        ),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='/home/'), name='logout'),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='purchases/reset_password.html'),
        name='password_change'
        ),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='purchases/password_reset_sent.html'),
        name='password_reset'
        ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='purchases/password_reset_form.html'),
        name='password_reset_confirm'
        ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='purchases/password_reset_done.html'),
        name='password_reset_complete'
        ),
]
