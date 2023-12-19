

from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from core.api.viewsets import Pontosturistico_Viewsets


router = routers.DefaultRouter() 
router.register(r'pontoturistico',Pontosturistico_Viewsets)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]
