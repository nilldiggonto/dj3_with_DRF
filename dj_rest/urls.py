  
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from rest_framework.authtoken.views import obtain_auth_token

from board.urls import router

# from rest_framework import routers

# router = routers.SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/token/',obtain_auth_token,name='api-token'),
    path('api/',include('crud_app.urls')),
    path('drf/',include('rest_app.urls')),
    path('board/',include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)