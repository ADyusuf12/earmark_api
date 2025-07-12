from rest_framework import viewsets, permissions, status, filters
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PropertyFilter


from .models import Property
from .serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all().order_by('-date_posted')
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PropertyFilter
    search_fields = ['title', 'description', 'location',]
    ordering_fields = ['date_posted', 'price', 'view_count', 'title']

    def perform_create(self, serializer):
        user = self.request.user
        user_groups = user.groups.values_list('name', flat=True)

        if not any(group in ['Agent', 'Developer', 'Owner'] for group in user_groups):
            raise PermissionDenied("Only agents, developers, or owners can create listings.")

        profile = user.userprofile
        serializer.save(owner_profile=profile)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save(update_fields=['view_count'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
