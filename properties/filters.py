import django_filters
from .models import Property

class PropertyFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    is_featured = django_filters.BooleanFilter(field_name='is_featured')
    
    class Meta:
        model = Property
        fields = ['location', 'listing_type', 'category', 'min_price', 'max_price', 'is_featured']
