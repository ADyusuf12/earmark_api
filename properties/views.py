from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from .models import Property
from .serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        user_groups = user.groups.values_list('name', flat=True)

        if not any(group in ['Agent', 'Developer', 'Owner'] for group in user_groups):
            raise PermissionDenied("Only agents, developers, or owners can create listings.")

        profile = user.userprofile
        serializer.save(owner_profile=profile)
