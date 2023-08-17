from django.urls import path, include
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, 
    PasswordResetCompleteView, LoginView, LogoutView
    )
from .views import (
        profile_update, change_password, 
        CustomUserList,
        add, 
        edit, delete, 
        validate_username,
    )
from .forms import EmailValidationOnForgotPassword


urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('setting/', profile_update, name='edit_profile'),
    path('change_password/', change_password, name='change_password'),

    path('custom-users/', CustomUserList.as_view(), name='list'),
    path('custom-user/add/', add, name='add'),
    path('custom-user/<int:pk>/edit/', edit, name='edit'),
    path('custom-users/<int:pk>/delete/', delete, name='delete'),

    path('ajax/validate-username/', validate_username, name='validate_username'),
]
