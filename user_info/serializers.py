from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
import datetime

from rest_framework_jwt.settings import api_settings
from rest_app.serializers import StatusSerializer

User = get_user_model()



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