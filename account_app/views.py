from django.shortcuts import render
from django.contrib.auth import authenticate,get_user_model
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.conf import settings
from django.utils import timezone
import datetime

from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER



# Create your views here.





expire_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']
def jwt_response_payload_handler(token,user=None,request=None):
    return {
        'token':token,
        'user':user.username,
        'expires': timezone.now() + expire_delta - datetime.timedelta(seconds=3000)
    }



User = get_user_model()

class AuthView(APIView):
    # autentication_classes = []
    permission_classes = [permissions.AllowAny,]
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return Response({'status':'You are already authenticated'},status=400)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username,password=password)

        qs = User.objects.filter(Q(username__iexact=username)|Q(email__iexact=username)).distinct()
        if qs.count()==1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user= user_obj


                print(user)
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                print(token)
                response = jwt_response_payload_handler(token,user,request=request)
                return Response(response)
        return Response({'detail':'wrong info'})
