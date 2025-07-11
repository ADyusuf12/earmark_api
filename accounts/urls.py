from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, InterestViewSet, RegisterUserAPIView

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet, basename='profiles')
router.register(r'interests', InterestViewSet, basename='interests')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterUserAPIView.as_view(), name='register'),
]
