from django.urls import path
from .views import (StatusListSearchAPIView,StatusListAPIView,StatusCreateAPIView,StatusDetailAPIView,
                    StatusUpdateAPIView,StatusDeleteAPIView)

urlpatterns = [
    path('list/',StatusListSearchAPIView.as_view(),name='drf-list'),
    path('create/',StatusCreateAPIView.as_view(),name='drf-create'),
    # path('detail/<int:pk>/',StatusDetailAPIView.as_view(),name='drf-detail'),
    path('detail/<int:id>/',StatusDetailAPIView.as_view(),name='drf-detail'),
    path('update/<int:pk>/',StatusUpdateAPIView.as_view(),name='drf-update'),
    path('delete/<int:pk>/',StatusDeleteAPIView.as_view(),name='drf-delete'),

    


]