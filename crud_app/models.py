from django.db import models

# Create your models here.
from django.conf import settings


def upload_update_image(instance,filename):
    return 'updated/{user}/{filename}'.format(user=instance.user,filename=filename)


class UpdateImage(models.Model):
    user    =   models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content =   models.TextField(blank=True,null=True)
    image   =   models.ImageField(upload_to=upload_update_image,blank=True,null=True)
    updated     = models.DateField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content or ""