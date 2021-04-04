from django.shortcuts import render
from .models import Status
from .serializers import StatusSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins


from django.shortcuts import get_object_or_404
import json
# from rest_framework import 

def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid
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

# class StatusRetrieveUpdateDeleteAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
class StatusRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
#mixins
    # def put(self,request,*args,**kwargs):
    #     return self.update(request,*args,**kwargs)

    
    # def patch(self,request,*args,**kwargs):
    #     return self.update(request,*args,**kwargs)

    # def delete(self,request,*args,**kwargs):
    #     return self.destroy(request,*args,**kwargs)


#Single API View TO DO ALL CRUD
class StatusCrudAPIView(mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,generics.ListAPIView):

                        serializer_class = StatusSerializer
                        passed_id = None

                        #list view
                        def get_queryset(self):
                                request = self.request
                                qs = Status.objects.all()
                                query = self.request.GET.get('q')
                                if query is not None:
                                    qs = qs.filter(content__icontains=query)
                                return qs

                        # retrive view
                        
                        def get_object(self):
                            request = self.request
                            passed_id = request.GET.get('id',None) or self.passed_id
                            queryset = self.get_queryset()
                            obj = None
                            if passed_id is not None:
                                obj = get_object_or_404(queryset,id=passed_id)
                                self.check_object_permissions(request,obj)
                            return obj
                        
                        def get(self,request,*args,**kwargs):
                            url_passed_id = request.GET.get('id',None)
                            json_data = {}
                            body_ = request.body
                            if is_json(body_):
                                json_data = json.loads(request.body)

                            # json_data = json.loads(request.body)
                            json_passed_id = json_data.get('id',None)
                            passed_id = url_passed_id or json_passed_id or None
                            self.passed_id = passed_id
                            if passed_id is not None:
                                return self.retrieve(request,*args,**kwargs)
                            return super().get(request,*args,**kwargs)

                        #post view
                        def post(self,request,*args,**kwargs):
                            
                            return self.create(request,*args,**kwargs)

                        def put(self,request,*args,**kwargs):
                            url_passed_id = request.GET.get('id',None)
                            json_data = {}
                            body_ = request.body
                            if is_json(body_):
                                json_data = json.loads(request.body)

                            # json_data = json.loads(request.body)
                            json_passed_id = json_data.get('id',None)
                            requested_id = request.data.get('id')
                            passed_id = url_passed_id or json_passed_id or requested_id or None
                            self.passed_id = passed_id
                            return self.update(request,*args,**kwargs)

                        def patch(self,request,*args,**kwargs):
                            return self.update(request,*args,**kwargs)

                        def perform_destroy(self, instance):
                            if instance is not None:
                                return instance.delete()
                            else:
                                return None 

                        def delete(self,request,*args,**kwargs):
                            return self.destroy(request,*args,**kwargs)

######## Status new detail view
class StatusNewDetailAPIView(mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.RetrieveAPIView):
    permission_classes = []
    authentications_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
        




