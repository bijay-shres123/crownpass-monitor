from django import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from regions_api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('regions',views.RegionViewset)

urlpatterns = [
    path('', include(router.urls)),
    
]