from django.urls import path
from .views import UserDetailAPIView

urlpatterns = [
    path('info/',UserDetailAPIView.as_view(),name='user-info-rest'),
]