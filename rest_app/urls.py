from django.urls import path
from .views import StatusListSearchAPIView,StatusListAPIView,StatusCreateAPIView

urlpatterns = [
    path('list/',StatusListSearchAPIView.as_view(),name='drf-list'),
    path('create/',StatusCreateAPIView.as_view(),name='drf-create'),

]