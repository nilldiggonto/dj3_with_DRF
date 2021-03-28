from django.contrib import admin

# Register your models here.
from .models import UpdateImage

@admin.register(UpdateImage)
class UpdateImageAdmin(admin.ModelAdmin):
    list_display = ['user','content','updated','timestamp']