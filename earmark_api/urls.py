from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ API routes grouped under version 1
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/properties/', include('properties.urls')),
    path('api/v1/blog/', include('blog.urls')),
    path('api/v1/contact/', include('contact.urls')),

    # ✅ JWT authentication routes
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
