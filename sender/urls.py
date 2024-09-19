from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet #, SendViewSet, MessageViewSet


router = DefaultRouter()
router.register(r'client', ClientViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    
]
