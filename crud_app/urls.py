from django.urls import path
from .views import list_view,ListAPIview,ListAPIview2

urlpatterns = [
    path('list/',list_view,name='rest-list'),
    path('list/one/',ListAPIview.as_view(),name='rest-list-one'),
    path('list/two/',ListAPIview2.as_view(),name='rest-list-two')
]