from django.shortcuts import render
from .models import Status
from .serializers import StatusSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.
class StatusListSearchAPIView(APIView):
    
    # pass
    def get(self,request,format=None):
        qs = Status.objects.all()
        # serializer = [user.user.username for user in qs]
        serializer = StatusSerializer(qs,many=True)
        return Response(serializer.data)

    # def post(self,request,format=None):
    #     qs = Status.objects.all()
    #     # serializer = [user.user.username for user in qs]
    #     serializer = StatusSerializer(qs,many=True)
    #     return Response(serializer.data)

#generic LIST VIEW
class StatusListAPIView(generics.ListAPIView):

    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs


