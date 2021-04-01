from rest_framework import serializers
from .models import Sprint,Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source ='get_full_name', read_only=True)
    class Meta:
        model = User
        fields = ('id',User.USERNAME_FIELD,'full_name','is_active')


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ['id','name','description','endtime']
        


#creating custom mixins with DRF
class TaskSerializer(serializers.ModelSerializer):

    assigned = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD,read_only=True)


    status_display = serializers.SerializerMethodField('get_status_display')
    class Meta:
        model = Task
        fields = ['id','name','description','sprint','status_display','status','order','assigned','started','due','completed']

    def get_status_display(self,obj):
        return obj.get_status_display()