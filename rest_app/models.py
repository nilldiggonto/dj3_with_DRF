from django.db import models
from django.conf import settings

# Create your models here.

def upload_status_image(instance,filename):
    return 'updated/{user}/{filename}'.format(user=instance.user,filename=filename)

class StatusQuerySet(models.QuerySet):
    pass

class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model,using=self._db)
class Status(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content     = models.TextField(null=True,blank=True)
    image       = models.ImageField(upload_to=upload_status_image,null=True,blank=True)
    updated     = models.DateTimeField(auto_now=True,null=True,blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = StatusManager()

    def __str__(self):
        return str(self.content)[:20]

    # class Meta:
    #     verb
    @property
    def owner(self):
        return self.user