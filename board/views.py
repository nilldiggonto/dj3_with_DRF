from django.shortcuts import render
from .models import Sprint,Task
from .serializer import SprintSerializer,TaskSerializer,UserSerializer
# Create your views here.
from rest_framework import viewsets,authentication,permissions
from django.contrib.auth.models import User

from rest_framework import authentication,permissions,viewsets,filters


#creating a custom mixins
class DefaultMixins(object):
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication
    )
    permission_classes = (permissions.IsAuthenticated,)

    paginated_by =25
    paginated_by_param = 'page_size'
    max_paginated_by = 100

    filter_backends =(
        # filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
class SprintViewApi(DefaultMixins,viewsets.ModelViewSet):
    queryset = Sprint.objects.order_by('-endtime')
    serializer_class = SprintSerializer
    search_fields = ('name',)
    ordering_fields = ('endtime','name')


############ TASK
class TaskViewSet(DefaultMixins,viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    search_fields = ('name', 'description', )
    ordering_fields = ('name', 'order', 'started', 'due', 'completed', ) 

#userview Serializer
class UserViewSet(DefaultMixins,viewsets.ReadOnlyModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer

    search_fields = (User.USERNAME_FIELD, )


    #do the router test