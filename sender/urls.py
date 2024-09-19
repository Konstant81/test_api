from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet , SendViewSet, MessageViewSet


router = DefaultRouter()
router.register(r'client', ClientViewSet)
router.register(r'send', SendViewSet)
router.register(r'message', MessageViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('drf-auth/', include('rest_framework.urls')),
    re_path(r'^auth/', include('djoser.urls')),
    
]
