from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
import datetime

from rest_framework_jwt.settings import api_settings
# from rest_app.serializers import StatusSerializer


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()

expire_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']
def jwt_response_payload_handler(token,user=None,request=None):
    return {
        'token':token,
        'user':user.username,
        'expires': timezone.now() + expire_delta - datetime.timedelta(seconds=3000)
    }




## Serializer more user-friendly
class UserPublicSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id','username','uri'
        ]
    def get_uri(self,obj):
        return 'username/url/{id}'.format(id=obj.id)


class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    status_list = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id','username','uri','status_list'
        ]
    def get_uri(self,obj):
        return 'username/url/{id}'.format(id=obj.id)
    def get_status_list(self,obj):
        return 'oj'

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)
    success_message = serializers.SerializerMethodField(read_only=True)
    # token_response = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['username','email','password','password2','token','expires','success_message']#,'token_response']
        # extra_kwargs = {'password':{'write_only':True}}
    
    def get_success_message(self,obj):
        return "Thank you for register. Verify by confirming mail"

    ### WAYS TO GET RESPONSE
    # def get_token_response(self,obj):
    #     user = obj
    #     payload = jwt_payload_handler(user)
    #     token = jwt_encode_handler(payload)
    #     context= self.context
    #     # print(token)
    #     # request = None
    #     request = context['request']

    #     # response = jwt_response_payload_handler(token,user,request=request)
    #     response = jwt_response_payload_handler(token,user,request=context['request'])

    #     return response


    def get_expires(self,obj):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=3000)


    def validate_email(self,value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('Email alreay exists')
        return value

    def validate_username(self,value):
        qs = User.objects.filter(username__iexact= value)
        if qs.exists():
            raise serializers.ValidationError('Username already exists')
        return value
    
    def get_token(self,obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token
        # pass
    
    def validate(self,data):
        pw = data.get('password')
        pw2 = data.pop('password2')
        if pw != pw2:
            raise serializers.ValidationError('Password must match')
        return data

    def create(self,validated_data):
        print(validated_data)
        user_obj = User(username=validated_data.get('username'),email=validated_data.get('email'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.is_active=  False
        user_obj.save()
        return user_obj
