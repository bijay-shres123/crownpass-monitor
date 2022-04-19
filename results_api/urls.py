from django import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from results_api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('results',views.ResultsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]