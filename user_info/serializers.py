from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
import datetime

from rest_framework_jwt.settings import api_settings
from rest_app.serializers import StatusSerializer,StatusLineUserSerailizer

User = get_user_model()



class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)


    # status_list = serializers.SerializerMethodField(read_only=True)
    # recent_status = serializers.SerializerMethodField(read_only=True)
    # status_uri  = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id','username','uri','status'#'status_list','status'#'recent_status','status'#'status_uri'
        ]
    def get_uri(self,obj):
        return '/drf/detail/{id}/'.format(id=obj.id)
    # def get_status_list(self,obj):
    #     qs = obj.status_set.all()
    #     return StatusLineUserSerailizer(qs,many=True).data

    def get_recent_status(self,obj):
        qs = obj.status_set.all()
        return StatusLineUserSerailizer(qs,many=True).data

    # def get_status_uri(self,obj):
    #     return self.get_uri(obj) + 'status/'

    def get_status(self,obj):
        data = {
            'uri': self.get_uri(obj) +'status/',
            'recent':self.get_recent_status(obj)
        }
        return data