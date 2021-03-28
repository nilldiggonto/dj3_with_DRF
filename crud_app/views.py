from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.core.serializers import serialize

# Create your views here.
from .models import UpdateImage

import json

from django.views.generic import View
from .api_mixins import ListAPIviewmixins

### GETTING JSON RESPONSE WITH VIEW
def list_view(request):


    data = {
        'one':'one',
        'two':'two'

    }
    # json_data = json.dumps(data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(data)

############################## WITH CLASS 
class ListAPIview(View):
    def get(self,request,*args,**kwargs):
        data = {
            'one':'one',
            'two':'two',
        }
        return JsonResponse(data)



## WITH CUSTOM MIXINS
class ListAPIview2(ListAPIviewmixins,View):
    def get(self,request,*args,**kwargs):
        data ={
            'one':'one',
            'two':'two',
        }

        return self.render_to_json_response(data)


####### SERIALIZER VIEW
# class SerailizedDetailview(ListAPIviewmixins,View):


class SerailizedListview(View):
    def get(self,request,*args,**kwargs):
        qs = UpdateImage.objects.all()
        # data = serialize('json',qs,fields=('user','content'))
        # data = {
        #     'user':obj.user.username,
        #     'content':obj.content

        # }
        # json_data = json.dumps(data)
        # json_data = data
        json_data = UpdateImage.objects.all().serialize() #model manager
        return HttpResponse(json_data,content_type='application/json')
        # return self.render_to_json_response(data)
class SerailizedDetailview(View):
    def get(self,request,*args,**kwargs):
        obj = UpdateImage.objects.get(id=1)
        # data = serialize('json',[obj,],fields=('user,content'))
        # data = {
        #     'user':obj.user.username,
        #     'content':obj.content

        # }
        # json_data = json.dumps(data)
        # json_data = data
        json_data = obj.serialize()
        return HttpResponse(json_data,content_type='application/json')
        # return self.render_to_json_response(data)





