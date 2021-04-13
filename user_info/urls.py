from django.urls import path
from .views import UserDetailAPIView,UserDetailStatusAPIView

urlpatterns = [
    path('info/<str:username>/',UserDetailAPIView.as_view(),name='user-info-rest'),
    path('info/<str:username>/status/',UserDetailStatusAPIView.as_view(),name='user-status-rest'),

]