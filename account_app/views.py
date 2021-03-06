from django.shortcuts import render
from django.contrib.auth import authenticate,get_user_model
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.conf import settings
from django.utils import timezone
import datetime

from .serializers import UserRegistrationSerializer,UserDetailSerializer
from rest_framework import generics

from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


from .permissions import AnonPermissionOnly



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
    permission_classes = [AnonPermissionOnly,]
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
                # print(token)
                response = jwt_response_payload_handler(token,user,request=request)
                return Response(response)
        return Response({'detail':'wrong info'})


#register view
class RegisterView(APIView):
    # autentication_classes = []
    permission_classes = [permissions.AllowAny,]
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return Response({'status':'You are already authenticated'},status=400)
        data = request.data
        ## required fields
        try:
            username    = data.get('username')
            email       = data.get('email')
            password    = data.get('password')     
            password2   = data.get('password2')
            ##
            # user = authenticate(username=username,password=password)

            qs = User.objects.filter(Q(username__iexact=username)|Q(email__iexact=username)).distinct()
            if password != password2:
                return Response({'detail':'password should match'})
            if qs.exists():
                return Response({'detail':'User Already Exists'})
            else:
                user = User.objects.create(username=username,email=email)
                user.set_password(password)
                user.save()
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                # print(token)
                response = jwt_response_payload_handler(token,user,request=request)
                return Response(response)

        
            return Response({'detail':'what the hell is that'})
        except:
            return Response({'status':'not ok'})



#with serializer
class RegisterAPIView(generics.CreateAPIView):
    queryst = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AnonPermissionOnly,]

    def get_serializer_context(self,*args,**kwargs):
        return {'request':self.request}


########### USER DETAIL VIEW
class UserDetailAPIView(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = 'username'
