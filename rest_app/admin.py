from django.contrib import admin
from .models import Status
# Register your models here.
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display=['user','content','timestamp','updated']