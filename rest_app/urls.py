from django.urls import path
from .views import (StatusListSearchAPIView,StatusListAPIView,StatusCreateAPIView,StatusDetailAPIView,StatusCrudAPIView,
                    StatusUpdateAPIView,StatusDeleteAPIView,StatusListCreateAPIView,StatusRetrieveUpdateDeleteAPIView,
                    StatusNewDetailAPIView)

urlpatterns = [
    path('crud/',StatusCrudAPIView.as_view(),name='drf-crud'),
    path('list/',StatusListSearchAPIView.as_view(),name='drf-list'),
    path('create/',StatusCreateAPIView.as_view(),name='drf-create'),
    path('list/create/',StatusListCreateAPIView.as_view(),name='drf-list-create'),
    ##
    path('new/crud/<int:id>/',StatusNewDetailAPIView.as_view(),name='drf-new-crud'),
    path('detail/update/delete/<int:pk>/',StatusRetrieveUpdateDeleteAPIView.as_view(),name='drf-up-d'),
    # path('detail/<int:pk>/',StatusDetailAPIView.as_view(),name='drf-detail'),
    path('detail/<int:id>/',StatusDetailAPIView.as_view(),name='drf-detail'),
    path('update/<int:pk>/',StatusUpdateAPIView.as_view(),name='drf-update'),
    path('delete/<int:pk>/',StatusDeleteAPIView.as_view(),name='drf-delete'),

    


]