from rest_framework import serializers
from .models import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['user','content','image']

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