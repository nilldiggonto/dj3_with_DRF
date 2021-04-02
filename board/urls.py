from django.urls import path
from .views import SprintViewApi,TaskViewSet,UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'sprints', SprintViewApi)
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)

# urlpatterns = [
#     # path('sprint/',SprintViewApi.as_view(),name='sprit-list'),
# ]
