from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet

router = DefaultRouter()
router.register(r'', PropertyViewSet, basename='properties')

urlpatterns = router.urls
