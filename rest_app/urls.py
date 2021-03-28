from django.urls import path
from .views import StatusListSearchAPIView,StatusListAPIView

urlpatterns = [
    path('list/',StatusListAPIView.as_view(),name='drf-list'),

]