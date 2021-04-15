from django.shortcuts import render
from django.contrib.auth import authenticate,get_user_model
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,pagination
from django.conf import settings
from django.utils import timezone
import datetime
from rest_framework import generics
from .serializers import UserDetailSerializer
# Create your views here.
from rest_app.serializers import StatusLineUserSerailizer
from rest_app.models import Status



User = get_user_model()
class UserDetailAPIView(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = 'username'



class CustomPagination(pagination.PageNumberPagination):
    page_size = 3
class UserDetailStatusAPIView(generics.ListAPIView):
    # queryset = User.objects.filter(is_active=True)
    serializer_class = StatusLineUserSerailizer
    pagination_class = CustomPagination
    def get_queryset(self,*args,**kwargs):
        username = self.kwargs.get('username',None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)
    