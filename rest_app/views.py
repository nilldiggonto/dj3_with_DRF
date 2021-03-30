from django.shortcuts import render
from .models import Status
from .serializers import StatusSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins
# from rest_framework import 
# Create your views here.
class StatusListAPIView(APIView):
    
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
class StatusListSearchAPIView(generics.ListAPIView):

    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

#generics CREATE VIEW
class StatusCreateAPIView(generics.CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def perform_create(self,serializer):
        serializer.save(user =self.request.user)

#generic Detail View
class StatusDetailAPIView(generics.RetrieveAPIView):
    lookup_field = 'id' #slug
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    #### another way to lookup
    # def get_object(self,*args,**kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Status.objects.get(id=kw_id)

#generic Update API View
class StatusUpdateAPIView(generics.UpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

#generic Delete API View
class StatusDeleteAPIView(generics.DestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


####  MIXINS ############## ############
class StatusListCreateAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class StatusRetrieveUpdateDeleteAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



