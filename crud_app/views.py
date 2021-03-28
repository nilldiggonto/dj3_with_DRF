from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

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
