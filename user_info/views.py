from django.shortcuts import render
from django.contrib.auth import authenticate,get_user_model
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.conf import settings
from django.utils import timezone
import datetime
from rest_framework import generics
from .serializers import UserDetailSerializer
# Create your views here.

User = get_user_model()
class UserDetailAPIView(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = 'username'