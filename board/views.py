from django.shortcuts import render
from .models import Sprint
from .serializer import SprintSerializer
# Create your views here.
from rest_framework import viewsets

class SprintViewApi(viewsets.ModelViewSet):
    queryset = Sprint.objects.order_by('-endtime')
    serializer_class = SprintSerializer