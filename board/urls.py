from django.urls import path
from .views import SprintViewApi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'sprints', SprintViewApi)
# router.register(r'tasks', views.TaskViewSet)
# router.register(r'users', views.UserViewSet)

# urlpatterns = [
#     # path('sprint/',SprintViewApi.as_view(),name='sprit-list'),
# ]
