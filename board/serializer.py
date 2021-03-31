from rest_framework import serializers
from .models import Sprint

class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ['id','name','description','endtime']
        


#creating custom mixins with DRF
class DefaultMixins(object):
    pass