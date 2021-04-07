from django.urls import path
from django.contrib import admin
from rest_framework_jwt.views import refresh_jwt_token,obtain_jwt_token

from .views import AuthView,RegisterView

urlpatterns = [
    path('',AuthView.as_view(),name='auth_app_home'),
    path('register/',RegisterView.as_view(),name='auth-app-register'),
    path('jwt/',obtain_jwt_token),
    path('jwt/refresh/',refresh_jwt_token),
]