from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Sprint(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True,blank=True)
    endtime = models.DateField(unique=True)

    def __str__(self):
        return self.name



class Task(models.Model):
    STATUS_TODO =1
    STATUS_IN_PROGRESS =2
    STATUS_TESTING =3
    STATUS_DONE = 4

    STATUS_CHOICES = (
        (STATUS_TODO,('Not Started')),
        (STATUS_IN_PROGRESS,('In progress')),
        (STATUS_TESTING,('Testing')),
        (STATUS_DONE,('Done'))
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    sprint = models.ForeignKey(Sprint,null=True,blank=True,on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=STATUS_CHOICES,default=STATUS_TODO)
    order = models.SmallIntegerField(default=0)
    assigned = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    started = models.DateField(blank=True,null=True)
    due     = models.DateField(blank=True,null=True)
    completed = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.name

