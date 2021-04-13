from rest_framework import serializers
from .models import Status
from account_app.serializers import UserPublicSerializer


class StatusLineUserSerailizer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status
        fields = ['id','content','image','uri']
        # read_only_fields =['user']

    def get_uri(self,obj):
        return 'url/url/{id}'.format(id=obj.id)

class StatusSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Status
        fields = ['id','user','content','image','uri']
        read_only_fields = ['user',]
    
    def get_uri(self,obj):
        return 'drf/{id}/'.format(id=obj.id)

    # def validate_content(self,value):
    #     if len(value)>100:
    #         raise serializers.ValidationError('Too long to write')
    #     return value
    def validate(self,data):
        content = data.get('content',None)
        if content == '':
            content = None
        image = data.get('iamge',None)
        if content is None and image is None:
            raise serializers.ValidationError('Make sure one field is filled')
        return data


### 
# class CustomSerializer(serializers.Serializer):
#     content = serializers.CharField()
#     email   = serializers.CharField()