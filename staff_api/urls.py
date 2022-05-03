from django import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from staff_api import views



router = DefaultRouter()
router.register('profile',views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),

]