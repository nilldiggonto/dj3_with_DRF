from django.db import models
from django.core.serializers import serialize

# Create your models here.
from django.conf import settings
import json


def upload_update_image(instance,filename):
    return 'updated/{user}/{filename}'.format(user=instance.user,filename=filename)

class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        qs=self
        ##
        final_array = []
        for obj in qs:
            stuct = json.loads(obj.serialize())
            final_array.append(stuct)
        return json.dumps(final_array)
        # return serialize('json',qs,fields=('user','content','image'))
class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model,using=self._db)



class UpdateImage(models.Model):
    user    =   models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content =   models.TextField(blank=True,null=True)
    image   =   models.ImageField(upload_to=upload_update_image,blank=True,null=True)
    updated     = models.DateField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    def serialize(self):

        json_data = serialize('json',[self],fields=('user','content','image'))
        stuct = json.loads(json_data)
        # return 
        data = json.dumps(stuct[0]['fields'])
        return data